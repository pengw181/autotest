# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/11 下午3:02

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.main.python.lib.css import change_color
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def map_style(theme, custom_bg_color, bg_color_rgb, show_title, title_alignment, title_font_size, show_district,
              show_color_bar, min_value, max_value, min_value1, max_value1):
    """
    # 地图
    :param theme: 主题样式
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param show_district: 显示地区名称，是/否
    :param show_color_bar: 显示颜色条，是/否
    :param min_value: 最小值
    :param max_value: 最大值
    :param min_value1: 下级最小值
    :param max_value1: 下级最大值

    {
        "主题样式": "青春主题",
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "显示地区名称": "是",
        "显示颜色条": "是",
        "最小值": "1",
        "最大值": "9999",
        "下级最小值": "1",
        "下级最大值": "1000"
    }
    """
    tab_div_xpath = "//*[@class='dlg-tabsDiv']"
    browser = gbl.service.get("browser")
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

    # 显示地区名称
    if show_district:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='show-label']/following-sibling::span[text()='{0}']".format(
                show_district)).click()
        log.info("设置显示地区名称: {0}".format(show_district))
        sleep(1)

    # 显示颜色条
    if show_color_bar:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='show-visualMap']/following-sibling::span[text()='{0}']".format(
                show_color_bar)).click()
        log.info("设置显示颜色条: {0}".format(show_color_bar))
        sleep(1)

    # 最小值
    if min_value:
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='min']").clear()
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='min']").send_keys(min_value)
        log.info("设置最小值: {0}".format(min_value))
        sleep(1)

    # 最大值
    if max_value:
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='max']").clear()
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='max']").send_keys(max_value)
        log.info("设置最大值: {0}".format(max_value))
        sleep(1)

    # 下级最小值
    if min_value1:
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='min1']").clear()
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='min1']").send_keys(min_value1)
        log.info("设置下级最小值: {0}".format(min_value1))
        sleep(1)

    # 下级最大值
    if max_value1:
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='max1']").clear()
        browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='max1']").send_keys(max_value1)
        log.info("设置下级最大值: {0}".format(max_value1))
        sleep(1)
