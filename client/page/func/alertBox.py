# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:52

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class BeAlertBox:

    def __init__(self, back_iframe=True, timeout=30):
        """
        :param back_iframe: 返回iframe
        :param timeout: 超时时间，秒
        """
        self.browser = get_global_var("browser")
        self.exist_alert = False
        # 弹出框在编辑框的上一层iframe，需要用switch_to.parent_frame()返回上一层iframe
        # 弹出框在最外层，需要使用switch_to.default_content()
        if back_iframe is True:
            self.browser.switch_to.parent_frame()
        elif back_iframe == "default":
            self.browser.switch_to.default_content()
        else:
            pass
        wait = WebDriverWait(self.browser, timeout)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@class='BeAlert_box']")))
            self.exist_alert = True
            sleep(1)
        except TimeoutException:
            # 没有检测到弹出框
            pass

    def get_msg(self):
        msg = self.browser.find_element(By.XPATH, "//div[@class='BeAlert_title']").text
        return msg

    def click_ok(self):
        self.browser.find_element(By.XPATH, "//*[@class='BeAlert_confirm']").click()

    def click_cancel(self):
        self.browser.find_element(By.XPATH, "//*[@class='BeAlert_cancel']").click()

    def title_contains(self, content, auto_click_ok=True):
        msg = self.get_msg()
        log.info("弹出框返回: {0}".format(msg))
        content = content.split("|")    # 支持匹配多个中的任意一个，用竖线分割
        contain = False
        for tmp in content:
            if msg.find(tmp.strip()) > -1:
                if auto_click_ok:
                    self.click_ok()
                contain = True
            else:
                continue
        return contain
