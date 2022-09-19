# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/18 下午5:31

from common.page.func.alertBox import BeAlertBox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.log.logger import log
from common.variable.globalVariable import *


def data_access_business(node_name, access_type, access_task_name, invoke_syn, advance_set):
    """
    :param node_name: 节点名称
    :param access_type: 接入类型
    :param access_task_name: 接入任务
    :param invoke_syn: 同步调用，是/否
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试数据接入节点流程",
            "节点类型": "数据接入节点",
            "节点名称": "数据接入节点",
            "接入类型": "FTP",
            "接入任务": "pw接入任务配置-ftp接入",
            "同步调用": "是",
            "高级配置": {
                "状态": "开启",
                "超时时间": "600",
                "超时重试次数": "2"
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

    # 选择接入类型
    if access_type:
        browser.find_element(By.XPATH, "//*[@id='accessType']/following-sibling::span//a").click()
        access_type_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'accessType') and text()='{0}']".format(access_type))
        browser.execute_script("arguments[0].scrollIntoView(true);", access_type_element)
        access_type_element.click()
        log.info("选择接入类型: {0}".format(access_type))
        sleep(1)

    # 选择接入任务
    if access_task_name:
        browser.find_element(By.XPATH, "//*[@id='accessId']/following-sibling::span//a").click()
        access_task_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'accessId') and text()='{0}']".format(access_task_name))
        browser.execute_script("arguments[0].scrollIntoView(true);", access_task_element)
        access_task_element.click()
        log.info("选择接入任务: {0}".format(access_task_name))
        # 等待任务加载
        sleep(5)

    # 是否同步调用
    js = 'return $("#invokeSyn")[0].checked;'
    status = browser.execute_script(js)
    log.info("【同步调用】勾选状态: {0}".format(status))

    invokeSyn_element = browser.find_element(By.XPATH, "//*[@for='invokeSyn']")
    browser.execute_script("arguments[0].scrollIntoView(true);", invokeSyn_element)

    if invoke_syn == "是":
        if not status:
            invokeSyn_element.click()
        log.info("开启【同步调用】")
    elif invoke_syn == "否":
        if status:
            invokeSyn_element.click()
        log.info("取消【同步调用】")
    else:
        pass

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

            browser.find_element(By.XPATH, "//*[@name='invokeTimeout']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='invokeTimeout']/preceding-sibling::input").send_keys(timeout)
            browser.find_element(By.XPATH, "//*[@name='retryTimes']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='retryTimes']/preceding-sibling::input").send_keys(retry_times)
            log.info("设置高级模式")
            sleep(1)
        else:
            try:
                browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                disable_click = browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='关闭高级模式']")
                disable_click.click()
                log.info("关闭【高级配置】")

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@onclick='saveAccessInfo()']//*[text()='保存']").click()
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
