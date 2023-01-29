# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:04

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from client.page.script.css import change_color
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def bar_style(theme, custom_theme_colors, custom_bg_color, bg_color_rgb, data_dis_direction, show_metrics,
              metrics_font_size, show_title, title_alignment, title_font_size, axis_name_font_size,
              axis_tick_label_font_size, x_axis_area_zoom, y_axis_area_zoom, image_type, area_fill_color):
    """
    # 柱状图
    :param theme: 主题样式
    :param custom_theme_colors: 自定义主题色彩，数组，#00008B
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param data_dis_direction: 数据展示方向，横向/竖向
    :param show_metrics: 是否显示度量，显示/隐藏
    :param metrics_font_size: 度量字体大小
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param axis_name_font_size: 坐标轴名称字体大小
    :param axis_tick_label_font_size: 坐标轴刻度标签字体大小
    :param x_axis_area_zoom: X轴区域缩放，字典
    :param y_axis_area_zoom: Y轴区域缩放，字典
    :param image_type: 图像类型，柱状图/折线图
    :param area_fill_color: 区域填充颜色，填充/不填充

    {
        "主题样式": "自定义主题",
        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080"],
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "数据展示方向": "竖向",
        "是否显示度量": "显示",
        "度量字体大小": "15",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "坐标轴名称字体大小": "20",
        "坐标轴刻度标签字体大小": "17",
        "X轴区域缩放": {
            "状态": "开启",
            "X轴起始百分比": "20",
            "X轴结束百分比": "75"
        },
        "Y轴区域缩放": {
            "状态": "开启",
            "Y轴起始百分比": "30",
            "Y轴结束百分比": "100"
        },
        "图像类型": "折线图",
        "区域填充颜色": "填充"
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

    # 自定义主题色彩
    if custom_theme_colors:
        if not isinstance(custom_theme_colors, list):
            raise TypeError("【自定义主题色彩】格式不是数组")
        for colors in custom_theme_colors:
            browser.find_element(By.XPATH, tab_div_xpath + "//*[@name='border-color']").send_keys(colors)
            browser.find_element(By.XPATH, tab_div_xpath + "//*[@title='增加自定义主题色彩']").click()
            log.info("设置自定义主题色彩: {0}".format(colors))
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

    # 数据展示方向
    if data_dis_direction:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='data-direction']/following-sibling::span[text()='{0}']".format(
                data_dis_direction)).click()
        log.info("设置数据展示方向: {0}".format(data_dis_direction))
        sleep(1)

    # 是否显示度量
    if show_metrics:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[@name='showMeasure']/following-sibling::span[text()='{0}']".format(
                show_metrics)).click()
        log.info("设置是否显示度量: {0}".format(show_metrics))

    # 度量字体大小
    if metrics_font_size:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='labelFontSize']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(metrics_font_size) - int(basic_value)) * 5
        size_slider = browser.find_element(By.XPATH, "//*[@id='labelFontSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置度量字体大小: {0}".format(metrics_font_size))
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

    # 坐标轴名称字体大小
    if axis_name_font_size:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='nameTextStyle-fontSize']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(axis_name_font_size) - int(basic_value)) * 5
        size_slider = browser.find_element(By.XPATH, "//*[@id='nameTextStyle-fontSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置坐标轴名称字体大小: {0}".format(axis_name_font_size))
        sleep(1)

    # 坐标轴刻度标签字体大小
    if axis_tick_label_font_size:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='axisLabel-fontSize']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(axis_tick_label_font_size) - int(basic_value)) * 5
        size_slider = browser.find_element(By.XPATH, "//*[@id='axisLabel-fontSize']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置坐标轴刻度标签字体大小: {0}".format(axis_tick_label_font_size))
        sleep(1)

    # X轴区域缩放
    if x_axis_area_zoom:
        xAxis_status = x_axis_area_zoom.get("状态")
        xAxis_start = x_axis_area_zoom.get("X轴起始百分比")
        xAxis_end = x_axis_area_zoom.get("X轴结束百分比")

        # 获取当前选中状态
        js = "return $('#xDataZoomCfg')[0].checked;"
        status = browser.execute_script(js)
        log.info("【X轴区域缩放】状态: {0}".format(status))

        tmp = True if xAxis_status == "开启" else False
        if tmp ^ status:
            browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='xDataZoomCfg']").click()
            log.info("{0}X轴区域缩放".format(xAxis_status))
            sleep(1)

        # X轴起始百分比
        if xAxis_start:
            slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='xAxis_start']")
            basic_value = slider.get_attribute("value")
            x_offset = (int(xAxis_start) - int(basic_value)) * 2
            size_slider = browser.find_element(By.XPATH, "//*[@id='xAxis_start']/following-sibling::div[1]//a")
            action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
            log.info("设置X轴起始百分比: {0}".format(xAxis_start))
            sleep(1)

        # X轴结束百分比
        if xAxis_end:
            slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='xAxis_end']")
            basic_value = slider.get_attribute("value")
            x_offset = (int(xAxis_end) - int(basic_value)) * 2
            size_slider = browser.find_element(By.XPATH, "//*[@id='xAxis_end']/following-sibling::div[1]//a")
            action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
            log.info("设置X轴结束百分比: {0}".format(xAxis_end))
            sleep(1)

    # Y轴区域缩放
    if y_axis_area_zoom:
        yAxis_status = y_axis_area_zoom.get("状态")
        yAxis_start = y_axis_area_zoom.get("Y轴起始百分比")
        yAxis_end = y_axis_area_zoom.get("Y轴结束百分比")

        # 获取当前选中状态
        js = "return $('#yDataZoomCfg')[0].checked;"
        status = browser.execute_script(js)
        log.info("【Y轴区域缩放】状态: {0}".format(status))

        tmp = True if yAxis_status == "开启" else False
        if tmp ^ status:
            browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='yDataZoomCfg']").click()
            log.info("{0}Y轴区域缩放".format(yAxis_status))
            sleep(1)

        # Y轴起始百分比
        if yAxis_start:
            slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='yAxis_start']")
            basic_value = slider.get_attribute("value")
            x_offset = (int(yAxis_start) - int(basic_value)) * 2
            size_slider = browser.find_element(By.XPATH, "//*[@id='yAxis_start']/following-sibling::div[1]//a")
            action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
            log.info("设置Y轴起始百分比: {0}".format(yAxis_start))
            sleep(1)

        # Y轴结束百分比
        if yAxis_end:
            slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='yAxis_end']")
            basic_value = slider.get_attribute("value")
            x_offset = (int(yAxis_end) - int(basic_value)) * 2
            size_slider = browser.find_element(By.XPATH, "//*[@id='yAxis_end']/following-sibling::div[1]//a")
            action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
            log.info("设置Y轴结束百分比: {0}".format(yAxis_end))
            sleep(1)

    # 图像类型
    if image_type:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[text()='图像类型']/following-sibling::div[1]//*[text()='{0}']".format(
                image_type)).click()
        log.info("设置图像类型: {0}".format(image_type))
        sleep(1)

    # 区域填充颜色
    if area_fill_color:
        browser.find_element(
            By.XPATH, tab_div_xpath + "//*[text()='区域填充颜色']/following-sibling::label[1]//*[text()='{0}']".format(
                area_fill_color)).click()
        log.info("设置区域填充颜色: {0}".format(area_fill_color))
        sleep(1)
