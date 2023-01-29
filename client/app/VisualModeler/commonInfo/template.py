# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/1/28 下午6:10

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from client.page.func.pageMaskWait import page_wait
from client.page.func.regular import RegularCube
from client.page.func.alertBox import BeAlertBox
from client.page.func.dateUtil import set_calendar
from client.page.handle.windows import WindowHandles
from client.page.func.upload import upload
from client.page.func.positionPanel import getPanelXpath
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class Template:

    def __init__(self, temp_type):
        """
        :param temp_type: 模版类型
        """
        self.browser = get_global_var("browser")
        self.temp_type = temp_type
        DoctorWho().choose_menu("常用信息管理-网元模版配置")
        # 进入模版配置列表页面
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/zg/zgTempCfg.html')]"))
        page_wait()
        # 切换到对应模版类型
        self.browser.find_element(By.XPATH, "//*[text()='{0}']".format(temp_type)).click()
        log.info("进入 {0}".format(temp_type))
        if self.temp_type == "网元基础信息":
            self.tab_xpath = "//*[@id='tab1']"
        elif self.temp_type == "网元辅助资料":
            self.tab_xpath = "//*[@id='tab2']"
        else:
            self.tab_xpath = "//*[@id='tab3']"
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

        # 模版名称
        if query.__contains__("模版名称"):
            zg_temp_name = query.get("模版名称")
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@name='zgTempName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@name='zgTempName']/preceding-sibling::input[1]").send_keys(
                zg_temp_name)
            select_item = zg_temp_name

        # 数据表名称
        if query.__contains__("数据表名称"):
            zg_table_name = query.get("数据表名称")
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@name='zgTableName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.tab_xpath + "//*[@name='zgTableName']/preceding-sibling::input[1]").send_keys(
                zg_table_name)

        # 查询
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-search-primary')]").click()
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
                        By.XPATH, self.tab_xpath + "//*[@field='zgTempName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add_zg_temp(self, zg_temp_name):
        """
        :param zg_temp_name: 模版名称
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-add')]").click()
        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
        # 进入表名配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'./zgTempWin.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]")))

        # 模版名称
        if zg_temp_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").send_keys(zg_temp_name)
            log.info("设置模版名称: {0}".format(zg_temp_name))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@onclick='saveTable()']//*[text()='保存']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox(timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(zg_temp_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update_zg_temp(self, zg_temp, zg_temp_name):
        """
        :param zg_temp: 模版名称
        :param zg_temp_name: 新模版名称
        """
        log.info("开始修改数据")
        self.search(query={"模版名称": zg_temp}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-edit')]").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            msg = alert.get_msg()
            set_global_var("ResultMsg", msg, False)
        else:
            # 进入表配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
            # 进入表名配置页面
            wait = WebDriverWait(self.browser, 30)
            wait.until(
                ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'./zgTempWin.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]")))

            # 新模版名称
            if zg_temp_name:
                self.browser.find_element(By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").send_keys(zg_temp_name)
                log.info("设置新模版名称: {0}".format(zg_temp_name))

            # 保存
            self.browser.find_element(By.XPATH, "//*[@onclick='saveTable()']//*[text()='保存']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(zg_temp))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(zg_temp, msg))
            set_global_var("ResultMsg", msg, False)

    def col_sets(self, zg_temp_name, col_set):
        """
        :param zg_temp_name: 模版名称
        :param col_set: 列配置，数组
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-edit')]").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
        log.info("开始进行表配置")
        sleep(1)

        for col in col_set:
            col_obj = col.get("配置项")
            opt_type = col.get("操作类型")
            col_name = col.get("列名")
            col_order = col.get("列序号")
            var_name = col.get("业务变量")
            col_type = col.get("数据类型")
            col_length = col.get("长度")
            col_floatNum = col.get("小位数")
            in_data_format = col.get("输入格式")
            out_data_format = col.get("输出格式")
            data_format_regex = col.get("数据校验")

            # 目标列
            if col_obj:
                self.browser.find_element(
                    By.XPATH, "//*[@class='header' and contains(text(),'{0}')]".format(col_obj)).click()
                log.info("选择列: {0}".format(col_obj))
                sleep(1)

            # 操作类型
            if opt_type:
                if opt_type == "添加":
                    self.browser.find_element(By.XPATH, "//*[@onclick='showColBox()']/span/span").click()
                    sleep(1)
                elif opt_type == "修改":
                    # 配置项
                    if col_obj is None:
                        raise KeyError("修改列时需要指定【配置项】")
                    self.browser.find_element(
                        By.XPATH, "//*[@class='header' and contains(text(),'{0}')]".format(col_obj)).click()
                    sleep(1)
                elif opt_type == "删除":
                    # 配置项
                    if col_obj is None:
                        raise KeyError("删除列时需要指定【配置项】")
                    # 点击某列删除按钮
                    self.browser.find_element(
                        By.XPATH, "//*[@class='header' and contains(text(),'{0}')]/following-sibling::a".format(
                            col_obj)).click()
                    alert = BeAlertBox()
                    msg = alert.get_msg()
                    if alert.title_contains("您确定需要删除{0}吗".format(col_obj), auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(timeout=30, back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("删除成功"):
                            log.info("{0} 删除成功".format(col_obj))
                            # 进入表配置页面
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
                        else:
                            log.warning("{0} 删除失败，失败提示: {0}".format(col_obj, msg))
                        set_global_var("ResultMsg", msg, False)
                    else:
                        log.warning("{0} 删除失败，失败提示: {0}".format(col_obj, msg))
                    set_global_var("ResultMsg", msg, False)
                    return
                else:
                    raise KeyError("操作类型 仅支持添加/修改/删除，当前值: {0}".format(opt_type))

            # 列名
            if col_name:
                self.browser.find_element(By.XPATH, "//*[@id='colCname_editCol']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colCname_editCol']/following-sibling::span/input[1]").send_keys(col_name)
                log.info("设置列名: {0}".format(col_name))

            # 列序号
            if col_order:
                self.browser.find_element(By.XPATH, "//*[@id='colOrder_editCol']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colOrder_editCol']/following-sibling::span/input[1]").send_keys(col_order)
                log.info("设置列序号: {0}".format(col_order))

            # 业务变量
            if var_name:
                self.browser.find_element(By.XPATH, "//*[@id='varName_editCol']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='varName_editCol']/following-sibling::span/input[1]").send_keys(var_name)
                log.info("设置业务变量: {0}".format(var_name))

            # 数据类型
            if col_type:
                self.browser.find_element(By.XPATH, "//*[@id='colCls_editCol']/following-sibling::span//a").click()
                sleep(1)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'colCls_editCol') and text()='{0}']".format(col_type)).click()
                log.info("设置数据类型: {0}".format(col_type))
                sleep(1)

            # 长度
            if col_length:
                self.browser.find_element(By.XPATH, "//*[@id='colLength_editCol']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colLength_editCol']/following-sibling::span/input[1]").send_keys(col_length)
                log.info("设置长度: {0}".format(col_length))

            # 小位数
            if col_floatNum:
                self.browser.find_element(By.XPATH, "//*[@id='colFloatNum_editCol']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='colFloatNum_editCol']/following-sibling::span/input[1]").send_keys(col_floatNum)
                log.info("设置小位数: {0}".format(col_floatNum))

            # 输入格式
            if in_data_format:
                time_format = in_data_format[0]
                custom_format = in_data_format[1]
                self.browser.find_element(By.XPATH, "//*[@id='colInFormat']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'colInFormat') and text()='{0}']".format(time_format)).click()
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

            # 数据校验
            if data_format_regex:
                regex_area = self.browser.find_element(By.XPATH, "//*[@id='regexModeDiv']//h3")
                regular_cube = RegularCube()
                self.browser.execute_script("arguments[0].scrollIntoView(true);", regex_area)
                regular_cube.setRegular(set_type=data_format_regex.get("设置方式"),
                                        regular_name=data_format_regex.get("正则模版名称"),
                                        advance_mode=data_format_regex.get("高级模式"),
                                        regular=data_format_regex.get("标签配置"),
                                        expression=data_format_regex.get("表达式"))
                if regular_cube.needJumpIframe:
                    self.browser.switch_to.parent_frame()
                    alert = BeAlertBox()
                    msg = alert.get_msg()
                    if alert.title_contains("成功"):
                        log.info("保存正则模版成功")
                        # 进入表配置页面
                        wait = WebDriverWait(self.browser, 30)
                        wait.until(ec.frame_to_be_available_and_switch_to_it((
                            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
                    else:
                        log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                    set_global_var("ResultMsg", msg, False)
                else:
                    # 返回上层iframe
                    self.browser.switch_to.parent_frame()

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='saveColCfgA']//*[text()='保存']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功", auto_click_ok=False):
                alert.click_ok()
                log.info("列【{0}】配置成功".format(col_name))
                # 进入表配置页面
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
                sleep(1)
            else:
                log.warning("保存列配置失败，失败提示: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)

    def _transfer_col_map(self, cname):
        # 列名与字段名映射关系
        cols = self.browser.find_elements(By.XPATH, "//*[@scope='col']/span")
        col_cnames = []
        for col in cols:
            col_cnames.append(col.get_attribute("innerText"))
        cols = self.browser.find_elements(By.XPATH, "//*[@class='tr_colEname']/td/span")
        col_enames = []
        for col in cols:
            col_enames.append(col.get_attribute("innerText"))
        col_map = {}
        for i in range(len(col_cnames)):
            col_map[col_cnames[i]] = col_enames[i]
        return col_map.get(cname)

    def set_search(self, zg_temp_name, col_list):
        """
        # 搜索条件
        :param zg_temp_name: 模版名称
        :param col_list: 列名列表，中文名
        """
        if not isinstance(col_list, list):
            raise TypeError("列名列表格式错误，需要是数组")

        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-edit')]").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
        sleep(1)

        for col in col_list:
            tmp = self._transfer_col_map(col)
            self.browser.find_element(By.XPATH, "//*[@class='tr_isSearch']//*[@colename='{0}']".format(tmp)).click()
            page_wait()
            log.info("列【{0}】点击搜索条件".format(col))

    def set_null(self, zg_temp_name, col_list):
        """
        # 允许为空
        :param zg_temp_name: 模版名称
        :param col_list: 列名列表，中文名
        """
        if not isinstance(col_list, list):
            raise TypeError("列名列表格式错误，需要是数组")

        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-edit')]").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
        sleep(1)

        for col in col_list:
            tmp = self._transfer_col_map(col)
            self.browser.find_element(By.XPATH, "//*[@class='tr_isNull']//*[@colename='{0}']".format(tmp)).click()
            page_wait()
            log.info("列【{0}】点击允许为空".format(col))

    def set_frozen(self, zg_temp_name, col_list):
        """
        # 是否冻结
        :param zg_temp_name: 模版名称
        :param col_list: 列名列表，中文名
        """
        if not isinstance(col_list, list):
            raise TypeError("列名列表格式错误，需要是数组")

        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-edit')]").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        # 进入表配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgTempCfgEdit.html')]")))
        sleep(1)

        for col in col_list:
            tmp = self._transfer_col_map(col)
            self.browser.find_element(By.XPATH, "//*[@class='tr_isFrozen']//*[@colename='{0}']".format(tmp)).click()
            page_wait()
            log.info("列【{0}】点击是否冻结".format(col))

    def delete_zg_temp(self, zg_temp_name):
        """
        :param zg_temp_name: 模版名称
        """
        log.info("开始删除数据")
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-cancel')]").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(zg_temp_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(zg_temp_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(zg_temp_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, zg_temp_name, fuzzy_match=False):
        """
        :param zg_temp_name: 模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(
            By.XPATH, self.tab_xpath + "//*[@name='zgTempName']/preceding-sibling::input").clear()
        self.browser.find_element(
            By.XPATH, self.tab_xpath + "//*[@name='zgTempName']/preceding-sibling::input").send_keys(zg_temp_name)
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-search-primary')]").click()
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, self.tab_xpath + "//*[@field='zgTempName']/*[starts-with(text(),'{0}')]".format(zg_temp_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, self.tab_xpath + "//*[@field='zgTempName']/*[text()='{0}']".format(zg_temp_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            search_result = pe.text
            pe.click()
            log.info("选择: {0}".format(search_result))
            # 删除
            self.browser.find_element(By.XPATH, self.tab_xpath + "//*[contains(@data-options,'icon-cancel')]").click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("{0} 删除成功".format(search_result))
                    page_wait()
                    if fuzzy_match:
                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH, self.tab_xpath + "//*[@field='zgTempName']/*[starts-with(text(),'{0}')]".format(
                                zg_temp_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(zg_temp_name, msg))
                set_global_var("ResultMsg", msg, False)
                break

    def copy_zg_temp(self, zg_temp_name, copy_name=None):
        """
        # 复制
        :param zg_temp_name: 模版名称
        :param copy_name: 新模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@funcid='DeviceManager2001_copy']").click()

        if copy_name is not None:
            self.browser.find_element(By.XPATH, "//*[@id='copyName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='copyName']/following-sibling::span/input[1]").send_keys(copy_name)
            log.info("设置新模版名称: {0}".format(copy_name))
        self.browser.find_element(By.XPATH, "//*[contains(@class,'icon-ok')]").click()
        alert = BeAlertBox(timeout=30, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("复制成功"):
            log.info("模版 {0} 复制成功".format(zg_temp_name))
        else:
            log.info("模版 {0} 复制失败，失败原因:{1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def push_alarm(self, zg_temp_name):
        """
        # 推送告警
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isAlarm']//a[@excetype='alarmPush']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版推送至告警平台吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("推送成功"):
                log.info("{0} 推送成功".format(zg_temp_name))
            else:
                log.warning("{0} 推送失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 推送失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def sync_alarm(self, zg_temp_name):
        """
        # 同步告警
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isAlarm']//a[@excetype='alarmSync']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版同步至告警平台吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("同步成功"):
                log.info("{0} 同步成功".format(zg_temp_name))
            else:
                log.warning("{0} 同步失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 同步失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def revoke_alarm(self, zg_temp_name):
        """
        # 撤销告警
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isAlarm']//a[@excetype='alarmRevoke']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版从告警平台撤销吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("撤销成功"):
                log.info("{0} 撤销成功".format(zg_temp_name))
            else:
                log.warning("{0} 撤销失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 撤销失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def push_dashboard(self, zg_temp_name):
        """
        # 推送仪表盘
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isDashboardDs']//a[@excetype='dashboardPush']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版推送至仪表盘自定义接口吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("推送成功"):
                log.info("{0} 推送成功".format(zg_temp_name))
            else:
                log.warning("{0} 推送失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 推送失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def sync_dashboard(self, zg_temp_name):
        """
        # 同步告警
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isDashboardDs']//a[@excetype='dashboardSync']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版同步至仪表盘自定义接口吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("同步成功"):
                log.info("{0} 同步成功".format(zg_temp_name))
            else:
                log.warning("{0} 同步失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 同步失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def revoke_dashboard(self, zg_temp_name):
        """
        # 撤销告警
        :param zg_temp_name: 模版名称
        """
        self.search(query={"模版名称": zg_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/../../*[@field='isDashboardDs']//a[@excetype='dashboardRevoke']".format(
                zg_temp_name)).click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定将模版从仪表盘自定义接口撤销吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("撤销成功"):
                log.info("{0} 撤销成功".format(zg_temp_name))
            else:
                log.warning("{0} 撤销失败，失败原因: {1}".format(zg_temp_name, msg))
        else:
            log.warning("{0} 撤销失败，失败原因: {1}".format(zg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)


class ZgDataManage(Template):

    def __init__(self, temp_type, zg_temp_name):
        """
        :param temp_type: 模版类型
        :param zg_temp_name: 模版名称
        """
        current_win_handle = WindowHandles()
        if get_global_var("ZgTempType") != temp_type:
            current_win_handle.close(title="数据管理")
        try:
            current_win_handle.switch("数据管理")
            self.browser = get_global_var("browser")
            self.temp_type = temp_type
            if self.temp_type == "网元基础信息":
                self.tab_xpath = "//*[@id='tab1']"
            elif self.temp_type == "网元辅助资料":
                self.tab_xpath = "//*[@id='tab2']"
            else:
                self.tab_xpath = "//*[@id='tab3']"
        except NoSuchWindowException:
            super().__init__(temp_type)
            self.search(query={"模版名称": zg_temp_name}, need_choose=True)
            # 点击数据管理
            self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@funcid='DeviceManager2001_dm']").click()
            page_wait()

            # 保存新窗口，并切换到新窗口
            current_win_handle.save("数据管理")
            current_win_handle.switch("数据管理")
        finally:
            set_global_var("ZgTempType", self.temp_type)
            page_wait()
            sleep(1)

        self.browser.find_element(By.XPATH, "//*[contains(@class,'tabs-first')]").click()
        page_wait()

    def search_data(self, query, unique=None, need_choose=False):
        """
        :param query: 查询条件
        :param unique: 唯一值，用来确定选择对象，为空选择第一条
        :param need_choose: 是否选择
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件不是字典")
        select_item = None
        for key, value in query.items():
            if isinstance(value, list):
                # 时间或数值类型
                first = value[0]
                # noinspection PyBroadException
                try:
                    second = value[1]
                except Exception:
                    second = None
                col_obj = self.browser.find_element(
                    By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::input[1]".format(key))
                col_class = col_obj.get_attribute("class")
                if col_class.find("datetimebox") > -1:
                    # 时间
                    if first:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]//a".format(
                                key)).click()
                        set_calendar(date_s=first, date_format='%Y-%m-%d %H:%M:%S')
                    if second:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[2]//a".format(
                                key)).click()
                        set_calendar(date_s=second, date_format='%Y-%m-%d %H:%M:%S')
                else:
                    # 数值
                    if first:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]/input[1]".format(
                                key)).clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]/input[1]".format(
                                key)).send_keys(first)
                    if second:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[2]/input[1]".format(
                                key)).clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[2]/input[1]".format(
                                key)).send_keys(second)
            elif isinstance(value, str):
                # 字符类型
                if key == "网元名称":
                    select_item = value
                col_obj = self.browser.find_element(
                    By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::input[1]".format(key))
                col_class = col_obj.get_attribute("class")
                if col_class.find("combobox") > -1:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]//a".format(
                            key)).click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(value)).click()
                else:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]/input[1]".format(
                            key)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@class='col_item']/*[text()='{0}']/following-sibling::span[1]/input[1]".format(
                            key)).send_keys(value)
            self.browser.find_element(By.XPATH, "//*[@id='tb']//*[contains(@data-options,'icon-search-primary')]").click()
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
                        By.XPATH, "//*[@field='NETUNIT_NAME']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add_data(self, data_info):
        """
        # 一次添加一条
        :param data_info: 数据信息
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgDataManageEdit.html')]")))
        sleep(1)
        if not isinstance(data_info, list):
            raise KeyError("数据格式错误，不是数组")
        self.data_page(data_info=data_info)

        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据保存成功")
        else:
            log.warning("数据保存失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def update_data(self, netunit_name, data_info):
        """
        # 修改数据，目前仅网元基础信息适用
        :param netunit_name: 网元名称
        :param data_info: 数据信息
        """
        self.search_data(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'zgDataManageEdit.html')]")))
        sleep(1)
        if not isinstance(data_info, list):
            raise KeyError("数据格式错误，不是数组")
        self.data_page(data_info=data_info)

        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据保存成功")
        else:
            log.warning("数据保存失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def data_page(self, data_info):
        """
        :param data_info: 数据信息
        """
        for data in data_info:
            if not isinstance(data, list):
                raise KeyError("数据格式错误，不是数组")
            col_name = data[0]
            col_value = data[1]
            if col_name in ["网元类型", "生产厂家", "设备型号", "业务状态"]:
                col_type = "combobox"
            else:
                col_type = "input"
            if col_type == "input":
                self.browser.find_element(
                    By.XPATH, "//*[@id='editDiv']//*[contains(text(),'{0}')]/../following-sibling::div[1]/span/input[1]".format(
                        col_name)).clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='editDiv']//*[contains(text(),'{0}')]/../following-sibling::div[1]/span/input[1]".format(
                        col_name)).send_keys(col_value)
            elif col_type == "combobox":
                self.browser.find_element(By.XPATH, "//*[@id='editDiv']//*[text()='{0}']/../following-sibling::div[1]//a".format(
                    col_name)).click()
                panel_xpath = getPanelXpath()
                self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(col_value)).click()
            log.info("{0} 设置值 {1}".format(col_name, col_value))

    def delete_data(self, query):
        """
        # 删除满足条件的所有数据
        :param query: 查询条件
        """
        if self.temp_type == "网元其它资料":
            if query:
                self.search_data(query=query)
            data = self.browser.find_elements(By.XPATH, "//*[@type='checkbox' and @name='ck']")
            for row in data:
                row.click()
        else:
            self.search_data(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要批量删除吗|您确定需要删除", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("数据删除成功")
            else:
                log.warning("数据删除失败，失败提示: {0}".format(msg))
        else:
            log.warning("数据删除失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def upload(self, file_path):
        """
        # 导入
        :param file_path: 文件路径
        """
        # 点击导入
        self.browser.find_element(By.XPATH, "//*[@id='importBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/upload/uploadBatchImport.html')]")))
        sleep(1)

        # 导入
        upload(file_name=file_path)
        self.browser.find_element(By.XPATH, "//*[@id='submitImport']").click()
        page_wait(timeout=300)

        # 获取导入结果
        result_box = self.browser.find_element(By.XPATH, "//*[@class='r-box']")
        result = result_box.get_attribute("innerText")
        log.info("导入结果: {0}".format(result))
        set_global_var("ResultMsg", result, False)

    def download_templ(self):
        # 下载导入模版
        self.browser.find_element(By.XPATH, "//*[@id='importBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/upload/uploadBatchImport.html')]")))
        sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='downloadTmplBtn']").click()

    def download(self):
        # 导出
        self.browser.find_element(By.XPATH, "//*[contains(@data-options,'icon-export')]").click()

    def clear(self):
        # 网元其它资料清空
        self.browser.find_element(By.XPATH, "//*[@id='clear']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除全部数据吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("删除成功")
            else:
                log.warning("删除失败，失败原因: {0}".format(msg))
        else:
            log.warning("删除失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)


class DoubleConfirm(ZgDataManage):

    # 网元基础信息使用

    def __init__(self, temp_type, zg_temp_name):
        super().__init__(temp_type, zg_temp_name)
        self.browser.find_element(By.XPATH, "//*[contains(@class,'tabs-last')]").click()
        page_wait()

    def search_data(self, query, unique=None, need_choose=False):
        """
        :param query: 查询条件，字典
        :param unique: 唯一值，用来确定选择对象，为空选择第一条
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None

        # 网元名称
        if query.__contains__("网元名称"):
            ne_name = query.get("网元名称")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='netunitName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='netunitName']/preceding-sibling::input[1]").send_keys(ne_name)
            select_item = ne_name

        # 网元IP
        if query.__contains__("网元IP"):
            ne_ip = query.get("网元IP")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='netunitIp']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='netunitIp']/preceding-sibling::input[1]").send_keys(ne_ip)

        # 状态
        if query.__contains__("状态"):
            operate = query.get("状态")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='operaType']/preceding-sibling::span[1]//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'combobox') and text()='{0}']".format(operate)).click()

        # 网元类型
        if query.__contains__("网元类型"):
            level = query.get("网元类型")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='levelId']/preceding-sibling::span[1]//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'combobox') and text()='{0}']".format(level)).click()

        # 厂家
        if query.__contains__("厂家"):
            vendor = query.get("厂家")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='vendorId']/preceding-sibling::span[1]//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'combobox') and text()='{0}']".format(vendor)).click()

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//*[@name='netunitModelId']/preceding-sibling::span[1]//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'combobox') and text()='{0}']".format(model)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='tb2']//*[contains(@data-options,'icon-search-primary')]").click()
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
                        By.XPATH, "//*[@field='netunitName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def confirm_selected(self, ne_list, query=None):
        """
        # 确认所选
        :param ne_list: 网元列表
        :param query: 查询条件
        """
        if query is not None:
            self.search_data(query=query)
        for ne in ne_list:
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']/following-sibling::div//*[@field='netunitName']//*[text()='{0}']".format(
                    ne)).click()
        self.browser.find_element(By.XPATH, "//*[@id='confirmSelect']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定要确认所选吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确认成功"):
                log.info("确认成功")
            else:
                log.warning("确认失败，失败原因: {0}".format(msg))
        else:
            log.warning("确认失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def confirm_all(self, query=None):
        """
        # 确认全部
        :param query: 查询条件
        """
        if query is not None:
            self.search_data(query=query)

        self.browser.find_element(By.XPATH, "//*[@id='confirmAll']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定要确认全部吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确认成功"):
                log.info("确认成功")
            else:
                log.warning("确认失败，失败原因: {0}".format(msg))
        else:
            log.warning("确认失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def revoke_selected(self, ne_list, query=None):
        """
        # 撤销所选
        :param ne_list: 网元列表
        :param query: 查询条件
        """
        if query is not None:
            self.search_data(query=query)
        for ne in ne_list:
            self.browser.find_element(
                By.XPATH, "//*[@id='tb2']//following-sibling::div//*[@field='netunitName']//*[text()='{0}']".format(
                    ne)).click()
        self.browser.find_element(By.XPATH, "//*[@id='revokeSelect']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定要撤销所选吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("撤销成功"):
                log.info("撤销成功")
            else:
                log.warning("撤销失败，失败原因: {0}".format(msg))
        else:
            log.warning("撤销失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def revoke_all(self, query=None):
        """
        # 撤销全部
        :param query: 查询条件
        """
        if query is not None:
            self.search_data(query=query)

        self.browser.find_element(By.XPATH, "//*[@id='revokeAll']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定要撤销全部吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("撤销成功"):
                log.info("撤销成功")
            else:
                log.warning("撤销失败，失败原因: {0}".format(msg))
        else:
            log.warning("撤销失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)
