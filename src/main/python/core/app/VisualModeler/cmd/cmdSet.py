# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午4:09

import json
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.level import choose_level
from src.main.python.lib.input import set_textarea
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.regular import RegularCube
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.core.app.VisualModeler.cmd.tplVar import variable_manage


class CmdSet:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("指令配置-指令集")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdSet.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input")))
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

        # 指令名称
        if query.__contains__("指令名称"):
            cmd_name = query.get("指令名称")
            self.browser.find_element(By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='cmdKeyword']/preceding-sibling::input").send_keys(cmd_name)
            log.info("设置指令名称: {0}".format(cmd_name))
            select_item = cmd_name

        # 指令用途
        if query.__contains__("指令用途"):
            cmd_use = query.get("指令用途")
            self.browser.find_element(By.XPATH, "//*[@id='cmdUse']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'cmdUse') and text()='{0}']".format(cmd_use)).click()
            log.info("设置指令用途: {0}".format(cmd_use))

        # 启用状态
        if query.__contains__("启用状态"):
            alive = query.get("启用状态")
            self.browser.find_element(By.XPATH, "//*[@id='isAlive']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'isAlive') and text()='{0}']".format(alive)).click()
            log.info("设置启用状态: {0}".format(alive))

        # 公有指令
        if query.__contains__("公有指令"):
            public_cmd = query.get("公有指令")
            self.browser.find_element(By.XPATH, "//*[@id='isPublicCmd']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'isPublicCmd') and text()='{0}']".format(public_cmd)).click()
            log.info("设置公有指令: {0}".format(public_cmd))

        # 指令来源
        if query.__contains__("指令来源"):
            cmd_from = query.get("指令来源")
            self.browser.find_element(By.XPATH, "//*[@id='isDown']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'isDown') and text()='{0}']".format(cmd_from)).click()
            log.info("设置指令来源: {0}".format(cmd_from))

        # 审批状态
        if query.__contains__("审批状态"):
            check_tag = query.get("审批状态")
            self.browser.find_element(By.XPATH, "//*[@id='checkTag']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'checkTag') and text()='{0}']".format(check_tag)).click()
            log.info("设置审批状态: {0}".format(check_tag))

        # 网元分类
        if query.__contains__("网元分类"):
            level = query.get("网元分类")
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            choose_level(level_list=level)
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            log.info("设置网元分类: {0}".format(level))
            sleep(1)

        # 厂家
        if query.__contains__("厂家"):
            vendor = query.get("厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vendor') and text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModel') and text()='{0}']".format(model)).click()
            log.info("设置设备型号: {0}".format(model))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-query']").click()
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
                        By.XPATH, "//*[@field='cmdName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

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
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='cmdSet-add']")))
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-add']").click()
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
        gbl.temp.set("ResultMsg", msg)

    def update(self, query, cmd_name, cmd_category, cmd_use, public_cmd, sensitive_cmd, cmd_timeout, command, remark,
               rulerx_analyzer, cmd_pagedown, expected_return, sensitive_regex):
        """
        :param query: 查询条件
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
        self.search(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-update']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/gooflow/processInfoEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='process_name']/preceding-sibling::input")))

        self.cmd_page(cmd_name=cmd_name, cmd_category=cmd_category, cmd_use=cmd_use, public_cmd=public_cmd,
                      sensitive_cmd=sensitive_cmd, cmd_timeout=cmd_timeout, command=command, remark=remark,
                      rulerx_analyzer=rulerx_analyzer, cmd_pagedown=cmd_pagedown, expected_return=expected_return,
                      sensitive_regex=sensitive_regex)
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
        gbl.temp.set("ResultMsg", msg)

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

    def delete(self, query):
        """
        :param query: 查询条件
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='cmdSet-del']").click()
        cmd_name = query.get("指令名称")
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
        gbl.temp.set("ResultMsg", msg)

    def _get_status(self, cmd_name):
        """
        获取当前状态
        :param cmd_name: 指令名称
        :return: True/False
        """
        try:
            cmd = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdInfoTab')]//*[text()='{0}']/../../..".format(cmd_name))
            row_index = cmd.get_attribute("datagrid-row-index")
            js = 'return $(".switchbutton")[{0}].checked;'.format(row_index)
            current_status = self.browser.execute_script(js)
        except NoSuchElementException:
            current_status = False
        return current_status

    def update_status(self, query, status, research=True):
        """
        # 启用/禁用
        :param query: 查询条件
        :param status: 状态
        :param research: 是否查询

        # 指令集未被使用时，可以正常启用/禁用
        # 指令集已被使用时，可以启用，无法禁用
        """
        if research:
            self.search(query=query, need_choose=True)
        cmd_name = query.get("指令名称")
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
        else:
            log.info("指令【{0}】状态已经是{1}".format(cmd_name, status))
            msg = "{0}成功".format(status)
        gbl.temp.set("ResultMsg", msg)

    def set_input_param(self, query, params):
        """
        # 输入参数
        :param query: 查询条件
        :param params: 参数信息，列表
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[contains(@class,'selected')]//*[@field='o']//*[@funcid='cmd_inputParam']").click()
        page_wait(10)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'../cmd/inputParamWin.html')]")))
        sleep(1)

        # 参数信息
        for param in params:
            i = 1
            var_info = param.get("变量配置")        # 列表
            var_param = param.get("变量参数")       # 变量参数与输出参数二选一
            output_param = param.get("输出参数")

            # 变量配置
            if var_info:
                for var in var_info:
                    self.browser.find_element(By.XPATH, "//*[@id='varDiv']//*[contains(@class,'add')]").click()
                    page_wait(10)
                    variable_manage(var_mode=var.get("变量模式"), var_name=var.get("变量名称"),
                                    var_type=var.get("变量类型"), var_desc=var.get("变量描述"),
                                    algorithm_list=var.get("运算规则配置"), time_set=var.get("时间配置"),
                                    list_content=var.get("列表内容"), agg_func_set=var.get("聚合函数配置"),
                                    func_set=var.get("功能函数配置"))

            # 变量参数
            if var_param:
                self.browser.find_element(
                    By.XPATH, "//*[@class='args_row'][{}]//*[contains(@class,'addon')]//a".format(i)).click()
                panel_xpath = getPanelXpath()
                self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(var_param)).click()
                log.info("选择变量参数: {}".format(var_param))

            # 输出参数
            if output_param:
                self.browser.find_element(
                    By.XPATH, "//*[@class='args_row'][{}]//a[contains(@id,'searchParam')]".format(i)).click()
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'outputParamListWin.html')]")))
                sleep(1)
                self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").send_keys(output_param)
                self.browser.find_element(By.XPATH, "//*[@id='cmdOutputParam-query']").click()
                page_wait(1)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'cmdOutputParamTab')]//*[@field='paramName']/*[text()='{}']".format(
                        output_param)).click()
                self.browser.find_element(By.XPATH, "//*[@id='cmdOutputParam-ok']").click()
                self.browser.switch_to.parent_frame()
                log.info("选择输出参数: {}".format(output_param))
            sleep(1)
            i += 1

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='inputParam-save']").click()
        alert = BeAlertBox(timeout=3)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("设置输入参数成功")
        else:
            log.warning("设置输入参数失败，失败原因: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def set_output_param(self, query, regex_param=None, table_param=None):
        """
        # 输出参数
        :param query: 查询条件
        :param regex_param: 正则参数，列表
        :param table_param: 二维表参数，列表
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[contains(@class,'selected')]//*[@field='o']//*[@funcid='cmd_outputParam']").click()
        page_wait(10)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'../cmd/outputParamWin.html')]")))
        sleep(1)

        # 正则参数
        if regex_param:
            for rg in regex_param:
                i = 1
                param_name = rg.get("参数名称")
                param_remark = rg.get("参数说明")
                param_flag = rg.get("私有参数")     # 是/否
                regexp_info = rg.get("正则魔方")
                value_type = rg.get("取值")

                self.browser.find_element(By.XPATH, "//*[@id='outputParam-addRegexpParam']").click()
                sleep(1)

                # 获取正则模版id
                _regex_obj = self.browser.find_element(
                    By.XPATH, "//*[@class='border-form' and @parammode='regex'][{}]".format(i))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", _regex_obj)
                regex_id = _regex_obj.get_attribute("id")
                regex_row_xpath = "//*[@class='border-form' and @parammode='regex'][{}]".format(i)

                # 参数名称
                if param_name:
                    self.browser.find_element(
                        By.XPATH,
                        regex_row_xpath + "//*[contains(@class,'paramName')]/following-sibling::span/input[1]".format(
                            i)).clear()
                    self.browser.find_element(
                        By.XPATH,
                        regex_row_xpath + "//*[contains(@class,'paramName')]/following-sibling::span/input[1]".format(
                            i)).send_keys(param_name)

                # 参数说明
                if param_remark:
                    self.browser.find_element(
                        By.XPATH,
                        regex_row_xpath + "//*[contains(@class,'paramDesc')]/following-sibling::span/input[1]".format(
                            i)).clear()
                    self.browser.find_element(
                        By.XPATH,
                        regex_row_xpath + "//*[contains(@class,'paramDesc')]/following-sibling::span/input[1]".format(
                            i)).send_keys(param_remark)

                # 私有参数
                if param_flag:
                    if param_flag == "是":
                        self.browser.find_element(
                            By.XPATH, regex_row_xpath + "//*[@class='paramFlag']".format(i)).click()

                # 正则魔方:
                if regexp_info:
                    regular = RegularCube()
                    confirm_selector = "//*[@id='regexp{}']".format(regex_id)
                    regular.setRegular(set_type=regexp_info.get("设置方式"), regular_name=regexp_info.get("正则模版名称"),
                                       advance_mode=regexp_info.get("高级模式"), regular=regexp_info.get("标签配置"),
                                       expression=regexp_info.get("表达式"), enable_check=regexp_info.get("开启验证"),
                                       check_msg=regexp_info.get("样例数据"), confirm_selector=confirm_selector)

                # 取值
                if value_type:
                    self.browser.find_element(
                        By.XPATH,
                        regex_row_xpath + "//*[contains(@class,'valueType')]/following-sibling::span//a").click()
                    panel_xpath = getPanelXpath(1)
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(value_type)).click()

                i += 1
                sleep(1)

        # 二维表参数
        if table_param:
            for tg in table_param:
                i = 1
                param_name = tg.get("参数名称")
                param_remark = tg.get("参数说明")
                param_flag = tg.get("私有参数")     # 是/否
                analyzer = tg.get("解析模版")
                table_value = tg.get("取值")

                self.browser.find_element(By.XPATH, "//*[@id='outputParam-addTableParam']").click()

                # 获取正则模版id
                _table_obj = self.browser.find_element(
                    By.XPATH, "//*[@class='border-form' and @parammode='table'][{}]".format(i))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", _table_obj)
                table_row_xpath = "//*[@class='border-form' and @parammode='table'][{}]".format(i)

                # 参数名称
                if param_name:
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[contains(@class,'paramName')]/following-sibling::span/input[1]".format(
                            i)).clear()
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[contains(@class,'paramName')]/following-sibling::span/input[1]".format(
                            i)).send_keys(param_name)

                # 参数说明
                if param_remark:
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[contains(@class,'paramDesc')]/following-sibling::span/input[1]".format(
                            i)).clear()
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[contains(@class,'paramDesc')]/following-sibling::span/input[1]".format(
                            i)).send_keys(param_remark)

                # 私有参数
                if param_flag:
                    if param_flag == "是":
                        self.browser.find_element(
                            By.XPATH, table_row_xpath + "//*[@class='paramFlag']".format(i)).click()

                # 解析模版
                if analyzer:
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[contains(@class,'analyzerSelect')]/following-sibling::span//a").click()
                    panel_xpath = getPanelXpath(1)
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(analyzer)).click()
                    sleep(1)

                # 取值
                if table_value:
                    base_value = table_value[0]
                    self.browser.find_element(
                        By.XPATH,
                        table_row_xpath + "//*[@class='tableValueDiv']//*[contains(@class,'addon')]/a").click()
                    panel_xpath = getPanelXpath(2)
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(base_value)).click()

                    if len(table_value) > 1:
                        more_value = table_value[1]
                    else:
                        more_value = None
                    for mv in more_value:   # 元组
                        mi = 1
                        lv, ov = mv
                        self.browser.find_element(
                            By.XPATH,
                            table_row_xpath + "//*[@class='tableValueDiv']//*[contains(@class,'icon-add')]").click()
                        self.browser.find_element(
                            By.XPATH,
                            table_row_xpath + "//*[@class='moreValue']/div[{}]//*[@class='textbox']/input[1]".format(
                                mi)).send_keys(lv)
                        self.browser.find_element(
                            By.XPATH,
                            table_row_xpath + "//*[@class='moreValue']/div[{}]//*[@class='textbox combo']/input[1]".format(
                                mi)).click()
                        panel_xpath = getPanelXpath(2)
                        self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(ov)).click()
                i += 1
                sleep(1)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='outputParam-save']").click()
        alert = BeAlertBox(timeout=3)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("设置输出参数成功")
        else:
            log.warning("设置输出参数失败，失败原因: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, cmd_name, fuzzy_match=False):
        """
        :param cmd_name: 指令名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"指令名称": cmd_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='cmdName']//*[starts-with(@data-mtips,'{}')]".format(cmd_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='cmdName']//*[@data-mtips='{0}']".format(cmd_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            js = 'return $(".cmdInfoTab_datagrid-cell-c1-cmdName")[1].innerText;'
            search_result = self.browser.execute_script(js)
            if self._get_status(search_result):
                self.update_status(query={"指令名称": search_result}, status="禁用", research=False)
            pe.click()
            log.info("选择: {0}".format(search_result))
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='cmdSet-del']").click()
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
                log.warning("{0} 删除失败，失败提示: {1}".format(cmd_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
