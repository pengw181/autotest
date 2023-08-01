# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:00

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def cmd_template_business(node_name, cmd_temp_name, use_temp_name, advance_set):
    """
    :param node_name: 节点名称
    :param cmd_temp_name: 指令任务模版
    :param use_temp_name: 应用指令模版名称，是/否
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "指令模版节点",
            "节点名称": "指令模版节点",
            "业务配置": {
                "节点名称": "指令模版节点1",
                "指令任务模版": "pw指令模板-组合指令",
                "应用指令模版名称": "是",
                "高级配置": {
                    "状态": "开启",
                    "超时时间": "600",
                    "超时重试次数": ""
                }
            }
        }
    }
    """
    browser = gbl.service.get("browser")
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 点击选择指令任务
    if cmd_temp_name:
        log.info("开始选择指令模版")
        browser.find_element(By.XPATH, "//*[@id='cmdTemplateName']/following-sibling::span[1]//a").click()
        browser.switch_to.frame(
            browser.find_element(By.XPATH, "//iframe[contains(@src, '../../cmd/queryCmdTmplSubPage.html?')]"))
        # 等待页面加载
        page_wait()
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='模版名称']/following-sibling::span[1]/input[1]")))
        sleep(1)
        # 输入指令模版名称
        browser.find_element(By.XPATH, "//*[text()='模版名称']/following-sibling::span[1]/input[1]").send_keys(cmd_temp_name)
        page_wait()
        # 点击查询
        browser.find_element(By.XPATH, "//*[@id='cmdTmpl-query']").click()
        page_wait()
        # 勾选指令模版
        browser.find_element(By.XPATH, "//*[@field='templName']//*[text()='{0}']".format(cmd_temp_name)).click()
        # 点击确定
        browser.find_element(By.XPATH, "//*[@id='cmdTmplSelect']").click()
        log.info("指令模版选择完成")
        sleep(1)
        # 返回上层iframe
        browser.switch_to.parent_frame()
        page_wait()

    # 应用指令模版名称
    js = 'return $("#is_use_cmd_template_name")[0].checked;'
    status = browser.execute_script(js)
    log.info("【应用指令模版名称】勾选状态: {0}".format(status))
    # 聚焦元素
    enable_click = browser.find_element(By.XPATH, "//*[@id='is_use_cmd_template_name']")
    browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

    if use_temp_name == "是":
        # 点击应用指令模版名称
        if not status:
            enable_click.click()
        log.info("勾选【应用指令模版名称】")
    else:
        if status:
            enable_click.click()
            sleep(1)
            if node_name:
                browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
                browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
            log.info("取消勾选【应用指令模版名称】")
    sleep(1)

    # 设置高级模式
    if advance_set:
        if advance_set.get("状态") == "开启":
            timeout = advance_set.get("超时时间")
            # retry_times = advance_set.get("超时重试次数")
            try:
                enable_click = browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                enable_click.click()
                log.info("开启【高级配置】")
            except NoSuchElementException:
                pass

            browser.find_element(By.XPATH, "//*[@name='cmd_timeout']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='cmd_timeout']/preceding-sibling::input").send_keys(timeout)
            # browser.find_element(By.XPATH, "//*[@name='try_time']/preceding-sibling::input").send_keys(retry_times)
            log.info("设置高级模式")
            sleep(1)
        elif advance_set.get("状态") == "关闭":
            try:
                browser.find_element(By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                disable_click = browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='关闭高级模式']")
                disable_click.click()
                log.info("关闭【高级配置】")
        else:
            raise KeyError("【高级模式】状态只支持：开启/关闭")

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='save_retrieve']").click()

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("保存成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    gbl.temp.set("ResultMsg", msg)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name
