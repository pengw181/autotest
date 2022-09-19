# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:31

from time import sleep
from selenium.webdriver.common.by import By
from common.page.func.processVar import choose_var
from common.page.func.input import set_text_enable_var
from common.log.logger import log
from common.variable.globalVariable import *


def network_addr(input_type, input_addr, ip, output_var, value_type):
    # 网络地址运算
    """
    :param input_type: 输入方式，子网掩码/位元数，非必填
    :param input_addr: 输入地址，必填
    :param ip: TCP/IP地址，输入方式为子网掩码时必填
    :param output_var: 输出名称，字典，必填
    :param value_type: 赋值方式，替换/追加，非必填

    # 子网掩码方式
    {
        "输入方式": "子网掩码",
        "输入地址": "255.255.0.0",
        "TCP/IP地址": "192.168.88.123",
        "输出名称": {
            "类型": "输入",
            "变量名": "网络地址运算结果-子网掩码输入方式"
        },
        "赋值方式": "替换"
    }

    # 位元数方式
    {
        "输入方式": "位元数",
        "输入地址": "11",
        "输出名称": {
            "类型": "输入",
            "变量名": "网络地址运算结果-子网掩码输入方式"
        },
        "赋值方式": "替换"
    }
    """
    browser = get_global_var("browser")
    # 切换到网络地址运算iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgIpaddr.html')]"))

    # 输入方式
    if input_type:
        browser.find_element(By.XPATH, "//*[text()='{0}']".format(input_type)).click()
        log.info("设置输入方式: {0}".format(input_type))
        sleep(1)

    # 输入地址
    if input_addr:
        input_xpath = "//*[@name='inputAddr']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=input_addr)
        log.info("设置输入地址: {0}".format(input_addr))
        sleep(1)

    # TCP/IP地址
    if ip:
        input_xpath = "//*[@name='tcpIpAddr']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=ip)
        log.info("设置TCP/IP地址: {0}".format(ip))
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
        log.info("设置输出名称: {0}".format(output_var))
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

    # 返回到上层iframe
    browser.switch_to.parent_frame()
