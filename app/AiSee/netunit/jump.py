# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:05

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


class JumpCmd(object):

    def __init__(self):
        self.browser = get_global_var("browser")
        choose_menu(menu="统一登录指令配置")

        # 切到统一登录指令配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJumpCmdTempCfgInfo.html')]")))
        page_wait()
        sleep(1)

    def choose(self, cmd_name):
        """
        :param cmd_name: 登录指令名称
        """
        input_ele = self.browser.find_element_by_xpath(
            "//*[@id='cmdTempName']/following-sibling::span/input[1]")
        input_ele.clear()
        input_ele.send_keys(cmd_name)
        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        self.browser.find_element_by_xpath(
            "//*[@field='cmdTempName']//*[@data-mtips='{}']".format(cmd_name)).click()
        log.info("已选登录指令: {}".format(cmd_name))

    def add(self, cmd_name, remark, cmd):
        """
        :param cmd_name: 登录指令名称
        :param remark: 登录指令用途
        :param cmd: 指令配置
        """
        self.browser.find_element_by_xpath("//*[@id='cmdTempName']/following-sibling::span/input[1]").clear()
        self.browser.find_element_by_xpath("//*[@id='cmdTempName']/following-sibling::span/input[1]").send_keys(cmd_name)
        self.browser.find_element_by_xpath("//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        sleep(1)
        result = False
        try:
            self.browser.find_element_by_xpath("//*[@field='cmdTempName']//*[text()='{0}']".format(cmd_name))
            log.info("登录指令【{}】存在，开始修改".format(cmd_name))
            result = self.update(obj_cmd=cmd_name, cmd_name=cmd_name, remark=remark, cmd=cmd)
        except NoSuchElementException:
            log.info("登录指令【{}】不存在，开始添加".format(cmd_name))
            self.browser.find_element_by_xpath("//*[@id='addBtn']//*[text()='添加']").click()
            self.browser.switch_to.frame(
                self.browser.find_element_by_xpath("//iframe[contains(@src,'midJumpCmdTempCfgInfoEdit.html?type=add')]"))
            sleep(1)
            result = self.jump_cmd_page(cmd_name=cmd_name, remark=remark, cmd=cmd)
        finally:
            return result

    def update(self, obj_cmd, cmd_name, remark, cmd):
        """
        :param obj_cmd: 目标登录指令
        :param cmd_name: 登录指令名称
        :param remark: 登录指令用途
        :param cmd: 指令配置
        """
        self.choose(cmd_name=obj_cmd)
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
            result = self.jump_cmd_page(cmd_name=cmd_name, remark=remark, cmd=cmd)

            return result

    def jump_cmd_page(self, cmd_name, remark, cmd):
        """
        :param cmd_name: 登录指令名称
        :param remark: 登录指令用途
        :param cmd: 指令配置
        """
        # 登录指令名称
        if cmd_name:
            self.browser.find_element_by_xpath("//*[@id='cmdTempName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='cmdTempName']/following-sibling::span[1]/input[1]").send_keys(cmd_name)
            log.info("设置登录指令名称: {}".format(cmd_name))

        # 登录指令用途
        if remark:
            self.browser.find_element_by_xpath("//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置登录指令用途: {}".format(remark))

        # 指令配置
        if cmd:
            cmd_field = "//*[@id='tb']/following-sibling::div[1]"
            row_num = 1

            for c in cmd:
                try:
                    row_ele = self.browser.find_element_by_xpath(
                        cmd_field + "//*[contains(@class,'rownumber') and text()='{}']".format(
                            row_num))
                    # 如果已存在，则单击修改
                    action = ActionChains(self.browser)
                    action.move_to_element(row_ele).click().perform()
                    sleep(1)
                except NoSuchElementException:
                    # 如果不存在，则点击添加按钮
                    self.browser.find_element_by_xpath("//*[@onclick='appendCmd()']//*[text()='添加']").click()
                finally:
                    self.set_cmd(cmd=c.get("指令内容"), account=c.get("账号名称"), expected_str=c.get("期待返回符"),
                                 failed_str=c.get("失败返回符"), hide_input_cmd=c.get("隐藏输入指令"),
                                 hide_return=c.get("隐藏指令返回"), quit_cmd=c.get("退出命令"),
                                 sleep_time=c.get("执行后等待时间"), translate_netunit=c.get("是否适配网元"),
                                 charset=c.get("字符集"), line_break=c.get("换行符"), cmd_field=cmd_field)
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
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").send_keys(cmd)
            log.info("设置指令内容: {}".format(cmd))

        # 账号名称
        if account:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='accountTempId']//a").click()
            account_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(account))
            action = ActionChains(self.browser)
            action.move_to_element(account_list).click().perform()
            log.info("设置账号名称: {}".format(account))

        # 期待返回符
        if expected_str:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").send_keys(expected_str)
            log.info("设置期待返回符: {}".format(expected_str))

        # 失败返回符
        if failed_str:
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").send_keys(failed_str)
            log.info("设置失败返回符: {}".format(failed_str))

        # 隐藏输入指令
        if hide_input_cmd:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='sensitiveCmd']//a").click()
            hide_input_cmd_list = self.browser.find_elements_by_xpath(
                "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(hide_input_cmd))
            for e in hide_input_cmd_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置隐藏输入指令: {}".format(hide_input_cmd))
                    break

        # 隐藏指令返回
        if hide_return:
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").send_keys(hide_return)
            log.info("设置隐藏指令返回: {}".format(hide_return))

        # 退出命令
        if quit_cmd:
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").send_keys(quit_cmd)
            log.info("设置退出命令: {}".format(quit_cmd))

        # 执行后等待时间
        if sleep_time:
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element_by_xpath(
                cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").send_keys(sleep_time)
            log.info("设置执行后等待时间: {}".format(sleep_time))

        # 是否适配网元
        if translate_netunit:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='translateNetunit']//a").click()
            translate_netunit_list = self.browser.find_elements_by_xpath(
                "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(translate_netunit))
            for e in translate_netunit_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置是否适配网元: {}".format(translate_netunit))
                    break

        # 字符集
        if charset:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='charset']//a").click()
            charset_list = self.browser.find_elements_by_xpath(
                "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(charset))
            for e in charset_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置字符集: {}".format(charset))
                    break

        # 换行符
        if line_break:
            self.browser.find_element_by_xpath(cmd_field + "//*[@field='lineBreak']//a").click()
            line_break_list = self.browser.find_elements_by_xpath(
                "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(line_break))
            for e in line_break_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置换行符: {}".format(line_break))
                    break
