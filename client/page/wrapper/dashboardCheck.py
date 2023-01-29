# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/26 上午10:54

from time import sleep
from selenium.webdriver.common.by import By
from client.page.script.css import setVisible
from service.lib.variable.globalVariable import get_global_var


# 关闭并进入仪表盘配置页面
def closeAndEnterDashboard(func):
    def wrapper(*args, **kwargs):
        browser = get_global_var("browser")
        while True:
            # noinspection PyBroadException
            try:
                sleep(1)
                browser.find_element(By.XPATH, "//*[@class='tabs-title' and text()='仪表盘列表']")
                break
            except Exception:
                class_name = "index-menu"
                setVisible(browser, class_name)
                browser.find_element(By.XPATH, "//*[@class='index-menu']/a[@class='close']").click()
        return func(*args, **kwargs)
    return wrapper
