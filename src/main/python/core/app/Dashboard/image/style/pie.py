# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:05

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from src.main.python.lib.css import change_color
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def pie_style(theme, custom_theme_colors, custom_bg_color, bg_color_rgb, pie, pie_radius, pie_outer_radius,
              pie_inner_radius, show_legend, legend_direction, legend_align, legend_font_size, show_title,
              title_alignment, title_font_size, legend_sortable):
    """
    # 饼状图
    :param theme: 主题样式
    :param custom_theme_colors: 自定义主题色彩，数组，#00008B
    :param custom_bg_color: 自定义背景颜色，是/否
    :param bg_color_rgb: 背景颜色，#00008B
    :param pie: 饼图样式，饼图/环形图/玫瑰图
    :param pie_radius: 半径
    :param pie_outer_radius: 外半径
    :param pie_inner_radius: 内半径
    :param show_legend: 是否显示图例，显示/隐藏
    :param legend_direction: 图例标示方向，横向/竖向
    :param legend_align: 图例对齐方式，左对齐/居中/右对齐
    :param legend_font_size: 图例字体大小
    :param show_title: 是否显示标题，显示/隐藏
    :param title_alignment: 标题对齐方式，左对齐/居中/右对齐
    :param title_font_size: 标题字体大小
    :param legend_sortable: 启用图例拖拽排序，开启/关闭

    {
        "主题样式": "自定义主题",
        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080"],
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "饼图样式": "饼图",
        "半径": "90",
        "是否显示图例": "显示",
        "图例标示方向": "横向",
        "图例对齐方式": "居中",
        "图例字体大小": "20",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "启用图例拖拽排序": "开启"
    }
    
    {
        "主题样式": "自定义主题",
        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080"],
        "自定义背景颜色": "是",
        "背景颜色": "#f1f1f1",
        "饼图样式": "环形图",
        "外半径": "75",
        "内半径": "35",
        "是否显示图例": "显示",
        "图例标示方向": "横向",
        "图例对齐方式": "居中",
        "图例字体大小": "20",
        "是否显示标题": "显示",
        "标题对齐方式": "右对齐",
        "标题字体大小": "26",
        "启用图例拖拽排序": "开启"
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

    # 饼图样式
    if pie:
        browser.find_element(By.XPATH, "//*[@name='pie-style']/following-sibling::span[text()='{0}']".format(pie)).click()
        log.info("设置饼图样式: {0}".format(pie))
        sleep(1)

    # 半径
    if pie_radius:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='pie-radius']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(pie_radius) - int(basic_value)) * 2
        size_slider = browser.find_element(By.XPATH, "//*[@id='pie-radius']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置半径: {0}".format(pie_radius))
        sleep(1)

    # 外半径
    if pie_outer_radius:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='pie-outer-radius']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(pie_outer_radius) - int(basic_value)) * 2
        size_slider = browser.find_element(By.XPATH, "//*[@id='pie-outer-radius']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置外半径: {0}".format(pie_outer_radius))
        sleep(1)

    # 内半径
    if pie_inner_radius:
        slider = browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='pie-inner-radius']")
        basic_value = slider.get_attribute("value")
        x_offset = (int(pie_inner_radius) - int(basic_value)) * 2
        size_slider = browser.find_element(By.XPATH, "//*[@id='pie-inner-radius']/following-sibling::div[1]//a")
        action.drag_and_drop_by_offset(size_slider, x_offset, 0).perform()
        log.info("设置内半径: {0}".format(pie_inner_radius))
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

    # 启用图例拖拽排序
    if legend_sortable:
        # 获取当前选中状态
        js = "return $('#legendSortable')[0].checked;"
        status = browser.execute_script(js)
        log.info("【启用图例拖拽排序】状态: {0}".format(status))

        tmp = True if legend_sortable == "开启" else False
        if tmp ^ status:
            browser.find_element(By.XPATH, tab_div_xpath + "//*[@id='legendSortable']").click()
            log.info("{0}启用图例拖拽排序".format(legend_sortable))
            sleep(1)
