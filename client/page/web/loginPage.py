# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:28

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.handle.windows import WindowHandles
from client.page.browser.initBrowser import initBrowser
from client.page.func.pageMaskWait import page_wait
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class LoginPage:

    username = (By.ID, "userId")
    password = (By.ID, "password")
    okButton = (By.ID, "loginButton")

    def __init__(self):
        self.browser = initBrowser()
        self.page_url = get_global_var("PageUrl")
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
    log.info("登录用户名：%s, 用户密码：%s" % (get_global_var("LoginUser"), get_global_var("LoginPwd")))
    page_wait()
    sleep(1)
    current_win_handle = WindowHandles()
    current_win_handle.save("首页")
