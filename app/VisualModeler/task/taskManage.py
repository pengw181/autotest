# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/6/16 下午3:40

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from common.page.func.input import set_textarea
from common.page.func.alertBox import BeAlertBox
from common.date.dateCalculation import calculation
from common.date.dateUtil import set_calendar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from time import sleep
from common.log.logger import log


class TaskManage:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("任务管家-任务模版管理")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfo.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='taskName']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def choose(self, taskName):
        """
        :param taskName: 任务名称
        """
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").clear()
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").send_keys(taskName)
        self.browser.find_element_by_xpath("//*[@id='btn']").click()
        page_wait()
        self.browser.find_element_by_xpath("//*[@field='taskName']//*[text()='{0}']".format(taskName)).click()
        log.info("选择任务: {0}".format(taskName))

    def add(self, taskName, taskType, bindTask, timeTurner, timingConf, remark):
        """
        # 添加任务
        :param taskName: 任务名称
        :param taskType: 模版类型
        :param bindTask: 绑定任务名称
        :param timeTurner: 配置定时任务
        :param timingConf: 定时配置
        :param remark: 任务说明
        """
        self.browser.find_element_by_xpath("//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfoEdit.html')]")))
        sleep(1)
        self.taskPage(taskName, taskType, bindTask, timeTurner, timingConf, remark)

    def update(self, task, taskName, timeTurner, timeConf, remark):
        """
        :param task: 任务名称
        :param taskName: 任务名称
        :param timeTurner: 配置定时任务，开启/关闭
        :param timeConf: 定时配置
        :param remark: 任务说明
        """
        self.choose(task)

        self.browser.find_element_by_xpath("//*[@id='editBtn']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            set_global_var("ResultMsg", msg, False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfoEdit.html')]")))
            sleep(1)
            self.taskPage(taskName, None, None, timeTurner, timeConf, remark)

    def taskPage(self, taskName, taskType, bindTask, timeTurner, timeConf, remark):
        """
        # 任务配置页面
        :param taskName: 任务名称
        :param taskType: 模版类型
        :param bindTask: 绑定任务名称
        :param timeTurner: 配置定时任务，开启/关闭
        :param timeConf: 定时配置
        :param remark: 任务说明
        """
        # 任务名称
        if taskName:
            self.browser.find_element_by_xpath(
                "//*[@id='editDiv']//*[@name='taskName']/preceding-sibling::input").clear()
            self.browser.find_element_by_xpath(
                "//*[@id='editDiv']//*[@name='taskName']/preceding-sibling::input").send_keys(taskName)
            log.info("设置任务名称: {0}".format(taskName))

        # 模版类型
        if taskType:
            self.browser.find_element_by_xpath(
                "//*[@id='editDiv']//*[@id='taskTempType']/following-sibling::span//a").click()
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'taskTempType') and text()='{0}']".format(taskType)).click()
            log.info("选择模版类型: {0}".format(taskType))

        # 绑定任务名称
        if bindTask:
            self.browser.find_element_by_xpath(
                "//*[@id='editDiv']//*[@id='bindTaskId']/following-sibling::span//a").click()
            sleep(1)
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'bindTaskId') and text()='{0}']".format(bindTask)).click()
            log.info("选择绑定任务名称: {0}".format(bindTask))

        # 配置定时任务
        if timeTurner:
            js = 'return $("#configCyc")[0].checked;'
            status = self.browser.execute_script(js)
            tmp = True if timeTurner == "开启" else False
            if tmp ^ status:
                self.browser.find_element_by_xpath("//*[@id='configCyc']").click()
                log.info("配置定时任务 {0}".format(timeTurner))

        # 定时配置
        if timeConf:
            if not isinstance(timeConf, dict):
                raise ValueError
            first_exec_time = timeConf.get("首次执行时间")
            interval = timeConf.get("间隔周期")
            unit = timeConf.get("间隔周期单位")
            advance_mode = timeConf.get("高级模式")
            cron = timeConf.get("Cron表达式")
            use_cron = False

            # 首次执行时间
            if first_exec_time:
                self.browser.find_element_by_xpath("//*[@id='firstExecDate']/following-sibling::span//a[2]").click()
                if isinstance(first_exec_time, dict):
                    exec_time = calculation(interval=first_exec_time.get("间隔"), unit=first_exec_time.get("单位"))
                else:
                    exec_time = first_exec_time
                set_calendar(date_s=exec_time, date_format='%Y-%m-%d %H:%M:%S')
                log.info("设置首次执行时间: {0}".format(exec_time))

            # 高级模式
            if advance_mode:
                js = 'return $("#isHighCheck")[0].checked;'
                status = self.browser.execute_script(js)
                tmp = True if advance_mode == "开启" else False
                if tmp ^ status:
                    self.browser.find_element_by_xpath("//*[@id='isHighCheck']").click()
                    log.info("{0} 高级模式".format(advance_mode))

            # 间隔周期
            if interval:
                self.browser.find_element_by_xpath("//*[@id='intervalCyc']/following-sibling::span/input[1]").clear()
                self.browser.find_element_by_xpath(
                    "//*[@id='intervalCyc']/following-sibling::span/input[1]").send_keys(interval)
                log.info("设置间隔周期: {0}".format(interval))

            # 间隔周期单位
            if unit:
                self.browser.find_element_by_xpath("//*[@id='intervalUnit']/following-sibling::span//a").click()
                self.browser.find_element_by_xpath(
                    "//*[contains(@id,'intervalUnit') and text()='{0}']".format(unit)).click()
                log.info("设置间隔周期单位: {0}".format(unit))

            # Cron表达式
            if cron:
                self.browser.find_element_by_xpath("//*[@id='cronExp']/following-sibling::span/input[1]").clear()
                self.browser.find_element_by_xpath(
                    "//*[@id='cronExp']/following-sibling::span/input[1]").send_keys(cron)
                log.info("设置Cron表达式: {0}".format(cron))
                use_cron = True

            # 预览最近五次执行时间
            if use_cron is False:
                self.browser.find_element_by_xpath("//*[@id='execTimeBtn']").click()
            else:
                self.browser.find_element_by_xpath("//*[@id='execTimeBtn2']").click()
            execTimeUl = self.browser.find_element_by_xpath("//*[@id='execTimeUl']")
            recent5Times = execTimeUl.get_attribute("innerText").split(r"\n")
            log.info("最近五次执行时间: \n{0}".format('\n'.join(recent5Times)))

        # 任务说明
        if remark:
            remark_textarea = self.browser.find_element_by_xpath(
                "//*[@id='taskDesc']/following-sibling::span/textarea")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置任务说明: {0}".format(remark))

        # 提交
        self.browser.find_element_by_xpath("//*[@id='saveBtn']").click()
        alter = BeAlertBox()
        msg = alter.get_msg()
        if alter.title_contains("保存成功"):
            log.info("{0}保存成功".format(taskName))
        else:
            log.info("{0}保存失败，失败原因: {1}".format(taskName, msg))
        set_global_var("ResultMsg", msg, False)

    def updateStatus(self, taskName, status):
        """
        # 启用/禁用状态
        :param taskName: 任务名称
        :param status: 状态，启用/禁用
        """
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").clear()
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").send_keys(taskName)
        self.browser.find_element_by_xpath("//*[@id='btn']").click()
        page_wait()
        task = self.browser.find_element_by_xpath(
            "//*[contains(@id,'dg')]//*[text()='{0}']/../../..".format(taskName))
        row_index = task.get_attribute("datagrid-row-index")
        js = 'return $(".switchbutton-value")[{0}].checked;'.format(row_index)
        current_status = self.browser.execute_script(js)

        tmp = True if status == "启用" else False
        if tmp ^ current_status:
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'dg')]//*[text()='{0}']/../../following-sibling::td[1]//*[@class='switchbutton']".format(
                    taskName)).click()
            log.info("{0}任务: {1}".format(status, taskName))

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("更新任务状态成功")
            else:
                log.info("更新任务状态失败，失败原因: {0}".format(msg))
        else:
            log.info("任务: {0}状态已经是{1}状态".format(taskName, status))
            msg = "保存成功"
        set_global_var("ResultMsg", msg, False)

    def delete(self, taskName):
        """
        :param taskName: 任务名称
        """
        self.choose(taskName)

        self.browser.find_element_by_xpath("//*[@id='delBtn']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(taskName), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("任务{0}删除成功".format(taskName))
            else:
                log.info("任务{0}删除失败，失败原因{1}".format(taskName, msg))
        else:
            log.info("任务{0}删除失败，失败原因{1}".format(taskName, msg))
        set_global_var("ResultMsg", msg, False)

    def triggerTask(self, taskName):
        """
        # 触发任务
        :param taskName: 任务名称
        """
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").clear()
        self.browser.find_element_by_xpath("//*[@name='taskName']/preceding-sibling::input").send_keys(taskName)
        self.browser.find_element_by_xpath("//*[@id='btn']").click()
        page_wait()

        self.browser.find_element_by_xpath(
            "//*[@field='taskName']//*[text()='{0}']/../../following-sibling::td[2]".format(
                taskName)).click()

        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("立即执行 {0} 任务".format(taskName), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("运行成功"):
                log.info("更新任务状态成功")
            log.info("手动触发任务失败，失败原因: {0}".format(msg))
        else:
            log.info("手动触发任务失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)
