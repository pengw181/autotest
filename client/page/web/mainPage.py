# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:24

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.resource.AiSee.menuXpath import *
from time import sleep
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *
from client.page.func.pageMaskWait import page_wait


class AiSee:

    def __init__(self):
        self.browser = get_global_var("browser")

    def close_tips(self):
        sleep(1)
        try:
            self.browser.find_element(By.XPATH, "//button[@id='closeBtn']").click()
        except NoSuchElementException:
            pass

    def enter_domain(self, belong, domain):

        # belong: 广州市
        # domain: 广州核心网
        self.close_tips()
        text = "{0}>{1}".format(belong, domain)
        try:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.visibility_of_element_located((By.XPATH, "//span[text()='{0}']".format(text))))
            domain_ele = self.browser.find_element(By.XPATH, "//span[text()='{0}']".format(text))
            self.browser.execute_script("arguments[0].click();", domain_ele)
            return True
        except TimeoutError:
            log.error("找不到领域，belong: {0}, domain: {1}".format(belong, domain))
            return False

    def choose_menu_func(self, func):

        # func填写如：用户管理、网元管理
        # 需要进入应用中心的菜单时，需要执行两次函数，一次传应用中心，一次传里面的云平台、告警平台、安全审计
        try:
            self.browser.find_element(By.XPATH, "//*[@class='menu']").click()
            sleep(1)
            self.browser.find_element(By.XPATH, bar_xpath.get(func)).click()
            page_wait()
            sleep(3)
        except NoSuchElementException as e:
            raise e

    def logout(self):

        try:
            self.browser.find_element(By.XPATH, "//*[@title='退出系统']").click()
        except NoSuchElementException as e:
            raise e

    def change_skin(self, color):

        try:
            self.browser.find_element(By.XPATH, "//*[@class='change']").click()
            self.browser.find_element(By.XPATH, "//*[@class='color']/*[text()='{0}']".format(color)).click()
        except NoSuchElementException as e:
            raise e

    def modify_user_info(self, msg):
        # TODO
        try:
            self.browser.find_element(By.XPATH, "//*[@title='用户设置']").click()
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, "../user/portalUserEditWin.html"))

            """
            输入参数进行修改
            """
        except NoSuchElementException:
            raise

    def in_menu(self, menu_name):
        try:
            self.browser.switch_to.default_content()
            self.browser.find_element(
                By.XPATH,  "//*[@id='main']/following-sibling::div[1]//*[text()='{}']".format(menu_name))
            log.info("当前在{}页面".format(menu_name))
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
            in_menu_stats = True
        except NoSuchElementException:
            in_menu_stats = False
        return in_menu_stats
