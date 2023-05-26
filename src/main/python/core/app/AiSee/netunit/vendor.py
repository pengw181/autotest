# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/10/21 下午5:01

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_menu, choose_domain
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class Vendor(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="设备厂家")

        # 切到设备厂家配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'../../html/nu/vendorInfo.html')]")))
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

        # 厂家
        if query.__contains__("厂家"):
            vendor = query.get("厂家")
            self.browser.find_element(By.XPATH, "//*[@id='s_vendorCname']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(vendor)).click()
            select_item["厂家"] = vendor

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(model)).click()
            select_item["设备型号"] = model

        # 关键字
        if query.__contains__("关键字"):
            keyword = query.get("关键字")
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::span/input[1]").send_keys(
                keyword)

        # 查询
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
                if select_item.__contains__("设备型号"):
                    vendor = select_item.get("厂家")
                    model = select_item.get("设备型号")
                    try:
                        self.browser.find_element(
                            By.XPATH, "//*[@field='vendorCname']/*[text()='{0}']/../following-sibling::td[2]/*[text()='{1}']".format(
                                vendor, model)).click()
                    except NoSuchElementException:
                        raise KeyError("未找到匹配数据")
                elif select_item.__contains__("厂家") and not select_item.__contains__("设备型号"):
                    vendor = select_item.get("厂家")
                    try:
                        self.browser.find_element(
                            By.XPATH, "//*[@field='vendorCname']/*[text()='{0}']".format(vendor)).click()
                    except NoSuchElementException:
                        raise KeyError("未找到匹配数据")
                else:
                    raise KeyError("条件不足，未找到匹配数据")
                log.info("选择: {0}".format(json.dumps(query, ensure_ascii=False)))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, vendor_cname, vendor_ename, belong_vendor, model):
        """
        :param vendor_cname: 厂家中文名
        :param vendor_ename: 厂家英文名
        :param belong_vendor: 所属厂家
        :param model: 设备型号
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'vendorInfoEdit.html')]"))
        sleep(1)
        self.vendor_page(vendor_cname=vendor_cname, vendor_ename=vendor_ename, belong_vendor=belong_vendor, model=model)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(timeout=10, back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
            alert.click_ok()
        gbl.temp.set("ResultMsg", msg)

    def update(self, vendor, vendor_cname, vendor_ename, model):
        """
        :param vendor: 设备厂家
        :param vendor_cname: 厂家中文名
        :param vendor_ename: 厂家英文名
        :param model: 设备型号
        """
        self.search(query=vendor, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到修改网元信息页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'vendorInfoEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='vendorCname']/preceding-sibling::input")))
            self.vendor_page(vendor_cname=vendor_cname, vendor_ename=vendor_ename, belong_vendor=None, model=model)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def vendor_page(self, vendor_cname, vendor_ename, belong_vendor, model):
        """
        :param vendor_cname: 厂家中文名
        :param vendor_ename: 厂家英文名
        :param belong_vendor: 所属厂家
        :param model: 设备型号
        """
        # 厂家中文名
        if vendor_cname:
            self.browser.find_element(By.XPATH, "//*[@name='vendorCname']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='vendorCname']/preceding-sibling::input").send_keys(
                vendor_cname)
            log.info("设置厂家中文名: {}".format(vendor_cname))

        # 厂家英文名
        if vendor_ename:
            self.browser.find_element(By.XPATH, "//*[@name='vendorEname']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='vendorEname']/preceding-sibling::input").send_keys(
                vendor_ename)
            log.info("设置厂家中文名: {}".format(vendor_ename))

        # 所属厂家
        if belong_vendor:
            # 切换到设备型号tab
            self.browser.find_element(By.XPATH, "//*[@id='editTab']//*[@class='tabs-last']/a").click()
            self.browser.find_element(By.XPATH, "//*[@id='e2_vendorCname']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(belong_vendor)).click()
            log.info("设置所属厂家: {}".format(belong_vendor))

        # 设备型号
        if model:
            # 切换到设备型号tab
            self.browser.find_element(By.XPATH, "//*[@id='editTab']//*[@class='tabs-last']/a").click()
            self.browser.find_element(By.XPATH, "//*[@name='netunitModelName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='netunitModelName']/preceding-sibling::input").send_keys(
                model)
            log.info("设置设备型号: {}".format(model))
