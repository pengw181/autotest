# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:53

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from service.lib.variable.globalVariable import *


def page_wait(interval=0.1, timeout=30):
    """
    # 每页面出现mask元素，是系统增加的一个加载效果，当该元素存在时，表示页面还在加载中
    :param interval: 查询间隔，默认0.1
    :param timeout: 超时时间，默认30秒
    """
    time_count = 0
    browser = get_global_var("browser")
    while time_count <= timeout:
        try:
            browser.find_element(By.XPATH, "//*[@class='datagrid-mask' and @style='display:block']")
            time_count += interval
            sleep(interval)
            continue
        except NoSuchElementException:
            pass

        try:
            browser.find_element(By.XPATH, "//*[contains(@class,'datagrid-mask') and contains(@style,'display: block')]")
            time_count += interval
            sleep(interval)
            continue
        except NoSuchElementException:
            pass

        try:
            browser.find_element(By.XPATH, "//*[@id='loadingDiv']")
            time_count += interval
            sleep(interval)
            continue
        except NoSuchElementException:
            break

    # log.debug("加载%.1f秒" % time_count)
