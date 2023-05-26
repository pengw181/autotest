# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:04

from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class AccountTemp(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        choose_menu(menu="统一账号配置")

        # 切到统一账号管理页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJpAccountTempCfgInfo.html')]")))
        page_wait()
        sleep(1)

    def choose(self, account_temp_name):
        """
        :param account_temp_name: 账号模版名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@id='accountTempName']/following-sibling::span/input[1]")
        input_ele.clear()
        input_ele.send_keys(account_temp_name)
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
        page_wait()
        self.browser.find_element(
            By.XPATH, "//*[@field='accountTempName']//*[@data-mtips='{}']".format(account_temp_name)).click()
        log.info("已选账号模版: {}".format(account_temp_name))

    def add(self, account_temp_name, account_temp_type, remark):
        """
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        """
        self.browser.find_element(By.XPATH, "//*[@id='accountTempName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='accountTempName']/following-sibling::span/input[1]").send_keys(account_temp_name)
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
        page_wait()
        sleep(1)
        try:
            self.browser.find_element(By.XPATH, "//*[@field='accountTempName']//*[text()='{0}']".format(account_temp_name))
            log.info("账号模版【{}】存在，开始修改".format(account_temp_name))
            self.update(obj_account_temp=account_temp_name, account_temp_name=account_temp_name,
                        account_temp_type=account_temp_type, remark=remark)
        except NoSuchElementException:
            log.info("账号模版【{}】不存在，开始添加".format(account_temp_name))
            self.browser.find_element(By.XPATH, "//*[@id='addBtn']//*[text()='添加']").click()
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'midJpAccountTempCfgInfoEdit.html?type=add')]"))
            sleep(1)
            self.account_temp_page(account_temp_name=account_temp_name, account_temp_type=account_temp_type, remark=remark)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def update(self, obj_account_temp, account_temp_name, account_temp_type, remark):
        """
        :param obj_account_temp: 目标账号模版
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        """
        self.choose(account_temp_name=obj_account_temp)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']//*[text()='修改']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到修改账号模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJpAccountTempCfgInfoEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='accountTempName']/preceding-sibling::input")))
            self.account_temp_page(account_temp_name=account_temp_name, account_temp_type=account_temp_type, remark=remark)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def account_temp_page(self, account_temp_name, account_temp_type, remark):
        """
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        """
        # 账号模版名称
        if account_temp_name:
            self.browser.find_element(By.XPATH, "//*[@id='accountTempName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='accountTempName']/following-sibling::span[1]/input[1]").send_keys(account_temp_name)
            log.info("设置账号模版名称: {}".format(account_temp_name))

        # 账号模版类型
        if account_temp_type:
            self.browser.find_element(By.XPATH, "//*[@id='accountType']/following-sibling::span//a").click()
            sleep(1)
            account_type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'accountType') and text()='{}']".format(account_temp_type))
            action = ActionChains(self.browser)
            action.move_to_element(account_type_list).click().perform()
            log.info("设置账号模版类型: {}".format(account_temp_type))

        # 账号模版用途
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置账号模版用途: {}".format(remark))

    def set_account(self, obj_account_temp, operation, account_scope, username, password):
        """
        :param obj_account_temp: 目标账号模版
        :param operation: 账号操作类型，添加/修改/删除
        :param account_scope: 账号作用域
        :param username: 用户名
        :param password: 密码
        """

        self.choose(account_temp_name=obj_account_temp)
        self.browser.find_element(
            By.XPATH, "//*[@data-mtips='{}']/../../../*[@field='accountTempId']//a".format(obj_account_temp)).click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到配置账号页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfo.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='userName']/following-sibling::span[1]/input[1]")))

            account = Account()
            if operation == "添加":
                account.add(username=username, password=password, account_scope=account_scope)
            elif operation == "修改":
                account.update(account_scope=account_scope, username=username, password=password)
            else:
                account.delete(account_scope=account_scope)


class Account(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")

    def add(self, username, password, account_scope):
        """
        :param username: 用户名
        :param password: 密码
        :param account_scope: 账号作用域
        :return:
        """
        log.info("开始添加账号")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
            alert.click_ok()
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfoEdit.html?type=add')]")))
            self.account_page(account_scope=account_scope, username=username, password=password)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def choose(self, account_scope, creator=None):
        """
        :param creator: 创建者
        :param account_scope: 账号作用域
        """
        if account_scope == "私有":
            if creator is None:
                raise KeyError("选择私有账号时，需指定创建者")
            else:
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@data-mtips='私有']/../../following-sibling::td[3]/*[text()='{}']".format(
                            creator)).click()
                except NoSuchElementException:
                    raise KeyError("未找到{}创建的私有账号，请检查账号".format(creator))
        else:
            # 公有
            try:
                self.browser.find_element(By.XPATH, "//*[@data-mtips='公有']").click()
            except NoSuchElementException:
                raise KeyError("未找到公有账号，请检查账号")

    def update(self, account_scope, username, password):
        """
        # 如果作用域是私有，则只修改本人创建的账号
        :param account_scope: 账号作用域
        :param username: 用户名
        :param password: 密码
        """
        log.info("开始修改账号")
        if account_scope == "公有":
            self.choose(account_scope=account_scope)
        else:
            current_user = gbl.service.get("LoginUser")
            self.choose(account_scope=account_scope, creator=current_user)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfoEdit.html?type=edit')]")))
        self.account_page(account_scope=account_scope, username=username, password=password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
            alert.click_ok()
        gbl.temp.set("ResultMsg", msg)

    def account_page(self, account_scope, username, password):
        """
        :param account_scope: 账号作用域
        :param username: 用户名
        :param password: 密码
        """
        # 用户名
        if username:
            self.browser.find_element(By.XPATH, "//*[@name='userName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='userName']/preceding-sibling::input").send_keys(username)
            log.info("设置用户名: {}".format(username))

        # 密码
        if password:
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").send_keys(password)
            log.info("设置密码: {}".format(password))

        # 账号作用域
        if account_scope:
            self.browser.find_element(By.XPATH, "//*[@id='accountScopeId']/following-sibling::span//a").click()
            sleep(1)
            account_type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'accountScopeId') and text()='{}']".format(account_scope))
            action = ActionChains(self.browser)
            action.move_to_element(account_type_list).click().perform()
            log.info("设置账号作用域: {}".format(account_scope))

    def delete(self, account_scope):
        """
        # 如果作用域是私有，则只删除本人创建的账号
        :param account_scope: 账号作用域
        """
        log.info("开始删除账号")
        if account_scope == "公有":
            self.choose(account_scope=account_scope)
            obj_username = self.browser.find_element(By.XPATH, "//*[@data-mtips='公有']/../../following-sibling::td[1]/div")
        else:
            current_user = gbl.service.get("LoginUser")
            self.choose(account_scope=account_scope, creator=current_user)
            obj_username = self.browser.find_element(
                By.XPATH, "//*[@data-mtips='私有']/../../following-sibling::td[3]/*[text()='{}']/../preceding-sibling::td[2]/div".format(
                    current_user))
        username = obj_username.get_attribute("text")
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(username, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(username))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(username, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(username, msg))
        gbl.temp.set("ResultMsg", msg)

    def issue_account(self):
        # 账号下发
        pass
