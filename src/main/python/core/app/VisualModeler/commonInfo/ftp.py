# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:24

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class FTP:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        DoctorWho().choose_menu("常用信息管理-远程FTP服务器管理")
        self.browser.switch_to.frame(
            self.browser.find_element(
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/ftpServerCfg.html')]"))
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

        # 服务器名称
        if query.__contains__("服务器名称"):
            server_name = query.get("服务器名称")
            self.browser.find_element(By.XPATH, "//*[@id='serverName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='serverName']/following-sibling::span/input[1]").send_keys(
                server_name)
            select_item = server_name

        # 服务器IP
        if query.__contains__("服务器IP"):
            server_ip = query.get("服务器IP")
            self.browser.find_element(By.XPATH, "//*[@id='serverIP']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='serverIP']/following-sibling::span/input[1]").send_keys(
                server_ip)

        # 服务器端口
        if query.__contains__("服务器端口"):
            server_port = query.get("服务器端口")
            self.browser.find_element(By.XPATH, "//*[@id='serverPort']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='serverPort']/following-sibling::span/input[1]").send_keys(
                server_port)

        # 用户名
        if query.__contains__("用户名"):
            user_name = query.get("用户名")
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").send_keys(
                user_name)

        #  服务器类型
        if query.__contains__("服务器类型"):
            server_type = query.get("服务器类型")
            self.browser.find_element(By.XPATH, "//*[@id='serverType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[contains(@id,'serverType') and text()='{0}']".format(server_type)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='btn']").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
            return
        if need_choose:
            if select_item:
                try:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='serverName']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, server_name, ip, port, username, pwd, server_type, encoding, data_type):
        """
        :param server_name: 服务器名称
        :param ip: 服务器IP
        :param port: 服务器端口
        :param username: 用户名
        :param pwd: 密码
        :param server_type: 服务器类型
        :param encoding: 服务器编码
        :param data_type: 数据类型
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'ftpServerCfgEdit.html?type=save')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='serverName']/preceding-sibling::input")))

        self.ftp_page(server_name=server_name, ip=ip, port=port, username=username, pwd=pwd, server_type=server_type,
                      encoding=encoding, data_type=data_type)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='submitBtn']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("数据 {0} 添加成功".format(server_name))
        else:
            log.warning("数据 {0} 添加失败，失败提示: {1}".format(server_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, ftp, server_name, ip, port, username, pwd, server_type, encoding, data_type):
        """
        :param ftp: 服务器名称
        :param server_name: 服务器名称
        :param ip: 服务器IP
        :param port: 服务器端口
        :param username: 用户名
        :param pwd: 密码
        :param server_type: 服务器类型
        :param encoding: 服务器编码
        :param data_type: 数据类型
        """
        log.info("开始修改数据")
        self.search(query={"服务器名称": ftp}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'ftpServerCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='serverName']/preceding-sibling::input")))

            self.ftp_page(server_name=server_name, ip=ip, port=port, username=username, pwd=pwd, server_type=server_type,
                          encoding=encoding, data_type=data_type)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='submitBtn']").click()
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 修改成功".format(ftp))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(ftp, msg))
            gbl.temp.set("ResultMsg", msg)

    def ftp_page(self, server_name, ip, port, username, pwd, server_type, encoding, data_type):
        """
        :param server_name: 服务器名称
        :param ip: 服务器IP
        :param port: 服务器端口
        :param username: 用户名
        :param pwd: 密码
        :param server_type: 服务器类型
        :param encoding: 服务器编码
        :param data_type: 数据类型
        """
        # 服务器名称
        if server_name:
            self.browser.find_element(By.XPATH, "//*[@name='serverName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='serverName']/preceding-sibling::input").send_keys(
                server_name)
            log.info("设置服务器名称: {0}".format(server_name))

        # 服务器IP
        if ip:
            self.browser.find_element(By.XPATH, "//*[@name='serverIp']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='serverIp']/preceding-sibling::input").send_keys(ip)
            log.info("设置服务器IP: {0}".format(ip))

        # 服务器端口
        if port:
            self.browser.find_element(By.XPATH, "//*[@name='serverPort']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='serverPort']/preceding-sibling::input").send_keys(port)
            log.info("设置服务器端口: {0}".format(port))

        # 用户名
        if username:
            self.browser.find_element(By.XPATH, "//*[@name='serverUser']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='serverUser']/preceding-sibling::input").send_keys(username)
            log.info("设置用户名: {0}".format(username))

        # 密码
        if pwd:
            try:
                # 判断是否是修改密码
                self.browser.find_element(
                    By.XPATH, "//*[@id='serverPwd']/following-sibling::span//a[contains(@class, 'edit')]").click()
            except NoSuchElementException:
                pass
            self.browser.find_element(By.XPATH, "//*[@name='serverPwd']/preceding-sibling::input").send_keys(pwd)
            sleep(1)
            log.info("设置密码: {0}".format(pwd))

        # 服务器类型
        if server_type:
            self.browser.find_element(By.XPATH, "//*[@name='serverType']/preceding-sibling::input").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'serverType') and text()='{0}']".format(server_type)).click()
            log.info("设置服务器类型: {0}".format(server_type))

        # 服务器编码
        if encoding:
            self.browser.find_element(By.XPATH, "//*[@name='serverEncoding']/preceding-sibling::input").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'serverEncoding') and text()='{0}']".format(encoding)).click()
            log.info("设置服务器名称: {0}".format(encoding))

        # 数据类型
        if data_type:
            self.browser.find_element(By.XPATH, "//*[@name='dataTypeId']/preceding-sibling::input").click()
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.visibility_of_element_located((
                By.XPATH, "//*[contains(@id,'dataTypeId') and text()='{0}']".format(data_type))))
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'dataTypeId') and text()='{0}']".format(data_type)).click()
            log.info("设置数据类型: {0}".format(data_type))

    def test(self, server_name):
        """
        :param server_name: 服务器名称
        """
        log.info("开始测试数据")
        self.search(query={"服务器名称": server_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'ftpServerCfgEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='serverName']/preceding-sibling::input")))

            self.browser.find_element(By.XPATH, "//*[@id='testBtn']").click()
            alert = BeAlertBox(timeout=30)
            msg = alert.get_msg()
            if alert.title_contains("测试成功"):
                log.info("{0} 测试成功".format(server_name))
            else:
                log.warning("{0} 测试失败，测试返回结果: {1}".format(server_name, msg))
            gbl.temp.set("ResultMsg", msg)

    def delete(self, server_name):
        """
        :param server_name: 服务器名称
        """
        log.info("开始删除数据")
        self.search(query={"服务器名称": server_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='delBtn']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(server_name), auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(server_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(server_name, msg))
        elif alert.title_contains("数据存在引用，不能删除"):
            log.warning("{0} 删除失败，失败提示: {1}".format(server_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(server_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, server_name, fuzzy_match=False):
        """
        :param server_name: 服务器名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.search(query={"服务器名称": server_name}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='serverName']//*[starts-with(text(),'{0}')]".format(server_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='serverName']//*[text()='{0}']".format(server_name))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

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
                            By.XPATH, "//*[@field='serverName']//*[starts-with(text(),'{0}')]".format(server_name))
                        if len(record_element) == 0:
                            # 查询结果为空,修改exist_data为False，退出循环
                            log.info("数据清理完成")
                            exist_data = False
                    else:
                        break
                else:
                    raise Exception("删除数据时出现未知异常: {0}".format(msg))
            else:
                # 无权操作
                log.warning("{0} 清理失败，失败提示: {1}".format(server_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
