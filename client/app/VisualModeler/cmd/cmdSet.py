# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午4:09

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from client.page.func.alertBox import BeAlertBox
from client.page.func.level import choose_level
from client.page.func.input import set_textarea
from time import sleep
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.func.pageMaskWait import page_wait
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class CmdSet:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("指令配置-指令集")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdSet.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def search(self, cmd_name=None, cmd_use=None, alive=None, public_cmd=None, cmd_from=None, check_tag=None,
               level=None, vendor=None, model=None):
        """
        # 查询。指令名称/网元分类/厂家/设备型号可确定唯一指令
        :param cmd_name: 指令名称
        :param cmd_use: 指令用途
        :param alive: 启用状态
        :param public_cmd: 公有指令
        :param cmd_from: 指令来源
        :param check_tag: 审批状态
        :param level: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :return:
        """
        # 指令名称
        if cmd_name:
            self.browser.find_element(By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input").send_keys(cmd_name)
            log.info("设置指令名称: {0}".format(cmd_name))

        # 指令用途
        if cmd_use:
            self.browser.find_element(By.XPATH, "//*[@id='cmdUse']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'cmdUse') and text()='{0}']".format(cmd_use)).click()
            log.info("设置指令用途: {0}".format(cmd_use))

        # 启用状态
        if alive:
            self.browser.find_element(By.XPATH, "//*[@id='isAlive']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'isAlive') and text()='{0}']".format(alive)).click()
            log.info("设置启用状态: {0}".format(alive))

        # 公有指令
        if public_cmd:
            self.browser.find_element(By.XPATH, "//*[@id='isPublicCmd']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'isPublicCmd') and text()='{0}']".format(public_cmd)).click()
            log.info("设置公有指令: {0}".format(public_cmd))

        # 指令来源
        if cmd_from:
            self.browser.find_element(By.XPATH, "//*[@id='isDown']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'isDown') and text()='{0}']".format(cmd_from)).click()
            log.info("设置指令来源: {0}".format(cmd_from))

        # 审批状态
        if check_tag:
            self.browser.find_element(By.XPATH, "//*[@id='checkTag']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'checkTag') and text()='{0}']".format(check_tag)).click()
            log.info("设置审批状态: {0}".format(check_tag))

        # 网元分类
        if level:
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            choose_level(level_list=level)
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            log.info("设置网元分类: {0}".format(level))
            sleep(1)

        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vendor') and text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModel') and text()='{0}']".format(model)).click()
            log.info("设置设备型号: {0}".format(model))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-query']").click()
        page_wait()

        # 判断是否有谈出口
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.warning("查询提示: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)
            return False

        # 判断查询是有有结果
        try:
            self.browser.find_element(
                By.XPATH, "//*[@class='datagrid-body']//*[contains(@id,'cmdInfoTab')]//*[@class='datagrid-cell-rownumber' and text()='1']")
            log.info("查询有结果")
            return True
        except NoSuchElementException:
            log.info("查询无结果")
            return None

    def choose(self, cmd_name, level, vendor, model):
        """
        :param cmd_name: 指令名称
        :param level: 网元分类，数组
        :param vendor: 厂家
        :param model: 设备型号
        """
        search_result = self.search(cmd_name=cmd_name, level=level, vendor=vendor, model=model)
        if search_result:
            self.browser.find_element(
                By.XPATH, "//*[@field='cmdName']/*[contains(@class,'cmdName')]/*[text()='{}']".format(cmd_name)).click()
            log.info("选择指令：{0}".format(cmd_name))
        elif search_result is None:
            raise Exception("所选指令不存在, 指令名称: {0}".format(cmd_name))
        else:
            raise Exception("查询异常")

    def add(self, cmd_name, cmd_category, cmd_use, level, vendor, model, login_type, public_cmd, sensitive_cmd,
            personal_cmd, cmd_timeout, command, remark, rulerx_analyzer, cmd_pagedown, expected_return, sensitive_regex):
        """
        :param cmd_name: 指令名称
        :param cmd_category: 指令类别
        :param cmd_use: 指令用途
        :param level: 网元分类
        :param vendor: 厂家
        :param model: 设备型号，数组，支持多选
        :param login_type: 登录模式
        :param public_cmd: 公有指令
        :param sensitive_cmd: 隐藏输入指令
        :param personal_cmd: 个性指令
        :param cmd_timeout: 指令等待超时
        :param command: 指令
        :param remark: 说明
        :param rulerx_analyzer: 指令解析模版，数组
        :param cmd_pagedown: 指令翻页符
        :param expected_return: 期待返回的结束符
        :param sensitive_regex: 隐藏指令返回

        {
            "操作": "",
            "参数": {
                "指令名称": "自动化指令_不带参数",
                "指令类别": "不带参数指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": "",
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping wwww.baidu.com -c 5"]
                "说明": "ping百度",
                "指令解析模版": "",
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        """
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='添加']")))
        self.browser.find_element(By.XPATH, "//*[text()='添加']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/cmd/cmdSetEditWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='cmdName']/following-sibling::span/input[1]")))

        self.cmd_page(cmd_name=cmd_name, cmd_category=cmd_category, cmd_use=cmd_use, level=level, vendor=vendor,
                      model=model, login_type=login_type, public_cmd=public_cmd, sensitive_cmd=sensitive_cmd,
                      personal_cmd=personal_cmd, cmd_timeout=cmd_timeout, command=command, remark=remark,
                      rulerx_analyzer=rulerx_analyzer, cmd_pagedown=cmd_pagedown, expected_return=expected_return,
                      sensitive_regex=sensitive_regex)

    def update(self, cmd_info, cmd_name, cmd_category, cmd_use, public_cmd, sensitive_cmd, cmd_timeout, command, remark,
               rulerx_analyzer, cmd_pagedown, expected_return, sensitive_regex):
        """
        :param cmd_info: 指令信息
        :param cmd_name: 指令名称
        :param cmd_category: 指令类别
        :param cmd_use: 指令用途
        :param public_cmd:  公有指令
        :param sensitive_cmd:  隐藏输入指令
        :param cmd_timeout:  指令等待超时
        :param command:  指令
        :param remark:  说明
        :param rulerx_analyzer:  指令解析模版，数组
        :param cmd_pagedown:  指令翻页符
        :param expected_return:  期待返回的结束符
        :param sensitive_regex:  隐藏指令返回
        """
        if not isinstance(cmd_info, dict):
            raise ValueError
        self.choose(cmd_name=cmd_info.get("指令名称"), level=cmd_info.get("网元分类"), vendor=cmd_info.get("厂家"),
                    model=cmd_info.get("设备型号"))
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/gooflow/processInfoEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='process_name']/preceding-sibling::input")))

        self.cmd_page(cmd_name=cmd_name, cmd_category=cmd_category, cmd_use=cmd_use, public_cmd=public_cmd,
                      sensitive_cmd=sensitive_cmd, cmd_timeout=cmd_timeout, command=command, remark=remark,
                      rulerx_analyzer=rulerx_analyzer, cmd_pagedown=cmd_pagedown, expected_return=expected_return,
                      sensitive_regex=sensitive_regex)

    def cmd_page(self, cmd_name, cmd_category, cmd_use,  public_cmd, sensitive_cmd, cmd_timeout, command, remark,
                 rulerx_analyzer, cmd_pagedown, expected_return, sensitive_regex, level=None, vendor=None,
                 model=None, login_type=None, personal_cmd=None):
        """
        :param cmd_name: 指令名称
        :param cmd_category: 指令类别
        :param cmd_use: 指令用途
        :param level: 网元分类，数组
        :param vendor: 厂家
        :param model:  设备型号
        :param login_type:  登录模式
        :param public_cmd:  公有指令
        :param sensitive_cmd:  隐藏输入指令
        :param personal_cmd:  个性指令
        :param cmd_timeout:  指令等待超时
        :param command:  指令
        :param remark:  说明
        :param rulerx_analyzer:  指令解析模版，数组
        :param cmd_pagedown:  指令翻页符
        :param expected_return:  期待返回的结束符
        :param sensitive_regex:  隐藏指令返回
        """
        # 指令名称
        if cmd_name:
            self.browser.find_element(By.XPATH, "//*[@id='cmdName']/following-sibling::span/input[1]").send_keys(cmd_name)
            log.info("设置指令名称: {0}".format(cmd_name))

        # 指令类别
        if cmd_category:
            self.browser.find_element(By.XPATH, "//*[@id='cmdCategory']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdCategory') and text()='{}']".format(cmd_category)).click()
            log.info("设置指令类别: {0}".format(cmd_category))

        # 指令用途
        if cmd_use:
            self.browser.find_element(By.XPATH, "//*[@id='cmdUse']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'cmdUse') and text()='{}']".format(cmd_use)).click()
            log.info("设置指令用途: {0}".format(cmd_use))

        # 网元分类
        if level:
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            choose_level(level_list=level)
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            log.info("设置网元分类: {0}".format(level))

        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span[1]//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vendor') and text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span[1]//a").click()
            page_wait()
            sleep(1)
            if model != "全选":
                self.browser.find_element(By.XPATH, "//*[contains(@class,'checkAll') and contains(text(),'全选')]").click()
                sleep(1)
                for m in model:
                    self.browser.find_element(
                        By.XPATH, "//*[@id='cmdInfoForm']/following-sibling::div[5]//*[contains(@id,'netunitModel') and text()='{0}']".format(
                            m)).click()
                    log.info("设置设备型号: {0}".format(m))
            else:
                log.info("设置设备型号: 全选")
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span[1]//a").click()

        # 登录模式
        if login_type:
            self.browser.find_element(By.XPATH, "//*[@id='loginType']/following-sibling::span[1]//a").click()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'loginTypeSelectWin.html')]")))
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
            page_wait()

            self.browser.find_element(
                By.XPATH, "//*[@id='loginTypeTb']/following-sibling::div[1]//*[@field='loginTypeName']/*[contains(@class,'loginTypeName') and text()='{}']".format(
                    login_type)).click()
            self.browser.find_element(By.XPATH, "//*[@id='loginType-ok']//span[text()='确定']").click()
            self.browser.switch_to.parent_frame()
            log.info("设置登录模式: {0}".format(login_type))

        # 公有指令
        if public_cmd:
            self.browser.find_element(
                By.XPATH, "//*[@name='isPublicCmd']/following-sibling::span[text()='{}']".format(public_cmd)).click()
            log.info("设置公有指令: {0}".format(public_cmd))

        # 隐藏输入指令
        if sensitive_cmd:
            self.browser.find_element(
                By.XPATH, "//*[@name='sensitiveCmd']/following-sibling::span[text()='{}']".format(sensitive_cmd)).click()
            log.info("设置隐藏输入指令: {0}".format(sensitive_cmd))

        # 个性指令
        if personal_cmd:
            self.browser.find_element(
                By.XPATH, "//*[@name='cmdType']/following-sibling::span[text()='{}']".format(personal_cmd)).click()
            log.info("设置个性指令: {0}".format(personal_cmd))

        # 指令等待超时
        if cmd_timeout:
            self.browser.find_element(By.XPATH, "//*[@id='timeOut']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='timeOut']/following-sibling::span/input[1]").send_keys(cmd_timeout)
            log.info("设置指令等待超时: {0}".format(cmd_timeout))

        # 指令
        if command:
            cmd_textarea = self.browser.find_element(By.XPATH, "//*[@id='command']/following-sibling::span/textarea")
            action = ActionChains(self.browser)
            action.move_to_element(cmd_textarea).perform()
            set_textarea(cmd_textarea, command)
            log.info("设置指令: {0}".format('\n'.join(command)))

        # 说明
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/textarea")
            action = ActionChains(self.browser)
            action.move_to_element(remark_textarea).perform()
            set_textarea(remark_textarea, remark)
            if isinstance(remark, list):
                log.info("设置说明: {0}".format('\n'.join(remark)))
            else:
                log.info("设置说明: {0}".format(remark))

        # 指令解析模版
        if rulerx_analyzer:
            for analyzer in rulerx_analyzer:
                self.browser.find_element(By.XPATH, "//*[@id='rulerxAnalyzer']/following-sibling::span[1]//a").click()
                self.set_cmd_analyzer(analyzer)
                sleep(1)
            log.info("设置指令解析模版: {0}".format(", ".join(rulerx_analyzer)))

        # 指令翻页符
        if cmd_pagedown:
            self.browser.find_element(By.XPATH, "//*[@id='cmdPageDownStr']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='cmdPageDownStr']/following-sibling::span/input[1]").send_keys(
                cmd_pagedown)
            log.info("设置指令翻页符: {0}".format(cmd_pagedown))

        # 期待返回的结束符
        if expected_return:
            self.browser.find_element(By.XPATH, "//*[@id='readUntil']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='readUntil']/following-sibling::span/input[1]").send_keys(
                expected_return)
            log.info("设置期待返回的结束符: {0}".format(expected_return))

        # 隐藏指令返回
        if sensitive_regex:
            self.browser.find_element(By.XPATH, "//*[@id='sensitiveRegex']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='sensitiveRegex']/following-sibling::span/input[1]").send_keys(
                sensitive_regex)
            log.info("设置隐藏指令返回: {0}".format(sensitive_regex))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-submit']").click()
        alert = BeAlertBox()
        if alert.exist_alert:
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("指令集保存成功")
            else:
                log.warning("指令集保存失败，失败提示: {0}".format(msg))
        else:
            log.warning("没有弹出框提示信息")
            msg = None
        set_global_var("ResultMsg", msg, False)

    def set_cmd_analyzer(self, analyzer):
        """
        :param analyzer: 指令解析模版
        """
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'rulerxTmplSelectWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]")))

        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]").send_keys(analyzer)
        self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-query']//span[text()='查询']").click()
        page_wait()
        self.browser.find_element(
            By.XPATH, "//*[@id='rulerxTmplTb']/following-sibling::div[1]//*[@field='analyzerName']/*[contains(@class,'analyzerName')]/*[text()='{}']".format(
                analyzer)).click()
        self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-ok']//span[text()='确定']").click()
        self.browser.switch_to.parent_frame()
        log.info("选择指令解析模版: {}".format(analyzer))

    def delete(self, cmd_info):
        """
        :param cmd_info: 指令信息
        """
        if not isinstance(cmd_info, dict):
            raise ValueError
        cmd_name = cmd_info.get("指令名称")
        level = cmd_info.get("网元分类")
        vendor = cmd_info.get("厂家")
        model = cmd_info.get("设备型号")
        self.choose(cmd_name, level, vendor, model)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(cmd_name, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} 删除成功".format(cmd_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(cmd_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(cmd_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update_status(self, cmd_info, status):
        """
        # 启用/禁用
        :param cmd_info: 指令信息
        :param status: 状态

        # 指令集未被使用时，可以正常启用/禁用
        # 指令集已被使用时，可以启用，无法禁用
        """
        if not isinstance(cmd_info, dict):
            raise ValueError
        cmd_name = cmd_info.get("指令名称")
        level = cmd_info.get("网元分类")
        vendor = cmd_info.get("厂家")
        model = cmd_info.get("设备型号")
        self.choose(cmd_name, level, vendor, model)
        cmd = self.browser.find_element(
            By.XPATH, "//*[contains(@id,'cmdInfoTab')]//*[text()='{0}']/../../..".format(cmd_name))
        row_index = cmd.get_attribute("datagrid-row-index")
        js = 'return $(".switchbutton")[{0}].checked;'.format(row_index)
        current_status = self.browser.execute_script(js)

        tmp = True if status == "启用" else False
        if tmp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdInfoTab')]//*[text()='{0}']/../../following-sibling::td[4]//*[@class='switchbutton']".format(
                    cmd_name)).click()
            log.info("{0}指令: {1}".format(status, cmd_name))

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("启用成功"):
                # 启用指令模版成功
                log.info("启用指令成功")
            elif alert.title_contains("禁用成功"):
                log.info("启用指令成功")
            else:
                log.warning("{0}指令失败，失败原因: {1}".format(status, msg))
            set_global_var("ResultMsg", msg, False)
        else:
            log.info("指令【{0}】状态已经是{1}".format(cmd_name, status))
            msg = "{0}成功".format(status)
            set_global_var("ResultMsg", msg, False)

    def data_clear(self, cmd_name, fuzzy_match=False):
        """
        :param cmd_name: 指令名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='cmdKeyword']/following-sibling::span/input[1]")))
        self.browser.find_element(By.XPATH, "//*[@id='cmdKeyword']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='cmdKeyword']/following-sibling::span/input[1]").send_keys(cmd_name)
        self.browser.find_element(By.XPATH, "//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        sleep(1)
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='cmdName']//*[starts-with(@data-mtips,'{}')]".format(cmd_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='cmdName']//*[@data-mtips='{0}']".format(cmd_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                js = 'return $(".cmdInfoTab_datagrid-cell-c1-cmdName")[1].innerText;'
                search_result = self.browser.execute_script(js)
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
                                By.XPATH, "//*[@field='cmdName']//*[starts-with(@data-mtips,'{}')]".format(cmd_name))
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
                    log.warning("{0} 删除失败，失败提示: {1}".format(cmd_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
