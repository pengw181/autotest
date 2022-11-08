# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午10:54

from client.page.func.alertBox import BeAlertBox
from time import sleep
from client.page.func.processVar import choose_var
from client.page.func.input import set_blob
from client.page.func.loadData import load_sample
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def interface_business(node_name, interface, request_body, request_header, params, advance_set):
    """
    :param node_name: 节点名称
    :param interface: 接口
    :param request_body: 请求体内容
    :param request_header: 请求头列表，字典
    :param params: 参数列表，字典
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "接口节点",
            "节点名称": "接口节点",
            "业务配置": {
                "节点名称": "接口节点1",
                "接口": "万能mock-delete",
                "请求体内容": "",
                "请求头列表": {
                    "param1": {
                        "设置方式": "变量",
                        "参数值": "时间"
                    },
                    "param2": {
                        "设置方式": "固定值",
                        "参数值": "2020-10-20 10:00:00"
                    }
                },
                "参数列表": {
                    "name": {
                        "设置方式": "变量",
                        "参数值": "名字"
                    }
                },
                "高级配置": {
                    "状态": "开启",
                    "超时时间": "600",
                    "超时重试次数": "2"
                }
            }
        }
    }

    """
    browser = get_global_var("browser")
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 选择接口
    if interface:
        browser.find_element(By.XPATH, "//*[@name='interfaceId']/preceding-sibling::input").click()
        interface_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'interfaceId') and text()='{0}']".format(interface))
        browser.execute_script("arguments[0].scrollIntoView(true);", interface_element)
        interface_element.click()
        log.info("选择接口: {0}".format(interface))
        sleep(1)

    # 请求体内容
    if request_body:
        request_title = browser.find_element(By.XPATH, "//h4[contains(text(),'请求体内容')]")
        browser.execute_script("arguments[0].scrollIntoView(true);", request_title)
        request_ele = browser.find_element(By.XPATH, "//*[@id='requestBody']")
        if isinstance(request_body, str):
            # 支持传文件名，从文件中读取内容
            request_body = load_sample(sample_file_name=request_body)
            request_body_arr = []
            newline = {
                "类型": "快捷键",
                "快捷键": "换行"
            }
            for s in request_body:
                custom_value = {
                    "类型": "自定义值",
                    "自定义值": s
                }
                request_body_arr.append(custom_value)
                if s != request_body[-1]:
                    request_body_arr.append(newline)
        else:
            request_body_arr = request_body
        log.info(request_body_arr)
        set_blob(textarea=request_ele, array=request_body_arr)
        js = "return $(\"textarea[id='requestBody']\").val();"
        request_body_in_textarea = browser.execute_script(js)
        log.info("设置请求体内容: {0}".format(request_body_in_textarea))
        sleep(1)

    # 请求头列表
    if request_header:
        log.info("开始配置请求头列表")
        request_header_title = browser.find_element(By.XPATH, "//*[@class='panel_title' and contains(text(),'请求头列表')]")
        browser.execute_script("arguments[0].scrollIntoView(true);", request_header_title)
        for key, value in request_header.items():
            set_header(param_name=key, param_type=value.get("设置方式"), param_value=value.get("参数值"))

    # 参数列表
    if params:
        log.info("开始配置参数列表")
        params_title = browser.find_element(By.XPATH, "//*[@class='panel_title' and contains(text(),'参数列表')]")
        browser.execute_script("arguments[0].scrollIntoView(true);", params_title)
        for key, value in params.items():
            set_param(param_name=key, param_type=value.get("设置方式"), param_value=value.get("参数值"))

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

            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").send_keys(timeout)
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").send_keys(retry_times)
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
    browser.find_element(By.XPATH, "//*[@onclick='savePortParamInfo(true)']//*[text()='保存']").click()
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


def set_header(param_name, param_type, param_value):
    """
    :param param_name: 参数名
    :param param_type: 设置方式
    :param param_value: 参数值
    """
    browser = get_global_var("browser")
    req_header = "//*[contains(@data-i18n-text,'reqestHeaderList')]/following-sibling::div"
    browser.find_element(
        By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[1][@field='valueType']//a".format(
            param_name)).click()
    val_type_element = browser.find_elements(
        By.XPATH, req_header + "//*[contains(@id,'valType') and text()='{0}']".format(param_type))
    # 点击当前页面可见的元素
    for e in val_type_element:
        if e.is_displayed():
            e.click()
            break
    sleep(1)
    if param_type == "变量":
        browser.find_element(
            By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[2][@field='paramValue']//a".format(param_name)).click()
        # 选择变量
        choose_var(var_name=param_value)
    else:
        # 输入固定值内容
        input_ele = browser.find_element(
            By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[2][@field='paramValue']//*[contains(@id,'input')]".format(
                param_name))
        input_ele.clear()
        input_ele.send_keys(param_value)
    log.info("请求头{0}配置完成".format(param_name))
    sleep(1)


def set_param(param_name, param_type, param_value):
    """
    :param param_name: 参数名
    :param param_type: 设置方式
    :param param_value: 参数值
    """
    browser = get_global_var("browser")
    req_header = "//*[contains(@data-i18n-text,'paraList')]/following-sibling::div"
    browser.find_element(
        By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[1][@field='valueType']//a".format(
            param_name)).click()
    val_type_element = browser.find_elements(
        By.XPATH, req_header + "//*[contains(@id,'valType') and text()='{0}']".format(param_type))
    # 点击当前页面可见的元素
    for e in val_type_element:
        if e.is_displayed():
            e.click()
            break
    sleep(1)
    if param_type == "变量":
        browser.find_element(
            By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[2][@field='paramValue']//a".format(
                param_name)).click()
        # 选择变量
        choose_var(var_name=param_value)
    else:
        # 输入固定值内容
        input_ele = browser.find_element(
            By.XPATH, req_header + "//*[text()='{0}']/../following-sibling::td[2][@field='paramValue']//*[contains(@id,'input')]".format(
                param_name))
        input_ele.clear()
        input_ele.send_keys(param_value)
    log.info("参数{0}配置完成".format(param_name))
    sleep(1)
