# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:01

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class ProfessionField:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("常用信息管理-专业领域管理")
        self.browser.switch_to.frame(
            self.browser.find_element(
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/templetManageInfo.html')]"))
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

        # 专业领域名称
        if query.__contains__("专业领域名称"):
            temp_name = query.get("专业领域名称")
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeName']/following-sibling::span/input[1]").send_keys(
                temp_name)
            select_item = temp_name

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
                        By.XPATH, "//*[@field='tempTypeName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, field_name):
        """
        :param field_name: 专业领域名称
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'addTempletManageInfo.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='tempTypeNameInfo']/preceding-sibling::input")))

        # 专业领域名称
        if field_name:
            self.browser.find_element(
                By.XPATH, "//*[@name='tempTypeNameInfo']/preceding-sibling::input").send_keys(field_name)
            log.info("设置专业领域名称: {0}".format(field_name))

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']//*[text()='保存']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(field_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(field_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, field, field_name):
        """
        :param field: 专业领域名称
        :param field_name: 专业领域名称
        """
        log.info("开始修改数据")
        self.search(query={"专业领域名称": field}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'addTempletManageInfo.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='tempTypeNameInfo']/preceding-sibling::input")))

            # 专业领域名称
            if field_name:
                self.browser.find_element(By.XPATH, "//*[@name='tempTypeNameInfo']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='tempTypeNameInfo']/preceding-sibling::input").send_keys(field_name)
                log.info("设置专业领域名称: {0}".format(field_name))

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']//*[text()='保存']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 修改成功".format(field))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(field, msg))
            gbl.temp.set("ResultMsg", msg)

    def delete(self, field_name):
        """
        :param field_name: 专业领域名称
        """
        log.info("开始删除数据")
        self.search(query={"专业领域名称": field_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(field_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(field_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(field_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(field_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, field_name, fuzzy_match=False):
        """
        :param field_name: 专业领域名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"专业领域名称": field_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tempTypeName']//*[starts-with(text(),'{0}')]".format(field_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tempTypeName']//*[text()='{0}']".format(field_name))
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
            # 删除
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
                            By.XPATH, "//*[@field='tempTypeName']//*[starts-with(text(),'{0}')]".format(field_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(field_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
