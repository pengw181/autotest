# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/13 下午5:15

from client.app.Dashboard.dashboard.dashboard import Dashboard
from client.app.Dashboard.dashboard.editDashboard import DefaultDashboard, MyDashboard
from client.app.Dashboard.image.image import Image
from client.app.Dashboard.dictionary.dictionary import Dictionary
from client.app.Dashboard.dataInterface.interface import CustomizeInterface
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from client.page.func.pageMaskWait import page_wait


class Monitor(Dashboard):

    def __init__(self):
        DoctorWho().choose_menu("个人中心-我的监控")
        page_wait(5)
        self.iframe_xpath = "//iframe[contains(@src, '/VisualModeler/html/personalcenter/myMonitor.html')]"
        super().__init__(self.iframe_xpath)

    def clickButton(self, button_name):
        """
        # 点击按钮
        :param button_name: 按钮
        :return:
        """
        self.click(button_name)

    def showDashboard(self, dashboard_name):
        """
        # 预览仪表盘
        :param dashboard_name: 仪表盘名称
        :return:
        """
        self.show(dashboard_name)

    @staticmethod
    def setDefaultDashboard(dashboard_info):
        """
        # 默认仪表盘
        :param dashboard_info: 仪表盘配置
        """
        dashboard = DefaultDashboard()
        dashboard_name = dashboard_info.get("仪表盘名称")
        subtitle = dashboard_info.get("仪表盘副标题")
        remark = dashboard_info.get("备注")
        theme = dashboard_info.get("主题样式")
        show_title = dashboard_info.get("显示标题")
        carousel = dashboard_info.get("启用轮播")
        carousel_interval = dashboard_info.get("轮播间隔")
        dashboard.edit(dashboard_name, subtitle, remark, theme, show_title, carousel, carousel_interval)

    @staticmethod
    def setMyDashboard(dashboard_info):
        """
        # 我的仪表盘
        :param dashboard_info: 仪表盘配置
        """
        dashboard = MyDashboard()
        dashboard_name = dashboard_info.get("仪表盘名称")
        subtitle = dashboard_info.get("仪表盘副标题")
        remark = dashboard_info.get("备注")
        theme = dashboard_info.get("主题样式")
        show_title = dashboard_info.get("显示标题")
        carousel = dashboard_info.get("启用轮播")
        carousel_interval = dashboard_info.get("轮播间隔")
        dashboard.edit(dashboard_name, subtitle, remark, theme, show_title, carousel, carousel_interval)

    def addDashboard(self, dashboard_info):
        """
        # 添加仪表盘
        :param dashboard_info: 仪表盘配置
        """
        self.add(dashboard_info)

    def editDashboard(self, dashboard_name, dashboard_info):
        """
        # 编辑仪表盘
        :param dashboard_name: 仪表盘名称
        :param dashboard_info: 仪表盘配置
        """
        self.edit(dashboard_name, dashboard_info)

    def deleteDashboard(self, dashboard_name):
        """
        # 删除仪表盘
        :param dashboard_name: 仪表盘名称
        """
        self.delete(dashboard_name)

    @staticmethod
    def addImage(image_info):
        """
        # 添加图像
        :param image_info: 图像配置
        """
        image = Image()
        image_name = image_info.get("图像名称")
        catalog = image_info.get("主题分类")
        interface = image_info.get("数据接口")
        image_type = image_info.get("图像类型")
        data_source = image_info.get("数据源配置")
        style = image_info.get("样式配置")
        image.add(image_name, catalog, interface, image_type, data_source, style)

    @staticmethod
    def deleteImage(image_name):
        """
        删除图像
        :param image_name: 图像名称
        """
        image = Image()
        image.delete(image_name)

    @staticmethod
    def clearImage(image_name, fuzzy_match):
        """
        :param image_name: 图像名称
        :param fuzzy_match: 模糊匹配
        """
        img = Image()
        img.imageClear(image_name, fuzzy_match)

    @staticmethod
    def addDictionary(dictionary_info):
        """
        # 添加字典
        :param dictionary_info: 字典配置
        """
        dictionary = Dictionary()
        dictionary.add(dictionary_info)

    @staticmethod
    def editDictionary(dict_name, dictionary_info):
        """
        # 编辑字典
        :param dict_name: 字典名
        :param dictionary_info: 字典配置
        """
        dictionary = Dictionary()
        dictionary.update(dict_name, dictionary_info)

    @staticmethod
    def deleteDictionary(dict_name):
        """
        # 删除字典
        :param dict_name: 字典名
        """
        dictionary = Dictionary()
        dictionary.delete(dict_name)

    @staticmethod
    def clearDictionary(dict_name, fuzzy_match):
        """
        # 清除字典
        :param dict_name: 字典名
        :param fuzzy_match: 模糊匹配
        """
        dictionary = Dictionary()
        dictionary.clear_dict(dict_name, fuzzy_match)

    def addInImage(self, dashboard_name, image_list):
        """
        # 仪表盘加入图像
        :param dashboard_name: 仪表盘名称
        :param image_list: 图像列表
        """
        self.bind(dashboard_name, image_list)

    @staticmethod
    def fieldConversion(table_name, conversion):
        """
        # 字段类型转化
        :param table_name: 表中文名称
        :param conversion: 转化配置，数组
        """
        interface = CustomizeInterface()
        interface.fieldConversion(table_name, conversion)

    @staticmethod
    def fieldClassify(table_name, x_list, y_list, g_list):
        """
        # 字段分类
        :param table_name: 表中文名称
        :param x_list: 维度字段，数组
        :param y_list: 度量字段，数组
        :param g_list: 分组字段，数组
        """
        interface = CustomizeInterface()
        interface.fieldClassify(table_name, x_list, y_list, g_list)
