# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:05

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.func.alertBox import BeAlertBox
from client.page.func.pageMaskWait import page_wait
from client.page.func.positionPanel import getPanelXpath
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class Database:

    def __init__(self):
        self.browser = get_global_var("browser")
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
            set_global_var("ResultMsg", msg, False)
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
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(db_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(db_name, msg))
        set_global_var("ResultMsg", msg, False)

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
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'dbCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dbName']/preceding-sibling::input")))

            self.database_page(db_name=db_name, db_driver=db_driver, db_url=db_url, username=username, pwd=pwd,
                               belong_type=belong_type, data_type=data_type)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(db))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(db, msg))
            set_global_var("ResultMsg", msg, False)

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

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitBtn']//*[text()='提交']").click()

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
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'dbCfgEdit.html?type=edit')]")))

            self.browser.find_element(By.XPATH, "//*[@id='testBtn']//*[text()='测试']").click()
            alert = BeAlertBox(back_iframe=True, timeout=60)
            msg = alert.get_msg()
            if alert.title_contains("测试成功"):
                log.info("{0} 测试成功".format(db_name))
            else:
                log.warning("{0} 测试失败，测试返回结果: {1}".format(db_name, msg))
            set_global_var("ResultMsg", msg, False)

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
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, db_name, fuzzy_match=False):
        """
        :param db_name: 数据库名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='dbName']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='dbName']/preceding-sibling::input").send_keys(db_name)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dbName']/*[contains(@class,'dbName') and starts-with(text(),'{0}')]".format(db_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dbName']/*[contains(@class,'dbName') and text()='{0}']".format(db_name))
        if len(record_element) > 0:
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
                                By.XPATH, "//*[@field='dbName']/*[contains(@class,'dbName') and text()='{0}']".format(
                                    db_name))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(db_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
