# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/4/25 下午3:10

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.variable.globalVariable import *
from common.log.logger import log
from common.page.func.toast import Toast
from common.page.func.pageMaskWait import page_wait
from common.wrapper.dashboardCheck import closeAndEnterDashboard
from selenium.webdriver import ActionChains
from time import sleep


@closeAndEnterDashboard
class CustomizeInterface:

    def __init__(self):
        self.browser = get_global_var("browser")
        page_wait(5)
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='自定义数据接口']")))
        self.browser.find_element(By.XPATH, "//*[text()='自定义数据接口']").click()
        sleep(1)

    def _choose(self, tableName):
        """
        # 选择一条表接口
        :param tableName: 表中文名称
        """
        self.browser.find_element(By.XPATH, "//*[@id='tableName']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='tableName']/following-sibling::span/input[1]").send_keys(tableName)
        log.info("表中文名称输入: {0}".format(tableName))
        self.browser.find_element(By.XPATH, "//*[@title='查询自定义数据接口列表']").click()
        sleep(2)
        self.browser.find_element(By.XPATH, "//*[@field='tableNameCH']/*[text()='{0}']".format(tableName)).click()
        log.info("选择表: {0}".format(tableName))

    def fieldConversion(self, tableName, conversion):
        """
        # 字段类型转化
        :param tableName: 表中文名称
        :param conversion: 转化配置，数组
        """
        # 选择表
        self._choose(tableName)
        self.browser.find_element(By.XPATH, "//*[text()='字段类型转换']").click()
        page_wait(3)
        sleep(1)

        # 转化配置
        for config in conversion:
            if not isinstance(config, dict):
                raise TypeError
            colName = config.get("字段")
            targetType = config.get("目标格式")
            dateSourceType = config.get("日期源格式")
            dateNewType = config.get("日期新格式")

            # 字段
            self.browser.find_element(
                By.XPATH, "//*[@class='targetareaParentDiv']/div[2]/*[contains(text(),'{0}')]".format(colName)).click()
            log.info("选择字段: {0}".format(colName))

            # 目标格式
            if targetType:
                self.browser.find_element(By.XPATH, "//*[@id='fieldConversionType']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'fieldConversionType') and text()='{0}']".format(targetType)).click()
                log.info("设置目标格式: {0}".format(targetType))

            # 日期源格式
            if dateSourceType:
                self.browser.find_element(By.XPATH, "//*[@id='dateSourceType']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'dateSourceType') and text()='{0}']".format(dateSourceType)).click()
                log.info("设置日期源格式: {0}".format(dateSourceType))

            # 日期新格式
            if dateNewType:
                self.browser.find_element(By.XPATH, "//*[@id='dateNewType']/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'dateNewType') and text()='{0}']".format(dateSourceType)).click()
                log.info("设置日期新格式: {0}".format(dateNewType))

            # 保存
            self.browser.find_element(By.XPATH, "//*[@id='fieldConversionSave']").click()
            toast = Toast()
            msg = toast.get_msg()
            if toast.msg_contains("保存成功"):
                log.info("【{0}】字段转化保存成功".format(colName))
                set_global_var("ResultMsg", msg, False)
                toast.waitUntil()
            else:
                log.error("【{0}】字段转化保存失败，失败原因: {1}".format(colName, msg))
                break

    def fieldClassify(self, tableName, xList, yList, gList):
        """
        # 字段分类
        :param tableName: 表中文名称
        :param xList: 维度字段，数组
        :param yList: 度量字段，数组
        :param gList: 分组字段，数组
        """
        # 选择表
        self._choose(tableName)
        self.browser.find_element(By.XPATH, "//*[text()='字段分类']").click()
        page_wait(3)
        sleep(1)
        action = ActionChains(self.browser)

        # 维度字段
        if xList:
            if not isinstance(xList, list):
                raise TypeError("【维度字段】不是数组")
            element = self.browser.find_element(By.XPATH, "//*[@list='xList']")
            for xCol in xList:
                targetCol = self.browser.find_element(
                    By.XPATH, "//*[@class='targetareaParentDiv']/div[2]//*[text()='{0}']".format(xCol))
                action.drag_and_drop(targetCol, element).perform()
                log.info("维度字段加入: {0}".format(xCol))
                sleep(1)

        # 度量字段
        if yList:
            if not isinstance(yList, list):
                raise TypeError("【度量字段】不是数组")
            element = self.browser.find_element(By.XPATH, "//*[@list='yList']")
            for yCol in yList:
                targetCol = self.browser.find_element(
                    By.XPATH, "//*[@class='targetareaParentDiv']/div[2]//*[text()='{0}']".format(yCol))
                action.drag_and_drop(targetCol, element).perform()
                log.info("度量字段加入: {0}".format(yCol))
                sleep(1)

        # 分组字段
        if gList:
            if not isinstance(gList, list):
                raise TypeError("【分组字段】不是数组")
            element = self.browser.find_element(By.XPATH, "//*[@list='gList']")
            for gCol in gList:
                targetCol = self.browser.find_element(
                    By.XPATH, "//*[@class='targetareaParentDiv']/div[2]//*[text()='{0}']".format(gCol))
                action.drag_and_drop(targetCol, element).perform()
                log.info("分组字段加入: {0}".format(gCol))
                sleep(1)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='fieldClassifySave']").click()
        toast = Toast()
        msg = toast.get_msg()
        if toast.msg_contains("保存成功"):
            log.info("字段分类保存成功")
        else:
            log.error("字段分类保存失败，失败原因: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)
