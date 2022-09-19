# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:05

from common.log.logger import log
from common.variable.globalVariable import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from app.AiSee.netunit.menu import choose_menu
from time import sleep
from common.date.dateUtil import set_calendar
from common.page.func.tableData import get_table_data


class ConnectTestReport(object):

    def __init__(self):
        self.browser = get_global_var("browser")
        choose_menu(menu="连通测试报告")

        # 切到连通测试报告页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/connectTestInfoReport.html')]")))
        page_wait(timeout=180)
        sleep(1)

    def choose(self, test_user, connect_type, begin_time=None, end_time=None):
        """
        :param test_user: 触发用户
        :param connect_type: 测试类型
        :param begin_time: 开始时间
        :param end_time: 结束时间
        """
        # 触发用户
        if test_user:
            self.browser.find_element_by_xpath("//*[@id='userName']/following-sibling::span/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='userName']/following-sibling::span/input[1]").send_keys(test_user)
            log.info("触发用户输入关键字: {}".format(test_user))

        # 测试类型
        if connect_type:
            self.browser.find_element_by_xpath("//*[@id='connectType']/following-sibling::span//a").click()
            type_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'connectType') and text()='{}']".format(connect_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("测试类型选择: {}".format(connect_type))

        # 开始时间
        if begin_time:
            self.browser.find_element_by_xpath("//*[@id='startTime']/following-sibling::span[1]//input[1]").click()
            set_calendar(date_s=begin_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("开始时间选择: {}".format(begin_time))
            sleep(1)

        # 结束时间
        if end_time:
            self.browser.find_element_by_xpath("//*[@id='endTime']/following-sibling::span[1]//input[1]").click()
            set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("结束时间选择: {}".format(end_time))
            sleep(1)

        # 点击查询
        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait(timeout=180)

        report_list = self.browser.find_elements_by_xpath(
            "//*[@field='userName']/*[text()='{0}']/../following-sibling::td[@field='connectType']/*[text()='{1}']".format(test_user, connect_type))
        # 按时间降序，查询结果存在多条记录时，选择第一个
        report_list[0].click()
        log.info("已选【{0}】触发的最新【{1}】连通性测试报告".format(test_user, connect_type))

        # self.get_connect_result()

    @staticmethod
    def get_connect_result(row_num=1):
        """
        # 获取第N行数据
        :param row_num: 行号，从1开始，默认为1，表示最新的一条
        :return: 返回结果汇总字段内容
        """
        data_xpath = "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]//table"
        table_data = get_table_data(data_xpath, limit=row_num)
        result = table_data[0][3]
        log.info("结果汇总:【{}】".format(result))
        return result

    def get_connect_result_detail(self, row_num=1):
        """
        # 查看报告详细内容，
        :param row_num: 行号，从1开始，默认为1，表示最新的一条
        :return: 返回登录明细页面各设备登录状态，二维表
        """
        element = self.browser.find_element_by_xpath(
            "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]//table//tr[{}]/td[3]//a".format(row_num))
        element.click()
        # 切到登录明细页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'connectTestInfoNetunitDetail.html')]")))
        page_wait()
