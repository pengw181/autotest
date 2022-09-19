# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:35

from selenium.common.exceptions import NoSuchElementException
from common.page.func.alertBox import BeAlertBox
from time import sleep
from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


class Process:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("流程编辑器-流程配置")
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/gooflow/queryProcessInfo.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
        page_wait()
        sleep(1)

    def add(self, process_name, field, process_type, exec_mode, process_desc, advance_set):
        """
        :param process_name: 流程名称
        :param field: 专业领域，数组
        :param process_type: 流程类型
        :param process_desc: 流程说明
        :param exec_mode: 执行模式
        :param advance_set:  高级配置
        """
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='添加']")))
        self.browser.find_element(By.XPATH, "//*[text()='添加']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/gooflow/processInfoEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='process_name']/preceding-sibling::input")))

        self.process_page(process_name=process_name, field=field, process_type=process_type, exec_mode=exec_mode,
                          process_desc=process_desc, advance_set=advance_set)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 添加成功".format(process_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(process_name, msg))
        set_global_var("ResultMsg", msg, False)

    def choose(self, process_name):
        try:
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").send_keys(process_name)
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[contains(@data-dg-query,'process_info_tab')]//*[text()='查询']").click()
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'process_info')]/*[@field='processName']//*[text()='{0}']".format(
                    process_name)).click()
            log.info("选择流程：{0}".format(process_name))
        except NoSuchElementException:
            raise Exception("所选流程不存在, 流程名称: {0}".format(process_name))

    def update(self, obj, process_name, field, exec_mode, process_desc, advance_set):
        """
        :param obj: 流程名称
        :param process_name: 流程名称
        :param field: 专业领域，数组
        :param process_desc: 流程说明
        :param exec_mode: 执行模式
        :param advance_set: 高级配置
        """
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/html/gooflow/processInfoEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='process_name']/preceding-sibling::input")))

        self.process_page(process_name=process_name, field=field, exec_mode=exec_mode, process_desc=process_desc,
                          advance_set=advance_set)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("数据 {0} 修改成功".format(obj))
        else:
            log.warning("数据 {0} 修改失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def process_page(self, process_name, field,  process_desc, advance_set, process_type=None, exec_mode=None):
        """
        :param process_name: 流程名称
        :param field: 专业领域，数组
        :param process_type: 流程类型，不可修改
        :param process_desc: 流程说明
        :param exec_mode: 执行模式，3.2新增功能
        :param advance_set:  高级配置
        """
        # 流程名称
        if process_name:
            self.browser.find_element(By.XPATH, "//*[@name='process_name']/preceding-sibling::input").clear()
            self.browser.find_element(
                By.XPATH, "//*[@name='process_name']/preceding-sibling::input").send_keys(process_name)
            log.info("设置流程名称: {0}".format(process_name))

        # 专业领域
        if field:
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            page_wait()
            sleep(1)
            # 判断当前是否已经选择了专业领域，如果是，则先取消
            choose_field_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'temp_type_id') and contains(@class,'selected')]")
            if len(choose_field_list) > 0:
                for cf in choose_field_list:
                    cf.click()
            # 依次选择专业领域
            for f in field:
                field_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'temp_type_id') and text()='{0}']".format(f))
                for element in field_elements:
                    if element.is_displayed():
                        element.click()
                        break
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 流程类型
        if process_type:
            combobox = self.browser.find_element(By.XPATH, "//*[@name='processTypeId']/preceding-sibling::input")
            self.browser.execute_script("arguments[0].click();", combobox)
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'processTypeId') and text()='{0}']".format(process_type)).click()
            log.info("设置流程类型: {0}".format(process_type))

        # 执行模式
        if exec_mode:
            self.browser.find_element(By.XPATH, "//*[@id='execMode']/following-sibling::span[1]//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'execMode') and text()='{0}']".format(exec_mode)).click()
            log.info("设置执行模式: {0}".format(exec_mode))

        # 流程说明
        if process_desc:
            self.browser.find_element(By.XPATH, "//*[@name='re_mark']/preceding-sibling::textarea").clear()
            self.browser.find_element(
                By.XPATH, "//*[@name='re_mark']/preceding-sibling::textarea").send_keys(process_desc)
            log.info("设置流程说明: {0}".format(process_desc))

        # 高级配置
        if advance_set:
            self.advance_set(exception_end=advance_set.get("节点异常终止流程"), process_var=advance_set.get("自定义流程变量"),
                             err_output=advance_set.get("输出异常"))

        # 提交
        self.browser.find_element(By.XPATH, "//*[text()='提交']").click()

    def advance_set(self, exception_end=None, process_var=None, err_output=None):
        # 流程高级配置
        """
        :param exception_end: 节点异常终止流程
        :param process_var: 自定义流程变量，字典
        :param err_output: 输出异常，字典

        {
            "节点异常终止流程": "是",
            "自定义流程变量": {
                "状态": "开启",
                "参数列表": {
                    "时间": "2020-10-20###必填",
                    "地点": "广州###",
                    "名字": "pw###必填"
                }
            },
            "输出异常": {
                "状态": "关闭",
                "告警方式": "邮件",
                "发件人": "pw@henghaodata.com",
                "收件人": "pw@henghaodata.com",
                "抄送人": "pw@henghaodata.com",
                "主题": "pw自动化流程异常",
                "正文": "pw自动化流程运行异常"
            }
        }
        """

        # 节点异常终止流程
        js = 'return $("#isNodeExpEnd")[0].checked;'
        status = self.browser.execute_script(js)
        # log.info("【节点异常终止流程】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = self.browser.find_element(By.XPATH, "//*[@id='isNodeExpEnd']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if exception_end == "是":
            # 点击节点异常终止流程
            if not status:
                enable_click.click()
            log.info("勾选【节点异常终止流程】")
        elif exception_end == "否":
            if status:
                enable_click.click()
            log.info("取消勾选【节点异常终止流程】")
        else:
            pass

        # 自定义流程变量
        if process_var:
            self.conf_process_var(enable_status=process_var.get("状态"), var_param=process_var.get("参数列表"))

        # 输出异常
        if err_output:
            self.output_err(enable_status=err_output.get("状态"), alarm_type=err_output.get("告警方式"),
                            sender=err_output.get("发件人"), receiver=err_output.get("收件人"),
                            cc=err_output.get("抄送人"), theme=err_output.get("主题"), content=err_output.get("正文"))

    def conf_process_var(self, enable_status, var_param):
        """
        :param enable_status: 状态，开启/关闭
        :param var_param: 参数列表，字典
        """
        # 获取勾选状态
        status = self.browser.find_element(By.XPATH, "//*[@id='isProcessVarConfig']").get_attribute("checked")
        # log.info("【自定义流程变量】勾选状态: {0}".format(status))

        if enable_status == "开启":
            if not status:
                # 当前未开启，勾选
                self.browser.find_element(By.XPATH, "//*[@id='isProcessVarConfig']").click()
                log.info("勾选【自定义流程变量】")
                current_row_num = 0
            else:
                # 获取当前行号
                current_row_num = 1
                flag = True
                while flag:
                    try:
                        self.browser.find_element(
                            By.XPATH, "//*[@id='relaCol{}']/following-sibling::span/input".format(current_row_num))
                        current_row_num += 1
                    except NoSuchElementException:
                        current_row_num -= 1
                        flag = False

            # 判断流程变量是否已存在，存在则更新，否则添加
            for param_key, param_value in var_param.items():
                tmp = str(param_value).split("###", 1)
                default_value = tmp[0]
                must_fill_flag = tmp[1]

                try:
                    # 判断变量是否已存在
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/*[@value='{}']".format(param_key))

                    # 输入默认值
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/*[@value='{}']/../../following-sibling::div[1]/span/input[1]".format(
                            param_key)).clear()
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/*[@value='{}']/../../following-sibling::div[1]/span/input[1]".format(
                            param_key)).send_keys(default_value)

                    # 是否必填
                    must_fill_ele = self.browser.find_element(
                        By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/*[@value='{}']/../../following-sibling::label[1]/input".format(
                            param_key))
                    must_fill_id = must_fill_ele.get_attribute("id")
                    js = 'return $("#{}")[0].checked;'.format(must_fill_id)
                    status = self.browser.execute_script(js)
                    # log.info("{0}【必填】勾选状态: {1}".format(param_key, status))
                    # 聚焦元素
                    enable_click = self.browser.find_element(By.XPATH, "//*[@id='{}']".format(must_fill_id))
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

                    if must_fill_flag:
                        if not status:
                            enable_click.click()
                        # log.info("{}勾选【必填】".format(param_key))
                    else:
                        if status:
                            enable_click.click()
                        # log.info("{}取消勾选【必填】".format(param_key))
                    log.info("更新流程变量: {0}".format(param_key))
                except NoSuchElementException:
                    # 变量不存在，添加
                    if current_row_num > 0:
                        # 如果是在已有变量情况下添加，点击当前最后一行的添加按钮
                        self.browser.find_element(
                            By.XPATH, "//*[@id='relaItem{}']//*[contains(@onclick, 'addOutRelaItem')]".format(
                                current_row_num)).click()
                        new_row_num = current_row_num + 1
                    else:
                        # 如果是全新添加，开启自定义流程变量会自动添加一行，不需要点添加
                        new_row_num = 1

                    # 输入参数名
                    self.browser.find_element(
                        By.XPATH, "//*[@id='relaCol%d']/following-sibling::span/input" % new_row_num).send_keys(param_key)

                    # 输入默认值
                    self.browser.find_element(
                        By.XPATH, "//*[@id='defaultVal%d']/following-sibling::span/input" % new_row_num).send_keys(
                        default_value)

                    # 是否必填
                    if must_fill_flag:
                        self.browser.find_element(By.XPATH, "//*[@id='must_fill_{0}']".format(new_row_num)).click()
                    log.info("添加流程变量: {0}".format(param_key))

                    # 添加一行之后，需要将最大行号加1
                    current_row_num = new_row_num
                    # new_row_num += 1

            # 删除多余的变量
            elements = self.browser.find_elements(By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/input[2]")
            if len(elements) == 0:
                # 当前未配置流程变量
                pass
            else:
                # 当前有配置流程变量，删除不在参数列表中的变量
                for element in elements:
                    current_process_var = element.get_attribute("value")
                    if not var_param.__contains__(current_process_var):
                        self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'relaCol')]/following-sibling::span/*[@value='{}']/../../following-sibling::a[2]".format(
                                current_process_var)).click()
                        log.info("删除流程变量: {}".format(current_process_var))
                        sleep(1)

            log.info("自定义流程变量配置完成")
        elif enable_status == "关闭":
            if not status:
                pass
            else:
                self.browser.find_element(By.XPATH, "//*[@id='isProcessVarConfig']").click()
                log.info("取消勾选【自定义流程变量】")
        else:
            raise KeyError("【自定义流程变量】状态只支持：开启/关闭")

    def output_err(self, enable_status, alarm_type, sender, receiver, cc, theme, content):
        """
        :param enable_status: 状态，开启/关闭
        :param alarm_type: 告警方式
        :param sender: 发件人
        :param receiver: 收件人，数组
        :param cc: 抄送人，数组
        :param theme: 主题
        :param content: 正文
        """
        # 获取勾选状态
        status = self.browser.find_element(By.XPATH, "//*[@id='isOutputError']").get_attribute("checked")
        # log.info("【输出异常】勾选状态: {0}".format(status))
        if enable_status == "开启":
            if not status:
                self.browser.find_element(By.XPATH, "//*[@id='isOutputError']").click()
                log.info("勾选【输出异常】")
            else:
                enable_output_err = self.browser.find_element(By.XPATH, "//*[@id='isOutputError']")
                enable_output_err.click()
                enable_output_err.click()
                # action = ActionChains(self.browser)
                # action.double_click(enable_output_err).perform()

            # 聚焦元素
            output_target = self.browser.find_element(
                By.XPATH, "//*[contains(text(), '发件人')]/../following-sibling::div[1]/div/span")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", output_target)
            sleep(1)

            # 告警方式
            if alarm_type:
                pass

            # 发件人
            if sender:
                self.browser.find_element(
                    By.XPATH, "//*[contains(text(), '发件人')]/../following-sibling::div[1]/div/span").click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id, 'sender_') and text()='{0}']".format(sender)).click()
                log.info("设置发件人: {0}".format(sender))

            # 收件人
            if receiver:
                self.browser.find_element(
                    By.XPATH, "//*[contains(text(), '收件人')]/../following-sibling::div[1]/div/span").click()
                # 将已勾选的勾掉
                while True:
                    try:
                        selected = self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'recipients') and contains(@class,'selected')]")
                        selected.click()
                    except NoSuchElementException:
                        break
                for email in receiver:
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id, 'recipients') and text()='{0}']".format(email)).click()
                self.browser.find_element(
                    By.XPATH, "//*[contains(text(), '收件人')]/../following-sibling::div[1]/div/span").click()
                log.info("设置收件人: {0}".format(",".join(receiver)))

            # 抄送人
            if cc:
                self.browser.find_element(By.XPATH, "//*[@id='copySenders']/following-sibling::span/input").click()
                # 将已勾选的勾掉
                while True:
                    try:
                        selected = self.browser.find_element(
                            By.XPATH, "//*[contains(@id,'copySenders_') and contains(@class,'selected')]")
                        selected.click()
                    except NoSuchElementException:
                        break
                for email in cc:
                    self.browser.find_element(
                        By.XPATH, "//*[contains(@id, 'copySenders_') and text()='{0}']".format(email)).click()
                self.browser.find_element(By.XPATH, "//*[@id='copySenders']/following-sibling::span/input").click()
                log.info("设置抄送人: {0}".format(",".join(cc)))

            # 主题
            if theme:
                self.browser.find_element(By.XPATH, "//*[@id='theme']/following-sibling::span/input").clear()
                self.browser.find_element(By.XPATH, "//*[@id='theme']/following-sibling::span/input").send_keys(theme)
                log.info("设置主题: {0}".format(theme))

            # 正文
            if content:
                self.browser.find_element(By.XPATH, "//*[@id='mailContent']/following-sibling::span/textarea").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='mailContent']/following-sibling::span/textarea").send_keys(content)
                log.info("设置正文: {0}".format(content))
        elif enable_status == "关闭":
            if not status:
                pass
            else:
                self.browser.find_element(By.XPATH, "//*[@id='isOutputError']").click()
                log.info("取消勾选【输出异常】")
        else:
            raise KeyError("【输出异常】状态只支持：开启/关闭")

    def delete(self, obj):
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        # 用于清除数据，在测试之前执行, 使用process_name开头模糊查询
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
        self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[contains(@data-dg-query,'process_info_tab')]//*[text()='查询']").click()
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='processName']/*[contains(@class,'processName')]/*[starts-with(text(),'{0}')]".format(obj))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='processName']/*[contains(@class,'processName')]/*[text()='{0}']".format(obj))
        if len(record_element) > 0:
            log.info("根据名称查到{}条满足条件数据".format(len(record_element)))
            exist_data = True

            while exist_data:
                pe = record_element[0]
                pe.click()
                search_result = pe.text
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element(By.XPATH, "//*[text()='删除']").click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除{0}流程吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    # 删除流程是否有子流程被其它流程引用
                    try:
                        # 等待页面加载
                        page_wait()
                        self.browser.switch_to.frame(
                            self.browser.find_element(
                                By.XPATH, "//iframe[contains(@src,'../gooflow/deleteChildProcessInfos.html')]"))
                        self.browser.find_element(By.XPATH, "//*[@onclick='delProcessAndChilds()']//*[text()='提交']").click()
                        # 返回上层iframe
                        self.browser.switch_to.parent_frame()
                        alert = BeAlertBox(back_iframe=False)
                        alert.click_ok()
                    except NoSuchElementException:
                        pass
                    finally:
                        alert = BeAlertBox(back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("成功"):
                            log.info("{0} 删除成功".format(search_result))
                            page_wait()
                            if fuzzy_match:
                                # 重新获取页面查询结果
                                record_element = self.browser.find_elements(
                                    By.XPATH, "//*[@field='processName']/*[contains(@class,'processName')]/*[starts-with(text(),'{0}')]".format(
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
                    log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
                    set_global_var("ResultMsg", msg, False)

        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
