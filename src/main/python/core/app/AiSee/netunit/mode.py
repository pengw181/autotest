# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/19 下午12:05

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
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class LoginMode:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="网元登录模式")

        # 切到网元登录模式页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'../../html/nu/netunitLoginCfgInfo.html')]")))
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
        select_item = {}

        # 网元类型
        if query.__contains__("网元类型"):
            cfg_level_type = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='cfgLevelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(cfg_level_type)).click()
            log.info("网元类型选择: {}".format(cfg_level_type))
            select_item["网元类型"] = cfg_level_type

        # 登录模式名称
        if query.__contains__("登录模式名称"):
            login_type_name = query.get("登录模式名称")
        else:
            login_type_name = "普通模式"    # 默认普通模式
        select_item["登录模式名称"] = login_type_name

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
                cfg_level_type = select_item.get("网元类型")
                login_type_name = select_item.get("登录模式名称")
                try:
                    self.browser.find_element(
                        By.XPATH,
                        "//*[@field='levelName']/*[text()='{}']/../following-sibling::td[@field='loginTypeName']/*[text()='{}']".format(
                            cfg_level_type, login_type_name)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {0}".format(", ".join(select_item.values())))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, cfg_level_type, login_type_name, remark, search_if_exist=True):
        """
        # 新增加网元类型后，需要给当前操作用户分配网元类型权限，分配后会自动增加一个普通模式的登录模式。
        # 不分配则增加登录模式时无法选择改网元类型。

        :param cfg_level_type: 网元类型
        :param login_type_name: 登录模式名称
        :param remark: 登录模式描述
        :param search_if_exist: 搜索是否存在，存在则修改
        """
        search_if_exist = True if search_if_exist == "是" else False
        if search_if_exist:
            self.search(query={"网元类型": cfg_level_type, "登录模式名称": login_type_name}, need_choose=False)
            page_wait()
            sleep(1)
            try:
                self.browser.find_element(
                    By.XPATH,
                    "//*[@field='levelName']/*[text()='{}']/../following-sibling::td[@field='loginTypeName']/*[text()='{}']".format(
                        cfg_level_type, login_type_name)).click()
                log.info("{} {}登录模式已存在，开始修改".format(cfg_level_type, login_type_name))
                self.update(query=None, login_type_name=login_type_name, remark=remark)
                return
            except NoSuchElementException:
                log.info("登录模式不存在")

        log.info("开始添加登录模式")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'netunitLoginCfgInfoEdit.html')]"))
        sleep(1)
        self.login_type_page(cfg_level_type=cfg_level_type, login_type_name=login_type_name, remark=remark)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveBtn']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("保存配置成功")
        else:
            log.warning("保存配置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def update(self, query, login_type_name, remark):
        """
        :param query: 查询条件
        :param login_type_name: 登录模式名称
        :param remark: 登录模式描述
        """
        if query:
            self.search(query=query, need_choose=True)
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
            # 切到网元登录模式页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//*[contains(@src,'../../html/nu/netunitLoginCfgInfo.html')]")))
            # 切换到修改账号模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'netunitLoginCfgInfoEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='loginTypeName']/preceding-sibling::input")))
            self.login_type_page(cfg_level_type=None, login_type_name=login_type_name, remark=remark)

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

    def login_type_page(self, cfg_level_type, login_type_name, remark):
        """
        :param cfg_level_type: 网元类型
        :param login_type_name: 登录模式名称
        :param remark: 登录模式描述
        """
        # 网元类型
        if cfg_level_type:
            self.browser.find_element(
                By.XPATH, "//*[@id='edit-form']//*[@id='levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(cfg_level_type)).click()
            log.info("设置网元类型: {}".format(cfg_level_type))

        # 登录模式名称
        if login_type_name:
            self.browser.find_element(By.XPATH, "//*[@id='loginTypeName']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='loginTypeName']/following-sibling::span[1]/input[1]").send_keys(login_type_name)
            log.info("设置登录模式名称: {}".format(login_type_name))

        # 登录模式描述
        if remark:
            self.browser.find_element(By.XPATH, "//*[@id='loginTypeDesc']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='loginTypeDesc']/following-sibling::span[1]/input[1]").send_keys(remark)
            log.info("设置登录模式描述: {}".format(remark))
