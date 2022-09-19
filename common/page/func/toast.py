# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/14 上午11:08

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.variable.globalVariable import *
from common.log.logger import log
from time import sleep


class Toast:

    def __init__(self, timeout=10):
        self.browser = get_global_var("browser")
        count_times = 0
        while True:
            if count_times < timeout:
                try:
                    self.browser.find_element(By.XPATH, "//*[@id='toast-container']//*[@class='toast-message']")
                    self.exist = True
                    break
                except NoSuchElementException:
                    count_times += 0.5
                    sleep(0.5)
            else:
                self.exist = False
                break

    def get_msg(self):
        msg_elements = self.browser.find_elements(By.XPATH, "//*[@id='toast-container']//*[@class='toast-message']")
        if len(msg_elements) > 0:
            # 取最后一条信息
            msg = msg_elements[-1].text
        else:
            msg = msg_elements[0].text
        return msg

    def msg_contains(self, content):
        msg = self.get_msg()
        log.info("Toast-container返回: {0}".format(msg))
        content = content.split("|")  # 支持匹配多个中的任意一个，用竖线分割
        contain = False
        for tmp in content:
            if msg.find(tmp.strip()) > -1:
                contain = True
            else:
                continue
        return contain

    def waitUntil(self, timeout=20):
        count_times = 0
        while True:
            if count_times < timeout:
                try:
                    self.browser.find_element(By.XPATH, "//*[@id='toast-container']//*[@class='toast-message']")
                    count_times += 1
                    sleep(1)
                except NoSuchElementException:
                    break
            else:
                break
