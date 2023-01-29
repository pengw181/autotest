# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/10 上午10:41

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from client.page.func.alertBox import BeAlertBox
from client.page.func.processVar import choose_var
from client.page.func.input import set_textarea
from client.page.func.loadData import load_sample
from client.page.func.pageMaskWait import page_wait
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def report_business(node_name, opt_type, obj_var, var_name, var_map, interface_name, remark, sample_data):
    """
    :param node_name: 节点名称
    :param opt_type: 操作方式，添加/修改/删除
    :param obj_var: 变量名，操作方式为修改/删除时需要
    :param var_name: 变量选择
    :param var_map: 变量索引配置，字典
    :param interface_name: 数据接口名称
    :param remark: 备注
    :param sample_data: 样例数据

    # 添加
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试报表节点",
            "节点类型": "报表节点",
            "节点名称": "报表节点",
            "业务配置": {
                "节点名称": "报表节点",
                "操作方式": "添加",
                "变量选择": "时间",
                "变量索引配置": [
                    ["1", "", "字符", "", "X轴(维度)"],
                    ["2", "", "字符", "", "分组"],
                    ["3", "", "数字", "", "Y轴(度量)"]
                ],
                "数据接口名称": "",
                "备注": "",
                "样例数据": ""
            }
        }
    }

    # 修改
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试报表节点",
            "节点类型": "报表节点",
            "节点名称": "报表节点",
            "业务配置": {
                "节点名称": "报表节点",
                "操作方式": "修改",
                "变量名": "时间",
                "变量选择": "时间",
                "变量索引配置": [
                    ["1", "", "字符", "", "X轴(维度)"],
                    ["2", "", "字符", "", "分组"],
                    ["3", "", "数字", "", "Y轴(度量)"]
                ],
                "数据接口名称": "",
                "备注": "",
                "样例数据": ""
            }
        }
    }

    # 删除
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试报表节点",
            "节点类型": "报表节点",
            "节点名称": "报表节点",
            "业务配置": {
                "节点名称": "报表节点",
                "操作方式": "删除",
                "变量名": "时间"
            }
        }
    }
    """
    browser = get_global_var("browser")
    sleep(1)
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))

    # 操作方式
    if opt_type == "添加":
        # 点击添加按钮
        browser.find_element(By.XPATH, "//*[@onclick='toVarCfg()']//*[text()='添加']").click()
        # 切换到变量配置页面
        page_wait()
        wait = WebDriverWait(browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'reportNodeEdit.html')]")))
        sleep(1)
    elif opt_type == "修改":
        # 变量名
        if obj_var:
            # 双击变量进入修改页面
            obj = browser.find_element(By.XPATH, "//*[contains(@id,'tableVarCfg')]//*[text()='{0}']".format(obj_var))
            action = ActionChains(browser)
            action.double_click(obj).perform()
            # 切换到变量配置页面
            page_wait()
            wait = WebDriverWait(browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'reportNodeEdit.html')]")))
            sleep(1)
        else:
            raise KeyError("修改变量时，未指定变量名")
    elif opt_type == "删除":
        # 变量名
        if obj_var:
            browser.find_element(By.XPATH, "//*[contains(@id,'tableVarCfg')]//*[text()='{0}']".format(obj_var)).click()
            # 点击删除按钮
            browser.find_element(By.XPATH, "//*[@onclick='delVarCfg()']//*[text()='删除']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(obj_var), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                if not alert.exist_alert:
                    # 若未出现弹框，则表示删除操作成功
                    log.info("{0} 删除成功".format(obj_var))
                else:
                    msg = alert.get_msg()
                    log.warning("{0} 删除失败，失败提示: {1}".format(obj_var, msg))
            else:
                # 操作异常
                log.warning("{0} 删除失败，失败提示: {1}".format(obj_var, msg))
            set_global_var("ResultMsg", msg, False)
            return
        else:
            raise KeyError("删除变量时，未指定变量名")
    else:
        raise KeyError("操作方式 仅支持添加/修改/删除，当前值: {0}".format(opt_type))

    # 变量名称
    if var_name:
        wait = WebDriverWait(browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='dataH_inputVar2Name']/following-sibling::span//a")))
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVar2Name']/following-sibling::span//a").click()
        choose_var(var_name=var_name)
        log.info("选择变量: {0}".format(var_name))

    # 变量索引配置
    if var_map:
        # 判断是否已经配置了变量索引关系，如果存在则删除
        col_set_ele = browser.find_elements(
            By.XPATH, "//*[contains(@id,'tableVarCfg')]/*[@field='varIndex']//*[@class='col_item']")
        if len(col_set_ele) > 0:
            for element in col_set_ele:
                element.click()
                browser.find_element(By.XPATH, "//*[@onclick='deleteRow()']//*[text()='删除']").click()
            log.info("变量索引配置删除{0}条配置".format(len(col_set_ele)))

        # 点击添加按钮
        browser.find_element(By.XPATH, "//*[@onclick='appendRow()']//*[text()='添加']").click()

        # 开始添加
        row_edit_xpath = "//*[contains(@id,'tableVarCfg') and contains(@class,'editing')]"
        for col in var_map:
            # 变量索引
            var_index = col[0]
            # 索引说明
            var_detail = col[1]
            # 变量元素类型
            data_type = col[2]
            # 变量元素格式
            data_format = col[3]
            # 类型
            col_type = col[4]

            # 变量索引
            if var_index:
                browser.find_element(
                    By.XPATH, row_edit_xpath + "/*[@field='varIndex']//input[contains(@id,'textbox')]").clear()
                browser.find_element(
                    By.XPATH, row_edit_xpath + "/*[@field='varIndex']//input[contains(@id,'textbox')]").send_keys(
                    var_index)
                log.info("设置变量索引: {0}".format(var_index))

            # 索引说明
            if var_detail:
                browser.find_element(
                    By.XPATH, row_edit_xpath + "/*[@field='varDetail']//input[contains(@id,'textbox')]").clear()
                browser.find_element(
                    By.XPATH, row_edit_xpath + "/*[@field='varDetail']//input[contains(@id,'textbox')]").send_keys(
                    var_detail)
                log.info("设置索引说明: {0}".format(var_detail))

            # 变量元素类型
            if data_type:
                browser.find_element(By.XPATH, row_edit_xpath + "/*[@field='dataType']//a").click()
                sleep(1)
                browser.find_element(
                    By.XPATH, "//*[contains(@id,'_easyui_combobox') and text()='{0}']".format(data_type)).click()
                log.info("设置变量元素类型: {0}".format(data_type))

            # 变量元素格式
            if data_format:
                browser.find_element(By.XPATH, row_edit_xpath + "/*[@field='dataFormat']//a").click()
                sleep(1)
                browser.find_element(
                    By.XPATH, "//*[contains(@id,'_easyui_combobox') and text()='{0}']".format(data_format)).click()
                log.info("设置变量元素格式: {0}".format(data_format))

            # 类型
            if col_type:
                browser.find_element(By.XPATH, row_edit_xpath + "/*[@field='colType']//a").click()
                sleep(1)
                browser.find_element(
                    By.XPATH, "//*[contains(@id,'_easyui_combobox') and text()='{0}']".format(col_type)).click()
                log.info("设置类型: {0}".format(col_type))

            # 如果不是数组最后一个，点击添加按钮继续添加，点击添加自动保存当前配置
            if col != var_map[-1]:
                browser.find_element(By.XPATH, "//*[@onclick='appendRow()']//*[text()='添加']").click()
            log.info("索引【{0}】配置完成".format(var_index))
            sleep(1)

    # 数据接口名称
    if interface_name:
        browser.find_element(By.XPATH, "//*[@id='interfaceName']/following-sibling::span/input[1]").clear()
        browser.find_element(
            By.XPATH, "//*[@id='interfaceName']/following-sibling::span/input[1]").send_keys(interface_name)
        log.info("设置数据接口名称: {0}".format(interface_name))

    # 备注
    if remark:
        remark_textarea = browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span/textarea")
        set_textarea(textarea=remark_textarea, msg=remark)
        log.info("设置备注")

    # 样例数据
    if sample_data:
        sample_data_area = browser.find_element(By.XPATH, "//*[@id='sampleData']")
        content = load_sample(sample_file_name=sample_data)
        set_textarea(textarea=sample_data_area, msg=content)
        log.info("设置样例数据")

    # 保存节点变量配置
    browser.find_element(By.XPATH, "//*[@onclick='saveNodeVarRel();']//*[text()='保存']").click()
    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("保存成功"):
        log.info("保存节点变量配置成功")
        # 进入节点业务配置页面
        wait = WebDriverWait(browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'./node/reportNode.html')]")))
    else:
        log.warning("保存节点变量配置失败，失败提示: {0}".format(msg))
    set_global_var("resultMsg", msg, False)

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='save_node_info']//*[text()='保存']").click()
    log.info("保存业务配置")

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
