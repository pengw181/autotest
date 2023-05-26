# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:07

import json
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.core.mainPage import AiSee
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.treeNode import TreeNode
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class User:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="用户管理")
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='qUserName']/following-sibling::span/input[1]")))
        page_wait()
        sleep(1)

    def search(self, query, need_choose=False):
        """
        :param query: 查询条件，字典
        :param need_choose: True/False
        """
        if not isinstance(query, dict):
            raise TypeError("查询条件需要是字典格式")
        log.info("查询用户信息，查询条件: {0}".format(json.dumps(query, ensure_ascii=False)))
        select_item = None

        # 用户（可能是登录账号，也可以是用户名称）
        if query.__contains__("用户"):
            user = query.get("用户")
            self.browser.find_element(By.XPATH, "//*[@id='qUserName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='qUserName']/following-sibling::span/input[1]").send_keys(user)
            select_item = user

        # 启用状态
        if query.__contains__("启用状态"):
            alive_status = query.get("启用状态")
            self.browser.find_element(By.XPATH, "//*[@id='qIsAlive']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[contains(@id,'qIsAlive') and text()='{0}']".format(
                alive_status)).click()

        # 锁定状态
        if query.__contains__("锁定状态"):
            lock_status = query.get("锁定状态")
            self.browser.find_element(By.XPATH, "//*[@id='qLockStat']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[contains(@id,'qLockStat') and text()='{0}']".format(
                lock_status)).click()

        # 查询
        self.browser.find_element(By.XPATH, "//*[@id='user-query']").click()
        page_wait()
        alert = BeAlertBox(timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            gbl.temp.set("ResultMsg", msg)
            return
        if need_choose:
            if select_item:
                wait = WebDriverWait(self.browser, 3)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
                try:
                    self.browser.find_element(By.XPATH, "//*[@field='userId']/*[text()='{0}']".format(select_item)).click()
                except NoSuchElementException:
                    try:
                        self.browser.find_element(By.XPATH, "//*[@field='userName']/*[text()='{0}']".format(
                            select_item)).click()
                    except NoSuchElementException:
                        raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, user_id, user_name, sex, password, belong_org, phone, email, wechat, is_alive, is_lock, pwd_overdue,
            pwd_warn_days):
        """
        :param user_id: 登录账号
        :param user_name: 用户名称
        :param sex: 性别
        :param password: 用户密码
        :param belong_org: 所属组织
        :param phone: 电话号码
        :param email: 邮箱
        :param wechat: portal号
        :param is_alive: 启用状态
        :param is_lock: 锁定状态
        :param pwd_overdue: 密码有效期(天)
        :param pwd_warn_days: 密码过期预警天数
        """
        log.info("开始添加用户")
        self.browser.find_element(By.XPATH, "//*[@id='user-add']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'userEditWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='userId']/following-sibling::span/input[1]")))
        page_wait()
        self.user_page(user_id, user_name, sex, password, belong_org, phone, email, wechat, is_alive, is_lock,
                       pwd_overdue, pwd_warn_days)
        alert = BeAlertBox(timeout=10, back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("用户信息保存成功"):
            log.info("添加用户 {0} 成功".format(user_id))
        else:
            log.warning("添加用户 {0} 失败，失败原因: {1}".format(user_id, msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, user, user_name=None, sex=None, password=None, belong_org=None, phone=None, email=None, wechat=None,
               is_alive=None, is_lock=None, pwd_overdue=None, pwd_warn_days=None, need_query=True):
        """
        :param user: 用户
        :param user_name: 用户名称
        :param sex: 性别
        :param password: 用户密码
        :param belong_org: 所属组织
        :param phone: 电话号码
        :param email: 邮箱
        :param wechat: portal号
        :param is_alive: 启用状态
        :param is_lock: 锁定状态
        :param pwd_overdue: 密码有效期(天)
        :param pwd_warn_days: 密码过期预警天数
        :param need_query:
        """
        if need_query:
            self.search(query={"用户": user}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='user-edit']").click()
        alert = BeAlertBox(timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.warning('修改用户 {0} 失败，失败原因: {1}'.format(user, msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            wait = WebDriverWait(self.browser, 3)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
            wait = WebDriverWait(self.browser, 30)
            wait.until(
                ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'userEditWin.html')]")))
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]")))
            page_wait()
            self.user_page(None, user_name, sex, password, belong_org, phone, email, wechat, is_alive, is_lock,
                           pwd_overdue, pwd_warn_days)
            alert = BeAlertBox(timeout=10, back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("用户信息修改成功"):
                log.info("修改用户 {0} 成功".format(user))
            else:
                log.warning("修改用户 {0} 失败，失败原因: {1}".format(user, msg))
            gbl.temp.set("ResultMsg", msg)

    def user_page(self, user_id, user_name, sex, password, belong_org, phone, email, wechat, is_alive, is_lock,
                  pwd_overdue, pwd_warn_days):
        """
        :param user_id: 登录账号
        :param user_name: 用户名称
        :param sex: 性别
        :param password: 用户密码
        :param belong_org: 所属组织
        :param phone: 电话号码
        :param email: 邮箱
        :param wechat: portal号
        :param is_alive: 启用状态
        :param is_lock: 锁定状态
        :param pwd_overdue: 密码有效期(天)
        :param pwd_warn_days: 密码过期预警天数
        """
        # 登录账号
        if user_id:
            self.browser.find_element(By.XPATH, "//*[@id='userId']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='userId']/following-sibling::span/input[1]").send_keys(user_id)
            log.info("设置登录账号: {0}".format(user_id))

        # 用户名称
        if user_name:
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='userName']/following-sibling::span/input[1]").send_keys(
                user_name)
            log.info("设置用户名称: {0}".format(user_name))

        # 性别
        if sex:
            self.browser.find_element(By.XPATH, "//*[@name='sex']/following-sibling::span[text()='{0}']".format(
                sex)).click()
            log.info("设置性别: {0}".format(sex))

        # 用户密码
        if password:
            try:
                # 判断是否是修改密码
                self.browser.find_element(
                    By.XPATH, "//*[@id='pwd']/following-sibling::span//a[contains(@class,'edit')]").click()
            except NoSuchElementException:
                pass
            self.browser.find_element(By.XPATH, "//*[@name='pwd']/preceding-sibling::input").send_keys(password)
            log.info("设置密码: {0}".format(password))
            sleep(1)

        # 所属组织
        if belong_org:
            self.browser.find_element(By.XPATH, "//*[@id='belongId']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            belong_tree = TreeNode(self.browser, panel_xpath)
            belong_tree.click(belong_org)
            log.info("设置所属组织: {0}".format(belong_org))

        # 电话号码
        if phone:
            self.browser.find_element(By.XPATH, "//*[@id='phone']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='phone']/following-sibling::span/input[1]").send_keys(phone)
            log.info("设置电话号码: {0}".format(phone))

        # 邮箱
        if email:
            self.browser.find_element(By.XPATH, "//*[@id='email']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='email']/following-sibling::span/input[1]").send_keys(email)
            log.info("设置邮箱: {0}".format(email))

        # portal号
        if wechat:
            self.browser.find_element(By.XPATH, "//*[@id='wechatAccount']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='wechatAccount']/following-sibling::span/input[1]").send_keys(
                wechat)
            log.info("设置portal号: {0}".format(wechat))

        # 启用状态
        if is_alive:
            self.browser.find_element(By.XPATH, "//*[@id='isAlive']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[contains(@id,'isAlive') and text()='{0}']".format(
                is_alive)).click()
            log.info("设置启用状态: {0}".format(is_alive))

        # 锁定状态
        if is_lock:
            self.browser.find_element(By.XPATH, "//*[@id='lockStat']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[contains(@id,'lockStat') and text()='{0}']".format(
                is_lock)).click()
            log.info("设置锁定状态: {0}".format(is_lock))

        # 密码有效期(天)
        if pwd_overdue:
            self.browser.find_element(By.XPATH, "//*[@id='pwdOverdue']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='pwdOverdue']/following-sibling::span/input[1]").send_keys(
                pwd_overdue)
            log.info("设置密码有效期(天): {0}".format(pwd_overdue))

        # 密码过期预警天数
        if pwd_warn_days:
            self.browser.find_element(By.XPATH, "//*[@id='pwdWarnDays']/following-sibling::span/input[1]").clear()
            self.browser.find_element(By.XPATH, "//*[@id='pwdWarnDays']/following-sibling::span/input[1]").send_keys(
                pwd_warn_days)
            log.info("设置密码过期预警天数: {0}".format(pwd_warn_days))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='user-form-submit']").click()

    def delete(self, user):
        """
        :param user: 用户
        """
        log.info("开始修改用户")
        self.search(query={"用户": user}, need_choose=True)
        self.browser.find_element(By.XPATH, "//*[@id='user-del']").click()
        alert = BeAlertBox(timeout=1)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(timeout=10, back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("用户信息删除成功"):
                log.warning('删除用户 {0} 成功'.format(user))
            else:
                log.warning('删除用户 {0} 失败，失败原因: {1}'.format(user, msg))
        else:
            log.warning('删除用户 {0} 失败，失败原因: {1}'.format(user, msg))
        gbl.temp.set("ResultMsg", msg)

    def clear(self, user, fuzzy_match=False):
        """
        :param user: 用户名称
        :param fuzzy_match: 模糊匹配
        """
        self.search(query={"用户": user}, need_choose=False)
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='userName']//*[starts-with(text(),'{}')]".format(user))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='userName']//*[text()='{0}']".format(user))
        if len(record_element) == 0:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            return

        exist_data = True
        while exist_data:
            pe = record_element[0]
            js = 'return $(".userInfoTab_datagrid-cell-c1-userName")[1].innerText;'
            search_result = self.browser.execute_script(js)
            js = 'return $(".userInfoTab_datagrid-cell-c1-isAliveText")[1].innerText;'
            is_alive = self.browser.execute_script(js)
            if is_alive == "启用":
                # 启用状态下用户无法删除，需要修改为禁用
                pe.click()
                self.update(user=search_result, is_alive="禁用", need_query=False)
                log.info("将用户状态修改为禁用")
                wait = WebDriverWait(self.browser, 3)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@id='qUserName']/following-sibling::span/input[1]")))
                page_wait()
                sleep(1)

            self.browser.find_element(By.XPATH, "//*[@field='userName']//*[text()='{0}']".format(
                search_result)).click()
            log.info("选择: {0}".format(search_result))
            # 删除
            self.browser.find_element(By.XPATH, "//*[@id='user-del']").click()
            alert = BeAlertBox(timeout=1)
            msg = alert.get_msg()
            if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                alert.click_ok()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("用户信息删除成功"):
                    log.info("{0} 删除成功".format(search_result))
                    wait = WebDriverWait(self.browser, 3)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
                    wait = WebDriverWait(self.browser, 10)
                    wait.until(ec.element_to_be_clickable((
                        By.XPATH, "//*[@id='qUserName']/following-sibling::span/input[1]")))
                    page_wait()
                    if fuzzy_match:
                        # 重新获取页面查询结果
                        record_element = self.browser.find_elements(
                            By.XPATH, "//*[@field='userName']//*[starts-with(text(),'{}')]".format(user))
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
                log.warning("{0} 删除失败，失败提示: {1}".format(user, msg))
                gbl.temp.set("ResultMsg", msg)
                break
