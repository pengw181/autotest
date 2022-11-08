# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午11:29

from time import sleep
from client.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def crawler_fetch(opt, target_var, var_name, element_name, value_type):
    """
    :param opt: 操作
    :param target_var: 变量名
    :param var_name: 元素名称
    :param element_name: 元素名称
    :param value_type: 赋值方式

    # 添加
    {
        "操作": "添加",
        "变量名": "流程-表格取数",
        "元素名称": "表格取数",
        "赋值方式": "替换"
    }

    # 修改
    {
        "操作": "修改",
        "目标变量": "流程-表格取数",
        "变量名": "流程-表格取数1",
        "元素名称": "表格取数",
        "赋值方式": "替换"
    }

    # 删除
    {
        "操作": "删除",
        "目标变量": "流程-表格取数1"
    }

    """
    browser = get_global_var("browser")
    if opt == "添加":
        browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        sleep(1)
        browser.switch_to.frame(
            browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataCrawlerNodeEdit.html')]"))
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))
        log.info("添加取数配置")
        sleep(1)

        # 变量名
        if var_name:
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名: {0}".format(var_name))
            sleep(1)

        # 元素名称
        if element_name:
            browser.find_element(By.XPATH, "//*[@name='elementName']/preceding-sibling::input").click()
            browser.find_element(
                By.XPATH, "//*[contains(@id,'elementNameSel') and text()='{0}']".format(element_name)).click()
            log.info("设置元素名称: {0}".format(element_name))
            sleep(1)

        # 赋值方式
        if value_type:
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='addFetchVar()']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存取数配置成功")
        else:
            log.warning("保存取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    elif opt == "修改":
        browser.find_element(By.XPATH, "//*[@field='varName']//*[text()='{0}']".format(target_var)).click()
        sleep(1)
        browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        sleep(2)
        browser.switch_to.frame(
            browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataCrawlerNodeEdit.html')]"))
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))
        log.info("修改取数配置")

        # 变量名
        if var_name:
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名: {0}".format(var_name))
            sleep(1)

        # 元素名称
        if element_name:
            browser.find_element(By.XPATH, "//*[@name='elementName']/preceding-sibling::input").click()
            browser.find_element(
                By.XPATH, "//*[contains(@id,'elementNameSel') and text()='{0}']".format(element_name)).click()
            log.info("设置元素名称: {0}".format(element_name))
            sleep(1)

        # 赋值方式
        if value_type:
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='addFetchVar()']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存取数配置成功")
        else:
            log.warning("保存取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    else:
        browser.find_element(By.XPATH, "//*[@field='varName']//*[text()='{0}']".format(target_var)).click()
        sleep(1)
        browser.find_element(By.XPATH, "//*[@id='delBtn']").click()
        log.info("删除取数配置")

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(target_var), auto_click_ok=False):
            alert.click_ok()

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("删除取数配置成功")
            else:
                log.warning("删除取数配置失败，失败提示: {0}".format(msg))
        else:
            log.warning("删除取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    # 切换到节点iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
    # 切换到取数配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataCrawlerNode.html')]"))
