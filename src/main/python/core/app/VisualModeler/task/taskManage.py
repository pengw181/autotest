# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/6/16 下午3:40

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class TaskManage:

    def __init__(self, exec_from=True):
        """
        :param exec_from: 是否在任务管家添加任务
        """
        self.browser = gbl.service.get("browser")
        if exec_from:
            DoctorWho().choose_menu("任务管家-任务模版管理")
            page_wait()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfo.html')]")))
        # 从流程配置、指令模版、数据拼盘创建任务，是自动跳转页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='taskName']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def search(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询任务模版信息，查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None

        # 任务名称
        if query.__contains__("任务名称"):
            task_name = query.get("任务名称")
            self.browser.find_element(By.XPATH, "//*[@name='taskName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='taskName']/preceding-sibling::input[1]").send_keys(
                task_name)
            select_item = task_name

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").send_keys(
                creator)

        # 任务状态
        if query.__contains__("任务状态"):
            task_status = query.get("任务状态")
            self.browser.find_element(By.XPATH, "//*[@id='taskStatusCombobox']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(task_status)).click()

        # 任务类型
        if query.__contains__("任务类型"):
            task_type = query.get("任务类型")
            self.browser.find_element(By.XPATH, "//*[@name='taskType']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(task_type)).click()

        # 模版类型
        if query.__contains__("模版类型"):
            temp_type = query.get("模版类型")
            self.browser.find_element(By.XPATH, "//*[@name='taskTempType']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(temp_type)).click()

        # 查询
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
                        By.XPATH, "//*[@field='taskName']//*[text()='{}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, task_name, task_type, bind_task, time_turner, timing_conf, remark):
        """
        # 添加任务
        :param task_name: 任务名称
        :param task_type: 模版类型
        :param bind_task: 绑定任务名称
        :param time_turner: 配置定时任务，开启/关闭
        :param timing_conf: 定时配置
        :param remark: 任务说明
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfoEdit.html')]")))
        sleep(1)
        self.taskPage(task_name, task_type, bind_task, time_turner, timing_conf, remark)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alter = BeAlertBox()
        msg = alter.get_msg()
        if alter.title_contains("保存成功"):
            log.info("{0}保存成功".format(task_name))
        else:
            log.info("{0}保存失败，失败原因: {1}".format(task_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, task, task_name, time_turner, timing_conf, remark):
        """
        :param task: 任务名称
        :param task_name: 任务名称
        :param time_turner: 配置定时任务，开启/关闭
        :param timing_conf: 定时配置
        :param remark: 任务说明
        """
        self.search(query={"任务名称": task}, need_choose=True)

        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/naga/taskManConfInfoEdit.html')]")))
            sleep(1)
            self.taskPage(task_name, None, None, time_turner, timing_conf, remark)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alter = BeAlertBox()
            msg = alter.get_msg()
            if alter.title_contains("保存成功"):
                log.info("{0}保存成功".format(task_name))
            else:
                log.info("{0}保存失败，失败原因: {1}".format(task_name, msg))
            gbl.temp.set("ResultMsg", msg)

    def taskPage(self, task_name, task_type, bind_task, time_turner, timing_conf, remark):
        """
        # 任务配置页面
        :param task_name: 任务名称
        :param task_type: 模版类型
        :param bind_task: 绑定任务名称
        :param time_turner: 配置定时任务，开启/关闭
        :param timing_conf: 定时配置
        :param remark: 任务说明
        """
        # 任务名称
        if task_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@name='taskName']/preceding-sibling::input").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@name='taskName']/preceding-sibling::input").send_keys(task_name)
            log.info("设置任务名称: {0}".format(task_name))

        # 模版类型
        if task_type:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='taskTempType']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'taskTempType') and text()='{0}']".format(task_type)).click()
            log.info("选择模版类型: {0}".format(task_type))
            sleep(1)

        # 绑定任务名称
        if bind_task:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='bindTaskId']/following-sibling::span//a").click()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[contains(@id,'bindTaskId') and text()='{0}']".format(bind_task))))
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'bindTaskId') and text()='{0}']".format(bind_task)).click()
            log.info("选择绑定任务名称: {0}".format(bind_task))

        # 配置定时任务
        if time_turner:
            js = 'return $("#configCyc")[0].checked;'
            status = self.browser.execute_script(js)
            tmp = True if time_turner == "开启" else False
            if tmp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='configCyc']").click()
                log.info("配置定时任务 {0}".format(time_turner))

        # 定时配置
        if timing_conf:
            if not isinstance(timing_conf, dict):
                raise ValueError("定时配置格式错误，请输入字典格式")
            first_exec_time = timing_conf.get("首次执行时间")
            advance_mode = timing_conf.get("高级模式")
            interval = timing_conf.get("间隔周期")
            unit = timing_conf.get("间隔周期单位")
            cron = timing_conf.get("Cron表达式")
            use_cron = False

            # 首次执行时间
            if first_exec_time:
                self.browser.find_element(By.XPATH, "//*[@id='firstExecDate']/following-sibling::span//a[2]").click()
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
                    self.browser.find_element(By.XPATH, "//*[@id='isHighCheck']").click()
                    log.info("{0} 高级模式".format(advance_mode))

            # 间隔周期
            if interval:
                self.browser.find_element(By.XPATH, "//*[@id='intervalCyc']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='intervalCyc']/following-sibling::span/input[1]").send_keys(interval)
                log.info("设置间隔周期: {0}".format(interval))

            # 间隔周期单位
            if unit:
                self.browser.find_element(By.XPATH, "//*[@id='intervalUnit']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'intervalUnit') and text()='{0}']".format(unit)).click()
                log.info("设置间隔周期单位: {0}".format(unit))

            # Cron表达式
            if cron:
                self.browser.find_element(By.XPATH, "//*[@id='cronExp']/following-sibling::span/input[1]").clear()
                self.browser.find_element(By.XPATH, "//*[@id='cronExp']/following-sibling::span/input[1]").send_keys(cron)
                log.info("设置Cron表达式: {0}".format(cron))
                use_cron = True

            # 预览最近五次执行时间
            if use_cron is False:
                self.browser.find_element(By.XPATH, "//*[@id='execTimeBtn']").click()
            else:
                self.browser.find_element(By.XPATH, "//*[@id='execTimeBtn2']").click()
            execTimeUl = self.browser.find_element(By.XPATH, "//*[@id='execTimeUl']")
            recent5Times = execTimeUl.get_attribute("innerText").split(r"\n")
            log.info("最近五次执行时间: \n{0}".format('\n'.join(recent5Times)))

        # 任务说明
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='taskDesc']/following-sibling::span/textarea")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置任务说明: {0}".format(remark))

    def updateStatus(self, task_name, status):
        """
        # 启用/禁用状态
        :param task_name: 任务名称
        :param status: 状态，启用/禁用
        """
        self.search(query={"任务名称": task_name}, need_choose=True)
        current_status = self._get_status(task_name)

        tmp = True if status == "启用" else False
        if tmp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'dg')]//*[text()='{0}']/../../following-sibling::td[1]//*[@class='switchbutton']".format(
                    task_name)).click()
            log.info("{0}任务: {1}".format(status, task_name))

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("更新任务状态成功")
            else:
                log.info("更新任务状态失败，失败原因: {0}".format(msg))
        else:
            log.info("任务: {0}状态已经是{1}状态".format(task_name, status))
            msg = "保存成功"
        gbl.temp.set("ResultMsg", msg)

    def delete(self, task_name):
        """
        :param task_name: 任务名称
        """
        self.search(query={"任务名称": task_name}, need_choose=True)

        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()
        alert = BeAlertBox(timeout=2, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(task_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("任务{0}删除成功".format(task_name))
            else:
                log.info("任务{0}删除失败，失败原因{1}".format(task_name, msg))
        else:
            log.info("任务{0}删除失败，失败原因{1}".format(task_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def triggerTask(self, task_name):
        """
        # 触发任务
        :param task_name: 任务名称
        """
        self.search(query={"任务名称": task_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[@field='taskName']//*[text()='{0}']/../../following-sibling::td[2]".format(
                task_name)).click()

        alert = BeAlertBox(timeout=10, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("立即执行 {0} 任务".format(task_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("运行成功"):
                log.info("手动触发任务成功")
            else:
                log.info("手动触发任务失败，失败原因: {0}".format(msg))
        else:
            log.info("手动触发任务失败，失败原因: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def _get_status(self, task_name):
        """
        # 获取状态
        :param task_name: 任务名称
        """
        try:
            task = self.browser.find_element(By.XPATH, "//*[@data-mtips='{0}']/../../..".format(task_name))
            row_index = task.get_attribute("datagrid-row-index")
            js = 'return $(".easyui-switchbutton")[{0}].checked;'.format(int(row_index))
            current_status = self.browser.execute_script(js)
        except NoSuchElementException:
            log.warning("无法找到任务")
            current_status = False
        return current_status

    def data_clear(self, query, fuzzy_match=False):
        """
        :param query: 查询条件
        :param fuzzy_match: 模糊匹配
        """
        self.search(query=query)
        fuzzy_match = True if fuzzy_match == "是" else False
        task_name = query.get("任务名称")
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='taskName']//*[starts-with(@data-mtips,'{0}')]".format(task_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='taskName']//*[@data-mtips='{0}']".format(task_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            js = 'return $(".dg_datagrid-cell-c1-taskName")[1].innerText;'
            search_result = self.browser.execute_script(js)
            pe.click()
            log.info("选择: {0}".format(search_result))
            # 禁用任务
            if self._get_status(search_result):
                log.info("禁用任务: {0}".format(search_result))
                self.browser.find_element(
                    By.XPATH, "//*[@data-mtips='{0}']/../../following-sibling::td[1]//*[@class='switchbutton']".format(
                        search_result)).click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("保存成功"):
                    log.info("禁用任务成功")
                    sleep(1)
                else:
                    log.info("禁用任务失败，失败原因: {0}".format(msg))
                    return
            # 删除
            self.browser.find_element(
                By.XPATH, "//*[@field='taskName']//*[@data-mtips='{0}']".format(search_result)).click()
            self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()
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
                            By.XPATH, "//*[@field='taskName']//*[starts-with(@data-mtips,'{0}')]".format(task_name))
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
                log.warning("{0} 删除失败，失败提示: {1}".format(task_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
