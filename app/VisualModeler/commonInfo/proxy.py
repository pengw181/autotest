# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午5:01

from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from time import sleep
from common.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


class Proxy:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("常用信息管理-代理管理")
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/proxyCfg.html')]"))
        page_wait()
        sleep(1)

    def search(self, proxy_name, ip_port, enable):
        """
        :param proxy_name: 代理名称
        :param ip_port: 代理服务器/端口
        :param enable: 是否有效
        """
        # 代理名称
        if proxy_name:
            self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").send_keys(proxy_name)
            log.info("设置代理服务器/端口")

        # 代理服务器/端口
        if ip_port:
            self.browser.find_element(By.XPATH, "//*[@name='proxyIP']/preceding-sibling::input").send_keys(ip_port)
            log.info("设置代理服务器/端口")

        # 是否有效
        if enable:
            self.browser.find_element(By.XPATH, "//*[@name='isAlive']/preceding-sibling::input").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'_combobox_') and text()='{0}']".format(enable)).click()
            log.info("设置是否有效")

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()

    def choose(self, proxy_name):
        """
        :param proxy_name: 代理名称
        """
        self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").send_keys(proxy_name)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        self.browser.find_element(By.XPATH, "//*[contains(@id,'proxyCfg')]//*[text()='{0}']".format(proxy_name)).click()
        log.info("已选择: {0}".format(proxy_name))

    def add(self, proxy_name, ip, port, username, pwd, protocol, enable, data_type):
        """
        :param proxy_name: 代理名称
        :param ip: 代理服务器
        :param port: 代理端口
        :param username: 代理用户名
        :param pwd: 代理密码
        :param protocol: 代理协议
        :param enable: 是否有效
        :param data_type: 数据类型
        """
        self.browser.find_element(By.XPATH, "//*[text()='添加']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'proxyCfgEdit.html?type=add')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='proxyName']/preceding-sibling::input")))

        self.proxy_page(proxy_name=proxy_name, ip=ip, port=port, username=username, pwd=pwd, protocol=protocol,
                        enable=enable, data_type=data_type)
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(proxy_name))
        else:
            log.warning("{0} 添加失败，失败原因：{1}".format(proxy_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, proxy_name, ip, port, username, pwd, protocol, enable, data_type):
        """
        :param obj: 代理名称
        :param proxy_name: 代理名称
        :param ip: 代理服务器
        :param port: 代理端口
        :param username: 代理用户名
        :param pwd: 代理密码
        :param protocol: 代理协议
        :param enable: 是否有效
        :param data_type: 数据类型
        """
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'proxyCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='proxyName']/preceding-sibling::input")))

            self.proxy_page(proxy_name=proxy_name, ip=ip, port=port, username=username, pwd=pwd, protocol=protocol,
                            enable=enable, data_type=data_type)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 修改成功".format(proxy_name))
            else:
                log.warning("{0} 修改失败，失败原因：{1}".format(proxy_name, msg))
            set_global_var("ResultMsg", msg, False)

    def proxy_page(self, proxy_name, ip, port, username, pwd, protocol, enable, data_type):
        """
        :param proxy_name: 代理名称
        :param ip: 代理服务器
        :param port: 代理端口
        :param username: 代理用户名
        :param pwd: 代理密码
        :param protocol: 代理协议
        :param enable: 是否有效
        :param data_type: 数据类型
        """
        # 代理名称
        if proxy_name:
            self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").send_keys(proxy_name)
            log.info("设置代理名称: {0}".format(proxy_name))

        # 代理服务器
        if ip:
            self.browser.find_element(By.XPATH, "//*[@name='proxyIp']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyIp']/preceding-sibling::input").send_keys(ip)
            log.info("设置代理名称: {0}".format(ip))

        # 代理端口
        if port:
            self.browser.find_element(By.XPATH, "//*[@name='proxyPort']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyPort']/preceding-sibling::input").send_keys(port)
            log.info("设置代理端口: {0}".format(port))

        # 代理用户名
        if username:
            self.browser.find_element(By.XPATH, "//*[@name='proxyUser']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyUser']/preceding-sibling::input").send_keys(username)
            log.info("设置代理用户名: {0}".format(username))

        # 代理密码
        if pwd:
            try:
                # 判断是否是修改密码
                self.browser.find_element(
                    By.XPATH, "//*[@id='proxyPwd']/following-sibling::span//a[contains(@class, 'edit')]").click()
            except NoSuchElementException:
                pass
            self.browser.find_element(By.XPATH, "//*[@name='proxyPwd']/preceding-sibling::input").send_keys(pwd)
            sleep(1)
            log.info("设置代理密码: {0}".format(pwd))

        # 代理协议
        if protocol:
            self.browser.find_element(By.XPATH, "//*[@name='proxyType']/preceding-sibling::input").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'_combobox_') and text()='{0}']".format(protocol)).click()
            log.info("设置代理协议: {0}".format(protocol))

        # 是否有效
        js = 'return $("#isAlive")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【是否有效】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = self.browser.find_element(By.XPATH, "//*[@for='isAlive']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)
        if enable == "有效":
            if not status:
                enable_click.click()
            log.info("勾选【是否有效】")
        else:
            if status:
                enable_click.click()
            log.info("取消勾选【是否有效】")

        # 数据类型
        if data_type:
            self.browser.find_element(By.XPATH, "//*[@name='dataTypeId']/preceding-sibling::input").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'dataTypeId_') and text()='{0}']".format(data_type)).click()
            log.info("设置数据类型: {0}".format(data_type))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitBtn']//*[text()='提交']").click()

    def delete(self, obj):
        """
        :param obj: 代理名称
        """
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: 代理名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and starts-with(text(),'{0}')]".format(obj))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and text()='{0}']".format(obj))
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
                                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and starts-with(text(),'{0}')]".format(obj))
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
                    break

        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
