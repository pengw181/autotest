# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午5:01

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from client.page.func.alertBox import BeAlertBox
from client.page.func.pageMaskWait import page_wait
from client.page.func.positionPanel import getPanelXpath
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class Proxy:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("常用信息管理-代理管理")
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/proxyCfg.html')]"))
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

        # 代理名称
        if query.__contains__("代理名称"):
            proxy_name = query.get("代理名称")
            self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input[1]").send_keys(
                proxy_name)
            select_item = proxy_name

        # 代理服务器/端口
        if query.__contains__("代理服务器/端口"):
            proxy_ip = query.get("代理服务器/端口")
            self.browser.find_element(By.XPATH, "//*[@name='proxyIP']/preceding-sibling::input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@name='proxyIP']/preceding-sibling::input[1]").send_keys(
                proxy_ip)

        #  是否有效
        if query.__contains__("是否有效"):
            is_alive = query.get("是否有效")
            self.browser.find_element(By.XPATH, "//*[@name='isAlive']/preceding-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'combobox') and text()='{0}']".format(is_alive)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
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
                        By.XPATH, "//*[@field='proxyName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

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
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
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

    def update(self, proxy, proxy_name, ip, port, username, pwd, protocol, enable, data_type):
        """
        :param proxy: 代理名称
        :param proxy_name: 代理名称
        :param ip: 代理服务器
        :param port: 代理端口
        :param username: 代理用户名
        :param pwd: 代理密码
        :param protocol: 代理协议
        :param enable: 是否有效
        :param data_type: 数据类型
        """
        self.search(query={"代理名称": proxy}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

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

    def delete(self, proxy_name):
        """
        :param proxy_name: 代理名称
        """
        self.search(query={"代理名称": proxy_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(proxy_name), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("{0} 删除成功".format(proxy_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(proxy_name, msg))
        elif alert.title_contains("数据存在引用，不能删除"):
            log.warning("{0} 删除失败，失败提示: {1}".format(proxy_name, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(proxy_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, proxy_name, fuzzy_match=False):
        """
        :param proxy_name: 代理名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='proxyName']/preceding-sibling::input").send_keys(proxy_name)
        self.browser.find_element(By.XPATH, "//*[@id='btn']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and starts-with(text(),'{0}')]".format(
                    proxy_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and text()='{0}']".format(proxy_name))
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
                                By.XPATH, "//*[@field='proxyName']/*[contains(@class,'proxyName') and starts-with(text(),'{0}')]".format(
                                    proxy_name))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(proxy_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break

        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
