# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:08

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.core.app.AlarmPlatform.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class TableBelong:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        # 进入菜单
        choose_menu("连接配置-表归属配置")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/dataConfig/tableBelong/tableBelongList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableName']/following-sibling::span[1]/input[1]")))
        page_wait()
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

        # 表名称
        if query.__contains__("表名称"):
            table_name = query.get("表名称")
            self.browser.find_element(By.XPATH, "//*[@name='tableName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='tableName']/preceding-sibling::input[1]").send_keys(
                table_name)
            select_item = table_name

        # 表使用对象
        if query.__contains__("表使用对象"):
            table_object = query.get("表使用对象")
            self.browser.find_element(By.XPATH, "//*[@name='tableObject']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(table_object)).click()

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").send_keys(
                creator)

        # 创建时间
        if query.__contains__("创建时间"):
            begin_time, end_time = query.get("创建时间")
            # 开始时间
            if begin_time:
                self.browser.find_element(By.XPATH, "//*[@name='startDate']/preceding-sibling::span//a").click()
                if isinstance(begin_time, dict):
                    # 间隔，0表示当前，正数表示未来，负数表示过去
                    time_interval = begin_time.get("间隔")
                    # 单位，年、月、天、时、分、秒
                    time_unit = begin_time.get("单位")
                    begin_time = calculation(interval=time_interval, unit=time_unit)
                else:
                    raise AttributeError("开始时间必须是字典")
                set_calendar(date_s=begin_time, date_format='%Y-%m-%d %H:%M:%S')
                log.info("设置创建开始时间: {0}".format(begin_time))

            # 结束时间
            if end_time:
                self.browser.find_element(By.XPATH, "//*[@name='endDate']/preceding-sibling::span//a").click()
                if isinstance(end_time, dict):
                    # 间隔，0表示当前，正数表示未来，负数表示过去
                    time_interval = end_time.get("间隔")
                    # 单位，年、月、天、时、分、秒
                    time_unit = end_time.get("单位")
                    end_time = calculation(interval=time_interval, unit=time_unit)
                else:
                    raise AttributeError("结束时间必须是字典")
                set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
                log.info("设置创建结束时间: {0}".format(end_time))

        # 表周期
        if query.__contains__("表周期"):
            table_period = query.get("表周期")
            self.browser.find_element(By.XPATH, "//*[@name='tablePeriod']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(table_period)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_tb_query']").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
            return
        if need_choose:
            if select_item:
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='tableNameCh']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, database_name, table_en_ame, table_cn_Name, table_object, table_period, remark):
        """
        :param database_name: 数据库名称
        :param table_en_ame: 表英文名称
        :param table_cn_Name: 表中文名称
        :param table_object: 表使用对象
        :param table_period: 表周期
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/tableBelong/addTableBelong.html')]")))
        sleep(1)
        self.table_belong_page(database_name, table_en_ame, table_cn_Name, table_object, table_period, remark)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("数据 {0} 添加成功".format(table_cn_Name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(table_cn_Name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, table, table_cn_Name, remark):
        """
        :param table: 表中文名称
        :param table_cn_Name: 表中文名称
        :param remark: 备注
        """
        self.search(query={"表名称": table}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/tableBelong/addTableBelong.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]")))

        self.table_belong_page(None, None, table_cn_Name, None, None, remark)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("{0} 修改成功".format(table))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(table, msg))
        gbl.temp.set("ResultMsg", msg)

    def table_belong_page(self, database_name, table_en_ame, table_cn_Name, table_object, table_period, remark):
        """
        :param database_name: 数据库名称
        :param table_en_ame: 表英文名称
        :param table_cn_Name: 表中文名称
        :param table_object: 表使用对象
        :param table_period: 表周期
        :param remark: 备注
        """
        # 数据库名称
        if database_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseInfoId']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'databaseInfoId') and text()='{0}']".format(database_name)).click()
            log.info("设置数据库: {0}".format(database_name))

        # 表英文名称
        if database_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameEn']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameEn']/following-sibling::span/input[1]").send_keys(
                table_en_ame)
            log.info("设置表英文名称: {0}".format(table_en_ame))

        # 表中文名称
        if table_cn_Name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(
                table_cn_Name)
            log.info("设置表中文名称: {0}".format(table_cn_Name))

        # 表使用对象
        if table_object:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableObject']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'tableObject') and text()='{0}']".format(table_object)).click()
            log.info("设置表使用对象: {0}".format(table_object))

        # 表周期
        if table_period:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tablePeriod']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'tablePeriod') and text()='{0}']".format(table_period)).click()
            log.info("设置表周期: {0}".format(table_period))

        # 备注
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']")
            set_textarea(remark_textarea, remark)
            log.info("设置备注: {0}".format(remark))

    def delete(self, table_cn_name):
        """
        :param table_cn_name: 表中文名称
        """
        self.search(query={"表名称": table_cn_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(table_cn_name, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(table_cn_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(table_cn_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(table_cn_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, table_cn_name, fuzzy_match=False):
        """
        :param table_cn_name: 服务器名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"表名称": table_cn_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tableNameCh']//*[starts-with(text(),'{}')]".format(table_cn_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tableNameCh']//*[text()='{}']".format(table_cn_name))
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
            self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
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
                            By.XPATH, "//*[@field='tableNameCh']//*[starts-with(text(),'{0}')]".format(table_cn_name))
                        if len(record_element) == 0:
                            # 查询结果为空,修改exist_data为False，退出循环
                            log.info("数据清理完成")
                            exist_data = False
                    else:
                        break
                else:
                    raise Exception("删除数据时出现未知异常: {0}".format(msg))
            else:
                # 无权操作
                log.warning("{0} 清理失败，失败提示: {1}".format(table_cn_name, msg))
                gbl.temp.set("ResultMsg", msg)
