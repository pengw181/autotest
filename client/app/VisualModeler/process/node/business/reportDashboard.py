# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/10 下午3:46

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver import ActionChains
from client.page.handle.windows import WindowHandles
from client.page.func.pageMaskWait import page_wait
from client.app.Dashboard.image.image import Image
from client.app.Dashboard.dashboard.editDashboard import EditDashboard
from client.app.Dashboard.dictionary.dictionary import Dictionary
from client.app.VisualModeler.process.draw.processInfo import Process
from service.lib.variable.globalVariable import *


class ReportDashboard:

    default_msg = "操作成功"

    def __init__(self):

        self.browser = get_global_var("browser")
        self.current_win_handle = WindowHandles()
        page_wait(3)

    def access_report_dashboard(self, process_name, node_name):
        """
        :param process_name: 流程名称
        :param node_name: 节点名称
        """
        # 是否在流程图编辑器页面
        sleep(1)
        try:
            self.current_win_handle.switch("流程图编辑器")
        except NoSuchWindowException:
            Process().search(query={"关键字": process_name}, need_choose=True)
            self.browser.find_element(By.XPATH, "//*[text()='画流程图']").click()
            # 保存新窗口，并切换到新窗口
            self.current_win_handle.save("流程图编辑器")
            self.current_win_handle.switch("流程图编辑器")
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(node_name))))
            page_wait()

        # 是否在报表节点页面
        try:
            self.browser.find_element(By.XPATH, "//*[@id='form_id']//*[text()='仪表盘配置']")
        except NoSuchElementException:
            node_element = self.browser.find_element(
                By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(node_name))
            # 双击进入节点
            action = ActionChains(self.browser)
            action.double_click(node_element).perform()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[contains(@src, './node/reportNode.html')]"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            page_wait()
            sleep(1)

        # 点击仪表盘配置，进入仪表盘主配置页
        self.browser.find_element(By.XPATH, "//*[@id='dashboard_cfg']").click()
        self.current_win_handle.save("仪表盘主配置页")
        self.current_win_handle.switch("仪表盘主配置页")
        sleep(1)
        set_global_var("ResultMsg", self.default_msg, False)

    @staticmethod
    def set_dashboard(dashboard_info):
        """
        :param dashboard_info: 仪表盘配置，字典
        """
        dashboard = EditDashboard()
        dashboard_name = dashboard_info.get("仪表盘名称")
        subtitle = dashboard_info.get("仪表盘副标题")
        remark = dashboard_info.get("备注")
        theme = dashboard_info.get("主题样式")
        show_title = dashboard_info.get("显示标题")
        carousel = dashboard_info.get("启用轮播")
        carousel_interval = dashboard_info.get("轮播间隔")
        dashboard.edit(dashboard_name, subtitle, remark, theme, show_title, carousel,  carousel_interval)

    @staticmethod
    def set_image(image):
        """
        :param image: 图像配置，字典
        """
        img = Image()
        imageName = image.get("图像名称")
        catalog = None
        interface = None
        imageType = image.get("图像类型")
        dataSource = image.get("数据源配置")
        style = image.get("样式配置")
        img.add(imageName, catalog, interface, imageType, dataSource, style)

    @staticmethod
    def delete_image(image_name):
        """
        :return: 图像名称
        """
        img = Image()
        img.delete(image_name)

    @staticmethod
    def clear_image(image_name, fuzzy_match):
        """
        :param image_name: 图像名称
        :param fuzzy_match: 模糊匹配
        """
        img = Image()
        img.imageClear(image_name, fuzzy_match)

    @staticmethod
    def add_dictionary(dictionary_list):
        """
        :param dictionary_list: 字典配置，数组
        """
        dictionary = Dictionary()
        dictionary.add(dict_list=dictionary_list)

    @staticmethod
    def edit_dictionary(dict_name, dictionary_list):
        """
        :param dict_name: 字典名称
        :param dictionary_list: 字典配置，数组
        """
        dictionary = Dictionary()
        dictionary.update(dict_name=dict_name, dictionary=dictionary_list)

    @staticmethod
    def delete_dictionary(dict_name):
        """
        :param dict_name: 字典名称
        """
        dictionary = Dictionary()
        dictionary.delete(dict_name=dict_name)

    @staticmethod
    def clear_dictionary(dictionary_name, fuzzy_match):
        """
        :param dictionary_name: 字典名称
        :param fuzzy_match: 模糊匹配
        """
        dictionary = Dictionary()
        dictionary.clear_dict(dictionary_name, fuzzy_match)

    @staticmethod
    def add_in_image(image_list):
        """
        :param image_list: 图像列表
        """
        dashboard = EditDashboard()
        dashboard.addInImage(image_list=image_list)

    def refresh_report_node(self):
        """
        # 刷新
        """
        self.current_win_handle.switch("流程图编辑器")
        # 点击刷新
        self.browser.find_element(By.XPATH, "//*[@onclick='queryVarCfgList()']").click()
        set_global_var("ResultMsg", self.default_msg, False)

    def view_dashboard(self, var_name):
        """
        :param var_name: 变量名
        """
        self.current_win_handle.switch("流程图编辑器")
        sleep(1)
        # 点击图像预览
        self.browser.find_element(By.XPATH, "//*[text()='{0}']/../following-sibling::td[2]//a".format(var_name)).click()
        self.current_win_handle.save("图像预览")
        self.current_win_handle.switch("图像预览")
        set_global_var("ResultMsg", self.default_msg, False)
