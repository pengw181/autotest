# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/27 上午11:27

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.static.alarmplatform_menu import *


def choose_menu(menu_path):
    browser = gbl.service.get("browser")
    menu_list = str(menu_path).split("-")
    first_menu = menu_list[0]
    if len(menu_list) > 1:
        second_menu = menu_list[1]
    else:
        second_menu = None

    # 一级菜单
    wait = WebDriverWait(browser, 10)
    wait.until(ec.element_to_be_clickable((By.XPATH, first_menu_xpath.get(first_menu))))
    browser.find_element(By.XPATH, first_menu_xpath.get(first_menu)).click()
    log.info("点击一级菜单: {0}".format(first_menu))
    sleep(1)

    # 二级菜单
    if second_menu:
        wait = WebDriverWait(browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, second_menu_xpath.get(second_menu))))
        browser.find_element(By.XPATH, second_menu_xpath.get(second_menu)).click()
        log.info("点击二级菜单: {0}".format(second_menu))
        sleep(1)

    # try:
    #     browser.find_element(By.XPATH, first_menu_xpath.get(first_menu)).click()
    #     log.info("点击一级菜单: {0}".format(first_menu))
    #     sleep(1)
    #
    #     if second_menu:
    #         second_menu_element = browser.find_element(By.XPATH, second_menu_xpath.get(second_menu))
    #         browser.execute_script("arguments[0].scrollIntoView(true);", second_menu_element)
    #         second_menu_element.click()
    #         log.info("点击二级菜单: {0}".format(second_menu))
    #         sleep(1)
    #
    #     return True
    # except NoSuchElementException as e:
    #     log.error("找不到菜单, {}".format(str(e)))
    #     return False
