# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:06

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_textarea
from client.page.func.positionPanel import getPanelXpath
from client.page.statics.AlarmPlatform.chooseMenu import choose_menu
from client.page.func.alertBox import BeAlertBox
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


class Dictionary:

    def __init__(self):
        self.browser = get_global_var("browser")
        self.upperOrLower = None
        # 进入菜单
        choose_menu("告警配置-字典配置")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/dataConfig/dictionary/dictGroupList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='dictGroupName']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def choose(self, dict_name):
        """
        :param dict_name: 字典名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@name='dictGroupName']/preceding-sibling::input")
        input_ele.clear()
        input_ele.send_keys(dict_name)
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_dict_query']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='dictGroupName']//a[text()='{}']".format(dict_name)).click()
        log.info("已选择字典: {}".format(dict_name))

    def add(self, dict_name, comment, dict_type, table_belong, item_key, item_value, filter_set):
        """
        :param dict_name: 字典组名称
        :param comment: 字典描述
        :param dict_type: 字典类型
        :param table_belong: 字典表名称
        :param item_key: 关键字
        :param item_value: 值
        :param filter_set: 过滤条件
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/addDictGroup.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='dictGroupName']/following-sibling::span/input[1]")))
        sleep(1)
        self.dict_page(dict_name, comment, dict_type, table_belong, item_key, item_value, filter_set)

        # 点击保存
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_dict_save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(dict_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(dict_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, dict_name, comment, filter_set):
        """
        :param obj: 字典组名称
        :param dict_name: 字典组名称
        :param comment: 字典描述
        :param filter_set: 过滤条件
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/addDictGroup.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='dictGroupName']/following-sibling::span/input[1]")))

        self.dict_page(dict_name, comment, None, None, None, None, filter_set)

        # 点击保存
        self.browser.find_element(By.XPATH, "//*[@funcid='AlarmPlatform_dict_save']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 修改成功".format(obj))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def dict_page(self, dict_name, comment, dict_type, table_belong, item_key, item_value, filter_set):
        """
        :param dict_name: 字典组名称
        :param comment: 字典描述
        :param dict_type: 字典类型
        :param table_belong: 字典表名称
        :param item_key: 关键字
        :param item_value: 值
        :param filter_set: 过滤条件

        # 过滤条件
        {
            "操作": "添加",
            "条件": [
                {
                    "过虑字段": "",
                    "操作关系": "",
                    "比较值": "",
                    "值类型": ""
                },
                {
                    "过虑字段": "",
                    "操作关系": "",
                    "比较值": "",
                    "值类型": ""
                }
            ]
        }

        {
            "操作": "修改",
            "序号": "1",
            "条件": {
                "过虑字段": "",
                "操作关系": "",
                "比较值": "",
                "值类型": ""
            }
        }

        {
            "操作": "删除",
            "序号": "1"
        }

        """
        # 字典组名称
        if dict_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='dictGroupName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='dictGroupName']/following-sibling::span/input[1]").send_keys(dict_name)
            log.info("设置字典组名称: {0}".format(dict_name))

        # 字典描述
        if comment:
            comment_textarea = self.browser.find_element(By.XPATH, "//*[@id='dictGroupComment']")
            set_textarea(textarea=comment_textarea, msg=comment)
            log.info("设置字典描述: {0}".format(comment))

        # 字典类型
        if dict_type:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='dictGroupType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'dictGroupType') and text()='{0}']".format(dict_type)).click()
            log.info("设置字典类型: {0}".format(dict_type))

        # 字典表名称
        if table_belong:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableBelongId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'tableBelongId') and text()='{0}']".format(table_belong)).click()
            log.info("设置字典表名称: {0}".format(table_belong))
            sleep(1)

        # 关键字
        if item_key:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='dictItemKeyCol']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'dictItemKeyCol') and text()='{0}']".format(item_key)).click()
            log.info("设置关键字: {0}".format(item_key))

        # 值
        if item_value:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='dictItemValCol']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'dictItemValCol') and text()='{0}']".format(item_value)).click()
            log.info("设置值: {0}".format(item_value))

        # 过滤条件
        if filter_set:
            action = filter_set.get("操作")
            if action == "添加":
                conditions = filter_set.get("条件")
                row_index = 0
                for condition in conditions:
                    field_name = condition.get("过虑字段")
                    operation = condition.get("操作关系")
                    value = condition.get("比较值")
                    field_type = condition.get("值类型")
                    self.browser.find_element(By.XPATH, "//*[@id='conditionDiv']//*[text()='添加']").click()
                    log.info("设置第{0}行过滤条件".format(row_index + 1))
                    sleep(1)

                    # 过虑字段
                    if field_name:
                        self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='fieldName']//a".format(
                                row_index)).click()
                        panel_xpath = getPanelXpath()
                        self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(field_name)).click()
                        log.info("设置过虑字段: {0}".format(field_name))

                    # 操作关系
                    if operation:
                        self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='opt']//a".format(
                                row_index)).click()
                        panel_xpath = getPanelXpath()
                        self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(operation)).click()
                        log.info("设置操作关系: {0}".format(operation))

                    # 比较值
                    if value:
                        self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='value']//input".format(
                                row_index)).clear()
                        self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='value']//input".format(
                                row_index)).send_keys(value)
                        log.info("设置比较值: {0}".format(value))

                    # 值类型
                    if field_type:
                        self.browser.find_element(
                            By.XPATH,
                            "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='fieldType']//a".format(
                                row_index)).click()
                        panel_xpath = getPanelXpath()
                        self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(field_type)).click()
                        log.info("设置值类型: {0}".format(field_type))

                    # 点击确定
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='ff']//*[contains(@id,'sureBtn')]".format(
                            row_index)).click()
                    row_index += 1
                    sleep(1)

            elif action == "修改":
                row_index = filter_set.get("序号")
                condition = filter_set.get("条件")
                field_name = condition.get("过虑字段")
                operation = condition.get("操作关系")
                value = condition.get("比较值")
                field_type = condition.get("值类型")
                row_index = int(row_index)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']/*[@field='ff']//*[contains(@id,'editBtn')]".format(
                        row_index - 1)).click()

                # 过虑字段
                if field_name:
                    self.browser.find_element(
                        By.XPATH,
                        "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='fieldName']//a".format(
                            row_index - 1)).click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(field_name)).click()
                    log.info("设置过虑字段: {0}".format(field_name))

                # 操作关系
                if operation:
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='opt']//a".format(
                            row_index - 1)).click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(operation)).click()
                    log.info("设置操作关系: {0}".format(operation))

                # 比较值
                if value:
                    self.browser.find_element(
                        By.XPATH,
                        "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='value']//input".format(
                            row_index - 1)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='value']//input".format(
                            row_index - 1)).send_keys(value)
                    log.info("设置比较值: {0}".format(value))

                # 值类型
                if field_type:
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='fieldType']//a".format(
                            row_index - 1)).click()
                    panel_xpath = getPanelXpath()
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(field_type)).click()
                    log.info("设置值类型: {0}".format(field_type))

                # 点击确定
                self.browser.find_element(
                    By.XPATH,
                    "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@field='ff']//*[contains(@id,'sureBtn')]".format(
                        row_index - 1)).click()

            else:
                row_index = filter_set.get("序号")
                row_index = int(row_index)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'condition') and @datagrid-row-index='{0}']//*[@class='datagrid-cell-rownumber' and text()='{1}']".format(
                        row_index - 1, row_index)).click()
                self.browser.find_element(By.XPATH, "//*[@id='conditionDiv']//a//*[text()='删除']").click()
                alert = BeAlertBox(timeout=1)
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除行{0}吗".format(row_index), auto_click_ok=False):
                    alert.click_ok()
                    log.info("条件 {0} 删除成功".format(row_index))
                    wait = WebDriverWait(self.browser, 10)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH,
                        "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/addDictGroup.html')]")))
                    sleep(1)
                else:
                    log.warning("条件 {0} 删除失败，失败提示: {1}".format(row_index, msg))
                    set_global_var("ResultMsg", msg, False)
                    return

    def set_dict_detail(self, dict_name, detail):
        """
        :param dict_name: 字典组名称
        :param detail: 字典明细

        # 字典明细
        {
            "操作": "添加",
            "键值对": [
                ["", ""],
                ["", ""]
            ]
        }

        {
            "操作": "编辑",
            "关键字": "",
            "键值对": ["", ""]
        }

        {
            "操作": "删除",
            "关键字": ""
        }


        """
        log.info("开始编辑字典明细")
        self.choose(dict_name)
        self.browser.find_element(By.XPATH, "//*[@id='editDictBtn']").click()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
            return

        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/dictDetail.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='dictItemKey']/following-sibling::span//input[1]")))

        # 字典明细
        if detail:
            action = detail.get("操作")

            if action == "添加":
                item_key_value = detail.get("键值对")
                for kv in item_key_value:
                    _key = kv[0]
                    _value = kv[1]
                    # 点击添加
                    self.browser.find_element(
                        By.XPATH, "//*[@id='dictGroupId']/following-sibling::div/*[@id='addBtn']").click()
                    # 输入关键字
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@class,'dictItemKey') and contains(@class,'datagrid-editable')]//input").send_keys(
                        _key)
                    # 输入值
                    self.browser.find_element(
                        By.XPATH,
                        "//*[contains(@class,'dictItemValue') and contains(@class,'datagrid-editable')]//input").send_keys(
                        _value)
                    # 点击确定
                    self.browser.find_element(
                        By.XPATH, "//*[@field='ff']//*[not(contains(@style,'display: none')) and text()='确定']").click()
                    alert = BeAlertBox(timeout=3)
                    msg = alert.get_msg()
                    if alert.title_contains("保存成功"):
                        log.info("关键字 {0} 保存成功".format(_key))
                        wait = WebDriverWait(self.browser, 10)
                        wait.until(ec.frame_to_be_available_and_switch_to_it((
                            By.XPATH,
                            "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/dictDetail.html')]")))
                        set_global_var("ResultMsg", msg, False)
                        sleep(1)
                    else:
                        log.warning("关键字 {0} 保存失败，失败提示: {1}".format(_key, msg))
                        set_global_var("ResultMsg", msg, False)
                        return

            elif action == "编辑":
                key = detail.get("关键字")
                item_key_value = detail.get("键值对")
                self.browser.find_element(
                    By.XPATH, "//*[@id='dictItemKey']/following-sibling::span//input[1]").send_keys(key)
                # 点击查询
                self.browser.find_element(
                    By.XPATH, "//*[@id='dictGroupId']/following-sibling::div//*[@id='btn']").click()
                sleep(1)
                # 点击编辑，如果多个关键字同名，取第一个
                self.browser.find_element(
                    By.XPATH, "//*[@field='dictItemKey']/div[text()='{0}']/../following-sibling::td[2]//*[@onclick='editThisRow(this,0)']".format(
                        key)).click()
                _key = item_key_value[0]
                _value = item_key_value[1]
                # 输入关键字
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class,'dictItemKey') and contains(@class,'datagrid-editable')]//input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class,'dictItemKey') and contains(@class,'datagrid-editable')]//input").send_keys(
                    _key)
                # 输入值
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class,'dictItemValue') and contains(@class,'datagrid-editable')]//input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class,'dictItemValue') and contains(@class,'datagrid-editable')]//input").send_keys(
                    _value)
                # 点击确定
                self.browser.find_element(
                    By.XPATH, "//*[@field='ff']//*[not(contains(@style,'display: none')) and text()='确定']").click()
                alert = BeAlertBox(timeout=3)
                msg = alert.get_msg()
                if alert.title_contains("保存成功"):
                    log.info("关键字 {0} 保存成功".format(key))
                else:
                    log.warning("关键字 {0} 保存失败，失败提示: {1}".format(key, msg))
                set_global_var("ResultMsg", msg, False)

            else:
                key = detail.get("关键字")
                self.browser.find_element(
                    By.XPATH, "//*[@id='dictItemKey']/following-sibling::span//input[1]").send_keys(key)
                # 点击查询
                self.browser.find_element(
                    By.XPATH, "//*[@id='dictGroupId']/following-sibling::div//*[@id='btn']").click()
                sleep(1)
                # 查到多个同名关键字，则全部删除
                key_elements = self.browser.find_elements(
                    By.XPATH, "//*[@field='dictItemKey']/*[text()='{0}']".format(key))
                keys_num = len(key_elements)
                if keys_num == 0:
                    raise KeyError("找不到关键字")
                if keys_num > 0:
                    log.info("找到{0}个关键字，将全部删除".format(keys_num))
                for element in key_elements:
                    element.click()
                    # 点击删除
                    self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
                    alert = BeAlertBox(timeout=3)
                    msg = alert.get_msg()
                    if alert.title_contains("您确定需要删除吗", auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(timeout=2, back_iframe=False)
                        if not alert.exist_alert:
                            log.info("关键字 {0} 删除成功".format(key))
                            msg = "删除成功"
                            wait = WebDriverWait(self.browser, 10)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/dictionary/dictDetail.html')]")))
                        else:
                            msg = alert.get_msg()
                            log.warning("关键字 {0} 删除失败，失败提示: {1}".format(key, msg))
                            set_global_var("ResultMsg", msg, False)
                            break
                    else:
                        log.warning("关键字 {0} 删除失败，失败提示: {1}".format(key, msg))
                    set_global_var("ResultMsg", msg, False)
