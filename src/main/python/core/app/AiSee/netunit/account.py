# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:04

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.AiSee.netunit.menu import choose_domain
from src.main.python.core.app.AiSee.netunit.menu import choose_menu
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.pagination import Pagination
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class AccountTemp(object):

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="统一账号配置")

        # 切到统一账号管理页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'/html/nu/midJpAccountTempCfgInfo.html')]")))
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

        # 账号模版名称
        if query.__contains__("账号模版名称"):
            account_temp_name = query.get("账号模版名称")
            self.browser.find_element(By.XPATH, "//*[@id='accountTempName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='accountTempName']/following-sibling::span/input[1]").send_keys(account_temp_name)
            log.info("账号模版名称输入关键字: {}".format(account_temp_name))
            select_item = account_temp_name

        # 账号模版类型
        if query.__contains__("账号模版类型"):
            account_type = query.get("账号模版类型")
            self.browser.find_element(By.XPATH, "//*[@id='account_type']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(account_type)).click()
            log.info("账号模版类型选择: {}".format(account_type))

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(By.XPATH, "//*[@id='createrName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='createrName']/following-sibling::span/input[1]").send_keys(creator)
            log.info("创建人输入关键字: {}".format(creator))

        # 点击查询
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
                        By.XPATH, "//*[@field='accountTempName']//*[@data-mtips='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, account_temp_name, account_temp_type, remark, search_if_exist=True):
        """
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        :param search_if_exist: 搜索是否存在，存在则修改
        """
        search_if_exist = True if search_if_exist == "是" else False
        if search_if_exist:
            self.search(query={"账号模版名称": account_temp_name}, need_choose=False)
            page_wait()
            sleep(1)
            try:
                # 尝试找到一条记录并点击，点击为了修改时使用
                self.browser.find_element(
                    By.XPATH, "//*[@field='accountTempName']//*[@data-mtips='{0}']".format(account_temp_name)).click()
                log.info("账号模版【{}】存在，开始修改".format(account_temp_name))
                self.update(account_temp=None, account_temp_name=account_temp_name,
                            account_temp_type=account_temp_type, remark=remark)
                return
            except NoSuchElementException:
                log.info("账号模版不存在")

        log.info("开始添加账号模版")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'midJpAccountTempCfgInfoEdit.html')]"))
        sleep(1)
        self.account_temp_page(account_temp_name=account_temp_name, account_temp_type=account_temp_type, remark=remark)

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

    def update(self, account_temp, account_temp_name, account_temp_type, remark):
        """
        :param account_temp: 账号模版名称
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        """
        if account_temp:
            self.search(query={"账号模版名称": account_temp}, need_choose=False)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切到网元管理页面iframe
            wait = WebDriverWait(self.browser, 120)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
            # 切到统一账号管理页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//*[contains(@src,'/html/nu/midJpAccountTempCfgInfo.html')]")))
            # 切换到修改账号模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJpAccountTempCfgInfoEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='accountTempName']/preceding-sibling::input")))
            self.account_temp_page(account_temp_name=account_temp_name, account_temp_type=account_temp_type,
                                   remark=remark)

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

    def account_temp_page(self, account_temp_name, account_temp_type, remark):
        """
        :param account_temp_name: 账号模版名称
        :param account_temp_type: 账号模版类型
        :param remark: 账号模版用途
        """
        # 账号模版名称
        if account_temp_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='accountTempName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='accountTempName']/following-sibling::span[1]/input[1]").send_keys(account_temp_name)
            log.info("设置账号模版名称: {}".format(account_temp_name))

        # 账号模版类型
        if account_temp_type:
            self.browser.find_element(By.XPATH, "//*[@id='accountType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(account_temp_type)).click()
            log.info("设置账号模版类型: {}".format(account_temp_type))

        # 账号模版用途
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='remark']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置账号模版用途: {}".format(remark))


class Account(object):

    def __init__(self, account_temp_name):
        """
        # 账号配置
        :param account_temp_name: 账号模版名称
        """
        self.browser = gbl.service.get("browser")
        account_temp = AccountTemp()
        account_temp.search(query={"账号模版名称": account_temp_name}, need_choose=True)
        self.browser.find_element(
            By.XPATH, "//*[@data-mtips='{}']/../../../*[@field='accountTempId']//a".format(account_temp_name)).click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切换到配置账号页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfo.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(
                ec.element_to_be_clickable((By.XPATH, "//*[@id='userName']/following-sibling::span[1]/input[1]")))

    def search(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = {}

        # 作用域
        if query.__contains__("作用域"):
            account_scope = query.get("作用域")
            self.browser.find_element(By.XPATH, "//*[@id='accountScopeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(account_scope)).click()
            log.info("作用域选择: {}".format(account_scope))
            select_item["作用域"] = account_scope

        # 用户名
        if query.__contains__("用户名"):
            user_name = query.get("用户名")
            self.browser.find_element(By.XPATH, "//*[@id='user_name']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='user_name']/following-sibling::span/input[1]").send_keys(user_name)
            log.info("用户名输入关键字: {}".format(user_name))

        # 创建人
        if query.__contains__("创建人"):
            creator = query.get("创建人")
            self.browser.find_element(
                By.XPATH,
                "//*[@id='accountScopeId']/../following-sibling::div//*[@id='createrName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH,
                "//*[@id='accountScopeId']/../following-sibling::div//*[@id='createrName']/following-sibling::span/input[1]").send_keys(
                creator)
            log.info("创建人输入关键字: {}".format(creator))
            select_item["创建人"] = creator

        # 点击查询
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
                    account_scope = select_item.get("作用域")
                    creator = select_item.get("创建人")
                    if account_scope == "公有":
                        self.browser.find_element(
                            By.XPATH, "//*[@field='accountScopeName']//*[@data-mtips='{}']".format(account_scope)).click()
                    else:
                        self.browser.find_element(
                            By.XPATH,
                            "//*[@field='accountScopeName']//*[@data-mtips='{}']/../../following-sibling::td[@field='createrName']//*[text()='{}']".format(
                                account_scope, creator)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(','.join(select_item.values())))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, username, password, account_scope):
        """
        :param username: 用户名
        :param password: 密码
        :param account_scope: 账号作用域
        :return:
        """
        log.info("开始添加账号")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        alert = BeAlertBox(back_iframe="default", timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
        else:
            # 切到网元管理页面iframe
            wait = WebDriverWait(self.browser, 120)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
            # 切到统一账号管理页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//*[contains(@src,'/html/nu/midJpAccountTempCfgInfo.html')]")))
            # 切换到配置账号页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfo.html')]")))
            # 切换到账号编辑页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfoEdit.html')]")))
            self.account_page(account_scope=account_scope, username=username, password=password)

            # 提交
            self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("保存成功"):
                log.info("保存配置成功")
            else:
                log.warning("保存配置失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

    def update(self, account_scope, username, password, creator=None):
        """
        # 如果作用域是私有，则只修改本人创建的账号
        :param account_scope: 作用域
        :param creator: 创建人
        :param username: 用户名
        :param password: 密码
        """
        log.info("开始修改账号")
        if creator:
            self.search(query={"作用域": account_scope, "创建人": creator}, need_choose=True)
        else:
            self.search(query={"作用域": account_scope}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='editBtn']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfoEdit.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='userName']/preceding-sibling::input")))
        self.account_page(account_scope=None, username=username, password=password)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("修改成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def account_page(self, account_scope, username, password):
        """
        :param account_scope: 账号作用域
        :param username: 用户名
        :param password: 密码
        """
        # 用户名
        if username:
            self.browser.find_element(By.XPATH, "//*[@name='userName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='userName']/preceding-sibling::input").send_keys(username)
            log.info("设置用户名: {}".format(username))

        # 密码
        if password:
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").send_keys(password)
            log.info("设置密码: {}".format(password))

        # 账号作用域
        if account_scope:
            self.browser.find_element(By.XPATH, "//*[@id='accountScopeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(account_scope)).click()
            log.info("设置账号作用域: {}".format(account_scope))

    def delete(self, account_scope, creator=None):
        """
        # 只能删除本人创建的账号，如果作用域是私有，还需指明创建人
        :param account_scope: 账号作用域
        :param creator: 创建人
        """
        log.info("开始删除账号")
        self.search(query={"作用域": account_scope, "创建人": creator}, need_choose=True)
        if account_scope == "公有":
            obj_username = self.browser.find_element(
                By.XPATH, "//*[@data-mtips='公有']/../../following-sibling::td[1]/div")
        else:
            obj_username = self.browser.find_element(
                By.XPATH,
                "//*[@data-mtips='私有']/../../following-sibling::td[3]/*[text()='{}']/../preceding-sibling::td[2]/div".format(
                    creator))
        username = obj_username.get_attribute("innerHTML")
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{}吗".format(username), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(username))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(username, msg))
        else:
            log.warning("{0} 删除失败，失败提示: {1}".format(username, msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, creator):
        """
        # 清除账号模版下的账号
        :param creator: 创建人
        """
        self.search(query={"创建人": creator}, need_choose=False)
        record_element = self.browser.find_elements(
            By.XPATH, "//*[@field='createrName']/*[text()='{}']/../../*[@field='userName']/div".format(creator))
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
            self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("{0} 删除成功".format(search_result))
                    page_wait()
                    # 切到网元管理页面iframe
                    wait = WebDriverWait(self.browser, 120)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
                    # 切到统一账号管理页面iframe
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//*[contains(@src,'/html/nu/midJpAccountTempCfgInfo.html')]")))
                    # 切换到配置账号页面iframe
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfo.html')]")))

                    # 重新获取页面查询结果
                    record_element = self.browser.find_elements(
                        By.XPATH,
                        "//*[@field='createrName']/*[text()='{}']/../../*[@field='userName']/div".format(creator))
                    if len(record_element) == 0:
                        # 查询结果为空,修改exist_data为False，退出循环
                        log.info("数据清理完成")
                        exist_data = False
                else:
                    raise Exception("删除数据时出现未知异常: {0}".format(msg))
            else:
                # 无权操作
                log.warning("清理失败，失败提示: {}".format(msg))
                gbl.temp.set("ResultMsg", msg)
                break

    def issue_account(self, account_scope, issue_type, query, issue_obj, issue_scope, creator=None):
        """
        # 账号下发
        :param account_scope: 作用域
        :param creator: 创建人
        :param issue_scope: 下发对象类型，网元/统一网元配置
        :param query: 查询条件
        :param issue_obj: 下发对象，数组
        :param issue_type: 下发方式，下发所选/下发所有
        """
        log.info("开始账号下发")
        self.search(query={"作用域": account_scope, "创建人": creator}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='issueBtn']").click()

        # 切换到选择下发对象iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'midJumpAcInfoCfgInfoIssue.html')]")))

        # 下发对象类型
        if issue_scope:
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='{}']".format(issue_scope)).click()
            sleep(1)

        # 查询条件
        if query:
            if issue_scope is None or issue_scope == "网元":
                self.search_issue_netunit(query=query)
            else:
                self.search_issue_batch(query=query)

        # 下发对象
        if issue_obj:
            table_xpath = "//*[@id='tb1']/following-sibling::div[2]/table"
            p = Pagination(table_xpath)
            p.set_page_size(size=50)
            if issue_scope is None or issue_scope == "网元":
                for netunit in issue_obj:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='netunitName']//*[@data-mtips='{}']".format(netunit)).click()
                    log.info("选择账号下发到网元【{}】".format(netunit))
            else:
                for temp_name in issue_obj:
                    self.browser.find_element(
                        By.XPATH, "//*[@field='tempName']//*[@data-mtips='{}']".format(temp_name)).click()
                    log.info("选择账号下发到统一网元配置【{}】".format(temp_name))

        # 下发方式
        if issue_type:
            if issue_scope is None or issue_scope == "网元":
                if issue_type == "下发所选":
                    self.browser.find_element(By.XPATH, "//*[@class='tb1']//*[contains(@data-options,'more')]").click()
                else:
                    self.browser.find_element(By.XPATH, "//*[@class='tb1']//*[contains(@data-options,'sum')]").click()
            else:
                if issue_type == "下发所选":
                    self.browser.find_element(By.XPATH, "//*[@class='tb2']//*[contains(@data-options,'more')]").click()
                else:
                    self.browser.find_element(By.XPATH, "//*[@class='tb2']//*[contains(@data-options,'sum')]").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确认下发所选数据吗", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("下发成功"):
                log.info("账号下发成功")
            else:
                log.warning("账号下发失败，失败提示: {}".format(msg))
        elif alert.title_contains("您确认下发所有数据吗", auto_click_ok=False):
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("下发成功"):
                log.info("账号下发成功")
            else:
                log.warning("账号下发失败，失败提示: {}".format(msg))
        else:
            log.warning("账号下发失败，失败提示: {}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def search_issue_netunit(self, query):
        """
        # 账号下发搜索下发对象，按网元
        :param query: 查询条件
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))

        # 网元名称
        if query.__contains__("终端名称"):
            netunit_name = query.get("网元名称")
            self.browser.find_element(
                By.XPATH, "//*[@id='netunit-netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='netunit-netunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("网元名称输入: {}".format(netunit_name))

        # 网元类型
        if query.__contains__("网元类型"):
            level = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='netunit-levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(level)).click()
            log.info("网元类型选择: {}".format(level))

        # 登录模式
        if query.__contains__("登录模式"):
            login_type = query.get("登录模式")
            self.browser.find_element(By.XPATH, "//*[@id='netunit-loginTypeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(login_type)).click()
            log.info("登录模式选择: {}".format(login_type))

        # 发生变更
        if query.__contains__("发生变更"):
            is_change = query.get("发生变更")
            self.browser.find_element(By.XPATH, "//*[@id='netunit-isChange']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(is_change)).click()
            log.info("发生变更选择: {}".format(is_change))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='tb1']//*[contains(@data-options,'search')]").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)

    def search_issue_batch(self, query):
        """
        # 账号下发搜索下发对象，按网元
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))

        # 模版名称
        if query.__contains__("模版名称"):
            netunit_name = query.get("模版名称")
            self.browser.find_element(By.XPATH, "//*[@id='batch-netunitName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='batch-netunitName']/following-sibling::span/input[1]").send_keys(netunit_name)
            log.info("模版名称输入: {}".format(netunit_name))

        # 网元类型
        if query.__contains__("网元类型"):
            level = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='batch-levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(level)).click()
            log.info("网元类型选择: {}".format(level))

        # 登录模式
        if query.__contains__("登录模式"):
            login_type = query.get("登录模式")
            self.browser.find_element(By.XPATH, "//*[@id='batch-loginTypeId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(login_type)).click()
            log.info("登录模式选择: {}".format(login_type))

        # 发生变更
        if query.__contains__("发生变更"):
            is_change = query.get("发生变更")
            self.browser.find_element(By.XPATH, "//*[@id='batch-isChange']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(is_change)).click()
            log.info("发生变更选择: {}".format(is_change))

        # 点击查询
        self.browser.find_element(By.XPATH, "//*[@id='tb2']//*[contains(@data-options,'search')]").click()
        page_wait()
        alert = BeAlertBox(timeout=1, back_iframe=False)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("弹出框返回: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
