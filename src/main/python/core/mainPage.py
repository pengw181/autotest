# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:24

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.static.aisee_menu import *
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class AiSee:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        page_wait()

    def close_tips(self):
        """
        # 关闭提示
        """
        sleep(1)
        try:
            self.browser.find_element(By.XPATH, "//button[@id='closeBtn']").click()
        except NoSuchElementException:
            pass

    def enter_domain(self, belong, domain):
        """
        # 进入领域
        :param belong: 归属，如广州市
        :param domain: 领域，如广州核心网
        :return:
        """
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

    def choose_menu_func(self, menu):
        """
        :param menu: 填写如：用户管理、网元管理，或应用中心-云平台
        """
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@class='menu']")))
        sleep(1)
        self.browser.find_element(By.XPATH, "//*[@class='menu']").click()
        sleep(1)
        menu_list = menu.split("-")
        for m in menu_list:
            self.browser.find_element(By.XPATH, bar_xpath.get(m)).click()
            log.info("Menu菜单点击【{0}】".format(m))
        page_wait()

    def logout(self):

        self.browser.find_element(By.XPATH, "//*[@title='退出系统']").click()

    def change_skin(self, color):

        self.browser.find_element(By.XPATH, "//*[@class='change']").click()
        self.browser.find_element(By.XPATH, "//*[@class='color']/*[text()='{0}']".format(color)).click()

    def modify_user_info(self, user_info):
        """
        # 设置用户信息
        :param user_info: 用户信息
        :return:
        """
        # TODO
        self.browser.find_element(By.XPATH, "//*[@title='用户设置']").click()
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, "../user/portalUserEditWin.html"))

        """
        输入参数进行修改
        """

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
