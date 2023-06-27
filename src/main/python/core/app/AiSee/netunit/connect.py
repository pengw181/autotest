# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:05

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_domain
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class ConnectTest(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="网元连通性")

        # 切到网元连通性页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/connectTestInfo.html')]")))
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
        select_item = {}

        # 数据来源
        if query.__contains__("数据来源"):
            reuse = query.get("数据来源")
            self.browser.find_element(By.XPATH, "//*[@id='reuse']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(reuse)).click()
            log.info("数据来源选择: {}".format(reuse))

        # 网元名称
        if query.__contains__("网元名称"):
            netunit_name = query.get("网元名称")
            self.browser.find_element(By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("网元名称输入关键字: {}".format(netunit_name))
            select_item["网元名称"] = netunit_name

        # 网元类型
        if query.__contains__("网元类型"):
            level_type = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(level_type)).click()
            log.info("网元类型选择: {}".format(level_type))

        # 登录模式
        if query.__contains__("登录模式"):
            login_type = query.get("登录模式")
            self.browser.find_element(By.XPATH, "//*[@id='loginTypeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(login_type)).click()
            log.info("登录模式选择: {}".format(login_type))
            select_item["登录模式"] = login_type

        # 登录状态
        if query.__contains__("登录状态"):
            result = query.get("登录状态")
            self.browser.find_element(By.XPATH, "//*[@id='result']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(result)).click()
            log.info("登录状态选择: {}".format(result))

        # 生产厂家
        if query.__contains__("生产厂家"):
            vendor = query.get("生产厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendorId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(vendor)).click()
            log.info("生产厂家选择: {}".format(vendor))

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(model)).click()
            log.info("设备型号选择: {}".format(model))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
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
                    netunit_name = select_item.get("网元名称")
                    login_type = select_item.get("登录模式")
                    self.browser.find_element(
                        By.XPATH,
                        "//[@field='netunitName']//[@data-mtips='{}']/../../following-sibling::td[@field='loginTypeName']//*[text()='{}']".format(
                            netunit_name, login_type)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def test_all(self, query):
        """
        # 测试全部网元
        :param query: 查询条件
        """
        if query is None:
            log.warning("请加入查询条件后测试")
            return

        self.search(query=query, need_choose=False)
        self.browser.find_element(By.XPATH, "//*[@id='testAllBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("确定测试全部的网元", auto_click_ok=False):
            alert.click_ok()
            page_wait(timeout=120)
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动测试全部网元成功")
            else:
                log.warning("启动测试全部网元失败，失败提示: {0}".format(msg))
        else:
            log.warning("启动测试全部网元失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def test_selected(self, query, netunit_list):
        """
        # 测试选中网元
        :param query: 查询条件
        :param netunit_list: 网元列表

        网元列表
        [
            {
                "网元名称": "",
                "登录模式": ""
            },
            {
                "网元名称": "",
                "登录模式": ""
            }
        ]
        """
        if netunit_list is None:
            log.warning("未指定网元列表，无法测试")
            return

        self.search(query=query, need_choose=False)
        for netunit_data in netunit_list:
            netunit_name = netunit_data.get("网元名称")
            login_type = netunit_data.get("登录模式")
            self.browser.find_element(
                By.XPATH,
                "//*[@field='netunitName']//*[@data-mtips='{}']/../../following-sibling::td[@field='loginTypeName']//*[text()='{}']".format(
                    netunit_name, login_type)).click()
            log.info("选择待测试网元: {0}, 登录模式: {1}".format(netunit_name, login_type))
        self.browser.find_element(By.XPATH, "//*[@id='testSelectedBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("确定测试选中的网元", auto_click_ok=False):
            alert.click_ok()
            page_wait(timeout=120)
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动确定测试选中的网元成功")
            else:
                log.warning("启动确定测试选中的网元失败，失败提示: {0}".format(msg))
        else:
            log.warning("启动确定测试选中的网元失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)
