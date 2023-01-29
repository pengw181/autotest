# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:07

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_textarea
from client.page.statics.AlarmPlatform.chooseMenu import choose_menu
from client.page.func.alertBox import BeAlertBox
from client.page.func.pagination import Pagination
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


class MsgTemplate:

    def __init__(self):
        self.browser = get_global_var("browser")
        self.upperOrLower = None
        # 进入菜单
        choose_menu("告警配置-消息模版")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/messageTemplate/messageTemplateList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='templateName']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def choose(self, msg_temp_name):
        """
        :param msg_temp_name: 消息模版名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@name='templateName']/preceding-sibling::input")
        input_ele.clear()
        input_ele.send_keys(msg_temp_name)
        self.browser.find_element(By.XPATH, "//span[text()='查询']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='templateName']//a[text()='{}']".format(msg_temp_name)).click()
        log.info("已选择消息模版: {}".format(msg_temp_name))

    def add(self, rule_name, msg_temp_name, title, remark, config_model, result_tag, tag_config, input_template):
        """
        :param rule_name: 告警规则名称
        :param msg_temp_name: 消息模版名称
        :param title: 模版标题
        :param remark: 消息模版描述
        :param config_model: 配置模式
        :param result_tag: 结果标签，数组
        :param tag_config: 模版配置，字典
        :param input_template: 模版输入
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/messageTemplate/editMessageTemplate.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='template_name']")))
        sleep(1)
        self.msg_temp_page(rule_name, msg_temp_name, title, remark, config_model, result_tag, tag_config, input_template)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='template_add']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(msg_temp_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(msg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, msg_temp_name, title, remark, config_model, result_tag, tag_config, input_template):
        """
        :param obj: 消息模版名称
        :param msg_temp_name: 消息模版名称
        :param title: 模版标题
        :param remark: 消息模版描述
        :param config_model: 配置模式
        :param result_tag: 结果标签，数组
        :param tag_config: 模版配置，字典
        :param input_template: 模版输入
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
                By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/messageTemplate/editMessageTemplate.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='template_name']")))

            self.msg_temp_page(None, msg_temp_name, title, remark, config_model, result_tag, tag_config, input_template)

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='template_add']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(obj))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
            set_global_var("ResultMsg", msg, False)

    def msg_temp_page(self, rule_name, msg_temp_name, title, remark, config_model, result_tag, tag_config, input_template):
        """
        :param rule_name: 告警规则名称
        :param msg_temp_name: 消息模版名称
        :param title: 模版标题
        :param remark: 消息模版描述
        :param config_model: 配置模式
        :param result_tag: 结果标签，数组
        :param tag_config: 模版配置，数组
        :param input_template: 模版输入
        """
        # 告警规则名称
        if rule_name:
            self.browser.find_element(By.XPATH, "//*[@id='select_plan_select']/following-sibling::div//i").click()
            sleep(1)
            rule_name_ele = self.browser.find_element(
                By.XPATH, "//*[@id='select_plan_select']/following-sibling::div//dd[text()='{}']".format(rule_name))
            action = ActionChains(self.browser)
            action.move_to_element(rule_name_ele).click().perform()
            log.info("设置告警规则名称: {0}".format(rule_name))

        # 判断字段标签是大写或小写
        data_col_obj = self.browser.find_element(By.XPATH, "//*[@ID='editable_field1']/li[2]")
        col_temp = data_col_obj.get_attribute("innerText")
        if col_temp == col_temp.upper():
            self.upperOrLower = "upper"
            log.info("表字段大写")
        else:
            self.upperOrLower = "lower"
            log.info("表字段小写")
        set_global_var("UpperOrLower", self.upperOrLower, False)

        # 消息模版名称
        if msg_temp_name:
            self.browser.find_element(By.XPATH, "//*[@id='template_name']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='template_name']").send_keys(msg_temp_name)
            log.info("设置消息模版名称: {0}".format(msg_temp_name))

        # 模版标题
        if title:
            self.browser.find_element(By.XPATH, "//*[@id='template_subject']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='template_subject']").send_keys(title)
            log.info("设置模版标题: {0}".format(title))

        # 消息模版描述
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='template_desc']")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置消息模版描述: {0}".format(remark))

        # 配置模式
        if config_model:
            self.browser.find_element(
                By.XPATH, "//*[@lay-filter='radio_config_model']/following-sibling::div/*[text()='{0}']".format(
                    config_model)).click()
            log.info("设置配置模式: {0}".format(config_model))

        # 结果标签
        if result_tag:
            # 先删除所有已配置了字典的字段标签
            config_field_elements = self.browser.find_elements(
                By.XPATH, "//*[@id='editable_field1']/*[contains(@id,'config_')]/i")
            if len(config_field_elements) > 0:
                for element in config_field_elements:
                    element.click()
            # 配置字段标签，配置之后，id会变成config_xx
            for tag in result_tag:
                tag_name = tag[0]
                dict_name = tag[1]

                # 字段转换大小写
                if get_global_var("UpperOrLower") == "upper":
                    tag_name = tag_name.upper()
                else:
                    tag_name = tag_name.lower()

                # 点击字段名
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id, 'noconfig') and text()='{0}']".format(tag_name)).click()
                sleep(1)
                # 选择字典
                self.browser.find_element(By.XPATH, "//*[@id='dictionary_table_div']//i").click()
                sleep(1)
                dict_ele = self.browser.find_element(
                    By.XPATH, "//*[@id='dictionary_table_div']//dd[text()='{0}']".format(dict_name))
                action = ActionChains(self.browser)
                action.move_to_element(dict_ele).click().perform()
                sleep(1)
                # 保存字典
                self.browser.find_element(By.XPATH, "//*[@id='save_dictionary']").click()
                # 验证字典是否设置成功
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@id='editable_field1']/li[@id='config_{0}']".format(tag_name))
                except NoSuchElementException:
                    raise Exception("标签【{0}】设置字典失败".format(tag_name))
                else:
                    log.info("标签【{0}】设置字典【{1}】".format(tag_name, dict_name))

        # 模版配置
        """
        tag_config:
        [
            {
                "标签类型": "结果标签",
                "标签名称": "OBJ_STATUS"
            },
            {
                "标签类型": "结果标签",
                "标签名称": "OBJ_STATUS",
                "已配置": "是"
            },
            {
                "标签类型": "公共标签",
                "标签名称": "自定义文本",
                "自定义值": "网元名称："
            },
            {
                "标签类型": "公共标签",
                "标签名称": "换行"
            }
        ]
        """
        if tag_config:
            # 先清空所有标签
            self.browser.find_element(By.XPATH, "//*[@id='delete_all_result_item']").click()
            sleep(1)
            last_tag_in_config = None
            for tag_info in tag_config:
                tag_type = tag_info.get("标签类型")
                tag_name = tag_info.get("标签名称")

                # 字段转换大小写
                if get_global_var("UpperOrLower") == "upper":
                    tag_name = tag_name.upper()
                else:
                    tag_name = tag_name.lower()

                # 加入结果标签
                config_flag = False
                if tag_type == "结果标签":
                    config_flag = tag_info.get("已配置")
                    if config_flag == "是":
                        config_flag = True

                    if config_flag:
                        if len(tag_name) > 9:
                            # 标签名字长度超过9，后面会多出...
                            tag_ele = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_field1']/*[contains(@id,'config_{0}') and @title='{0}']".format(
                                    tag_name))
                        else:
                            tag_ele = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_field1']/*[contains(@id,'config_{0}') and text()='{0}']".format(
                                    tag_name))
                    else:
                        if len(tag_name) > 9:
                            tag_ele = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_field1']/*[contains(@id,'noconfig') and @title='{0}']".format(
                                    tag_name))
                        else:
                            tag_ele = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_field1']/*[contains(@id,'noconfig') and text()='{0}']".format(
                                    tag_name))
                # 加入公共标签
                elif tag_type == "公共标签":
                    tag_ele = self.browser.find_element(
                        By.XPATH, "//*[@id='editable_field']//*[text()='{0}']".format(tag_name))
                else:
                    raise KeyError("标签类型【{0}】错误".format(tag_type))

                # 将标签拖到模版配置框中，如果是第一次加入，则直接拖入配置池，否则已到距离最后一个标签x_offset=5，y_offset=0距离的位置
                action = ActionChains(self.browser)
                if last_tag_in_config is None:
                    target = self.browser.find_element(By.XPATH, "//*[@id='editable_trigger']")
                    action.drag_and_drop(tag_ele, target).perform()
                else:
                    target = last_tag_in_config
                    action.click_and_hold(tag_ele).move_to_element_with_offset(target, xoffset=100, yoffset=0).release().perform()
                log.info("模版配置加入标签【{0}】".format(tag_name))

                # 自定义值标签设置自定义值
                if tag_name == "自定义文本":
                    msg = tag_info.get("自定义值")
                    self.browser.find_element(
                        By.XPATH, "//*[@id='editable_trigger']//*[contains(@id,'common_item') and text()='自定义文本']").click()
                    text_area = self.browser.find_element(By.XPATH, "//*[@id='customer_text_value']")
                    set_textarea(textarea=text_area, msg=msg)
                    log.info("自定义文本标签设置值: {0}".format(msg))
                    # 点击保存
                    self.browser.find_element(By.XPATH, "//*[@id='save_customize_text']").click()
                    # 获取配置池最后一个标签
                    last_tag_in_config = self.browser.find_element(
                        By.XPATH, "//*[@id='editable_trigger']/*[contains(@id,'common_item') and text()='{0}']".format(msg))
                # 结果标签
                elif tag_type == "结果标签":
                    if len(tag_name) > 9:
                        last_tag_in_config = self.browser.find_element(
                            By.XPATH, "//*[@id='editable_trigger']/*[contains(@id,'noconfig') and @title='{0}']".format(tag_name))
                    else:
                        if config_flag:
                            last_tag_in_config = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_trigger']/*[contains(@id,'config') and text()='{0}']".format(tag_name))
                        else:
                            last_tag_in_config = self.browser.find_element(
                                By.XPATH, "//*[@id='editable_trigger']/*[contains(@id,'noconfig') and text()='{0}']".format(tag_name))
                # 换行
                else:
                    last_tag_in_config = self.browser.find_element(
                        By.XPATH, "//*[@id='editable_trigger']/*[contains(@id,'common_item') and text()='换行']")

            # 结果预览
            result_view_ele = self.browser.find_element(By.XPATH, "//*[@id='preview_mess_result_text']")
            result_view_text = result_view_ele.get_attribute("value")
            log.info("结果预览: {0}".format(result_view_text))

        # 模版输入
        if input_template:
            input_template_textarea = self.browser.find_element(By.XPATH, "//*[@id='input_template']")
            set_textarea(textarea=input_template_textarea, msg=input_template)
            log.info("模版输入设置值: {0}".format(input_template))

    def update_status(self, msg_temp_name, set_status, research=True):
        """
        :param msg_temp_name: 消息模版名称
        :param set_status: 状态，启用/禁用
        :param research: 是否重新查询，默认true
        """
        if research:
            self.choose(msg_temp_name)

        # 获取当前状态
        js = 'return $(".active_template_op")[0].checked;'
        current_status = self.browser.execute_script(js)
        log.info("【状态】勾选状态: {0}".format(current_status))

        temp = True if set_status == "启用" else False
        if temp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[text()='{0}']/../../../following-sibling::td[2]/div/span".format(msg_temp_name)).click()
            alert = BeAlertBox(timeout=1, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} {1} 成功".format(set_status, msg_temp_name))
            else:
                log.warning("{0} {1} 失败，失败提示: {2}".format(set_status, msg_temp_name, msg))
            set_global_var("ResultMsg", msg, False)

    def set_default_template(self, msg_temp_name, set_default):
        """
        :param msg_temp_name: 消息模版名称
        :param set_default: 默认模版，是/否
        """
        self.choose(msg_temp_name)

        # 获取当前状态
        js = 'return $(".is_default_template")[0].checked;'
        default_status = self.browser.execute_script(js)
        log.info("【默认模版】勾选状态: {0}".format(default_status))

        if set_default == "是":
            if default_status:
                log.info("{0}已经设置为默认模版".format(msg_temp_name))
                set_global_var("ResultMsg", "操作成功", False)
            else:
                self.browser.find_element(
                    By.XPATH, "//*[text()='{0}']/../../../following-sibling::td[3]/div/span".format(msg_temp_name)).click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("{0}已经设置为默认模版".format(msg_temp_name))
                elif alert.title_contains("模版已禁用，不能设置为默认消息模版"):
                    log.warning("更新默认消息模版状态失败，失败提示: {0}".format(msg))
                else:
                    log.warning("更新默认消息模版状态失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)
        else:
            if default_status:
                self.browser.find_element(
                    By.XPATH, "//*[text()='{0}']/../../../following-sibling::td[3]/div/span".format(msg_temp_name)).click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("更新默认消息模版状态成功")
                else:
                    log.warning("更新默认消息模版状态失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)
            else:
                log.info("{0}已经取消设置为默认模版".format(msg_temp_name))

    def query(self, query):
        """
        :param query: 查询条件
        """
        if isinstance(query, dict):
            # 告警计划名称
            if query.__contains__("告警计划名称"):
                alarm_plan_name = query.get("告警计划名称")
                self.browser.find_element(By.XPATH, "//*[@name='alarmPlanName']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='alarmPlanName']/preceding-sibling::input").send_keys(alarm_plan_name)
                log.info("告警计划名称输入: {0}".format(alarm_plan_name))

            # 告警规则名称
            if query.__contains__("告警规则名称"):
                alarm_rule_name = query.get("告警规则名称")
                self.browser.find_element(By.XPATH, "//*[@name='alarmRuleName']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='alarmRuleName']/preceding-sibling::input").send_keys(alarm_rule_name)
                log.info("告警规则名称输入: {0}".format(alarm_rule_name))

            # 消息模版名称
            if query.__contains__("消息模版名称"):
                template_name = query.get("消息模版名称")
                self.browser.find_element(By.XPATH, "//*[@name='templateName']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='templateName']/preceding-sibling::input").send_keys(template_name)
                log.info("消息模版名称输入: {0}".format(template_name))

            # 状态
            if query.__contains__("状态"):
                status = query.get("状态")
                self.browser.find_element(
                    By.XPATH, "//*[@textboxname ='templateState']/following-sibling::span//a").click()
                sleep(1)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'templateState') and text()='{0}']".format(status)).click()
                log.info("状态选择: {0}".format(status))

            # 创建人
            if query.__contains__("创建人"):
                creator = query.get("创建人")
                self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input").send_keys(creator)
                log.info("创建人输入: {0}".format(creator))

            # 查询
            self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_msg_query']//*[text()='查询']").click()
            page_wait()
            sleep(1)
            return
        else:
            raise KeyError("查询条件不是字典")

    def batch_enable(self, query):
        """
        # 批量将查询后的数据启用
        :param query: 查询条件
        """
        self.query(query)
        table_xpath = "//*[@id='tb']/following-sibling::div[2]/table"
        p = Pagination(table_xpath)
        p.set_page_size(size=50)
        row_status = self.browser.find_elements(
            By.XPATH, "//*[contains(@class,'active_template_op')]/following-sibling::span")
        if len(row_status) > 0:
            num = 0
            enable_success_flag = True  # 更新是否成功标识
            while enable_success_flag:
                element = row_status[num]
                js = 'return $(".active_template_op")[{0}].checked;'.format(num)
                current_status = self.browser.execute_script(js)
                if current_status:
                    set_global_var("ResultMsg", "操作成功", False)
                    if num == len(row_status)-1:
                        break
                    else:
                        num += 1
                else:
                    action = ActionChains(self.browser)
                    action.move_to_element(element).click().perform()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("操作成功"):
                        # 更新状态成功后，会将该条记录置于列表顶部（更新了修改时间）
                        num = 0
                        # 如果查询条件包含了状态，更新成功后会自动刷新页面，需要重新获取
                        row_status = self.browser.find_elements(
                            By.XPATH, "//*[contains(@class,'active_template_op')]/following-sibling::span")
                        if len(row_status) == 0:
                            break
                        sleep(1)
                    else:
                        log.warning("第{0}行启用失败，失败提示: {1}".format(num+1, msg))
                        break
                    set_global_var("ResultMsg", msg, False)
        else:
            raise Exception("未查询到记录")

    def batch_disable(self, query):
        """
        # 批量将查询后的数据启用
        :param query: 查询条件
        """
        self.query(query)
        table_xpath = "//*[@id='tb']/following-sibling::div[2]/table"
        p = Pagination(table_xpath)
        p.set_page_size(size=50)
        row_status = self.browser.find_elements(
            By.XPATH, "//*[contains(@class,'active_template_op')]/following-sibling::span")
        if len(row_status) > 0:
            num = 0
            enable_success_flag = True  # 更新是否成功标识
            while enable_success_flag:
                element = row_status[num]
                js = 'return $(".active_template_op")[{0}].checked;'.format(num)
                current_status = self.browser.execute_script(js)
                if not current_status:
                    set_global_var("ResultMsg", "操作成功", False)
                    if num == len(row_status)-1:
                        break
                    else:
                        num += 1
                else:
                    action = ActionChains(self.browser)
                    action.move_to_element(element).click().perform()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("操作成功"):
                        # 更新状态成功后，会将该条记录置于列表顶部（更新了修改时间）
                        num = 0
                        # 如果查询条件包含了状态，更新成功后会自动刷新页面，需要重新获取
                        row_status = self.browser.find_elements(
                            By.XPATH, "//*[contains(@class,'active_template_op')]/following-sibling::span")
                        if len(row_status) == 0:
                            break
                        sleep(1)
                    else:
                        log.warning("第{0}行禁用失败，失败提示: {1}".format(num+1, msg))
                        break
                    set_global_var("ResultMsg", msg, False)
        else:
            raise Exception("未查询到记录")

    def delete(self, msg_temp_name):
        """
        :param msg_temp_name: 消息模版名称
        """
        log.info("开始删除数据")
        self.choose(msg_temp_name)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(msg_temp_name, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(msg_temp_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(msg_temp_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(msg_temp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, msg_temp_name, fuzzy_match=False):
        """
        :param msg_temp_name: 消息模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='templateName']/preceding-sibling::input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@name='templateName']/preceding-sibling::input[1]").send_keys(msg_temp_name)
        self.browser.find_element(By.XPATH, "//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='templateName']//*[starts-with(text(),'{0}')]".format(msg_temp_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='templateName']//*[text(),'{0}']".format(msg_temp_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                # 将模版禁用
                self.update_status(msg_temp_name=search_result, set_status="禁用", research=False)
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
                                By.XPATH, "//*[@field='templateName']//*[starts-with(text(),'{0}')]".format(msg_temp_name))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(msg_temp_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
