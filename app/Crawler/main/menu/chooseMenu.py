# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/10 下午5:58

from common.page.handle.tab import TabHandles
from .menuXpath import *
from common.log.logger import log
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from common.variable.globalVariable import *


def get_menu_xpath(level, menu):
    """
    # 获取菜单xpath
    :param level: 层级，first/second
    :param menu: 菜单名
    :return: xpath or None
    """
    if level == "first":
        xpath_object = first_menu_xpath
    else:
        xpath_object = second_menu_xpath

    result = xpath_object.get(menu)
    if result is None:
        raise Exception("菜单【{0}】未定义".format(menu))
    return result


def choose_menu(menu_path):
    browser = get_global_var("browser")
    menu_list = str(menu_path).split("-")
    first_menu = menu_list[0]
    second_menu = menu_list[1]
    current_tab_handle = TabHandles()

    try:
        first_menu_element = browser.find_element_by_xpath(get_menu_xpath("first", first_menu))
        browser.execute_script("arguments[0].scrollIntoView(true);", first_menu_element)
        first_menu_element.click()
        log.info("点击一级菜单: {0}".format(first_menu))
        sleep(1)

        if second_menu:
            second_menu_element = browser.find_element_by_xpath(get_menu_xpath("second", second_menu))
            browser.execute_script("arguments[0].scrollIntoView(true);", second_menu_element)
            second_menu_element.click()
            log.info("点击二级菜单: {0}".format(second_menu))
            current_tab_handle.save(second_menu)
            current_tab_handle.switch(second_menu)
            sleep(1)

        return True
    except NoSuchElementException:
        return False
