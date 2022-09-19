# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:48

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from app.VisualModeler.main.menu.tabXpath import tab_xpath as visual_tab
from app.Crawler.main.menu.tabXpath import tab_xpath as crawler_tab
from common.variable.globalVariable import *
from common.log.logger import log


def get_tab_xpath(tab):
    """
    # 获取标签xpath
    :param tab: 标签名
    :return: xpath or None
    """
    application = get_global_var("Application")
    if application == "VisualModeler":
        tab_xpath = visual_tab
    elif application == "Crawler":
        tab_xpath = crawler_tab
    else:
        tab_xpath = None
    result = tab_xpath.get(tab)
    if result is None:
        raise Exception("tab标签【(0)】未定义".format(tab))
    return result


class TabHandles:

    def __init__(self):
        self.browser = get_global_var("browser")

        self.table_handles = get_global_var("TableHandles")
        if self.table_handles is None:
            self.table_handles = {}

    def save(self, title):

        if title not in self.table_handles.keys():
            self.table_handles[title] = get_tab_xpath(title)
            set_global_var("TableHandles", self.table_handles)
            log.info("tab列表增加: %s, %s" % (title, get_tab_xpath(title)))
        log.info("当前tab句柄信息: {0}".format(get_global_var("TableHandles")))

    def switch(self, title):
        try:
            self.browser.find_element(By.XPATH, self.table_handles.get(title)).click()
            log.info("切换到tab页: {0}，{1}".format(title, self.table_handles.get(title)))
        except NoSuchElementException:
            raise "tab {0} 不存在！！！".format(title)
