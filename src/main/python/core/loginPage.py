# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:28

import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.windows import WindowHandles
from src.main.python.lib.browser import initBrowser
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class LoginPage:

    username = (By.ID, "userId")
    password = (By.ID, "password")
    okButton = (By.ID, "loginButton")

    def __init__(self):
        chrome_driver_path = gbl.service.get("chromeDriverPath")
        download_path = os.path.dirname(os.path.dirname(__file__)) + '/download/'
        self.browser = initBrowser(chrome_driver_path, download_path)
        gbl.service.set("browser", self.browser)
        self.page_url = gbl.service.get("PageUrl")
        self.browser.get(self.page_url)
        self.browser.maximize_window()

        # https高级
        if str(self.page_url).startswith("https"):
            self.browser.find_element(
                By.XPATH, "//*[text()='返回安全连接']/following-sibling::button[2][contains(text(),'高级')]").click()
            self.browser.find_element(By.XPATH, "//*[@id='proceed-link']").click()

        # 等待页面加载
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='autoLoadImg_companyInLogin']")))

    def set_username(self, username):
        name = self.browser.find_element(*LoginPage.username)
        name.send_keys(username)

    def set_password(self, password):
        pwd = self.browser.find_element(*LoginPage.password)
        pwd.send_keys(password)

    def click_ok(self):
        button = self.browser.find_element(*LoginPage.okButton)
        button.click()

    def get_login_status(self):
        try:
            self.browser.find_element(*LoginPage.username)
            status = False
        except NoSuchElementException:
            status = True
        return status


def login(username, password):

    # 是否关闭谷歌进程, IOS下无效，Windows下可以关闭所有谷歌进程
    # os.app('TASKKILL /F /IM chrome.exe 1>nul')

    login_action = LoginPage()
    login_action.set_username(username)
    login_action.set_password(password)
    login_action.click_ok()
    log.info("#######################欢迎登录AiSee系统#######################")
    log.info("登录用户名：%s, 用户密码：%s" % (gbl.service.get("LoginUser"), gbl.service.get("LoginPwd")))
    page_wait()
    sleep(1)
    current_win_handle = WindowHandles()
    current_win_handle.save("首页")
