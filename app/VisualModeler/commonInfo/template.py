# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/1/28 下午6:10

from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from time import sleep
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.page.func.regular import RegularCube
from common.log.logger import log
from common.variable.globalVariable import *


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
            self.tab_id = "tab1"
        elif self.temp_type == "网元辅助资料":
            self.tab_id = "tab2"
        else:
            self.tab_id = "tab3"
        sleep(1)

    def choose(self, table_name):
        """
        :param table_name: 表名
        """
        self.browser.find_element(
            By.XPATH, "//*[@id='{0}']//*[@name='zgTempName']/preceding-sibling::input".format(self.tab_id)).clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='{0}']//*[@name='zgTempName']/preceding-sibling::input".format(
                self.tab_id)).send_keys(table_name)
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='查询']".format(self.tab_id)).click()
        page_wait()
        self.browser.find_element(
            By.XPATH, "//*[@id='{0}']//*[@field='zgTempName']/*[text()='{1}']".format(self.tab_id, table_name)).click()
        log.info("已选择: {0}".format(table_name))

    def add_table(self, table_name):
        """
        :param table_name: 表名
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='添加']".format(self.tab_id)).click()
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

        # 表名
        if table_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").send_keys(table_name)
            log.info("设置表名: {0}".format(table_name))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@onclick='saveTable()']//*[text()='保存']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox(timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(table_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(table_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update_table(self, obj, table_name):
        """
        :param obj: 表名
        :param table_name: 表名
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='修改']".format(self.tab_id)).click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
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

            # 表名
            if table_name:
                self.browser.find_element(By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='zgTempName']/following-sibling::span/input[1]").send_keys(table_name)
                log.info("设置表名: {0}".format(table_name))

            # 保存
            self.browser.find_element(By.XPATH, "//*[@onclick='saveTable()']//*[text()='保存']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(obj))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
            set_global_var("ResultMsg", msg, False)

    def col_sets(self, table_name, col_set):
        """
        :param table_name: 表名
        :param col_set: 列配置，数组
        """
        self.choose(table_name)
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='修改']".format(self.tab_id)).click()

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

    def delete_table(self, obj):
        """
        :param obj: 表名
        """
        log.info("开始删除数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='删除']".format(self.tab_id)).click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: 表名
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(
            By.XPATH, "//*[@id='{0}']//*[@name='zgTempName']/preceding-sibling::input".format(self.tab_id)).clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='{0}']//*[@name='zgTempName']/preceding-sibling::input".format(self.tab_id)).send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='查询']".format(self.tab_id)).click()
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@id='{0}']//*[@field='zgTempName']/*[starts-with(text(),'{1}')]".format(self.tab_id, obj))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@id='{0}']//*[@field='zgTempName']/*[text()='{1}']".format(self.tab_id, obj))
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
            self.browser.find_element(By.XPATH, "//*[@id='{0}']//*[text()='删除']".format(self.tab_id)).click()
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
                            By.XPATH, "//*[@id='{0}']//*[@field='zgTempName']/*[starts-with(text(),'{1}')]".format(
                                self.tab_id, obj))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(obj, msg))
                set_global_var("ResultMsg", msg, False)
                break
