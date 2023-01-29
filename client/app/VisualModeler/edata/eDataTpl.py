# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/3/21 下午2:25

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.func.pageMaskWait import page_wait
from client.page.func.level import choose_level
from client.page.func.alertBox import BeAlertBox
from client.page.func.positionPanel import getPanelXpath
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from client.app.VisualModeler.edata.tableMode import TableModeEData as TableMode
from client.app.VisualModeler.edata.normalMode import NormalModeEData as NormalMode
from client.app.VisualModeler.edata.sectionMode import SectionModeEData as SectionMode
from client.app.VisualModeler.edata.dataMode import DateModeEData as DataMode
from client.app.VisualModeler.edata.joinMode import JoinModeEData as JoinMode
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class EDataTemplate:

    def __init__(self, temp_type):
        """
        :param temp_type: 模版类型
        """
        self.browser = get_global_var("browser")
        self.temp_type = temp_type
        DoctorWho().choose_menu("数据拼盘-模版配置")
        sleep(1)
        self.eData_iframe_xpath = "//iframe[contains(@src, '/VisualModeler/html/edata/edataTmpl.html')]"
        # 进入模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
        page_wait()

        # 点击模式tab
        self.browser.find_element(By.XPATH, "//*[text()='{0}']".format(temp_type)).click()
        page_wait(5)
        log.info("进入 {0}".format(temp_type))

        if self.temp_type == "二维表模式":

            self.tab_name = "2D_TABLE_MODE"
            self.tab_xpath = "//*[@id='updateMode' and @value='{0}']/following-sibling::div".format(self.tab_name)
            # 二维表模式iframe
            self.tab_iframe_xpath = "//iframe[contains(@src,'./edataModeTmpl.html?updateMode={0}')]".format(
                self.tab_name)
            # 表配置页面iframe
            self.table_main_iframe_xpath = "//iframe[contains(@src,'../edata/tablemode/edataTmplEditWin.html')]"
            # 表名配置页面iframe
            self.table_name_iframe_xpath = "//iframe[contains(@src,'tableNameCfgWin.html')]"
            # 列配置页面iframe
            self.col_iframe_xpath = "//iframe[contains(@src,'colCfgWin.html')]"
            self.eData = TableMode(self.eData_iframe_xpath, self.tab_xpath, self.tab_iframe_xpath,
                                   self.table_main_iframe_xpath, self.col_iframe_xpath)

        elif self.temp_type == "列更新模式":

            self.tab_name = "NORMAL_MODE"
            # 列更新模式iframe
            self.tab_iframe_xpath = "//iframe[contains(@src,'./edataModeTmpl.html?updateMode={0}')]".format(
                self.tab_name)
            self.tab_xpath = "//*[@id='updateMode' and @value='{0}']/following-sibling::div".format(self.tab_name)
            # 表配置页面iframe
            self.table_main_iframe_xpath = "//iframe[contains(@src,'../edata/edataTmplEditWin.html')]"
            # 表名配置页面iframe
            self.table_name_iframe_xpath = "//iframe[contains(@src,'tableNameCfgWin.html')]"
            # 列配置页面iframe
            self.col_iframe_xpath = "//iframe[contains(@src,'colCfgWin.html')]"
            self.eData = NormalMode(self.eData_iframe_xpath, self.tab_xpath, self.tab_iframe_xpath,
                                    self.table_main_iframe_xpath, self.col_iframe_xpath)

        elif self.temp_type == "分段模式":

            self.tab_name = "SUBSECTION_MODE"
            # 分段模式iframe
            self.tab_iframe_xpath = "//iframe[contains(@src,'./edataModeTmpl.html?updateMode={0}')]".format(
                self.tab_name)
            self.tab_xpath = "//*[@id='updateMode' and @value='{0}']/following-sibling::div".format(self.tab_name)
            # 表配置页面iframe
            self.table_main_iframe_xpath = "//iframe[contains(@src,'../edata/edataTmplEditWin.html')]"
            # 表名配置页面iframe
            self.table_name_iframe_xpath = "//iframe[contains(@src,'./subsectionmode/tableNameCfgWin.html')]"
            # 列配置页面iframe
            self.col_iframe_xpath = "//iframe[contains(@src,'colCfgWin.html')]"
            self.eData = SectionMode(self.eData_iframe_xpath, self.tab_xpath, self.tab_iframe_xpath,
                                     self.table_main_iframe_xpath, self.table_name_iframe_xpath, self.col_iframe_xpath)

        elif self.temp_type == "数据模式":

            self.tab_name = "DATA_MODE"
            # 数据模式iframe
            self.tab_iframe_xpath = "//iframe[contains(@src,'./edataModeTmpl.html?updateMode={0}')]".format(
                self.tab_name)
            self.tab_xpath = "//*[@id='updateMode' and @value='{0}']/following-sibling::div".format(self.tab_name)
            # 表配置页面iframe
            self.table_main_iframe_xpath = "//iframe[contains(@src,'../edata/edataTmplEditWin.html')]"
            # 表名配置页面iframe
            self.table_name_iframe_xpath = "//iframe[contains(@src,'tableNameCfgWin.html')]"
            # 列配置页面iframe
            self.col_iframe_xpath = "//iframe[contains(@src,'colCfgWin.html')]"
            self.eData = DataMode()

        elif self.temp_type == "合并模式":

            self.tab_name = "JOIN_MODE"
            # 合并模式iframe
            self.tab_iframe_xpath = "//iframe[contains(@src,'./joinmode/joinModeTmpl.html?updateMode={0}')]".format(
                self.tab_name)
            self.tab_xpath = "//*[@id='updateMode' and @value='{0}']/following-sibling::div".format(self.tab_name)
            self.eData = JoinMode(self.eData_iframe_xpath, self.tab_xpath)

        else:
            raise KeyError("数据拼盘模式【{0}】错误".format(self.temp_type))

        # 进入对应模版类型配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
        sleep(1)

    def search(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None

        # 数据表名称
        if query.__contains__("数据表名称"):
            table_name = query.get("数据表名称")
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@id='tableName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@id='tableName']/following-sibling::span/input[1]").send_keys(
                table_name)
            select_item = table_name

        # 是否启用
        if query.__contains__("是否启用"):
            temp_status = query.get("是否启用")
            self.browser.find_element(By.XPATH, "//*[@id='tempStatus']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'tempStatus') and text()='{0}']".format(temp_status)).click()

        # 是否告警
        if query.__contains__("是否告警"):
            is_alarm = query.get("是否告警")
            self.browser.find_element(By.XPATH, "//*[@id='isAlarm']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'isAlarm') and text()='{0}']".format(is_alarm)).click()

        # 专业领域
        if query.__contains__("专业领域"):
            field = query.get("专业领域")
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'tempTypeId') and text()='{0}']".format(field)).click()

        # 查询
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-query']").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)
            return
        if need_choose:
            if select_item:
                try:
                    self.browser.find_element(
                        By.XPATH, self.tab_xpath + "//*[@field='tableNameCh']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add_table(self, table_name, field, remark, cmd, regexp_start, regexp_end, sample):
        """
        :param table_name: 数据表名称
        :param field: 专业领域
        :param remark: 备注
        :param cmd: 取参指令，分段模式使用
        :param regexp_start: 段开始特征行，字典，分段模式使用
        :param regexp_end: 段结束特征行，字典，分段模式使用
        :param sample: 样例数据，数组或文件名，分段模式使用
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-add']").click()
        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_main_iframe_xpath)))
        # 进入表名配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_name_iframe_xpath)))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]")))

        if self.temp_type == "二维表模式":
            self.eData.table_name_page(table_name, field, remark)

        elif self.temp_type == "列更新模式":
            self.eData.table_name_page(table_name, field, remark)

        elif self.temp_type == "分段模式":
            self.eData.table_name_page(table_name, field, remark, cmd, regexp_start, regexp_end, sample)

        elif self.temp_type == "数据模式":
            self.eData.table_name_page(table_name, field, remark)

        elif self.temp_type == "合并模式":
            raise KeyError("合并模式不支持该方法")

        else:
            raise KeyError("未知模式【{0}】".format(self.temp_type))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='tableNameCfg-save']").click()
        self.browser.switch_to.default_content()
        # 进入模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
        alert = BeAlertBox(back_iframe=False, timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(table_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(table_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update_table(self, table, table_name, field, remark, cmd, regexp_start, regexp_end, sample):
        """
        :param table: 数据表名称
        :param table_name: 数据表名称
        :param field: 专业领域
        :param remark: 备注
        :param cmd: 取参指令，分段模式使用
        :param regexp_start: 段开始特征行，字典，分段模式使用
        :param regexp_end: 段结束特征行，字典，分段模式使用
        :param sample: 样例数据，数组或文件名，分段模式使用
        """
        log.info("开始修改数据")
        self.search(query={"数据表名称": table}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-update']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 进入表配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_main_iframe_xpath)))
            self.browser.find_element(By.XPATH, "//*[@id='cfg-tableName']").click()
            # 进入表名配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_name_iframe_xpath)))
            sleep(1)
            # 等待页面可操作
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]")))

            if self.temp_type == "二维表模式":
                self.eData.table_name_page(table, table_name, field, remark)

            elif self.temp_type == "列更新模式":
                self.eData.table_name_page(table, table_name, field, remark)

            elif self.temp_type == "分段模式":
                self.eData.table_name_page(table, table_name, field, remark, cmd, regexp_start, regexp_end, sample)

            elif self.temp_type == "数据模式":
                self.eData.table_name_page(table, table_name, field, remark)

            elif self.temp_type == "合并模式":
                raise KeyError("合并模式不支持该方法")

            else:
                raise KeyError("未知模式【{0}】".format(self.temp_type))

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='tableNameCfg-save']").click()
            self.browser.switch_to.parent_frame()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(table))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(table, msg))
            set_global_var("ResultMsg", msg, False)

    def set_cols(self, table_name, col_set):
        """
        :param table_name: 数据表名称
        :param col_set: 列配置，数组
        """
        self.search(query={"数据表名称": table_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-update']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 进入表配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_main_iframe_xpath)))
            sleep(1)

            if self.temp_type in ["二维表模式", "数据模式"]:
                self.col_sets_page(col_set)
            elif self.temp_type in ["列更新模式", "分段模式"]:
                self.eData.col_sets_page(col_set)
            else:
                raise KeyError("【{0}】模式不支持该方法".format(self.temp_type))

    def set_search_col(self):
        # 设置搜索条件列
        js = 'return $(".isSearch")[0].checked;'
        search_status = self.browser.execute_script(js)
        log.info("【搜索条件】勾选状态: {0}".format(search_status))

    def set_frozen_col(self):
        # 设置冻结列
        pass

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

            # 目标列
            if col_obj:
                self.browser.find_element(
                    By.XPATH, "//*[@class='header' and contains(text(),'{0}')]".format(col_obj)).click()
                log.info("选择列: {0}".format(col_obj))
                sleep(1)

            # 操作类型
            if opt_type:
                if opt_type == "添加":
                    self.browser.find_element(By.XPATH, "//*[@id='cfg-col']").click()
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
                        By.XPATH, "//*[@id='colInFormatCustom']/following-sibling::span/input[1]").send_keys(custom_format)
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
                        By.XPATH, "//*[@id='colOutFormatCustom']/following-sibling::span/input[1]").send_keys(custom_format)
                    log.info("设置自定义输出格式: {0}".format(custom_format))

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

    def configure_update_rule(self, table_name, cmd, rulerX, result_bind):
        """
        # 二维表模式使用
        :param table_name: 数据表名称
        :param cmd: 取参指令
        :param rulerX: 指令解析模版
        :param result_bind: 二维表结果绑定
        """
        self.search(query={"数据表名称": table_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-update']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 进入表配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.table_main_iframe_xpath)))
            sleep(1)

            self.eData.configure_update_rule(cmd, rulerX, result_bind)

    def add_join_table(self, join_table_list, join_type, left_table_set, right_table_set, new_table_name, field, new_table_set):
        """
        # 合并模式
        :param join_table_list: 合并表名称，数组
        :param join_type: 关联方式，左关联/右关联
        :param left_table_set: 左表配置，数组
        :param right_table_set: 右表配置，数组
        :param new_table_name: 数据表名称
        :param field: 专业领域，数组
        :param new_table_set: 新表配置，数组
        """
        self.eData.add_join_table(join_table_list, join_type, left_table_set, right_table_set, new_table_name, field, new_table_set)

    def add_union_table(self, join_table_list, join_type, join_table_set, new_table_name, field, new_table_set):
        """
        # 合并模式
        :param join_table_list: 合并表名称，数组
        :param join_type: 关联方式，UNION/UNION ALL
        :param join_table_set: 合并表配置，数组
        :param new_table_name: 数据表名称
        :param field: 专业领域，数组
        :param new_table_set: 新表配置，数组
        """
        self.eData.add_union_table(join_table_list, join_type, join_table_set, new_table_name, field, new_table_set)

    def bind_netunit(self, table_name, netunit_list):
        """
        # 绑定网元
        :param table_name: 数据表名称
        :param netunit_list: 网元列表，数组

        {
            "数据表名称": "",
            "网元列表": [
                {
                    "网元名称": "",
                    "网元分类": "",
                    "厂家": "",
                    "设备型号": ""
                },
                {
                    "网元名称": "",
                    "网元分类": "",
                    "厂家": "",
                    "设备型号": ""
                },
                {
                    "网元名称": "",
                    "网元分类": "",
                    "厂家": "",
                    "设备型号": ""
                }
            ]
        }
        """
        if self.temp_type in ["二维表模式", "列更新模式", "分段模式"]:
            # 选择表
            self.search(query={"数据表名称": table_name}, need_choose=True)

            # 点击绑定网元
            self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-bindNE']").click()
            # 判断是否进入绑定网元页面
            alert = BeAlertBox(timeout=3)
            if alert.exist_alert:
                msg = alert.get_msg()
                set_global_var("ResultMsg", msg, False)
                return
            else:
                # 进入对应模版类型配置页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))

            # 进入绑定网元页面
            page_wait()
            bindNE_iframe_xpath = "//iframe[contains(@src,'/VisualModeler/html/edata/bindingNetunitInfoWin.html')]"
            # 进入绑定网元页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, bindNE_iframe_xpath)))
            sleep(1)
            # 等待页面可操作
            wait = WebDriverWait(self.browser, 5)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]")))
            sleep(1)

            # 判断当前是否存在已分配网元，存在则先移除
            assigned_ne = self.browser.find_elements(By.XPATH, "//*[contains(@id,'assignedNetunitTab')]//*[text()='1']")
            if len(assigned_ne) > 0:
                sleep(1)
                log.info("存在已分配网元，先移除")
                # 移除右侧所有网元
                self.browser.find_element(By.XPATH, "//*[@class='operatorBtn']/button[4]").click()
                self.browser.switch_to.default_content()
                # 进入模版配置列表页面
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
                alert = BeAlertBox(back_iframe=False)
                alert.click_ok()
                page_wait()

                # 进入对应模版类型配置页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                # 进入绑定网元页面iframe
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, bindNE_iframe_xpath)))
                # 等待页面可操作
                wait = WebDriverWait(self.browser, 5)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]")))
                sleep(1)
                log.info("移除成功")

            # 网元列表
            for ne in netunit_list:
                if not isinstance(ne, dict):
                    raise KeyError("待分配网元列表无网元，请核实")

                # 网元名称
                if ne.__contains__("网元名称"):
                    ne_name = ne.get("网元名称")
                    self.browser.find_element(
                        By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").send_keys(ne_name)
                    log.info("设置网元名称: {0}".format(ne_name))
                    sleep(1)

                # 网元分类
                if ne.__contains__("网元分类"):
                    ne_level = ne.get("网元分类")
                    self.browser.find_element(By.XPATH, "//*[@id='bindingLevelNE']/following-sibling::span//a").click()
                    choose_level(level_list=ne_level)
                    # 再次点击收起下拉框
                    self.browser.find_element(By.XPATH, "//*[@id='bindingLevelNE']/following-sibling::span//a").click()
                    log.info("设置网元分类: {0}".format(ne_level))
                    sleep(1)

                # 厂家
                if ne.__contains__("厂家"):
                    vendor = ne.get("厂家")
                    self.browser.find_element(By.XPATH, "//*[@id='bindingVendorNE']/following-sibling::span//a").click()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'bindingVendorNE') and text()='{0}']".format(vendor)).click()
                    log.info("设置厂家: {0}".format(vendor))
                    sleep(1)

                # 设备型号
                if ne.__contains__("设备型号"):
                    model = ne.get("设备型号")
                    self.browser.find_element(
                        By.XPATH, "//*[@id='bindingNetunitModelNE']/following-sibling::span//a").click()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'bindingNetunitModelNE') and text()='{0}']".format(model)).click()
                    log.info("设置设备型号: {0}".format(model))
                    sleep(1)

                # 点击查询待分配
                self.browser.find_element(By.XPATH, "//*[text()='查询待分配']").click()
                page_wait()

                unassigned_ne = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'unassignedNetunitTab')]//*[text()='1']")
                if len(unassigned_ne) == 0:
                    raise AttributeError("网元列表里的数据格式需要是字典")

                # 分配左侧所有网元
                self.browser.find_element(By.XPATH, "//*[@class='operatorBtn']/button[1]").click()

                self.browser.switch_to.default_content()
                # 进入模版配置列表页面
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("您确定分配当前查询条件下左表所有网元吗", auto_click_ok=False):
                    alert.click_ok()
                    log.info("分配网元成功")
                    set_global_var("ResultMsg", "保存成功", False)
                    page_wait()

                    # 进入对应模版类型配置页面iframe
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                    # 进入绑定网元页面iframe
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, bindNE_iframe_xpath)))
                    sleep(1)
                else:
                    log.warning("保存列配置失败，失败提示: {0}".format(msg))
        else:
            raise KeyError("【{0}】不需要绑定网元")

    def get_table_status(self, table_name):
        """
        # 获取数据当前状态
        :param table_name: 数据表名称
        :return: True/False
        """

        record = self.browser.find_element(
            By.XPATH, "//*[@field='tableNameCh']//*[text()='{0}']/../../..".format(table_name))
        row_index = record.get_attribute("datagrid-row-index")

        # 获取数据当前状态
        js = 'return $(".switchbutton")[{0}].checked;'.format(row_index)
        current_status = self.browser.execute_script(js)
        return current_status

    def update_status(self, table_name, set_status, need_query=True):
        """
        # 更新第一条数据状态
        :param table_name: 数据表名称
        :param set_status: 状态，启用/禁用
        :param need_query: 是否查询
        """
        # 选择表
        if need_query:
            self.search(query={"数据表名称": table_name})
        current_status = self.get_table_status(table_name)

        if set_status == "启用":
            if current_status:
                log.info("{0}已启用".format(table_name))
                set_global_var("ResultMsg", "启用模版成功", False)
            else:
                if self.temp_type == "合并模式":
                    self.browser.find_element(
                        By.XPATH, "//*[text()='{0}']/../../following-sibling::td[4]/div/span".format(table_name)).click()
                else:
                    self.browser.find_element(
                        By.XPATH, "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(table_name)).click()

                alert = BeAlertBox(timeout=5)
                msg = alert.get_msg()
                if alert.title_contains("启用模版成功", auto_click_ok=False):
                    alert.click_cancel()
                    sleep(1)
                    log.info("{0} 启用成功".format(table_name))
                    set_global_var("ResultMsg", "启用模版成功", False)

                    # 进入对应模式配置页面iframe
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                else:
                    log.warning("{0} 启用失败，失败提示: {1}".format(table_name, msg))
                    set_global_var("ResultMsg", msg, False)
        elif set_status == "禁用":
            if current_status:
                if self.temp_type == "合并模式":
                    self.browser.find_element(
                        By.XPATH, "//*[text()='{0}']/../../following-sibling::td[4]/div/span".format(table_name)).click()
                else:
                    self.browser.find_element(
                        By.XPATH, "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(table_name)).click()

                alert = BeAlertBox(timeout=5)
                msg = alert.get_msg()
                if alert.title_contains("您确定禁用所选模版吗", auto_click_ok=False):
                    alert.click_ok()
                    sleep(1)
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("禁用成功"):
                        log.info("{0} 禁用成功".format(table_name))

                        # 进入对应模式配置页面iframe
                        wait = WebDriverWait(self.browser, 30)
                        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                    else:
                        log.warning("{0} 禁用失败，失败提示: {1}".format(table_name, msg))
                else:
                    log.warning("{0} 禁用失败，失败提示: {1}".format(table_name, msg))
                set_global_var("ResultMsg", msg, False)
            else:
                log.info("{0}未启用".format(table_name))
                set_global_var("ResultMsg", "禁用成功", False)
        else:
            raise KeyError("状态只支持启用/禁用，当前值: {0}".format(set_status))

    def delete_table(self, table_name):
        """
        :param table_name: 数据表名称
        """
        log.info("开始删除数据")
        self.search(query={"数据表名称": table_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-del']").click()

        alert = BeAlertBox(timeout=3)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(table_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("{0} 删除成功".format(table_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(table_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(table_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, table_name, fuzzy_match=False):
        """
        :param obj: 数据表名称
        :param fuzzy_match: 模糊匹配
        """
        log.info("开始进行数据清理")
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(
            By.XPATH, self.tab_xpath + "//*[@id='tableName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(
            By.XPATH, self.tab_xpath + "//*[@id='tableName']/following-sibling::span/input[1]").send_keys(table_name)
        # 点击查询
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-query']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'edataTmplTab')]/*[@field='tableNameCh']//*[starts-with(text(),'{0}')]".format(
                    table_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'edataTmplTab')]/*[@field='tableNameCh']//*[text()='{0}']".format(table_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                # 启用状态不允许删除，则先禁用
                current_status = self.get_table_status(search_result)
                if current_status:
                    self.update_status(search_result, "禁用", False)
                    sleep(1)
                else:
                    pe.click()
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-del']").click()
                alert = BeAlertBox()
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("删除成功"):
                        log.info("{0} 删除成功".format(search_result))
                        page_wait()

                        # 进入对应模式配置页面iframe
                        wait = WebDriverWait(self.browser, 30)
                        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.tab_iframe_xpath)))
                        if fuzzy_match:
                            # 重新获取页面查询结果
                            record_element = self.browser.find_elements(
                                By.XPATH, "//*[contains(@id,'edataTmplTab')]/*[@field='tableNameCh']//*[starts-with(text(),'{0}')]".format(
                                    table_name))
                            if len(record_element) > 0:
                                exist_data = True
                            else:
                                # 查询结果为空,修改exist_data为False，退出循环
                                log.info("数据清理完成")
                                exist_data = False
                        else:
                            break
                    else:
                        raise Exception("删除数据时出现未知异常: {0}".format(msg))
                else:
                    # 无权操作
                    log.warning("{0} 清理失败，失败提示: {1}".format(table_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
