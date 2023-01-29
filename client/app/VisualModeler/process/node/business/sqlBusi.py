# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午11:06

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.func.pageMaskWait import page_wait
from client.page.func.alertBox import BeAlertBox
from client.page.func.processVar import choose_var
from client.page.func.input import set_blob
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def sql_business(node_name, opt_mode, sql_config, advance_set):
    """
    :param node_name: 节点名称
    :param opt_mode: 操作模式
    :param sql_config: sql配置
    :param advance_set: 高级配置，字典

    高级模式
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "Sql节点",
            "节点名称": "Sql节点",
            "业务配置": {
                "节点名称": "Sql节点1",
                "操作模式": "sql节点高级模式",
                "sql配置": {
                    "数据库": "AiSee",
                    "编写sql": [
                        {
                            "类型": "自定义值",
                            "值": "select * from "
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "值": "加载pw自动化测试文件名1"
                        },
                        {
                            "类型": "自定义值",
                            "值": " where col_2 = "
                        },
                        {
                            "类型": "变量",
                            "变量分类": "流程定义变量",
                            "值": "地点"
                        },
                        {
                            "类型": "自定义值",
                            "值": " and col_3 = "
                        },
                        {
                            "类型": "变量",
                            "变量分类": "系统内置变量",
                            "值": "流程实例ID"
                        }
                    ]
                },
                "高级配置": {
                    "状态": "开启",
                    "超时时间": "600",
                    "超时重试次数": ""
                }
            }
        }
    }

    普通模式
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "Sql节点",
            "节点名称": "Sql节点",
            "业务配置": {
                "节点名称": "Sql节点2",
                "操作模式": "sql节点普通模式",
                "sql配置": {
                    "变量": "时间",
                    "数据库": "AiSee",
                    "存储模式": "",
                    "表选择": "pw网元其他资料新表",
                    "字段映射": {
                        "列1": {
                            "值类型": "索引",
                            "字段值": "1"
                        },
                        "列2": {
                            "值类型": "变量名",
                            "字段值": "地点"
                        },
                        "列3": {
                            "值类型": "自定义值",
                            "字段值": "hello"
                        },
                        "列4": {
                            "值类型": "自定义值",
                            "字段值": ""
                        },
                        "列5": {
                            "值类型": "索引",
                            "字段值": "2"
                        }
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
    sleep(1)
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))

    # 选择操作模式
    if opt_mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(opt_mode)).click()
        log.info("设置操作模式: {0}".format(opt_mode))
        sleep(1)

    # 根据操作模式来分别处理
    js = "return $(\"input[name='node_model_id']\").val();"
    operate_mode = browser.execute_script(js)
    log.info("操作模式: {0}".format(operate_mode))
    if operate_mode == "900":
        operate_mode = "sql节点高级模式"
    elif operate_mode == "901":
        operate_mode = "sql节点普通模式"
    else:
        raise Exception("获取操作模式失败")
    log.info("操作模式转义: {0}".format(operate_mode))

    # sql配置
    if sql_config:
        if operate_mode == "sql节点高级模式":
            log.info("配置sql节点高级模式")
            sql_advance_mode(db=sql_config.get("数据库"), sql=sql_config.get("编写sql"))
        else:
            log.info("配置sql节点普通模式")
            sql_normal_mode(var=sql_config.get("变量"), db=sql_config.get("数据库"),
                            storage_mode=sql_config.get("存储模式"), table_name=sql_config.get("表选择"),
                            col_map=sql_config.get("字段映射"))

    # 设置高级模式
    if advance_set:
        if advance_set.get("状态") == "开启":
            timeout = advance_set.get("超时时间")
            retry_times = advance_set.get("超时重试次数")
            try:
                browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']").click()
                log.info("开启【高级配置】")
            except NoSuchElementException:
                pass

            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='timeOut']/preceding-sibling::input").send_keys(timeout)
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").send_keys(retry_times)
            log.info("设置高级模式")

        else:
            try:
                browser.find_element(By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                browser.find_element(
                    By.XPATH, "//*[@onclick='show_advanced_mode($(this))']//*[text()='关闭高级模式']").click()
                log.info("关闭【高级配置】")
        sleep(1)

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='save_sqlContent']//*[text()='保存']").click()
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


def sql_advance_mode(db, sql):
    """
    :param db: 数据库，必填
    :param sql: 编写sql，必填
    """
    browser = get_global_var("browser")
    # 选择数据库
    if db:
        browser.find_element(By.XPATH, "//*[@name='dbId']/preceding-sibling::input").click()
        db_element = browser.find_element(By.XPATH, "//*[contains(@id,'db_name') and text()='{0}']".format(db))
        browser.execute_script("arguments[0].scrollIntoView(true);", db_element)
        db_element.click()

    # 切换到编写sql的iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'sqlNodeAdv.html')]"))

    # 编写sql
    if sql:
        log.info("开始填写sql")
        log.info(sql)
        text_area = browser.find_element(By.XPATH, "//*[@id='sql_content']")
        set_blob(textarea=text_area, array=sql)
        log.info("sql填写完成")

    # 编写完sql后，需要返回到上层iframe
    browser.switch_to.parent_frame()


def sql_normal_mode(var, db, storage_mode, table_name, col_map):
    """
    :param var: 变量，必填
    :param db: 数据库，必填
    :param storage_mode: 存储模式，非必填
    :param table_name: 表选择，必填
    :param col_map: 字段映射，字典，必填
    """
    browser = get_global_var("browser")
    # 点击添加
    browser.find_element(By.XPATH, "//*[@id='normalCfgAdd']//*[text()='添加']").click()
    page_wait()
    sleep(1)

    # 进入普通模式iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'sqlNodeNormalEdit.html?')]"))
    # 等待页面加载
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='dataH_inputVar2Name']/following-sibling::span//a")))

    # 点击选择变量
    if var:
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVar2Name']/following-sibling::span//a").click()
        choose_var(var_name=var)
        log.info("选择变量: {0}".format(var))
        sleep(1)

    # 选择数据库
    if db:
        browser.find_element(By.XPATH, "//*[@name='dbId']/preceding-sibling::input").click()
        db_element = browser.find_element(By.XPATH, "//*[contains(@id,'dbId') and text()='{0}']".format(db))
        browser.execute_script("arguments[0].scrollIntoView(true);", db_element)
        db_element.click()
        log.info("选择数据库: {0}".format(db))
        sleep(1)

    # 设置存储模式
    if storage_mode:
        browser.find_element(By.XPATH, "//*[@name='storageMode']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'storageMode') and text()='{0}']".format(storage_mode)).click()
        log.info("选择存储模式: {0}".format(storage_mode))
        sleep(1)

    # 选择表
    if table_name:
        page_wait()
        table_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'tree_easyui_tree_')]//*[text()='{0}']".format(table_name))
        browser.execute_script("arguments[0].scrollIntoView(true);", table_element)
        table_element.click()
        log.info("选择表: {0}".format(table_name))
        sleep(1)

    # 配置字段映射
    if col_map:
        log.info("开始配置字段映射")
        for key, value in col_map.items():
            col_type = value.get("值类型")
            col_value = value.get("字段值")
            # 等待列加载完成
            wait = WebDriverWait(browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@field='columnChiName']/*[text()='{}']".format(key))))
            # 设置值类型
            browser.find_element(
                By.XPATH, "//*[@field='columnChiName']/*[text()='{}']/../following-sibling::td[2]//a".format(key)).click()
            type_element = browser.find_elements(By.XPATH, "//*[contains(@id,'typeCOL') and text()='{0}']".format(col_type))
            for e in type_element:
                if e.is_displayed():
                    e.click()
                    break
            # 填写值
            if col_type == "变量名":
                # 变量
                browser.find_element(
                    By.XPATH, "//*[@field='columnChiName']/*[text()='{}']/../following-sibling::td[1]//a".format(key)).click()
                choose_var(var_name=col_value)
            else:
                browser.find_element(
                    By.XPATH, "//*[@field='columnChiName']/*[text()='{}']/../following-sibling::td[1]//*[contains(@id,'input')]".format(
                        key)).send_keys(col_value)
            log.info("字段: {0} 映射配置完成".format(key))
            sleep(1)

    # 点击保存
    browser.find_element(By.XPATH, "//*[@onclick='saves()']//*[text()='保存']").click()
    # 切回业务配置iframe
    browser.switch_to.parent_frame()
