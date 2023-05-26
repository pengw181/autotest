# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:07

import json
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.core.app.AlarmPlatform.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.dateUtil import set_calendar
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class AlarmPlan:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        # 进入菜单
        choose_menu("告警配置-告警计划")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/alarmConfig/alarmPlanList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='alarmPlanName']/preceding-sibling::input")))
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

        # 告警计划名称
        if query.__contains__("告警计划名称"):
            plan_name = query.get("告警计划名称")
            self.browser.find_element(By.XPATH, "//*[@name='alarmPlanName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='alarmPlanName']/preceding-sibling::input[1]").send_keys(
                plan_name)
            select_item = plan_name

        # 告警类型
        if query.__contains__("告警类型"):
            alarm_type = query.get("告警类型")
            self.browser.find_element(By.XPATH, "//*[@name='alarmTypeId']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(alarm_type)).click()

        # 数据源名称
        if query.__contains__("数据源名称"):
            data_source = query.get("数据源名称")
            self.browser.find_element(By.XPATH, "//*[@name='dataSourceId']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(data_source)).click()

        # 状态
        if query.__contains__("状态"):
            alarm_status = query.get("状态")
            self.browser.find_element(By.XPATH, "//*[@name='alarmPlanState']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(alarm_status)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_plan_query']").click()
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
                        By.XPATH, "//*[@field='alarmPlanName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc):
        """
        :param plan_name: 告警计划名称
        :param alarm_type: 告警类型
        :param data_source: 数据源名称
        :param region_tag: 标签分类
        :param domain_tag: 领域标签
        :param plan_desc: 计划描述
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmPlanEdit.html')]")))
        sleep(1)
        self.plan_page(plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc)
        # 保存
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_plan_save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(plan_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(plan_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, plan, plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc):
        """
        :param plan: 告警计划
        :param plan_name: 告警计划名称
        :param alarm_type: 告警类型
        :param data_source: 数据源名称
        :param region_tag: 标签分类
        :param domain_tag: 领域标签
        :param plan_desc: 计划描述
        """
        self.search(query={"告警计划名称": plan}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmPlanEdit.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input")))

        self.plan_page(plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc)
        # 保存
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_plan_save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 修改成功".format(plan))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(plan, msg))
        gbl.temp.set("ResultMsg", msg)

    def plan_page(self, plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc):
        """
        :param plan_name: 告警计划名称
        :param alarm_type: 告警类型
        :param data_source: 数据源名称
        :param region_tag: 标签分类
        :param domain_tag: 领域标签
        :param plan_desc: 计划描述
        """
        # 告警计划名称
        if plan_name:
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input").clear()
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input").send_keys(
                plan_name)
            log.info("设置告警计划名称: {0}".format(plan_name))

        # 告警类型
        if alarm_type:
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@name='alarmTypeId']/preceding-sibling::input").click()
            sleep(1)
            self.browser.find_element(
                By.XPATH, "//*[@class='plan-form']/following-sibling::div//*[contains(@id,'easyui') and text()='{0}']".format(
                    alarm_type)).click()
            log.info("设置告警类型: {0}".format(alarm_type))

        # 数据源名称
        if data_source:
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@name='dataSourceId']/preceding-sibling::input").click()
            sleep(1)
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'dataSourceId') and text()='{0}']".format(data_source)).click()
            log.info("设置数据源名称: {0}".format(data_source))

        # 标签分类
        if region_tag:
            self.browser.find_element(By.XPATH, "//*[@id='regionTag']/following-sibling::span[1]//a").click()
            sleep(1)
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'regionTag') and text()='{0}']".format(region_tag)).click()
            log.info("设置标签分类: {0}".format(region_tag))

        # 领域标签
        if domain_tag:
            self.browser.find_element(By.XPATH, "//*[@id='domainTag']/following-sibling::span[1]//a").click()
            sleep(1)
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'domainTag') and text()='{0}']".format(domain_tag)).click()
            log.info("设置领域标签: {0}".format(domain_tag))

        # 计划描述
        if plan_desc:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@name='alarmPlanDesc']")
            set_textarea(remark_textarea, plan_desc)
            log.info("设置计划描述: {0}".format(plan_desc))

    def _get_status(self, plan_name):
        """
        获取当前状态
        :param plan_name: 告警计划名称
        :return: True/False
        """
        try:
            plan = self.browser.find_element(
                By.XPATH, "//*[text()='{}']/../../..".format(plan_name))
            row_index = plan.get_attribute("datagrid-row-index")
            js = 'return $(".easyui-switchbutton")[{0}].checked;'.format(int(row_index))
            current_status = self.browser.execute_script(js)
        except NoSuchElementException:
            current_status = False
        return current_status

    def update_status(self, plan_name, set_status, research=True):
        """
        :param plan_name: 告警计划名称
        :param set_status: 状态，启用/禁用
        :param research: 是否重新查询，默认true
        """
        if research:
            self.search(query={"告警计划名称": plan_name}, need_choose=True)
        # 获取当前状态
        js = 'return $(".easyui-switchbutton")[0].checked;'
        current_status = self.browser.execute_script(js)
        log.info("【状态】勾选状态: {0}".format(current_status))

        temp = True if set_status == "启用" else False
        if current_status ^ temp:
            self.browser.find_element(
                By.XPATH, "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(plan_name)).click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确认启用{0}吗|确认禁用{0}吗".format(plan_name), auto_click_ok=False):
                alert.click_ok()
                sleep(1)
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("{0} {1}成功".format(plan_name, set_status))
                else:
                    log.warning("{0} {1}失败，失败提示: {2}".format(plan_name, set_status, msg))
            else:
                log.warning("{0} {1}失败，失败提示: {2}".format(plan_name, set_status, msg))
            gbl.temp.set("ResultMsg", msg)

    def delete(self, plan_name):
        """
        :param plan_name: 告警计划名称
        """
        self.search(query={"告警计划名称": plan_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(plan_name, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("{0} 删除成功".format(plan_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(plan_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(plan_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def redo(self, plan_name, start_time=None, end_time=None):
        """
        :param plan_name: 告警计划名称
        :param start_time: 开始时间
        :param end_time: 结束时间
        """
        self.search(query={"告警计划名称": plan_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='redoBtn']").click()
        log.info("重调告警计划: {0}".format(plan_name))
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmRedo.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='startTime']/following-sibling::span//a")))

        # 开始时间
        if start_time is None:
            # 如果未设置开始时间，指定当天0点
            start_time = datetime.strftime(datetime.now(), '%Y-%m-%d 00:00:00')
        else:
            if isinstance(start_time, dict):
                # 间隔，0表示当前，正数表示未来，负数表示过去
                time_interval = start_time.get("间隔")
                # 单位，年、月、天、时、分、秒
                time_unit = start_time.get("单位")
                start_time = calculation(interval=time_interval, unit=time_unit)
            else:
                raise AttributeError("开始时间必须是字典")
        self.browser.find_element(By.XPATH, "//*[@id='startTime']/following-sibling::span//a").click()
        set_calendar(date_s=start_time, date_format='%Y-%m-%d %H:%M:%S')
        log.info("设置重调开始时间: {0}".format(start_time))

        # 结束时间
        if end_time is None:
            # 如果未设置结束时间，指定当天24点
            end_time = datetime.strftime(datetime.now(), '%Y-%m-%d 23:59:59')
        else:
            if isinstance(end_time, dict):
                # 间隔，0表示当前，正数表示未来，负数表示过去
                time_interval = end_time.get("间隔")
                # 单位，年、月、天、时、分、秒
                time_unit = end_time.get("单位")
                end_time = calculation(interval=time_interval, unit=time_unit)
            else:
                raise AttributeError("结束时间必须是字典")
        self.browser.find_element(By.XPATH, "//*[@id='endTime']/following-sibling::span//a").click()
        set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
        log.info("设置重调结束时间: {0}".format(end_time))

        # 点击确定
        self.browser.find_element(By.XPATH, "//*[contains(@class, 'save-btn')]").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 重调成功".format(plan_name))
        else:
            log.warning("{0} 重调失败，失败提示: {1}".format(plan_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, plan_name, fuzzy_match=False):
        """
        :param plan_name: 告警计划名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"告警计划名称": plan_name}, need_choose=False)
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='alarmPlanName']//*[starts-with(text(),'{0}')]".format(plan_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='alarmPlanName']//*[text()='{0}']".format(plan_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            search_result = pe.text
            pe.click()
            log.info("选择: {0}".format(search_result))
            if self._get_status(search_result):
                self.browser.find_element(
                    By.XPATH, "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(search_result)).click()
                log.info("禁用告警计划: {}".format(search_result))
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("确认禁用{0}吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    sleep(1)
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("操作成功"):
                        log.info("{0} 禁用成功".format(search_result))
                    else:
                        log.warning("{0} 禁用失败，失败提示: {1}".format(search_result, msg))
                        return
                else:
                    log.warning("{0} 禁用失败，失败提示: {1}".format(search_result, msg))
                    return
                # 重新点击该行记录
                self.browser.find_element(
                    By.XPATH, "//*[@field='alarmPlanName']//*[text()='{0}']".format(search_result)).click()
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
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
                            By.XPATH, "//*[@field='alarmPlanName']//*[starts-with(text(),'{0}')]".format(plan_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(plan_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
