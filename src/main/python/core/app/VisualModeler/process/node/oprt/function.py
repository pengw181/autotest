# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午9:19

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.regular import RegularCube
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class FunctionWorker:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        page_wait()
        # 切换到函数配置iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'funcList.html')]")))
        # 等待页面加载
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(@onclick,'chooseEmailVar')]")))

    def run(self, var_name, var_index, func_list):
        """
        :param var_name: 输入变量
        :param var_index: 数组索引
        :param func_list: 函数处理列表，数组

        [
            {
                "动作": "添加",
                "函数": "取绝对值"
            },
            {
                "动作": "添加",
                "函数": "数组转字符串(array to string)",
                "分隔符": ","
            }
        ]


        {
            "表达式": [
                ["函数", {
                    "输入变量": "时间",
                    "数组索引": "1,3",
                    "函数处理列表": [
                        {
                            "动作": "添加",
                            "函数": "取绝对值"
                        },
                        {
                            "动作": "添加",
                            "函数": "数组转字符串(array to string)",
                            "分隔符": ","
                        },
                        {
                            "动作": "添加",
                            "函数": "时间处理(date handler)",
                            "时间格式": "yyyyMMddHHmmss",
                            "间隔": "-1",
                            "单位": "天",
                            "语言": "中文"
                        }
                    ]
                }]
            ],
            "输出名称": "普通运算函数结果",
            "输出列": "*",
            "赋值方式": "替换",
            "是否转置": "否",
            "批量修改所有相同的变量名": "否"
        }
        """

        # 输入变量
        if var_name:
            self.browser.find_element(By.XPATH, "//*[contains(@onclick,'chooseEmailVar')]").click()
            choose_var(var_name=var_name)

        # 数组索引
        if var_index:
            self.browser.find_element(
                By.XPATH, "//*[@name='inputVarIndex']/preceding-sibling::input").send_keys(var_index)
            log.info("设置数组索引: {0}".format(var_index))
            sleep(1)

        # 函数处理列表
        if func_list:
            for func in func_list:
                # 操作
                action = func.get("动作")
                # 函数名
                func_name = func.get("函数")
                if action == "添加":
                    self.browser.find_element(By.XPATH, "//*[@onclick='addFuncBtnInfo()']//*[text()='添加']").click()
                    func.pop("动作")
                    func.pop("函数")
                    self.set_function(func_name=func_name, func_set=func)

                elif action == "修改":
                    # 选择函数
                    self.browser.find_element(
                        By.XPATH, "//*[@field='funcName']/*[contains(text(),'{0}')]".format(func_name)).click()
                    func.pop("动作")
                    func.pop("函数")
                    self.set_function(func_name=func_name, func_set=func)

                else:
                    # 选择函数
                    self.browser.find_element(
                        By.XPATH, "//*[@field='funcName']/*[contains(text(),'{0}')]".format(func_name)).click()
                    # 点击删除
                    self.browser.find_element(By.XPATH, "//*[@onclick='delete_func();']//*[text()='保存']").click()
                    alert = BeAlertBox(back_iframe="default")
                    msg = alert.get_msg()
                    if alert.title_contains(func_name, auto_click_ok=False):
                        alert.click_ok()
                        msg = alert.get_msg()
                        if alert.title_contains("成功"):
                            log.info("删除函数成功")
                        else:
                            log.warning("删除函数失败，失败提示: {0}".format(msg))
                    else:
                        log.warning("删除函数失败，失败提示: {0}".format(msg))
                    gbl.temp.set("ResultMsg", msg)

                    # 切到节点iframe
                    self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                    # 切到操作配置iframe
                    self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
                    # 切换到运算配置iframe
                    self.browser.switch_to.frame(
                        self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                    # 切换到基础运算iframe
                    self.browser.switch_to.frame(
                        self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgBase.html')]"))
                    # 切换到函数配置iframe
                    self.browser.switch_to.frame(
                        self.browser.find_element(By.XPATH, "//iframe[contains(@src,'funcList.html')]"))
                # 休眠
                sleep(1)

        # 保存
        self.browser.find_element(By.XPATH, "//*[@onclick='save_func();']//*[text()='保存']").click()
        # 切换到上层iframe
        self.browser.switch_to.parent_frame()
        sleep(1)

    def set_function(self, func_name, func_set):
        """
        {
            "动作": "添加",
            "函数": "取绝对值"
        },
        {
            "动作": "添加",
            "函数": "数组转字符串",
            "分隔符": ","
        },
        {
            "动作": "添加",
            "函数": "时间处理",
            "时间格式": "yyyyMMddHHmmss",
            "间隔": "-1",
            "单位": "日",
            "语言": "中文"
        },
        {
            "动作": "添加",
            "函数": "10进制转16进制"
        },
        {
            "动作": "添加",
            "函数": "去重"
        },
        {
            "动作": "添加",
            "函数": "科学计数法转普通数字"
        },
        {
            "动作": "添加",
            "函数": "获取网元属性",
            "网元列": "1"
        },
        {
            "动作": "添加",
            "函数": "16进制转10进制"
        },
        {
            "动作": "添加",
            "函数": "数组格式化"
        },
        {
            "动作": "添加",
            "函数": "长度"
        },
        {
            "动作": "添加",
            "函数": "科学计算"
        },
        {
            "动作": "添加",
            "函数": "字符替换",
            "正则匹配": "否",
            "查找内容": "aaabbc",
            "替换": "nice",
            "方式": "替换所有"
        },
        {
            "动作": "添加",
            "函数": "取小数位数",
            "小数位数": "2",
            "使用千分位分隔符": "是"
        },
        {
            "动作": "添加",
            "函数": "拆分",
            "拆分方式": "文本",
            "分隔符": ","
        },
        {
            "动作": "添加",
            "函数": "字符串转数字"
        },
        {
            "动作": "添加",
            "函数": "科学计算"
        },
        {
            "动作": "添加",
            "函数": "字符串截取",
            "开始": "1",
            "结束": "5"
        },
        {
            "动作": "添加",
            "函数": "转置"
        },
        {
            "动作": "添加",
            "函数": "去空格"
        }

        """

        # 选择函数
        self.browser.find_element(By.XPATH, "//*[@name='funclist']/preceding-sibling::input").click()
        self.browser.find_element(
            By.XPATH, "//*[contains(@id,'funclist') and contains(text(),'{0}')]".format(func_name)).click()

        if func_name.find("数组转字符串") > -1:
            # 分隔符
            if func_set.__contains__("分隔符"):
                ar_split = func_set.get("分隔符")
                self.browser.find_element(By.XPATH, "//*[@name='ar_split']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='ar_split']/preceding-sibling::input").send_keys(ar_split)
                log.info("设置分隔符: {0}".format(ar_split))
                sleep(1)

        elif func_name.find("时间处理") > -1:
            # 时间格式
            if func_set.__contains__("时间格式"):
                time_format = func_set.get("时间格式")
                self.browser.find_element(
                    By.XPATH, "//*[@class='timeArea']//*[@id='format']/following-sibling::span[1]//a").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'format') and text()='{0}']".format(time_format)).click()
                log.info("设置时间格式: {0}".format(time_format))
                sleep(1)

            # 间隔
            if func_set.__contains__("间隔"):
                time_interval = func_set.get("间隔")
                self.browser.find_element(By.XPATH, "//*[@name='interval']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='interval']/preceding-sibling::input").send_keys(time_interval)
                log.info("设置间隔: {0}".format(time_interval))
                sleep(1)

            # 分隔符
            if func_set.__contains__("单位"):
                time_unit = func_set.get("单位")
                self.browser.find_element(
                    By.XPATH, "//*[@class='timeArea']//*[@name='unit']/preceding-sibling::input").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'unit') and text()='{0}']".format(time_unit)).click()
                log.info("设置单位: {0}".format(time_unit))
                sleep(1)

            # 语言
            if func_set.__contains__("语言"):
                language = func_set.get("语言")
                self.browser.find_element(
                    By.XPATH, "//*[@class='timeArea']//*[@name='language']/preceding-sibling::input").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'language') and text()='{0}']".format(language)).click()
                log.info("设置语言: {0}".format(language))
                sleep(1)

            # 预览
            self.browser.find_element(By.XPATH, "//*[@onclick='previewTimeFormat();']//*[text()='预览']").click()
            js = 'return $("#timeResult")[0].textContent;'
            time_result = self.browser.execute_script(js)
            sleep(1)
            log.info("时间函数预览结果: {0}".format(time_result))

        elif func_name.find("获取网元属性") > -1:
            # 网元列
            if func_set.__contains__("网元列"):
                var_index = func_set.get("网元列")
                self.browser.find_element(By.XPATH, "//*[@name='var_index']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='var_index']/preceding-sibling::input").send_keys(var_index)
                log.info("设置网元列: {0}".format(var_index))
                sleep(1)

        elif func_name.find("字符替换") > -1:
            # 正则匹配
            if func_set.__contains__("正则匹配"):
                # 获取是否正则匹配当前勾选状态
                js = 'return $("#isRegex")[0].checked;'
                status = self.browser.execute_script(js)
                log.info("【正则匹配】勾选状态: {0}".format(status))
                # 聚焦元素
                is_regular = self.browser.find_element(By.XPATH, "//*[@id='isRegex']")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", is_regular)
                if func_set.get("正则匹配") == "是":
                    if not status:
                        is_regular.click()
                    log.info("勾选【正则匹配】")

                    # 查找内容
                    if func_set.__contains__("查找内容"):
                        regex = func_set.get("查找内容")
                        self.browser.find_element(By.XPATH, "//*[@id='keyExpr1']//following-sibling::span[1]//a").click()
                        sleep(1)
                        # 切换到正则配置iframe
                        self.browser.switch_to.frame(
                            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
                        regular_cube = RegularCube()
                        regular_cube.setRegular(set_type=regex.get("设置方式"), regular_name=regex.get("正则模版名称"),
                                                advance_mode=regex.get("高级模式"), regular=regex.get("标签配置"),
                                                expression=regex.get("表达式"))
                        if regular_cube.needJumpIframe:
                            alert = BeAlertBox(back_iframe="default")
                            msg = alert.get_msg()
                            if alert.title_contains("成功"):
                                log.info("保存正则模版成功")
                                # 切换到节点iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                                # 切换到操作配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
                                # 切换到运算配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                                # 切换到基础运算iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgBase.html')]"))
                                # 切换到函数配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'funcList.html')]"))
                            else:
                                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                            gbl.temp.set("ResultMsg", msg)

                        # 关闭正则魔方配置
                        self.browser.find_element(
                            By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
                        sleep(1)
                else:
                    if status:
                        is_regular.click()
                        log.info("取消勾选【正则匹配】")
                    else:
                        log.info("【正则匹配】标识为否，不开启")
            else:
                # 查找内容
                if func_set.__contains__("查找内容"):
                    find = func_set.get("查找内容")
                    self.browser.find_element(By.XPATH, "//*[@name='find1']/preceding-sibling::input").clear()
                    self.browser.find_element(By.XPATH, "//*[@name='find1']/preceding-sibling::input").send_keys(find)
                    log.info("设置查找内容: {0}".format(find))
                    sleep(1)

            # 替换
            if func_set.__contains__("替换"):
                replace = func_set.get("替换")
                self.browser.find_element(By.XPATH, "//*[@name='replace']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='replace']/preceding-sibling::input").send_keys(replace)
                log.info("设置替换: {0}".format(replace))
                sleep(1)

            # 方式
            if func_set.__contains__("方式"):
                replace_type = func_set.get("方式")
                self.browser.find_element(By.XPATH, "//*[@name='type']/preceding-sibling::input").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'type') and text()='{0}']".format(replace_type)).click()
                log.info("设置方式: {0}".format(replace_type))
                sleep(1)

        elif func_name.find("取小数位数") > -1:
            # 小数位数
            if func_set.__contains__("小数位数"):
                precision = func_set.get("小数位数")
                self.browser.find_element(By.XPATH, "//*[@name='precision']/preceding-sibling::input").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@name='precision']/preceding-sibling::input").send_keys(precision)
                log.info("设置小数位数: {0}".format(precision))
                sleep(1)

            # 使用千分位分隔符
            if func_set.__contains__("使用千分位分隔符"):
                # 获取使用千分位分隔符当前勾选状态
                js = 'return $("#separator")[0].checked;'
                status = self.browser.execute_script(js)
                log.info("【使用千分位分隔符】勾选状态: {0}".format(status))
                # 聚焦元素
                separator = self.browser.find_element(By.XPATH, "//*[@id='separator']")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", separator)
                if func_set.get("使用千分位分隔符") == "是":
                    if not status:
                        separator.click()
                    log.info("勾选【使用千分位分隔符】")
                else:
                    if status:
                        separator.click()
                        log.info("取消勾选【使用千分位分隔符】")
                    else:
                        log.info("【使用千分位分隔符】标识为否，不开启")

        elif func_name.find("拆分") > -1:
            # 拆分方式
            if func_set.__contains__("拆分方式"):
                split_type = func_set.get("拆分方式")
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'splitType')]//*[text()='{0}']".format(split_type)).click()
                log.info("设置拆分方式: {0}".format(split_type))
                sleep(1)

                # 分隔符
                if func_set.__contains__("分隔符"):
                    seperator = func_set.get("分隔符")
                    if split_type == "文本":
                        self.browser.find_element(By.XPATH, "//*[text()='分隔符']/following-sibling::span/input[1]").clear()
                        self.browser.find_element(
                            By.XPATH, "//*[text()='分隔符']/following-sibling::span/input[1]").send_keys(seperator)
                        log.info("设置分隔符: {0}".format(seperator))
                        sleep(1)
                    else:
                        self.browser.find_element(By.XPATH, "//*[@id='keyExpr2']/following-sibling::span//a").click()
                        sleep(1)
                        # 切换到正则配置iframe
                        self.browser.switch_to.frame(
                            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
                        regular_cube = RegularCube()
                        regular_cube.setRegular(set_type=seperator.get("设置方式"), regular_name=seperator.get("正则模版名称"),
                                                advance_mode=seperator.get("高级模式"), regular=seperator.get("标签配置"),
                                                expression=seperator.get("表达式"))
                        if regular_cube.needJumpIframe:
                            alert = BeAlertBox(back_iframe="default")
                            msg = alert.get_msg()
                            if alert.title_contains("成功"):
                                log.info("保存正则模版成功")
                                # 切换到节点iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                                # 切换到操作配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
                                # 切换到运算配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateVar.html')]"))
                                # 切换到基础运算iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgBase.html')]"))
                                # 切换到函数配置iframe
                                self.browser.switch_to.frame(
                                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'funcList.html')]"))
                            else:
                                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                            gbl.temp.set("ResultMsg", msg)

                        # 关闭正则魔方配置
                        self.browser.find_element(
                            By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
                        sleep(1)

        elif func_name.find("字符串截取") > -1:
            # 开始
            if func_set.__contains__("开始"):
                begin = func_set.get("开始")
                self.browser.find_element(By.XPATH, "//*[@name='begin']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='begin']/preceding-sibling::input").send_keys(begin)
                log.info("设置开始: {0}".format(begin))
                sleep(1)

            # 结束
            if func_set.__contains__("结束"):
                end = func_set.get("结束")
                self.browser.find_element(By.XPATH, "//*[@name='end']/preceding-sibling::input").clear()
                self.browser.find_element(By.XPATH, "//*[@name='end']/preceding-sibling::input").send_keys(end)
                log.info("设置结束: {0}".format(end))
                sleep(1)

        # 保存函数
        save_ele = self.browser.find_element(By.XPATH, "//*[@onclick='addFuncRow()']//span[2]")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", save_ele)
        save_ele.click()

        # 获取函数表达式
        js = 'return $("#expr")[0].textContent;'
        expr = self.browser.execute_script(js)
        log.info("函数表达式: {0}".format(expr))
