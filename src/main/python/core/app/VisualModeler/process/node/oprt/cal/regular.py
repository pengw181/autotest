# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:17

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.regular import RegularCube
from src.main.python.lib.input import set_textarea
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def regular(input_var, output_var, value_type, var_index, transpose, ruler, fetch):
    # 正则运算
    """
    :param input_var: 输入变量， 必填
    :param output_var: 输出变量， 必填
    :param value_type: 赋值方式：替换/追加，非必填
    :param var_index: 数组索引，文本，多列以逗号分隔，非必填
    :param transpose: bool
    :param ruler: 解析配置，字典，必填
    :param fetch: 取数配置，字典，非必填

    # 文本拆分
    {
        "输入变量": "时间",
        "输出变量": "正则运算结果",
        "赋值方式": "替换",
        "数组索引": "2,3,5",
        "是否转置": "否",
        "解析配置": {
            "解析开始行": "1",
            "通过正则匹配数据列": "否",
            "列总数": "4",
            "拆分方式": "文本",
            "拆分符": ",",
            "高级配置": {}
            "样例数据": ["a1,1,2,3", "a2,1,2,3", "a3,1,2,3", "a4,1,2,3", "a5,1,2,3"]
        },
        "取值配置": {
            "默认值配置": {
                "默认值": "0",
                "行": "3",
                "列": "4"
            },
            "取值规则": {
                "行": "3",
                "列": "4"
            }
        }
    }

    # 正则拆分
    {
        "输入变量": "时间",
        "输出变量": "正则运算结果",
        "赋值方式": "替换",
        "数组索引": "2,3,5",
        "是否转置": "否",
        "解析配置": {
            "解析开始行": "1",
            "通过正则匹配数据列": "否",
            "列总数": "4",
            "拆分方式": "正则",
            "高级配置": "",
            "正则配置": {
                "设置方式": "选择",
                "正则模版名称": "pw按时间拆分"
            }
            "样例数据": ["a1,1,2,3", "a2,1,2,3", "a3,1,2,3", "a4,1,2,3", "a5,1,2,3"]
        }
    }

    # 通过正则匹配数据列
    {
        "输入变量": "时间",
        "输出变量": "正则运算结果",
        "赋值方式": "替换",
        "数组索引": "2,3,5",
        "是否转置": "否",
        "解析配置": {
            "解析开始行": "1",
            "通过正则匹配数据列": "是",
            "高级配置": {},
            "正则配置": {
                "设置方式": "添加",
                "正则模版名称": "pw自动化正则模版-正则运算",
                "高级模式": "否",
                "标签配置": [
                    {
                        "标签": "自定义文本",
                        "自定义值": "pw",
                        "是否取值": "黄色"
                    },
                    {
                        "标签": "任意字符",
                        "长度": "1到多个",
                        "是否取值": "绿色"
                    },
                    {
                        "标签": "自定义文本",
                        "自定义值": "test",
                        "是否取值": "无"
                    }
                ]
            },
            "样例数据": ["pw 001", "pw 002", "pw 003", "pw 004", "pw 005"]
        }
    }
    """
    browser = gbl.service.get("browser")
    # 切换到正则运算iframe
    wait = WebDriverWait(browser, 30)
    wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'operateCfgRegular.html')]")))
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='dataH_inputVarName']/following-sibling::span//a")))

    # 输入变量
    if input_var:
        browser.find_element(By.XPATH, "//*[@id='dataH_inputVarName']/following-sibling::span//a").click()
        choose_var(var_name=input_var)
        log.info("设置输入变量: {0}".format(input_var))
        sleep(1)

    # 输出变量
    if output_var:
        browser.find_element(By.XPATH, "//*[@name='varName']/preceding-sibling::input").send_keys(output_var)
        log.info("设置输出变量: {0}".format(output_var))
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

    # 数组索引
    if var_index:
        browser.find_element(By.XPATH, "//*[@name='inputVarIndex']/preceding-sibling::input").send_keys(var_index)
        log.info("设置数组索引: {0}".format(var_index))
        sleep(1)

    # 是否转置
    js = 'return $("#isTranspose")[0].checked;'
    status = browser.execute_script(js)
    log.info("【是否转置】勾选状态: {0}".format(status))
    # 聚焦元素
    transpose_click = browser.find_element(By.XPATH, "//*[@id='isTranspose']")
    browser.execute_script("arguments[0].scrollIntoView(true);", transpose_click)
    if transpose:
        if not status:
            transpose_click.click()
        log.info("勾选【是否转置】")
    else:
        if status:
            transpose_click.click()
            log.info("取消勾选【是否转置】")
        else:
            log.info("【是否转置】标识为否，不开启")

    # 解析配置
    if ruler:
        confirm_selector = "//*[@id='regexpregex_advCfg']"
        regular_cube = RegularCube()
        regular_cube.setAnalyze(begin_row=ruler.get("解析开始行"), enable_magic=ruler.get("通过正则匹配数据列"),
                                total_columns=ruler.get("列总数"), row_split_type=ruler.get("拆分方式"),
                                split_tag=ruler.get("拆分符"), advance_conf=ruler.get("高级配置"),
                                magic=ruler.get("正则配置"), confirm_selector=confirm_selector)
        if regular_cube.needJumpIframe:
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存正则模版成功")
                # 切换到节点iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                # 切换到操作配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
                # 切换到运算配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                # 切换到正则运算iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgRegular.html')]"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

    # 输入样例数据
    if ruler.__contains__("样例数据"):
        sample_data = ruler.get("样例数据")
        textarea = browser.find_element(
            By.XPATH, "//*[@id='tableExampleDataregex_advCfg']/following-sibling::span/textarea")
        browser.execute_script("arguments[0].scrollIntoView(true);", textarea)
        set_textarea(textarea=textarea, msg=sample_data)
        sleep(1)

    # 格式化结果
    format_ele = browser.find_element(By.XPATH, "//*[text()='效果预览']/following-sibling::div[2]/a")
    browser.execute_script("arguments[0].scrollIntoView(true);", format_ele)
    format_ele.click()
    sleep(1)

    # 取值配置
    if fetch:
        regular_fetch(default_config=fetch.get("默认值配置"), fetch_config=fetch.get("取值规则"))
        sleep(1)

    # 返回到上层iframe
    browser.switch_to.parent_frame()


def regular_fetch(default_config, fetch_config):
    """
    :param default_config: 默认值配置，字典，非必填
    :param fetch_config: 取值规则，字典，非必填

    {
        "默认值配置": {
            "默认值": "0",
            "行": "3",
            "列": "4"
        },
        "取值规则": {
            "行": "3",
            "列": "4"
        }
    }
    """
    browser = gbl.service.get("browser")
    fetch_ele = browser.find_element(By.XPATH, "//*[text()='取值配置']")
    browser.execute_script("arguments[0].scrollIntoView(true);", fetch_ele)
    log.info("开始取值配置")
    # 默认值配置
    if default_config:
        # 默认值
        if default_config.__contains__("默认值"):
            default_var = default_config.get("默认值")
            browser.find_element(By.XPATH, "//*[@name='outDefaultVal']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='outDefaultVal']/preceding-sibling::input").send_keys(default_var)
            log.info("设置默认值: {0}".format(default_var))
        # 行
        if default_config.__contains__("行"):
            default_row = default_config.get("行")
            browser.find_element(By.XPATH, "//*[@name='outRowDefault']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='outRowDefault']/preceding-sibling::input").send_keys(default_row)
            log.info("设置行: {0}".format(default_row))
        # 列
        if default_config.__contains__("列"):
            default_col = default_config.get("列")
            browser.find_element(By.XPATH, "//*[@name='outColDefault']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='outColDefault']/preceding-sibling::input").send_keys(default_col)
            log.info("设置列: {0}".format(default_col))

    # 取值规则
    if fetch_config:
        # 行
        if fetch_config.__contains__("行"):
            fetch_row = fetch_config.get("行")
            browser.find_element(By.XPATH, "//*[@name='resultRow']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='resultRow']/preceding-sibling::input").send_keys(fetch_row)
            log.info("设置行: {0}".format(fetch_row))
        # 列
        if fetch_config.__contains__("列"):
            fetch_col = fetch_config.get("列")
            browser.find_element(By.XPATH, "//*[@name='resultCol']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='resultCol']/preceding-sibling::input").send_keys(fetch_col)
            log.info("设置列: {0}".format(fetch_col))
