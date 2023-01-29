# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:26

from time import sleep
from selenium.webdriver.common.by import By
from client.page.func.processVar import choose_var
from client.app.VisualModeler.process.node.oprt.condition import condition
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def basic(expression, output_var, output_col, value_type, transpose):
    # 基础运算
    """
    :param expression: 表达式，字典，必填
    :param output_var: 输出名称，必填，字典
    :param output_col: 输出列， 多列以逗号分隔，非必填
    :param value_type: 赋值方式， 替换/追加，非必填
    :param transpose: 是否转置， bool
    :return 只配置，返回到上层iframe，不保存

    {
        "表达式": [
            ["变量", "时间"],
            ["并集", ""],
            ["变量", "地点"]
        ],
        "输出名称": {
            "类型": "输入",
            "变量名": "普通运算结果"
        },
        "输出列": "*",
        "赋值方式": "替换",
        "是否转置": "否"
    }
    """
    browser = get_global_var("browser")
    # 切换到基础运算iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgBase.html')]"))

    # 配置表达式
    if expression:
        condition(array=expression, basic_cal=True)
        log.info("表达式配置完成")
        sleep(1)

    # 输出名称
    if output_var:
        output_var_type = output_var.get("类型")
        output_var_value = output_var.get("变量名")
        if output_var_type == "输入":
            out_var_element = browser.find_element(
                By.XPATH, "//*[@id='dataH_resultBaseVarName']/following-sibling::span//input[1]")
            browser.execute_script("arguments[0].scrollIntoView(true);", out_var_element)
            out_var_element.send_keys(output_var_value)
        elif output_var_type == "选择":
            # 输出名称选择变量
            browser.find_element(By.XPATH, "//*[@id='dataH_resultBaseVarName']/following-sibling::span//a").click()
            choose_var(var_name=output_var_value)
        else:
            raise KeyError("【输出名称】类型只支持: 输入、选择")
        log.info("设置输出名称: {0}".format(output_var_value))
        sleep(1)

    # 输出列
    if output_col:
        browser.find_element(By.XPATH, "//*[@name='outColumn']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='outColumn']/preceding-sibling::input").send_keys(output_col)
        log.info("设置输出名称: {0}".format(output_col))
        sleep(1)

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valueType') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break

    # 是否转置
    js = 'return $("#isTranspose")[0].checked;'
    status = browser.execute_script(js)
    log.info("【是否转置】勾选状态: {0}".format(status))

    # 聚焦元素
    transpose_click = browser.find_element(By.XPATH, "//*[@id='isTranspose']")
    browser.execute_script("arguments[0].scrollIntoView(true);", transpose_click)

    if transpose:
        if not status:
            transpose_click.click()
        log.info("勾选【是否转置】")
    else:
        if status:
            transpose_click.click()
            log.info("取消勾选【是否转置】")
        else:
            log.info("【是否转置】标识为否，不开启")

    # 返回到上层iframe
    browser.switch_to.parent_frame()
