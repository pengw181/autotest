# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:33

from time import sleep
from selenium.webdriver.common.by import By
from client.page.func.processVar import choose_var
from client.page.func.regular import RegularCube
from client.page.func.input import set_textarea
from client.page.func.alertBox import BeAlertBox
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def section(output_var, input_var, value_type, begin_config, end_config, sample_data):
    # 分段拆分运算
    """
    :param output_var: 变量名称，必填
    :param input_var: 输入变量，必填
    :param value_type: 赋值方式，替换/追加，非必填
    :param begin_config: 开始特征行，字典，非必填
    :param end_config: 结束特征行，字典，非必填
    :param sample_data: 样例数据，textarea，必填

    {
        "变量名称": "分段拆分运算结果",
        "输入变量": "地点",
        "赋值方式": "追加",
        "开始特征行": {
            "flag": "是",
            "设置方式": "选择",
            "正则模版名称": "pw按时间拆分"
        },
        "结束特征行": {
            "flag": "是",
            "设置方式": "添加",
            "正则模版名称": "pw自动化正则模版-分段拆分运算",
            "高级模式": "否",
            "标签配置": [
                {
                    "标签": "自定义文本",
                    "值": "pw",
                    "是否取值": "黄色"
                },
                {
                    "标签": "任意字符",
                    "值": "1到多个",
                    "是否取值": "绿色"
                },
                {
                    "标签": "自定义文本",
                    "值": "test",
                    "是否取值": "无"
                }
            ]
        },
        "样例数据": ["pw 001 test", "pw 002 test", "pw 003 test", "pw 004 test", "pw 005 test"
    }
    """
    browser = get_global_var("browser")
    # 切换到分段拆分运算iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgSection.html')]"))

    # 变量名称
    if output_var:
        browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(output_var)
        log.info("设置输出变量名称: {0}".format(output_var))
        sleep(1)

    # 输入变量
    if input_var:
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVarName']/following-sibling::span//a").click()
        choose_var(var_name=input_var)
        log.info("选择输入变量: {0}".format(input_var))
        sleep(1)

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break

    # 开始特征行
    if begin_config:
        flag = True if begin_config.get("状态") == "开启" else False
        begin_sep_set(enable_flag=flag, set_type=begin_config.get("设置方式"),
                      regular_name=begin_config.get("正则模版名称"), advance_mode=begin_config.get("高级模式"),
                      regular=begin_config.get("标签配置"), expression=begin_config.get("表达式"))

    # 结束特征行
    if end_config:
        flag = True if end_config.get("状态") == "开启" else False
        end_sep_set(enable_flag=flag, set_type=end_config.get("设置方式"),
                    regular_name=end_config.get("正则模版名称"), advance_mode=end_config.get("高级模式"),
                    regular=end_config.get("标签配置"), expression=end_config.get("表达式"))

    # 输入样例数据
    if sample_data:
        textarea = browser.find_element(By.XPATH, "//*[@id='section_area']//textarea[@id='sampleData']")
        browser.execute_script("arguments[0].scrollIntoView(true);", textarea)
        set_textarea(textarea=textarea, msg=sample_data)
        log.info("输入样例数据")
        sleep(1)

    # 格式化结果
    format_ele = browser.find_element(By.XPATH, "//*[@onclick=\"previewSection('1')\"]//*[text()='格式化结果']")
    browser.execute_script("arguments[0].scrollIntoView(true);", format_ele)
    format_ele.click()
    sleep(1)

    # 返回到上层iframe
    browser.switch_to.parent_frame()


def begin_sep_set(enable_flag, set_type, regular_name, advance_mode, regular, expression):
    """
    :param enable_flag: flag，bool
    :param set_type: 设置方式
    :param regular_name: 正则模版名称
    :param advance_mode: 高级模式
    :param regular: 标签配置
    :param expression: 表达式

    {
        "flag": "是",
        "设置方式": "选择",
        "正则模版名称": "pw按时间拆分"
    }
    """
    browser = get_global_var("browser")
    js = 'return $("#isBeginRow1")[0].checked;'
    status = browser.execute_script(js)
    log.info("【开始特征行】勾选状态: {0}".format(status))
    # 聚焦元素
    begin_sep = browser.find_element(By.XPATH, "//*[@id='isBeginRow1']")
    browser.execute_script("arguments[0].scrollIntoView(true);", begin_sep)
    if enable_flag:
        if not status:
            begin_sep.click()
        log.info("开启【开始特征行】")
        # 开始配置正则
        confirm_selector = "//*[@id='isBeginRowTr1']"
        regular_cube = RegularCube()
        regular_cube.setRegular(confirm_selector=confirm_selector, set_type=set_type, regular_name=regular_name,
                                advance_mode=advance_mode, regular=regular, expression=expression)
        if regular_cube.needJumpIframe:
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存正则模版成功")
                # 切换到节点iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                # 切换到操作配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("OptIframe")))
                # 切换到运算配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                # 切换到分段拆分运算iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgSection.html')]"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            set_global_var("resultMsg", msg, False)
    else:
        if status:
            # 如果flag为否，但当前已勾选，则再点击一次，取消勾选
            begin_sep.click()
            log.info("关闭【开始特征行】")
        else:
            log.info("【开始特征行】标识为否，不开启")


def end_sep_set(enable_flag, set_type, regular_name, advance_mode, regular, expression):
    """
    :param enable_flag: flag，bool
    :param set_type: 设置方式
    :param regular_name: 正则模版名称
    :param advance_mode: 高级模式
    :param regular: 标签配置
    :param expression: 表达式
    """
    browser = get_global_var("browser")
    js = 'return $("#isBeginRow2")[0].checked;'
    status = browser.execute_script(js)
    log.info("【结束特征行】勾选状态: {0}".format(status))
    # 聚焦元素
    end_sep = browser.find_element(By.XPATH, "//*[@id='isBeginRow2']")
    browser.execute_script("arguments[0].scrollIntoView(true);", end_sep)
    if enable_flag:
        if not status:
            end_sep.click()
        log.info("开启【结束特征行】")
        # 开始配置正则
        confirm_selector = "//*[@id='isBeginRowTr2']"
        regular_cube = RegularCube()
        regular_cube.setRegular(confirm_selector=confirm_selector, set_type=set_type, regular_name=regular_name,
                                advance_mode=advance_mode, regular=regular, expression=expression)
        if regular_cube.needJumpIframe:
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存正则模版成功")
                # 切换到节点iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                # 切换到操作配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("OptIframe")))
                # 切换到运算配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                # 切换到分段拆分运算iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgSection.html')]"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            set_global_var("resultMsg", msg, False)

    else:
        if status:
            # 如果flag为否，但当前已勾选，则再点击一次，取消勾选
            end_sep.click()
            log.info("关闭【结束特征行】")
        else:
            log.info("【结束特征行】标识为否，不开启")
