# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:39

from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def sort(input_var, sort_config, output_var, output_col, value_type):
    # 排序运算
    """
    :param input_var: 选择变量，必填
    :param sort_config: 排序配置，字典，必填
    :param output_var: 输出名称，字典，必填
    :param output_col: 输出列，多列以逗号分隔，非必填
    :param value_type: 赋值方式，替换/追加，非必填

    {
        "选择变量": "地点",
        "排序配置": [
            {
                "操作": "添加",
                "列索引": "1",
                "排序方式": "升序"
            },
            {
                "操作": "添加",
                "列索引": "2",
                "排序方式": "降序"
            },
            {
                "操作": "添加",
                "列索引": "4",
                "排序方式": "升序"
            },
            {
                "操作": "修改",
                "已排序索引": "4",
                "列索引": "3",
                "排序方式": "降序"
            },
            {
                "操作": "删除",
                "列索引": "3"
            }
        ],
        "输出名称": {
            "类型": "输入",
            "变量名": "排序运算结果"
        },
        "输出列": "*",
        "赋值方式": "追加"
    }
    """
    browser = gbl.service.get("browser")
    # 切换到排序运算iframe
    browser.switch_to.frame(
        browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgSort.html')]"))

    # 选择变量
    if input_var:
        browser.find_element(By.XPATH, "//*[@id='dataH_inputSortVarName']/following-sibling::span//a").click()
        choose_var(var_name=input_var)
        log.info("选择变量: {0}".format(input_var))
        sleep(1)

    # 排序配置
    if sort_config:
        for so in sort_config:
            sort_col(action=so.get("操作"), sorted_col_index=so.get("已排序索引"), col_index=so.get("列索引"),
                     sort_type=so.get("排序方式"))
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
                panel_xpath = getPanelXpath()
                browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(value_type)).click()
                log.info("设置赋值方式: {0}".format(value_type))
                sleep(1)
                break

    # 返回到上层iframe
    browser.switch_to.parent_frame()


def sort_col(action, sorted_col_index, col_index, sort_type):
    """
    :param action:
    :param sorted_col_index:
    :param col_index:
    :param sort_type:

    [
        {
            "操作": "添加",
            "列索引": "1",
            "排序方式": "升序"
        },
        {
            "操作": "添加",
            "列索引": "2",
            "排序方式": "降序"
        },
        {
            "操作": "添加",
            "列索引": "4",
            "排序方式": "升序"
        },
        {
            "操作": "修改",
            "已排序索引": "4",
            "列索引": "3",
            "排序方式": "降序"
        },
        {
            "操作": "删除",
            "已排序索引": "3"
        }
    ]
    """
    browser = gbl.service.get("browser")
    # 操作
    if action == "添加":
        browser.find_element(By.XPATH, "//*[@onclick='addSortInfo();']//*[text()='添加']").click()
        sleep(1)

        # 列索引
        if col_index:
            browser.find_element(By.XPATH, "//*[@name='col_index']/preceding-sibling::input").send_keys(col_index)

        # 排序方式
        if sort_type:
            browser.find_element(By.XPATH, "//*[@name='sort_type']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'sort_type') and text()='{0}']".format(sort_type)).click()

        browser.find_element(By.XPATH, "//*[@onclick='addSortRow()']//*[text()='保存']").click()
        log.info("添加排序列: {0}".format(col_index))

    elif action == "修改":
        browser.find_element(
            By.XPATH, "//*[contains(@id,'varSortTable')]//div[contains(text(),'排序列：{0}')]".format(
                sorted_col_index)).click()
        browser.find_element(By.XPATH, "//*[@onclick='edit_sort_var();']//*[text()='修改']").click()

        # 列索引
        if col_index:
            browser.find_element(By.XPATH, "//*[@name='col_index']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='col_index']/preceding-sibling::input").send_keys(col_index)

        # 排序方式
        if sort_type:
            browser.find_element(By.XPATH, "//*[@name='sort_type']/preceding-sibling::input").click()
            browser.find_element(By.XPATH, "//*[contains(@id,'sort_type') and text()='{0}']".format(sort_type)).click()

        browser.find_element(By.XPATH, "//*[@onclick='addSortRow()']//*[text()='保存']").click()
        log.info("修改排序列: {0}".format(sorted_col_index))

    else:
        # 只是页面从列表删除，并不会操作数据库，需要保存才生效
        browser.find_element(
            By.XPATH, "//*[contains(@id,'varSortTable')]//div[contains(text(),'排序列：{0}')]".format(
                sorted_col_index)).click()
        browser.find_element(By.XPATH, "//*[@onclick='delete_sort_var();']//*[text()='删除']").click()
        log.info("删除排序列: {0}".format(sorted_col_index))

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("确定需要删除", auto_click_ok=False):
            alert.click_ok()
            log.info("删除排序列成功")
        else:
            log.warning("删除排序列失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

        # 切换到节点iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
        # 切换到操作配置iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
        # 切换到运算配置iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
        # 切换到过滤运算iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgSort.html')]"))
