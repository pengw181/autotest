# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:10

import json
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.func.upload import upload
from client.page.func.alertBox import BeAlertBox
from client.page.func.pageMaskWait import page_wait
from client.page.func.positionPanel import getPanelXpath
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class Script:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("常用信息管理-脚本管理")
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/scriptCfg.html')]"))
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

        # 脚本名称
        if query.__contains__("脚本名称"):
            server_name = query.get("脚本名称")
            self.browser.find_element(By.XPATH, "//*[@id='scriptName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='scriptName']/following-sibling::span/input[1]").send_keys(
                server_name)
            select_item = server_name

        # 创建人
        if query.__contains__("创建人"):
            create_name = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@id='createName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='createName']/following-sibling::span/input[1]").send_keys(
                create_name)

        # 脚本类型
        if query.__contains__("脚本类型"):
            script_type = query.get("脚本类型")
            self.browser.find_element(By.XPATH, "//*[@id='scriptType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'scriptType') and text()='{0}']".format(script_type)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[contains(@data-options,'icon-search-primary')]").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)
            return
        if need_choose:
            if select_item:
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='scriptName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, script_name, script_type, data_type):
        """
        :param script_name: 脚本名称
        :param script_type: 脚本类型
        :param data_type: 数据类型
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=add')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='scriptName']/preceding-sibling::input")))

        self.script_page(script_name=script_name, script_type=script_type, data_type=data_type)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@onclick='saveScriptCfgInfo()']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("数据 {0} 添加成功".format(script_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(script_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, script, script_name, data_type):
        """
        :param script: 脚本名称
        :param script_name: 脚本名称
        :param data_type: 数据类型
        """
        log.info("开始修改数据")
        self.search(query={"脚本名称": script}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            set_global_var("ResultMsg", msg, False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='scriptName']/preceding-sibling::input")))

            self.script_page(script_name=script_name, data_type=data_type)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@onclick='saveScriptCfgInfo()']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} 修改成功".format(script))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(script, msg))
            set_global_var("ResultMsg", msg, False)

    def script_page(self, script_name, data_type, script_type=None):
        """
        :param script_name: 脚本名称
        :param script_type: 脚本类型
        :param data_type: 数据类型
        """
        # 脚本名称
        if script_name:
            self.browser.find_element(By.XPATH, "//*[@name='scriptName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='scriptName']/preceding-sibling::input").send_keys(
                script_name)
            log.info("设置脚本名称: {0}".format(script_name))

        # 脚本类型
        if script_type:
            self.browser.find_element(By.XPATH, "//*[@id='scriptName']/../following-sibling::div[1]/span/span/a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'scriptType') and text()='{0}']".format(script_type)).click()
            log.info("设置脚本类型: {0}".format(script_type))

        # 数据类型
        if data_type:
            self.browser.find_element(By.XPATH, "//*[@textboxname='dataTypeId']/following-sibling::span[1]//a").click()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.visibility_of_element_located((
                By.XPATH, "//*[contains(@id,'dataTypeId') and text()='{0}']".format(data_type))))
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'dataTypeId') and text()='{0}']".format(data_type)).click()
            log.info("设置数据类型: {0}".format(data_type))

    def choose_version(self, script_name, ver_no):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        """
        self.search(query={"脚本名称": script_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=edit')]")))
            page_wait()
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[@class='addScript_div']//*[contains(@id,'version')]//*[@field='createrName']/*[text()='{0}']".format(
                    ver_no))))
            self.browser.find_element(
                By.XPATH, "//*[@class='addScript_div']//*[contains(@id,'version')]//*[@field='createrName']/*[text()='{0}']".format(
                    ver_no)).click()
            page_wait()
            log.info("选择版本【{0}】".format(ver_no))

    def add_param(self, script_name, ver_no, params):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        :param params: 脚本参数
        """
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        i = 1
        for param in params:
            self.browser.find_element(By.XPATH, "//*[@id='addParamSpan']").click()
            self.browser.find_element(
                By.XPATH, "//*[@id='inId{0}']/following-sibling::span[1]/input[1]".format(i)).send_keys(param)
            i += 1
            log.info("脚本 {0}, 版本【{1}】添加参数: {2}".format(script_name, ver_no, param))
            # sleep(1)
        # 保存当前版本
        self.save_current_version()

    def update_param(self, script_name, ver_no, params):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        :param params: 脚本参数
        """
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        sleep(1)
        for order, new_param in params:
            self.browser.find_element(
                By.XPATH, "//*[@id='inId{0}']/following-sibling::span[1]/input[1]".format(order)).clear()
            # self.browser.find_element(By.XPATH, 
            #     "//*[@id='inId{0}']/following-sibling::span[1]/input[1]".format(order)).click()
            self.browser.find_element(
                By.XPATH, "//*[@id='inId{0}']/following-sibling::span[1]/input[1]".format(order)).send_keys(new_param)
            log.info("脚本 {0}, 版本【{1}】修改参数: 序号{2} > {3}".format(script_name, ver_no, order, new_param))
            # sleep(1)
        # 保存当前版本
        self.save_current_version()

    def upload_script_file(self, script_name, ver_no, file_name):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        :param file_name: 脚本文件名
        """
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        # 调用上传文件操作
        log.info("执行上传脚本文件操作")
        upload(file_name=file_name, catalog="script")
        self.browser.find_element(By.XPATH, "//*[@id='importScriptFile']//*[text()='上传文件']").click()

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("脚本 {0}, 版本【{1}】上传脚本文件: {2}".format(script_name, ver_no, file_name))
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=edit')]"))
            # 保存当前版本
            self.save_current_version()
        else:
            log.warning("脚本 {0}, 版本【{1}】上传文件失败，返回结果: {2}".format(script_name, ver_no, msg))
        set_global_var("ResultMsg", msg, False)

    def script_file_r_click(self, script_name, ver_no, file_name, operate):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        :param file_name: 脚本文件名
        :param operate: 右键
        """
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)
        page_wait()
        # 焦点定位到文件名元素上
        file_element = self.browser.find_element(
            By.XPATH, "//*[@id='file_tree']//*[contains(text(),'{0}')]".format(file_name))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", file_element)
        # 左键单击脚本文件名，展示脚本内容
        file_element.click()
        page_wait()
        sleep(1)
        # 指定脚本文件右键
        action = ActionChains(self.browser)
        action.context_click(file_element).perform()
        sleep(1)

        if operate == "设置为主脚本":
            self.browser.find_element(By.XPATH, "//*[@id='setMainScriptBtn']//*[text()='设置为主脚本']").click()
            log.info("执行设置主脚本操作")

            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("确认要设置{0}为主类吗".format(file_name), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("脚本 {0}, 版本【{1}】设置主脚本: {2} 成功".format(script_name, ver_no, file_name))

                    self.browser.switch_to.frame(
                        self.browser.find_element(By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=edit')]"))
                    # 保存当前版本
                    self.save_current_version()
                else:
                    log.warning("脚本 {0}, 版本【{1}】右键文件 {2} 操作失败，返回结果: {3}".format(
                        script_name, ver_no, file_name, msg))
                set_global_var("ResultMsg", msg, False)
            else:
                raise "脚本文件名右键设置主脚本失败，弹出框返回: {0}".format(msg)

        elif operate == "删除脚本":
            self.browser.find_element(By.XPATH, "//*[@id='delScriptBtn']//*[text()='删除脚本']").click()
            log.info("执行删除脚本文件操作")

            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}文件吗".format(file_name), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("脚本 {0}, 版本【{1}】删除脚本: {2} 成功".format(script_name, ver_no, file_name))

                    self.browser.switch_to.frame(
                        self.browser.find_element(By.XPATH, "//iframe[contains(@src,'scriptCfgEdit.html?type=edit')]"))
                    # 保存当前版本
                    self.save_current_version()
                else:
                    log.warning(
                        "脚本 {0}, 版本【{1}】右键文件 {2} 操作失败，返回结果: {3}".format(script_name, ver_no, file_name, msg))
                set_global_var("ResultMsg", msg, False)
            else:
                raise "脚本文件名右键删除脚本失败，弹出框返回: {0}".format(msg)

        elif operate == "下载脚本":
            log.info("执行下载脚本文件操作")
            self.browser.find_element(By.XPATH, "//*[@onclick='downloadFile()']//*[text()='下载脚本']").click()
            log.info("脚本 {0}, 版本【{1}】下载脚本文件: {2}".format(script_name, ver_no, file_name))
        else:
            raise KeyError("脚本文件名右键操作值: {0} 不支持".format(operate))

    def update_script_content(self, script_name, ver_no, file_name, content):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        :param file_name: 脚本文件名
        :param content: 脚本内容
        """
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        # 焦点定位到文件名元素上
        file_element = self.browser.find_element(
            By.XPATH, "//*[@id='file_tree']//*[contains(text(),'{0}')]".format(file_name))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", file_element)
        # 左键单击脚本文件名，展示脚本内容
        file_element.click()
        page_wait()
        full_screen = self.browser.find_element(By.XPATH, "//*[@id='full_btn']//*[text()='全屏']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", full_screen)
        full_screen.click()

        # 切换到全屏修改脚本内容iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'editCodeScriptWin.html')]")))
        sleep(1)

        # 脚本内容操作待补充
        log.info("脚本文件更新内容: {0}".format(content))
        # TODO

        # 保存
        self.browser.find_element(By.XPATH, "//*[@id='saveFileContent']//*[text()='保存']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("更新脚本内容成功")
        else:
            log.warning("更新脚本内容失败，返回结果: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def save_current_version(self):
        # 需要先点击版本后开始操作

        # 焦点定位到文件名元素上
        element = self.browser.find_element(By.XPATH, "//*[@onclick=\"saveVersionParamCfg('0')\"]//*[text()='保存当前版本']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        element.click()

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存当前版本成功")
        else:
            log.warning("保存当前版本失败，返回结果: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def save_new_version(self):
        # 需要先点击版本后开始操作

        # 焦点定位到文件名元素上
        element = self.browser.find_element(By.XPATH, "//*[@onclick=\"saveVersionParamCfg('1')\"]//*[text()='保存新版本']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        element.click()

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存新版本成功")
        else:
            log.warning("保存新版本失败，返回结果: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def test(self, script_name, ver_no):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        """
        log.info("开始测试脚本")
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        # 点击测试按钮
        self.browser.find_element(By.XPATH, "//*[@id='testJava()']//*[text()='测试']").click()
        alert = BeAlertBox(back_iframe=True, timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("编译成功"):
            log.info("脚本 {0}, 版本[{1}] 测试成功".format(script_name, ver_no))
        else:
            log.warning("脚本 {0}, 版本[{1}] 测试失败，测试返回结果: {2}".format(script_name, ver_no, msg))
        set_global_var("ResultMsg", msg, False)

    def delete_version(self, script_name, ver_no=1):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        """
        log.info("开始删除版本")
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        self.browser.find_element(By.XPATH, "//*[@onclick='deleteVersion()']//*[text()='删除']").click()
        log.info("执行删除版本操作")

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除版本号【{0}】吗".format(ver_no), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("脚本 {0}, 版本【{1}】删除成功".format(script_name, ver_no))
            else:
                log.warning("脚本 {0}, 版本【{1}】删除失败，返回结果: {2}".format(script_name, ver_no, msg))
        else:
            log.warning("脚本 {0}, 版本【{1}】删除失败，返回结果: {2}".format(script_name, ver_no, msg))
        set_global_var("ResultMsg", msg, False)

    def download_version(self, script_name, ver_no=1):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        """
        log.info("开始下载版本")
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)
        self.browser.find_element(By.XPATH, "//*[@onclick='downloadVersion()']//*[text()='下载']").click()
        sleep(3)
        log.info("已下载脚本{0}, 版本[{1}]".format(script_name, ver_no))

    def submit_for_approval(self, script_name, ver_no):
        """
        :param script_name: 脚本名称
        :param ver_no: 版本号
        """
        log.info("开始提交版本审批")
        # 需要先点击版本后开始操作
        self.choose_version(script_name, ver_no)

        self.browser.find_element(By.XPATH, "//*[@onclick=\"auditVersion('{0}')\"]".format(ver_no)).click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("提交审批", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("版本【{0}】提交审批返回：{1}".format(ver_no, msg))
                log.info("等待自动审批...")
                # sleep(5)
                # self.browser.find_element(By.XPATH, 
                #     "//*[@id='scriptVersionRefresh']//*[contains(@class,'reload')]").click()
            else:
                log.warning("版本【{0}】提交审批失败，失败提示: {1}".format(ver_no, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(ver_no, msg))
        set_global_var("ResultMsg", msg, False)

    def delete(self, script_name):
        """
        :param script_name: 脚本名称
        """
        log.info("开始删除数据")
        self.search(query={"脚本名称": script_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(script_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(script_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(script_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(script_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, script_name, fuzzy_match=False):
        """
        :param script_name: 脚本名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='scriptName']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='scriptName']/preceding-sibling::input").send_keys(script_name)
        self.browser.find_element(By.XPATH, "//*[contains(@data-options,'icon-search-primary')]").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='scriptName']/*[contains(@class,'scriptName') and starts-with(text(),'{0}')]".format(
                    script_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='scriptName']/*[contains(@class,'scriptName') and text()='{0}']".format(script_name))
        if len(record_element) > 0:
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
                                By.XPATH, "//*[@field='scriptName']/*[contains(@class,'scriptName') and starts-with(text(),'{0}')]".format(
                                    script_name))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(script_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
