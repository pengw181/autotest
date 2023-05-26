# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:08

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.core.app.AlarmPlatform.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class FTP:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        # 进入菜单
        choose_menu("连接配置-FTP配置")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/dataConfig/ftpConfig/ftpConfigList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='ftpName']/following-sibling::span[1]/input[1]")))
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

        # FTP名称
        if query.__contains__("FTP名称"):
            ftp_name = query.get("FTP名称")
            self.browser.find_element(By.XPATH, "//*[@name='ftpName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='ftpName']/preceding-sibling::input[1]").send_keys(ftp_name)
            select_item = ftp_name

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").send_keys(
                creator)

        # 创建时间
        if query.__contains__("创建时间"):
            begin_time, end_time = query.get("创建时间")
            # 开始时间
            if begin_time:
                self.browser.find_element(By.XPATH, "//*[@name='startDate']/preceding-sibling::span//a").click()
                if isinstance(begin_time, dict):
                    # 间隔，0表示当前，正数表示未来，负数表示过去
                    time_interval = begin_time.get("间隔")
                    # 单位，年、月、天、时、分、秒
                    time_unit = begin_time.get("单位")
                    begin_time = calculation(interval=time_interval, unit=time_unit)
                else:
                    raise AttributeError("开始时间必须是字典")
                set_calendar(date_s=begin_time, date_format='%Y-%m-%d %H:%M:%S')
                log.info("设置创建开始时间: {0}".format(begin_time))

            # 结束时间
            if end_time:
                self.browser.find_element(By.XPATH, "//*[@name='endDate']/preceding-sibling::span//a").click()
                if isinstance(end_time, dict):
                    # 间隔，0表示当前，正数表示未来，负数表示过去
                    time_interval = end_time.get("间隔")
                    # 单位，年、月、天、时、分、秒
                    time_unit = end_time.get("单位")
                    end_time = calculation(interval=time_interval, unit=time_unit)
                else:
                    raise AttributeError("结束时间必须是字典")
                set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
                log.info("设置创建结束时间: {0}".format(end_time))

        # 查询
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_ftp_query']").click()
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
                        By.XPATH, "//*[@field='ftpName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, ftp_name, host, port, username, password):
        """
        :param ftp_name: FTP名称
        :param host: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        self.ftp_page(ftp_name, host, port, username, password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("数据 {0} 添加成功".format(ftp_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(ftp_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, ftp, ftp_name, host, port, username, password):
        """
        :param ftp: FTP名称
        :param ftp_name: FTP名称
        :param host: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.search(query={"FTP名称": ftp}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]")))

        self.ftp_page(ftp_name, host, port, username, password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("{0} 修改成功".format(ftp))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(ftp, msg))
        gbl.temp.set("ResultMsg", msg)

    def ftp_page(self, ftp_name, host, port, username, password):
        """
        :param ftp_name: FTP名称
        :param host: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        # FTP名称
        if ftp_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]").send_keys(ftp_name)
            log.info("设置FTP名称: {0}".format(ftp_name))

        # 连接地址
        if host:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpHostname']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpHostname']/following-sibling::span/input[1]").send_keys(host)
            log.info("设置连接地址: {0}".format(host))

        # 端口
        if port:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpPort']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpPort']/following-sibling::span/input[1]").send_keys(port)
            log.info("设置端口: {0}".format(port))

        # 用户名
        if username:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpUsername']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpUsername']/following-sibling::span/input[1]").send_keys(username)
            log.info("设置用户名: {0}".format(username))

        # 密码
        if password:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpPassword']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='ftpPassword']/following-sibling::span/input[1]").send_keys(password)
            sleep(1)
            log.info("设置密码: {0}".format(password))

    def test(self, ftp_name):
        """
        :param ftp_name: FTP名称
        """
        self.search(query={"FTP名称": ftp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]")))
        # 点击测试按钮
        self.browser.find_element(By.XPATH, "//*[@id='testButtonId']").click()
        alert = BeAlertBox(back_iframe=True, timeout=60)
        msg = alert.get_msg()
        if alert.title_contains("测试成功"):
            log.info("{0} 测试成功".format(ftp_name))
        else:
            log.warning("{0} 测试失败，测试返回结果: {1}".format(ftp_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def delete(self, ftp_name):
        """
        :param ftp_name: FTP名称
        """
        self.search(query={"FTP名称": ftp_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(ftp_name, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(ftp_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(ftp_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(ftp_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, ftp_name, fuzzy_match=False):
        """
        :param ftp_name: FTP名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"FTP名称": ftp_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='ftpName']//*[starts-with(text(),'{}')]".format(ftp_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='ftpName']//*[text()='{}']".format(ftp_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            search_result = pe.text
            pe.click()
            log.info("选择: {0}".format(search_result))
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("{0} 删除成功".format(search_result))
                    page_wait()
                    if fuzzy_match:
                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH, "//*[@field='ftpName']//*[starts-with(text(),'{0}')]".format(ftp_name))
                        if len(record_element) == 0:
                            # 查询结果为空,修改exist_data为False，退出循环
                            log.info("数据清理完成")
                            exist_data = False
                    else:
                        break
                else:
                    raise Exception("删除数据时出现未知异常: {0}".format(msg))
            else:
                # 无权操作
                log.warning("{0} 清理失败，失败提示: {1}".format(ftp_name, msg))
                gbl.temp.set("ResultMsg", msg)
