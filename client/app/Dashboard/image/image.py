# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/4/21 上午10:49

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.func.pageMaskWait import page_wait
from client.page.func.alertBox import BeAlertBox
from client.page.func.toast import Toast
from client.page.wrapper.dashboardCheck import closeAndEnterDashboard
from client.app.Dashboard.image.util.imageType import getImageType
from client.app.Dashboard.image.style.bar import bar_style
from client.app.Dashboard.image.style.line import line_style
from client.app.Dashboard.image.style.pie import pie_style
from client.app.Dashboard.image.style.gauge import gauge_style
from client.app.Dashboard.image.style.radar import radar_style
from client.app.Dashboard.image.style.table import table_style
from client.app.Dashboard.image.style.rectangle import rectangle_style
from client.app.Dashboard.image.style.map import map_style
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


@closeAndEnterDashboard
class Image:

    def __init__(self):
        self.browser = get_global_var("browser")
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='可视化图像列表']")))
        self.browser.find_element(By.XPATH, "//*[text()='可视化图像列表']").click()
        log.info("进入可视化图像列表页面")
        self.image_type = None
        sleep(1)

    def add(self, image_name, catalog, interface, image_type, data_source, style):
        """
        # 添加
        :param image_name: 图像名称
        :param catalog: 主题分类
        :param interface: 数据接口
        :param image_type: 图像类型
        :param data_source: 数据源配置，字典
        :param style: 样式配置，字典
        """
        # 等待页面加载
        page_wait()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@title='添加可视化图像']")))
        self.browser.find_element(By.XPATH, "//*[@title='添加可视化图像']").click()
        sleep(1)

        # 图像名称
        if image_name:
            self.browser.find_element(By.XPATH, "//*[@id='add-name']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='add-name']").send_keys(image_name)
            log.info("设置图像名称: {0}".format(image_name))

        # 主题分类
        if catalog:
            self.browser.find_element(By.XPATH, "//*[@id='catalog']/following-sibling::span//a").click()
            sleep(1)
            self.browser.find_element(By.XPATH, "//*[contains(@id,'catalog') and text()='{0}']".format(catalog)).click()
            log.info("设置主题分类: {0}".format(catalog))

        # 数据接口
        if interface:
            self.browser.find_element(By.XPATH, "//*[@name='interface']/preceding-sibling::span//a").click()
            sleep(1)
            i_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(interface))
            if len(i_elements) == 0:
                raise NoSuchElementException
            for element in i_elements:
                if element.is_displayed():
                    element.click()
                    log.info("选择数据接口: {0}".format(interface))
                    break
            sleep(1)

        # 图像类型
        if image_type:
            imageTypeExistFlag = False
            while not imageTypeExistFlag:
                # noinspection PyBroadException
                try:
                    self.browser.find_element(By.XPATH, "//*[@title='{0}']/img".format(image_type)).click()
                    imageTypeExistFlag = True
                except Exception:
                    next_button = self.browser.find_element(By.XPATH, "//*[@id='addDlg']/form/div/div[5]/div[3]")
                    next_clickable = next_button.get_attribute("class")
                    if next_clickable.find("swiper-button-disabled") == -1:
                        next_button.click()
            if imageTypeExistFlag:
                log.info("设置图像类型: {0}".format(image_type))
                self.image_type = getImageType(image_type)
            else:
                raise NoSuchElementException("找不到图像类型: {0}".format(image_type))

        # 点击下一步
        self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
        toast = Toast(timeout=1)
        if toast.exist:
            msg = toast.get_msg()
            log.warning("msg")
            set_global_var("ResultMsg", msg, False)
            return
        page_wait(10)

        # 数据源配置
        if data_source:
            self.browser.find_element(By.XPATH, "//li[text()='数据源配置']").click()
            if not isinstance(data_source, dict):
                raise TypeError('数据源配置不是字典格式')
            self.data_source_set(y_set=data_source.get("y轴"), x_set=data_source.get("x轴"), region=data_source.get("区域"),
                                 g_info=data_source.get("分组"), col_legend=data_source.get("数据列"),
                                 r_set=data_source.get("排序"), filter_set=data_source.get("数据过滤"),
                                 escape=data_source.get("字典转义"))

        # 点击下一步
        self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
        toast = Toast(timeout=3)
        if toast.exist:
            log.info(toast.get_msg())
            toast.waitUntil()

        # 样式配置
        if style:
            self.browser.find_element(By.XPATH, "//li[text()='样式配置']").click()
            self.style_set(style=style)

        toast = Toast(10)
        toast.waitUntil()
        # 保存
        self.browser.find_element(By.XPATH, "//*[@class='imageCfg']/following-sibling::div//*[text()='保存']").click()
        toast = Toast(3)
        msg = toast.get_msg()
        set_global_var("ResultMsg", msg, False)

    def data_source_set(self, y_set, x_set, region, g_info, col_legend, r_set, filter_set, escape):
        """
        # 数据源配置
        :param y_set: y轴
        :param x_set: x轴
        :param region: 区域
        :param g_info: 分组
        :param col_legend: 数据列
        :param r_set: 排序
        :param filter_set: 数据过滤
        :param escape: 字典转义
        """
        # y轴
        if y_set:
            y_num = 1
            for y in y_set:

                col_name = y.get("度量")
                custom_name = y.get("自定义名称")
                measuring_unit = y.get("度量单位")

                # 选择度量
                if col_name:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='Y轴']/../following-sibling::div[{0}]/div//a".format(
                            y_num)).click()
                    y_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(col_name))
                    if len(y_elements) == 0:
                        raise NoSuchElementException
                    for element in y_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择度量: {0}".format(col_name))
                            break

                # 设置自定义名称
                if custom_name:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='Y轴']/../following-sibling::div[{0}]/div[2]//input".format(
                            y_num)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='Y轴']/../following-sibling::div[{0}]/div[2]//input".format(
                            y_num)).send_keys(custom_name)
                    log.info("设置自定义名称: {0}".format(custom_name))

                # 设置度量单位
                if measuring_unit:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='Y轴']/../following-sibling::div[{0}]/div[3]//input".format(
                            y_num)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='Y轴']/../following-sibling::div[{0}]/div[3]//input".format(
                            y_num)).send_keys(measuring_unit)
                    log.info("设置度量单位: {0}".format(measuring_unit))
                    sleep(1)

                # 添加下一个
                if y != y_set[-1]:
                    y_num += 1
                    self.browser.find_element(By.XPATH, "//*[@class='dlg-tabsDiv']//*[@title='增加度量']").click()
                    sleep(1)

            # 区域
            if region:
                district = region.get("地区")
                drill = region.get("钻取")
                province = region.get("省份字段")
                city = region.get("城市字段")

                # 地区
                if district:
                    self.browser.find_element(By.XPATH, "//*[@name='district']/preceding-sibling::span/a").click()
                    d_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(district))
                    if len(d_elements) == 0:
                        raise NoSuchElementException
                    for element in d_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择地区: {0}".format(district))
                            break

                # 钻取，启用/关闭
                if drill:
                    js = "return document.getElementsByName('drill')[0].checked;"
                    status = self.browser.execute_script(js)
                    tmp = True if drill == "启用" else False
                    if status ^ tmp:
                        self.browser.find_element(By.XPATH, "//*[@name='drill']").click()
                        log.info("{0}钻取".format(drill))

                # 省份字段
                if province:
                    self.browser.find_element(By.XPATH, "//*[@name='province']/preceding-sibling::span/a").click()
                    p_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(province))
                    if len(p_elements) == 0:
                        raise NoSuchElementException
                    for element in p_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择省份字段: {0}".format(province))
                            break

                # 城市字段
                if city:
                    self.browser.find_element(By.XPATH, "//*[@name='city']/preceding-sibling::span/a").click()
                    c_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(city))
                    if len(c_elements) == 0:
                        raise NoSuchElementException
                    for element in c_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择城市字段: {0}".format(city))
                            break

        # x轴
        if x_set:
            col_name = x_set.get("维度")
            custom_name = x_set.get("自定义名称")

            # 选择维度
            if col_name:
                self.browser.find_element(
                    By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='X轴']/../following-sibling::div[1]/div/div/span/span/a").click()
                x_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(col_name))
                if len(x_elements) == 0:
                    raise NoSuchElementException
                for element in x_elements:
                    if element.is_displayed():
                        element.click()
                        log.info("选择维度: {0}".format(col_name))
                        break

            # 设置自定义名称
            if custom_name:
                self.browser.find_element(
                    By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='X轴']/../following-sibling::div[1]/div[2]//input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='X轴']/../following-sibling::div[1]/div[2]//input").send_keys(
                    custom_name)
                log.info("设置自定义名称: {0}".format(custom_name))
                sleep(1)

        # 分组
        if g_info:
            self.browser.find_element(
                By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='分组']/../following-sibling::div[1]/div/div/span/span/a").click()
            g_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(g_info))
            if len(g_elements) == 0:
                raise NoSuchElementException
            for element in g_elements:
                if element.is_displayed():
                    element.click()
                    log.info("选择分组: {0}".format(g_info))
                    break

        # 数据列
        if col_legend:
            c_num = 1
            for col in col_legend:

                table_col = col.get("列选择")
                custom_name = col.get("自定义名称")
                custom_color = col.get("自定义列颜色")

                # 列选择
                if table_col:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据列']/../following-sibling::div[{0}]/div//a".format(
                            c_num)).click()
                    col_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(table_col))
                    if len(col_elements) == 0:
                        raise NoSuchElementException
                    for element in col_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择数据列: {0}".format(table_col))
                            break

                # 设置自定义名称
                if custom_name:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据列']/../following-sibling::div[{0}]/div[2]//input".format(
                            c_num)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据列']/../following-sibling::div[{0}]/div[2]//input".format(
                            c_num)).send_keys(custom_name)
                    log.info("设置自定义名称: {0}".format(custom_name))

                # 自定义列颜色
                if custom_color:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据列']/../following-sibling::div[{0}]/div[3]//*[@name='colFontColor']".format(
                            c_num)).click()
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据列']/../following-sibling::div[{0}]/div[3]//*[@name='col-color']".format(
                            c_num)).send_keys(custom_color)
                    log.info("设置自定义列颜色: {0}".format(custom_color))

                # 添加下一个
                if col != col_legend[-1]:
                    c_num += 1
                    self.browser.find_element(By.XPATH, "//*[@class='dlg-tabsDiv']//*[@title='增加数据列']").click()
                    sleep(1)

        # 排序
        if r_set:
            r_num = 1
            for r in r_set:

                self.browser.find_element(By.XPATH, "//*[@class='dlg-tabsDiv']//*[@title='增加排序字段']").click()

                col_name = r.get("排序字段")
                rank_type = r.get("排序方式")

                # 选择排序字段
                if col_name:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='排序']/../following-sibling::div[{0}]/div//a".format(
                            r_num)).click()
                    r_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(col_name))
                    if len(r_elements) == 0:
                        raise NoSuchElementException
                    for element in r_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择排序字段: {0}".format(col_name))
                            break

                # 设置排序方式
                if rank_type:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='排序']/../following-sibling::div[{0}]/div[2]//*[text()='{1}']".format(
                            r_num, rank_type)).click()
                    log.info("选择排序方式: {0}".format(rank_type))

                # 添加下一个
                r_num += 1
                sleep(1)

        # 数据过滤
        if filter_set:
            f_num = 1
            if filter_set:
                for f in filter_set:

                    self.browser.find_element(By.XPATH, "//*[@class='dlg-tabsDiv']//*[@title='增加数据过滤']").click()

                    col_name = f.get("过滤字段")
                    custom_name = f.get("自定义名称")
                    relationship = f.get("逻辑关系")
                    filter_value = f.get("过滤值")
                    dynamic_query = f.get("动态查询")
                    filter_range = f.get("作用范围")

                    # 选择过滤字段
                    if col_name:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[2]//a".format(
                                f_num)).click()
                        f_elements = self.browser.find_elements(
                            By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(col_name))
                        if len(f_elements) == 0:
                            raise NoSuchElementException
                        for element in f_elements:
                            if element.is_displayed():
                                element.click()
                                log.info("选择过滤字段: {0}".format(col_name))
                                break

                    # 设置自定义名称
                    if custom_name:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[3]//input".format(
                                f_num)).clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[3]//input".format(
                                f_num)).send_keys(custom_name)
                        log.info("设置自定义名称: {0}".format(custom_name))

                    # 选择逻辑关系
                    if relationship:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[4]//a".format(
                                f_num)).click()
                        rela_elements = self.browser.find_elements(
                            By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(relationship))
                        if len(rela_elements) == 0:
                            raise NoSuchElementException
                        for element in rela_elements:
                            if element.is_displayed():
                                element.click()
                                log.info("选择逻辑关系: {0}".format(relationship))
                                break

                    # 选择过滤值
                    if filter_value:
                        self.browser.find_element(
                            By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[5]//a".format(
                                f_num)).click()
                        sleep(1)
                        fv_elements = self.browser.find_elements(
                            By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(filter_value))
                        if len(fv_elements) == 0:
                            self.browser.find_element(
                                By.XPATH, "//*[@class='dlg-tabsDiv']//*[text()='数据过滤']/../following-sibling::div[{0}]/div[5]//"
                                "*[@name='filter-value']/preceding-sibling::input[1]".format(f_num)).send_keys(filter_value)
                        for element in fv_elements:
                            if element.is_displayed():
                                element.click()
                                log.info("选择过滤值: {0}".format(filter_value))
                                break

                    # 动态查询
                    if dynamic_query:
                        js = "return document.getElementsByName('dynamic')[{0}].checked;".format(f_num-1)
                        status = self.browser.execute_script(js)
                        tmp = True if dynamic_query == "启用" else False
                        if status ^ tmp:
                            self.browser.find_element(
                                By.XPATH, "//*[text()='数据过滤']/../following-sibling::div[{0}]//*[@name='dynamic']".format(
                                    f_num)).click()
                            log.info("{0}动态查询".format(dynamic_query))

                    # 作用范围
                    if filter_range:
                        js = "return document.getElementsByName('optional')[{0}].checked;".format(f_num-1)
                        status = self.browser.execute_script(js)
                        tmp = True if dynamic_query == "启用" else False
                        if status ^ tmp:
                            self.browser.find_element(
                                By.XPATH, "//*[text()='数据过滤']/../following-sibling::div[{0}]//*[@name='optional']".format(
                                    f_num)).click()
                            self.browser.find_element(
                                By.XPATH, "//*[text()='数据过滤']/../following-sibling::div[{0}]//*[@name='range']/preceding-sibling::span//a".format(
                                    f_num)).click()
                            range_elements = self.browser.find_elements(
                                By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(filter_range))
                            if len(range_elements) == 0:
                                raise NoSuchElementException
                            for element in range_elements:
                                if element.is_displayed():
                                    element.click()
                                    log.info("选择作用范围: {0}".format(filter_range))
                                    break

                    # 添加下一个
                    f_num += 1
                    sleep(1)

        # 字典转义
        if escape:
            e_num = 2
            for esc in escape:
                if not isinstance(esc, dict):
                    raise TypeError
                escape_field = esc.get("转义字段")
                dictionary = esc.get("转义字典")
                self.browser.find_element(By.XPATH, "//*[@title='增加字典转义']").click()
                escape_xpath = "//*[contains(@class,'ds-DE')]/div[{0}]".format(e_num)

                # 转义字段
                if escape_field:
                    self.browser.find_element(
                        By.XPATH, escape_xpath + "//*[@data-i18n-text='dictionaryEscape.escapeField']/following-sibling::span[1]//a").click()
                    e_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(escape_field))
                    if len(e_elements) == 0:
                        raise NoSuchElementException
                    for element in e_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择转义字段: {0}".format(escape_field))
                            break

                # 转义字典
                if dictionary:
                    self.browser.find_element(
                        By.XPATH, escape_xpath + "//*[@data-i18n-text='dictionaryEscape.dictionary']/following-sibling::span[1]//a").click()
                    d_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(dictionary))
                    if len(d_elements) == 0:
                        raise NoSuchElementException
                    for element in d_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("选择转义字典: {0}".format(dictionary))
                            break

                # 添加下一个
                e_num += 1
                sleep(1)

    def style_set(self, style):
        """
        # 样式配置
        :param style: 样式配置
        """
        if self.image_type == "bar":
            # 柱状图
            bar_style(theme=style.get("主题样式"), custom_theme_colors=style.get("自定义主题色彩"),
                      custom_bg_color=style.get("自定义背景颜色"), bg_color_rgb=style.get("背景颜色"),
                      data_dis_direction=style.get("数据展示方向"), show_metrics=style.get("是否显示度量"),
                      metrics_font_size=style.get("度量字体大小"), show_title=style.get("是否显示标题"),
                      title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                      axis_name_font_size=style.get("坐标轴名称字体大小"),
                      axis_tick_label_font_size=style.get("坐标轴刻度标签字体大小"),
                      x_axis_area_zoom=style.get("X轴区域缩放"), y_axis_area_zoom=style.get("Y轴区域缩放"),
                      image_type=style.get("图像类型"), area_fill_color=style.get("区域填充颜色"))

        elif self.image_type == "line":
            # 折线图
            line_style(theme=style.get("主题样式"), custom_theme_colors=style.get("自定义主题色彩"),
                       custom_bg_color=style.get("自定义背景颜色"), bg_color_rgb=style.get("背景颜色"),
                       area_fill_color=style.get("区域填充颜色"), show_metrics=style.get("是否显示度量"),
                       metrics_font_size=style.get("度量字体大小"), show_title=style.get("是否显示标题"),
                       title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                       axis_name_font_size=style.get("坐标轴名称字体大小"),
                       axis_tick_label_font_size=style.get("坐标轴刻度标签字体大小"),
                       x_axis_area_zoom=style.get("X轴区域缩放"), y_axis_area_zoom=style.get("Y轴区域缩放"))

        elif self.image_type == "pie":
            # 饼状图
            pie_style(theme=style.get("主题样式"), custom_theme_colors=style.get("自定义主题色彩"),
                      custom_bg_color=style.get("自定义背景颜色"), bg_color_rgb=style.get("背景颜色"),
                      pie=style.get("饼图样式"), pie_radius=style.get("半径"), pie_outer_radius=style.get("外半径"),
                      pie_inner_radius=style.get("内半径"), show_legend=style.get("是否显示图例"),
                      legend_direction=style.get("图例标示方向"), legend_align=style.get("图例对齐方式"),
                      legend_font_size=style.get("图例字体大小"), show_title=style.get("是否显示标题"),
                      title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                      legend_sortable=style.get("启用图例拖拽排序"))

        elif self.image_type == "gauge":
            # 仪表图
            gauge_style(theme=style.get("主题样式"), custom_bg_color=style.get("自定义背景颜色"),
                        bg_color_rgb=style.get("背景颜色"), show_title=style.get("是否显示标题"),
                        title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                        margin_top=style.get("上边距"), margin_left=style.get("左边距"),
                        radius=style.get("半径"), start_angle=style.get("开始角度"), angle=style.get("角度大小"),
                        low_threshold=style.get("低阈比例"), high_threshold=style.get("高阈比例"),
                        min_value=style.get("最小值"), max_value=style.get("最大值"))

        elif self.image_type == "radar":
            # 雷达图
            radar_style(theme=style.get("主题样式"), custom_bg_color=style.get("自定义背景颜色"),
                        bg_color_rgb=style.get("背景颜色"), show_legend=style.get("是否显示图例"),
                        legend_direction=style.get("图例标示方向"), legend_align=style.get("图例对齐方式"),
                        legend_font_size=style.get("图例字体大小"), show_title=style.get("是否显示标题"),
                        title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                        radius=style.get("半径"), min_value=style.get("最小值"), max_value=style.get("最大值"))

        elif self.image_type == "table":
            # 数据表格
            table_style(theme=style.get("主题样式"), custom_bg_color=style.get("自定义背景颜色"),
                        bg_color_rgb=style.get("背景颜色"), show_title=style.get("是否显示标题"),
                        title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                        page_size=style.get("每页展示条数"), col_align=style.get("列对齐方式"),
                        col_width=style.get("列宽度"), frozen_column=style.get("冻结列"))

        elif self.image_type == "treeMap":
            # 矩形树图
            rectangle_style(theme=style.get("主题样式"), custom_bg_color=style.get("自定义背景颜色"),
                            bg_color_rgb=style.get("背景颜色"), show_title=style.get("是否显示标题"),
                            title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"))

        elif self.image_type == "map":
            # 地图
            map_style(theme=style.get("主题样式"), custom_bg_color=style.get("自定义背景颜色"),
                      bg_color_rgb=style.get("背景颜色"), show_title=style.get("是否显示标题"),
                      title_alignment=style.get("标题对齐方式"), title_font_size=style.get("标题字体大小"),
                      show_district=style.get("显示地区名称"), show_color_bar=style.get("显示颜色条"),
                      min_value=style.get("最小值"), max_value=style.get("最大值"), min_value1=style.get("下级最小值"),
                      max_value1=style.get("下级最大值"))

        else:
            if not self.image_type:
                raise KeyError("未指定图像类型")
            else:
                raise KeyError("暂不支持的图像类型: {0}".format(self.image_type))

    def delete(self, image_name):
        """
        :param image_name: 图像名称
        """
        self.browser.find_element(By.XPATH, "//*[@id='visualImageName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='visualImageName']/following-sibling::span/input[1]").send_keys(image_name)
        log.info("图像名称输入: {0}".format(image_name))
        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@title='查询可视化图像']").click()
        page_wait(1)
        self.browser.find_element(
            By.XPATH, "//*[@field='visualImageName']//div[@data-mtips='{0}']".format(image_name)).click()
        # 点击删除
        self.browser.find_element(By.XPATH, "//*[@title='删除可视化图像']").click()
        alert = BeAlertBox(timeout=3, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(image_name), auto_click_ok=False):
            alert.click_ok()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("删除成功"):
                log.info("删除图像【{0}】成功".format(image_name))
            else:
                log.error("删除图像【{0}】失败，失败原因{1}".format(image_name, msg))
            set_global_var("ResultMsg", msg, False)
        else:
            log.error("删除图像【{0}】失败，失败原因{1}".format(image_name, msg))
            set_global_var("ResultMsg", msg, False)

    def imageClear(self, image_name, fuzzy_match=False):
        """
        :param image_name: 图像名称
        :param fuzzy_match: 模糊匹配
        """
        self.browser.find_element(By.XPATH, "//*[@id='visualImageName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='visualImageName']/following-sibling::span/input[1]").send_keys(image_name)
        log.info("图像名称输入: {0}".format(image_name))
        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@title='查询可视化图像']").click()
        page_wait(3)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='visualImageName']//div[starts-with(@data-mtips,'{0}')]".format(image_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='visualImageName']//div[@data-mtips='{0}']".format(image_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 点击删除
                self.browser.find_element(By.XPATH, "//*[@title='删除可视化图像']").click()
                alert = BeAlertBox(timeout=1, back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    toast = Toast()
                    if toast.exist:
                        msg = toast.get_msg()
                        if not toast.msg_contains("删除成功"):
                            log.info("删除图像失败，失败原因: {0}".format(msg))
                            set_global_var("ResultMsg", msg, False)
                            break

                        log.info("{0} {1}".format(search_result, msg))
                        toast.waitUntil()
                        if not fuzzy_match:
                            break

                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH,
                            "//*[@field='visualImageName']//div[starts-with(@data-mtips,'{0}')]".format(image_name))
                        if len(record_element) > 0:
                            exist_data = True
                        else:
                            # 查询结果为空,修改exist_data为False，退出循环
                            log.info("数据清理完成")
                            exist_data = False
                else:
                    # 无权操作
                    log.warning("清理失败，失败提示: {0}".format(msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
