# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午11:03

from common.page.func.alertBox import BeAlertBox
from time import sleep
from common.page.func.processVar import choose_var
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


def script_business(node_name, script_name, ver_no, params, advance_set):
    """
    :param node_name: 节点名称
    :param script_name: 脚本
    :param ver_no: 版本号
    :param params: 参数列表，字典
    :param advance_set: 高级配置，字典

    无参数
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "脚本节点",
            "节点名称": "脚本节点",
            "业务配置": {
                "节点名称": "脚本节点1",
                "脚本": "pw测试脚本",
                "版本号": "V 3",
                "参数列表": {}
            }
        }
    }

    有参数
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "脚本节点",
            "节点名称": "脚本节点",
            "业务配置": {
                "节点名称": "脚本节点1",
                "脚本": "pw测试相对路径java",
                "版本号": "V 9",
                "高级配置": {
                    "状态": "开启",
                    "超时时间": "600",
                    "超时重试次数": "2"
                },
                "参数列表": {
                    "a": {
                        "设置方式": "变量",
                        "参数值": "时间"
                    },
                    "b": {
                        "设置方式": "固定值",
                        "参数值": "2020-10-20 10:00:00"
                    }
                }
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
        sleep(1)

    # 选择脚本
    if script_name:
        browser.find_element(By.XPATH, "//*[@id='scriptId']/following-sibling::span//a").click()
        script_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'scriptId') and text()='{0}']".format(script_name))
        browser.execute_script("arguments[0].scrollIntoView(true);", script_element)
        script_element.click()
        log.info("选择脚本: {0}".format(script_name))
        sleep(2)

    # 选择版本
    if ver_no:
        browser.find_element(By.XPATH, "//*[@id='versionNo']/following-sibling::span//a").click()
        page_wait()
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[contains(@id,'versionNo') and text()='{0}']".format(ver_no))))

        version_element = browser.find_element(By.XPATH, "//*[contains(@id,'versionNo') and text()='{0}']".format(ver_no))
        browser.execute_script("arguments[0].scrollIntoView(true);", version_element)
        version_element.click()
        log.info("选择版本: {0}".format(ver_no))
        sleep(1)

    # 参数设置
    if params:
        log.info("开始配置脚本参数")
        for key, value in params.items():
            script_param_set(param_key=key, param_type=value.get("设置方式"), param_value=value.get("参数值"))

    # 设置高级模式
    if advance_set:
        if advance_set.get("状态") == "开启":
            timeout = advance_set.get("超时时间")
            retry_times = advance_set.get("超时重试次数")
            try:
                enable_click = browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='开启高级模式']")
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
        elif advance_set.get("状态") == "关闭":
            try:
                browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                disable_click = browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='关闭高级模式']")
                disable_click.click()
                log.info("关闭【高级配置】")
        else:
            raise KeyError("【高级配置】状态只支持：开启/关闭")

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@onclick='saveScriptParamInfo(true)']//*[text()='保存']").click()
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


def script_param_set(param_key, param_type, param_value):
    """
    :param param_key: 参数名
    :param param_type: 设置方式
    :param param_value: 参数值
    """
    browser = get_global_var("browser")
    # 获取参数所在行号
    row_index = browser.find_element(
        By.XPATH, "//*[@field='paramName']/*[text()='{}']/../preceding-sibling::td/div".format(
            param_key)).get_attribute("innerText")
    # 行号从0开始，参数序号从1开始
    row_index = int(row_index)
    # 点击参数类型下拉箭头，展示出参数类型
    browser.find_element(By.XPATH, "//*[@id='valType_{0}']/following-sibling::span//a".format(row_index)).click()

    # 选择参数类型
    param_type_ele = browser.find_elements(
        By.XPATH, "//*[contains(@id,'valType_{0}') and text()='{1}']".format(row_index, param_type))
    for pt in param_type_ele:
        if pt.is_displayed():
            pt.click()
            sleep(1)
            break

    # 设置参赛值
    if param_type == "变量":
        browser.find_element(By.XPATH, "//*[@id='p_var_{0}']/following-sibling::span//a".format(row_index)).click()
        # 选择变量
        choose_var(var_name=param_value)
    else:
        # 输入固定值内容
        browser.find_element(By.XPATH, "//*[@id='paraVal_{0}']/following-sibling::span/input[1]".format(row_index)).clear()
        browser.find_element(
            By.XPATH, "//*[@id='paraVal_{0}']/following-sibling::span/input[1]".format(row_index)).send_keys(param_value)
    log.info("参数{0}配置完成".format(param_key))
    sleep(1)
