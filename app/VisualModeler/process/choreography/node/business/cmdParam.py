# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午4:30

from common.page.func.processVar import choose_var
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.log.logger import log
from common.variable.globalVariable import *


def cmd_node_param_set(param_mode, params):
    """
    :param param_mode: 模式，独立模式/二维表模式，非必填
    :param params: 参数，字典，必填
    {
        "模式": "独立模式",
        "参数": "时间,地点"
    }

    {
        "模式": "二维表模式",
        "参数": {
            "选择变量": "名字",
            "对象设置": "[1]",
            "参数1": "[2],a",
            "参数2": "[3],b"
        }
    }
    """
    browser = get_global_var("browser")
    # 进入参数设置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'paramCmdNode.html?')]"))

    # 等待页面加载
    sleep(3)
    # wait = WebDriverWait(browser, 5)
    # wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='aloneModelBtn' and @value='0']")))

    # 进入参数设置页面
    if param_mode == "独立模式":
        # 独立模式依次选择变量
        log.info("独立模式配置参数")
        browser.find_element(By.XPATH, "//*[@id='aloneModelBtn' and @value='0']").click()
        sleep(1)
        var_list = params.split(",")
        for i in range(len(var_list)):
            # 点击选择变量
            browser.find_element(By.XPATH, "//*[@name='paramid_{0}']/following-sibling::span[1]//a".format(i + 1)).click()
            # 进入变量检索页面选择变量
            choose_var(var_name=var_list[i])

    elif param_mode == "二维表模式":
        # 选择二维表模式
        log.info("二维表模式配置参数")
        browser.find_element(By.XPATH, "//*[@id='tableModelBtn' and @value='1']").click()
        sleep(1)
        # 点击选择变量
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVarName']/following-sibling::span[1]//a").click()
        # 进入变量检索页面选择变量
        choose_var(var_name=params.get("选择变量"))

        # 对象设置
        browser.find_element(By.XPATH, "//*[@id='obj_index']/following-sibling::span[1]/input[1]").send_keys(
            params.get("对象设置"))
        sleep(1)

        # 填写参数，剔除"选择变量"和"对象设置"，只保留参数
        params.pop("选择变量")
        params.pop("对象设置")
        flag = True
        i = 1
        while flag:
            if params.get("参数{0}".format(i)):
                tmp = params.get("参数{0}".format(i)).split(",", 1)
                index = tmp[0]
                name = tmp[1]
                # 输入参数对象索引
                browser.find_element(
                    By.XPATH, "//*[@name='param_{0}index']/preceding-sibling::input[1]".format(i)).send_keys(index)
                # 输入参数名称
                browser.find_element(
                    By.XPATH, "//*[@name='param_{0}name']/preceding-sibling::input[1]".format(i)).send_keys(name)
                log.info("已配置参数{0}, 对象设置{1}, 参数名称{2}".format(i, index, name))
                i += 1
            else:
                flag = False

    # 保存参数设置
    browser.find_element(By.XPATH, "//*[@onclick='saveCmdParam()']//span[text()='保存']").click()
    sleep(1)

    # 判断是否配置参数成功
    # 如果try的时候出现异常，即使捕获NoSuchElementException，browser也无效了
    try:
        # iframe切回parent
        browser.switch_to.parent_frame()
        browser.find_element(By.XPATH, "//*[@field='cmdName']//*[text()='指令名称']")
        log.info("保存参数成功")
        sleep(2)
    except NoSuchElementException:
        raise
