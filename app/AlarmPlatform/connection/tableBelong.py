# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:08

from common.variable.globalVariable import *
from common.page.func.pageMaskWait import page_wait
from common.page.func.input import set_textarea
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.AlarmPlatform.main.menu.chooseMenu import choose_menu
from common.page.func.alertBox import BeAlertBox
from time import sleep
from common.log.logger import log


class TableBelong:

    def __init__(self):
        self.browser = get_global_var("browser")
        # 进入菜单
        choose_menu("连接配置-表归属配置")
        page_wait()
        # 切换iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'html/dataConfig/tableBelong/tableBelongList.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableName']/following-sibling::span[1]/input[1]")))
        page_wait()
        sleep(1)

    def choose(self, table_cn_name):
        """
        :param table_cn_name: 表中文名称
        """
        input_ele = self.browser.find_element(By.XPATH, "//*[@id='tableName']/following-sibling::span[1]/input[1]")
        input_ele.clear()
        input_ele.send_keys(table_cn_name)
        self.browser.find_element(By.XPATH, "//span[text()='查询']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@field='tableNameCh']//a[text()='{}']".format(table_cn_name)).click()
        log.info("已选择表: {}".format(table_cn_name))

    def add(self, database_name, table_en_ame, table_cn_Name, table_object, table_period, remark):
        """
        :param database_name: 数据库名称
        :param table_en_ame: 表英文名称
        :param table_cn_Name: 表中文名称
        :param table_object: 表使用对象
        :param table_period: 表周期
        :param remark: 备注
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']//*[text()='添加']").click()
        page_wait()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/tableBelong/addTableBelong.html')]")))
        sleep(1)
        self.table_belong_page(database_name, table_en_ame, table_cn_Name, table_object, table_period, remark)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("数据 {0} 添加成功".format(table_cn_Name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(table_cn_Name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, table_cn_Name, remark):
        """
        :param obj: 表中文名称
        :param table_cn_Name: 表中文名称
        :param remark: 备注
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        self.browser.switch_to.parent_frame()
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AlarmPlatform/html/dataConfig/tableBelong/addTableBelong.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]")))

        self.table_belong_page(None, None, table_cn_Name, None, None, remark)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交成功"):
            log.info("{0} 修改成功".format(obj))
        else:
            log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def table_belong_page(self, database_name, table_en_ame, table_cn_Name, table_object, table_period, remark):
        """
        :param database_name: 数据库名称
        :param table_en_ame: 表英文名称
        :param table_cn_Name: 表中文名称
        :param table_object: 表使用对象
        :param table_period: 表周期
        :param remark: 备注
        """
        # 数据库名称
        if database_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='databaseInfoId']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'databaseInfoId') and text()='{0}']".format(database_name)).click()
            log.info("设置数据库: {0}".format(database_name))

        # 表英文名称
        if database_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameEn']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameEn']/following-sibling::span/input[1]").send_keys(
                table_en_ame)
            log.info("设置表英文名称: {0}".format(table_en_ame))

        # 表中文名称
        if table_cn_Name:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(
                table_cn_Name)
            log.info("设置表中文名称: {0}".format(table_cn_Name))

        # 表使用对象
        if table_object:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tableObject']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'tableObject') and text()='{0}']".format(table_object)).click()
            log.info("设置表使用对象: {0}".format(table_object))

        # 表周期
        if table_period:
            self.browser.find_element(
                By.XPATH, "//*[@id='editDiv']//*[@id='tablePeriod']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'tablePeriod') and text()='{0}']".format(table_period)).click()
            log.info("设置表周期: {0}".format(table_period))

        # 备注
        if remark:
            remark_textarea = self.browser.find_element(By.XPATH, "//*[@id='remark']")
            set_textarea(remark_textarea, remark)
            log.info("设置备注: {0}".format(remark))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitButtonId']//*[text()='提交']").click()

    def delete(self, obj):
        """
        :param obj: 表中文名称
        """
        log.info("开始删除数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: 服务器名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@id='tableName']/following-sibling::span[1]/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='tableName']/following-sibling::span[1]/input[1]").send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tableNameCh']/*[contains(@class,'tableNameCh')]/*[starts-with(text(),'{}')]".format(
                    obj))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='tableNameCh']/*[contains(@class,'tableNameCh')]/*[text()='{}']".format(obj))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
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
                                By.XPATH, "//*[@field='tableNameCh']/*[contains(@class,'tableNameCh')]/*[starts-with(text(),'{0}')]".format(
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
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
