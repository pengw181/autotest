# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午4:09

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class CmdTemplate:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("指令配置-指令模版")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmpl.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='templName']/following-sibling::span/input")))
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

        # 模版名称
        if query.__contains__("模版名称"):
            temp_name = query.get("模版名称")
            self.browser.find_element(By.XPATH, "//*[@id='templName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='templName']/following-sibling::span/input[1]").send_keys(temp_name)
            select_item = temp_name

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").send_keys(creator)

        # 模版启用
        if query.__contains__("模版启用"):
            temp_status = query.get("模版启用")
            self.browser.find_element(By.XPATH, "//*[@id='templStatus']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(temp_status)).click()

        # 开始时间
        if query.__contains__("开始时间"):
            begin_time = query.get("开始时间")
            self.browser.find_element(By.XPATH, "//*[@id='startTime']/following-sibling::span//a").click()
            if isinstance(begin_time, dict):
                # 间隔，0表示当前，正数表示未来，负数表示过去
                time_interval = begin_time.get("间隔")
                # 单位，年、月、天、时、分、秒
                time_unit = begin_time.get("单位")
                begin_time = calculation(interval=time_interval, unit=time_unit)
            else:
                raise AttributeError("开始时间必须是字典")
            set_calendar(date_s=begin_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("设置开始时间: {0}".format(begin_time))

        # 结束时间
        if query.__contains__("结束时间"):
            end_time = query.get("结束时间")
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
            log.info("设置结束时间: {0}".format(end_time))

        # 网络层级
        if query.__contains__("网络层级"):
            level = query.get("网络层级")
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(level)).click()

        # 选择方式
        if query.__contains__("选择方式"):
            sel_mode = query.get("选择方式")
            self.browser.find_element(By.XPATH, "//*[@id='selMode']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(sel_mode)).click()

        # 专业领域
        if query.__contains__("专业领域"):
            field = query.get("专业领域")
            self.browser.find_element(By.XPATH, "//*[@id='templTypeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            for f in field:
                self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(f)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-query']").click()
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
                        By.XPATH, "//*[@field='templName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, template_name, field, levels, mode, remark):
        """
        :param template_name: 模版名称
        :param field: 专业领域
        :param levels: 网络层级
        :param mode: 选择方式
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-add']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmplEditWin.html')]")))
        page_wait(2)
        self.basicInfoPage(template_name, field, levels, mode, remark)

    def update(self, template_name, basic_info, auto_follow_strategy, bind_ne, bind_ne_level, bind_cmd):
        """
        # 4个tab页面，每次只修改其中一个
        :param template_name: 模版名称
        :param basic_info: 模版基本信息
        :param auto_follow_strategy: 自动跟进策略配置
        :param bind_ne: 模版网元绑定
        :param bind_ne_level: 模版网元类型绑定
        :param bind_cmd: 模版指令绑定
        """
        self.search(query={"模版名称": template_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-update']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.warning("修改指令模版失败，失败原因: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmplEditWin.html')]")))
            page_wait(1)

            # 模版基本信息
            if basic_info:
                template_name = basic_info.get("模版名称")
                fields = basic_info.get("模版名称")
                mode = basic_info.get("选择方式")
                remark = basic_info.get("备注")
                self.basicInfoPage(template_name, fields, None, mode, remark)
                return

            # 自动跟进策略配置
            if auto_follow_strategy:
                enable = auto_follow_strategy.get("状态")
                follow_scope = auto_follow_strategy.get("跟进范围")
                follow_period = auto_follow_strategy.get("跟进周期")
                follow_time = auto_follow_strategy.get("跟进次数")
                self.autoFollowUpStrategy(enable, follow_scope, follow_period, follow_time)
                return

            # 模版网元绑定
            if bind_ne:
                netunit_name = bind_ne.get("网元名称")
                levels = bind_ne.get("网元分类")
                vendor = bind_ne.get("厂家")
                model = bind_ne.get("设备型号")
                level_type = bind_ne.get("网元类型")
                unassigned_list = bind_ne.get("待分配网元")
                self.templateBindNE(netunit_name, levels, vendor, model, level_type, unassigned_list)
                return

            # 模版网元类型绑定
            if bind_ne_level:
                unassigned_list = bind_ne_level.get("待分配网元类型")
                self.templateBindNELevel(unassigned_list)
                return

            # 模版指令绑定
            if bind_cmd:
                cmd_name = bind_cmd.get("指令名称")
                levels = bind_cmd.get("网元分类")
                vendor = bind_cmd.get("厂家")
                model = bind_cmd.get("设备型号")
                unassigned_list = bind_cmd.get("待分配指令")
                self.templateBindCmd(cmd_name, levels, vendor, model, unassigned_list)
                return

    def basicInfoPage(self, template_name, fields, levels, mode, remark):
        """
        # 模版基本信息
        :param template_name: 模版名称
        :param fields: 专业领域
        :param levels: 网络层级，不可修改
        :param mode: 选择方式
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版基本信息']").click()
        sleep(1)

        # 模版名称
        if template_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='templName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='templName']/following-sibling::span/input[1]").send_keys(
                template_name)
            log.info("设置模版名称: {0}".format(template_name))

        # 专业领域
        if fields:
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='templTypeId']/following-sibling::span//a").click()
            selected_fields = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'templTypeId') and contains(@class,'selected')]")
            if len(selected_fields):
                for element in selected_fields:
                    element.click()
            if not isinstance(fields, list):
                raise TypeError("专业领域非数组格式")
            for f in fields:
                self.browser.find_element(
                    By.XPATH, "//*[@id='cmdTmplTabs']/following-sibling::div//*[contains(@id,'templTypeId') and text()='{0}']".format(
                        f)).click()
                log.info("选择专业领域: {0}".format(f))

        # 网络层级
        if levels:
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='level']/following-sibling::span//a").click()
            if not isinstance(levels, list):
                raise TypeError("网络层级非数组格式")
            for lev in levels:
                self.browser.find_element(
                    By.XPATH, "//*[@id='cmdTmplTabs']/following-sibling::div//*[@class='tree-title' and text()='{0}']".format(
                        lev)).click()
                log.info("选择网络层级: {0}".format(lev))

        # 选择方式
        if mode:
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='selMode']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplTabs']/following-sibling::div//*[contains(@id,'selMode') and text()='{0}']".format(
                    mode)).click()
            log.info("选择方式: {0}".format(mode))

        # 备注
        if remark:
            textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span/textarea")
            set_textarea(textarea=textarea, msg=remark)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-saveTmpl']").click()
        alert = BeAlertBox(timeout=10)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存指令模版成功")
        else:
            log.warning("保存指令模版失败，失败原因: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def autoFollowUpStrategy(self, enable, follow_scope, follow_period, follow_time):
        """
        # 自动跟进策略配置
        :param enable: 状态，启用/禁用
        :param follow_scope: 跟进范围
        :param follow_period: 跟进周期
        :param follow_time: 跟进次数
        """
        log.info("自动跟进策略配置")
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='自动跟进策略配置']").click()
        sleep(1)

        js = 'return $("#isFollowUp")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【启用自动跟进策略】勾选状态: {0}".format(status))

        # 状态
        if enable:
            tmp = True if enable == "启用" else False
            if tmp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='isFollowUp']").click()
                log.info("【{0}】自动跟进策略".format(enable))

        # 跟进范围
        if follow_scope:
            self.browser.find_element(By.XPATH, "//*[@id='followUpScope']/following-sibling::span//a").click()
            selected_elements = self.browser.find_elements(By.XPATH, "//*[contains(@class,'tree-checkbox1')]")
            for element in selected_elements:
                element.click()
            for result in follow_scope:
                self.browser.find_element(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(result)).click()
                log.info("跟进范围选择: {0}".format(result))
            self.browser.find_element(By.XPATH, "//*[@id='followUpScope']/following-sibling::span//a").click()

        # 跟进周期
        if follow_period:
            self.browser.find_element(By.XPATH, "//*[@id='followUpPeriod']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='followUpPeriod']/following-sibling::span/input[1]").send_keys(follow_period)
            log.info("设置跟进周期: {0}".format(follow_period))

        # 跟进次数
        if follow_time:
            self.browser.find_element(By.XPATH, "//*[@id='followUpTime']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='followUpTime']/following-sibling::span/input[1]").send_keys(follow_time)
            log.info("设置跟进次数: {0}".format(follow_time))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-saveFollowUp']").click()
        alert = BeAlertBox(timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存自动跟进策略成功")
        else:
            log.warning("保存自动跟进策略失败，失败原因: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def templateBindNE(self, netunit_name, levels, vendor, model, level_type, unassigned_list):
        """
        # 模版网元绑定
        :param netunit_name: 网元名称
        :param levels: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :param level_type: 网元类型
        :param unassigned_list: 待分配网元
        """
        log.info("模版网元绑定")
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版网元']").click()
        sleep(1)

        # 网元名称
        if netunit_name:
            self.browser.find_element(By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("设置网元名称: {0}".format(netunit_name))

        # 网元分类
        if levels:
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelNE']/following-sibling::span//a").click()
            for level in levels:
                self.browser.find_element(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(level)).click()
                log.info("选择网元分类: {0}".format(level))
            # 收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelNE']/following-sibling::span//a").click()
            sleep(1)

        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='bindingVendorNE']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(vendor)).click()
            log.info("选择厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='bindingNetunitModelNE']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, panel_xpath + "//*[text()='{0}']".format(model))))
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(model)).click()
            log.info("选择设备型号: {0}".format(model))
            sleep(1)

        # 网元类型
        if level_type:
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").send_keys(level_type)
            log.info("设置网元类型: {0}".format(level_type))

        # 查询待分配
        self.browser.find_element(By.XPATH, "//*[@id='bindingNetunit']//*[contains(@class,'queryUnassigned')]").click()
        page_wait()

        # 待分配网元
        for ne in unassigned_list:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'unassignedNetunitTab')]/td/div[text()='{0}']".format(ne)).click()
            log.info("选择网元: {0}".format(ne))
        # 分配
        self.browser.find_element(By.XPATH, "//*[@id='bindingNetunit']//*[@class='operatorBtn']/button[2]").click()
        alert = BeAlertBox(timeout=2)
        msg = alert.get_msg()
        if alert.title_contains("您确定分配已选网元吗", auto_click_ok=False):
            alert.click_ok()
            msg = "保存成功"
        gbl.temp.set("ResultMsg", msg)

    def templateBindNELevel(self, unassigned_list):
        """
        # 模版网元类型绑定
        :param unassigned_list: 待分配网元类型
        """
        log.info("模版网元类型绑定")
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版网元类型']").click()
        sleep(1)

        # 待分配网元类型
        for ne_level in unassigned_list:
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").send_keys(ne_level)
            # 查询待分配
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevel']//*[contains(@class,'queryUnassigned')]").click()
            page_wait()

            self.browser.find_element(
                By.XPATH, "//*[@field='levelName']/*[contains(@class,'unassignedLevelTab') and text()='{0}']".format(
                    ne_level)).click()
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevel']//*[@class='operatorBtn']/button[2]").click()
            alert = BeAlertBox(timeout=1)
            msg = alert.get_msg()
            if alert.title_contains("您确定分配已选网元类型吗", auto_click_ok=False):
                alert.click_ok()
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmplEditWin.html')]")))
                page_wait(1)
                msg = "保存成功"
                gbl.temp.set("ResultMsg", msg)
            else:
                gbl.temp.set("ResultMsg", msg)
                return
            log.info("分配网元类型: {0}".format(ne_level))

    def templateBindCmd(self, cmd_name, levels, vendor, model, unassigned_list):
        """
        # 模版指令绑定
        :param cmd_name: 指令名称
        :param levels: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :param unassigned_list: 待分配指令
        """
        log.info("模版指令绑定")
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版指令']").click()
        sleep(1)

        # 指令名称
        if cmd_name:
            self.browser.find_element(By.XPATH, "//*[@id='bindingCmdName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingCmdName']/following-sibling::span/input[1]").send_keys(cmd_name)
            log.info("设置指令名称: {0}".format(cmd_name))

        # 网元分类
        if levels:
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelCmd']/following-sibling::span//a").click()
            for level in levels:
                self.browser.find_element(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(level)).click()
                log.info("选择网元分类: {0}".format(level))
            # 收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelCmd']/following-sibling::span//a").click()
            sleep(1)

        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='bindingVendorCmd']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'bindingVendorCmd') and text()='{0}']".format(vendor)).click()
            log.info("选择厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='bindingNetunitModelCmd']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'bindingNetunitModelCmd') and text()='{0}']".format(model)).click()
            log.info("选择设备型号: {0}".format(model))

        # 查询待选择
        self.browser.find_element(By.XPATH, "//*[@id='bindingCmdInfo']//*[contains(@class,'queryUnassigned')]").click()
        page_wait()
        sleep(1)

        # 待分配指令[["指令集", "解析模版"], ["指令集", "解析模版"]]
        for cmd, analyzer in unassigned_list:
            # 指令集
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'unassignedCmdTab')]/td/div[text()='{0}']".format(cmd)).click()
            log.info("选择指令: {0}".format(cmd))

            # 解析模版
            if len(analyzer) > 0:
                self.browser.find_element(
                    By.XPATH, "//*[@field='cmdName']//*[text()='{0}']/../following-sibling::td[1]//a".format(cmd)).click()
                panel_xpath = getPanelXpath()
                self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(analyzer)).click()
                log.info("选择解析模版: {0}".format(analyzer))

        # 分配
        self.browser.find_element(By.XPATH, "//*[@id='bindingCmdInfo']//*[@class='operatorBtn']/button[1]").click()
        alert = BeAlertBox(timeout=2)
        msg = alert.get_msg()
        if alert.title_contains("您确定分配已选指令吗", auto_click_ok=False):
            alert.click_ok()
            msg = "保存成功"
        gbl.temp.set("ResultMsg", msg)

    def _get_status(self, template_name):
        """
        # 获取状态
        :param template_name: 模版名称
        """
        try:
            template = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../..".format(template_name))
            row_index = template.get_attribute("datagrid-row-index")
            js = 'return $(".switchbutton")[{0}].checked;'.format(int(row_index))
            current_status = self.browser.execute_script(js)
        except NoSuchElementException:
            current_status = False
        return current_status

    def updateStatus(self, template_name, status):
        """
        # 启用/禁用
        :param template_name: 模版名称
        :param status: 状态

        # 启用指令模版时，若未创建任务则提示是否创建任务；若已创建任务，则提示是否同步启用任务
        # 禁用指令模版时，先弹出二次确认，确认后先禁用模版，若已创建任务且任务已启用，则将任务禁用
        """
        self.search(query={"模版名称": template_name}, need_choose=True)
        page_wait(2)
        template = self.browser.find_element(
            By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../..".format(template_name))
        row_index = template.get_attribute("datagrid-row-index")
        js = 'return $(".switchbutton")[{0}].checked;'.format(int(row_index))
        current_status = self.browser.execute_script(js)

        tmp = True if status == "启用" else False
        if tmp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../following-sibling::td[1]//*[@class='switchbutton']".format(
                    template_name)).click()
            log.info("{0}指令模版: {1}".format(status, template_name))

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("启用指令模版成功", auto_click_ok=False):
                # 启用指令模版成功
                alert.click_cancel()
                log.info("启用指令模版成功")
            elif alert.title_contains("您确定禁用所选指令模版吗", auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("禁用指令模版成功", auto_click_ok=False):
                    # 禁用指令模版成功
                    alert.click_ok()
                    log.info("禁用指令模版成功")
                else:
                    log.info("禁用指令模版失败，失败原因: {0}".format(msg))
        else:
            log.info("指令模版【{0}】状态已经是{1}".format(template_name, status))
            msg = "{0}指令模版成功".format(status)
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, template_name, fuzzy_match=False):
        """
        :param template_name: 模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"模版名称": template_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='templName']//*[starts-with(text(),'{0}')]".format(template_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='templName']//*[text()='{0}']".format(template_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            js = 'return $(".cmdTmplTab_datagrid-cell-c1-templName")[1].innerText;'
            search_result = self.browser.execute_script(js)
            pe.click()
            log.info("选择: {0}".format(search_result))
            if self._get_status(search_result):
                log.info("禁用指令模版: {0}".format(search_result))
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../following-sibling::td[1]//*[@class='switchbutton']".format(
                        search_result)).click()
                alert = BeAlertBox(back_iframe=False)
                if alert.title_contains("您确定禁用所选指令模版吗", auto_click_ok=False):
                    alert.click_ok()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("禁用指令模版成功", auto_click_ok=False):
                        # 禁用指令模版成功
                        alert.click_ok()
                        log.info("禁用指令模版成功")
                        sleep(1)
                    else:
                        log.info("禁用指令模版失败，失败原因: {0}".format(msg))
                        return
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-del']").click()
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
                            By.XPATH, "//*[@field='templName']//*[starts-with(text(),'{}')]".format(template_name))
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
                log.warning("{0} 删除失败，失败提示: {1}".format(template_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
