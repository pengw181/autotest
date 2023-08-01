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
from selenium.webdriver import ActionChains
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.lib.tableData import get_table_data2
from src.main.python.core.app.AlarmPlatform.menu import choose_menu
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.pagination import Pagination
from src.main.python.lib.dateUtil import set_calendar, set_laydate
from src.main.python.lib.dateCalculation import calculation
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class AlarmRule:

    def __init__(self):
        self.rule_name = None
        self.upperOrLower = None
        self.browser = gbl.service.get("browser")
        # 进入菜单
        choose_menu("告警配置-告警规则")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/alarmConfig/alarmRuleList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='alarmRuleName']/preceding-sibling::input")))
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

        # 告警规则名称
        if query.__contains__("告警规则名称"):
            rule_name = query.get("告警规则名称")
            self.browser.find_element(By.XPATH, "//*[@name='alarmRuleName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='alarmRuleName']/preceding-sibling::input[1]").send_keys(
                rule_name)
            select_item = rule_name

        # 状态
        if query.__contains__("状态"):
            alarm_status = query.get("状态")
            self.browser.find_element(By.XPATH, "//*[@name='alarmStatus']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(alarm_status)).click()

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='creator']/preceding-sibling::input[1]").send_keys(
                creator)

        # 告警等级
        if query.__contains__("告警等级"):
            data_level = query.get("告警等级")
            self.browser.find_element(By.XPATH, "//*[@name='alarmLevelId']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(data_level)).click()

        # 告警类型
        if query.__contains__("告警类型"):
            alarm_type = query.get("告警类型")
            self.browser.find_element(By.XPATH, "//*[@name='alarmTypeId']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(alarm_type)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_rule_query']").click()
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
                        By.XPATH, "//*[@field='alarmRuleName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, alarm_type, alarm_plan, basic_conf, dimension_conf, filter_conf, result_conf, storage_conf):
        """
        :param alarm_type: 告警类型
        :param alarm_plan: 告警计划
        :param basic_conf: 基本信息配置
        :param dimension_conf: 告警维度配置
        :param filter_conf: 过滤条件配置
        :param result_conf: 告警结果配置
        :param storage_conf: 告警存储配置
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/alarmRuleBeforeAdd.html')]")))
        sleep(1)

        # 告警类型
        if alarm_type:
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@comboname='alarmTypeId']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[@class='plan-form']/following-sibling::div//*[contains(@id,'easyui') and text()='{0}']".format(
                    alarm_type)).click()
            log.info("设置告警类型: {0}".format(alarm_type))

        # 告警计划
        if alarm_plan:
            self.browser.find_element(
                By.XPATH, "//*[@class='alarm-edit-form']//*[@comboname='alarmPlanId']/following-sibling::span[1]//a").click()
            sleep(1)
            self.browser.find_element(By.XPATH, "//*[contains(@id,'alarmPlanId') and text()='{0}']".format(
                alarm_plan)).click()
            log.info("设置告警计划: {0}".format(alarm_plan))

        # 点击确定进入基本信息配置
        self.browser.find_element(By.XPATH, "//*[@class='form_row']/following-sibling::div//*[text()='确定']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/alarmConfig/../dbRuleConfig/addAlarmRule.html')]")))
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='add_rule_name']")))

        self.rule_page(basic_conf, dimension_conf, filter_conf, result_conf, storage_conf)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(self.rule_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(self.rule_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, rule, basic_conf, dimension_conf, filter_conf, result_conf, storage_conf):
        """
        :param rule: 告警规则名称
        :param basic_conf: 基本信息配置
        :param dimension_conf: 告警维度配置
        :param filter_conf: 过滤条件配置
        :param result_conf: 告警结果配置
        :param storage_conf: 告警存储配置
        """
        self.search(query={"告警规则名称": rule}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        alert = BeAlertBox(timeout=3, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
            return
        else:
            self.browser.switch_to.parent_frame()
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dbRuleConfig/editAlarmRule.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='add_rule_name']")))

            self.rule_page(basic_conf, dimension_conf, filter_conf, result_conf, storage_conf)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("修改成功"):
                log.info("{0} 修改成功".format(rule))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(rule, msg))
            gbl.temp.set("ResultMsg", msg)

    def rule_page(self, basic_conf, dimension_conf, filter_conf, result_conf, storage_conf):
        """
        :param basic_conf: 基本信息配置
        :param dimension_conf: 告警维度配置
        :param filter_conf: 过滤条件配置
        :param result_conf: 告警结果配置
        :param storage_conf: 告警存储配置
        """
        # 基本信息配置
        if basic_conf:
            self.basic_config(rule_name=basic_conf.get("规则名称"), rule_desc=basic_conf.get("规则描述"),
                              alarm_level=basic_conf.get("告警等级"), valid_begin_time=basic_conf.get("有效开始时间"),
                              valid_end_time=basic_conf.get("有效结束时间"), start_time=basic_conf.get("开始时间"),
                              ym=basic_conf.get("同比/环比"), series_time=basic_conf.get("连续次数"),
                              rate=basic_conf.get("检测频率"), rate_unit=basic_conf.get("检测频率单位"),
                              compare_field=basic_conf.get("同/环比字段"), yq_base_value=basic_conf.get("字段基值"),
                              yq_period=basic_conf.get("周期单位"))
        # 基本信息配置页面点击下一步，进入告警维度配置页面
        self.browser.find_element(By.XPATH, "//*[@id='rule_name_next']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='createDemensionTreeColumnDiv']//*[text()='领域']/following-sibling::i")))

        # 告警维度配置
        if dimension_conf:
            self.dimension_config(domain=dimension_conf.get("领域"))
        # 告警维度页面点击下一步，进入过滤条件配置页面
        self.browser.find_element(By.XPATH, "//*[@id='rule_dimension_next']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='rule_config_next']")))

        # 过滤条件配置
        if filter_conf:
            self.filter_config(filter_condition=filter_conf.get("过滤条件"), alarm_area_config=filter_conf.get("告警区域配置"),
                               view_config=filter_conf.get("配置预览"), test_config=filter_conf.get("规则测试"))
        # 过滤条件配置页面点击下一步，进入告警结果配置页面
        self.browser.find_element(By.XPATH, "//*[@id='rule_config_next']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='rule_result_next']")))

        # 告警结果配置
        if result_conf:
            self.result_config(result_field=result_conf.get("告警字段英文名"))
        # 告警结果配置页面点击下一步，进入告警存储配置页面
        self.browser.find_element(By.XPATH, "//*[@id='rule_result_next']").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='rule_result_output_next']")))

        # 告警存储配置
        if storage_conf:
            self.storage_config(config_ftp=storage_conf.get("FTP存储"), config_table=storage_conf.get("数据库存储"))

        # 告警存储配置页面点击保存，保存整个配置
        self.browser.find_element(By.XPATH, "//*[@id='rule_result_output_next']").click()

    def basic_config(self, rule_name, rule_desc, alarm_level, valid_begin_time, valid_end_time, start_time, ym,
                     series_time, rate, rate_unit, compare_field, yq_base_value, yq_period):
        """
        :param rule_name: 规则名称
        :param rule_desc: 规则描述
        :param alarm_level: 告警等级
        :param valid_begin_time: 有效开始时间
        :param valid_end_time: 有效结束时间
        :param start_time: 开始时间
        :param ym: 同比/环比
        :param series_time: 连续次数
        :param rate: 检测频率
        :param rate_unit: 检测频率单位
        :param compare_field: 同/环比字段
        :param yq_base_value: 字段基值
        :param yq_period: 周期单位
        """
        # 规则名称
        if rule_name:
            self.browser.find_element(By.XPATH, "//*[@id='add_rule_name']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='add_rule_name']").send_keys(rule_name)
            log.info("设置规则名称: {0}".format(rule_name))

        # 规则描述
        if rule_desc:
            rule_desc_textarea = self.browser.find_element(By.XPATH, "//*[@id='add_rule_desc']")
            set_textarea(rule_desc_textarea, rule_desc)
            log.info("设置规则描述: {0}".format(rule_desc))
            sleep(1)

        # 告警等级
        if alarm_level:
            self.browser.find_element(By.XPATH, "//*[@id='rule_config_level']//i").click()
            sleep(1)
            alarm_level_ele = self.browser.find_element(
                By.XPATH, "//*[@id='rule_config_level']//dd[text()='{0}']".format(alarm_level))
            action = ActionChains(self.browser)
            action.move_to_element(alarm_level_ele).click().perform()
            log.info("设置告警等级: {0}".format(alarm_level))

        # 有效开始时间
        if valid_begin_time:
            self.browser.find_element(By.XPATH, "//*[@id='rule_task_config_startTime']").click()
            set_laydate(date_s=valid_begin_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("设置有效开始时间: {0}".format(valid_begin_time))

        # 有效结束时间
        if valid_end_time:
            self.browser.find_element(By.XPATH, "//*[@id='rule_task_config_endTime']").click()
            set_laydate(date_s=valid_end_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("设置有效结束时间: {0}".format(valid_end_time))

        # 开始时间
        if start_time:
            self.browser.find_element(By.XPATH, "//*[@id='rule_config_trigger_time']").click()
            set_laydate(date_s=start_time, date_format='%Y-%m-%d %H:%M:%S')
            log.info("设置开始时间: {0}".format(start_time))

        # 同比/环比
        if ym:
            self.browser.find_element(By.XPATH, "//*[@id='select_yqoyq_div']//i").click()
            self.browser.find_element(By.XPATH, "//*[@id='select_yqoyq_div']//dd[text()='{}']".format(ym)).click()
            log.info("设置同比/环比: {0}".format(ym))

        # 连续次数
        if series_time:
            self.browser.find_element(By.XPATH, "//*[@id='rule_alarm_config_isSeries']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='rule_alarm_config_isSeries']").send_keys(series_time)
            log.info("设置连续次数: {0}".format(series_time))

        # 检测频率
        if rate:
            self.browser.find_element(By.XPATH, "//*[@id='rule_alarm_rate']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='rule_alarm_rate']").send_keys(rate)
            log.info("设置连续次数: {0}".format(rate))

        # 检测频率单位
        if rate_unit:
            self.browser.find_element(By.XPATH, "//*[@id='rule_config_rateunit']//i").click()
            self.browser.find_element(
                By.XPATH, "//*[@id='rule_config_rateunit']//dd[text()='{}']".format(rate_unit)).click()
            log.info("设置检测频率单位: {0}".format(rate_unit))

        # 同/环比字段
        if compare_field:
            self.browser.find_element(By.XPATH, "//*[@id='yq_field']//i").click()
            sleep(1)
            compare_field_ele = self.browser.find_element(
                By.XPATH, "//*[@id='yq_field']//dd[text()='{}']".format(compare_field))
            action = ActionChains(self.browser)
            action.move_to_element(compare_field_ele).click().perform()
            log.info("设置同/环比字段: {0}".format(compare_field))

        # 字段基值
        if yq_base_value:
            self.browser.find_element(By.XPATH, "//*[@id='yq_base_value']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='yq_base_value']").send_keys(yq_base_value)
            log.info("设置字段基值: {0}".format(yq_base_value))

        # 周期单位
        if yq_period:
            self.browser.find_element(By.XPATH, "//*[@id='select_yqoyq_period_div']//i").click()
            self.browser.find_element(
                By.XPATH, "//*[@id='select_yqoyq_period_div']//dd[text()='{}']".format(yq_period)).click()
            log.info("设置周期单位: {0}".format(yq_period))

        # 获取当前告警规则名称
        self.rule_name = self.browser.find_element(By.XPATH, "//*[@id='add_rule_name']").get_attribute("value")
        if self.rule_name is not None:
            log.info("获取规则名称: {0}".format(self.rule_name))

    def dimension_config(self, domain):
        """
        :param domain: 领域，数组
        """
        # 获取领域勾选状态
        domain_checkbox = self.browser.find_element(By.XPATH, "//*[text()='领域']/..")
        checked_status = domain_checkbox.get_attribute("class")
        checked_status = True if checked_status.find("checked") > -1 else False

        # 领域
        if domain:
            if not checked_status:
                self.browser.find_element(By.XPATH, "//*[text()='领域']").click()
                sleep(1)
            log.info("勾选【领域】")

            for d in domain:
                self.browser.find_element(By.XPATH, "//*[@title='{0}']/following-sibling::div[1]/span".format(d)).click()
                log.info("领域选择: {0}".format(d))
        else:
            if checked_status:
                self.browser.find_element(By.XPATH, "//*[text()='领域']").click()
            log.info("取消勾选【领域】")

    def filter_config(self, filter_condition, alarm_area_config, view_config, test_config):
        """
        :param filter_condition: 过滤条件，数组
        :param alarm_area_config: 告警区域配置，字典
        :param view_config: 配置预览，是/否
        :param test_config: 规则测试，是/否

        {
            "过滤条件": [
                {
                    "标签类型": "公共标签",
                    "标签名": "",
                    "标签属性": {
                        "逻辑条件": "",
                        "字段类型": "",
                        "字段值": ""
                    }
                },
                {
                    "标签类型": "字段标签",
                    "标签名": "",
                    "标签属性": ""
                },
                {
                    "标签类型": "公共标签",
                    "标签名": "",
                    "标签属性": {
                        "逻辑条件": "",
                        "字符值": ""
                    }
                }
            ],
            "告警区域配置": {
                "col_2": {
                    "聚合函数": "",
                    "结果名称": "",
                    "阈值条件": "",
                    "告警阈值": ""
                },
                "col_3": {
                    "聚合函数": "",
                    "结果名称": "",
                    "阈值条件": "",
                    "告警阈值": ""
                }
            },
            "配置预览": "是",
            "规则测试": "是"
        }
        """
        # 过滤条件
        if filter_condition:
            # 先点击清空
            self.browser.find_element(By.XPATH, "//*[@id='delete_all_where_item']").click()
            focus_area = self.browser.find_element(By.XPATH, "//*[@id='alarm_rule_config_div']//*[text()='公共标签']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", focus_area)
            for f in filter_condition:
                tag_type = f.get("标签类型")
                tag_name = f.get("标签名")
                tag_attribute = f.get("标签属性")

                # 判断字段标签是大写或小写
                data_col_obj = self.browser.find_element(By.XPATH, "//*[@ID='field_item']/li[2]")
                col_temp = data_col_obj.get_attribute("innerText")
                if col_temp == col_temp.upper():
                    self.upperOrLower = "upper"
                    log.info("表字段大写")
                else:
                    self.upperOrLower = "lower"
                    log.info("表字段小写")
                gbl.temp.set("UpperOrLower", self.upperOrLower)

                # 标签类型
                if tag_type == "公共标签":
                    tag_element = self.browser.find_element(
                        By.XPATH, "//*[@id='common_item']/li[@fieldchinesename='{0}']".format(tag_name))
                else:
                    # 字段标签转换大小写
                    if gbl.temp.get("UpperOrLower") == "upper":
                        tag_name = tag_name.upper()
                    else:
                        tag_name = tag_name.lower()
                    tag_element = self.browser.find_element(
                        By.XPATH, "//*[@id='field_item']/li[@fieldchinesename='{0}']".format(tag_name))
                filter_trigger = self.browser.find_element(By.XPATH, "//*[@id='editable_trigger']")
                action = ActionChains(self.browser)
                # 将标签拖到过滤条件框中
                action.drag_and_drop(tag_element, filter_trigger).perform()
                log.info("过滤条件加入标签【{0}】".format(tag_name))

                # 给标签设置属性
                if tag_type == "公共标签":
                    tag_elements = self.browser.find_elements(
                        By.XPATH, "//*[@id='editable_trigger']//*[contains(@id,'common_item_li') and @fieldchinesename='{0}']".format(
                            tag_name))
                else:
                    tag_elements = self.browser.find_elements(
                        By.XPATH, "//*[@id='editable_trigger']//*[contains(@id,'field_item_li') and @fieldchinesename='{0}']".format(
                            tag_name))
                if len(tag_elements) > 0:
                    # 选择匹配到的最后一个标签，表示最新加入的标签
                    element = tag_elements[-1]
                    element.click()
                    # 给标签设置属性值
                    if tag_attribute:
                        if tag_type == "公共标签":
                            if tag_name == "自定义过滤条件":
                                customize_sql = tag_attribute.get("自定义sql")
                                self.browser.find_element(
                                    By.XPATH, "//*[@id='where_customize_sql_value']").send_keys(customize_sql)
                        else:
                            logic_operator = tag_attribute.get("逻辑条件")
                            field_type = tag_attribute.get("字段类型")
                            tag_text_value = tag_attribute.get("字段值")
                            # 逻辑条件
                            if logic_operator:
                                self.browser.find_element(
                                    By.XPATH, "//*[@id='where_select_logic_operator']/following-sibling::div[1]//i").click()
                                sleep(1)
                                logic_ele = self.browser.find_element(
                                    By.XPATH, "//*[@id='where_select_logic_operator']/following-sibling::div[1]//dd[text()='{0}']".format(
                                        logic_operator))
                                action.move_to_element(logic_ele)
                                logic_ele.click()
                                log.info("设置逻辑条件: {0}".format(logic_operator))
                            # 字段类型，默认字符
                            if field_type == "数值":
                                input_text_ele = self.browser.find_element(
                                    By.XPATH, "//*[@id='where_item_number_single_value']")
                            else:
                                input_text_ele = self.browser.find_element(
                                    By.XPATH, "//*[@id='where_customer_tag_text_value']")
                            # 字段值
                            if tag_text_value:
                                input_text_ele.clear()
                                input_text_ele.send_keys(tag_text_value)
                                log.info("设置字符值: {0}".format(tag_text_value))
                        # 点击保存
                        self.browser.find_element(By.XPATH, "//*[@id='save_customer_tag_text']").click()
                else:
                    raise KeyError("标签【{0}】未加入到过滤条件，请检查")

        # 告警区域配置
        if alarm_area_config:
            editable_field = self.browser.find_element(By.XPATH, "//*[@id='editable_field']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", editable_field)
            # 先点击清空
            self.browser.find_element(By.XPATH, "//*[@id='delete_all_result_item']").click()
            for tag, tag_info in alarm_area_config.items():
                agg_function = tag_info.get("聚合函数")
                agg_result_name = tag_info.get("结果名称")
                agg_logic = tag_info.get("阈值条件")
                agg_threshold = tag_info.get("告警阈值")

                # 字段转换大小写
                if gbl.temp.get("UpperOrLower") == "upper":
                    tag = tag.upper()
                else:
                    tag = tag.lower()

                # 将字段标签拖入告警区域配置
                action = ActionChains(self.browser)
                # 将标签拖到过滤条件框中
                tag_element = self.browser.find_element(
                    By.XPATH, "//*[@id='alarm_rule_config_div']//*[contains(@id,'field_item') and @fieldchinesename='{0}']".format(
                        tag))
                alarm_area = self.browser.find_element(By.XPATH, "//*[@id='editable_field']")
                action.drag_and_drop(tag_element, alarm_area).perform()
                log.info("告警区域配置加入标签【{0}】".format(tag))

                # 点击字段标签
                tag_elements = self.browser.find_elements(
                    By.XPATH, "//*[@id='result_row_left']//*[contains(@id,'field_item') and @fieldchinesename='{0}']".format(
                        tag))
                if len(tag_elements) > 0:
                    # 选择匹配到的最后一个标签，表示最新加入的标签
                    element = tag_elements[-1]
                    element.click()
                    log.info("选择字段标签: {0}".format(tag))
                    # 聚合函数
                    if agg_function:
                        self.browser.find_element(
                            By.XPATH, "//*[@id='select_agg_function']/following-sibling::div[1]//i").click()
                        self.browser.find_element(
                            By.XPATH, "//*[@id='select_agg_function']/following-sibling::div[1]//dd[text()='{0}']".format(
                                agg_function)).click()
                        log.info("选择聚合函数: {0}".format(agg_function))
                    # 结果名称
                    if agg_result_name:
                        self.browser.find_element(By.XPATH, "//*[@id='input_agg_result_alias_name']").clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@id='input_agg_result_alias_name']").send_keys(agg_result_name)
                        log.info("设置结果名称: {0}".format(agg_result_name))
                    # 阈值条件
                    if agg_logic:
                        self.browser.find_element(
                            By.XPATH, "//*[@id='select_logic_operator']/following-sibling::div[1]//i").click()
                        self.browser.find_element(
                            By.XPATH, "//*[@id='select_logic_operator']/following-sibling::div[1]//dd[text()='{0}']".format(
                                agg_logic)).click()
                        log.info("设置阈值条件: {0}".format(agg_logic))
                    # 告警阈值
                    if agg_threshold:
                        self.browser.find_element(By.XPATH, "//*[@id='input_agg_threshold']").clear()
                        self.browser.find_element(By.XPATH, "//*[@id='input_agg_threshold']").send_keys(agg_threshold)
                        log.info("设置告警阈值: {0}".format(agg_threshold))
                    # 点击保存
                    self.browser.find_element(By.XPATH, "//*[@id='result_agg_save']").click()
                else:
                    raise KeyError("标签【{0}】未加入到告警区域配置，请检查")

        # 配置预览
        if view_config == "是":
            view_config_button = self.browser.find_element(By.XPATH, "//*[@id='view_config_sql_text']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", view_config_button)
            view_config_button.click()
            log.info("点击配置预览")
            page_wait(10)
            sleep(3)
            # 获取sql内容
            view_sql_area = self.browser.find_element(By.XPATH, "//*[@id='rule_sql_view']")
            view_sql = view_sql_area.get_attribute("value")
            log.info("获取sql预览内容: \n{0}".format(view_sql))

        # 规则测试
        if test_config == "是":
            test_button = self.browser.find_element(By.XPATH, "//*[@id='test_config_sql']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", test_button)
            test_button.click()
            log.info("点击规则测试")
            page_wait(10)
            sleep(3)
            # 获取测试结果数据
            log.info("获取规则测试结果")
            table_xpath = "//*[@id='selectedFieldTable']/following-sibling::div/"
            get_table_data2(table_xpath=table_xpath, return_column=True)

    def result_config(self, result_field):
        """
        :param result_field: 告警字段英文名，数组
        """
        # 告警字段英文名
        if result_field:
            for field in result_field:

                # 字段转换大小写
                if gbl.temp.get("UpperOrLower") == "upper":
                    field = field.upper()
                else:
                    field = field.lower()

                # 根据字段名获取行号
                field_row = self.browser.find_element(By.XPATH, "//*[@data-content='{0}']/..".format(field))
                data_index = field_row.get_attribute("data-index")
                if data_index is not None:
                    data_index = int(data_index)
                else:
                    raise AttributeError("列表不存在字段【{0}】".format(field))
                # 判断指定行的复选框是否勾选
                data_checkbox = self.browser.find_element(
                    By.XPATH, "//*[@class='layui-table-body']//*[@data-index='{0}']/td/div/div".format(data_index))
                checked = data_checkbox.get_attribute("class")
                if checked.find("checked") > -1:
                    checked = True
                else:
                    checked = False
                # 如果未勾选，则勾选
                if not checked:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='layui-table-body']//*[@data-index='{0}']/td/div/div/i".format(
                            data_index)).click()
                log.info("勾选字段: {0}".format(field))

    def storage_config(self, config_ftp, config_table):
        """
        :param config_ftp: FTP存储
        :param config_table: 数据库存储

        {
            "FTP存储": {
                "状态": "打开",
                "FTP名称": "",
                "存储目录": "",
                "文件名称": "",
                "文件类型": "",
                "时间单位": "",
                "保存间隔": "",
                "保存方式": ""
            },
            "数据库存储": {
                "状态": "打开",
                "选择数据库": "",
                "选择表": "",
                "字段映射": [
                    ["netunit_name", "col_1"],
                    ["col_2", "col_2"]
                ]
            }
        }
        """
        # FTP存储
        if config_ftp:
            # 获取开关状态
            ftp_open_button = self.browser.find_element(
                By.XPATH, "//*[@id='rule_output_ftp_switch_id']/following-sibling::div")
            open_status = ftp_open_button.get_attribute("innerText")
            if open_status == "ON" or open_status == "打开":
                open_status = "打开"
            else:
                open_status = "关闭"

            # 状态
            if config_ftp.__contains__("状态"):
                status = config_ftp.get("状态")
                if open_status != status:
                    ftp_open_button.click()
                log.info("【FTP存储】开关设为: {0}".format(status))
                sleep(1)

            # FTP名称
            if config_ftp.__contains__("FTP名称"):
                ftp_name = config_ftp.get("FTP名称")
                self.browser.find_element(By.XPATH, "//*[@id='select_output_ftp_name']/following-sibling::div//i").click()
                ftp_name_ele = self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_name']/following-sibling::div[1]//dd[text()='{0}']".format(ftp_name))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", ftp_name_ele)
                ftp_name_ele.click()
                log.info("选择FTP: {0}".format(ftp_name))

            # 存储目录
            if config_ftp.__contains__("存储目录"):
                save_dir = config_ftp.get("存储目录")
                self.browser.find_element(By.XPATH, "//*[@id='select_output_ftp_save_directory']").clear()
                self.browser.find_element(By.XPATH, "//*[@id='select_output_ftp_save_directory']").send_keys(save_dir)
                log.info("设置存储目录: {0}".format(save_dir))

            # 文件名称
            if config_ftp.__contains__("文件名称"):
                ftp_file_name = config_ftp.get("文件名称")
                self.browser.find_element(By.XPATH, "//*[@id='select_output_ftp_file_name']").clear()
                self.browser.find_element(By.XPATH, "//*[@id='select_output_ftp_file_name']").send_keys(ftp_file_name)
                log.info("设置文件名称: {0}".format(ftp_file_name))

            # 文件类型
            if config_ftp.__contains__("文件类型"):
                ftp_file_type = config_ftp.get("文件类型")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_file_type']/following-sibling::div//i").click()
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_file_type']/following-sibling::div[1]//dd[text()='{0}']".format(
                        ftp_file_type)).click()
                log.info("选择文件类型: {0}".format(ftp_file_type))

            # 时间单位
            if config_ftp.__contains__("时间单位"):
                time_unit = config_ftp.get("时间单位")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_time_unit']/following-sibling::div//i").click()
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_time_unit']/following-sibling::div[1]//dd[text()='{0}']".format(
                        time_unit)).click()
                log.info("选择时间单位: {0}".format(time_unit))

            # 保存间隔
            if config_ftp.__contains__("保存间隔"):
                interval = config_ftp.get("保存间隔")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_interval']/following-sibling::div//i").click()
                interval_ele = self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_interval']/following-sibling::div[1]//dd[text()='{0}']".format(
                        interval))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", interval_ele)
                interval_ele.click()
                log.info("选择保存间隔: {0}".format(interval))

            # 保存方式
            if config_ftp.__contains__("保存方式"):
                save_type = config_ftp.get("保存方式")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_type']/following-sibling::div//i").click()
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_ftp_save_type']/following-sibling::div[1]//dd[text()='{0}']".format(
                        save_type)).click()
                log.info("选择保存方式: {0}".format(save_type))

        # 数据库存储
        if config_table:
            # 获取开关状态
            table_open_button = self.browser.find_element(
                By.XPATH, "//*[@id='rule_output_table_switch_id']/following-sibling::div")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", table_open_button)
            open_status = table_open_button.get_attribute("innerText")
            if open_status == "ON" or open_status == "打开":
                open_status = "打开"
            else:
                open_status = "关闭"
            # 状态
            if config_table.__contains__("状态"):
                status = config_table.get("状态")
                if open_status != status:
                    table_open_button.click()
                log.info("【数据库存储】开关设为: {0}".format(status))
                sleep(1)

            # 选择数据库
            if config_table.__contains__("选择数据库"):
                database_name = config_table.get("选择数据库")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_databbase']/following-sibling::div//i").click()
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@id='select_output_databbase']/following-sibling::div[1]//dd[text()='{0}']".format(
                        database_name))))
                database_ele = self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_databbase']/following-sibling::div[1]//dd[text()='{0}']".format(
                        database_name))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", database_ele)
                database_ele.click()
                log.info("选择数据库: {0}".format(database_name))

            # 选择表
            if config_table.__contains__("选择表"):
                table_name = config_table.get("选择表")
                self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_database_table']/following-sibling::div//i").click()
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@id='select_output_database_table']/following-sibling::div[1]//dd[text()='{0}']".format(
                        table_name))))
                table_ele = self.browser.find_element(
                    By.XPATH, "//*[@id='select_output_database_table']/following-sibling::div[1]//dd[text()='{0}']".format(
                        table_name))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", table_ele)
                table_ele.click()
                log.info("选择表: {0}".format(table_name))
                sleep(1)

            # 字段映射
            if config_table.__contains__("字段映射"):
                field_map = config_table.get("字段映射")
                for field_rela in field_map:
                    field_name = field_rela[0]
                    output_field_name = field_rela[1]

                    # 字段转换大小写
                    if gbl.temp.get("UpperOrLower") == "upper":
                        field_name = field_name.upper()
                    else:
                        field_name = field_name.lower()

                    # 点击操作
                    self.browser.find_element(
                        By.XPATH, "//*[text()='{0}']/../following-sibling::td[3]//a".format(field_name)).click()
                    wait = WebDriverWait(self.browser, 3)
                    wait.until(ec.element_to_be_clickable((
                        By.XPATH, "//*[@id='output_field_radio_group']//*[contains(text(),'{0} (')]".format(
                            output_field_name))))
                    sleep(1)
                    # 选择映射的输出字段
                    self.browser.find_element(
                        By.XPATH, "//*[@id='output_field_radio_group']//*[contains(text(),'{0}')]".format(
                            output_field_name)).click()
                    sleep(1)
                    # 确认
                    self.browser.find_element(By.XPATH, "//*[text()='确认']").click()
                    log.info("将【{0}】映射到【{1}】".format(field_name, output_field_name))
                    sleep(1)

    def _get_current_status(self):
        """
        获取当前状态，需要先点击该行
        :return: True/False
        """
        # 先获取所有告警规则行对象，抽取node-id组成数组
        rule_elements = self.browser.find_elements(
            By.XPATH, "//tr[contains(@id,'dg_datagrid-row-r') and not(contains(@id,'plan'))]")
        rule_node_ids = [element.get_attribute("node-id") for element in rule_elements]
        try:
            # 判断当前选中行的node-id是在第几行，从而判断状态开关
            rule = self.browser.find_element(
                By.XPATH, "//tr[contains(@class,'selected')]")
            node_id = rule.get_attribute("node-id")
            i = None
            for i in range(len(rule_node_ids)):
                if node_id == rule_node_ids[i]:
                    break
            js = 'return $(".easyui-switchbutton")[{0}].checked;'.format(i)
            current_status = self.browser.execute_script(js)
        except NoSuchElementException:
            log.warning("请点击一行告警规则")
            current_status = False
        return current_status

    def update_status(self, rule_name, set_status, research=True):
        """
        :param rule_name: 告警规则名称
        :param set_status: 状态，启用/禁用
        :param research: 是否重新查询，默认true
        """
        if research:
            self.search(query={"告警规则名称": rule_name}, need_choose=True)

        # 获取当前状态
        js = 'return $(".easyui-switchbutton")[0].checked;'
        current_status = self.browser.execute_script(js)
        log.info("【状态】勾选状态: {0}".format(current_status))

        temp = True if set_status == "启用" else False
        if temp ^ current_status:
            self.browser.find_element(
                By.XPATH, "//*[text()='{0}']/../../../following-sibling::td[2]/div/span".format(rule_name)).click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确认启用{0}吗|确认禁用{0}吗".format(rule_name), auto_click_ok=False):
                alert.click_ok()
                sleep(1)
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("操作成功"):
                    log.info("{0} {1}成功".format(rule_name, set_status))
                else:
                    log.warning("{0} {1}失败，失败提示: {2}".format(rule_name, set_status, msg))
            else:
                log.warning("{0} {1}失败，失败提示: {2}".format(rule_name, set_status, msg))
            gbl.temp.set("ResultMsg", msg)

    def batch_enable(self, query):
        """
        # 批量将查询后的数据启用
        :param query: 查询条件
        """
        self.search(query=query, need_choose=False)
        table_xpath = "//*[@id='tb']/following-sibling::div[2]/table"
        p = Pagination(table_xpath)
        p.set_page_size(size=50)
        row_status = self.browser.find_elements(By.XPATH, "//*[@funcid='AlarmPlatform_rule_active']/following-sibling::span")
        if len(row_status) > 0:
            num = 0
            enable_success_flag = True  # 更新是否成功标识
            while enable_success_flag:
                element = row_status[num]
                js = 'return $(".easyui-switchbutton")[{0}].checked;'.format(num)
                current_status = self.browser.execute_script(js)
                if current_status:
                    gbl.temp.set("ResultMsg", "操作成功")
                    if num == len(row_status)-1:
                        break
                    else:
                        num += 1
                else:
                    action = ActionChains(self.browser)
                    action.move_to_element(element).click().perform()
                    alert = BeAlertBox(timeout=3, back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("确认启用", auto_click_ok=False):
                        alert.click_ok()
                        sleep(1)
                        alert = BeAlertBox(timeout=30, back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("操作成功"):
                            # 更新状态成功后，会将该条记录置于列表顶部（更新了修改时间）
                            num = 0
                            sleep(1)
                            # 如果查询条件包含了状态，更新成功后会自动刷新页面，需要重新获取
                            row_status = self.browser.find_elements(
                                By.XPATH, "//*[@funcid='AlarmPlatform_rule_active']/following-sibling::span")
                            if len(row_status) == 0:
                                break
                            sleep(1)
                        else:
                            log.warning("第{0}行启用失败，失败提示: {1}".format(num+1, msg))
                            break
                    else:
                        log.warning("第{0}行启用失败，失败提示: {1}".format(num+1, msg))
                        break
                    gbl.temp.set("ResultMsg", msg)
        else:
            raise Exception("未查询到记录")

    def batch_disable(self, query):
        """
        # 批量将查询后的数据禁用
        :param query: 查询条件
        """
        self.search(query=query, need_choose=False)
        table_xpath = "//*[@id='tb']/following-sibling::div[2]/table"
        p = Pagination(table_xpath)
        p.set_page_size(size=50)
        row_status = self.browser.find_elements(By.XPATH, "//*[@funcid='AlarmPlatform_rule_active']/following-sibling::span")
        if len(row_status) > 0:
            num = 0
            enable_success_flag = True  # 更新是否成功标识
            while enable_success_flag:
                element = row_status[num]
                js = 'return $(".easyui-switchbutton")[{0}].checked;'.format(num)
                current_status = self.browser.execute_script(js)
                if not current_status:
                    gbl.temp.set("ResultMsg", "操作成功")
                    if num == len(row_status)-1:
                        break
                    else:
                        num += 1
                else:
                    action = ActionChains(self.browser)
                    action.move_to_element(element).click().perform()
                    alert = BeAlertBox(timeout=3, back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("确认禁用", auto_click_ok=False):
                        alert.click_ok()
                        sleep(1)
                        alert = BeAlertBox(timeout=30, back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("操作成功"):
                            # 更新状态成功后，会将该条记录置于列表顶部（更新了修改时间）
                            num = 0
                            sleep(1)
                            # 如果查询条件包含了状态，更新成功后会自动刷新页面，需要重新获取
                            row_status = self.browser.find_elements(
                                By.XPATH, "//*[@funcid='AlarmPlatform_rule_active']/following-sibling::span")
                            if len(row_status) == 0:
                                break
                            sleep(1)
                        else:
                            log.warning("第{0}行禁用失败，失败提示: {1}".format(num+1, msg))
                            break
                    else:
                        log.warning("第{0}行禁用失败，失败提示: {1}".format(num+1, msg))
                        break
                    gbl.temp.set("ResultMsg", msg)
        else:
            raise Exception("未查询到记录")

    def delete(self, rule_name):
        """
        :param rule_name: 告警规则名称
        """
        self.search(query={"告警规则名称": rule_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(rule_name, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(rule_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(rule_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(rule_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def redo(self, rule_name, start_time=None, end_time=None):
        """
        :param rule_name: 告警规则名称
        :param start_time: 开始时间
        :param end_time: 结束时间
        """
        self.search(query={"告警规则名称": rule_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='redoBtn']").click()
        log.info("重调告警规则: {0}".format(rule_name))
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
        self.browser.find_element(By.XPATH, "//*[@class='form_row']//*[contains(@class,'save-btn')]").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 重调成功".format(rule_name))
        else:
            log.warning("{0} 重调失败，失败提示: {1}".format(rule_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, rule_name, fuzzy_match=False):
        """
        :param rule_name: 告警规则名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"告警规则名称": rule_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='alarmRuleName']//*[starts-with(text(),'{0}')]".format(rule_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='alarmRuleName']//*[text()='{0}']".format(rule_name))
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
            if self._get_current_status():
                # 将规则禁用
                self.browser.find_element(
                    By.XPATH, "//*[text()='{0}']/../../../following-sibling::td[2]/div/span".format(search_result)).click()
                log.info("禁用告警规则: {}".format(search_result))
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
                    By.XPATH, "//*[@field='alarmRuleName']//*[text()='{0}']".format(search_result)).click()
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除", auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("{0} 删除成功".format(search_result))
                    page_wait()
                    if fuzzy_match:
                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH, "//*[@field='alarmRuleName']//*[starts-with(text(),'{0}')]".format(rule_name))
                        if len(record_element) == 0:
                            # 查询结果为空,修改exist_data为False，退出循环
                            log.info("数据清理完成")
                            exist_data = False
                    else:
                        break
                else:
                    raise Exception("删除数据时出现未知异常: {0}".format(msg))
            else:
                log.warning("{0} 清理失败，失败提示: {1}".format(rule_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
