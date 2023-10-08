# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/8/23 下午2:49

import json
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.input import set_textarea
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho


class BlackList:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("指令配置-指令集黑名单")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/cmd/cmdBlacklist.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
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

        # 关键字
        if query.__contains__("关键字"):
            cmd_name = query.get("关键字")
            self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").send_keys(cmd_name)
            log.info("设置关键字: {0}".format(cmd_name))
            select_item = cmd_name

        # 厂家
        if query.__contains__("厂家"):
            vendor = query.get("厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            if isinstance(model, str):
                model = [model]
            for m in model:
                self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(m)).click()
                log.info("设置设备型号: {0}".format(model))

        # 启用状态
        if query.__contains__("启用状态"):
            alive = query.get("启用状态")
            self.browser.find_element(By.XPATH, "//*[@id='isAlive']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(alive)).click()
            log.info("设置启用状态: {0}".format(alive))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='blacklist-query']").click()
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
                        By.XPATH, "//*[@field='blackListStr']/*[text()='{}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, vendor, model, blacklist_str, remark):
        """
        :param vendor: 厂家
        :param model: 设备型号，数组
        :param blacklist_str: 黑名单内容
        :param remark: 备注

        {
            "操作": "",
            "参数": {
                "厂家": "",
                "设备型号": ["", ""],
                "黑名单内容": "--test",
                "备注": ""
            }
        }
        """
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='blacklist-add']")))
        self.browser.find_element(By.XPATH, "//*[@id='blacklist-add']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'addBlackList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='blacklistStr']")))

        self.blacklist_page(vendor, model, blacklist_str, remark)
        # 提交
        self.browser.find_element(By.XPATH, "//*[@onclick='submitForm();']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("添加指令集黑名单成功"):
            log.info("添加指令集黑名单成功")
        else:
            log.warning("添加指令集黑名单失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, query, vendor, model, blacklist_str, remark):
        """
        :param query: 查询条件
        :param vendor: 厂家
        :param model: 设备型号，数组
        :param blacklist_str: 黑名单内容
        :param remark: 备注

        {
            "操作": "UpdateCmdBlacklist",
            "参数": {
                "查询条件": {
                    "厂家": "图科",
                    "设备型号": ["TKea"],
                    "关键字": "auto_bl_test",
                },
                "修改内容": {
                    "厂家": "图科",
                    "设备型号": ["TKea"],
                    "黑名单内容": ["auto_bl_test"],
                    "备注": "指令集黑名单"
                }
            }
        }
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='blacklist-edit']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'addBlackList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='blacklistStr']")))
        sleep(1)

        self.blacklist_page(vendor, model, blacklist_str, remark)
        # 提交
        self.browser.find_element(By.XPATH, "//*[@onclick='submitForm();']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("修改黑名单信息成功"):
            log.info("修改黑名单信息成功")
        else:
            log.warning("修改黑名单信息失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def blacklist_page(self, vendor, model, blacklist_str, remark):
        """
        :param vendor: 厂家
        :param model: 设备型号，数组
        :param blacklist_str: 黑名单内容
        :param remark: 备注
        """
        page_wait()
        sleep(1)
        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='addVendor']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.element_to_be_clickable((By.XPATH, panel_xpath + "//*[text()='{0}']".format(vendor))))
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))
            sleep(1)

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='addNetunitModel']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            sleep(1)
            # 先取消勾选
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.element_to_be_clickable((By.XPATH, panel_xpath + "//*[contains(@class,'checkAll')]")))
            selected_model = self.browser.find_elements(By.XPATH, panel_xpath + "//*[contains(@class,'selected')]")
            if len(selected_model) > 0:
                for m in selected_model:
                    m.click()
            # 重新选择
            if model != "全选":
                for m in model:
                    self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(m)).click()
                    log.info("设置设备型号: {0}".format(m))
            else:
                self.browser.find_element(By.XPATH, panel_xpath + "//*[contains(@class,'checkAll')]").click()
                log.info("设置设备型号: 全选")
            # 收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='addNetunitModel']/following-sibling::span//a").click()

        # 黑名单内容
        if blacklist_str:
            textarea = self.browser.find_element(By.XPATH, "//*[@id='blacklistStr']")
            set_textarea(textarea=textarea, msg=blacklist_str)
            log.info("设置黑名单内容: {0}".format('\n'.join(blacklist_str)))

        # 备注
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='remark']").clear()
            self.browser.find_element(By.XPATH, "//*[@id='remark']").send_keys(remark)
            log.info("设置备注: {0}".format(remark))

    def set_status(self, query, status, research=True):
        """
        :param query: 查询条件
        :param status: 状态，启用/禁用
        :param research: 是否查询
        """
        if research:
            self.search(query=query, need_choose=True)
        blacklist = query.get("关键字")
        js = 'return $(".switchbutton")[0].checked;'
        current_status = self.browser.execute_script(js)
        temp = True if status == "启用" else False
        if temp ^ current_status:
            self.browser.find_element(
                By.XPATH,
                "//*[@field='blackListStr']/*[text()='{}']/../preceding-sibling::td[1]//*[@class='switchbutton']".format(
                    blacklist)).click()
            log.info("{0}指令集黑名单: {1}".format(status, blacklist))

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("启用黑名单成功"):
                # 启用指令集黑名单成功
                log.info("启用指令集黑名单成功")
            elif alert.title_contains("禁用黑名单成功"):
                log.info("禁用指令集黑名单成功")
            else:
                log.warning("{0}指令集黑名单失败，失败原因: {1}".format(status, msg))
        else:
            log.info("指令集黑名单【{0}】状态已经是{1}".format(blacklist, status))
            msg = "{0}黑名单成功".format(status)
        gbl.temp.set("ResultMsg", msg)

    def delete(self, query):
        """
        :param query: 查询条件
        """
        self.search(query=query, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='blacklist-del']").click()
        blacklist = query.get("关键字")
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{}吗".format(blacklist), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("删除黑名单信息成功"):
                log.info("{0} 删除成功".format(blacklist))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(blacklist, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(blacklist, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, blacklist, fuzzy_match=False):
        """
        :param blacklist: 黑名单内容
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"关键字": blacklist}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='blackListStr']//*[starts-with(text(),'{}')]".format(blacklist))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='blackListStr']//*[@text()='{0}']".format(blacklist))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            js = 'return $(".blacklistTab_datagrid-cell-c1-blackListStr")[1].innerHTML;'
            search_result = self.browser.execute_script(js)
            pe.click()
            log.info("选择: {0}".format(search_result))
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='blacklist-del']").click()
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
                            By.XPATH, "//*[@field='blackListStr']//*[starts-with(text(),'{}')]".format(blacklist))
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
                log.warning("{0} 删除失败，失败提示: {1}".format(blacklist, msg))
                gbl.temp.set("ResultMsg", msg)
                break
