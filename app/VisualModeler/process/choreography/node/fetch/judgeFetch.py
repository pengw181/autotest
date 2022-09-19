# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午11:18

from time import sleep
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.log.logger import log
from common.variable.globalVariable import *


def judge_fetch(**kwargs):
    """
    # 添加
    {
        "操作": "添加",
        "变量名称": "格式化二维表结果",
        "对象类型": "网元",
        "结果类型": "格式化二维表结果",
        "指标": "全部",
        "赋值方式": "替换"
    }

    # 修改
    {
        "操作": "修改",
        "目标变量": "格式化二维表结果",
        "变量名称": "解析结果",
        "对象类型": "网元",
        "结果类型": "解析结果",
        "指标": "全部",
        "赋值方式": "替换"
    }

    # 删除
    {
        "操作": "删除",
        "目标变量": "解析结果"
    }

    """
    browser = get_global_var("browser")
    if not kwargs.__contains__("操作"):
        raise AttributeError("未指明操作类型")

    opt = kwargs.get("操作")
    if opt == "添加":
        browser.find_element(By.XPATH, "//*[@id='addIdxVarBtn']").click()
        wait = WebDriverWait(browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))

        # 变量名称
        if kwargs.__contains__("变量名称"):
            var_name = kwargs.get("变量名称")
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名称: {0}".format(var_name))
            sleep(1)

        # 对象类型
        if kwargs.__contains__("对象类型"):
            obj_type = kwargs.get("对象类型")
            browser.find_element(By.XPATH, "//*[@name='objType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'objType') and text()='{0}']".format(obj_type)).click()
            log.info("设置对象类型: {0}".format(obj_type))
            sleep(1)

        # 结果类型
        if kwargs.__contains__("结果类型"):
            result_type = kwargs.get("结果类型")
            browser.find_element(By.XPATH, "//*[@name='resultType']/preceding-sibling::input").click()
            browser.find_element(
                By.XPATH, "//*[contains(@id,'resultType') and text()='{0}']".format(result_type)).click()
            log.info("设置结果类型: {0}".format(result_type))
            sleep(1)

        # 指标
        if kwargs.__contains__("指标"):
            cmd_name = kwargs.get("指标")
            browser.find_element(By.XPATH, "//*[@id='NuMemberId']/following-sibling::span/input[1]").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'NuMemberId') and text()='{0}']".format(cmd_name)).click()
            log.info("设置指标: {0}".format(cmd_name))
            sleep(1)

        # 赋值方式
        if kwargs.__contains__("赋值方式"):
            value_type = kwargs.get("赋值方式")
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(
                By.XPATH, "//*[contains(@id,'valuetype_cmd') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 点击保存
        browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存取数配置成功")
        else:
            log.warning("保存取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    elif opt == "修改":
        obj = kwargs.get("目标变量")
        browser.find_element(By.XPATH, "//*[@field='varName']//*[text()='{0}']".format(obj)).click()
        browser.find_element(By.XPATH, "//*[@id='editIdxVarBtn']").click()
        wait = WebDriverWait(browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='varName']/preceding-sibling::input")))

        # 变量名称
        if kwargs.__contains__("变量名称"):
            var_name = kwargs.get("变量名称")
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(var_name)
            log.info("设置变量名称: {0}".format(var_name))
            sleep(1)

        # 对象类型
        if kwargs.__contains__("对象类型"):
            obj_type = kwargs.get("对象类型")
            browser.find_element(By.XPATH, "//*[@name='objType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'objType') and text()='{0}']".format(obj_type)).click()
            log.info("设置对象类型: {0}".format(obj_type))
            sleep(1)

        # 结果类型
        if kwargs.__contains__("结果类型"):
            result_type = kwargs.get("结果类型")
            browser.find_element(By.XPATH, "//*[@name='resultType']/preceding-sibling::input").click()
            browser.find_element(
                By.XPATH, "//*[contains(@id,'resultType') and text()='{0}']".format(result_type)).click()
            log.info("设置结果类型: {0}".format(result_type))
            sleep(1)

        # 指标
        if kwargs.__contains__("指标"):
            cmd_name = kwargs.get("指标")
            browser.find_element(By.XPATH, "//*[@id='NuMemberId']/following-sibling::span/input[1]").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'NuMemberId') and text()='{0}']".format(cmd_name)).click()
            log.info("设置指标: {0}".format(cmd_name))
            sleep(1)

        # 赋值方式
        if kwargs.__contains__("赋值方式"):
            value_type = kwargs.get("赋值方式")
            browser.find_element(By.XPATH, "//*[@name='valueType']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type)).click()
            log.info("设置赋值方式: {0}".format(value_type))
            sleep(1)

        # 点击保存
        browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存取数配置成功")
        else:
            log.warning("保存取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    else:
        obj = kwargs.get("目标变量")
        browser.find_element(By.XPATH, "//*[@field='varName']//*[text()='{0}']".format(obj)).click()
        browser.find_element(By.XPATH, "//*[@onclick='del_getdata_cmdvar();']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(obj), auto_click_ok=False):
            alert.click_ok()

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("删除取数配置成功")
            else:
                log.warning("删除取数配置失败，失败提示: {0}".format(msg))
        else:
            log.warning("删除取数配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    # 切换到节点iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
    # 切换到取数配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='getdata_edata_custom_node']"))
