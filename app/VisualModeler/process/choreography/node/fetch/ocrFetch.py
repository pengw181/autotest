# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午9:59

from time import sleep
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


def ocr_fetch(opt, target_var, var_name, result_type, get_col_name, value_type):
    """
    :param opt: 操作
    :param target_var: 目标变量
    :param var_name: 变量名
    :param result_type: 取值类型
    :param get_col_name: 获取列名，是/否
    :param value_type: 赋值方式

    # 添加
    {
        "操作": "添加",
        "变量名": "ocr基本信息",
        "取值类型": "基本信息",
        "赋值方式": "替换",
        "获取列名": "是"
    }

    # 修改
    {
        "操作": "修改",
        "目标变量": "ocr基本信息",
        "变量名": "ocr基本信息1",
        "取值类型": "基本信息",
        "赋值方式": "替换",
        "获取列名": "是"
    }

    # 删除
    {
        "操作": "删除",
        "目标变量": "ocr基本信息1"
    }

    """
    browser = get_global_var("browser")
    page_wait()
    if opt == "添加":
        browser.find_element(By.XPATH, "//*[@onclick='addOcrVarInfo()']").click()
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))

        # 变量名
        if var_name:
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名: {0}".format(var_name))
            sleep(1)

        # 取值类型
        if result_type:
            browser.find_element(By.XPATH, "//*[@name='resultType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'resultType') and text()='{0}']".format(result_type)).click()
            log.info("设置取值类型: {0}".format(result_type))
            sleep(1)

        # 赋值方式
        if value_type:
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 获取列名
        js = 'return $("#isGetColumnName")[0].checked;'
        status = browser.execute_script(js)
        log.info("【获取列名】勾选状态: {0}".format(status))
        # 聚焦元素
        contains_column_name = browser.find_element(By.XPATH, "//*[@for='isGetColumnName']")
        browser.execute_script("arguments[0].scrollIntoView(true);", contains_column_name)
        if get_col_name == "是":
            if not status:
                contains_column_name.click()
            log.info("勾选【获取列名】")
        else:
            if status:
                contains_column_name.click()
                log.info("取消勾选【获取列名】")
            else:
                log.info("【获取列名】标识为否，不开启")

        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='addOcrVar()']").click()

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
        browser.find_element(By.XPATH, "//*[@onclick='edit_getdata_ocr();']").click()
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))

        # 变量名
        if var_name:
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名: {0}".format(var_name))
            sleep(1)

        # 取值类型
        if result_type:
            browser.find_element(By.XPATH, "//*[@name='resultType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'resultType') and text()='{0}']".format(result_type)).click()
            log.info("设置取值类型: {0}".format(result_type))
            sleep(1)

        # 赋值方式
        if value_type:
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 获取列名
        js = 'return $("#isGetColumnName")[0].checked;'
        status = browser.execute_script(js)
        log.info("【获取列名】勾选状态: {0}".format(status))
        # 聚焦元素
        contains_column_name = browser.find_element(By.XPATH, "//*[@for='isGetColumnName']")
        browser.execute_script("arguments[0].scrollIntoView(true);", contains_column_name)
        if get_col_name == "是":
            if not status:
                contains_column_name.click()
            log.info("勾选【获取列名】")
        else:
            if status:
                contains_column_name.click()
                log.info("取消勾选【获取列名】")
            else:
                log.info("【获取列名】标识为否，不开启")

        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='addOcrVar()']").click()

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
        browser.find_element(By.XPATH, "//*[@onclick='del_getdata_ocr();']").click()

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
            set_global_var("ResultMsg", msg, False)
        else:
            log.warning("删除取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    # 切换到节点iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
    # 切换到取数配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataOcrNode.html')]"))
