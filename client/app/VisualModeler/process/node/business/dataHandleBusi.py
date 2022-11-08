# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午9:55

from client.page.func.alertBox import BeAlertBox
from time import sleep
from client.page.func.processVar import choose_var
from service.lib.log.logger import log
from selenium.webdriver.common.by import By
from service.lib.variable.globalVariable import *


def datahandle_business(node_name, mode, var_name1, var_name2, rela_set, update_set, base_var, output_type,
                        output_var, output_cols, value_type):
    """
    :param node_name: 节点名称
    :param mode: 处理模式
    :param var_name1: 变量1
    :param var_name2: 变量2
    :param rela_set: 关联列，数组
    :param update_set: 更新列，数组
    :param base_var: 基准变量
    :param output_type: 输出类型
    :param output_var: 输出变量名称
    :param output_cols: 输出列
    :param value_type: 赋值方式

    # 数据比对
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "数据处理节点",
            "节点名称": "数据处理节点",
            "业务配置": {
                "节点名称": "数据处理节点1",
                "处理模式": "数据比对",
                "变量1": "时间",
                "变量2": "名字",
                "关联列": [
                    ["1", "1"],
                    ["2", "3"],
                    ["3", "4"]
                ],
                "基准变量": "变量1",
                "输出类型": "关联结果",
                "输出变量名称": "数据比对-关联结果",
                "输出列": "1,2,3,4,5,6",
                "赋值方式": "替换"
            }
        }
    }

    # 数据更新
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "数据处理节点",
            "节点名称": "数据处理节点",
            "业务配置": {
                "节点名称": "数据处理节点1",
                "处理模式": "数据更新",
                "变量1": "时间",
                "变量2": "名字",
                "关联列": [
                    ["1", "1"],
                    ["2", "3"],
                    ["3", "4"]
                ],
                "更新列": [
                    ["4", "4"],
                    ["5", "7"],
                    ["6", "3"]
                ],
                "基准变量": "变量1"
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

    # 处理模式
    if mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(mode)).click()
        log.info("设置处理模式: {0}".format(mode))
        sleep(1)

    # 获取处理模式当前选择值
    js = "return $(\"input[name='node_model_id']\").val();"
    operate_mode = browser.execute_script(js)
    log.info("处理模式: {0}".format(operate_mode))
    if operate_mode == "1101":
        operate_mode = "数据比对"
    elif operate_mode == "1102":
        operate_mode = "数据更新"
    else:
        raise Exception("获取处理模式失败")
    log.info("处理模式转义: {0}".format(operate_mode))

    if operate_mode == "数据比对":
        # 切换到数据比对iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'dataHandleCompare.html')]"))
    else:
        # 切换到数据比对iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'dataHandleUpdate.html')]"))

    # 变量1
    if var_name1:
        browser.find_element(By.XPATH, "//*[@id='dataH_var1Name']/following-sibling::span//a").click()
        choose_var(var_name=var_name1)
        log.info("设置变量1: {0}".format(var_name1))

    # 变量2
    if var_name2:
        browser.find_element(By.XPATH, "//*[@id='dataH_var2Name']/following-sibling::span//a").click()
        choose_var(var_name=var_name2)
        log.info("设置变量2: {0}".format(var_name2))

    # 关联列
    if rela_set:
        num = 1
        for left, right in rela_set:
            # 输入左侧值
            browser.find_element(By.XPATH, "//*[@name='relaCol1_{0}']/preceding-sibling::input".format(num)).clear()
            browser.find_element(By.XPATH, "//*[@name='relaCol1_{0}']/preceding-sibling::input".format(num)).send_keys(left)

            # 输入右侧值
            browser.find_element(By.XPATH, "//*[@name='relaCol2_{0}']/preceding-sibling::input".format(num)).clear()
            browser.find_element(By.XPATH, "//*[@name='relaCol2_{0}']/preceding-sibling::input".format(num)).send_keys(right)

            log.info("关联列{0}输入值: {1}, {2}".format(num, left, right))
            sleep(1)
            if num < len(rela_set):
                browser.find_element(
                    By.XPATH, "//*[@name='relaCol2_{0}']/../../following-sibling::div[1]//*[@onclick='addRelaCol(this)']".format(
                        num)).click()
                num += 1

    # 更新列
    if update_set:
        num = 1
        for left, right in update_set:
            # 输入左侧值
            browser.find_element(By.XPATH, "//*[@name='updateCol1_{0}']/preceding-sibling::input".format(num)).clear()
            browser.find_element(
                By.XPATH, "//*[@name='updateCol1_{0}']/preceding-sibling::input".format(num)).send_keys(left)

            # 输入右侧值
            browser.find_element(By.XPATH, "//*[@name='updateCol2_{0}']/preceding-sibling::input".format(num)).clear()
            browser.find_element(
                By.XPATH, "//*[@name='updateCol2_{0}']/preceding-sibling::input".format(num)).send_keys(right)

            log.info("更新列{0}输入值: {1}, {2}".format(num, left, right))
            sleep(1)
            if num < len(update_set):
                browser.find_element(
                    By.XPATH, "//*[@name='updateCol2_{0}']/../../following-sibling::div[1]//*[@onclick='addUpdateCol(this)']".format(
                        num)).click()
                num += 1

    # 基准变量
    if base_var:
        browser.find_element(By.XPATH, "//*[@name='base']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'base') and text()='{0}']".format(base_var)).click()
        log.info("设置基准变量: {0}".format(base_var))
        sleep(1)

    # 输出类型
    if output_type:
        browser.find_element(By.XPATH, "//*[@name='outputType']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'outputType') and text()='{0}']".format(output_type)).click()
        log.info("设置输出类型: {0}".format(output_type))
        sleep(1)

    # 输出变量名称
    if output_var:
        browser.find_element(By.XPATH, "//*[@id='resultBaseVarName']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='resultBaseVarName']/following-sibling::span/input[1]").send_keys(output_var)
        log.info("设置输出变量名称: {0}".format(output_var))
        sleep(1)

    # 输出列
    if output_cols:
        browser.find_element(By.XPATH, "//*[@name='outColumn']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='outColumn']/preceding-sibling::input").send_keys(output_cols)
        log.info("设置输出列: {0}".format(output_cols))
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

    # 返回上层iframe
    browser.switch_to.parent_frame()

    # 获取节点名称
    node_name = browser.find_element(
        By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@onclick='saveHandleNode(true);']//*[text()='保存']").click()
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
