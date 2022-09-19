# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/21 下午4:02

from time import sleep
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.page.func.input import set_textarea
from common.page.func.level import choose_level
from common.log.logger import log
from common.variable.globalVariable import *


class TableModeEData:

    def __init__(self, eData_iframe_xpath, tab_xpath, tab_iframe_xpath, table_main_iframe_xpath, col_iframe_xpath):
        """
        :param eData_iframe_xpath:
        :param tab_xpath:
        :param tab_iframe_xpath:
        :param table_main_iframe_xpath:
        :param col_iframe_xpath:
        """
        self.browser = get_global_var("browser")
        self.eData_iframe_xpath = eData_iframe_xpath
        self.tab_xpath = tab_xpath
        self.tab_iframe_xpath = tab_iframe_xpath
        self.table_main_iframe_xpath = table_main_iframe_xpath
        self.col_iframe_xpath = col_iframe_xpath

    def table_name_page(self, table_name, field, remark):
        """
        :param table_name: 数据表名称
        :param field: 专业领域
        :param remark: 备注
        """
        # 数据表名称
        if table_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(table_name)
            log.info("设置数据表名称: {0}".format(table_name))

        # 专业领域
        if field:
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            page_wait()
            sleep(1)
            # 判断当前是否已经选择了专业领域，如果是，则先取消
            choose_field_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'tempTypeId') and contains(@class,'selected')]")
            if len(choose_field_list) > 0:
                for cf in choose_field_list:
                    cf.click()
            # 依次选择专业领域
            for f in field:
                field_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'tempTypeId') and text()='{0}']".format(f))
                for element in field_elements:
                    if element.is_displayed():
                        element.click()
                        break
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 备注
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span/textarea")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置备注: {0}".format(remark))

    def configure_update_rule(self, cmd, rulerX, result_bind):
        """
        :param cmd: 取参指令
        :param rulerX: 指令解析模版
        :param result_bind: 二维表结果绑定
        """

        log.info("开始进行【配置更新规则】配置")
        self.browser.find_element(By.XPATH, "//*[@id='showPng']").click()
        sleep(1)
        steps_row_element = self.browser.find_element(By.XPATH, "//*[@class='steps_row'][1]")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", steps_row_element)

        # 取参指令
        if cmd:
            self.browser.find_element(By.XPATH, "//*[@id='cmdRow']/following-sibling::span//a").click()
            # 进入绑定指令集页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[contains(@src,'../bindingCmdInfoWin.html')]")))
            sleep(1)
            self.bind_cmd_info(query=cmd)

        # 指令解析模版
        if rulerX:
            self.browser.find_element(By.XPATH, "//*[@id='rulerxRow']/following-sibling::span//a").click()
            # 进入绑定指令解析模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it(
                (By.XPATH, "//iframe[contains(@src,'../bindingRulerxTmplWin.html')]")))
            sleep(1)
            # 关键字
            self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").send_keys(
                rulerX)
            log.info("设置关键字: {0}".format(rulerX))

            # 查询
            self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-query']").click()
            page_wait()
            # 点击解析模版
            self.browser.find_element(By.XPATH, "//*[@field='analyzerName']//*[text()='{}']".format(rulerX)).click()
            # 确定
            self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-ok']").click()
            # 返回上层iframe
            self.browser.switch_to.parent_frame()
            page_wait(5)
            sleep(1)

        # 二维表结果绑定
        if result_bind:
            bind_row_element = self.browser.find_element(By.XPATH, "//*[text()='二维表结果绑定:']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", bind_row_element)
            i = 1
            for col_name in result_bind:
                self.browser.find_element(By.XPATH, "//*[@id='edataFormatTable']//th[{0}]//a".format(i)).click()
                col_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(col_name))
                for element in col_elements:
                    if element.is_displayed():
                        element.click()
                        log.info("第{0}列绑定到{1}".format(i, col_name))
                        i += 1
                        sleep(1)
                        break

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='tablemode-updateRuleCfgSave']").click()
        self.browser.switch_to.default_content()
        # 进入模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("保存成功", auto_click_ok=False):
            alert.click_ok()
            log.info("配置更新规则成功")
        else:
            log.warning("配置更新规则失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def bind_cmd_info(self, query):
        """
        :param query: 查询条件
        :return: 选择指令后，自动返回上层iframe
        """
        # 关键字
        if query.__contains__("关键字"):
            keyword = query.get("关键字")
            self.browser.find_element(By.XPATH, "//*[@id='cmdKeyword']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='cmdKeyword']/following-sibling::span/input[1]").send_keys(keyword)
            log.info("设置关键字: {0}".format(keyword))

        # 网元分类
        if query.__contains__("网元分类"):
            level = query.get("网元分类")
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            choose_level(level_list=level)
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            log.info("设置网元分类: {0}".format(level))

        # 厂家
        if query.__contains__("厂家"):
            vendor = query.get("厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vendor') and text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModel') and text()='{0}']".format(model)).click()
            log.info("设置设备型号: {0}".format(model))

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='cmd-query']").click()
        page_wait()
        # 选列表第一个
        self.browser.find_element(By.XPATH, "//*[contains(@id,'cmdInfoTab')][1]/*[@field='cmdName']").click()
        # 确定
        self.browser.find_element(By.XPATH, "//*[@id='cmd-ok']").click()
        # 返回上层iframe
        self.browser.switch_to.parent_frame()
