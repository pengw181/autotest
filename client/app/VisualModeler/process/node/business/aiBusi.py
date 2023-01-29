# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午4:06

from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from client.page.func.processVar import choose_var
from client.page.func.alertBox import BeAlertBox
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def ai_business(node_name, mode, algorithm, model, var_name, param_map, interval, advance_set):
    """
    :param node_name: 节点名称
    :param mode: 节点模式
    :param algorithm: 算法选择
    :param model: 模型
    :param var_name: 输入变量
    :param param_map: 对应关系配置，字典
    :param interval: 预测步长
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "AI节点",
            "节点名称": "AI节点",
            "业务配置": {
                "节点名称": "AI节点1",
                "节点模式": "pw测试脚本",
                "算法选择": "",
                "模型": "",
                "输入变量": "",
                "对应关系配置": {
                    "状态": "开启",
                    "1": "time(时间列)",
                    "2": "online_number(预测列)"
                },
                "预测步长": "",
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
    sleep(1)
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 节点模式
    if mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input").click()
        mode_element = browser.find_element(By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(mode))
        browser.execute_script("arguments[0].scrollIntoView(true);", mode_element)
        mode_element.click()
        log.info("设置节点模式: {0}".format(mode))
        sleep(1)

    # 算法选择
    if algorithm:
        browser.find_element(By.XPATH, "//*[@name='algorithmId']/preceding-sibling::input").click()
        algorithm_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'algorithmId') and text()='{0}']".format(algorithm))
        browser.execute_script("arguments[0].scrollIntoView(true);", algorithm_element)
        algorithm_element.click()
        log.info("设置算法选择: {0}".format(algorithm))
        sleep(1)

    # 模型
    if model:
        browser.find_element(By.XPATH, "//*[@name='algorithmModeId']/preceding-sibling::input").click()
        model_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'algorithmModeId') and text()='{0}']".format(model))
        browser.execute_script("arguments[0].scrollIntoView(true);", model_element)
        model_element.click()
        log.info("设置模型: {0}".format(model))
        sleep(1)

    # 输入变量
    if var_name:
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVarName']/following-sibling::span//a").click()
        choose_var(var_name=var_name)
        log.info("设置输入变量: {0}".format(var_name))
        sleep(1)

    # 对应关系配置
    if param_map:
        # 判断是否开启了对应关系配置
        try:
            browser.find_element(By.XPATH, "//*[@id='relaParaTab' and contains(@style,'inline-block')]")
            # 出现配置对应关系输入框，开启开关设为false
            enable_button = False
        except NoSuchElementException:
            enable_button = True

        if param_map.get("状态") == "开启":
            if enable_button:
                browser.find_element(By.XPATH, "//*[@id='rela_cfg']/span").click()
                log.info("开启【对应关系配置】")
                sleep(1)
            else:
                log.info("【对应关系配置】已启用")
            num = 1
            param_map.pop("状态")
            for index, col_name in param_map.items():
                browser.find_element(By.XPATH, "//*[@name='relaCol{0}']/preceding-sibling::input".format(num)).clear()
                browser.find_element(
                    By.XPATH, "//*[@name='relaCol{0}']/preceding-sibling::input".format(num)).send_keys(index)
                browser.find_element(
                    By.XPATH, "//*[@id='cfgcoltype{0}']/following-sibling::span//input[1]".format(num)).click()
                browser.find_element(
                    By.XPATH, "//*[contains(@id,'cfgcoltype{0}') and contains(text(),'{1}')]".format(num, col_name)).click()
                if num < len(param_map):
                    browser.find_element(
                        By.XPATH, "//*[@id='cfgcoltype{0}']/../following-sibling::div[1]/*[@onclick='addIrRelaItem(this)']".format(
                            num)).click()
                num += 1
                sleep(1)
        elif param_map.get("状态") == "关闭":
            if enable_button:
                log.info("【对应关系配置】未启用")
            else:
                browser.find_element(By.XPATH, "//*[@id='rela_cfg']/span").click()
                log.info("关闭【对应关系配置】")
        else:
            raise KeyError("【对应关系配置】状态只支持：开启/关闭")

    # 预测步长
    if interval:
        interval_element = browser.find_element(By.XPATH, "//*[@value='预测步长']/following-sibling::input[1]")
        browser.execute_script("arguments[0].scrollIntoView(true);", interval_element)
        interval_element.clear()
        interval_element.send_keys(interval)
        log.info("设置预测步长: {0}".format(interval))
        sleep(1)

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

            browser.find_element(By.XPATH, "//*[@name='aiTimeout']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='aiTimeout']/preceding-sibling::input").send_keys(timeout)
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
    browser.find_element(By.XPATH, "//*[@onclick='saveIRContent(true)']//*[text()='保存']").click()
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
