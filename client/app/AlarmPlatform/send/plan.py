# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:12

from service.lib.variable.globalVariable import *
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_textarea
from client.page.func.dateUtil import set_calendar
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from client.page.resource.AlarmPlatform.chooseMenu import choose_menu
from client.page.func.alertBox import BeAlertBox
from client.page.func.positionPanel import getPanelXpath
from time import sleep
from service.lib.log.logger import log


class SendPlan:

    def __init__(self):
        self.browser = get_global_var("browser")
        self.upperOrLower = None
        # 进入菜单
        choose_menu("推送计划")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/sendPlan/sendPlanList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='sendPlanName']/preceding-sibling::input[1]")))
        page_wait()
        sleep(1)

    def choose(self, plan_name):
        """
        :param plan_name: 推送计划名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@name='sendPlanName']/preceding-sibling::input[1]")
        input_ele.clear()
        input_ele.send_keys(plan_name)
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_send_query']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='sendPlanName']//*[text()='{0}']".format(plan_name)).click()
        log.info("已选择推送计划名称: {}".format(plan_name))

    def add(self, plan_name, send_type, msg_template, receiver, send_date, effect_start_date, effect_end_date,
            send_start_time, send_end_time, remark):
        """
        :param plan_name: 推送计划名称
        :param send_type: 推送类型
        :param msg_template: 消息模版
        :param receiver: 接收对象
        :param send_date: 推送日期
        :param effect_start_date: 有效开始日期
        :param effect_end_date: 有效结束日期
        :param send_start_time: 有效开始时段
        :param send_end_time: 有效结束时段
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/sendPlan/sendPlanEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='add_send_plan_form']//*[@name='sendPlanName']/preceding-sibling::input[1]")))
        sleep(1)
        self.send_plan_page(plan_name, send_type, msg_template, receiver, send_date, effect_start_date, effect_end_date,
                            send_start_time, send_end_time, remark)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(plan_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(plan_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, plan_name, send_type, msg_template, receiver, send_date, effect_start_date, effect_end_date,
               send_start_time, send_end_time, remark):
        """
        :param obj: 推送计划名称
        :param plan_name: 推送计划名称
        :param send_type: 推送类型
        :param msg_template: 消息模版
        :param receiver: 接收对象
        :param send_date: 推送日期
        :param effect_start_date: 有效开始日期
        :param effect_end_date: 有效结束日期
        :param send_start_time: 有效开始时段
        :param send_end_time: 有效结束时段
        :param remark: 备注
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(timeout=3, back_iframe=False)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return
        else:
            self.browser.switch_to.parent_frame()
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/sendPlan/sendPlanEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[@id='add_send_plan_form']//*[@name='sendPlanName']/preceding-sibling::input[1]")))

            self.send_plan_page(plan_name, send_type, msg_template, receiver, send_date, effect_start_date, effect_end_date,
                                send_start_time, send_end_time, remark)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(obj))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
            set_global_var("ResultMsg", msg, False)

    def send_plan_page(self, plan_name, send_type, msg_template, receiver, send_date, effect_start_date, effect_end_date,
                       send_start_time, send_end_time, remark):
        """
        :param plan_name: 推送计划名称
        :param send_type: 推送类型
        :param msg_template: 消息模版
        :param receiver: 接收对象
        :param send_date: 推送日期
        :param effect_start_date: 有效开始日期
        :param effect_end_date: 有效结束日期
        :param send_start_time: 有效开始时段
        :param send_end_time: 有效结束时段
        :param remark: 备注
        """
        # 推送计划名称
        if plan_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='add_send_plan_form']//*[@name='sendPlanName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='add_send_plan_form']//*[@name='sendPlanName']/preceding-sibling::input[1]").send_keys(
                plan_name)
            log.info("设置推送计划名称: {0}".format(plan_name))

        # 推送类型
        if send_type:
            # 取消所有已勾选
            selected_element = self.browser.find_elements(
                By.XPATH, "//*[@id='sendTypeTr']//*[contains(@class,'checkbox-checked')]")
            for element in selected_element:
                element.click()
            # 重新选择
            for _type in send_type:
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'sendType') and @label='{0}']/following-sibling::span[1]".format(
                        _type)).click()
                log.info("设置推送类型: {0}".format(_type))

        # 消息模版
        if msg_template:
            self.browser.find_element(By.XPATH, "//*[@id='messageTemplateId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'messageTemplateId') and text()='{0}']".format(
                    msg_template)).click()
            log.info("设置消息模版: {0}".format(msg_template))

        # 接收对象
        if receiver:
            self.browser.find_element(By.XPATH, "//*[@id='receiveObjectName']/following-sibling::span//a").click()
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'receiveObject.html')]")))
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@onclick='checkAll();']")))
            sleep(1)

            receiver_type = receiver.get("接收类型")
            receiver_object = receiver.get("接收人")

            # 接收类型
            self.browser.find_element(By.XPATH, "//*[@id='funcAssignType']//*[text()='{0}']".format(receiver_type)).click()
            log.info("设置接收类型: {0}".format(receiver_type))
            sleep(1)

            # 接收人
            self.browser.find_element(By.XPATH, "//*[@onclick='expandAll();']").click()
            sleep(1)
            self.browser.find_element(By.XPATH, "//*[@onclick='checkAll();']").click()
            sleep(1)
            self.browser.find_element(By.XPATH, "//*[@onclick='uncheckAll();']").click()
            sleep(1)

            for person in receiver_object:
                element = self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'menuTree')]//*[@class='tree-title' and text()='{0}']/"
                              "preceding-sibling::span[contains(@class,'tree-checkbox')]".format(person))
                action = ActionChains(self.browser)
                action.move_to_element(element).click().perform()
                log.info("设置接收对象: {0}".format(person))
            self.browser.find_element(By.XPATH, "//*[@onclick='submitMenusForm();']").click()
            self.browser.switch_to.parent_frame()

        # 推送日期
        if send_date:
            # 取消所有已勾选
            selected_element = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'sendDate')]/following-sibling::span//*[contains(@class,'checkbox-checked')]")
            for element in selected_element:
                element.click()
            # 重新选择
            for _date in send_date:
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'sendDate') and @label='{0}']/following-sibling::span[1]".format(
                        _date)).click()
                log.info("设置推送日期: {0}".format(_date))

        # 有效开始日期
        if effect_start_date:
            self.browser.find_element(By.XPATH, "//*[@id='effectStartDate']/following-sibling::span[1]//a").click()
            set_calendar(date_s=effect_start_date, date_format='%Y-%m-%d')
            log.info("设置有效开始日期: {0}".format(effect_start_date))

        # 有效结束日期
        if effect_end_date:
            self.browser.find_element(By.XPATH, "//*[@id='effectEndDate']/following-sibling::span[1]//a").click()
            set_calendar(date_s=effect_end_date, date_format='%Y-%m-%d')
            log.info("设置有效结束日期: {0}".format(effect_end_date))

        # 有效开始时段
        if send_start_time:
            self.browser.find_element(By.XPATH, "//*[@id='sendStartTime']/following-sibling::span[1]//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='sendStartTime']/following-sibling::span[1]//input[1]").send_keys(send_start_time)
            log.info("设置有效开始时段: {0}".format(send_start_time))

        # 有效结束时段
        if send_end_time:
            self.browser.find_element(By.XPATH, "//*[@id='sendEndTime']/following-sibling::span[1]//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='sendEndTime']/following-sibling::span[1]//input[1]").send_keys(send_end_time)
            log.info("设置有效结束时段: {0}".format(send_end_time))

        # 备注
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置备注: {0}".format(remark))

        # 保存
        self.browser.find_element(By.XPATH, "//*[contains(@data-options,'icon-ok')]").click()

    def update_status(self, plan_name, set_status, research=True):
        """
        :param plan_name: 推送计划名称
        :param set_status: 状态，启用/禁用
        :param research: 是否重新查询，默认true
        """
        if research:
            self.choose(plan_name)

        # 获取当前状态
        js = 'return $(".easyui-switchbutton")[0].checked;'
        current_status = self.browser.execute_script(js)
        log.info("【状态】勾选状态: {0}".format(current_status))

        temp = True if set_status == "启用" else False
        if temp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[@field ='sendPlanName']//*[text()='{0}']/../../following-sibling::td[@field='sendPlanStatus']/div/span".format(
                    plan_name)).click()
            alert = BeAlertBox(timeout=1, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确认{0}{1}吗".format(set_status, plan_name), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("{0} {1} 成功".format(set_status, plan_name))
                else:
                    log.warning("{0} {1} 失败，失败提示: {2}".format(set_status, plan_name, msg))
            else:
                log.warning("{0} {1} 失败，失败提示: {2}".format(set_status, plan_name, msg))
            set_global_var("ResultMsg", msg, False)

    def delete(self, plan_name):
        """
        :param plan_name: 消息模版名称
        """
        log.info("开始删除数据")
        self.choose(plan_name)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(plan_name), auto_click_ok=False):
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
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, plan_name, fuzzy_match=False):
        """
        :param plan_name: 消息模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='sendPlanName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@name='sendPlanName']/preceding-sibling::input[1]").send_keys(plan_name)
        self.browser.find_element(By.XPATH, "//*[@funcid ='AlarmPlatform_send_query']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field ='sendPlanName']//*[starts-with(text(),'{0}')]".format(plan_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field ='sendPlanName']//*[text()='{0}']".format(plan_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                # 将发送计划禁用
                self.update_status(plan_name=search_result, set_status="禁用", research=False)
                log.info("选择: {0}".format(search_result))
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
                                By.XPATH, "//*[@field ='sendPlanName']//*[starts-with(text(),'{0}')]".format(plan_name))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(plan_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
