# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:08

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.AlarmPlatform.main.menu.chooseMenu import choose_menu
from common.page.func.alertBox import BeAlertBox
from time import sleep
from common.log.logger import log


class FTP:

    def __init__(self):
        self.browser = get_global_var("browser")
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

    def choose(self, ftp_name):
        """
        :param ftp_name: FTP名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@id='ftpName']/following-sibling::span[1]/input[1]")
        input_ele.clear()
        input_ele.send_keys(ftp_name)
        self.browser.find_element(By.XPATH, "//span[text()='查询']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='ftpName']//a[text()='{}']".format(ftp_name)).click()
        log.info("已选择ftp: {}".format(ftp_name))

    def add(self, ftp_name, host, port, username, password):
        """
        :param ftp_name: FTP名称
        :param host: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']//*[text()='添加']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        self.ftp_page(ftp_name, host, port, username, password)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("数据 {0} 添加成功".format(ftp_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(ftp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, ftp_name, host, port, username, password):
        """
        :param obj: FTP名称
        :param ftp_name: FTP名称
        :param host: 连接地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]")))

        self.ftp_page(ftp_name, host, port, username, password)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("{0} 修改成功".format(obj))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

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

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']//*[text()='提交']").click()

    def test(self, ftp_name):
        """
        :param ftp_name: FTP名称
        """
        log.info("开始修改数据")
        self.choose(ftp_name)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/ftpConfig/addFtpConfig.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='ftpName']/following-sibling::span/input[1]")))
        self.browser.find_element(By.XPATH, "//*[@id='testButtonId']//*[text()='测试']").click()
        alert = BeAlertBox(back_iframe=True, timeout=60)
        msg = alert.get_msg()
        if alert.title_contains("测试成功"):
            log.info("{0} 测试成功".format(ftp_name))
        else:
            log.warning("{0} 测试失败，测试返回结果: {1}".format(ftp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def delete(self, obj):
        """
        :param obj: FTP名称
        """
        log.info("开始删除数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: FTP名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@id='ftpName']/following-sibling::span[1]/input[1]").clear()
        self.browser.find_element(
            By.XPATH, "//*[@id='ftpName']/following-sibling::span[1]/input[1]").send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='ftpName']/*[contains(@class,'ftpName')]/*[starts-with(text(),'{}')]".format(obj))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='ftpName']/*[contains(@class,'ftpName')]/*[text()='{}']".format(obj))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element(By.XPATH, "//*[text()='删除']").click()
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
                                By.XPATH, "//*[@field='ftpName']/*[contains(@class,'ftpName')]/*[starts-with(text(),'{0}')]".format(
                                    obj))
                            if len(record_element) > 0:
                                exist_data = True
                            else:
                                # 查询结果为空,修改exist_data为False，退出循环
                                log.info("数据清理完成")
                                exist_data = False
                        else:
                            break
                    else:
                        raise Exception("删除数据时出现未知异常: {0}".format(msg))
                else:
                    # 无权操作
                    log.warning("{0} 清理失败，失败提示: {1}".format(obj, msg))
                    set_global_var("ResultMsg", msg, False)
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
