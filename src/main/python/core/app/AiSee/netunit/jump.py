# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:05

import json
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl
from src.main.python.lib.alertBox import BeAlertBox


class JumpCmd(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        choose_menu(menu="统一登录指令配置")

        # 切到统一登录指令配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJumpCmdTempCfgInfo.html')]")))
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

        # 登录指令名称
        if query.__contains__("登录指令名称"):
            cmd_temp_name = query.get("登录指令名称")
            self.browser.find_element(By.XPATH, "//*[@id='cmdTempName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTempName']/following-sibling::span/input[1]").send_keys(cmd_temp_name)
            log.info("登录指令名称输入关键字: {}".format(cmd_temp_name))
            select_item = cmd_temp_name

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
                        By.XPATH, "//*[@field='cmdTempName']//*[@data-mtips='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, cmd_temp_name, remark, jump_cmd):
        """
        :param cmd_temp_name: 登录指令名称
        :param remark: 登录指令用途
        :param jump_cmd: 指令配置
        """
        self.search(query={"登录指令名称": cmd_temp_name}, need_choose=False)
        page_wait()
        sleep(1)
        try:
            self.browser.find_element(By.XPATH, "//*[@field='cmdTempName']//*[@data-mtips='{}']".format(cmd_temp_name))
            log.info("登录指令【{}】存在，开始修改".format(cmd_temp_name))
            self.update(cmd_temp=cmd_temp_name, cmd_temp_name=cmd_temp_name, remark=remark, jump_cmd=jump_cmd)
        except NoSuchElementException:
            log.info("登录指令【{}】不存在，开始添加".format(cmd_temp_name))
            self.browser.find_element(By.XPATH, "//*[@id='addBtn']//*[text()='添加']").click()
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'midJumpCmdTempCfgInfoEdit.html?type=add')]"))
            sleep(1)
            self.cmd_temp_page(cmd_temp_name=cmd_temp_name, remark=remark, jump_cmd=jump_cmd)

    def update(self, cmd_temp, cmd_temp_name, remark, jump_cmd):
        """
        :param cmd_temp: 登录指令
        :param cmd_temp_name: 登录指令名称
        :param remark: 登录指令用途
        :param jump_cmd: 指令配置
        """
        self.search(query={"登录指令名称": cmd_temp}, need_choose=False)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到修改终端页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpCustomCfgInfoEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='accountTempName']/preceding-sibling::input")))
            self.cmd_temp_page(cmd_temp_name=cmd_temp_name, remark=remark, jump_cmd=jump_cmd)

    def cmd_temp_page(self, cmd_temp_name, remark, jump_cmd):
        """
        :param cmd_temp_name: 登录指令名称
        :param remark: 登录指令用途
        :param jump_cmd: 指令配置
        """
        # 登录指令名称
        if cmd_temp_name:
            self.browser.find_element(By.XPATH, "//*[@id='cmdTempName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTempName']/following-sibling::span[1]/input[1]").send_keys(cmd_temp_name)
            log.info("设置登录指令名称: {}".format(cmd_temp_name))

        # 登录指令用途
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置登录指令用途: {}".format(remark))

        # 指令配置
        if jump_cmd:
            cmd_field = "//*[@id='tb']/following-sibling::div[1]"
            row_num = 1

            for cmd in jump_cmd:
                try:
                    row_ele = self.browser.find_element(
                        By.XPATH, cmd_field + "//*[contains(@class,'rownumber') and text()='{}']".format(
                            row_num))
                    # 如果已存在，则单击修改
                    action = ActionChains(self.browser)
                    action.move_to_element(row_ele).click().perform()
                    sleep(1)
                except NoSuchElementException:
                    # 如果不存在，则点击添加按钮
                    self.browser.find_element(By.XPATH, "//*[@onclick='appendCmd()']").click()
                finally:
                    self.set_cmd(cmd=cmd.get("指令内容"), account=cmd.get("账号名称"), expected_str=cmd.get("期待返回符"),
                                 failed_str=cmd.get("失败返回符"), hide_input_cmd=cmd.get("隐藏输入指令"),
                                 hide_return=cmd.get("隐藏指令返回"), quit_cmd=cmd.get("退出命令"),
                                 sleep_time=cmd.get("执行后等待时间"), translate_netunit=cmd.get("是否适配网元"),
                                 charset=cmd.get("字符集"), line_break=cmd.get("换行符"), cmd_field=cmd_field)
                    row_num += 1

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

    def set_cmd(self, cmd, account, expected_str, failed_str, hide_input_cmd, hide_return, quit_cmd, sleep_time,
                translate_netunit, charset, line_break, cmd_field):
        """
        :param cmd: 指令内容
        :param account: 账号名称
        :param expected_str: 期待返回符
        :param failed_str: 失败返回符
        :param hide_input_cmd: 隐藏输入指令
        :param hide_return: 隐藏指令返回
        :param quit_cmd: 退出命令
        :param sleep_time: 执行后等待时间
        :param translate_netunit: 是否适配网元
        :param charset: 字符集
        :param line_break: 换行符
        :param cmd_field:
        :return:
        """
        # 指令内容
        if cmd:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").send_keys(cmd)
            log.info("设置指令内容: {}".format(cmd))

        # 账号名称
        if account:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='accountTempId']//a").click()
            account_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(account))
            action = ActionChains(self.browser)
            action.move_to_element(account_list).click().perform()
            log.info("设置账号名称: {}".format(account))

        # 期待返回符
        if expected_str:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").send_keys(expected_str)
            log.info("设置期待返回符: {}".format(expected_str))

        # 失败返回符
        if failed_str:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").send_keys(
                failed_str)
            log.info("设置失败返回符: {}".format(failed_str))

        # 隐藏输入指令
        if hide_input_cmd:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='sensitiveCmd']//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[text()='{}']".format(hide_input_cmd)).click()
            log.info("设置隐藏输入指令: {}".format(hide_input_cmd))

        # 隐藏指令返回
        if hide_return:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").send_keys(hide_return)
            log.info("设置隐藏指令返回: {}".format(hide_return))

        # 退出命令
        if quit_cmd:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").send_keys(quit_cmd)
            log.info("设置退出命令: {}".format(quit_cmd))

        # 执行后等待时间
        if sleep_time:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").send_keys(sleep_time)
            log.info("设置执行后等待时间: {}".format(sleep_time))

        # 是否适配网元
        if translate_netunit:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='translateNetunit']//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[text()='{}']".format(translate_netunit)).click()
            log.info("设置是否适配网元: {}".format(translate_netunit))

        # 字符集
        if charset:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='charset']//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[text()='{}']".format(charset)).click()
            log.info("设置字符集: {}".format(charset))

        # 换行符
        if line_break:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='lineBreak']//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[text()='{}']".format(line_break)).click()
            log.info("设置换行符: {}".format(line_break))
