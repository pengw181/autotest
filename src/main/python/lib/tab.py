# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:48

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from src.main.python.static.visualmodeler_menu import tab_xpath as visual_tab
from src.main.python.static.crawler_menu import tab_xpath as crawler_tab
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def get_tab_xpath(tab):
    """
    # 获取标签xpath
    :param tab: 标签名
    :return: xpath or None
    """
    application = gbl.service.get("application")
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
        self.browser = gbl.service.get("browser")

        self.table_handles = gbl.service.get("TableHandles")
        if self.table_handles is None:
            self.table_handles = {}

    def save(self, title):

        if title not in self.table_handles.keys():
            self.table_handles[title] = get_tab_xpath(title)
            gbl.service.set("TableHandles", self.table_handles)
            log.info("tab列表增加: %s" % title)
        log.info("当前tab句柄信息: {0}".format(gbl.service.get("TableHandles")))

    def switch(self, title):
        try:
            self.browser.find_element(By.XPATH, self.table_handles.get(title)).click()
            log.info("切换到tab页: {0}".format(title))
        except NoSuchElementException:
            raise "tab {0} 不存在！！！".format(title)
