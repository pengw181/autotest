# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:06

from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class Confirm(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        choose_menu(menu="登录配置确认")

        # 切到登录配置确认页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJumpConfirmInfo.html')]")))
        page_wait()
        sleep(1)

    def choose(self, netunit_list):
        """
        :param netunit_list: 网元列表
        """
        for n in netunit_list:
            element = self.browser.find_element(
                By.XPATH, "//*[@field='netunitName']//*[@data-mtips='{}']/../../../following-sibling::td[1]/*[text()='新值']".format(
                    n))
            element.click()
            log.info("已选网元: {}".format(n))

    def search(self, condition):
        """
        :param condition: 查询条件
        """
        # 网元名称
        if condition.__contains__("网元名称"):
            netunit_name = condition.get("网元名称")
            self.browser.find_element(By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("网元名称输入关键字: {}".format(netunit_name))

        # 网元类型
        if condition.__contains__("网元类型"):
            netunit_type = condition.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='levelType']/following-sibling::span//a").click()
            type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'levelType') and text()='{}']".format(netunit_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("网元类型选择: {}".format(netunit_type))

        # 生产厂家
        if condition.__contains__("生产厂家"):
            vendor = condition.get("生产厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendorId']/following-sibling::span//a").click()
            vendor_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'vendorId') and text()='{}']".format(vendor))
            action = ActionChains(self.browser)
            action.move_to_element(vendor_list).click().perform()
            log.info("生产厂家选择: {}".format(vendor))

        # 设备型号
        if condition.__contains__("设备型号"):
            netunit_model = condition.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='netunitModelId']/following-sibling::span/input[1]").send_keys(netunit_model)
            log.info("设备型号输入关键字: {}".format(netunit_model))

        # 登录模式
        if condition.__contains__("登录模式"):
            login_type = condition.get("登录模式")
            self.browser.find_element(By.XPATH, "//*[@id='loginTypeName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='loginTypeName']/following-sibling::span/input[1]").send_keys(login_type)
            log.info("登录模式输入关键字: {}".format(login_type))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='searchBtn']").click()
        page_wait()

    def confirm_all(self, condition):
        """
        # 确认全部
        :param condition: 查询条件
        """
        if condition is None:
            log.warning("未避免对其他人的数据造成影响，请加入查询条件后确认")
        else:
            self.search(condition=condition)
            self.browser.find_element(By.XPATH, "//*[@id='confirmAll']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("该操作将覆盖原有的登录信息，是否确认", auto_click_ok=False):
                alert.click_ok()
                page_wait(timeout=120)
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("确认成功"):
                    log.info("确认成功")
                else:
                    log.warning("确认失败，失败提示: {0}".format(msg))
                    alert.click_ok()
            else:
                log.warning("确认失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def confirm_selected(self, condition, netunit_list):
        """
        # 确认所选
        :param condition: 查询条件
        :param netunit_list: 网元列表
        """
        if netunit_list is None:
            log.warning("未指定网元泪奔，无法确认")
        else:
            self.search(condition=condition)
            self.choose(netunit_list=netunit_list)
            self.browser.find_element(By.XPATH, "//*[@id='confirmAll']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("该操作将覆盖原有的登录信息，是否确认", auto_click_ok=False):
                alert.click_ok()
                page_wait(timeout=120)
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("确认成功"):
                    log.info("确认成功")
                else:
                    log.warning("确认失败，失败提示: {0}".format(msg))
                    alert.click_ok()
            else:
                log.warning("确认失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def cancel_selected(self, condition, netunit_list):
        """
        # 取消配置下发
        :param condition: 查询条件
        :param netunit_list: 网元列表
        """
        if netunit_list is None:
            log.warning("未指定网元列表，无法取消配置下发")
        else:
            self.search(condition=condition)
            self.choose(netunit_list=netunit_list)
            self.browser.find_element(By.XPATH, "//*[@id='deleteSelected']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("该操作将取消配置下发，是否确认", auto_click_ok=False):
                alert.click_ok()
                page_wait(timeout=120)
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("取消配置下发成功")
                else:
                    log.warning("取消配置下发失败，失败提示: {0}".format(msg))
                    alert.click_ok()
            else:
                log.warning("取消配置下发失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)
