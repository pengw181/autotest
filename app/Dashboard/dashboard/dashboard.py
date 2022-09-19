# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/13 上午11:30

from app.Dashboard.dashboard.editDashboard import EditDashboard
from common.variable.globalVariable import *
from common.page.script.css import setVisible
from time import sleep
from common.page.func.alertBox import BeAlertBox
from common.page.func.toast import Toast
from common.page.func.pageMaskWait import page_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.log.logger import log
from common.wrapper.dashboardCheck import closeAndEnterDashboard


class Dashboard:

    default_msg = "操作成功"

    def __init__(self, iframe_xpath):
        self.browser = get_global_var("browser")
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, iframe_xpath)))
        log.info("进入仪表盘页面")
        page_wait(3)
        sleep(1)

    # def menuVisible(self, iframe):
    #     """
    #     # 将主页菜单显示处理
    #     :param iframe: page iframe element
    #     """
    #     class_name = "index-menu"
    #     setVisible(self.browser, iframe, class_name)

    def click(self, button_name):
        """
        # 点击右上角按钮
        :param button_name: 按钮名称
        """
        class_name = "index-menu"
        setVisible(self.browser, class_name)
        if button_name == "查询":
            menu_class = "search"
        elif button_name == "轮播开关":
            menu_class = "carousel-switch"
        elif button_name == "导出PNG":
            menu_class = "exp-png"
        elif button_name == "导出PDF":
            menu_class = "exp-pdf"
        elif button_name == "全屏":
            menu_class = "expand"
        elif button_name == "关闭进入配置页":
            menu_class = "close"
        else:
            raise KeyError("菜单名称错误")
        self.browser.find_element(By.XPATH, "//*[@class='index-menu']/a[@class='{0}']".format(menu_class)).click()
        page_wait(10)
        # 操作没有提示，给一个默认提示
        set_global_var("ResultMsg", self.default_msg, False)
        sleep(1)

    def show(self, dashboardName):
        """
        # 展示仪表盘，仅在vm首页仪表盘使用
        :param dashboardName: 仪表盘名称
        """
        self.browser.find_element(By.XPATH, "//*[@class='dashboard-select']/div[@class='arrow']").click()
        self.browser.find_element(By.XPATH, "//*[@name='dashboards']/preceding-sibling::span/a").click()
        dashboard_element = self.browser.find_elements(
            By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(dashboardName))
        if len(dashboard_element) == 0:
            raise dashboard_element
        for element in dashboard_element:
            if element.is_displayed():
                element.click()
                log.info("选择仪表盘: {0}".format(dashboardName))
                # 操作没有提示，给一个默认提示
                set_global_var("ResultMsg", self.default_msg, False)
                page_wait()
                sleep(1)
                break

    @closeAndEnterDashboard
    def _enterListPage(self):
        """
        # 进入仪表盘列表页面
        # 如果当前没有内部仪表盘，刷新页面，会自动进入仪表盘列表页面
        """
        page_wait(3)
        self.browser.find_element(By.XPATH, "//*[@class='tabs-title' and text()='仪表盘列表']").click()
        sleep(1)

    def _choose(self, dashboardName):
        """
        # 仪表盘列表选择仪表盘
        :param dashboardName: 仪表盘名称
        """
        # 进入仪表盘列表页面
        self._enterListPage()

        # 仪表盘名称
        self.browser.find_element(By.XPATH, "//*[@name='dashoardName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@name='dashoardName']/preceding-sibling::input[1]").send_keys(dashboardName)
        self.browser.find_element(By.XPATH, "//*[@title='查询仪表盘']").click()
        page_wait(2)
        self.browser.find_element(
            By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']".format(dashboardName)).click()
        sleep(1)

    def viewDashboard(self, dashboardName):
        """
        # 仪表盘列表预览
        :param dashboardName: 仪表盘名称
        """
        # 选择仪表盘
        self._choose(dashboardName)

        # 点击预览
        self.browser.find_element(
            By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']/../../following-sibling::td[2]//input".format(
                dashboardName)).click()
        log.info("预览仪表盘【{0}】".format(dashboardName))
        # 操作没有提示，给一个默认提示
        set_global_var("ResultMsg", self.default_msg, False)

    def setPublicStatus(self, dashboardName, public):
        """
        # 公开
        :param dashboardName: 仪表盘名称
        :param public: 是否公开，公开/取消公开
        """
        # 选择仪表盘
        self._choose(dashboardName)

        # 获取公开状态
        js = 'return document.getElementsByName("dashboard-share")[0].checked'
        status = self.browser.excute_script(js)

        # 是否公开
        tmp = True if public == "公开" else False
        if status ^ tmp:
            self.browser.find_element(
                By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']/../../following-sibling::td[3]//input".format(
                    dashboardName)).click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定要{0}该仪表盘吗".format(public), auto_click_ok=False):
                alert.click_ok()
                sleep(1)
                js = 'return document.getElementsByName("dashboard-share")[0].checked'
                status = self.browser.excute_script(js)
                if status:
                    log.info("公开仪表盘")
                else:
                    log.info("取消公开仪表盘")
            else:
                log.info("设置仪表盘【{0}】公开状态失败，失败原因: {1}".format(dashboardName, msg))
        else:
            log.info("仪表盘【{0}】公开状态已经是 {1}".format(dashboardName, public))
        # 操作没有提示，给一个默认提示
        set_global_var("ResultMsg", self.default_msg, False)

    def setActivateStatus(self, dashboardName, activate):
        """
        # 激活
        :param dashboardName: 仪表盘名称
        :param activate: 是否激活，激活/取消激活
        """
        # 选择仪表盘
        self._choose(dashboardName)

        # 获取激活状态
        js = 'return document.getElementsByName("activeDashboard")[0].checked'
        status = self.browser.excute_script(js)

        # 是否激活
        tmp = True if activate == "激活" else False
        if status ^ tmp:
            self.browser.find_element(
                By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']/../../following-sibling::td[4]//input".format(
                    dashboardName)).click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定{0}仪表盘【{1}】吗".format(activate, dashboardName), auto_click_ok=False):
                alert.click_ok()
                sleep(1)
                js = 'return document.getElementsByName("dashboard-share")[0].checked'
                status = self.browser.excute_script(js)
                if status:
                    log.info("激活仪表盘")
                else:
                    log.info("取消激活仪表盘")
            else:
                log.info("设置仪表盘【{0}】激活状态失败，失败原因: {1}".format(dashboardName, msg))
        else:
            log.info("仪表盘【{0}】激活状态已经是 {1}".format(dashboardName, activate))
        # 操作没有提示，给一个默认提示
        set_global_var("ResultMsg", self.default_msg, False)

    @closeAndEnterDashboard
    def add(self, dashboardInfo):
        """
        # 添加仪表盘
        :param dashboardInfo: 仪表盘配置
        """
        self.browser.find_element(By.XPATH, "//*[@title='新建仪表盘']").click()
        dashboard = EditDashboard()
        dashboard_name = dashboardInfo.get("仪表盘名称")
        subtitle = dashboardInfo.get("仪表盘副标题")
        remark = dashboardInfo.get("备注")
        theme = dashboardInfo.get("主题样式")
        show_title = dashboardInfo.get("显示标题")
        carousel = dashboardInfo.get("启用轮播")
        carousel_interval = dashboardInfo.get("轮播间隔")
        dashboard.edit(dashboard_name, subtitle, remark, theme, show_title, carousel, carousel_interval)

    @closeAndEnterDashboard
    def edit(self, dashboardName, dashboardInfo):
        """
        # 修改仪表盘
        :param dashboardName: 仪表盘名称
        :param dashboardInfo: 仪表盘配置
        """
        # 选择仪表盘
        self._choose(dashboardName)

        self.browser.find_element(By.XPATH, "//*[@title='修改仪表盘']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            set_global_var("ResultMsg", msg, False)
        else:
            dashboard = EditDashboard()
            dashboard_name = dashboardInfo.get("仪表盘名称")
            subtitle = dashboardInfo.get("仪表盘副标题")
            remark = dashboardInfo.get("备注")
            theme = dashboardInfo.get("主题样式")
            show_title = dashboardInfo.get("显示标题")
            carousel = dashboardInfo.get("启用轮播")
            carousel_interval = dashboardInfo.get("轮播间隔")
            dashboard.edit(dashboard_name, subtitle, remark, theme, show_title, carousel, carousel_interval)

    @closeAndEnterDashboard
    def delete(self, dashboardName):
        """
        # 删除仪表盘
        :param dashboardName: 仪表盘名称
        """
        # 选择仪表盘
        self._choose(dashboardName)

        self.browser.find_element(By.XPATH, "//*[@title='删除仪表盘']").click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(dashboardName), auto_click_ok=False):
            alert.click_ok()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("删除成功"):
                log.info("删除仪表盘【{0}】成功".format(dashboardName))
            else:
                log.error("删除仪表盘【{0}】失败".format(dashboardName))
            set_global_var("ResultMsg", msg, False)
        else:
            log.info("设置仪表盘【{0}】激活状态失败，失败原因: {1}".format(dashboardName, msg))
            set_global_var("ResultMsg", msg, False)

    @closeAndEnterDashboard
    def activateLibView(self, dashboardName):
        """
        # 公开库预览
        :param dashboardName: 仪表盘名称
        """
        # 进入公开库页面
        self.browser.find_element(By.XPATH, "//*[@id='dashboardTb']//*[@title='仪表盘公开库']").click()
        page_wait(3)
        sleep(1)

        # 仪表盘名称
        self.browser.find_element(By.XPATH, "//*[@name='dashboardName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@name='dashboardName']/preceding-sibling::input[1]").send_keys(dashboardName)
        self.browser.find_element(By.XPATH, "//*[@id='shareDashboardBar']//*[text()='查询']").click()
        page_wait(3)
        sleep(1)
        self.browser.find_element(
            By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']/../../following-sibling::td[3]//a[1]".format(
                dashboardName)).click()
        log.info("预览公开库仪表盘【{0}】".format(dashboardName))
        # 操作没有提示，给一个默认提示
        set_global_var("ResultMsg", self.default_msg, False)

    @closeAndEnterDashboard
    def clone(self, dashboardName):
        """
        # 公开库克隆
        :param dashboardName: 仪表盘名称
        """
        # 进入公开库页面
        self.browser.find_element(By.XPATH, "//*[@id='dashboardTb']//*[@title='仪表盘公开库']").click()
        page_wait(3)
        sleep(1)

        # 仪表盘名称
        self.browser.find_element(By.XPATH, "//*[@name='dashboardName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@name='dashboardName']/preceding-sibling::input[1]").send_keys(dashboardName)
        self.browser.find_element(By.XPATH, "//*[@id='shareDashboardBar']//*[text()='查询']").click()
        page_wait(3)
        sleep(1)
        self.browser.find_element(
            By.XPATH, "//*[@field='dashboardName']//*[@data-mtips='{0}']/../../following-sibling::td[3]//a[2]".format(
                dashboardName)).click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定克隆该仪表盘吗", auto_click_ok=False):
            alert.click_ok()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("克隆仪表盘成功"):
                sleep(1)
                log.info("克隆公开库仪表盘【{0}】成功".format(dashboardName))
                set_global_var("ResultMsg", msg, False)
        else:
            log.info("克隆仪表盘【{0}】失败，失败原因: {1}".format(dashboardName, msg))
            set_global_var("ResultMsg", msg, False)

    def bind(self, dashboardName, imageList):
        """
        # 仪表盘加入图像
        :param dashboardName: 仪表盘名称
        :param imageList: 图像列表
        """
        # 选择仪表盘
        self._choose(dashboardName)

        self.browser.find_element(By.XPATH, "//*[@title='修改仪表盘']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            set_global_var("ResultMsg", msg, False)
        else:
            dashboard = EditDashboard()
            dashboard.addInImage(imageList)

    @closeAndEnterDashboard
    def clear(self, dashboardName, fuzzy_match=False):
        """
        清空仪表盘
        :param dashboardName: 仪表盘名称
        :param fuzzy_match: 模糊匹配
        """
        # 进入仪表盘列表页面
        self._enterListPage()

        # 仪表盘名称
        self.browser.find_element(By.XPATH, "//*[@name='dashoardName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@name='dashoardName']/preceding-sibling::input[1]").send_keys(dashboardName)
        self.browser.find_element(By.XPATH, "//*[@title='查询仪表盘']").click()
        page_wait(2)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dashboardName']//div[starts-with(@data-mtips,'{0}')]".format(dashboardName))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dashboardName']//div[@data-mtips='{0}']".format(dashboardName))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 点击删除
                self.browser.find_element(By.XPATH, "//*[@title='删除仪表盘']").click()
                alert = BeAlertBox(timeout=1, back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    toast = Toast()
                    if toast.exist:
                        msg = toast.get_msg()
                        if not toast.msg_contains("删除成功"):
                            log.info("删除仪表盘失败，失败原因: {0}".format(msg))
                            set_global_var("ResultMsg", msg, False)
                            break

                        log.info("{0} {1}".format(search_result, msg))
                        toast.waitUntil()
                        if not fuzzy_match:
                            break

                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH,
                            "//*[@field='dashboardName']//div[starts-with(@data-mtips,'{0}')]".format(dashboardName))
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
