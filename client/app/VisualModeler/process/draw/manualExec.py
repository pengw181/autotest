# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午4:12

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchWindowException
from client.page.func.pageMaskWait import page_wait
from client.page.func.alertBox import BeAlertBox
from client.page.handle.windows import WindowHandles
from client.app.VisualModeler.process.draw.processInfo import Process
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


class ManualExecute:

    def __init__(self, process_name):
        """
        :param process_name: 流程名称
        """
        self.browser = get_global_var("browser")
        self.process_name = process_name
        # 判断当前是否在一键启动页面
        self.current_win_handle = WindowHandles()
        try:
            self.current_win_handle.switch(title="一键启动")
            self.current_win_handle.close(title="一键启动")
            self.current_win_handle.switch("vm")
        except NoSuchWindowException:
            pass
        self.process = Process()
        self.process.search(query={"关键字": self.process_name}, need_choose=True)

    def test(self):
        """
        # 测试
        """
        self.browser.find_element(By.XPATH, "//*[@onclick='test_process();']").click()
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '../gooflow/testProcess.html')]")))
        self.browser.find_element(By.XPATH, "//*[@onclick='SaveForm()']").click()
        alert = BeAlertBox(timeout=5)
        msg = alert.get_msg()
        if alert.title_contains("调用测试流程成功,请到流程运行日志中查看"):
            log.info("调用测试流程成功")
        else:
            log.error("调用测试流程失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def fast_run(self, params):
        """
        # 一键启动
        :param params: 参数列表
        """
        # 点击进入一键启动页面
        self.browser.find_element(
            By.XPATH, "//*[text()='{0}']/./../../following-sibling::td[5]//img".format(self.process_name)).click()
        current_win_handle = WindowHandles()
        current_win_handle.save(title="一键启动")
        current_win_handle.switch(title="一键启动")
        page_wait()
        sleep(2)
        # wait = WebDriverWait(self.browser, 30)
        # wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='run_process']")))
        if params:
            if not isinstance(params, dict):
                raise TypeError("参数列表格式不是字典")
            for key, value in params.items():
                self.browser.find_element(
                    By.XPATH, "//*[@value='{0}']/../following-sibling::td[1]/span/input[1]".format(key)).clear()
                self.browser.find_element(
                    By.XPATH, "//*[@value='{0}']/../following-sibling::td[1]/span/input[1]".format(key)).send_keys(value)
                log.info("设置 {0} 的值: {1}".format(key, value))
        # 点击启动
        self.browser.find_element(By.XPATH, "//*[@id='run_process']").click()
        page_wait()
        alert = BeAlertBox(timeout=3)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.error("一键启动失败，失败原因: {0}".format(msg))
        else:
            msg = "操作成功"
            log.info("一键启动成功")
        set_global_var("ResultMsg", msg, False)
