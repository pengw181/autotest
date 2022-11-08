# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:08

from selenium.common.exceptions import NoSuchElementException
from service.lib.variable.globalVariable import *
from client.page.func.pageMaskWait import page_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.resource.AlarmPlatform.chooseMenu import choose_menu
from client.page.func.alertBox import BeAlertBox
from time import sleep
from service.lib.log.logger import log


class DatabaseConfig:

    def __init__(self):
        self.browser = get_global_var("browser")
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

    def choose(self, database_name):
        """
        :param database_name: 数据库名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@id='databaseName']/following-sibling::span[1]/input[1]")
        input_ele.clear()
        input_ele.send_keys(database_name)
        self.browser.find_element(By.XPATH, "//span[text()='查询']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='databaseName']//a[text()='{}']".format(database_name)).click()
        log.info("已选择数据库: {}".format(database_name))

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
        self.browser.find_element(By.XPATH, "//*[@id='databaseName']/following-sibling::span[1]/input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='databaseName']/following-sibling::span[1]/input[1]").send_keys(database_name)
        self.browser.find_element(By.XPATH, "//*[text()='查询']").click()
        page_wait()
        sleep(1)
        try:
            self.browser.find_element(By.XPATH, "//*[@field='databaseName']//a[text()='{}']".format(database_name))
            log.info("数据库【{}】已存在，开始修改".format(database_name))
            self.update(database_name, database_type, database_name, database_sid, address, port, username, password)
        except NoSuchElementException:
            log.info("数据库【{}】不存在，开始添加".format(database_name))
            self.browser.find_element(By.XPATH, "//*[@id='addBtn']//*[text()='添加']").click()
            page_wait()
            self.browser.switch_to.parent_frame()
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/databaseInfo/addDatabase.html')]")))
            sleep(1)
            self.database_page(database_type, database_name, database_sid, address, port, username, password)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("数据 {0} 添加成功".format(database_name))
            else:
                log.warning("数据 {0} 添加失败，失败提示: {1}".format(database_name, msg))
            set_global_var("ResultMsg", msg, False)

    def update(self, obj, database_type, database_name, database_sid, address, port, username, password):
        """
        :param obj: 数据库名称
        :param database_type: 数据库类型
        :param database_name: 数据库名称
        :param database_sid: 服务名/SID
        :param address: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/databaseInfo/addDatabase.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='databaseName']/following-sibling::span/input[1]")))

        self.database_page(database_type, database_name, database_sid, address, port, username, password)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 修改成功".format(obj))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

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

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']//*[text()='提交']").click()

    def test(self, database_name):
        """
        :param database_name: 数据库名称
        """
        log.info("开始修改数据")
        self.choose(database_name)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
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
        set_global_var("ResultMsg", msg, False)
