# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:56

from selenium.common.exceptions import NoSuchElementException
from common.page.func.alertBox import BeAlertBox
from common.page.func.regular import RegularCube
from common.page.func.input import set_textarea
from time import sleep
from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


class RegexpTemplate:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("指令配置-正则模版管理")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/regexp/regexpTmplMgr.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def choose(self, regexp_name):
        """
        :param regexp_name: 正则模版名称
        """
        try:
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").send_keys(regexp_name)
            page_wait()
            self.browser.find_element(By.XPATH, "//*[@id='regexp-query']//*[text()='查询']").click()
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[@field='regxTemplName']/*[contains(@class,'regxTemplName')]/*[text()='{}']".format(
                    regexp_name)).click()
            log.info("选择正则模版：{0}".format(regexp_name))
        except NoSuchElementException:
            log.error("所选正则模版不存在, 正则模版名称: {0}".format(regexp_name))

    def add(self, regexp_name, remark, regexp_info):
        """
        :param regexp_name: 正则模版名称
        :param remark: 模版描述
        :param regexp_info: 正则魔方
        {
            "正则模版名称": "",
            "模版描述": "",
            "正则魔方": {
                "正则模版名称": "pw自动化正则模版",
                "高级模式": "否",
                "标签配置": [
                    {
                        "标签": "自定义文本",
                        "自定义值": "pw",
                        "是否取值": "黄色"
                    },
                    {
                        "标签": "任意字符",
                        "长度": "1到多个",
                        "是否取值": "绿色"
                    },
                    {
                        "标签": "数字",
                        "正数负数": "正数",
                        "匹配小数": "是",
                        "匹配%": "是",
                        "匹配千分位": "是",
                        "匹配并去掉逗号": "是",
                        "长度": "1到多个",
                        "是否取值": "绿色"
                    },
                    {
                        "标签": "特殊字符",
                        "特殊字符": "|",
                        "长度": "1到多个",
                        "是否取值": "绿色"
                    },
                    {
                        "标签": "IP",
                        "IPV4": "是",
                        "IPV6": "是",
                        "是否取值": "绿色"
                    }
                ],
                "开启验证": "是",
                "样例数据": "ping_sample.txt"
            }
        }

        方式三，高级模式：
        {
            "模版名称": "",
            "模版描述": "",
            "正则魔方": {
                "设置方式": "添加",
                "正则模版名称": "pw自动化正则模版",
                "高级模式": "是",
                "表达式": "(pw)(.+)",
                "开启验证": "是",
                "样例数据": "ping_sample.txt"
            }
        }
        """
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='添加']")))
        self.browser.find_element(By.XPATH, "//*[text()='添加']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'regexpTmplEditWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='regxTemplName']/following-sibling::span/input[1]")))

        self.regexp_page(regexp_name=regexp_name, remark=remark, regexp_info=regexp_info)

        # 提交
        self.browser.find_element(By.XPATH, "//*[text()='提交']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(regexp_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(regexp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, regexp_name, remark, regexp_info):
        """
        :param obj: 正则模版名称
        :param regexp_name: 正则模版名称
        :param remark: 模版描述
        :param regexp_info: 正则魔方
        """
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'regexpTmplEditWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='regxTemplName']/following-sibling::span/input[1]")))

        # 删除已添加的所有标签
        if regexp_info.__contains__("标签配置"):
            current_tag = self.browser.find_elements(By.XPATH, "//*[@class='removeTag']")
            for tag in current_tag:
                tag.click()

        self.regexp_page(regexp_name=regexp_name, remark=remark, regexp_info=regexp_info)

        # 提交
        self.browser.find_element(By.XPATH, "//*[text()='提交']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 修改成功".format(obj))
        else:
            log.warning("数据 {0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def regexp_page(self, regexp_name, remark, regexp_info):
        """
        :param regexp_name: 正则模版名称
        :param remark: 模版描述
        :param regexp_info: 正则魔方
        """
        # 正则模版名称
        if regexp_name:
            self.browser.find_element(By.XPATH, "//*[@id='regxTemplName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='regxTemplName']/following-sibling::span/input[1]").send_keys(regexp_name)
            log.info("设置模版名称: {0}".format(regexp_name))

        # 模版描述
        if remark:
            remark_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='regxTemplDesc']/following-sibling::span/textarea")
            set_textarea(remark_textarea, remark)
            log.info("设置模版描述: {0}".format(remark))

        # 正则魔方
        if regexp_info:
            confirm_selector = "//*[@id='regexContainerDiv']"
            regular = RegularCube()
            regular.setRegular(regular_name=regexp_info.get("正则模版名称"), advance_mode=regexp_info.get("高级模式"),
                               regular=regexp_info.get("标签配置"), expression=regexp_info.get("表达式"),
                               enable_check=regexp_info.get("开启验证"), check_msg=regexp_info.get("样例数据"),
                               confirm_selector=confirm_selector)

    def delete(self, regexp_name):
        """
        :param regexp_name: 正则模版名称
        """
        self.choose(regexp_name)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(regexp_name, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} 删除成功".format(regexp_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(regexp_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(regexp_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, regexp_name, fuzzy_match=False):
        """
        :param regexp_name: 正则模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]")))
        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").send_keys(regexp_name)
        self.browser.find_element(By.XPATH, "//*[text()='查询']").click()
        page_wait()
        sleep(1)
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='regxTemplName']//*[starts-with(@data-mtips,'{}')]".format(regexp_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='regxTemplName']//*[@data-mtips='{0}']".format(regexp_name))
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
                                By.XPATH, "//*[@field='regxTemplName']//*[starts-with(@data-mtips,'{}')]".format(
                                    regexp_name))
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
                    log.warning("{0} 删除失败，失败提示: {1}".format(regexp_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
