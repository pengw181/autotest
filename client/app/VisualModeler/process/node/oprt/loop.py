# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/11/9 下午4:54

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from .condition import condition
from client.page.func.processVar import choose_var
from client.page.func.input import set_text_enable_var
from client.page.func.pageMaskWait import page_wait
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def var_loop(mode, var_name, loop_var_name, value_type, var_type="指令输出变量"):
    """
    :param mode: 模式
    :param var_type: 变量类型
    :param var_name: 变量选择
    :param loop_var_name: 循环行变量名称
    :param value_type: 赋值方式

    # 按变量列表循环
    """
    browser = get_global_var("browser")
    # 选择模式
    if mode:
        if mode == "自定义模式":
            browser.find_element(By.XPATH, "//*[@id='listBtn_mode1']").click()
        else:
            browser.find_element(By.XPATH, "//*[@id='listBtn_mode2']").click()
            # 选择变量类型,目前固定为指令输出变量
            if var_type:
                browser.find_element(By.XPATH, "//*[@name='vartype']/preceding-sibling::input").click()
                browser.find_element(By.XPATH, "//*[contains(@id,'vartype') and text()='{0}']".format(var_type)).click()
        log.info("设置模式: {0}".format(mode))
        sleep(1)

    # 选择变量
    if var_name:
        elements = browser.find_elements(By.XPATH, "//*[contains(text(),'变量选择')]/..//following-sibling::div//a")
        # 点击选择变量
        for e in elements:
            if e.is_displayed():
                e.click()
                break
        choose_var(var_name=var_name)
        log.info("设置变量: {0}".format(var_name))
        sleep(1)

    # 循环行变量名称
    if loop_var_name:
        elements = browser.find_elements(By.XPATH, "//*[@name='outVarName']/preceding-sibling::input")
        for e in elements:
            if e.is_displayed():
                e.clear()
                e.send_keys(loop_var_name)
                log.info("设置循环行变量名称: {0}".format(loop_var_name))
                sleep(1)
                break

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break


def times_loop(loop_times, loop_var_name, value_type, next_condition, end_condition, common_tree, iframe_xpath_list):
    """
    :param loop_times: 循环次数
    :param loop_var_name: 循环变量名称
    :param value_type: 赋值方式
    :param next_condition: 跳至下一轮条件，数组
    :param end_condition: 结束循环条件，数组
    :param common_tree: bool
    :param iframe_xpath_list: 数组

    # 按次数循环
    """
    browser = get_global_var("browser")
    # 循环次数
    if loop_times:
        input_xpath = "//*[@id='cir_times']/following-sibling::span/input[1]"
        set_text_enable_var(input_xpath=input_xpath, msg=loop_times)
        log.info("设置循环次数: {0}".format(loop_times))
        sleep(1)

    # 循环变量名称
    if loop_var_name:
        browser.find_element(By.XPATH, "//*[@name='outVarName_2']/preceding-sibling::input").send_keys(loop_var_name)
        log.info("设置循环变量名称: {0}".format(loop_var_name))
        sleep(1)

    # 跳至下一轮条件
    if next_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('times_nextCondition');\"]//*[text()='修改']").click()
        else:
            browser.find_element(
                By.XPATH, "//*[@onclick=\"showAdd('times_nextCondition','1');\"]//*[text()='修改']").click()
        condition(array=next_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 结束循环条件
    if end_condition:
        if common_tree:
            elements = browser.find_elements(
                By.XPATH, "//*[@onclick=\"showAdd('times_endCondition');\"]//*[text()='修改']")
            for element in elements:
                if element.is_displayed():
                    element.click()
                    break
        else:
            elements = browser.find_elements(
                By.XPATH, "//*[@onclick=\"showAdd('times_endCondition','1');\"]//*[text()='修改']")
            for element in elements:
                if element.is_displayed():
                    element.click()
                    break
        condition(array=end_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 赋值方式
    # 由于设置条件会自动保存，会将赋值方式重置为"替换"，所以将赋值方式放到最后配置
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break
                break


def condition_loop(cir_condition, next_condition, end_condition, common_tree, iframe_xpath_list):
    """
    :param cir_condition: 跳至下一轮条件，数组
    :param next_condition: 结束循环条件，数组
    :param end_condition: 结束循环条件
    :param common_tree: bool
    :param iframe_xpath_list: 数组

    # 按条件循环
    """
    browser = get_global_var("browser")
    # 循环条件
    if cir_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('circleCondition');\"]//*[text()='修改']").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('circleCondition','1');\"]//*[text()='修改']").click()
        condition(array=cir_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 跳至下一轮条件
    if next_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('nextCondition');\"]//*[text()='修改']").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('nextCondition','1');\"]//*[text()='修改']").click()
        condition(array=next_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 结束循环条件
    if end_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('endCondition');\"]//*[text()='修改']").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('endCondition','1');\"]//*[text()='修改']").click()
        condition(array=end_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)


def step_loop(step_name, cir_var_name, value_type):
    """
    :param step_name: 步骤选择
    :param cir_var_name: 循环变量名称
    :param value_type: 赋值方式

    # 按步骤循环
    """
    browser = get_global_var("browser")
    # 步骤选择
    if step_name:
        browser.find_element(By.XPATH, "//*[@id='chooseStepName']/following-sibling::span//a").click()
        # 切换到选择步骤iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'stepList.html?')]"))
        # 等待页面加载
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='stepName']/preceding-sibling::input")))
        # 查询步骤名称
        browser.find_element(By.XPATH, "//*[@name='stepName']/preceding-sibling::input").send_keys(step_name)
        browser.find_element(By.XPATH, "//*[@data-dg-query='#query_steps_tab']//*[text()='查询']").click()
        page_wait()
        browser.find_element(By.XPATH, "//*[contains(@id,'query_steps')]//*[text()='{0}']".format(step_name)).click()
        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='saveChooseStepCondition();']//*[text()='保存']").click()
        log.info("选择步骤: {0}".format(step_name))
        sleep(1)
        # 切换到步骤循环iframe
        browser.switch_to.parent_frame()

    # 循环变量名称
    if cir_var_name:
        browser.find_element(By.XPATH, "//*[@name='circleVarName_Step']/preceding-sibling::input").send_keys(cir_var_name)
        log.info("设置循环变量名称: {0}".format(cir_var_name))
        sleep(1)

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break
