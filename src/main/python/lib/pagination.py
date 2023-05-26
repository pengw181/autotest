# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/19 下午4:00

import re
from time import sleep
from pykeyboard import PyKeyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.lib.pageMaskWait import page_wait


class Pagination:

    def __init__(self, table_xpath):
        self.browser = gbl.service.get("browser")
        self.table_xpath = table_xpath

    def get_total_page_num(self):
        total_page = self.browser.find_element(By.XPATH, self.table_xpath + "//td[8]/span").get_attribute("innerHTML")
        patt = r'共(\d+)页'
        match_info = re.match(patt, str(total_page))
        total_page_num = match_info.group(1)
        log.info("当前列表有{0}页".format(total_page_num))
        return int(total_page_num)

    def get_total_num(self):
        total_num = self.browser.find_element(
            By.XPATH, self.table_xpath + "/following-sibling::div[1]").get_attribute("innerHTML")
        patt = r'显示(\d+)到(\d+),共(\d+)记录'
        match_info = re.match(patt, str(total_num))
        total_num = match_info.group(3)
        log.info("总共有{0}条".format(total_num))
        return int(total_num)

    def next_page(self):
        next_click = self.browser.find_element(By.XPATH, self.table_xpath + "//td[10]/a")
        if next_click.get_attribute("class").find("disabled") > -1:
            log.info("当前是最后一页，不能再点击下一页")
        else:
            next_click.click()
            log.info("点击下一页")
            sleep(1)

    def pre_page(self):
        pre_click = self.browser.find_element(By.XPATH, self.table_xpath + "//td[4]/a")
        if pre_click.get_attribute("class").find("disabled") > -1:
            log.info("当前是第一页，不能再点击上一页")
        else:
            pre_click.click()
            log.info("点击上一页")
            sleep(1)

    def set_page_size(self, size):
        try:
            self.browser.find_element(By.XPATH, self.table_xpath + "//td[1]/select").click()
            wait = WebDriverWait(self.browser, 1)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, self.table_xpath + "//td[1]//option[text()='{0}']".format(size))))
            self.browser.find_element(By.XPATH, self.table_xpath + "//td[1]//option[text()='{0}']".format(size)).click()
            log.info("设置每页{0}条".format(size))
            page_wait(10)
        except NoSuchElementException:
            option_pool = self.browser.find_elements(By.XPATH, self.table_xpath + "//td[1]/select/option")
            size_pool = []
            for option in option_pool:
                size_pool.append(option.get_attribute("text"))
            log.error("每页大小支持：{0}".format(','.join(size_pool)))
            raise

    def step_to_page(self, page_index=1):
        total_page_num = self.get_total_page_num()
        if page_index > total_page_num:
            log.info("当前列表总共有{0}页".format(total_page_num))
            page_index = total_page_num
        try:
            self.browser.find_element(By.XPATH, self.table_xpath + "//td[7]/input").clear()
            self.browser.find_element(By.XPATH, self.table_xpath + "//td[7]/input").send_keys(page_index)
            k = PyKeyboard()
            k.press_keys(['Return'])
            log.info("进入第{0}页".format(page_index))
            sleep(1)
        except NoSuchElementException:
            raise
