# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/4/13 上午11:22

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.processVar import choose_var, choose_inner_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.input import set_textarea, set_text_enable_var
from src.main.python.core.app.VisualModeler.process.node.oprt.function import FunctionWorker
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def set_condition(array, iframe_xpath_list=None, basic_cal=False):
    """
    # iframe_xpath_list用于添加条件表达式后，会自动保存，需要重新进入iframe继续操作
    [
        ["变量", "时间"],
        ["不等于", ""],
        ["空值", ""],
        ["与", ""],
        ["变量", "地点"],
        ["包含", ""],
        ["自定义值", "abc ddd"]
    ]

    [
        ["变量", {
            "变量名称": "时间变量",
            "时间格式": "yyyyMMddHHmmss",
            "间隔": "-1",
            "单位": "日",
            "语言": "中文"
        }],
        ["包含", ""],
        ["自定义值", "1115"]
    ]
    """
    browser = gbl.service.get("browser")
    # 切换到条件表达式配置页面iframe， 基础运算/过滤运算/动作的表达式在当前页面，不需要再跳转iframe
    if not basic_cal:
        browser.switch_to.frame(
            browser.find_element(By.XPATH, "//iframe[contains(@src,'controlCfgLogic.html')]"))
    # 等待页面加载
    page_wait()
    wait = WebDriverWait(browser, 30)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text()='标签元素']")))

    for ele_tag, ele_value in array:
        # 将标签元素拖入表达式中
        element = browser.find_element(By.XPATH, "//*[text()='{0}']".format(ele_tag))
        expression_panel = browser.find_element(By.XPATH, "//*[@id='opera_sortable_0']")
        action = ActionChains(browser)
        action.drag_and_drop(element, expression_panel).perform()
        log.info("表达式加入 {0}".format(ele_tag))

        # 给标签设置值
        if ele_tag == "变量":
            var_name_tips = browser.find_elements(By.XPATH, "//*[contains(@id,'tip_pt_var')]")
            for vnt in var_name_tips:
                if vnt.get_attribute("title") == "":
                    vnt_id = vnt.get_attribute("id")[4:]
                    browser.find_element(
                        By.XPATH, "//*[contains(@onclick,'chooseFunc') and contains(@onclick,'{0}')]".format(
                            vnt_id)).click()
                    sleep(1)
                    break
            # 选择变量，自定义变量或系统内置变量
            try:
                # 如果包含属性"变量名称"，表示内置变量
                ele_value.get("变量名称")
                # 内置变量
                choose_inner_var(var_name=ele_value.get("变量名称"), time_format=ele_value.get("时间格式"),
                                 time_interval=ele_value.get("间隔"), time_unit=ele_value.get("单位"),
                                 language=ele_value.get("语言"))
            except AttributeError:
                choose_var(var_name=ele_value)

        elif ele_tag == "自定义值":
            text_tips = browser.find_elements(By.XPATH, "//*[contains(@id,'tip_pt_constant')]")
            for tt in text_tips:
                if tt.get_attribute("title") == "":
                    tt_id = tt.get_attribute("id")[4:]
                    browser.find_element(
                        By.XPATH, "//*[contains(@onclick,'showText') and contains(@onclick,'{0}')]".format(tt_id)).click()
                    sleep(1)
                    break
            # 切换到输入自定义值iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'showCustom.html?')]"))
            sleep(1)
            text_area = browser.find_element(By.XPATH, "//*[@id='custom_content']")
            set_textarea(textarea=text_area, msg=ele_value)
            sleep(1)
            # 保存自定义值
            browser.find_element(By.XPATH, "//*[@onclick='save_custom();']//*[text()='保存']").click()
            # 返回到表达式iframe
            browser.switch_to.parent_frame()

        elif ele_tag == "变量索引":
            browser.find_element(By.XPATH, "//*[contains(@id,'pt_index')]/following-sibling::span//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)
            sleep(1)

        elif ele_tag == "函数":
            func_name_tips = browser.find_elements(By.XPATH, "//*[contains(@id,'tip_pt_func')]")
            for fnt in func_name_tips:
                if fnt.get_attribute("text") is None:
                    fnt_id = fnt.get_attribute("id")[4:]
                    browser.find_element(
                        By.XPATH, "//*[contains(@onclick,'chooseFunc') and contains(@onclick,'{0}')]".format(
                            fnt_id)).click()
                    sleep(1)
                    break
            # 选择函数
            func = FunctionWorker()
            func.run(var_name=ele_value.get("输入变量"), var_index=ele_value.get("数组索引"),
                     func_list=ele_value.get("函数处理列表"))

        elif ele_tag == "休眠":
            # input_xpath = "//*[@title='sleep']/following-sibling::div//*[@class='textbox-value' and @value='']/preceding-sibling::input"
            input_xpath = "//*[@title='sleep']/following-sibling::div//*[@class='textbox-value']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=ele_value)

        elif ele_tag == "置空":
            var_name_tips = browser.find_elements(By.XPATH, "//*[contains(@id,'tip_pt_var')]")
            for vnt in var_name_tips:
                log.info(vnt.get_attribute("text"))
                if vnt.get_attribute("text") is None:
                    vnt_id = vnt.get_attribute("id")[4:]
                    browser.find_element(
                        By.XPATH, "//*[contains(@onclick,'chooseFunc') and contains(@onclick,'{0}')]".format(
                            vnt_id)).click()
                    sleep(1)
                    break
            # 选择变量
            choose_var(var_name=ele_value)

        elif ele_tag == "总计(sum)":
            browser.find_element(By.XPATH, "//*[@title='sum']/following-sibling::div//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)

        elif ele_tag == "计数(count)":
            browser.find_element(By.XPATH, "//*[@title='count']/following-sibling::div//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)

        elif ele_tag == "最大值(max)":
            browser.find_element(By.XPATH, "//*[@title='max']/following-sibling::div//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)

        elif ele_tag == "最小值(min)":
            browser.find_element(By.XPATH, "//*[@title='min']/following-sibling::div//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)

        elif ele_tag == "平均值(avg)":
            browser.find_element(By.XPATH, "//*[@title='avg']/following-sibling::div//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(ele_value)

        elif ele_tag == "分组连接":
            col, joiner = ele_value.split(",")
            # 第几列
            browser.find_element(By.XPATH, "//*[@title='listagg']/following-sibling::div/span[1]//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(col)
            # 连接符
            browser.find_element(By.XPATH, "//*[@title='listagg']/following-sibling::div/span[2]//*[@class='textbox-value' and "
                                           "@value='']/preceding-sibling::input").send_keys(joiner)

    log.info("表达式设置完成")
    sleep(1)

    if not basic_cal:
        # 保存表达式
        browser.find_element(By.XPATH, "//*[@onclick='saveExpr();']").click()
        sleep(1)

        if not iframe_xpath_list:
            # 默认返回上层iframe，适用于在if里配置条件
            browser.switch_to.parent_frame()
        else:
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存条件成功")
            else:
                log.warning("保存条件失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

            for frame_xpath in iframe_xpath_list:
                frame = browser.find_element(By.XPATH, frame_xpath)
                browser.switch_to.frame(frame)
    else:
        # 基础运算不需要保存表达式，通过保存运算时保存
        pass
