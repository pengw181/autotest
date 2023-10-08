# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:05

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.upload import upload
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.windows import WindowHandles
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class Database:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("常用信息管理-数据库管理")
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/dbCfg.html')]"))
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

        # 数据库名称
        if query.__contains__("数据库名称"):
            db_name = query.get("数据库名称")
            self.browser.find_element(By.XPATH, "//*[@id='db_name']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='db_name']/following-sibling::span/input[1]").send_keys(db_name)
            select_item = db_name

        # 数据库URL
        if query.__contains__("数据库URL"):
            db_url = query.get("数据库URL")
            self.browser.find_element(By.XPATH, "//*[@id='db_url']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='db_url']/following-sibling::span/input[1]").send_keys(db_url)

        # 数据库驱动
        if query.__contains__("数据库驱动"):
            db_driver = query.get("数据库驱动")
            self.browser.find_element(By.XPATH, "//*[@id='db_driver']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'db_driver') and text()='{0}']".format(db_driver)).click()

        # 归属类型
        if query.__contains__("归属类型"):
            belong_type = query.get("归属类型")
            self.browser.find_element(By.XPATH, "//*[@id='belong_type']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'belong_type') and text()='{0}']".format(belong_type)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
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
                    self.browser.find_element(By.XPATH, "//*[@field='dbName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, db_name, db_driver, db_url, username, pwd, belong_type, data_type):
        """
        :param db_name: 数据库名称
        :param db_driver: 数据库驱动
        :param db_url: 数据库URL
        :param username: 用户名
        :param pwd: 密码
        :param belong_type: 归属类型
        :param data_type: 数据类型
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'dbCfgEdit.html?type=add')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dbName']/preceding-sibling::input")))

        self.database_page(db_name=db_name, db_driver=db_driver, db_url=db_url, username=username, pwd=pwd,
                           belong_type=belong_type, data_type=data_type)
        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitBtn']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(db_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(db_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, db, db_name, db_driver, db_url, username, pwd, belong_type, data_type):
        """
        :param db: 数据库名称
        :param db_name: 数据库名称
        :param db_driver: 数据库驱动
        :param db_url: 数据库URL
        :param username: 用户名
        :param pwd: 密码
        :param belong_type: 归属类型
        :param data_type: 数据类型
        """
        log.info("开始修改数据")
        self.search(query={"数据库名称": db}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'dbCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dbName']/preceding-sibling::input")))

            self.database_page(db_name=db_name, db_driver=db_driver, db_url=db_url, username=username, pwd=pwd,
                               belong_type=belong_type, data_type=data_type)
            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='submitBtn']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(db))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(db, msg))
            gbl.temp.set("ResultMsg", msg)

    def database_page(self, db_name, db_driver, db_url, username, pwd, belong_type, data_type):
        """
        :param db_name: 数据库名称
        :param db_driver: 数据库驱动
        :param db_url: 数据库URL
        :param username: 用户名
        :param pwd: 密码
        :param belong_type: 归属类型
        :param data_type: 数据类型
        """
        # 数据库名称
        if db_name:
            self.browser.find_element(By.XPATH, "//*[@name='dbName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='dbName']/preceding-sibling::input").send_keys(db_name)
            log.info("设置数据库名称: {0}".format(db_name))

        # 数据库驱动
        if db_driver:
            self.browser.find_element(By.XPATH, "//*[@name='dbDriver']/preceding-sibling::input").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'dbDriver') and text()='{0}']".format(db_driver)).click()
            log.info("设置数据库驱动: {0}".format(db_driver))

        # 数据库URL
        if db_url:
            self.browser.find_element(By.XPATH, "//*[@name='dbUrl']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='dbUrl']/preceding-sibling::input").send_keys(db_url)
            log.info("设置数据库URL: {0}".format(db_url))

        # 用户名
        if username:
            self.browser.find_element(By.XPATH, "//*[@name='username']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='username']/preceding-sibling::input").send_keys(username)
            log.info("设置用户名: {0}".format(username))

        # 密码
        if pwd:
            try:
                # 判断是否是修改密码
                self.browser.find_element(
                    By.XPATH, "//*[@id='pwd']/following-sibling::span//a[contains(@class, 'edit')]").click()
            except NoSuchElementException:
                pass
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").send_keys(pwd)
            sleep(1)
            log.info("设置密码: {0}".format(pwd))

        # 归属类型
        if belong_type:
            self.browser.find_element(By.XPATH, "//*[@name='belongType']/preceding-sibling::input").click()
            belong_type = "外部库"
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'belongType') and text()='{0}']".format(belong_type)).click()
            log.info("设置归属类型: {0}".format(belong_type))

        # 数据类型
        if data_type:
            self.browser.find_element(By.XPATH, "//*[@name='dataTypeId']/preceding-sibling::input").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'dataTypeId') and text()='{0}']".format(data_type)).click()
            log.info("设置数据类型: {0}".format(data_type))

    def test(self, db_name):
        """
        :param db_name: 数据库名称
        """
        log.info("开始测试数据")
        self.search(query={"数据库名称": db_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(timeout=2, back_iframe=False)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'dbCfgEdit.html?type=edit')]")))

            self.browser.find_element(By.XPATH, "//*[@id='testBtn']").click()
            alert = BeAlertBox(back_iframe=True, timeout=60)
            msg = alert.get_msg()
            if alert.title_contains("测试成功"):
                log.info("{0} 测试成功".format(db_name))
            else:
                log.warning("{0} 测试失败，测试返回结果: {1}".format(db_name, msg))
            gbl.temp.set("ResultMsg", msg)

    def delete(self, db_name):
        """
        :param db_name: 数据库名称
        """
        log.info("开始删除数据")
        self.search(query={"数据库名称": db_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(db_name), auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} 删除成功".format(db_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(db_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(db_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, db_name, fuzzy_match=False):
        """
        :param db_name: 数据库名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"数据库名称": db_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dbName']//*[starts-with(text(),'{0}')]".format(db_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dbName']//*[text()='{0}']".format(db_name))
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
            self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()
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
                            By.XPATH, "//*[@field='dbName']//*[starts-with(text(),'{0}')]".format(db_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(db_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break


class TableManagement(Database):

    def __init__(self, database_name):
        """
        :param database_name: 数据库名称
        """
        super().__init__()
        self.search(query={"数据库名称": database_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='db-dataMgt']").click()

        # 保存新窗口，并切换到新窗口
        current_win_handle = WindowHandles()
        current_win_handle.save("数据库管理")
        current_win_handle.switch("数据库管理")
        page_wait()
        sleep(1)

    def add_table(self, zh_name, en_name):
        """
        :param zh_name: 数据表名称
        :param en_name: 表英文名
        """
        self.browser.find_element(By.XPATH, "//*[@id='table-add']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'./dbCfg_tableMgr_name.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]")))

        # 数据表名称
        if zh_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(zh_name)
            log.info("设置数据表名称: {}".format(zh_name))

        # 表英文名
        if en_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableNameEn']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameEn']/following-sibling::span/input[1]").send_keys(en_name)
            log.info("设置表英文名: {}".format(en_name))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='tableNameCfg-save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据表添加成功")
        else:
            log.warning("数据表添加失败，失败提示: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def delete_table(self, zh_name):
        """
        :param zh_name: 数据表名称
        """
        self.browser.find_element(By.XPATH, "//*[@id='tableTree']//*[text()='{}']".format(zh_name)).click()
        self.browser.find_element(By.XPATH, "//*[@id='table-del']").click()
        alert = BeAlertBox(timeout=1)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{}吗".format(zh_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("数据表删除成功")
            else:
                log.warning("数据表删除失败，失败提示: {}".format(msg))
        else:
            log.warning("数据表删除失败，失败提示: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def add_cols(self, zh_name, cols):
        """
        :param zh_name: 数据表名称
        :param cols: 列信息，数组
        """
        # 点击表
        self.browser.find_element(By.XPATH, "//*[@id='tableTree']//*[text()='{}']".format(zh_name)).click()
        self.browser.find_element(By.XPATH, "//*[@id='cfg']").click()

        for col in cols:
            table_col_name = col.get("列名(数据库)")
            zh_col_name = col.get("列名(自定义)")
            col_type = col.get("列类型")
            col_length = col.get("长度")
            col_floatNum = col.get("小位数")
            in_data_format = col.get("输入格式")
            out_data_format = col.get("输出格式")

            # 点击添加列
            self.browser.find_element(By.XPATH, "//*[@id='table-column-add']").click()
            self._col_set_page(table_col_name, zh_col_name, col_type, col_length, col_floatNum, in_data_format, out_data_format)

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='colCfg-save']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功", auto_click_ok=False):
                alert.click_ok()
                log.info("列配置成功")
            else:
                log.warning("保存列配置失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

    def edit_col(self, zh_name, obj_col, col_info):
        """
        :param zh_name: 数据表名称
        :param obj_col: 列名(自定义)，必填
        :param col_info: 列信息，字典，一次只能改一个字段
        :return:
        """
        # 点击表
        self.browser.find_element(By.XPATH, "//*[@id='tableTree']//*[text()='{}']".format(zh_name)).click()
        self.browser.find_element(By.XPATH, "//*[@id='cfg']").click()

        zh_col_name = col_info.get("列名(自定义)")
        col_length = col_info.get("长度")
        col_floatNum = col_info.get("小位数")
        in_data_format = col_info.get("输入格式")
        out_data_format = col_info.get("输出格式")

        # 点击目标列
        self.browser.find_element(
            By.XPATH, "//*[@class='colCanBeEdit' and contains(text(),'{0}')]".format(obj_col)).click()
        log.info("选择列名(自定义): {0}".format(obj_col))

        self._col_set_page(None, zh_col_name, None, col_length, col_floatNum, in_data_format, out_data_format)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='colCfg-save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功", auto_click_ok=False):
            alert.click_ok()
            log.info("列配置成功")
        else:
            log.warning("保存列配置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def _col_set_page(self, table_col_name, zh_col_name, col_type, col_length, col_floatNum, in_data_format, out_data_format):
        """
        :param table_col_name: 列名(数据库)
        :param zh_col_name: 列名(自定义)
        :param col_type: 列类型
        :param col_length: 长度
        :param col_floatNum: 小位数
        :param in_data_format: 输入格式
        :param out_data_format: 输出格式
        """

        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'./dbCfg_tableMgr_column.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]")))

        # 列名(数据库)
        if table_col_name:
            self.browser.find_element(By.XPATH, "//*[@id='colNameEn']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='colNameEn']/following-sibling::span/input[1]").send_keys(table_col_name)
            log.info("设置列名(数据库): {}".format(table_col_name))

        # 列名(自定义)
        if zh_col_name:
            self.browser.find_element(By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='colNameCh']/following-sibling::span/input[1]").send_keys(zh_col_name)
            log.info("设置列名(自定义): {}".format(zh_col_name))

        # 列类型
        if col_type:
            self.browser.find_element(
                By.XPATH, "//*[contains(@data-i18n-text, 'db.column.type') and text()='{}']".format(
                    col_type)).click()
            log.info("设置列类型: {}".format(col_type))
            sleep(1)

        # 长度
        if col_length:
            self.browser.find_element(By.XPATH, "//*[@id='colLength']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='colLength']/following-sibling::span/input[1]").send_keys(col_length)
            log.info("设置长度: {}".format(col_length))

        # 小位数
        if col_floatNum:
            self.browser.find_element(
                By.XPATH, "//*[@id='colFloatNum']//a[text()='{}']".format(col_floatNum)).click()
            log.info("设置小位数: {}".format(col_floatNum))

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

    def delete_col(self, zh_name, zh_col_name):
        """
        :param zh_name: 数据表名称
        :param zh_col_name: 列名(自定义)，必填
        """
        # 点击表
        self.browser.find_element(By.XPATH, "//*[@id='tableTree']//*[text()='{}']".format(zh_name)).click()
        self.browser.find_element(By.XPATH, "//*[@id='cfg']").click()

        self.browser.find_element(
            By.XPATH, "//*[@title='{}']/a[contains(@class,'deleteCol')]".format(zh_col_name)).click()
        alert = BeAlertBox(timeout=1)
        msg = alert.get_msg()
        if alert.title_contains("您确定删除列【{}】吗".format(zh_col_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=30)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("列【{}】删除成功".format(zh_col_name))
            else:
                log.warning("列【{}】删除失败，失败提示: {}".format(zh_col_name, msg))
        else:
            log.warning("列【{}】删除失败，失败提示: {}".format(zh_col_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def import_table(self, zh_name, en_name, col_file_name):
        """
        :param zh_name: 数据表名称
        :param en_name: 表英文名
        :param col_file_name: 字段文件名
        """
        self.browser.find_element(By.XPATH, "//*[@id='imp']").click()

        # 数据表名称
        if zh_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableChiName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableChiName']/following-sibling::span/input[1]").send_keys(zh_name)
            log.info("设置数据表名称: {}".format(zh_name))

        # 表英文名
        if en_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableEnName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableEnName']/following-sibling::span/input[1]").send_keys(en_name)
            log.info("设置表英文名: {}".format(en_name))

        # 字段文件名
        if col_file_name:
            upload(file_name=col_file_name, catalog="table", input_id='filebox_file_id_1')
            log.info("设置上传文件: {}".format(col_file_name))

        # 点击表字段上传
        self.browser.find_element(By.XPATH, "//*[@onclick='uploadTableFile()']").click()
        alert = BeAlertBox(timeout=60)
        msg = alert.get_msg()
        if alert.title_contains("操作成功", auto_click_ok=False):
            alert.click_ok()
            log.info("导入模式导入表{}成功".format(zh_name))
        else:
            log.warning("导入模式导入表{}失败，失败提示: {}".format(zh_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, zh_name, fuzzy_match=False):
        """
        :param zh_name: 数据表名称
        :param fuzzy_match: 模糊匹配
        """
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@id='tableTree']//*[starts-with(text(), '{}')]".format(zh_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@id='tableTree']//*[text()='{}']".format(zh_name))
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
            self.browser.find_element(By.XPATH, "//*[@id='table-del']").click()
            alert = BeAlertBox(timeout=1)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(timeout=30)
                msg = alert.get_msg()
                if alert.title_contains("删除成功"):
                    log.info("{0} 删除成功".format(search_result))
                    page_wait()
                    if fuzzy_match:
                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH, "//*[@id='tableTree']//*[starts-with(text(), '{}')]".format(zh_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(zh_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
