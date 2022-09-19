# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:04

from common.log.logger import log
from common.variable.globalVariable import *
from selenium.webdriver import ActionChains
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from common.page.func.pageMaskWait import page_wait
from app.AiSee.netunit.menu import choose_menu
from time import sleep


class Terminal(object):

    def __init__(self):
        self.browser = get_global_var("browser")
        choose_menu(menu="统一直连终端配置")

        # 切到统一直连终端配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJumpCustomCfgInfo.html')]")))
        page_wait()
        sleep(1)

    def choose(self, terminal_name):
        """
        :param terminal_name: 终端名称
        """
        input_ele = self.browser.find_element_by_xpath(
            "//*[@id='customName']/following-sibling::span/input[1]")
        input_ele.clear()
        input_ele.send_keys(terminal_name)
        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        self.browser.find_element_by_xpath(
            "//*[@field='accountTempName']//*[@data-mtips='{}']".format(terminal_name)).click()
        log.info("已选终端: {}".format(terminal_name))

    def add(self, terminal_name, terminal_type, account_temp, charset, expect_return, fail_return, terminal_ip,
            terminal_port, remark, login_cmd):
        """
        :param terminal_name: 终端名称
        :param terminal_type: 终端类型
        :param account_temp: 账号名称
        :param charset: 字符集
        :param expect_return: 期待返回符
        :param fail_return: 失败返回符
        :param terminal_ip: 终端IP
        :param terminal_port: 终端端口
        :param remark: 用途
        :param login_cmd: 登录指令
        """
        self.browser.find_element_by_xpath("//*[@id='customName']/following-sibling::span/input[1]").clear()
        self.browser.find_element_by_xpath(
            "//*[@id='customName']/following-sibling::span/input[1]").send_keys(terminal_name)
        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        sleep(1)
        result = False
        try:
            self.browser.find_element_by_xpath(
                "//*[@field='terminal_name']//*[text()='{0}']".format(terminal_name))
            log.info("终端【{}】已存在，开始修改".format(terminal_name))
            result = self.update(obj_terminal=terminal_name, terminal_name=terminal_name, terminal_type=terminal_type,
                                 account_temp=account_temp, charset=charset, expect_return=expect_return,
                                 fail_return=fail_return, terminal_ip=terminal_ip, terminal_port=terminal_port,
                                 remark=remark, login_cmd=login_cmd)
        except NoSuchElementException:
            log.info("终端【{}】不存在，开始添加".format(terminal_name))
            self.browser.find_element_by_xpath("//*[@id='addBtn']//*[text()='添加']").click()
            self.browser.switch_to.frame(
                self.browser.find_element_by_xpath(
                    "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html?type=add')]"))
            sleep(1)
            result = self.terminal_page(terminal_name=terminal_name, terminal_type=terminal_type,
                                        account_temp=account_temp, charset=charset, expect_return=expect_return,
                                        fail_return=fail_return, terminal_ip=terminal_ip, terminal_port=terminal_port,
                                        remark=remark, login_cmd=login_cmd)
        finally:
            return result

    def update(self, obj_terminal, terminal_name, terminal_type, account_temp, charset, expect_return, fail_return,
               terminal_ip, terminal_port, remark, login_cmd):
        """
        :param obj_terminal: 目标终端
        :param terminal_name: 终端名称
        :param terminal_type: 终端类型
        :param account_temp: 账号名称
        :param charset: 字符集
        :param expect_return: 期待返回符
        :param fail_return: 失败返回符
        :param terminal_ip: 终端IP
        :param terminal_port: 终端端口
        :param remark: 用途
        :param login_cmd: 登录指令
        """
        self.choose(terminal_name=obj_terminal)
        self.browser.find_element_by_xpath("//*[@id='editBtn']//*[text()='修改']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 切换到修改终端页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='accountTempName']/preceding-sibling::input")))
            result = self.terminal_page(terminal_name=terminal_name, terminal_type=terminal_type, account_temp=account_temp,
                                        charset=charset, expect_return=expect_return, fail_return=fail_return,
                                        terminal_ip=terminal_ip, terminal_port=terminal_port, remark=remark, login_cmd=login_cmd)

            return result

    def terminal_page(self, terminal_name, terminal_type, account_temp, charset, expect_return, fail_return,
                      terminal_ip, terminal_port, remark, login_cmd):
        """
        :param terminal_name: 终端名称
        :param terminal_type: 终端类型
        :param account_temp: 账号名称
        :param charset: 字符集
        :param expect_return: 期待返回符
        :param fail_return: 失败返回符
        :param terminal_ip: 终端IP
        :param terminal_port: 终端端口
        :param remark: 用途
        :param login_cmd: 登录指令
        """
        # 终端名称
        if terminal_name:
            self.browser.find_element_by_xpath("//*[@id='customName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='customName']/following-sibling::span[1]/input[1]").send_keys(terminal_name)
            log.info("设置终端名称: {}".format(terminal_name))

        # 终端类型
        if terminal_type:
            self.browser.find_element_by_xpath("//*[@id='loginMode']/following-sibling::span//a").click()
            sleep(1)
            type_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'loginMode') and text()='{}']".format(terminal_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("设置终端类型: {}".format(terminal_type))

        # 账号名称
        if account_temp:
            self.browser.find_element_by_xpath("//*[@id='accountTempId']/following-sibling::span//a").click()
            sleep(1)
            type_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'accountTempId') and text()='{}']".format(account_temp))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("设置账号名称: {}".format(account_temp))

        # 字符集
        if charset:
            self.browser.find_element_by_xpath("//*[@id='charset']/following-sibling::span//a").click()
            sleep(1)
            type_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'charset') and text()='{}']".format(charset))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("设置字符集: {}".format(charset))

        # 期待返回符
        if expect_return:
            self.browser.find_element_by_xpath(
                "//*[@id='telnetReturn']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='telnetReturn']/following-sibling::span[1]/input[1]").send_keys(expect_return)
            log.info("设置期待返回符: {}".format(expect_return))

        # 失败返回符
        if fail_return:
            self.browser.find_element_by_xpath("//*[@id='failReturn']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='failReturn']/following-sibling::span[1]/input[1]").send_keys(fail_return)
            log.info("设置失败返回符: {}".format(fail_return))

        # 终端IP
        if terminal_ip:
            self.browser.find_element_by_xpath("//*[@id='terminalIp']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='terminalIp']/following-sibling::span[1]/input[1]").send_keys(terminal_ip)
            log.info("设置终端IP: {}".format(terminal_ip))

        # 终端端口
        if terminal_port:
            self.browser.find_element_by_xpath(
                "//*[@id='terminalPort']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='terminalPort']/following-sibling::span[1]/input[1]").send_keys(terminal_port)
            log.info("设置终端端口: {}".format(terminal_port))

        # 用途
        if remark:
            self.browser.find_element_by_xpath(
                "//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置用途: {}".format(remark))

        # 登录指令
        if login_cmd:
            login_cmd_field = "//*[@id='cmdInfo_tool']/following-sibling::div[1]"
            row_num = 1

            for lc in login_cmd:
                try:
                    row_ele = self.browser.find_element_by_xpath(
                        login_cmd_field + "//*[contains(@class,'rownumber') and text()='{}']".format(row_num))
                    # 如果已存在，则单击修改
                    action = ActionChains(self.browser)
                    action.move_to_element(row_ele).click().perform()
                    sleep(1)
                except NoSuchElementException:
                    # 如果不存在，则点击添加按钮
                    self.browser.find_element_by_xpath("//*[@onclick='appendCmd()']//*[text()='添加']").click()
                finally:
                    self.browser.find_element_by_xpath(login_cmd_field + "/div[2]/div[2]//tr[{}]//a".format(row_num)).click()
                    account_list = self.browser.find_element_by_xpath(
                        "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(lc))
                    action = ActionChains(self.browser)
                    action.move_to_element(account_list).click().perform()
                    log.info("设置登录指令名称: {}".format(lc))
                    row_num += 1

        # 提交
        self.browser.find_element_by_xpath("//*[@id='saveBtn']//*[text()='提交']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warn("保存配置失败，失败提示: {0}".format(msg))
            alert.click_ok()
        set_global_var("ResultMsg", msg, False)
        return True

    def test_terminal(self, terminal_name):
        """
        测试选中终端
        :param terminal_name: 终端名称
        """
        self.choose(terminal_name=terminal_name)
        self.browser.find_element_by_xpath("//*[@id='testSelectedBtn']//*[text()='测试选中网管机']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        msg = alert.get_msg()
        if alert.title_contains("您确定测试选中的网管机吗", auto_click_ok=False):
            alert.click_ok()
            page_wait()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动终端【{}】测试成功".format(terminal_name))
            else:
                log.warn("启动终端【{0}】测试失败，失败提示: {1}".format(terminal_name, msg))
                alert.click_ok()
        else:
            log.warn("启动终端【{0}】测试失败，失败提示: {1}".format(terminal_name, msg))
            alert.click_ok()
        set_global_var("ResultMsg", msg, False)
        return True

    def test_all_terminal(self, condition):
        """
        测试全部终端
        :param condition: 过滤条件，字典
        """
        # 终端名称
        if condition.__contains__("终端名称"):
            terminal_name_key = condition.get("终端名称")
            self.browser.find_element_by_xpath("//*[@id='customName']/following-sibling::span/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='customName']/following-sibling::span/input[1]").send_keys(terminal_name_key)
            log.info("终端名称输入关键字: {}".format(terminal_name_key))

        # 终端类型
        if condition.__contains__("终端类型"):
            terminal_type = condition.get("终端类型")
            self.browser.find_element_by_xpath("//*[@id='loginMode']/following-sibling::span//a").click()
            type_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'loginMode') and text()='{}']".format(terminal_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("终端类型选择: {}".format(terminal_type))

        # 终端IP
        if condition.__contains__("终端IP"):
            terminal_ip = condition.get("终端IP")
            self.browser.find_element_by_xpath("//*[@id='ip']/following-sibling::span/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='ip']/following-sibling::span/input[1]").send_keys(terminal_ip)
            log.info("终端IP输入关键字: {}".format(terminal_ip))

        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        self.browser.find_element_by_xpath("//*[@id='testSelectedBtn']//*[text()='测试选中网管机']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        msg = alert.get_msg()
        if alert.title_contains("您确定测试全部的网管机吗", auto_click_ok=False):
            alert.click_ok()
            page_wait()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("设备测试中,请等待"):
                log.info("启动部分终端测试成功")
            else:
                log.warn("启动部分终端测试失败，失败提示: {}".format(msg))
                alert.click_ok()
        else:
            log.warn("启动部分终端测试失败，失败提示: {}".format(msg))
            alert.click_ok()
        set_global_var("ResultMsg", msg, False)
        return True
