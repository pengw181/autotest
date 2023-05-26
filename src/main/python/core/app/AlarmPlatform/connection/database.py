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
from src.main.python.core.app.AlarmPlatform.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class DatabaseConfig:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        # 进入菜单
        choose_menu("连接配置-关系型数据库配置")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/dataConfig/databaseInfo/databaseList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='databaseName']/following-sibling::span[1]/input[1]")))
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

        # 数据库名称
        if query.__contains__("数据库名称"):
            database_name = query.get("数据库名称")
            self.browser.find_element(By.XPATH, "//*[@name='databaseName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@name='databaseName']/preceding-sibling::input[1]").send_keys(database_name)
            select_item = database_name

        # 数据库类型
        if query.__contains__("数据库类型"):
            database_type = query.get("数据库类型")
            self.browser.find_element(By.XPATH, "//*[@name='databaseType']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(database_type)).click()

        # 用户名
        if query.__contains__("用户名"):
            database_username = query.get("用户名")
            self.browser.find_element(By.XPATH, "//*[@name='databaseUsername']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='databaseUsername']/preceding-sibling::input[1]").send_keys(
                database_username)

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

        # 查询
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_db_query']").click()
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
                        By.XPATH, "//*[@field='databaseName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, database_type, database_name, database_sid, address, port, username, password):
        """
        :param database_type: 数据库类型
        :param database_name: 数据库名称
        :param database_sid: 服务名/SID
        :param address: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/databaseInfo/addDatabase.html')]")))
        sleep(1)
        self.database_page(database_type, database_name, database_sid, address, port, username, password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("数据 {0} 添加成功".format(database_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(database_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, database, database_type, database_name, database_sid, address, port, username, password):
        """
        :param database: 数据库名称
        :param database_type: 数据库类型
        :param database_name: 数据库名称
        :param database_sid: 服务名/SID
        :param address: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.search(query={"数据库名称": database}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/databaseInfo/addDatabase.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='databaseName']/following-sibling::span/input[1]")))

        self.database_page(database_type, database_name, database_sid, address, port, username, password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 修改成功".format(database))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(database, msg))
        gbl.temp.set("ResultMsg", msg)

    def database_page(self, database_type, database_name, database_sid, address, port, username, password):
        """
        :param database_type: 数据库类型
        :param database_name: 数据库名称
        :param database_sid: 服务名/SID
        :param address: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        # 数据库类型
        if database_type:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseType']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'databaseType') and text()='{0}']".format(database_type)).click()
            log.info("设置数据库类型: {0}".format(database_type))

        # 数据库名称
        if database_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseName']/following-sibling::span/input[1]").send_keys(
                database_name)
            log.info("设置数据库名称: {0}".format(database_name))

        # 服务名/SID
        if database_sid:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseSid']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseSid']/following-sibling::span/input[1]").send_keys(
                database_sid)
            log.info("设置服务名/SID: {0}".format(database_sid))

        # 连接地址
        if address:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseAddress']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseAddress']/following-sibling::span/input[1]").send_keys(
                address)
            log.info("设置连接地址: {0}".format(address))

        # 端口
        if port:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databasePort']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databasePort']/following-sibling::span/input[1]").send_keys(
                port)
            log.info("设置端口: {0}".format(port))

        # 用户名
        if username:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseUsername']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseUsername']/following-sibling::span/input[1]").send_keys(
                username)
            log.info("设置用户名: {0}".format(username))

        # 密码
        if password:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databasePassword']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databasePassword']/following-sibling::span/input[1]").send_keys(
                password)
            sleep(1)
            log.info("设置密码: {0}".format(password))

    def test(self, database_name):
        """
        :param database_name: 数据库名称
        """
        self.search(query={"数据库名称": database_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/databaseInfo/addDatabase.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='databaseName']/following-sibling::span/input[1]")))
        self.browser.find_element(By.XPATH, "//*[@id='testButtonId']//*[text()='测试']").click()
        alert = BeAlertBox(back_iframe=True, timeout=60)
        msg = alert.get_msg()
        if alert.title_contains("测试成功"):
            log.info("{0} 测试成功".format(database_name))
        else:
            log.warning("{0} 测试失败，测试返回结果: {1}".format(database_name, msg))
        gbl.temp.set("ResultMsg", msg)
