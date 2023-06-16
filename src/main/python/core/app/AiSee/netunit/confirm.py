# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:06

import json
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
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

    def search(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None

        # 网元名称
        if query.__contains__("网元名称"):
            netunit_name = query.get("网元名称")
            self.browser.find_element(By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("网元名称输入关键字: {}".format(netunit_name))
            select_item = netunit_name

        # 网元类型
        if query.__contains__("网元类型"):
            level_type = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='levelType']/following-sibling::span//a").click()
            type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'levelType') and text()='{}']".format(level_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("网元类型选择: {}".format(level_type))

        # 生产厂家
        if query.__contains__("生产厂家"):
            vendor = query.get("生产厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendorId']/following-sibling::span//a").click()
            type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'vendorId') and text()='{}']".format(vendor))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("生产厂家选择: {}".format(vendor))

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span//a").click()
            type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModelId') and text()='{}']".format(model))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("设备型号选择: {}".format(model))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='searchBtn']").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
            return
        if need_choose:
            if select_item:
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='netunitName']//*[@data-mtips='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def confirm_all(self, query):
        """
        # 确认全部
        :param query: 查询条件
        """
        if query is None:
            log.warning("未避免对其他人的数据造成影响，请加入查询条件后确认")
            return

        self.search(query=query, need_choose=False)
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

    def confirm_selected(self, query, netunit_list):
        """
        # 确认所选
        :param query: 查询条件
        :param netunit_list: 网元列表
        """
        if netunit_list is None:
            log.warning("未指定网元列表，无法确认")
            return

        self.search(query=query, need_choose=False)
        for netunit in netunit_list:
            self.browser.find_element(
                    By.XPATH, "//*[@field='netunitName']//*[@data-mtips='{}']/../../../following-sibling::td[1]/*[text()='新值']".format(
                        netunit)).click()
            log.info("选择待确认网元: {}".format(netunit))
        self.browser.find_element(By.XPATH, "//*[@id='confirmSelected']").click()
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

    def cancel_selected(self, query, netunit_list):
        """
        # 取消配置下发
        :param query: 查询条件
        :param netunit_list: 网元列表
        """
        if netunit_list is None:
            log.warning("未指定网元列表，无法取消配置下发")
            return

        self.search(query=query, need_choose=False)
        for netunit in netunit_list:
            self.browser.find_element(
                By.XPATH,
                "//*[@field='netunitName']//*[@data-mtips='{}']/../../../following-sibling::td[1]/*[text()='新值']".format(
                    netunit)).click()
            log.info("选择待确认网元: {}".format(netunit))
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
