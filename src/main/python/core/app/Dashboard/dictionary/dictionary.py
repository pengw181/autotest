# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/4/25 下午3:10

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from src.main.python.lib.toast import Toast
from src.main.python.lib.input import set_textarea
from src.main.python.lib.loadDictionary import load_dictionary
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.wrap import Wrap
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


@Wrap(wrap_func='close_enter_dashboard')
class Dictionary:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        page_wait(5)
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='字典管理']")))
        self.browser.find_element(By.XPATH, "//*[text()='字典管理']").click()
        log.info("切换到字典管理页面")
        sleep(1)

    def add(self, dict_list):
        """
        :param dict_list: 字典配置，列表
        """
        # 点击添加
        self.browser.find_element(By.XPATH, "//*[@title='添加字典']").click()
        log.info("添加字典")
        num = self.browser.find_element(
            By.XPATH, "//*[@class='datagrid-view1']//*[contains(@id,'dictionaryTab') and contains(@class,'selected')]/td/div").text
        num = int(num)
        for dictionary in dict_list:
            if not isinstance(dictionary, dict):
                raise TypeError("单条字典信息需要字典格式")
            dict_name = dictionary.get("字典名称")
            catalog = dictionary.get("主题分类")
            interface = dictionary.get("数据接口")
            dict_item = dictionary.get("字典项")
            save_success = False
            row_xpath = "//*[contains(@id,'dictionaryTab')][{0}]".format(num)
            sleep(1)

            self.dict_page(dict_name, catalog, interface, dict_item, row_xpath)

            # 保存
            self.browser.find_element(By.XPATH, "//*[@title='保存字典']").click()
            alert = BeAlertBox(timeout=5, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("确定保存字典【{0}】吗".format(dict_name), auto_click_ok=False):
                alert.click_ok()
                toast = Toast()
                msg = toast.get_msg()
                if toast.msg_contains("保存成功"):
                    save_success = True
                    log.info("保存字典【{0}】成功".format(dict_name))
                else:
                    log.warning("保存字典失败，失败提示: {0}".format(msg))
                toast.waitUntil()
                gbl.temp.set("ResultMsg", msg)
            else:
                log.warning("保存字典失败，失败提示: {0}".format(msg))
                gbl.temp.set("ResultMsg", msg)
            if save_success:
                num += 1
                if dictionary != dict_list[-1]:
                    # 点击添加
                    self.browser.find_element(By.XPATH, "//*[@title='添加字典']").click()
            else:
                break

    def update(self, dict_name, dictionary):
        """
        :param dict_name: 字典名
        :param dictionary: 字典配置，字典
        :return:
        """
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").send_keys(dict_name)
        log.info("字典名称输入: {0}".format(dict_name))
        self.browser.find_element(By.XPATH, "//*[@title='查询字典']").click()
        page_wait(3)
        log.info("编辑字典")
        action = ActionChains(self.browser)
        element = self.browser.find_element(By.XPATH, "//*[@field='dictName']//div[text()='{0}']".format(dict_name))
        row = self.browser.find_element(By.XPATH, "//*[@field='dictName']/*[text()='{0}']/../..".format(dict_name))
        row_index = row.get_attribute("datagrid-row-index")
        num = int(row_index) + 1
        row_xpath = "//*[contains(@id,'dictionaryTab')][{0}]".format(num)
        action.double_click(element).perform()
        if not isinstance(dictionary, dict):
            raise TypeError("字典配置需要字典格式")
        dict_name = dictionary.get("字典名称")
        catalog = dictionary.get("主题分类")
        interface = dictionary.get("数据接口")
        dict_item = dictionary.get("字典项")
        self.dict_page(dict_name, catalog, interface, dict_item, row_xpath)
        # 保存
        self.browser.find_element(By.XPATH, "//*[@title='保存字典']").click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("确定保存字典【{0}】吗".format(dict_name), auto_click_ok=False):
            alert.click_ok()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("保存成功"):
                log.info("保存字典【{0}】成功".format(dict_name))
                toast.waitUntil()
            else:
                log.warning("保存字典失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            log.warning("保存字典失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

    def dict_page(self, dict_name, catalog, interface, dict_item, row_xpath):
        """
        :param dict_name: 字典名称
        :param catalog: 主题分类
        :param interface: 数据接口
        :param dict_item: 字典项
        :param row_xpath: 行xpath
        """
        # 字典名称
        if dict_name:
            self.browser.find_element(By.XPATH, row_xpath + "/td[2]//input[contains(@id,'textbox')]").clear()
            self.browser.find_element(
                By.XPATH, row_xpath + "/td[2]//input[contains(@id,'textbox')]").send_keys(dict_name)
            log.info("设置字典名称: {0}".format(dict_name))

        # 主题分类
        if catalog:
            self.browser.find_element(By.XPATH, row_xpath + "/td[3]//a").click()
            sleep(1)
            catalog_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(catalog))
            if len(catalog_elements) == 0:
                raise NoSuchElementException("找不到主题分类: {0}".format(catalog))
            for element in catalog_elements:
                if element.is_displayed():
                    element.click()
                    log.info("设置主题分类: {0}".format(catalog))
                    sleep(1)
                    break

        # 数据接口
        if interface:
            self.browser.find_element(By.XPATH, row_xpath + "/td[4]//a").click()
            sleep(1)
            interface_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(interface))
            if len(interface_elements) == 0:
                raise NoSuchElementException("找不到数据接口: {0}".format(interface))
            for element in interface_elements:
                if element.is_displayed():
                    element.click()
                    log.info("设置数据接口: {0}".format(interface))
                    sleep(1)
                    break

        # 字典项
        if dict_item:
            textarea = self.browser.find_element(By.XPATH, "//*[@id='dictionaryText']")
            if isinstance(dict_item, str):
                # 文件名
                content = load_dictionary(dict_item)
            else:
                # 数组
                content = dict_item
            set_textarea(textarea=textarea, msg=content)
            sleep(1)

    def delete(self, dict_name):
        """
        :param dict_name: 字典名
        """
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").send_keys(dict_name)
        self.browser.find_element(By.XPATH, "//*[@title='查询字典']").click()
        page_wait(3)

        self.browser.find_element(By.XPATH, "//*[@field='dictName']//div[text()='{0}']".format(dict_name)).click()
        # 点击删除
        self.browser.find_element(By.XPATH, "//*[@title='删除字典']").click()
        log.info("删除字典")
        alert = BeAlertBox(timeout=3, back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(dict_name), auto_click_ok=False):
            alert.click_ok()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("删除成功"):
                log.info("删除字典图【{0}】成功".format(dict_name))
            else:
                log.info("删字典【{0}】失败，失败原因: {1}".format(dict_name, msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            log.error("删除字典【{0}】失败，失败原因{1}".format(dict_name, msg))
            gbl.temp.set("ResultMsg", msg)

    def clear_dict(self, dict_name, fuzzy_match=False):
        """
        :param dict_name: 字典名，关键字
        :param fuzzy_match: 模糊匹配
        """
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='dictName']/following-sibling::span/input[1]").send_keys(dict_name)
        self.browser.find_element(By.XPATH, "//*[@title='查询字典']").click()
        page_wait(3)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dictName']//div[starts-with(text(),'{0}')]".format(dict_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='dictName']//div[text()='{0}']".format(dict_name))
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
            # 点击删除
            self.browser.find_element(By.XPATH, "//*[@title='删除字典']").click()
            alert = BeAlertBox(timeout=1, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                toast = Toast()
                if toast.exist:
                    msg = toast.get_msg()
                    if not toast.msg_contains("删除成功"):
                        log.info("删除字典失败，失败原因: {0}".format(msg))
                        gbl.temp.set("ResultMsg", msg)
                        break

                    log.info("{0} {1}".format(search_result, msg))
                    toast.waitUntil()
                    if not fuzzy_match:
                        break

                    # 重新获取页面查询结果
                    record_element = self.browser.find_elements(
                        By.XPATH,
                        "//*[@field='dictName']//div[starts-with(text(),'{0}')]".format(dict_name))
                    if len(record_element) > 0:
                        exist_data = True
                    else:
                        # 查询结果为空,修改exist_data为False，退出循环
                        log.info("数据清理完成")
                        exist_data = False
            else:
                # 无权操作
                log.warning("清理失败，失败提示: {0}".format(msg))
                gbl.temp.set("ResultMsg", msg)
                break
