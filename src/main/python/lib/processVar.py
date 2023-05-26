# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午4:13

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def choose_var(var_name, var_type=None):
    """
    # 变量检索页面
    :param var_name: 变量名
    :param var_type: 变量类型，节点定义变量、流程定义变量，默认为空

    """
    browser = gbl.service.get("browser")
    page_wait()
    # 切换iframe
    wait = WebDriverWait(browser, 30)
    wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'varList2.html?')]")))

    # 等待页面加载
    page_wait()
    sleep(2)
    # browser.find_element(By.XPATH, "//*[@for='listBtn_1' and text()='自定义变量']").click()

    # 输入变量名称
    var_name_input = browser.find_elements(
        By.XPATH, "//*[@id='query_vars_form']//*[@name='varName']/preceding-sibling::input")
    for vni in var_name_input:
        if vni.is_displayed():
            vni.send_keys(var_name)
            # log.info("输入变量名关键字: {0}".format(var_name))
            sleep(1)
            break

    # 选择变量分类
    if var_type:
        browser.find_element(By.XPATH, "//*[@id='varClassification']/following-sibling::span[1]//a").click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'varClassification_') and text()='{0}']".format(var_type)).click()
        log.info("选择变量分类: {0}".format(var_type))
        sleep(1)

    # 等待
    page_wait()

    # 点击查询
    search_button = browser.find_elements(By.XPATH, "//*[@id='queryUserDefBtn']//*[text()='查询']")
    for button in search_button:
        if button.is_displayed():
            button.click()
            # log.info("点击查询")
            break

    # 等待查询结果
    page_wait()

    # 勾选变量
    var_ele = browser.find_elements(By.XPATH, "//*[@field='varName']//*[text()='{0}']".format(var_name))
    for ve in var_ele:
        if ve.is_displayed():
            ve.click()
            log.info("勾选变量: {0}".format(var_name))
            break

    # 点击确定
    browser.find_element(By.XPATH, "//span[text()='确定']").click()
    log.info("选择变量 {0}".format(var_name))

    # iframe切回parent
    browser.switch_to.parent_frame()


def choose_inner_var(var_name, time_format, time_interval, time_unit, language):
    """
    :param var_name: 变量名称
    :param time_format: 时间格式
    :param time_interval: 间隔
    :param time_unit: 单位
    :param language: 语言

    {
        "变量名称": "时间变量",
        "时间格式": "yyyyMMddHHmmss",
        "间隔": "-1",
        "单位": "日",
        "语言": "中文"
    }
    """
    browser = gbl.service.get("browser")
    # 切换iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'varList2.html?')]"))

    # 等待页面加载
    page_wait()
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((
        By.XPATH, "//*[@id='query_vars_form']//*[@name='varName']/preceding-sibling::input")))

    # 系统内置变量
    browser.find_element(By.XPATH, "//*[@for='listBtn_2' and text()='系统内置变量']").click()
    sleep(1)

    # 选择变量
    if var_name:
        browser.find_element(By.XPATH, "//*[@name='buildvar']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'buildvar') and text()='{0}']".format(var_name)).click()
        sleep(1)

    # 获取操作模式当前选择值
    js = "return $(\"input[name='buildvar']\").val();"
    inner_func_name = browser.execute_script(js)
    log.info("内置函数: {0}".format(inner_func_name))
    if inner_func_name == "time":
        inner_func_name = "时间变量"
    else:
        # 其它类型
        pass
    log.info("内置函数转义: {0}".format(inner_func_name))

    # 设置内置变量
    if inner_func_name == "时间变量":

        # 时间格式
        if time_format:
            browser.find_element(By.XPATH, "//*[@id='format']/following-sibling::span[1]//a").click()
            # 先进行选择，如果选择不到，则直接输入
            try:
                browser.find_element(By.XPATH, "//*[contains(@id,'format') and text()='{0}']".format(time_format)).click()
            except NoSuchElementException:
                browser.find_element(By.XPATH, "//*[@id='format']/following-sibling::span[1]//input[1]").clear()
                browser.find_element(
                    By.XPATH, "//*[@id='format']/following-sibling::span[1]//input[1]").send_keys(time_format)
                sleep(1)
                browser.find_element(By.XPATH, "//*[@id='format']/following-sibling::span[1]//a").click()
            finally:
                log.info("设置时间格式: {0}".format(time_format))
                sleep(1)

        # 间隔
        if time_interval:
            browser.find_element(By.XPATH, "//*[@name='interval']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='interval']/preceding-sibling::input").send_keys(time_interval)
            log.info("设置间隔: {0}".format(time_interval))
            sleep(1)

        # 单位
        if time_unit:
            browser.find_element(By.XPATH, "//*[@name='unit']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'unit') and text()='{0}']".format(time_unit)).click()
            log.info("设置单位: {0}".format(time_unit))
            sleep(1)

        # 语言
        if language:
            browser.find_element(By.XPATH, "//*[@name='language']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'language') and text()='{0}']".format(language)).click()
            log.info("设置语言: {0}".format(language))
            sleep(1)

        # 点击预览
        browser.find_element(By.XPATH, "//*[@onclick='previewTimeFormat();']//*[text()='预览']").click()
        sleep(1)
        time_result = browser.find_element(By.XPATH, "//*[@id='timeResult']")
        time_view = time_result.get_attribute("innerText")
        log.info("时间函数预览结果: {0}".format(time_view))

    # 保存内置变量
    browser.find_element(By.XPATH, "//*[@onclick='saveBuildInVar();']//*[text()='保存']").click()

    # iframe切回parent
    browser.switch_to.parent_frame()


def var_list_panel(var_type, var_name):
    # 适用于流程的sql节点/接口节点/信息节点/邮件节点
    """
    :param var_type: 自定义变量/流程定义变量/系统内置变量
    :param var_name: 变量名
    :return: 双击变量，加入到左侧输入框，执行完之后，返回上层iframe，panel是在里层iframe
    """
    browser = gbl.service.get("browser")
    # 切换iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'varListPanel.html?')]"))
    # 点击变量分类tab
    browser.find_element(By.XPATH, "//*[@class='tabs-title' and text()='{0}']".format(var_type)).click()
    sleep(1)
    if var_type == "自定义变量":
        # 清空变量输入框
        browser.find_element(By.XPATH, "//*[@id='varNameDef_1']/following-sibling::span/input[1]").clear()
        # 输入变量名
        browser.find_element(By.XPATH, "//*[@id='varNameDef_1']/following-sibling::span/input[1]").send_keys(var_name)
        # 点击查询
        browser.find_element(By.XPATH, "//*[@id='varNameDefBtn']//*[text()='查询']").click()
        page_wait()
        var_element = browser.find_element(
            By.XPATH, "//*[@id='userdefinedTable_1']/*[@title='{0}']/span/span".format(var_name))
        # 双击变量名
        action = ActionChains(browser)
        action.double_click(var_element).perform()
        sleep(1)
        # 切回上层iframe
        browser.switch_to.parent_frame()
    elif var_type == "流程定义变量":
        # 清空变量输入框
        browser.find_element(By.XPATH, "//*[@id='varNameDef_2']/following-sibling::span/input[1]").clear()
        # 输入变量名
        browser.find_element(By.XPATH, "//*[@id='varNameDef_2']/following-sibling::span/input[1]").send_keys(var_name)
        # 点击查询
        browser.find_element(By.XPATH, "//*[@id='varNameDef2Btn']//*[text()='查询']").click()
        page_wait()
        var_element = browser.find_element(
            By.XPATH, "//*[@id='userdefinedTable_2']/*[@title='{0}']/span/span".format(var_name))
        # 双击变量名
        action = ActionChains(browser)
        action.double_click(var_element).perform()
        sleep(1)
        # 切回上层iframe
        browser.switch_to.parent_frame()
    elif var_type == "系统内置变量":
        var_element = browser.find_element(By.XPATH, "//*[@id='sysVarsTb']//*[text()='{0}']".format(var_name))
        # 双击变量名
        action = ActionChains(browser)
        action.double_click(var_element).perform()
        # 切回上层iframe
        browser.switch_to.parent_frame()
        sleep(1)
    else:
        raise KeyError("变量类型 {0} 错误，无法选择变量".format(var_type))
