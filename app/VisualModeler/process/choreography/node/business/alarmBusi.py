# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/18 下午5:31

from common.page.func.alertBox import BeAlertBox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.log.logger import log
from common.variable.globalVariable import *


def alarm_business(node_name, alarm_data_type, alarm_plan, alarm_rule, invoke_syn, advance_set):
    """
    :param node_name: 节点名称
    :param alarm_data_type: 告警类型
    :param alarm_plan: 告警计划
    :param alarm_rule: 告警规则
    :param invoke_syn: 同步调用，是/否
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试告警节点流程",
            "节点类型": "告警节点",
            "节点名称": "告警节点",
            "告警类型": "结构化数据",
            "告警计划": "pw告警计划",
            "告警规则": "pw告警规则，告警存储数据库",
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

    # 选择告警类型
    if alarm_data_type:
        browser.find_element(By.XPATH, "//*[@id='alarmDataType']/following-sibling::span//a").click()
        alarm_type_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'alarmDataType') and text()='{0}']".format(alarm_data_type))
        browser.execute_script("arguments[0].scrollIntoView(true);", alarm_type_element)
        alarm_type_element.click()
        log.info("选择告警类型: {0}".format(alarm_data_type))
        sleep(1)

    # 选择告警计划
    if alarm_plan:
        browser.find_element(By.XPATH, "//*[@id='alarmPlanId']/following-sibling::span//a").click()
        alarm_plan_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'alarmPlanId') and text()='{0}']".format(alarm_plan))
        browser.execute_script("arguments[0].scrollIntoView(true);", alarm_plan_element)
        alarm_plan_element.click()
        log.info("选择告警计划: {0}".format(alarm_plan))
        sleep(1)

    # 选择告警规则
    if alarm_rule:
        browser.find_element(By.XPATH, "//*[@id='alarmRuleId']/following-sibling::span//a").click()
        alarm_rule_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'alarmRuleId') and text()='{0}']".format(alarm_rule))
        browser.execute_script("arguments[0].scrollIntoView(true);", alarm_rule_element)
        alarm_rule_element.click()
        log.info("选择告警规则: {0}".format(alarm_rule))
        # 等待加载配置
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
    browser.find_element(By.XPATH, "//*[@onclick='saveAlarmInfo()']//*[text()='保存']").click()
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
