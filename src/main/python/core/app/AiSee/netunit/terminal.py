# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:04

import json
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_domain
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class Terminal(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="统一直连终端配置")

        # 切到统一直连终端配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJumpCustomCfgInfo.html')]")))
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

        # 终端名称
        if query.__contains__("终端名称"):
            terminal_name_key = query.get("终端名称")
            self.browser.find_element(By.XPATH, "//*[@id='customName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='customName']/following-sibling::span/input[1]").send_keys(terminal_name_key)
            log.info("终端名称输入关键字: {}".format(terminal_name_key))
            select_item = terminal_name_key

        # 终端类型
        if query.__contains__("终端类型"):
            terminal_type = query.get("终端类型")
            self.browser.find_element(By.XPATH, "//*[@id='loginMode']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(terminal_type)).click()
            log.info("设置终端类型: {}".format(terminal_type))

        # 终端IP
        if query.__contains__("终端IP"):
            terminal_ip = query.get("终端IP")
            self.browser.find_element(By.XPATH, "//*[@id='ip']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='ip']/following-sibling::span/input[1]").send_keys(terminal_ip)
            log.info("终端IP输入关键字: {}".format(terminal_ip))

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
                        By.XPATH, "//*[@field='customName']//*[@data-mtips='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, terminal_name, terminal_type, account_temp, charset, expect_return, fail_return, terminal_ip,
            terminal_port, remark, login_cmd, search_if_exist=True):
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
        :param search_if_exist: 搜索是否存在，存在则修改
        """
        search_if_exist = True if search_if_exist == "是" else False
        if search_if_exist:
            self.search(query={"终端名称": terminal_name}, need_choose=False)
            page_wait()
            sleep(1)
            try:
                # 尝试找到一条记录并点击，点击为了修改时使用
                self.browser.find_element(
                    By.XPATH, "//*[@field='customName']//*[text()='{0}']".format(terminal_name)).click()
                log.info("统一直连终端【{}】已存在，开始修改".format(terminal_name))
                self.update(terminal=None, terminal_name=terminal_name, terminal_type=terminal_type,
                            account_temp=account_temp, charset=charset, expect_return=expect_return,
                            fail_return=fail_return, terminal_ip=terminal_ip, terminal_port=terminal_port,
                            remark=remark, login_cmd=login_cmd)
                return
            except NoSuchElementException:
                log.info("统一直连终端不存在")

        log.info("开始添加统一直连终端")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html')]"))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='customName']/preceding-sibling::input")))
        self.terminal_page(terminal_name=terminal_name, terminal_type=terminal_type, account_temp=account_temp,
                           charset=charset, expect_return=expect_return, fail_return=fail_return,
                           terminal_ip=terminal_ip, terminal_port=terminal_port, remark=remark, login_cmd=login_cmd)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, terminal, terminal_name, terminal_type, account_temp, charset, expect_return, fail_return,
               terminal_ip, terminal_port, remark, login_cmd):
        """
        :param terminal: 终端名称
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
        if terminal:
            self.search(query={"终端名称": terminal}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切到网元管理页面iframe
            wait = WebDriverWait(self.browser, 120)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
            # 切到统一直连终端配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//*[contains(@src,'/html/nu/midJumpCustomCfgInfo.html')]")))
            # 切换到修改终端页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html')]")))
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='customName']/preceding-sibling::input")))
            self.terminal_page(terminal_name=terminal_name, terminal_type=terminal_type, account_temp=account_temp,
                               charset=charset, expect_return=expect_return, fail_return=fail_return,
                               terminal_ip=terminal_ip, terminal_port=terminal_port, remark=remark, login_cmd=login_cmd)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

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

        登录指令
        [
            {
                "操作类型": "删除"
            },
            {
                "操作类型": "添加",
                "指令信息": ""
            },
            {
                "操作类型": "修改",
                "登录指令名称": "",
                "指令信息": ""
            },
            {
                "操作类型": "删除",
                "登录指令名称": ""
            }
        ]
        """
        # 终端名称
        if terminal_name:
            self.browser.find_element(By.XPATH, "//*[@id='customName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='customName']/following-sibling::span[1]/input[1]").send_keys(terminal_name)
            log.info("设置终端名称: {}".format(terminal_name))

        # 终端类型
        if terminal_type:
            self.browser.find_element(By.XPATH, "//*[@id='loginMode']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(terminal_type)).click()
            log.info("设置终端类型: {}".format(terminal_type))

        # 账号名称
        if account_temp:
            self.browser.find_element(By.XPATH, "//*[@id='accountTempId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(account_temp)).click()
            log.info("设置账号名称: {}".format(account_temp))

        # 字符集
        if charset:
            self.browser.find_element(By.XPATH, "//*[@id='charset']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(charset)).click()
            log.info("设置字符集: {}".format(charset))

        # 期待返回符
        if expect_return:
            self.browser.find_element(By.XPATH, "//*[@id='telnetReturn']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='telnetReturn']/following-sibling::span[1]/input[1]").send_keys(expect_return)
            log.info("设置期待返回符: {}".format(expect_return))

        # 失败返回符
        if fail_return:
            self.browser.find_element(By.XPATH, "//*[@id='failReturn']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='failReturn']/following-sibling::span[1]/input[1]").send_keys(fail_return)
            log.info("设置失败返回符: {}".format(fail_return))

        # 终端IP
        if terminal_ip:
            self.browser.find_element(By.XPATH, "//*[@id='terminalIp']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='terminalIp']/following-sibling::span[1]/input[1]").send_keys(terminal_ip)
            log.info("设置终端IP: {}".format(terminal_ip))

        # 终端端口
        if terminal_port:
            self.browser.find_element(By.XPATH, "//*[@id='terminalPort']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='terminalPort']/following-sibling::span[1]/input[1]").send_keys(terminal_port)
            log.info("设置终端端口: {}".format(terminal_port))

        # 用途
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置用途: {}".format(remark))

        # 登录指令
        if login_cmd:
            for cmd in login_cmd:
                opt_type = cmd.get("操作类型")
                obj_cmd = cmd.get("登录指令名称")
                cmd_info = cmd.get("指令信息")
                if opt_type == "添加":
                    self.browser.find_element(By.XPATH, "//*[@onclick='appendCmd()']").click()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@class,'selected')]/*[@field='cmdTempId']//a").click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(cmd_info)).click()
                    log.info("设置登录指令名称: {}".format(cmd_info))

                elif opt_type == "修改":
                    self.browser.find_element(
                        By.XPATH, "//*[@field='command']//*[@data-mtips='{}']".format(obj_cmd)).click()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@class,'selected')]/*[@field='cmdTempId']//a").click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(cmd_info)).click()
                    log.info("设置登录指令名称: {}".format(cmd_info))

                elif opt_type == "删除":
                    if obj_cmd:
                        self.browser.find_element(
                            By.XPATH, "//*[@field='command']//*[@data-mtips='{}']".format(obj_cmd)).click()
                        self.browser.find_element(By.XPATH, "//*[@onclick='deleteCmdRow()']").click()
                        alert = BeAlertBox(back_iframe="default")
                        msg = alert.get_msg()
                        if alert.title_contains("您确定需要删除{}吗".format(obj_cmd), auto_click_ok=False):
                            alert.click_ok()
                            # 切换到网元管理菜单iframe
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
                            # 切换到统一直连终端页面iframe
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'../../html/nu/midJumpCustomCfgInfo.html')]")))
                            # 切换到统一直连终端编辑页面iframe
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html')]")))
                        else:
                            log.warning("删除指令失败，失败提示: {0}".format(msg))
                        gbl.temp.set("ResultMsg", msg)

                    else:  # 不指定指令内容，则删除所有指令
                        record_element = self.browser.find_elements(
                            By.XPATH,
                            "//*[contains(@id,'dg') and not(contains(@style,'transparent'))]//*[@field='cmdTempId']")
                        if len(record_element) == 0:
                            log.info("当前不存在指令需要删除")
                            exist_data = False
                        else:
                            exist_data = True
                        while exist_data:
                            pe = record_element[0]
                            search_result = pe.text
                            pe.click()
                            log.info("选择: {0}".format(search_result))
                            self.browser.find_element(By.XPATH, "//*[@onclick='deleteCmdRow()']").click()
                            alert = BeAlertBox(back_iframe="default")
                            msg = alert.get_msg()
                            if alert.title_contains("您确定需要删除{}吗".format(search_result), auto_click_ok=False):
                                alert.click_ok()
                                page_wait()
                                # 切换到网元管理菜单iframe
                                wait = WebDriverWait(self.browser, 30)
                                wait.until(ec.frame_to_be_available_and_switch_to_it((
                                    By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
                                # 切换到统一直连终端页面iframe
                                wait = WebDriverWait(self.browser, 30)
                                wait.until(ec.frame_to_be_available_and_switch_to_it((
                                    By.XPATH, "//iframe[contains(@src,'../../html/nu/midJumpCustomCfgInfo.html')]")))
                                # 切换到统一直连终端编辑页面iframe
                                wait = WebDriverWait(self.browser, 30)
                                wait.until(ec.frame_to_be_available_and_switch_to_it((
                                    By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html')]")))
                                # 重新获取页面查询结果
                                record_element = self.browser.find_elements(
                                    By.XPATH,
                                    "//*[contains(@id,'dg') and not(contains(@style,'transparent'))]//*[@field='cmdTempId']")
                                if len(record_element) == 0:
                                    log.info("指令清理完成")
                                    exist_data = False
                            else:
                                log.warning("删除指令失败，失败提示: {0}".format(msg))
                                gbl.temp.set("ResultMsg", msg)
                                break

                else:
                    raise KeyError("不支持的操作类型: {}".format(opt_type))

    def test_terminal(self, query):
        """
        测试选中终端
        :param query: 查询条件
        """
        self.search(query=query, need_choose=True)
        if query.__contains__("终端名称"):
            terminal_name = query.get("终端名称")
        else:
            raise KeyError("查询条件需要指明【终端名称】")
        self.browser.find_element(By.XPATH, "//*[@id='testSelectedBtn']").click()
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
                log.warning("启动终端【{0}】测试失败，失败提示: {1}".format(terminal_name, msg))
        else:
            log.warning("启动终端【{0}】测试失败，失败提示: {1}".format(terminal_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def test_all_terminal(self, query):
        """
        测试全部终端
        :param query: 查询条件，字典
        """
        self.search(query=query, need_choose=True)
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@id='testSelectedBtn']").click()
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
                log.warning("启动部分终端测试失败，失败提示: {}".format(msg))
        else:
            log.warning("启动部分终端测试失败，失败提示: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)
