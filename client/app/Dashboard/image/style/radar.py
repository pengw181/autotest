# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:07

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from client.page.script.css import change_color
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


def radar_style(theme, custom_bg_color, bg_color_rgb, show_legend, legend_direction, legend_align, legend_font_size,
                show_title, title_alignment, title_font_size, radius, min_value, max_value):
    """
    # 雷达图
    :param theme: 主题样式
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param show_legend: 是否显示图例，显示/隐藏
    :param legend_direction: 图例标示方向，横向/竖向
    :param legend_align: 图例对齐方式，左对齐/居中/右对齐
    :param legend_font_size: 图例字体大小
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param radius: 半径
    :param min_value: 最小值
    :param max_value: 最大值

    {
        "主题样式": "自定义主题",
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "是否显示图例": "显示",
        "图例标示方向": "横向",
        "图例对齐方式": "居中",
        "图例字体大小": "20",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "半径": "70",
        "最小值": "1",
        "最大值": "50"
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

    # 是否显示图例
    if show_legend:
        browser.find_element(
            By.XPATH, "//*[@name='legend-visible']/following-sibling::span[text()='{0}']".format(show_legend)).click()
        log.info("设置是否显示图例: {0}".format(show_legend))
        sleep(1)

    # 图例标示方向
    if legend_direction:
        browser.find_element(
            By.XPATH, "//*[@name='legend-direction']/following-sibling::span[text()='{0}']".format(
                legend_direction)).click()
        log.info("设置图例标示方向: {0}".format(legend_direction))
        sleep(1)

    # 图例对齐方式
    if legend_align:
        browser.find_element(
            By.XPATH, "//*[@name='legend-align']/following-sibling::span[text()='{0}']".format(legend_align)).click()
        log.info("设置图例对齐方式: {0}".format(legend_align))
        sleep(1)

    # 图例字体大小
    if legend_font_size:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='legendFontSize']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(legend_font_size) - int(basic_value)) * 5
        size_slider = browser.find_element(By.XPATH, "//*[@id='legendFontSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置图例字体大小: {0}".format(legend_font_size))
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

    # 半径
    if radius:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.radius']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(radius) - int(basic_value)) * 2
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.radius']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置半径: {0}".format(radius))
        sleep(1)

    # 最小值
    if min_value:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.minValue']/following-sibling::input[1]").clear()
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.minValue']/following-sibling::input[1]").send_keys(
            min_value)
        log.info("设置最小值: {0}".format(min_value))
        sleep(1)

    # 最大值
    if max_value:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.maxValue']/following-sibling::input[1]").clear()
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.maxValue']/following-sibling::input[1]").send_keys(
            max_value)
        log.info("设置最大值: {0}".format(max_value))
        sleep(1)
