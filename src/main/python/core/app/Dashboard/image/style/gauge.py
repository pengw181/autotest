# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:07

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.main.python.lib.css import change_color
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def gauge_style(theme, custom_bg_color, bg_color_rgb, show_title, title_alignment, title_font_size, margin_top,
                margin_left, radius, start_angle, angle, low_threshold, high_threshold, min_value, max_value):
    """
    # 仪表图
    :param theme: 主题样式
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param margin_top: 上边距
    :param margin_left: 左边距
    :param radius: 半径
    :param start_angle: 开始角度
    :param angle: 角度大小
    :param low_threshold: 低阈比例
    :param high_threshold: 高阈比例
    :param min_value: 最小值
    :param max_value: 最大值

    {
        "主题样式": "青春主题",
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "上边距": "50",
        "左边距": "50",
        "半径": "80",
        "开始角度": "250",
        "角度大小": "318",
        "低阈比例": "30",
        "高阈比例": "85",
        "最小值": "10",
        "最大值": "90"
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

    # 上边距
    if margin_top:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.marginTop']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(margin_top) - int(basic_value)) * 2
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.marginTop']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置上边距: {0}".format(margin_top))
        sleep(1)

    # 左边距
    if margin_left:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.marginLeft']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(margin_left) - int(basic_value)) * 2
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.marginLeft']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置左边距: {0}".format(margin_left))
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

    # 开始角度
    if start_angle:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.startAngle']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(start_angle) - int(basic_value)) * (200/359)
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.startAngle']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置开始角度: {0}".format(start_angle))
        sleep(1)

    # 角度大小
    if angle:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.angleSize']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(angle) - int(basic_value)) * (200/359)
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.angleSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置角度大小: {0}".format(angle))
        sleep(1)

    # 低阈比例
    if low_threshold:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.lowThresholdRatio']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(low_threshold) - int(basic_value)) * 2
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.lowThresholdRatio']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置低阈比例: {0}".format(low_threshold))
        sleep(1)

    # 高阈比例
    if high_threshold:
        slider = browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@data-i18n-text='imageCfg.gauge.highThresholdRatio']/following-sibling::div[1]")
        basic_value = slider.get_attribute("innerText")
        x_offset = (int(high_threshold) - int(basic_value)) * 2
        size_slider = browser.find_element(
            By.XPATH, "//*[@data-i18n-text='imageCfg.gauge.highThresholdRatio']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置高阈比例: {0}".format(high_threshold))
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
