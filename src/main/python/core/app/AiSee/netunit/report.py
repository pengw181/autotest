# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:05

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_domain
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.tableData import get_table_data
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class ConnectTestReport(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="连通测试报告")

        # 切到连通测试报告页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/connectTestInfoReport.html')]")))
        page_wait(timeout=180)
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

        # 触发用户
        if query.__contains__("触发用户"):
            user_name = query.get("触发用户")
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").send_keys(user_name)
            log.info("触发用户输入关键字: {}".format(user_name))
            select_item = user_name

        # 测试类型
        if query.__contains__("测试类型"):
            connect_type = query.get("测试类型")
            self.browser.find_element(By.XPATH, "//*[@id='connectType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(connect_type)).click()
            log.info("设置测试类型: {}".format(connect_type))

        # 开始时间
        if query.__contains__("开始时间"):
            start_time = query.get("开始时间")
            self.browser.find_element(By.XPATH, "//*[@id='startTime']/following-sibling::span//a").click()
            set_calendar(date_s=start_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("开始时间选择: {}".format(start_time))
            sleep(1)

        # 结束时间
        if query.__contains__("结束时间"):
            end_time = query.get("结束时间")
            self.browser.find_element(By.XPATH, "//*[@id='endTime']/following-sibling::span//a").click()
            set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("结束时间选择: {}".format(end_time))
            sleep(1)

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
                    self.browser.find_element(
                        By.XPATH, "//*[@field='userName']//*[text()='{}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def connect_retest(self, query):
        """
        # 连通性测试报告列表重新测试
        :param query: 查询条件
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='retestSelectedBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确认要重新测试这条数据吗", auto_click_ok=False):
            alert.click_ok()
            page_wait(timeout=120)
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动重新测试成功")
            else:
                log.warning("启动重新测试失败，失败提示: {0}".format(msg))
        else:
            log.warning("启动重新测试失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def get_connect_result(self, query, row_num=1):
        """
        # 获取连通性测试报告列表的第N行数据
        :param query: 查询条件
        :param row_num: 行号，从1开始，默认为1，表示最新的一条
        :return: 返回结果汇总字段内容
        """
        self.search(query=query, need_choose=False)
        data_xpath = "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@class='datagrid-body']/table"
        table_data = get_table_data(data_xpath, limit=row_num)
        result = table_data[0][3]
        log.info("结果汇总:【{}】".format(result))
        gbl.temp.set("ResultMsg", result)

    def get_connect_result_detail(self, query, netunit_name, row_num=1):
        """
        # 点击”设备数量列“查看报告详细内容，查看某个网元在某种登录模式下的登录日志
        :param query: 查询条件
        :param netunit_name: 网元名称
        :param row_num: 行号，从1开始，默认为1，表示最新的一条
        :return: 返回登录明细页面各设备登录状态，二维表
        """
        self.search(query=query, need_choose=False)
        report_list = self.browser.find_elements(
            By.XPATH, "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@field='nuCount']//a")
        report_list[row_num - 1].click()
        user_name = query.get("触发用户")
        log.info("选择【{}】触发的最新第{}条连通性测试报告".format(user_name, row_num))
        # 切到登录明细页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'connectTestInfoNetunitDetail.html')]")))
        page_wait()
        self.search_detail(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[contains(@class,'selected')]//*[@field='logId']//span").click()
        sleep(3)

    def connect_detail_retest(self, query, netunit_name, row_num=1):
        """
        # 网元设备登录明细中重新测试
        :param query: 查询条件
        :param netunit_name: 网元名称
        :param row_num: 行号，从1开始，默认为1，表示最新的一条
        """
        self.search(query=query, need_choose=False)
        report_list = self.browser.find_elements(
            By.XPATH, "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@field='nuCount']//a")
        report_list[row_num - 1].click()
        user_name = query.get("触发用户")
        log.info("选择【{}】触发的最新第{}条连通性测试报告".format(user_name, row_num))
        # 切到登录明细页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'connectTestInfoNetunitDetail.html')]")))
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH,
            "//body[not(@class)]//*[contains(@class,'panel-htop')]//*[@id='netunitName']/following-sibling::span/input[1]")))
        self.search_detail(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH,
            "//*[@id='retestSelectedBtn' and not(@funcid='netunitMgt_connectTestInfoReport_testSelected')]").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确认要重新测试这条数据吗", auto_click_ok=False):
            alert.click_ok()
            page_wait(timeout=120)
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动重新测试成功")
            else:
                log.warning("启动重新测试失败，失败提示: {0}".format(msg))
        else:
            log.warning("启动重新测试失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def search_detail(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None
        this_page_xpath = "//body[not(@class)]//*[contains(@class,'panel-htop')]"
        page_wait()

        # 网元名称
        if query.__contains__("网元名称"):
            netunit_name = query.get("网元名称")
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='netunitName']/following-sibling::span/input[1]").send_keys(
                netunit_name)
            log.info("网元名称输入关键字: {}".format(netunit_name))
            select_item = netunit_name

        # 服务器标识
        if query.__contains__("服务器标识"):
            server_name = query.get("服务器标识")
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='serverName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='serverName']/following-sibling::span/input[1]").send_keys(
                server_name)
            log.info("服务器标识输入关键字: {}".format(server_name))

        # 登录状态
        if query.__contains__("登录状态"):
            result = query.get("登录状态")
            self.browser.find_element(By.XPATH, this_page_xpath + "//*[@id='result']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(result)).click()
            log.info("登录状态选择: {}".format(result))

        # 开始时间
        if query.__contains__("开始时间"):
            start_time = query.get("开始时间")
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='startTime']/following-sibling::span//a").click()
            set_calendar(date_s=start_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("开始时间选择: {}".format(start_time))
            sleep(1)

        # 结束时间
        if query.__contains__("结束时间"):
            end_time = query.get("结束时间")
            self.browser.find_element(
                By.XPATH, this_page_xpath + "//*[@id='endTime']/following-sibling::span//a").click()
            set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("结束时间选择: {}".format(end_time))
            sleep(1)

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
                    self.browser.find_element(
                        By.XPATH, "//*[@field='netunitName']//*[@data-mtips='{}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")
