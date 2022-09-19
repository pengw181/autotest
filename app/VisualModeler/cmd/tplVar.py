# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/3/28 下午2:12

from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.variable.globalVariable import *
from common.log.logger import log
from common.page.func.regexp import regular_cube
from common.page.func.pageMaskWait import page_wait


class VarEditor:

    def __init__(self, var_mode):
        self.browser = get_global_var("browser")
        self.var_mode = var_mode
        page_wait()
        sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='menu']//*[text()='{0}']".format(self.var_mode)).click()
        log.info("选择 {0}".format(self.var_mode))

    def add(self, var_name, var_type, var_desc, algorithm_list, time_set, list_content, agg_func_set, func_set):
        """
        :param var_name: 变量名称
        :param var_type: 变量类型
        :param var_desc: 变量描述
        :param algorithm_list: 运算规则配置，数组
        :param time_set: 时间配置，字典
        :param list_content: 列表内容，字符串
        :param agg_func_set: 聚合函数配置，字典
        :param func_set: 功能函数配置，字典
        """
        if self.var_mode == "常用变量":
            self._add_common_var(var_name=var_name)

        elif self.var_mode == "高级模式":
            self._add_advance_var(var_name, var_type, var_desc, algorithm_list, time_set, list_content, agg_func_set, func_set)
        else:
            raise KeyError("变量模式错误")

        # 点击提交
        self.browser.find_element(By.XPATH, "//*[@id='vareditor-submit']").click()
        log.info("{0}添加: {1}".format(self.var_mode, var_name))

    def _add_common_var(self, var_name):
        self.browser.find_element(By.XPATH, "//*[contains(@id,'common_var_') and text()='{0}']".format(var_name)).click()
        sleep(1)

    def _add_advance_var(self, var_name, var_type, var_desc, algorithm_list, time_set, list_content, agg_func_set, func_set):
        """
        :param var_name: 变量名称
        :param var_type: 变量类型
        :param var_desc: 变量描述
        :param algorithm_list: 运算规则配置，数组
        :param time_set: 时间配置
        :param list_content: 列表内容
        :param agg_func_set: 聚合函数配置
        :param func_set: 功能函数配置
        """
        # 变量名称
        if var_name:
            self.browser.find_element(By.XPATH, "//*[@id='varName']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='varName']/following-sibling::span//input[1]").send_keys(var_name)
            log.info("设置变量名称: {0}".format(var_name))

        # 变量类型，关键字比较和二维表比较时，分别为关键字运算/列运算，需要注意
        if var_type:
            self.browser.find_element(By.XPATH, "//*[@id='varType']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'varType') and text()='{0}']".format(var_type)).click()
            log.info("设置变量类型: {0}".format(var_type))
            sleep(1)

        # 变量描述
        if var_desc:
            self.browser.find_element(By.XPATH, "//*[@id='varDesc']/following-sibling::span//input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='varDesc']/following-sibling::span//input[1]").send_keys(var_desc)
            log.info("设置变量描述: {0}".format(var_desc))

        # 运算规则配置
        if algorithm_list:
            # 关键字运算
            if not isinstance(algorithm_list, list):
                raise TypeError("运算规则配置格式错误")
            self._kw_opt(algorithm_list=algorithm_list)

        # 时间配置
        if time_set:
            # 时间类型
            if not isinstance(time_set, dict):
                raise TypeError("时间配置格式错误")
            self._time_type(time_format=time_set.get("时间格式"), custom_time=time_set.get("自定义"),
                            interval=time_set.get("间隔"), unit=time_set.get("单位"))

        # 列表内容
        if list_content:
            # 自定义列表
            if not isinstance(list_content, str):
                raise TypeError("列表内容格式错误")
            self._custom_list(list_content=list_content)

        # 聚合函数配置
        if agg_func_set:
            # 聚合函数
            if not isinstance(agg_func_set, dict):
                raise TypeError("聚合函数配置格式错误")
            self._agg_func(col_name=agg_func_set.get("操作内容"), func_name=agg_func_set.get("函数名称"))

        # 功能函数配置
        if func_set:
            # 功能函数
            if not isinstance(func_set, dict):
                raise TypeError("功能函数配置格式错误")
            self._function(func_name=func_set.get("函数名称"), col_name=func_set.get("操作内容"),
                           match_type=func_set.get("匹配方式"), match_value=func_set.get("匹配值"),
                           match_regex=func_set.get("匹配正则"), replace_value=func_set.get("替换值"))

    def _kw_opt(self, algorithm_list):
        """
        # 关键字运算
        :param algorithm_list: 运算规则配置，数组

        [
            ["", "行数", "+", "1", ""]
        ]
        """
        # 运算规则配置
        if algorithm_list:
            row_num = 1
            for algorithm in algorithm_list:
                if not isinstance(algorithm, list):
                    raise TypeError("运算规则里的每一步需要是数组")

                orBracketL = algorithm[0]
                orDataL = algorithm[1]
                orOperate = algorithm[2]
                orDataR = algorithm[3]
                orBracketR = algorithm[4]

                row_xpath = "//*[@id='cols']/div[2]/div[{0}]".format(row_num)
                log.info("配置第{0}行运算规则".format(row_num))

                # 左括弧
                if orBracketL:
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orBracketL')]/following-sibling::span[1]//a").click()
                    bracket_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(orBracketL))
                    if len(bracket_elements) == 0:
                        raise NoSuchElementException
                    for element in bracket_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("设置左括弧: {0}".format(orBracketL))
                            break

                # 左值
                if orDataL:
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orDataL')]/following-sibling::span[1]//input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orDataL')]/following-sibling::span[1]//input[1]").send_keys(
                        orDataL)
                    log.info("设置左值: {0}".format(orDataL))

                # 操作符
                if orOperate:
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orOperate')]/following-sibling::span[1]//a").click()
                    operate_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(orOperate))
                    if len(operate_elements) == 0:
                        raise NoSuchElementException
                    for element in operate_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("设置操作符: {0}".format(orOperate))
                            break

                # 右值
                if orDataR:
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orDataR')]/following-sibling::span[1]//input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orDataR')]/following-sibling::span[1]//input[1]").send_keys(
                        orDataR)
                    log.info("设置右值: {0}".format(orDataR))

                # 右括弧
                if orBracketR:
                    self.browser.find_element(
                        By.XPATH, row_xpath + "//*[contains(@class,'orBracketR')]/following-sibling::span[1]//a").click()
                    bracket_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(orBracketR))
                    if len(bracket_elements) == 0:
                        raise NoSuchElementException
                    for element in bracket_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("设置右括弧: {0}".format(orBracketR))
                            break

                # 继续添加
                if row_num < len(algorithm_list):
                    self.browser.find_element(By.XPATH, "//*[@id='cols']//a[contains(@class,'add')]").click()
                    row_num += 1
                    sleep(1)

            # 获取预览结果
            preview_element = self.browser.find_element(By.XPATH, "//*[@id='orPreview']/following-sibling::span/input[2]")
            preview_result = preview_element.get_attribute("value")
            log.info("规则预览: {0}".format(preview_result))

    def _time_type(self, time_format, custom_time, interval, unit):
        """
        # 时间类型
        :param time_format: 时间格式
        :param custom_time: 自定义
        :param interval: 间隔
        :param unit: 单位

        # 普通格式
        {
            "时间格式": "yyyyMMddHHmmss",
            "间隔": "-1",
            "单位": "天"
        }

        # 自定义格式
        {
            "时间格式": "自定义",
            "自定义": "yyyyMMddHHmmss",
            "间隔": "-1",
            "单位": "月"
        }
        """
        # 时间格式
        if time_format:
            self.browser.find_element(By.XPATH, "//*[@id='timeFormatSel']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'timeFormatSel') and text()='{0}']".format(time_format)).click()
            log.info("设置时间格式: {0}".format(time_format))

        # 自定义
        if custom_time:
            self.browser.find_element(By.XPATH, "//*[@id='customTime']/following-sibling::span[1]//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='customTime']/following-sibling::span[1]//input[1]").send_keys(custom_time)
            log.info("设置自定义: {0}".format(custom_time))

        # 间隔
        if interval:
            self.browser.find_element(By.XPATH, "//*[@id='timeInterval']/following-sibling::span[1]//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='timeInterval']/following-sibling::span[1]//input[1]").send_keys(interval)
            log.info("设置间隔: {0}".format(interval))

        # 单位
        if unit:
            self.browser.find_element(By.XPATH, "//*[@id='timeUnit']/following-sibling::span[1]//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'timeUnit') and text()='{0}']".format(unit)).click()
            log.info("设置单位: {0}".format(unit))

    def _custom_list(self, list_content):
        """
        # 自定义列表
        :param list_content: 列表内容
        """
        # 列表内容
        if list_content:
            self.browser.find_element(By.XPATH, "//*[@id='customListValue']/following-sibling::span[1]//textarea").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='customListValue']/following-sibling::span[1]//textarea").send_keys(list_content)
            log.info("设置列表内容: {0}".format(list_content))

    def _agg_func(self, col_name, func_name):
        """
        # 聚合函数
        :param col_name: 操作内容
        :param func_name: 函数名称

        {
            "操作内容": "行数",
            "函数名称": "总计(sum)"
        }
        """
        # 操作内容
        if col_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='aggregateFuncOperateCol']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'aggregateFuncOperateCol') and text()='{0}']".format(col_name)).click()
            log.info("设置操作内容: {0}".format(col_name))

        # 函数名称
        if func_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='aggregateFuncName']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'aggregateFuncName') and text()='{0}']".format(func_name)).click()
            log.info("设置函数名称: {0}".format(func_name))

    def _function(self, func_name, col_name, match_type, match_value, match_regex, replace_value):
        """
        # 功能函数
        :param func_name: 函数名称
        :param col_name: 操作内容
        :param match_type: 匹配方式
        :param match_value: 匹配值
        :param match_regex: 匹配正则，与匹配值二选一
        :param replace_value: 替换值

        # 文本替换
        {
            "函数名称": "字符串替换",
            "操作内容": "行数",
            "匹配方式": "文本",
            "匹配值": "abc",
            "替换值": "ddd"
        }

        # 正则替换
        {
            "函数名称": "字符串替换",
            "操作内容": "行数",
            "匹配方式": "正则",
            "匹配正则": {
                "标签配置": [
                    {
                        "": "",
                        "": "",
                        "": ""
                    },
                    {
                        "": "",
                        "": "",
                        "": ""
                    }
                ]
            },
            "替换值": "ddd"
        }
        """
        # 函数名称
        if func_name:
            self.browser.find_element(By.XPATH, "//*[@id='handleFuncSelect']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'handleFuncSelect') and text()='{0}']".format(func_name)).click()
            log.info("设置函数名称: {0}".format(func_name))

        # 操作内容
        if col_name:
            self.browser.find_element(By.XPATH, "//*[@id='handleFuncCol']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'handleFuncCol') and text()='{0}']".format(col_name)).click()
            log.info("设置操作内容: {0}".format(col_name))

        # 匹配方式
        if match_type:
            self.browser.find_element(
                By.XPATH, "//*[@name='replaceType']/following-sibling::span[text()='{0}']".format(match_type)).click()
            log.info("设置匹配方式: {0}".format(match_type))
            sleep(1)

        # 匹配值
        if match_value:
            self.browser.find_element(By.XPATH, "//*[@id='matchValue']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='matchValue']/following-sibling::span/input[1]").send_keys(match_value)
            log.info("设置匹配值: {0}".format(match_value))

        # 匹配正则
        if match_regex:
            # 页面划到正则魔方
            regex_cube = self.browser.find_element(By.XPATH, "//*[@id='regexpReplaceDiv']//h3[text()='正则魔方']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", regex_cube)
            confirm_selector = "//*[@id='regexpReplaceDiv']"
            regular_cube(advance_mode=match_regex.get("高级模式"), regular=match_regex.get("标签配置"),
                         expression=match_regex.get("表达式"), enable_check=match_regex.get("开启验证"),
                         check_msg=match_regex.get("样例数据"), confirm_selector=confirm_selector)
            log.info("设置匹配正则完成")

        # 替换值
        if replace_value:
            self.browser.find_element(By.XPATH, "//*[@id='replaceValue']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='replaceValue']/following-sibling::span/input[1]").send_keys(replace_value)
            log.info("设置替换值: {0}".format(replace_value))
