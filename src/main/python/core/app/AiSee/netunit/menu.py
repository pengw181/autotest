# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/28 下午4:09

from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def choose_domain(domain):
    browser = gbl.service.get("browser")
    page_wait(timeout=120)

    # 点击领域选择下拉按钮
    browser.find_element(By.XPATH, "//*[@id='domainTree']/following-sibling::span//a").click()
    sleep(1)

    # 选择领域
    browser.find_element(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(domain)).click()
    log.info("归属领域选择: {}".format(domain))

    # 等待页面加载网元信息列表
    page_wait(timeout=120)
    sleep(1)


def choose_menu(menu):
    browser = gbl.service.get("browser")
    # 进入网元管理，系统自动加载网元列表，等待页面加载
    page_wait(timeout=120)
    # 选择菜单
    browser.find_element(By.XPATH, "//*[contains(@id,'menuTree')]/*[text()='{}']".format(menu)).click()
    sleep(1)
    log.info("选择菜单: {}".format(menu))
