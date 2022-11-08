# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:12

from client.page.func.alertBox import BeAlertBox
from time import sleep
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.func.chooseDir import choose_ftp_dir
from .crawlerElement import crawler_element
from service.lib.tools.updateData import update_dict
from client.page.func.upload import upload
from client.app.VisualModeler.process.node.oprt.rightOpt import OptTreeServer
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_text_enable_var
from client.page.func.regular import RegularCube
from client.page.func.pagination import Pagination
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def crawler_business(node_name, system_name, element_config, tree_set, advance_set):
    """
    :param node_name: 节点名称
    :param system_name: 目标系统
    :param element_config: 元素配置，数组
    :param tree_set: 操作树，数组
    :param advance_set: 高级配置，字典

    # 操作: 引用crawler_step_set集合里的步骤
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "可视化操作模拟节点",
            "节点名称": "可视化操作模拟节点",
            "业务配置": {
                "节点名称": "可视化操作模拟节点1",
                "目标系统": "aisee_3.0不登录",
                "元素配置": [
                    {
                        "action": "点击按钮"
                    },
                    {
                        "action": "输入框输入",
                        "值输入": "清明时节雨纷纷"
                    },
                    {
                        "action": "表格取数",
                        "元素标识": "//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]/table[@class='datagrid-btable']",
                        "下一页元素标识": "//*[@id='tb']/following-sibling::div[2]//span[@class='l-btn-icon pagination-next']",
                        "状态": "关闭"
                    },
                    {
                        "action": "附件上传-远程加载-本地",
                        "目录": "OCR",
                        "文件名": "122",
                        "文件类型": "jpg"
                    },
                    {
                        "action": "文件下载"
                    },
                    {
                        "action": "跳转iframe"
                    },
                    {
                        "action": "休眠",
                        "循环次数": "1",
                        "休眠时间": "3",
                        "刷新页面": "否"
                    }
                ]
            }
        }
    }

    # 设置操作树的步骤
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "可视化操作模拟节点",
            "节点名称": "可视化操作模拟节点",
            "业务配置": {
                "节点名称": "可视化操作模拟节点1",
                "目标系统": "aisee_3.0不登录",
                "操作树": [
                    {
                        "对象": "操作",
                        "右键操作": "添加步骤",
                        "元素名称": "休眠,点击按钮,表格取数"
                    },
                    {
                        "对象": "操作",
                        "右键操作": "添加条件",
                        "条件配置": {
                            "if": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ],
                            "else": "是"
                        }
                    },
                    {
                        "对象": "操作",
                        "右键操作": "添加循环",
                        "循环配置": {
                            "循环类型": "变量列表",
                            "变量选择": "名字",
                            "循环行变量名称": "loop_a",
                            "赋值方式": "替换",
                        }
                    },
                    {
                        "对象": "休眠",
                        "右键操作": "删除"
                    }
                ]
            }
        }
    }

    """
    browser = get_global_var("browser")
    page_wait()
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
    sleep(1)

    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 选择目标系统
    if system_name:
        browser.find_element(By.XPATH, "//*[@name='platformId']/preceding-sibling::input").click()
        system_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'platformId') and text()='{0}']".format(system_name))
        browser.execute_script("arguments[0].scrollIntoView(true);", system_element)
        system_element.click()
        log.info("选择目标系统: {0}".format(system_name))
        sleep(1)

        # 选择目标系统后，需要先保存业务配置
        browser.find_element(By.XPATH, "//*[@onclick='saveFetchContent(true)']//*[text()='保存']").click()
        log.info("保存业务配置")

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存业务配置成功")
        else:
            log.warning("保存业务配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

        # 切换到节点iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/crawlerNode.html?')]"))
        # 切换到业务配置iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))

    # 元素配置
    if element_config:
        element_operate_result = config_element(elements=element_config)
        if element_operate_result:
            pass
        else:
            return

    # 设置高级模式
    if advance_set:
        if advance_set.get("状态") == "开启":
            timeout = advance_set.get("超时时间")
            retry_times = advance_set.get("超时重试次数")
            try:
                enable_click = browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                enable_click.click()
                log.info("开启【高级配置】")
            except NoSuchElementException:
                pass

            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").send_keys(timeout)
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").send_keys(retry_times)
            log.info("设置高级模式")
            sleep(1)
        else:
            try:
                browser.find_element(By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                disable_click = browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='关闭高级模式']")
                disable_click.click()
                log.info("关闭【高级配置】")

    # 操作树配置
    if tree_set:
        tree = OptTreeServer(location=2)
        for tree_step in tree_set:
            # 右键操作节点
            r_click_obj = tree_step.get("对象")
            r_opt = tree_step.get("右键操作")
            tree.r_click_opt(obj=r_click_obj, opt=r_opt)

            # 选择右键操作
            r_opt = tree_step.get("右键操作")
            if r_opt == "添加条件":
                if_set = tree_step.get("条件配置")
                if if_set.get("else") == "是":
                    enable_else_flag = True
                else:
                    enable_else_flag = False
                result = tree.add_if(if_array=if_set.get("if"), enable_else=enable_else_flag)

            elif r_opt == "添加循环":
                loop_set = tree_step.get("循环配置")
                result = tree.add_loop(where=1, loop_type=loop_set.get("循环类型"), loop_info=tree_step.get("循环配置"))

            elif r_opt == "添加步骤":
                result = tree.add_step(steps=tree_step.get("元素名称"))

            elif r_opt == "删除":
                result = tree.delete()

            else:
                raise KeyError("不支持的右键操作: {0}".format(r_opt))

            if not result:
                return

    # 获取节点名称
    node_name = browser.find_element(
        By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    save_elements = browser.find_elements(By.XPATH, "//*[@onclick='saveFetchContent(true)']//*[text()='保存']")
    for element in save_elements:
        if element.is_displayed():
            element.click()
            log.info("保存业务配置")
            break

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("操作成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    set_global_var("ResultMsg", msg, False)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name


def config_element(elements):
    """
    元素操作入口，包含元素是新增修改删除等，以及元素各项配置信息
    首先加载元素默认配置信息，在此基础上进行参数调整

    :param elements: 元素配置，数组
    """
    log.info("开始配置元素")
    rows = len(elements)
    log.info("需要配置{0}个元素".format(rows))
    for element_param in elements:
        # 根据action找到预置的步骤参数
        action = element_param.get("action")
        if action:
            # 加载元素配置默认参数
            original_param = crawler_element.get(action)
            # element_param删除key=action的值，其他输入值均表示需要替换默认参数
            if original_param:
                element_param.pop("action")
                # 根据输入依次替换默认参数值
                final_param = original_param
                for _key, _value in element_param.items():
                    # replace_dict_value会返回对输入数据替换后的值
                    final_param = update_dict(obj=original_param, key=_key, value=_value)
                    original_param = final_param
                # 如果传参有修改参数值，则替换original_param
                log.info("元素参数值: \n{0}".format(json.dumps(final_param, indent=4, ensure_ascii=False)))
                if final_param.__contains__("操作类型"):
                    action_type = final_param.get("操作类型")
                else:
                    action_type = "添加"
                element_config_result = element_list(action_type, final_param)
                sleep(1)
            else:
                raise KeyError("参数填写错误，无法找到action")
        else:
            # 使用元素全新配置
            log.info("元素参数值: \n{0}".format(json.dumps(element_param, indent=4, ensure_ascii=False)))
            if element_param.__contains__("操作类型"):
                action_type = element_param.get("操作类型")
            else:
                action_type = "添加"
            element_config_result = element_list(action_type, element_param)
            sleep(1)

        if not element_config_result:
            return False
    return True


def element_list(actionType, element):
    """
    元素增加、修改、删除、复制操作
    :param actionType: 操作类型，添加/修改/删除/复制
    :param element: 元素信息，字典
    """
    browser = get_global_var("browser")
    # 跳转iframe操作元素添加、修改、删除、复制按钮
    wait = WebDriverWait(browser, 30)
    wait.until(ec.frame_to_be_available_and_switch_to_it((
        By.XPATH, "//iframe[contains(@src,'crawlerStepsList.html?')]")))
    page_wait()
    wait = WebDriverWait(browser, 30)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text()='操作列表']")))
    sleep(1)

    if actionType == "添加":
        log.info("开始添加元素: {0}".format(element.get("元素名称")))
        # 点击添加按钮
        add_elements = browser.find_elements(By.XPATH, "//*[@id='addBtn']//*[text()='添加']")
        for e in add_elements:
            if e.is_displayed():
                e.click()
                sleep(2)
                break
        result = element_set(**element)

    elif actionType == "修改":
        obj = element.get("目标元素")
        log.info("开始修改元素: {0}".format(obj))
        try:
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(obj)).click()
        except NoSuchElementException:
            table_xpath = "//*[@id='query_steps_tb']/following-sibling::div[2]/table"
            page = Pagination(table_xpath)
            page.set_page_size(50)
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(obj)).click()
        finally:
            # 点击修改按钮
            edit_elements = browser.find_elements(By.XPATH, "//*[@id='editBtn']//*[text()='修改']")
            for e in edit_elements:
                if e.is_displayed():
                    e.click()
                    sleep(2)
                    break
            result = element_set(**element)

    elif actionType == "删除":
        obj = element.get("目标元素")
        log.info("开始删除元素: {0}".format(obj))
        try:
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(obj)).click()
        except NoSuchElementException:
            table_xpath = "//*[@id='query_steps_tb']/following-sibling::div[2]/table"
            page = Pagination(table_xpath)
            page.set_page_size(50)
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(obj)).click()
        finally:
            # 点击删除按钮
            edit_elements = browser.find_elements(By.XPATH, "//*[@id='delBtn']//*[text()='删除']")
            for e in edit_elements:
                if e.is_displayed():
                    e.click()
                    break
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains(obj, auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("删除成功"):
                    log.info("元素 {0} 删除成功".format(obj))
                    # 切换到节点配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))

                    result = True
                else:
                    log.warning("元素 {0} 删除失败，失败提示: {1}".format(obj, msg))
                    result = False
            else:
                log.warning("元素 {0} 删除失败，失败提示: {1}".format(obj, msg))
                result = False
            set_global_var("ResultMsg", msg, False)

    elif actionType == "复制":
        log.info("开始复制元素: {0}".format(element.get("元素名称")))
        # 点击复制按钮
        browser.find_element(By.XPATH, "//*[@id='copyBtn']//*[text()='复制']").click()
        # 等待页面加载
        wait = WebDriverWait(browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'crawlerCopySteps.html?')]")))
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='elementName']/preceding-sibling::input")))
        page_wait()

        # 选择节点名称
        browser.find_element(By.XPATH, "//*[@id='nodeId']/following-sibling::span//a").click()
        node_name = element.get("节点名称")
        browser.find_element(By.XPATH, "//*[contains(@id,'nodeId') and text()='{0}']".format(node_name)).click()
        log.info("选择节点: {0}".format(node_name))
        # 查询复制元素
        copy_element = element.get("复制元素")
        browser.find_element(By.XPATH, "//*[@name='elementName']/preceding-sibling::input").send_keys(copy_element)
        browser.find_element(By.XPATH, "//*[@id='btn']//span[text()='查询']").click()
        sleep(1)
        page_wait()
        # 选择复制元素
        try:
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(copy_element)).click()
        except NoSuchElementException:
            table_xpath = "//*[@id='tb']/following-sibling::div[2]/table"
            page = Pagination(table_xpath)
            page.set_page_size(50)
            browser.find_element(By.XPATH, "//*[@field='elementName']//*[text()='{0}']".format(copy_element)).click()
        finally:
            add_copy_button = browser.find_elements(By.XPATH, "//*[@id='addBtn']//span[text()='添加']")
            for e in add_copy_button:
                if e.is_displayed():
                    e.click()
                    sleep(1)
                    break
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerCopyStepRename.html')]"))
            if element.__contains__("元素名称"):
                element_name = element.get("元素名称")
                element_name_input = browser.find_elements(
                    By.XPATH, "//*[@id='elementName']/following-sibling::span/input[1]")
                for e in element_name_input:
                    if e.is_displayed():
                        e.clear()
                        e.send_keys(element_name)
                        break
                sleep(1)
            browser.find_element(By.XPATH, "//*[@id='crawlerStep-copy']//span[text()='确认']").click()

            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("元素 {0} 复制成功".format(copy_element))
                result = True
            else:
                log.warning("元素 {0} 复制失败，失败提示: {1}".format(copy_element, msg))
                result = False
            set_global_var("ResultMsg", msg, False)
            # 切换到节点iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/crawlerNode.html?')]"))
            # 切换到业务配置iframe
            browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))

    else:
        result = False

    return result


def element_set(**kwargs):
    """
    元素具体配置
    :param kwargs: 元素信息
    :return:
    """
    browser = get_global_var("browser")

    # 等待页面加载
    page_wait()

    # 进入元素添加配置页面
    wait = WebDriverWait(browser, 30)
    wait.until(ec.frame_to_be_available_and_switch_to_it((
        By.XPATH, "//iframe[contains(@src,'crawlerStepsEdit.html')]")))
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='elementName']/preceding-sibling::input")))
    sleep(1)

    # 元素名称
    if kwargs.__contains__("元素名称"):
        element_name = kwargs.get("元素名称")
        browser.find_element(By.XPATH, "//*[@name='elementName']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='elementName']/preceding-sibling::input").send_keys(element_name)
        log.info("设置 元素名称: {0}".format(element_name))
        sleep(1)

    # 元素类型
    if kwargs.__contains__("元素类型"):
        element_type = kwargs.get("元素类型")
        browser.find_element(By.XPATH, "//*[@name='types']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'types') and text()='{0}']".format(element_type)).click()
        log.info("设置 元素类型: {0}".format(element_type))
        sleep(1)

    # 动作
    if kwargs.__contains__("动作"):
        element_action = kwargs.get("动作")
        browser.find_element(By.XPATH, "//*[@name='action']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'elementaction') and text()='{0}']".format(element_action)).click()
        log.info("设置 动作: {0}".format(element_action))
        sleep(1)

    # 标识类型
    if kwargs.__contains__("标识类型"):
        element_label_type = kwargs.get("标识类型")
        browser.find_element(By.XPATH, "//*[@name='labelType']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'labelType') and text()='{0}']".format(element_label_type)).click()
        log.info("设置 标识类型: {0}".format(element_label_type))
        sleep(1)

    # 元素标识
    if kwargs.__contains__("元素标识"):
        ele_label = kwargs.get("元素标识")
        input_xpath = "//*[@id='elementLabel']/following-sibling::span/input[1]"
        browser.find_element(By.XPATH, input_xpath).clear()
        set_text_enable_var(input_xpath=input_xpath, msg=ele_label)
        log.info("设置 元素标识: {0}".format(ele_label))
        sleep(1)

    # 等待元素标识
    if kwargs.__contains__("等待元素标识"):
        wait_ele_label = kwargs.get("等待元素标识")
        input_xpath = "//*[@ID='waitElementLabel']/following-sibling::span/input[1]"
        browser.find_element(By.XPATH, input_xpath).clear()
        set_text_enable_var(input_xpath=input_xpath, msg=wait_ele_label)
        log.info("设置 等待元素标识: {0}".format(wait_ele_label))
        sleep(1)

    # 等待元素标识类型
    if kwargs.__contains__("等待元素标识类型"):
        wait_element_label_type = kwargs.get("等待元素标识类型")
        browser.find_element(By.XPATH, "//*[@name='wait_labelType']/preceding-sibling::input").click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'wait_labelType') and text()='{0}']".format(wait_element_label_type)).click()
        log.info("设置 等待元素标识类型: {0}".format(wait_element_label_type))
        sleep(1)

    # 最大等待时间
    if kwargs.__contains__("最大等待时间"):
        max_time = kwargs.get("最大等待时间")
        browser.find_element(By.XPATH, "//*[@ID='maxTime']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@ID='maxTime']/following-sibling::span/input[1]").send_keys(max_time)
        log.info("设置 最大等待时间: {0}".format(max_time))
        sleep(1)

    # 变量名
    if kwargs.__contains__("变量名"):
        var_name = kwargs.get("变量名")
        browser.find_element(By.XPATH, "//*[@ID='varName']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@ID='varName']/following-sibling::span/input[1]").send_keys(var_name)
        log.info("设置 变量名: {0}".format(var_name))
        sleep(1)

    # 描述
    if kwargs.__contains__("描述"):
        element_desc = kwargs.get("描述")
        browser.find_element(By.XPATH, "//*[@name='elementDesc']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='elementDesc']/preceding-sibling::input").send_keys(element_desc)
        log.info("设置 描述: {0}".format(element_desc))
        sleep(1)

    # 取数模式
    if kwargs.__contains__("取数模式"):
        access_mode = kwargs.get("取数模式")
        browser.find_element(By.XPATH, "//*[@name='accessMode']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'accessMode') and text()='{0}']".format(access_mode)).click()
        log.info("设置 取数模式: {0}".format(access_mode))
        sleep(1)

    # 值输入
    if kwargs.__contains__("值输入"):
        element_input = kwargs.get("值输入")
        input_xpath = "//*[@id='elecontent']/following-sibling::span/input[1]"
        browser.find_element(By.XPATH, input_xpath).clear()
        set_text_enable_var(input_xpath=input_xpath, msg=element_input)
        log.info("设置 值输入: {0}".format(element_input))
        sleep(1)

    # 敏感信息
    if kwargs.__contains__("敏感信息"):
        is_sensitive = kwargs.get("敏感信息")
        if is_sensitive == "是":
            browser.find_element(By.XPATH, "//*[@id='is_sensitive']/following-sibling::label").click()
            log.info("勾选 敏感信息")
            sleep(1)

    # 下一页元素标识
    if kwargs.__contains__("下一页元素标识"):
        next_ele_label = kwargs.get("下一页元素标识")
        browser.find_element(By.XPATH, "//*[@id='nextElementLabel']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='nextElementLabel']/following-sibling::span/input[1]").send_keys(
            next_ele_label)
        log.info("设置 下一页元素标识: {0}".format(next_ele_label))
        sleep(1)

    # 下一页标识类型
    if kwargs.__contains__("下一页标识类型"):
        next_label_type = kwargs.get("下一页标识类型")
        browser.find_element(By.XPATH, "//*[@name='nextLabelType']/preceding-sibling::input").click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'nextLabelType') and text()='{0}']".format(next_label_type)).click()
        log.info("设置 下一页标识类型: {0}".format(next_label_type))
        sleep(1)

    # 休眠时间
    if kwargs.__contains__("休眠时间"):
        sleep_times = kwargs.get("休眠时间")
        browser.find_element(By.XPATH, "//*[@name='sleepTimes']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='sleepTimes']/preceding-sibling::input").send_keys(sleep_times)
        log.info("设置 休眠时间: {0}".format(sleep_times))
        sleep(1)

    # 表格页数
    if kwargs.__contains__("表格页数"):
        page_count = kwargs.get("表格页数")
        browser.find_element(By.XPATH, "//*[@id='pageCount']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='pageCount']/following-sibling::span/input[1]").send_keys(page_count)
        log.info("设置 表格页数: {0}".format(page_count))
        sleep(1)

    # 是否配置期待值
    if kwargs.__contains__("是否配置期待值"):
        expected_msg = kwargs.get("是否配置期待值")
        if expected_msg.get("状态") == "开启":
            browser.find_element(By.XPATH, "//*[@id='is_expected']/following-sibling::label").click()
            log.info("勾选 是否配置期待值")
            focus = browser.find_element(By.XPATH, "//*[@name='expectedvalue']/preceding-sibling::input")
            browser.execute_script("arguments[0].scrollIntoView(true);", focus)
            sleep(1)

            # 期待值
            if expected_msg.__contains__("期待值"):
                expected_value = expected_msg.get("期待值")
                browser.find_element(By.XPATH, "//*[@name='expectedvalue']/preceding-sibling::input").clear()
                input_xpath = "//*[@name='expectedvalue']/preceding-sibling::input"
                set_text_enable_var(input_xpath=input_xpath, msg=expected_value)
                log.info("设置 期待值: {0}".format(expected_value))
                sleep(1)

            # 尝试次数
            if expected_msg.__contains__("尝试次数"):
                try_time = expected_msg.get("尝试次数")
                browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").clear()
                browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").send_keys(try_time)
                log.info("设置 尝试次数: {0}".format(try_time))
                sleep(1)

            # 等待时间
            if expected_msg.__contains__("等待时间"):
                wait_time = expected_msg.get("等待时间")
                browser.find_element(By.XPATH, "//*[@name='waitTime']/preceding-sibling::input").clear()
                browser.find_element(By.XPATH, "//*[@name='waitTime']/preceding-sibling::input").send_keys(wait_time)
                log.info("设置 等待时间: {0}".format(wait_time))
                sleep(1)

    # 循环次数
    if kwargs.__contains__("循环次数"):
        loop_num = kwargs.get("循环次数")
        browser.find_element(By.XPATH, "//*[@name='loopNum']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='loopNum']/preceding-sibling::input").send_keys(loop_num)
        log.info("设置 循环次数: {0}".format(loop_num))
        sleep(1)

    # 休眠动作休眠时间
    if kwargs.__contains__("_休眠时间"):
        _sleep = kwargs.get("_休眠时间")
        browser.find_element(By.XPATH, "//*[@name='sleep']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='sleep']/preceding-sibling::input").send_keys(_sleep)
        log.info("设置 休眠动作休眠时间: {0}".format(_sleep))
        sleep(1)

    # 刷新页面
    if kwargs.__contains__("刷新页面"):
        refresh = kwargs.get("刷新页面")
        js = 'return $("#is_fresh")[0].checked;'
        status = browser.execute_script(js)
        refresh_element = browser.find_element(By.XPATH, "//*[@for='is_fresh']")
        tmp = True if refresh == "是" else False
        if tmp ^ status:
            refresh_element.click()
        log.info("设置 刷新页面: {0}".format(refresh))

    # 附件
    if kwargs.__contains__("附件"):
        attach_msg = kwargs.get("附件")

        # 附件来源
        if attach_msg.__contains__("附件来源"):
            attach_source = attach_msg.get("附件来源")
            browser.find_element(By.XPATH, "//*[text()='{0}']".format(attach_source)).click()
            log.info("设置 附件来源: {0}".format(attach_source))
            sleep(1)

            if attach_source == "动态生成":
                # 附件标题
                if attach_msg.__contains__("附件标题"):
                    attach_title = attach_msg.get("附件标题")
                    patt = r'.*\$\{.+\}.*'
                    match_obj = re.match(patt, attach_title)
                    if match_obj:
                        input_xpath = "//*[@id='attachTitle']/following-sibling::span[1]/input[1]"
                        set_text_enable_var(input_xpath=input_xpath, msg=attach_title)
                    else:
                        browser.find_element(
                            By.XPATH, "//*[@name='attachTitle']/preceding-sibling::input").send_keys(attach_title)
                    log.info("设置 附件标题: {0}".format(attach_title))
                    sleep(1)

                # 附件内容
                if attach_msg.__contains__("附件内容"):
                    attach_content = attach_msg.get("附件内容")
                    patt = r'.*\$\{.+\}.*'
                    match_obj = re.match(patt, attach_content)
                    if match_obj:
                        input_xpath = "//*[@id='addAttachContent']/following-sibling::span[1]/input[1]"
                        set_text_enable_var(input_xpath=input_xpath, msg=attach_content)
                    else:
                        browser.find_element(
                            By.XPATH, "//*[@name='addAttachContent']/preceding-sibling::input").send_keys(attach_content)
                    log.info("设置 附件内容: {0}".format(attach_content))
                    sleep(1)

                # 附件类型
                if attach_msg.__contains__("附件类型"):
                    attach_type = attach_msg.get("附件类型")
                    browser.find_element(By.XPATH, "//*[@name='attachType']/preceding-sibling::input").click()
                    browser.find_element(
                        By.XPATH, "//*[contains(@id,'attachType') and text()='{0}']".format(attach_type)).click()
                    log.info("设置 附件类型: {0}".format(attach_type))
                    sleep(1)

            elif attach_source == "本地上传":
                file_name = attach_msg.get("附件名称")
                # 调用上传文件方法
                upload(file_name=file_name)
                log.info("上传 本地文件: {0}".format(file_name))
                sleep(1)

            else:
                # 远程加载
                attach_remote_set(storage_type=attach_msg.get("存储类型"), ftp=attach_msg.get("远程服务器"),
                                  dir_name=attach_msg.get("目录"), use_var=attach_msg.get("变量引用"),
                                  choose_type=attach_msg.get("文件过滤方式"), file_name=attach_msg.get("文件名"),
                                  file_type=attach_msg.get("文件类型"))

    # 下载目录
    if kwargs.__contains__("下载目录"):
        path = kwargs.get("下载目录")
        browser.find_element(By.XPATH, "//*[@id='eledownloadtr']//input[1]").click()
        try:
            path_element = browser.find_element(
                By.XPATH, "//*[contains(@id,'_easyui_tree_')]//*[text()='{0}']".format(path))
            browser.execute_script("arguments[0].scrollIntoView(true);", path_element)
            path_element.click()
            log.info("设置 下载目录: {0}".format(path))
            sleep(1)
        except NoSuchElementException:
            raise

    # 重复步骤
    if kwargs.__contains__("重复步骤"):
        repeat_step = kwargs.get("重复步骤")
        browser.find_element(By.XPATH, "//*[@id='repeat_step']/following-sibling::span[1]//a").click()
        page_wait()

        # 切换到选择重复步骤iframe
        wait = WebDriverWait(browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'fetchStepList.html')]")))
        # browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'fetchStepList.html')]"))
        sleep(1)

        # 根据元素名称选择
        table_xpath = "//*[@id='getdata_fetch_bar']/following-sibling::div[2]/table"
        page = Pagination(table_xpath)
        for s in repeat_step:
            try:
                browser.find_element(By.XPATH, "//*[contains(@id,'getdata_fetch')]//*[text()='{0}']".format(s)).click()
                sleep(1)
            except NoSuchElementException:
                page.set_page_size("50")
                browser.find_element(By.XPATH, "//*[contains(@id,'getdata_fetch')]//*[text()='{0}']".format(s)).click()
                sleep(1)
            finally:
                # 添加到右边已选择
                browser.find_element(By.XPATH, "//*[@id='toRight']").click()

                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("选择重复步骤: {0} 成功".format(s))
                else:
                    log.warning("选择重复步骤失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)

                # 切换到节点iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/crawlerNode.html?')]"))
                # 切换到业务配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))
                # 切换到添加元素iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerStepsList.html?')]"))
                # 切换到选择重复步骤iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerStepsEdit.html?')]"))
                # 切换到选择重复步骤列表iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'fetchStepList.html')]"))

        # 关闭选择重复步骤页面
        browser.switch_to.parent_frame()
        browser.find_element(By.XPATH, "//*[text()='操作步骤检索页面']/following-sibling::div[1]/a[2]").click()
        sleep(1)

    # 保存元素
    browser.find_element(By.XPATH, "//*[@onclick='saveFetchElementContents()']//*[text()='保存']").click()

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("保存成功"):
        log.info("元素操作成功")
        result = True
    else:
        log.warning("元素操作失败，失败提示: {0}".format(msg))
        result = False
    set_global_var("ResultMsg", msg, False)

    if result:
        # 切换到节点iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/crawlerNode.html?')]"))
        # 切换到业务配置iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))
    return result


def attach_remote_set(storage_type, ftp, dir_name, use_var, choose_type, file_name, file_type):
    """
    :param storage_type: 存储类型
    :param ftp: 远程服务器
    :param dir_name: 目录
    :param use_var: 变量引用
    :param choose_type: 文件过滤方式
    :param file_name: 文件名，关键字或正则（字典）
    :param file_type: 文件类型
    """
    browser = get_global_var("browser")
    # 存储类型
    if storage_type:
        browser.find_element(By.XPATH, "//*[text()='{0}']".format(storage_type)).click()
        log.info("勾选 存储类型: {0}".format(storage_type))
        sleep(1)

    # 获取当前存储类型
    js = 'return $("#remote_local")[0].checked;'
    choose_status = browser.execute_script(js)
    if choose_status:
        choose_storage = "本地"
    else:
        choose_storage = "远程"
    log.info("当前存储类型: {0}".format(choose_storage))

    if choose_storage == "本地":

        # 变量引用
        js = 'return $("#local_isKeyword")[0].checked;'
        status = browser.execute_script(js)
        log.info("目标【变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = browser.find_element(By.XPATH, "//*[@for='local_isKeyword']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if use_var == "是":
            # 点击变量引用
            if not status:
                enable_click.click()
            log.info("勾选目标【变量引用】")

            if dir_name:
                input_xpath = "//*[@name='local_keyword']/preceding-sibling::input"
                browser.find_element(By.XPATH, input_xpath).clear()
                set_text_enable_var(input_xpath=input_xpath, msg=dir_name)
        else:
            if status:
                enable_click.click()
            log.info("取消勾选【变量引用】")

            # 目录
            if dir_name:
                browser.find_element(By.XPATH, "//*[@id='local_choose_span']//input[1]").click()
                try:
                    path_element = browser.find_element(
                        By.XPATH, "//*[contains(@id,'_easyui_tree_')]//*[text()='{0}']".format(dir_name))
                    browser.execute_script("arguments[0].scrollIntoView(true);", path_element)
                    path_element.click()
                    log.info("设置 目录: {0}".format(dir_name))
                    sleep(1)
                except NoSuchElementException:
                    raise Exception("找不到指定目录: {0}".format(dir_name))

    else:
        # 远程服务器
        if ftp:
            browser.find_element(By.XPATH, "//*[@name='srcServerId']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'remote_srcServerId') and text()='{0}']".format(ftp)).click()
            log.info("设置 远程服务器: {0}".format(ftp))
            sleep(1)

            # ftp目录
            if dir_name:
                browser.find_element(By.XPATH, "//*[@id='remote_choose_span']//input[1]").click()
                choose_ftp_dir(path=dir_name)
                log.info("设置 目录: {0}".format(dir_name))
                sleep(1)

    # 文件过滤方式
    if choose_type:
        browser.find_element(By.XPATH, "//*[@id='fileFilterType1']/following-sibling::span[1]//input[1]").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileFilterType1') and text()='{0}']".format(choose_type)).click()
        log.info("设置 文件过滤方式: {0}".format(choose_type))
        sleep(1)

    # 先获取文件过滤类型
    choose = browser.find_element(By.XPATH, "//*[@id='fileFilterType1']/following-sibling::span[1]/input[2]")
    choose_type = choose.get_attribute("value")
    log.info("类型: {0}".format(choose_type))
    if choose_type == "0":
        choose_type = "关键字"
    elif choose_type == "1":
        choose_type = "正则匹配"
    log.info("当前文件过滤类型: {0}".format(choose_type))

    # 文件名
    if file_name:
        if choose_type == "关键字":
            input_xpath = "//*[@name='filepath1']/preceding-sibling::input"
            browser.find_element(By.XPATH, input_xpath).clear()
            set_text_enable_var(input_xpath=input_xpath, msg=file_name)
            log.info("设置 文件名: {0}".format(file_name))
            sleep(1)
        else:
            # 正则匹配
            browser.find_element(By.XPATH, "//*[@id='keyExpr2']/following-sibling::span[1]//a[1]").click()
            sleep(1)
            # 切换到正则配置iframe页面
            browser.switch_to.frame(
                browser.find_element(
                    By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]"))
            confirm_selector = "//*[@id='regexpPopUp']"
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=file_name.get("设置方式"), regular_name=file_name.get("正则模版名称"),
                                    advance_mode=file_name.get("高级模式"), regular=file_name.get("标签配置"),
                                    expression=file_name.get("表达式"), confirm_selector=confirm_selector)
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(
                        browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))
                    # 切换到元素列表iframe
                    browser.switch_to.frame(
                        browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerStepsList.html')]"))
                    # 切换到元素配置iframe
                    browser.switch_to.frame(
                        browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerStepsEdit.html')]"))
                    # 切换到正则配置iframe页面
                    browser.switch_to.frame(
                        browser.find_element(
                            By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                browser.switch_to.parent_frame()

            # 关闭确定
            browser.find_element(By.XPATH, "//*[@id='regexp-ok']//*[text()='确定']").click()
            browser.switch_to.parent_frame()

    # 文件类型
    if file_type:
        browser.find_element(By.XPATH, "//*[@name='fileType1']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileType1') and text()='{0}']".format(file_type)).click()
        log.info("设置 文件类型: {0}".format(file_type))
        sleep(1)
