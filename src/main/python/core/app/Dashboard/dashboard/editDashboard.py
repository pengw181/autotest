# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/4/24 下午5:16

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.toast import Toast
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.wrap import Wrap
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class EditDashboard:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        self.xpath = "//*[@data-name='edit-dashboard']"
        page_wait(3)

    def edit(self, dashboard_name, subtitle, remark, theme, show_title, carousel, carousel_interval):
        """
        :param dashboard_name: 仪表盘名称
        :param subtitle: 仪表盘副标题
        :param remark: 备注
        :param theme: 主题样式
        :param show_title: 显示标题，显示/隐藏
        :param carousel: 启用轮播，启用/关闭
        :param carousel_interval: 轮播间隔
        """
        # 仪表盘名称
        if dashboard_name:
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-name']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-name']/preceding-sibling::input[1]").send_keys(
                dashboard_name)
            log.info("设置仪表盘名称: {0}".format(dashboard_name))

        # 仪表盘副标题
        if subtitle:
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-sub-name']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-sub-name']/preceding-sibling::input[1]").send_keys(subtitle)
            log.info("设置仪表盘副标题: {0}".format(subtitle))

        # 备注
        if remark:
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-remark']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-remark']/preceding-sibling::input[1]").send_keys(remark)
            log.info("设置备注: {0}".format(remark))

        # 主题样式
        if theme:
            self.browser.find_element(By.XPATH, self.xpath + "//*[text()='主题样式']/following-sibling::div[1]/div").click()
            self.browser.find_element(By.XPATH, self.xpath + "//*[text()='{0}']".format(theme)).click()
            log.info("设置主题样式: {0}".format(theme))

        # 显示标题
        if show_title:
            js = "return $('.show-title')[2].checked;"
            show_status = self.browser.execute_script(js)
            log.info("显示标题: {0}".format(show_status))

            tmp = True if show_title == "显示" else False
            show_title_element = self.browser.find_element(By.XPATH, self.xpath + "//*[@name='show-title']")
            if tmp ^ show_status:
                show_title_element.click()
            log.info("设置{0}标题".format(show_title))

        # 启用轮播
        if carousel:
            js = "return $('.carousel-auto')[2].checked;"
            carousel_status = self.browser.execute_script(js)
            log.info("启用轮播: {0}".format(carousel_status))

            tmp = True if carousel == "启用" else False
            carousel_element = self.browser.find_element(By.XPATH, self.xpath + "//*[@name='carousel-auto']")
            if tmp ^ carousel_status:
                carousel_element.click()
            log.info("设置{0}轮播".format(carousel))

        # 轮播间隔
        if carousel_interval:
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-carousel-interval']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, self.xpath + "//*[@name='dashboard-carousel-interval']/preceding-sibling::input[1]").send_keys(
                carousel_interval)
            log.info("设置轮播间隔: {0}".format(carousel_interval))

        # 保存
        sleep(1)
        self.browser.find_element(By.XPATH, self.xpath + "//*[text()='保存']").click()
        toast = Toast(timeout=30)
        msg = toast.get_msg()
        if toast.msg_contains("保存成功"):
            log.info("仪表盘保存成功")
        else:
            log.info("仪表盘保存失败，失败原因: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def searchGlobal(self):
        # 查询全局
        pass

    def view(self):
        # 预览
        pass

    def addInImage(self, image_list):
        """
        # 添加图像
        :param image_list: 图像列表
        """
        self.browser.find_element(By.XPATH, self.xpath + "//*[text()='添加图像']").click()
        log.info("仪表盘加入图像")
        page_wait(3)
        wait = WebDriverWait(self.browser, 5)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='visualImageName']/preceding-sibling::input[1]")))
        for image in image_list:
            self.browser.find_element(
                By.XPATH, "//*[@id='selectImageDlg']//*[@field='visualImageName']//*[@data-mtips='{0}']".format(
                    image)).click()
            log.info("已选择图像: {0}".format(image))
        self.browser.find_element(By.XPATH, "//*[@id='selectImageDlg']//*[text()='确定']").click()
        log.info("加入图像成功")
        # 保存
        self.browser.find_element(By.XPATH, self.xpath + "//*[text()='保存']").click()
        toast = Toast()
        msg = toast.get_msg()
        gbl.temp.set("ResultMsg", msg)

    def setImageSize(self):
        pass

    def linkage(self):
        # 图像联动
        pass


@Wrap(wrap_func='close_enter_dashboard')
class MyDashboard(EditDashboard):

    """
    # 我的仪表盘, 功能与编辑仪表盘相同
    """
    def __init__(self):
        super().__init__()
        self.browser.find_element(By.XPATH, "//*[text()='我的仪表盘']").click()
        log.info("进入我的仪表盘页面")
        page_wait(3)


@Wrap(wrap_func='close_enter_dashboard')
class DefaultDashboard(EditDashboard):

    """
    # 默认仪表盘, 功能与编辑仪表盘相同
    """
    def __init__(self):
        super().__init__()
        self.browser.find_element(By.XPATH, "//*[text()='默认仪表盘']").click()
        log.info("进入默认仪表盘页面")
        page_wait(3)
