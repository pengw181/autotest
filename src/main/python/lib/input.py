# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:21

from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.main.python.lib.processVar import var_list_panel
from src.main.python.lib.waitElement import WaitElement
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def set_textarea(textarea, msg):
    """
    :param textarea: textarea元素
    :param msg: 文本内容，1、字符串；2、数组，每个值之间敲入回车
    """
    textarea.clear()
    sleep(1)
    if isinstance(msg, list):
        for s in msg:
            textarea.send_keys(s)
            if s != msg[-1]:
                textarea.send_keys(Keys.ENTER)
        log.debug("textarea输入内容: {0}".format("\n".join(msg)))
    elif isinstance(msg, str):
        textarea.send_keys(msg)
        log.debug("textarea输入内容: {0}".format(msg))
    else:
        raise KeyError("当前是textarea输入框，支持单行、多行，单行是使用字符串，多行需要使用数组参数，数组里每个值单独一行")


def set_text_enable_var(input_xpath, msg):
    """
    :param input_xpath: 输入框元素xpath
    :param msg: 输入内容，任意文本，可携带${a}
    """
    browser = gbl.service.get("browser")
    input_element = browser.find_element(By.XPATH, input_xpath)
    input_element.clear()
    log.info("定位到输入框，并清空输入框")

    # 解析msg
    end_flag = False
    current_position = 0
    begin_position = 0
    while not end_flag:
        # 寻找最近的${
        position = msg[begin_position:].find("${")  # 相对位置
        if position > -1:
            # 找到${
            enter_text = msg[begin_position: current_position + position + 2]  # 相对位置, +2表示${
            input_element.send_keys(enter_text)
            sleep(1)
            # 定位panel
            panel_xpath = getPanelXpath()
            if not panel_xpath:
                raise NoSuchElementException("找不到可操作的panel")
            current_position = current_position + position + 2

            # 寻找最近的}
            end_position = msg[current_position:].find("}")  # 相对位置
            if end_position > -1:
                end_position = current_position + end_position
                var_name = msg[begin_position + position + 2: end_position]
                begin_position = current_position = end_position + 1
                var_element_xpath = panel_xpath + "//*[contains(@id,'_combobox_') and text()='{0}']".format(var_name)
                try:
                    wait = WebDriverWait(browser, 15)
                    wait.until(ec.element_to_be_clickable((
                        By.XPATH, var_element_xpath)))
                    log.info("变量引用找到变量: {0}".format(var_name))
                    browser.find_element(By.XPATH, var_element_xpath).click()
                    sleep(1)
                except TimeoutException:
                    raise Exception("变量引用选择变量失败, 找不到变量【{0}】".format(var_name))

            else:
                input_element.send_keys(Keys.TAB)
                enter_text = msg[begin_position:]
                input_element.send_keys(enter_text)
                end_flag = True
        else:
            enter_text = msg[begin_position:]
            input_element.send_keys(enter_text)
            input_element.click()
            end_flag = True

    # 检测输入框最终输入内容是否和预期一致
    sleep(1)
    final_value = browser.find_element(By.XPATH, input_xpath + "/following-sibling::input").get_attribute("value")
    if final_value == msg:
        status = True
    else:
        raise Exception("输入框当前值: {0}, 预期输入: {1}, 两者不匹配".format(final_value, msg))
    return status


def set_blob(textarea, array):
    """
    # 大文本，用于邮件节点、信息节点、数据库节点、接口节点设置
    :param textarea: 输入框
    :param array: 数组

    # array
    [
        {
            "类型": "自定义值",
            "自定义值": " and col_3 = "
        },
        {
            "类型": "快捷键",
            "快捷键": "换行"
        },
        {
            "类型": "变量",
            "变量分类": "系统内置变量",
            "变量名": "流程实例ID"
        }
    ]
    """
    textarea.clear()
    for s in array:
        content_type = s.get("类型")
        if content_type == "自定义值":
            # 直接输入
            if s.__contains__("自定义值"):
                var_value = s.get("自定义值")
                textarea.send_keys(var_value)
            else:
                raise KeyError("【自定义值】类型需要包含 自定义值")
        elif content_type == "快捷键":
            if s.__contains__("快捷键"):
                var_value = s.get("快捷键")
                if var_value == "换行":
                    textarea.send_keys(Keys.ENTER)
                else:
                    # 后面补充
                    pass
            else:
                raise KeyError("【自定义值】类型需要包含 自定义值")
        else:
            var_type = s.get("变量分类")
            var_value = s.get("变量名")
            # 调用方法加入变量
            var_list_panel(var_type=var_type, var_name=var_value)
        sleep(1)
