# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午4:11

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from service.lib.log.logger import log
from client.page.func.positionPanel import getPanelXpath
from service.lib.variable.globalVariable import *


def choose_ftp_dir(path):
    """
    :param path: 类似根目录-pw-AI
    :return: 点击
    """
    browser = get_global_var("browser")
    path_level = path.split("-")

    panel_xpath = getPanelXpath()
    root_xpath = panel_xpath + "//*[contains(@class,'tree-root-one')]"
    element_xpath = None
    current_depth = 1
    level_xpath = root_xpath
    for level in path_level:

        # path为根目录
        if len(path_level) == 1:
            wait = WebDriverWait(browser, 5)
            wait.until(ec.element_to_be_clickable((By.XPATH, level_xpath)))
            browser.find_element(By.XPATH, level_xpath).click()
            break

        # 展开目录
        # noinspection PyBroadException
        try:
            if current_depth > 1:
                level_xpath += "/following-sibling::ul[1]/li/div/span[text()='{0}']/..".format(level)

            if level != path_level[-1]:
                # 当前非最后一级，点击层级前面的+展开下一级
                element_xpath = level_xpath + "/span[{0}]".format(current_depth)
            else:
                # 当前是最后一级，则点击层级名称
                element_xpath = level_xpath + "/span[text()='{0}']".format(level)
            wait = WebDriverWait(browser, 10)
            wait.until(ec.element_to_be_clickable((By.XPATH, element_xpath)))
            browser.find_element(By.XPATH, element_xpath).click()
            current_depth += 1
        except Exception:
            raise NoSuchElementException("无法找到元素: {0}".format(element_xpath))
    log.info("选择ftp目录: {0}".format("> ".join(path_level)))


def choose_file_dir(dir_name):
    """
    :param dir_name: 目录名
    :return: 点击
    """
    browser = get_global_var("browser")
    dir_element = browser.find_elements(
        By.XPATH, "//*[@class='tree-node']/*[@class='tree-title' and text()='{0}']".format(dir_name))
    for element in dir_element:
        if element.is_displayed():
            browser.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            log.info("选择目录: {0}".format(dir_name))
            break
