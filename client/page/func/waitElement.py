# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:24

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from service.lib.variable.globalVariable import *


class WaitElement:

    def __init__(self, timeout=30):
        self.browser = get_global_var("browser")
        self.timeout = timeout

    def visible(self, xpath):
        wait = WebDriverWait(self.browser, self.timeout)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise

    def clickable(self, xpath):
        wait = WebDriverWait(self.browser, self.timeout)
        try:
            wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            raise

    def value_present(self, xpath, text):
        wait = WebDriverWait(self.browser, self.timeout)
        try:
            wait.until(ec.text_to_be_present_in_element_value(("xpath", xpath), text))
        except TimeoutException:
            raise

    def switch_iframe(self, xpath):
        wait = WebDriverWait(self.browser, self.timeout)
        try:
            wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, xpath)))
        except TimeoutException:
            raise

    def wait_element(self, xpath):
        exist = None
        time_count = 0
        while not exist:
            if time_count < self.timeout:
                element_collection = self.browser.find_elements(By.XPATH, xpath)
                if len(element_collection) > 0:
                    for element in element_collection:
                        if element.is_displayed():
                            # 元素存在且可见
                            exist = element
                            break
                else:
                    time_count += 0.5
                    sleep(0.5)
            else:
                raise NoSuchElementException("找不到元素, xpath: {0}".format(xpath))
        return exist

    def until_displayed(self, xpath):
        element = None
        elements = self.browser.find_elements(By.XPATH, xpath)
        if len(elements) == 0:
            element = None
        for e in elements:
            if e.is_displayed():
                element = e
                break
        return element
