# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午4:09

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from common.page.func.input import set_textarea
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from time import sleep
from common.log.logger import log


class CmdTemplate:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("指令配置-指令模版")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmpl.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='templName']/following-sibling::span/input")))
        page_wait()
        sleep(1)

    def choose(self, templateName):
        """
        :param templateName: 模版名称
        """
        try:
            self.browser.find_element(By.XPATH, "//*[@id='templName']/following-sibling::span/input").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='templName']/following-sibling::span/input").send_keys(templateName)
            page_wait()
            self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-query']//*[text()='查询']").click()
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[@field='templName']/*[contains(@class,'templName')]/*[text()='{}']".format(
                    templateName)).click()
            log.info("选择模版：{0}".format(templateName))
        except NoSuchElementException:
            raise ("所选指令不存在, 指令名称: {0}".format(templateName))

    def add(self, templateName, field, level, mode, remark):
        """
        :param templateName: 模版名称
        :param field: 专业领域
        :param level: 网络层级
        :param mode: 选择方式
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-add']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmplEditWin.html')]")))
        page_wait(2)
        self.basicInfoPage(templateName, field, level, mode, remark)

    def update(self, obj, templateName, field, mode, remark):
        """
        # 只修改基本信息，同添加操作
        :param obj: 模版名称
        :param templateName: 模版名称
        :param field: 专业领域
        :param mode: 选择方式
        :param remark: 备注
        """
        self.choose(templateName=obj)
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-update']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.warning("修改指令模版失败，失败原因: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)
        else:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdTmplEditWin.html')]")))
            page_wait(2)
            self.basicInfoPage(templateName, field, None, mode, remark)

    def basicInfoPage(self, templateName, fields, levels, mode, remark):
        """
        # 模版基本信息
        :param templateName: 模版名称
        :param fields: 专业领域
        :param levels: 网络层级，不可修改
        :param mode: 选择方式
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版基本信息']").click()
        # 模版名称
        if templateName:
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='templName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='cmdTmplForm']//*[@id='templName']/following-sibling::span/input[1]").send_keys(
                templateName)
            log.info("设置模版名称: {0}".format(templateName))

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
        alert = BeAlertBox(10)
        if alert.exist_alert:
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存指令模版成功")
            else:
                log.warning("保存指令模版失败，失败原因: {0}".format(msg))
        else:
            log.warning("没有弹出框提示信息")
            msg = None
        set_global_var("ResultMsg", msg, False)

    def autoFollowUpStrategy(self, enable, followUpScope, followUpPeriod, followUpTime):
        """
        # 自动跟进策略配置
        :param enable: 状态，启用/禁用
        :param followUpScope: 跟进范围
        :param followUpPeriod: 跟进周期
        :param followUpTime: 跟进次数
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='自动跟进策略配置']").click()

        js = 'return $("#isFollowUp")[0].checked;'
        status = self.browser.excute_script(js)
        log.info("【启用自动跟进策略】勾选状态: {0}".format(status))

        # 状态
        if enable:
            tmp = True if enable == "启用" else False
            if tmp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='isFollowUp']").click()
                log.info("【{0}】自动跟进策略".format(enable))

        # 跟进范围
        if followUpScope:
            self.browser.find_element(By.XPATH, "//*[@id='followUpScope']/following-sibling::span//a").click()
            selected_elements = self.browser.find_elements(By.XPATH, "//*[contains(@class,'tree-checkbox1')]")
            for element in selected_elements:
                element.click()
            for result in followUpScope:
                self.browser.find_element(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(result)).click()
                log.info("跟进范围选择: {0}".format(result))

        # 跟进周期
        if followUpPeriod:
            self.browser.find_element(By.XPATH, "//*[@id='followUpPeriod']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='followUpPeriod']/following-sibling::span/input[1]").send_keys(followUpPeriod)
            log.info("设置跟进周期: {0}".format(followUpPeriod))

        # 跟进次数
        if followUpTime:
            self.browser.find_element(By.XPATH, "//*[@id='followUpTime']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='followUpTime']/following-sibling::span/input[1]").send_keys(followUpTime)
            log.info("设置跟进次数: {0}".format(followUpTime))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmpl-saveFollowUp']").click()
        alert = BeAlertBox(3)
        if alert.exist_alert:
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存自动跟进策略成功")
            else:
                log.warning("保存自动跟进策略失败，失败原因: {0}".format(msg))
        else:
            log.warning("没有弹出框提示信息")
            msg = None
        set_global_var("ResultMsg", msg, False)

    def templateBindNE(self, netunitName, levels, vendor, model, levelType, unassignedNeList):
        """
        # 模版网元绑定
        :param netunitName: 网元名称
        :param levels: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :param levelType: 网元类型
        :param unassignedNeList: 待分配网元
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版网元']").click()

        # 网元名称
        if netunitName:
            self.browser.find_element(By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingNetunitName']/following-sibling::span/input[1]").send_keys(netunitName)
            log.info("设置网元名称: {0}".format(netunitName))

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
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'bindingVendorNE') and text()='{0}']".format(vendor)).click()
            log.info("选择厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='bindingNetunitModelNE']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'bindingNetunitModelNE') and text()='{0}']".format(model)).click()
            log.info("选择设备型号: {0}".format(model))

        # 网元类型
        if levelType:
            self.browser.find_element(By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingLevelName']/following-sibling::span/input[1]").send_keys(levelType)
            log.info("设置网元类型: {0}".format(levelType))

        # 查询待选择
        self.browser.find_element(By.XPATH, "//*[@id='bindingNetunit']//*[text()='查询待分配']").click()
        page_wait()

        # 待分配网元
        for obj in unassignedNeList:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'unassignedNetunitTab')]/td/div[text()='{0}']".format(obj)).click()
            log.info("选择网元: {0}".format(obj))
        # 分配
        self.browser.find_element(By.XPATH, "//*[@id='bindingNetunit']//*[@class='operatorBtn']/button[2]").click()
        alert = BeAlertBox(timeout=2)
        msg = alert.get_msg()
        if alert.title_contains("您确定分配已选网元吗|您确定分配已选网元类型吗", auto_click_ok=False):
            alert.click_ok()
        else:
            set_global_var("ResultMsg", msg, False)

    def templateBindCmd(self, cmdName, levels, vendor, model, unassignedCmdList):
        """
        # 模版指令绑定
        :param cmdName: 指令名称
        :param levels: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :param unassignedCmdList: 待分配指令
        """
        self.browser.find_element(By.XPATH, "//*[@id='cmdTmplTabs']//*[text()='模版指令']").click()

        # 指令名称
        if cmdName:
            self.browser.find_element(By.XPATH, "//*[@id='bindingCmdName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='bindingCmdName']/following-sibling::span/input[1]").send_keys(cmdName)
            log.info("设置指令名称: {0}".format(cmdName))

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
        self.browser.find_element(By.XPATH, "//*[@id='bindingCmdInfo']//*[text()='查询待分配']").click()
        page_wait()

        # 待分配指令
        for obj in unassignedCmdList:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'unassignedCmdTab')]/td/div[text()='{0}']".format(obj)).click()
            log.info("选择指令: {0}".format(obj))
        # 分配
        self.browser.find_element(By.XPATH, "//*[@id='bindingCmdInfo']//*[@class='operatorBtn']/button[1]").click()
        alert = BeAlertBox(timeout=2)
        msg = alert.get_msg()
        if alert.title_contains("您确定分配已选指令吗", auto_click_ok=False):
            alert.click_ok()
        else:
            set_global_var("ResultMsg", msg, False)

    def updateStatus(self, templateName, status):
        """
        # 启用/禁用
        :param templateName: 模版名称
        :param status: 状态

        # 启用指令模版时，若未创建任务则提示是否创建任务；若已创建任务，则提示是否同步启用任务
        # 禁用指令模版时，先弹出二次确认，确认后先禁用模版，若已创建任务且任务已启用，则将任务禁用
        """
        template = self.browser.find_element(
            By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../..".format(templateName))
        row_index = template.get_attribute("datagrid-row-index")
        js = 'return $(".switchbutton")[{0}].checked;'.format(int(row_index)-1)
        current_status = self.browser.execute_script(js)

        tmp = True if status == "启用" else False
        if tmp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cmdTmplTab')]//*[text()='{0}']/../following-sibling::td[1]//*[@class='switchbutton']".format(
                    templateName)).click()
            log.info("{0}指令模版: {1}".format(status, templateName))

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
                    set_global_var("ResultMsg", msg, False)
            else:
                set_global_var("ResultMsg", msg, False)
        else:
            log.info("指令模版【{0}】状态已经是{1}".format(templateName, status))
            msg = "{0}指令模版成功".format(status)
            set_global_var("ResultMsg", msg, False)
