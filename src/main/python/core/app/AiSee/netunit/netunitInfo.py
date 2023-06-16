# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:03

import json
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_menu, choose_domain
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class NetUnit(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="网元信息(自身)")

        # 切到网元信息配置页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/netunitInfo.html')]")))
        page_wait(timeout=120)
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

        # 网元名称
        if query.__contains__("网元名称"):
            netunit_name = query.get("网元名称")
            self.browser.find_element(By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='netunitName']/following-sibling::span/input[1]").send_keys(
                netunit_name)
            select_item = netunit_name

        # 网元类型
        if query.__contains__("网元类型"):
            level_type = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(level_type)).click()

        # 网元IP
        if query.__contains__("网元IP"):
            netunit_ip = query.get("网元IP")
            self.browser.find_element(By.XPATH, "//*[@id='netunitIp']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='netunitIp']/following-sibling::span/input[1]").send_keys(
                netunit_ip)

        # 生产厂家
        if query.__contains__("生产厂家"):
            vendor = query.get("生产厂家")
            self.browser.find_element(By.XPATH, "//*[@id='vendorId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(vendor)).click()

        # 设备型号
        if query.__contains__("设备型号"):
            model = query.get("设备型号")
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}'".format(model)).click()

        # 机房信息
        if query.__contains__("机房信息"):
            room = query.get("机房信息")
            self.browser.find_element(By.XPATH, "//*[@id='roomInfo']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='roomInfo']/following-sibling::span/input[1]").send_keys(
                room)

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
                        By.XPATH, "//*[@field='netunitName']//*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, netunit_name, netunit_type, ip, vendor, netunit_model, state, maxCocurrentNum):
        """
        :param netunit_name: 网元名称
        :param netunit_type: 网元类型
        :param ip: 网元IP
        :param vendor: 生产厂家
        :param netunit_model: 设备型号
        :param state: 业务状态
        :param maxCocurrentNum: 最大并发数
        """
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'netunitInfoEdit.html?type=add')]"))
        sleep(1)
        self.netunit_page(netunit_name=netunit_name, netunit_type=netunit_type, ip=ip, vendor=vendor,
                          netunit_model=netunit_model, state=state, maxCocurrentNum=maxCocurrentNum)
        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
            alert.click_ok()
        gbl.temp.set("ResultMsg", msg)

    def update(self, netunit, netunit_name, netunit_type, ip, vendor, netunit_model, state, maxCocurrentNum):
        """
        :param netunit: 网元
        :param netunit_name: 网元名称
        :param netunit_type: 网元类型
        :param ip: 网元IP
        :param vendor: 生产厂家
        :param netunit_model: 设备型号
        :param state: 业务状态
        :param maxCocurrentNum: 最大并发数
        """
        self.search(query={"网元名称": netunit}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到修改网元信息页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'netunitInfoEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='ip']/preceding-sibling::input")))
            self.netunit_page(netunit_name=netunit_name, netunit_type=netunit_type, ip=ip, vendor=vendor,
                              netunit_model=netunit_model, state=state, maxCocurrentNum=maxCocurrentNum)
            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
                alert.click_ok()
            gbl.temp.set("ResultMsg", msg)

    def netunit_page(self, netunit_name, netunit_type, ip, vendor, netunit_model, state, maxCocurrentNum):
        """
        :param netunit_name: 网元名称
        :param netunit_type: 网元类型
        :param ip: 网元IP
        :param vendor: 生产厂家
        :param netunit_model: 设备型号
        :param state: 业务状态
        :param maxCocurrentNum: 最大并发数
        """

        # 网元名称
        if netunit_name:
            self.browser.find_element(By.XPATH, "//*[@name='netunitName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='netunitName']/preceding-sibling::input").send_keys(
                netunit_name)
            log.info("设置网元名称: {}".format(netunit_name))

        # 网元类型
        if netunit_type:
            self.browser.find_element(By.XPATH, "//*[@id='levelId']/following-sibling::span//a").click()
            sleep(1)
            type_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'levelId') and text()='{}']".format(netunit_type))
            action = ActionChains(self.browser)
            action.move_to_element(type_list).click().perform()
            log.info("设置网元类型: {}".format(netunit_type))

        # 网元IP
        if ip:
            self.browser.find_element(By.XPATH, "//*[@name='ip']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='ip']/preceding-sibling::input").send_keys(ip)
            log.info("设置网元IP: {}".format(ip))
            sleep(1)

        # 生产厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='vendorId']/following-sibling::span//a").click()
            sleep(1)
            vendor_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'vendorId') and text()='{}']".format(vendor))
            action = ActionChains(self.browser)
            action.move_to_element(vendor_list).click().perform()
            log.info("设置生产厂家: {}".format(vendor))

        # 设备型号
        if netunit_model:
            self.browser.find_element(By.XPATH, "//*[@id='netunitModelId']/following-sibling::span//a").click()
            sleep(1)
            nu_model_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModelId') and text()='{}']".format(netunit_model))
            action = ActionChains(self.browser)
            action.move_to_element(nu_model_list).click().perform()
            log.info("设置设备型号: {}".format(netunit_model))

        # 业务状态
        if state:
            self.browser.find_element(By.XPATH, "//*[@id='stateId']/following-sibling::span//a").click()
            sleep(1)
            nu_model_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'stateId') and text()='{}']".format(state))
            action = ActionChains(self.browser)
            action.move_to_element(nu_model_list).click().perform()
            log.info("设置业务状态: {}".format(state))

        # 最大并发数
        if maxCocurrentNum:
            self.browser.find_element(By.XPATH, "//*[@name='maxCocurrentNum']/preceding-sibling::input").clear()
            self.browser.find_element(
                By.XPATH, "//*[@name='maxCocurrentNum']/preceding-sibling::input").send_keys(maxCocurrentNum)
            log.info("设置最大并发数: {}".format(maxCocurrentNum))

        # # 提交
        # self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        # alert = BeAlertBox(back_iframe="default")
        # msg = alert.get_msg()
        # if alert.title_contains("保存成功"):
        #     log.info("保存配置成功")
        # else:
        #     log.warning("保存配置失败，失败提示: {0}".format(msg))
        #     alert.click_ok()
        # gbl.temp.set("ResultMsg", msg)

    def delete(self, netunit_name):
        """
        :param netunit_name: 网元名称
        """
        self.search(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(netunit_name, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(netunit_name))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(netunit_name, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(netunit_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def login_config(self, netunit_name, login_model_name, terminal, cmd_config):
        """
        :param netunit_name: 网元名称
        :param login_model_name: 登录模式
        :param terminal: 终端配置，字典
        :param cmd_config: 指令配置，数组，包含终端指令、登录指令
        :return:

        {
            "网元名称": "xxx",
            "登录模式": "普通模式",
            "终端配置": {
                "终端名称": "",
                "登录方式": "",
                "用户名": "",
                "密码": "",
                "IP": "",
                "端口": "",
                "期待返回符": "",
                "失败返回符": "",
                "字符集": ""
            },
            "指令配置": {
                "终端指令": [
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    },
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    }
                ],
                "登录指令": [
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    },
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    }
                ]
            }
        }
        """
        self.search(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='loginConfigBtn']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到登录模式配置页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'netunitInfoLoginMode.html')]")))
            sleep(1)

            # 终端
            terminal_field = "//*[contains(@id,'tb_')]//*[text()='{}']/../../../following-sibling::div[1]".format(
                login_model_name)

            # 按钮
            login_model_button_field = "//*[contains(@id,'tb_')]//*[text()='{}']/following-sibling::div[1]".format(
                login_model_name)

            # 终端配置
            if terminal:
                try:
                    # 如果已经配置了一条，则进行修改
                    row_ele = self.browser.find_element(
                        By.XPATH, terminal_field + "//*[contains(@class,'rownumber') and text()='1']")

                    # 双击修改
                    action = ActionChains(self.browser)
                    action.move_to_element(row_ele).double_click().perform()
                except NoSuchElementException:
                    # 该登录模式未配置信息，则添加
                    self.browser.find_element(By.XPATH, login_model_button_field + "//*[text()='添加']").click()
                finally:
                    sleep(1)
                    self.set_terminal(terminal_name=terminal.get("终端名称"), login_type=terminal.get("登录方式"),
                                      username=terminal.get("用户名"), password=terminal.get("密码"),
                                      ip=terminal.get("IP"), port=terminal.get("端口"),
                                      expected_str=terminal.get("期待返回符"), failed_str=terminal.get("失败返回符"),
                                      charset=terminal.get("字符集"), terminal_field=terminal_field)
                    # 保存终端配置
                    self.browser.find_element(By.XPATH, login_model_button_field + "//*[text()='保存']").click()
                    alert = BeAlertBox(back_iframe="default")
                    msg = alert.get_msg()
                    if alert.title_contains("保存成功"):
                        log.info("保存登录模式成功")
                    elif alert.title_contains("覆盖终端指令", auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(back_iframe="default")
                        msg = alert.get_msg()
                        if alert.title_contains("保存成功"):
                            log.info("保存登录模式成功")
                        else:
                            log.warning("保存登录模式失败，失败提示: {0}".format(msg))
                    else:
                        log.warning("保存登录模式失败，失败提示: {0}".format(msg))
                        alert.click_ok()
                    gbl.temp.set("ResultMsg", msg)

            # 指令配置
            if cmd_config:
                # 点击指令配置
                self.browser.find_element(By.XPATH, login_model_button_field + "//*[text()='指令配置']").click()
                # 切换指令配置页面iframe
                self.browser.switch_to.parent_frame()
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'netunitInfoCmdCfg.html')]")))
                sleep(1)

                # 终端指令
                if cmd_config.__contains__("终端指令"):
                    log.info("设置终端指令")
                    terminal_cmd = cmd_config.get("终端指令")
                    # 终端指令
                    terminal_cmd_field = "//*[@id='cmdInfo_form']/../following-sibling::div[1]"
                    row_num = 1

                    # 终端指令支持配置多条
                    for tc in terminal_cmd:
                        try:
                            row_ele = self.browser.find_element(
                                By.XPATH, terminal_cmd_field + "//*[contains(@class,'rownumber') and text()='{}']".format(
                                    row_num))
                            # 如果已存在，则双击修改
                            action = ActionChains(self.browser)
                            action.move_to_element(row_ele).double_click().perform()
                            sleep(1)
                        except NoSuchElementException:
                            # 如果不存在，则点击添加按钮
                            self.browser.find_element(By.XPATH, "//*[@id='cmdInfo_form']//*[text()='添加']").click()
                        finally:
                            self.set_cmd(cmd=tc.get("指令内容"), account=tc.get("账号名称"), expected_str=tc.get("期待返回符"),
                                         failed_str=tc.get("失败返回符"), hide_input_cmd=tc.get("隐藏输入指令"),
                                         hide_return=tc.get("隐藏指令返回"), quit_cmd=tc.get("退出命令"),
                                         sleep_time=tc.get("执行后等待时间"), translate_netunit=tc.get("是否适配网元"),
                                         charset=tc.get("字符集"), line_break=tc.get("换行符"), cmd_type=tc.get("指令类型"),
                                         cmd_field=terminal_cmd_field)
                            row_num += 1

                    # 保存终端指令
                    self.browser.find_element(By.XPATH, "//*[@id='cmdInfo_form']//*[text()='保存']").click()
                    alert = BeAlertBox(back_iframe="default")
                    msg = alert.get_msg()
                    if alert.title_contains("保存成功"):
                        log.info("保存终端指令成功")
                    else:
                        log.warning("保存终端指令失败，失败提示: {0}".format(msg))
                        alert.click_ok()
                    gbl.temp.set("ResultMsg", msg)

                # 登录指令
                if cmd_config.__contains__("登录指令"):
                    log.info("设置登录指令")
                    login_cmd = cmd_config.get("登录指令")
                    # 登录指令
                    login_cmd_field = "//*[@id='tb2']/following-sibling::div[1]"
                    row_num = 1

                    # 登录指令支持配置多条
                    for lc in login_cmd:
                        try:
                            row_ele = self.browser.find_element(
                                By.XPATH, login_cmd_field + "//*[contains(@class,'rownumber') and text()='{}']".format(
                                    row_num))
                            # 如果已存在，则双击修改
                            action = ActionChains(self.browser)
                            action.move_to_element(row_ele).double_click().perform()
                            sleep(1)
                        except NoSuchElementException:
                            # 如果不存在，则点击添加按钮
                            self.browser.find_element(By.XPATH, "//*[@id='tb2']//*[text()='添加']").click()
                        finally:
                            self.set_cmd(cmd=lc.get("指令内容"), account=lc.get("账号名称"), expected_str=lc.get("期待返回符"),
                                         failed_str=lc.get("失败返回符"), hide_input_cmd=lc.get("隐藏输入指令"),
                                         hide_return=lc.get("隐藏指令返回"), quit_cmd=lc.get("退出命令"),
                                         sleep_time=lc.get("执行后等待时间"), translate_netunit=lc.get("是否适配网元"),
                                         charset=lc.get("字符集"), line_break=lc.get("换行符"), cmd_type=lc.get("指令类型"),
                                         cmd_field=login_cmd_field)
                            row_num += 1

                    # 保存终端指令
                    self.browser.find_element(By.XPATH, "//*[@id='tb2']//*[text()='保存']").click()
                    alert = BeAlertBox(back_iframe="default")
                    msg = alert.get_msg()
                    if alert.title_contains("保存成功"):
                        log.info("保存登录指令成功")
                    elif alert.title_contains("是否将‘指令类型’设置为‘私有指令’", auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(back_iframe="default")
                        msg = alert.get_msg()
                        if alert.title_contains("保存成功"):
                            log.info("保存登录指令成功")
                        else:
                            log.warning("保存登录指令失败，失败提示: {0}".format(msg))
                            alert.click_ok()
                    else:
                        log.warning("保存登录指令失败，失败提示: {0}".format(msg))
                        alert.click_ok()
                    gbl.temp.set("ResultMsg", msg)

    def set_terminal(self, terminal_name, login_type, username, password, ip, port, expected_str, failed_str, charset,
                     terminal_field):
        """
        :param terminal_name: 终端名称
        :param login_type: 登录方式
        :param username: 用户名
        :param password: 密码
        :param ip: IP
        :param port: 端口
        :param expected_str: 期待返回符
        :param failed_str: 失败返回符
        :param charset: 字符集
        :param terminal_field:
        :return:
        """
        # 终端名称
        if terminal_name:
            self.browser.find_element(By.XPATH, terminal_field + "//*[@field='cid']//a").click()
            terminal_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(terminal_name))
            action = ActionChains(self.browser)
            action.move_to_element(terminal_list).click().perform()
            log.info("设置终端名称: {}".format(terminal_name))
            # 选完终端后，需要双击才能做修改
            row_ele = self.browser.find_element(
                By.XPATH, terminal_field + "//*[contains(@class,'rownumber') and text()='1']")
            # 双击修改
            action = ActionChains(self.browser)
            action.move_to_element(row_ele).double_click().perform()

        # 登录方式
        if login_type:
            self.browser.find_element(By.XPATH, terminal_field + "//*[@field='loginMode']//a").click()
            login_type_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(login_type))
            for e in login_type_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置登录方式: {}".format(login_type))
                    break

        # 用户名
        if username:
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='userName']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='userName']//*[@class='textbox']/input[1]").send_keys(username)
            log.info("设置用户名: {}".format(username))

        # 密码
        if password:
            self.browser.find_element(By.XPATH, terminal_field + "//*[@field='pwd']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='pwd']//*[@class='textbox']/input[1]").send_keys(password)
            log.info("设置密码: {}".format(password))
            sleep(1)

        # IP
        if ip:
            self.browser.find_element(By.XPATH, terminal_field + "//*[@field='ip']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='ip']//*[@class='textbox']/input[1]").send_keys(ip)
            log.info("设置IP: {}".format(ip))

        # 端口
        if port:
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='port']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='port']//*[@class='textbox']/input[1]").send_keys(port)
            log.info("设置端口: {}".format(port))

        # 期待返回符
        if expected_str:
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='telnetReturn']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='telnetReturn']//*[@class='textbox']/input[1]").send_keys(
                expected_str)
            log.info("设置期待返回符: {}".format(expected_str))

        # 失败返回符
        if failed_str:
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='failReturn']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, terminal_field + "//*[@field='failReturn']//*[@class='textbox']/input[1]").send_keys(failed_str)
            log.info("设置失败返回符: {}".format(failed_str))

        # 字符集
        if charset:
            self.browser.find_element(By.XPATH, terminal_field + "//*[@field='charset']//a").click()
            charset_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(charset))
            for e in charset_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置字符集: {}".format(charset))
                    break

    def set_cmd(self, cmd, account, expected_str, failed_str, hide_input_cmd, hide_return, quit_cmd, sleep_time,
                translate_netunit, charset, line_break, cmd_type, cmd_field):
        """
        :param cmd: 指令内容
        :param account: 账号名称
        :param expected_str: 期待返回符
        :param failed_str: 失败返回符
        :param hide_input_cmd: 隐藏输入指令
        :param hide_return: 隐藏指令返回
        :param quit_cmd: 退出命令
        :param sleep_time: 执行后等待时间
        :param translate_netunit: 是否适配网元
        :param charset: 字符集
        :param line_break: 换行符
        :param cmd_type: 指令类型
        :param cmd_field:
        :return:
        """
        # 指令内容
        if cmd:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='command']//*[@class='textbox']/input[1]").send_keys(cmd)
            log.info("设置指令内容: {}".format(cmd))

        # 账号名称
        if account:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='accountTempId']//a").click()
            account_list = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(account))
            action = ActionChains(self.browser)
            action.move_to_element(account_list).click().perform()
            log.info("设置账号名称: {}".format(account))

        # 期待返回符
        if expected_str:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='readUntil']//*[@class='textbox']/input[1]").send_keys(expected_str)
            log.info("设置期待返回符: {}".format(expected_str))

        # 失败返回符
        if failed_str:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='failureReaduntil']//*[@class='textbox']/input[1]").send_keys(failed_str)
            log.info("设置失败返回符: {}".format(failed_str))

        # 隐藏输入指令
        if hide_input_cmd:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='sensitiveCmd']//a").click()
            hide_input_cmd_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(hide_input_cmd))
            for e in hide_input_cmd_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置隐藏输入指令: {}".format(hide_input_cmd))
                    break

        # 隐藏指令返回
        if hide_return:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='sensitiveRegex']//*[@class='textbox']/input[1]").send_keys(hide_return)
            log.info("设置隐藏指令返回: {}".format(hide_return))

        # 退出命令
        if quit_cmd:
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='quitCommand']//*[@class='textbox']/input[1]").send_keys(quit_cmd)
            log.info("设置退出命令: {}".format(quit_cmd))

        # 执行后等待时间
        if sleep_time:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").clear()
            self.browser.find_element(
                By.XPATH, cmd_field + "//*[@field='waitTime']//*[@class='textbox']/input[1]").send_keys(sleep_time)
            log.info("设置执行后等待时间: {}".format(sleep_time))

        # 是否适配网元
        if translate_netunit:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='translateNetunit']//a").click()
            translate_netunit_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(translate_netunit))
            for e in translate_netunit_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置是否适配网元: {}".format(translate_netunit))
                    break

        # 字符集
        if charset:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='charset']//a").click()
            charset_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(charset))
            for e in charset_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置字符集: {}".format(charset))
                    break

        # 换行符
        if line_break:
            self.browser.find_element(By.XPATH, cmd_field + "//*[@field='lineBreak']//a").click()
            line_break_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(line_break))
            for e in line_break_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置换行符: {}".format(line_break))
                    break

        # 指令类型
        if cmd_type:
            cmd_type_ele = self.browser.find_element(By.XPATH, cmd_field + "//*[@field='isTemplCmd']//a")
            action = ActionChains(self.browser)
            action.move_to_element(cmd_type_ele).click().perform()
            cmd_type_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_easyui_combobox_') and text()='{}']".format(cmd_type))
            for e in cmd_type_list:
                if e.is_displayed():
                    action = ActionChains(self.browser)
                    action.move_to_element(e).click().perform()
                    log.info("设置指令类型: {}".format(cmd_type))
                    break

    def assign_rela(self, netunit_name, rela_type, ne_list, keyword):
        """
        # 分配网元关系
        :param netunit_name: 网元名称
        :param rela_type: 关系类型
        :param ne_list: 网元列表
        :param keyword: 关键字，设置关键字时，网元列表参数请传空
        """
        self.search(query={"网元名称": netunit_name}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='relaAssignBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'netunitInfoRelaAssign.html')]")))
        sleep(1)

        # 关系类型
        if rela_type:
            self.browser.find_element(By.XPATH, "//*[@id='tabs']//*[text()='{0}']".format(rela_type)).click()
            log.info("关系类型选择: {0}".format(rela_type))
            page_wait()

        # 网元列表
        if ne_list:
            if not isinstance(ne_list, list):
                raise TypeError("网元列表格式不是数组")
            if len(ne_list) > 0:
                for ne in ne_list:
                    self.browser.find_element(
                        By.XPATH, "//*[@id='tabs']/following-sibling::div//*[@id='netunitName']/following-sibling::span[1]/input[1]").clear()
                    self.browser.find_element(
                        By.XPATH, "//*[@id='tabs']/following-sibling::div//*[@id='netunitName']/following-sibling::span[1]/input[1]").send_keys(ne)
                    self.browser.find_element(By.XPATH, "//*[@id='searchBtn1']").click()
                    page_wait()
                    self.browser.find_element(
                        By.XPATH, "//*[@id='tabs']/following-sibling::div//*[@field='netunitName']//*[text()='{0}']".format(ne)).click()
                    # 分配所选
                    self.browser.find_element(By.XPATH, "//*[@id='allToSelected']").click()
                    alert = BeAlertBox(timeout=1, back_iframe="default")
                    msg = alert.get_msg()
                    if alert.title_contains("您确定需要分配所选数据吗", auto_click_ok=False):
                        alert.click_ok()
                        alert = BeAlertBox(timeout=10, back_iframe=False)
                        msg = alert.get_msg()
                        if alert.title_contains("分配成功"):
                            log.info("分配网元: {0}".format(ne))

                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
                            # 切到网元信息配置页面
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//*[contains(@src,'/html/nu/netunitInfo.html')]")))
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'netunitInfoRelaAssign.html')]")))
                        else:
                            log.error("分配网元: {0}失败，失败原因: {1}".format(ne, msg))
                            break
                    else:
                        log.error("分配网元: {0}失败，失败原因: {1}".format(ne, msg))
                        break
                    gbl.temp.set("ResultMsg", msg)

        # 关键字
        if keyword:
            self.browser.find_element(
                By.XPATH, "//*[@id='tabs']/following-sibling::div//*[@id='netunitName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tabs']/following-sibling::div//*[@id='netunitName']/following-sibling::span[1]/input[1]").send_keys(
                keyword)
            self.browser.find_element(By.XPATH, "//*[@id='searchBtn1']").click()
            page_wait()
            # 分配所选
            self.browser.find_element(By.XPATH, "//*[@id='allToSelected']").click()
            alert = BeAlertBox(timeout=1, back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("您确定需要分配全部数据吗", auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(timeout=10, back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("分配成功"):
                    log.info("按 {0} 查询后，分配网元成功".format(keyword))

                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
                    # 切到网元信息配置页面
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//*[contains(@src,'/html/nu/netunitInfo.html')]")))
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'netunitInfoRelaAssign.html')]")))
                else:
                    log.error("按 {0} 查询后，分配网元失败，失败原因: {1}".format(keyword, msg))
            else:
                log.error("按 {0} 查询后，分配网元失败，失败原因: {1}".format(keyword, msg))
            gbl.temp.set("ResultMsg", msg)

    def data_clear(self, netunit_name, fuzzy_match=False):
        """
        :param netunit_name: 网元名称
        :param fuzzy_match: 是否模糊查询，使用关键字开头模糊查询
        """
        self.search(query={"网元名称": netunit_name}, need_choose=False)
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='netunitName']//*[starts-with(text(),'{0}')]".format(netunit_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='netunitName']//*[text()='{0}']".format(netunit_name))
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
            self.browser.find_element(By.XPATH, "//*[text()='删除']").click()
            alert = BeAlertBox(back_iframe="default")
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
                            By.XPATH, "//*[@field='netunitName']//*[starts-with(text(),'{0}')]".format(netunit_name))
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
                log.warning("{0} 清理失败，失败提示: {1}".format(netunit_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
