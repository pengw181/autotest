# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:07

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.page.script.css import change_color
from selenium.common.exceptions import NoSuchElementException
from common.variable.globalVariable import *
from common.log.logger import log


def table_style(theme, custom_bg_color, bg_color_rgb, show_title, title_alignment, title_font_size, page_size,
                col_align, col_width, frozen_column):
    """
    # 数据表格
    :param theme: 主题样式
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param page_size: 每页展示条数
    :param col_align: 列对齐方式
    :param col_width: 列宽度
    :param frozen_column: 冻结列

    {
        "主题样式": "青春主题",
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "每页展示条数": "50",
        "列对齐方式": "居中",
        "列宽度": "自适应列宽",
        "冻结列": "名称"
    }
    """
    tab_div_xpath = "//*[@class='dlg-tabsDiv']"
    browser = get_global_var("browser")
    action = ActionChains(browser)
    # 主题样式
    if theme:
        browser.find_element(By.XPATH, tab_div_xpath + "//*[text()='主题样式']/following-sibling::div[1]/div").click()
        browser.find_element(By.XPATH, tab_div_xpath + "//*[text()='{0}']".format(theme)).click()
        log.info("设置主题样式: {0}".format(theme))
        sleep(1)

    # 自定义背景颜色
    if custom_bg_color:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='whetherCustomBgColor']/following-sibling::span[text()='{0}']".format(
                custom_bg_color)).click()
        log.info("设置自定义背景颜色: {0}".format(custom_bg_color))
        sleep(1)

    # 背景颜色
    if bg_color_rgb:
        change_color(browser, bg_color_rgb)
        log.info("设置背景颜色: {0}".format(bg_color_rgb))
        sleep(1)

    # 是否显示标题
    if show_title:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='title-show']/following-sibling::span[text()='{0}']".format(
                show_title)).click()
        log.info("设置是否显示标题: {0}".format(show_title))
        sleep(1)

    # 标题对齐方式
    if title_alignment:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='title-align']/following-sibling::span[text()='{0}']".format(
                title_alignment)).click()
        log.info("设置标题对齐方式: {0}".format(title_alignment))
        sleep(1)

    # 标题字体大小
    if title_font_size:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='title-fontSize']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(title_font_size) - int(basic_value)) * 5    # 每个步进值5个像素
        size_slider = browser.find_element(By.XPATH, "//*[@id='title-fontSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置标题字体大小: {0}".format(title_font_size))
        sleep(1)

    # 每页展示条数
    if page_size:
        browser.find_element(By.XPATH, "//*[text()='每页展示条数']/following-sibling::span//a").click()
        ps_elements = browser.find_elements(By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(page_size))
        if len(ps_elements) == 0:
            raise NoSuchElementException
        for element in ps_elements:
            if element.is_displayed():
                element.click()
                log.info("选择每页展示条数: {0}".format(page_size))
                sleep(1)
                break

    # 列对齐方式
    if col_align:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='col-align']/following-sibling::span[text()='{0}']".format(
                col_align)).click()
        log.info("设置列对齐方式: {0}".format(col_align))
        sleep(1)

    # 列宽度
    if col_width:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='col-width']/following-sibling::span[text()='{0}']".format(
                col_width)).click()
        log.info("设置列宽度: {0}".format(col_width))
        sleep(1)

    # 冻结列
    if frozen_column:
        browser.find_element(By.XPATH, "//*[text()='冻结列']/following-sibling::span//a").click()
        fc_elements = browser.find_elements(
            By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(frozen_column))
        if len(fc_elements) == 0:
            raise NoSuchElementException
        for element in fc_elements:
            if element.is_displayed():
                element.click()
                log.info("选择冻结列: {0}".format(frozen_column))
                sleep(1)
                break
