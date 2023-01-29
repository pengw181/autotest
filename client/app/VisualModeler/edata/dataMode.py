# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/21 下午4:02

from time import sleep
from selenium.webdriver.common.by import By
from client.page.func.pageMaskWait import page_wait
from client.page.func.input import set_textarea
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class DateModeEData:
    # 数据模式

    def __init__(self):
        self.browser = get_global_var("browser")

    def table_name_page(self, table_name, field, remark):
        """
        :param table_name: 数据表名称
        :param field: 专业领域
        :param remark: 备注
        """
        # 数据表名称
        if table_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(table_name)
            log.info("设置数据表名称: {0}".format(table_name))

        # 专业领域
        if field:
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            page_wait()
            sleep(1)
            # 判断当前是否已经选择了专业领域，如果是，则先取消
            choose_field_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'tempTypeId') and contains(@class,'selected')]")
            if len(choose_field_list) > 0:
                for cf in choose_field_list:
                    cf.click()
            # 依次选择专业领域
            for f in field:
                field_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'tempTypeId') and text()='{0}']".format(f))
                for element in field_elements:
                    if element.is_displayed():
                        element.click()
                        break
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 备注
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span/textarea")
            set_textarea(textarea=remark_textarea, msg=remark)
            log.info("设置备注: {0}".format(remark))
