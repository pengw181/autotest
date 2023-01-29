# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/21 下午4:02

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.func.alertBox import BeAlertBox
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_textarea
from client.page.func.level import choose_level
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class NormalModeEData:
    # 列更新模式

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

    def col_sets_page(self, col_set):
        """
        :param col_set: 列配置，数组
        """
        log.info("开始进行表配置")
        for col in col_set:
            col_obj = col.get("目标列")
            opt_type = col.get("操作类型")
            col_name = col.get("列名(自定义)")
            col_order = col.get("序号")
            col_type = col.get("列类型")
            col_length = col.get("字符长度")
            col_floatNum = col.get("小位数")
            in_data_format = col.get("输入格式")
            out_data_format = col.get("输出格式")
            cmd = col.get("取参指令")
            rulerX = col.get("指令解析模版")

            # 目标列
            if col_obj:
                self.browser.find_element(
                    By.XPATH, "//*[@class='header' and contains(text(),'{0}')]".format(col_obj)).click()
                log.info("选择列: {0}".format(col_obj))
                sleep(1)

            # 操作类型
            if opt_type:
                if opt_type == "添加":
                    self.browser.find_element(By.XPATH, "//*[@id='cfg-col']//*[text()='添加列']").click()
                elif opt_type == "修改":
                    self.browser.find_element(
                        By.XPATH, "//*[@class='colCanBeEdit' and text()='{0}']".format(col_obj)).click()
                elif opt_type == "删除":
                    # 点击某列删除按钮
                    self.browser.find_element(
                        By.XPATH, "//*[@class='colCanBeEdit' and text()='{0}']/following-sibling::a".format(
                            col_obj)).click()
                    self.browser.switch_to.default_content()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("您确定需要删除{0}吗".format(col_obj), auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(timeout=30, back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("删除成功"):
                            log.info("{0} 删除成功".format(col_obj))
                            # 进入模版配置列表页面
                            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
                            # 进入对应模版类型配置页面iframe
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                            # 进入列配置页面
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.col_iframe_xpath)))
                        else:
                            log.warning("{0} 删除失败，失败提示: {0}".format(col_obj, msg))
                        set_global_var("ResultMsg", msg, False)

                    else:
                        log.warning("{0} 删除失败，失败提示: {0}".format(col_obj, msg))
                    set_global_var("ResultMsg", msg, False)
                    return
                else:
                    raise KeyError("操作类型 仅支持添加/修改/删除，当前值: {0}".format(opt_type))

            # 进入列配置页面
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.col_iframe_xpath)))
            sleep(1)

            # 列名(自定义)
            if col_name:
                self.browser.find_element(By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]").send_keys(col_name)
                log.info("设置列名(自定义): {0}".format(col_name))

            # 序号
            if col_order:
                self.browser.find_element(By.XPATH, "//*[@id='colOrder']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colOrder']/following-sibling::span/input[1]").send_keys(col_order)
                log.info("设置序号: {0}".format(col_order))

            # 列类型
            if col_type:
                self.browser.find_element(By.XPATH, "//*[@id='colCls']//a[text()='{0}']".format(col_type)).click()
                log.info("设置列类型: {0}".format(col_type))

            # 字符长度
            if col_length:
                self.browser.find_element(By.XPATH, "//*[@id='colLength']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colLength']/following-sibling::span/input[1]").send_keys(col_length)
                log.info("设置字符长度: {0}".format(col_length))

            # 小位数
            if col_floatNum:
                self.browser.find_element(
                    By.XPATH, "//*[@id='colFloatNum']//a[text()='{0}']".format(col_floatNum)).click()
                log.info("设置小位数: {0}".format(col_floatNum))

            # 输入格式
            if in_data_format:
                time_format = in_data_format[0]
                custom_format = in_data_format[1]
                self.browser.find_element(By.XPATH, "//*[@id='colInFormat']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id, 'colInFormat') and text()='{0}']".format(time_format)).click()
                log.info("设置输入格式: {0}".format(time_format))
                if time_format == "自定义":
                    self.browser.find_element(
                        By.XPATH, "//*[@id='colInFormatCustom']/following-sibling::span/input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@id='colInFormatCustom']/following-sibling::span/input[1]").send_keys(
                        custom_format)
                    log.info("设置自定义输入格式: {0}".format(custom_format))

            # 输出格式
            if out_data_format:
                time_format = out_data_format[0]
                custom_format = out_data_format[1]
                self.browser.find_element(By.XPATH, "//*[@id='colOutFormat']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'colOutFormat') and text()='{0}']".format(time_format)).click()
                log.info("设置输出格式: {0}".format(time_format))
                if time_format == "自定义":
                    self.browser.find_element(
                        By.XPATH, "//*[@id='colOutFormatCustom']/following-sibling::span/input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@id='colOutFormatCustom']/following-sibling::span/input[1]").send_keys(
                        custom_format)
                    log.info("设置自定义输出格式: {0}".format(custom_format))

            # 取参指令
            if cmd:
                self.browser.find_element(By.XPATH, "//*[@id='cmdRow']//following-sibling::span//a[1]").click()

                # 进入绑定指令集页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it(
                    (By.XPATH, "//iframe[contains(@src,'../bindingCmdInfoWin.html')]")))
                sleep(1)
                self.bind_cmd_info(query=cmd)

            # 指令解析模版
            if rulerX:
                self.browser.find_element(By.XPATH, "//*[@id='rulerxRow']//following-sibling::span//a[1]").click()

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
                self.browser.find_element(
                    By.XPATH, "//*[@field='analyzerName']//*[text()='{}']".format(rulerX)).click()
                # 确定
                self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-ok']").click()
                # 返回上层iframe
                self.browser.switch_to.parent_frame()
                sleep(1)

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='colCfg-save']").click()
            self.browser.switch_to.default_content()
            # 进入模版配置列表页面
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("保存成功", auto_click_ok=False):
                alert.click_ok()
                log.info("列【{0}】配置成功".format(col.get("列名(自定义)")))

                # 进入对应模版类型配置页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                # 进入表配置页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_main_iframe_xpath)))
                sleep(1)
            else:
                log.warning("保存列配置失败，失败提示: {0}".format(msg))
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
