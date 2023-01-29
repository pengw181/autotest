# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午4:24

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def cmd_node_choose_level(level):
    """
    指令节点选择层级，单选
    :param level: 层级
    :return: 点击
    """
    browser = get_global_var("browser")
    level_path = level.split(",", 1)
    first_level = level_path[0]

    # 先等待3秒,下拉框有时候无法点击
    sleep(3)

    # 等待加载下拉框列表
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((
        By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(first_level))))

    element = browser.find_element(
        By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(first_level))
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    log.info("定位到层级: {0}".format(first_level))
    element.click()
    log.info("点击层级: {0}".format(first_level))
    sleep(1)

    if len(level_path) > 1:
        second_path = level_path[1]

        # 等待加载下拉框列表
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))))

        element = browser.find_element(
            By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        log.info("定位到层级: {0}".format(second_path))
        element.click()
        log.info("点击层级: {0}".format(second_path))
        sleep(1)


def cmd_node_choose_member(member_list):
    """
    指令节点选择层级成员，多选
    :param member_list: 层级成员，数组
    :return: 点击
    """
    browser = get_global_var("browser")
    need_wait = True
    for member in member_list:
        if need_wait:
            wait = WebDriverWait(browser, 30)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[contains(@id,'netunit_id_') and text()='{0}']".format(member))))
            need_wait = False

        ne_element = browser.find_element(By.XPATH, "//*[contains(@id,'netunit_id_') and text()='{0}']".format(member))
        browser.execute_script("arguments[0].scrollIntoView(true);", ne_element)
        action = ActionChains(browser)
        action.click(ne_element).perform()


def cmd_set_choose_level(level_list):
    """
    指令集选择层级，多选
    :param level_list: 层级列表
    :return: 点击
    """
    browser = get_global_var("browser")
    for level in level_list:
        level_path = level.split(",", 1)
        first_level = level_path[0]

        # 先等待3秒,下拉框有时候无法点击
        # sleep(3)

        # 等待加载下拉框列表
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(first_level))))

        try:
            first_level_xpath = "//*[@id='cmdInfoForm']/following-sibling::div[6]//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{}']".format(
                first_level)
            first_level_element = browser.find_element(By.XPATH, first_level_xpath)
            # 如果第一个层级存在，则判断层级是否已展开
            browser.execute_script("arguments[0].scrollIntoView(true);", first_level_element)
            log.info("定位到层级: {0}".format(first_level))
            expanded_element = browser.find_element(By.XPATH, first_level_xpath + "/preceding-sibling::span[3]")
            # 获取展开标识
            expand_class = expanded_element.get_attribute("class")
            # log.info(expand_class)
            if expand_class.find("tree-expanded") == -1:
                # 未展开，点击+展开
                expanded_element.click()
            # 展开后，则判断是否需要点击第二层级
            if len(level_path) > 1:
                # 如果有第二层级，则继续选择第二层级
                second_path = level_path[1]
                # 等待加载下拉框列表
                wait = WebDriverWait(browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH,
                    "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))))
                second_level_element = browser.find_element(
                    By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))
                browser.execute_script("arguments[0].scrollIntoView(true);", second_level_element)
                log.info("定位到层级: {0}".format(second_path))
                second_level_element.click()
                sleep(1)
            else:
                # 如果没有第二层级，则选择整个当前层级
                first_level_element.click()
        except NoSuchElementException:
            raise

        log.info("选择层级: {}".format(level_path))


def choose_level(level_list):
    """
    指令集搜索条件、数据拼盘选择网元分类，多选
    :param level_list: 网元分类，数组
    :return: 点击
    """
    browser = get_global_var("browser")

    # 先勾选取消所有已选项
    tree_selected = browser.find_elements(By.XPATH, "//*[contains(@id,'_tree_') and contains(@class, 'selected')]")
    if len(tree_selected) > 0:
        for element in tree_selected:
            action = ActionChains(browser)
            action.move_to_element(element).click().perform()

    if not isinstance(level_list, list):
        raise KeyError("网元分类需要是数组，每个值的一级和二级层级使用英文逗号分隔")

    for level in level_list:
        level_path = level.split(",", 1)
        first_level = level_path[0]

        # 等待加载下拉框列表
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH,
            "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(first_level))))

        try:
            first_level_xpath = "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{}']".format(
                first_level)
            first_level_element = browser.find_element(By.XPATH, first_level_xpath)
            # 如果第一个层级存在，则判断层级是否已展开
            browser.execute_script("arguments[0].scrollIntoView(true);", first_level_element)
            log.info("定位到层级: {0}".format(first_level))
            expanded_element = browser.find_element(By.XPATH, first_level_xpath + "/preceding-sibling::span[3]")
            # 获取展开标识
            expand_class = expanded_element.get_attribute("class")
            # log.info(expand_class)
            if expand_class.find("tree-expanded") == -1:
                # 未展开，点击+展开
                expanded_element.click()
            # 展开后，则判断是否需要点击第二层级
            if len(level_path) > 1:
                # 如果有第二层级，则继续选择第二层级
                second_path = level_path[1]
                # 等待加载下拉框列表
                wait = WebDriverWait(browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH,
                    "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))))
                second_level_element = browser.find_element(
                    By.XPATH, "//*[contains(@id,'_tree_')]/span[@class='tree-title' and text()='{0}']".format(second_path))
                browser.execute_script("arguments[0].scrollIntoView(true);", second_level_element)
                log.info("定位到层级: {0}".format(second_path))
                second_level_element.click()
                sleep(1)
            else:
                # 如果没有第二层级，则选择整个当前层级
                first_level_element.click()
        except NoSuchElementException:
            raise

        log.info("选择网元分类: {}".format(level_path))
