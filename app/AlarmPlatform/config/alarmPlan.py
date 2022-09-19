# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:07

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from common.page.func.input import set_textarea
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.AlarmPlatform.main.menu.chooseMenu import choose_menu
from common.page.func.alertBox import BeAlertBox
from common.date.dateUtil import set_calendar
from common.date.dateCalculation import calculation
from time import sleep
from datetime import datetime
from common.log.logger import log


class AlarmPlan:

    def __init__(self):
        self.browser = get_global_var("browser")
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

    def choose(self, plan_name):
        """
        :param plan_name: 告警计划名称
        """
        input_ele = self.browser.find_element_by_xpath("//*[@name='alarmPlanName']/preceding-sibling::input")
        input_ele.clear()
        input_ele.send_keys(plan_name)
        self.browser.find_element_by_xpath("//span[text()='查询']").click()
        page_wait()
        self.browser.find_element_by_xpath("//*[@field='alarmPlanName']//a[text()='{}']".format(plan_name)).click()
        log.info("已选择告警计划: {}".format(plan_name))

    def add(self, plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc):
        """
        :param plan_name: 告警计划名称
        :param alarm_type: 告警类型
        :param data_source: 数据源名称
        :param region_tag: 标签分类
        :param domain_tag: 领域标签
        :param plan_desc: 计划描述
        """
        self.browser.find_element_by_xpath("//*[@id='addBtn']//*[text()='添加']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmPlanEdit.html')]")))
        sleep(1)
        self.plan_page(plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(plan_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(plan_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc):
        """
        :param obj: 告警计划名称
        :param plan_name: 告警计划名称
        :param alarm_type: 告警类型
        :param data_source: 数据源名称
        :param region_tag: 标签分类
        :param domain_tag: 领域标签
        :param plan_desc: 计划描述
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element_by_xpath("//*[text()='修改']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmPlanEdit.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input")))

        self.plan_page(plan_name, alarm_type, data_source, region_tag, domain_tag, plan_desc)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 修改成功".format(obj))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

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
            self.browser.find_element_by_xpath(
                "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input").clear()
            self.browser.find_element_by_xpath(
                "//*[@class='alarm-edit-form']//*[@name='alarmPlanName']/preceding-sibling::input").send_keys(plan_name)
            log.info("设置告警计划名称: {0}".format(plan_name))

        # 告警类型
        if alarm_type:
            self.browser.find_element_by_xpath(
                "//*[@class='alarm-edit-form']//*[@name='alarmTypeId']/preceding-sibling::input").click()
            sleep(1)
            self.browser.find_element_by_xpath(
                "//*[@class='plan-form']/following-sibling::div//*[contains(@id,'easyui') and text()='{0}']".format(
                    alarm_type)).click()
            log.info("设置告警类型: {0}".format(alarm_type))

        # 数据源名称
        if data_source:
            self.browser.find_element_by_xpath(
                "//*[@class='alarm-edit-form']//*[@name='dataSourceId']/preceding-sibling::input").click()
            sleep(1)
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'dataSourceId') and text()='{0}']".format(data_source)).click()
            log.info("设置数据源名称: {0}".format(data_source))

        # 标签分类
        if region_tag:
            self.browser.find_element_by_xpath("//*[@id='regionTag']/following-sibling::span[1]//a").click()
            sleep(1)
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'regionTag') and text()='{0}']".format(region_tag)).click()
            log.info("设置标签分类: {0}".format(region_tag))

        # 领域标签
        if domain_tag:
            self.browser.find_element_by_xpath("//*[@id='domainTag']/following-sibling::span[1]//a").click()
            sleep(1)
            self.browser.find_element_by_xpath(
                "//*[contains(@id,'domainTag') and text()='{0}']".format(domain_tag)).click()
            log.info("设置领域标签: {0}".format(domain_tag))

        # 计划描述
        if plan_desc:
            remark_textarea = self.browser.find_element_by_xpath("//*[@name='alarmPlanDesc']")
            set_textarea(remark_textarea, plan_desc)
            log.info("设置计划描述: {0}".format(plan_desc))

        # 保存
        self.browser.find_element_by_xpath("//*[@funcid='AlarmPlatform_plan_save']//*[text()='保存']").click()

    def update_status(self, obj, set_status, research=True):
        """
        :param obj: 告警计划名称
        :param set_status: 状态，启用/禁用
        :param research: 是否重新查询，默认true
        """
        if research:
            self.choose(plan_name=obj)

        # 获取当前状态
        js = 'return $(".easyui-switchbutton")[0].checked;'
        current_status = self.browser.execute_script(js)
        log.info("【状态】勾选状态: {0}".format(current_status))

        if set_status == "启用":
            if current_status:
                log.info("{0}已启用".format(obj))
            else:
                self.browser.find_element_by_xpath(
                    "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(obj)).click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("确认启用{0}吗".format(obj), auto_click_ok=False):
                    alert.click_ok()
                    sleep(1)
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("操作成功"):
                        log.info("{0} 启用成功".format(obj))
                    else:
                        log.warning("{0} 启用失败，失败提示: {1}".format(obj, msg))
                else:
                    log.warning("{0} 启用失败，失败提示: {1}".format(obj, msg))
                set_global_var("ResultMsg", msg, False)
        else:
            if current_status:
                self.browser.find_element_by_xpath(
                    "//*[text()='{0}']/../../following-sibling::td[3]/div/span".format(obj)).click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("确认禁用{0}吗".format(obj), auto_click_ok=False):
                    alert.click_ok()
                    sleep(1)
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("操作成功"):
                        log.info("{0} 禁用成功".format(obj))
                    else:
                        log.warning("{0} 禁用失败，失败提示: {1}".format(obj, msg))
                else:
                    log.warning("{0} 禁用失败，失败提示: {1}".format(obj, msg))
                set_global_var("ResultMsg", msg, False)
            else:
                log.info("{0}未启用".format(obj))

    def delete(self, obj):
        """
        :param obj: 告警计划名称
        """
        log.info("开始删除数据")
        self.choose(obj)
        self.browser.find_element_by_xpath("//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def redo(self, obj, start_time=None, end_time=None):
        """
        :param obj: 告警计划名称
        :param start_time: 开始时间
        :param end_time: 结束时间
        """
        self.choose(obj)
        self.browser.find_element_by_xpath("//*[text()='重调']").click()
        log.info("开始重调告警计划: {0}".format(obj))
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
        self.browser.find_element_by_xpath("//*[@id='startTime']/following-sibling::span//a").click()
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
        self.browser.find_element_by_xpath("//*[@id='endTime']/following-sibling::span//a").click()
        set_calendar(date_s=end_time, date_format='%Y-%m-%d %H:%M:%S')
        log.info("设置重调结束时间: {0}".format(end_time))

        # 点击确定
        self.browser.find_element_by_xpath("//*[@class='form_row']//*[text()='确定']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 重调成功".format(obj))
        else:
            log.warning("{0} 重调失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: 告警计划名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element_by_xpath("//*[@name='alarmPlanName']/preceding-sibling::input[1]").clear()
        self.browser.find_element_by_xpath("//*[@name='alarmPlanName']/preceding-sibling::input[1]").send_keys(obj)
        self.browser.find_element_by_xpath("//*[text()='查询']").click()
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements_by_xpath(
                "//*[@field='alarmPlanName']/*[contains(@class,'alarmPlanName')]/*[starts-with(text(),'{0}')]".format(obj))
        else:
            record_element = self.browser.find_elements_by_xpath(
                "//*[@field='alarmPlanName']/*[contains(@class,'alarmPlanName')]/*[text()='{0}']".format(obj))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                # 将计划禁用
                self.update_status(obj=search_result, set_status="禁用", research=False)
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element_by_xpath("//*[text()='删除']").click()
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
                            record_element = self.browser.find_elements_by_xpath(
                                "//*[@field='alarmPlanName']/*[contains(@class,'alarmPlanName')]/*[starts-with(text(),'{0}')]".format(
                                    obj))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(obj, msg))
                    set_global_var("ResultMsg", msg, False)
                    break

        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
