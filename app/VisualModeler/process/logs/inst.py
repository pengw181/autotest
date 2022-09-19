# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/16 下午6:20

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from app.VisualModeler.doctorwho.doctorWho import DoctorWho


class ProcessLog:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("流程编辑器-流程运行日志")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/gooflow/queryProcessLogInfo.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='processName']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def search(self, process_name=None, status=None, begin_time=None, end_time=None):
        """
        查询流程日志
        :param process_name: 流程名称，默认查全部
        :param status: 运行状态，默认查全部
        :param begin_time: 开始时间，默认当天0点
        :param end_time: 结束时间，默认当前24点
        :return:
        """

    def view_process_log(self):
        """
        查看流程日志
        :return:
        """


    def view_cmd_log(self):
        """
        查看指令日志
        :return:
        """


    def rerun(self):
        """
        重新运行
        :return:
        """


    def view_run_info(self):
        """
        查看运行信息
        :return:
        """


    def view_report(self, report_title):
        """
        报表预览
        :param report_title:
        :return:
        """


    def view_ocr(self):
        """
        OCR预览
        :return:
        """

    def view_process_param(self):
        """
        流程参数预览
        :return:
        """

    def input_phone_code(self, code):
        """
        输入手机验证码
        :param code:
        :return:
        """

    def export(self):
        """
        导出
        :return:
        """


class Inst:

    def search(self, inst_name, inst_status=None):
        """
        查询实例
        :param inst_name: 实例名称
        :param inst_status: 实例状态，默认查全部
        :return:
        """

    def view_node_log(self, node_name, tab):
        """
        查看节点日志
        :param node_name:
        :param tab:
        :return:
        """

