# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/19 下午4:30

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


class LevelInfo:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="网元管理")
        wait = WebDriverWait(self.browser, 120)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/nu/netunitMgtIndex.html')]")))
        page_wait()
        sleep(1)

        choose_domain(domain=gbl.service.get("Domain"))
        choose_menu(menu="网元类型")

        # 切到网元类型页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//*[contains(@src,'../../html/nu/levelInfo.html')]")))
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

        # 网元类型
        if query.__contains__("网元类型"):
            level_name = query.get("网元类型")
            self.browser.find_element(By.XPATH, "//*[@id='levelName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='levelName']/following-sibling::span/input[1]").send_keys(level_name)
            log.info("网元类型输入关键字: {}".format(level_name))
            select_item = level_name

        # 网络层级
        if query.__contains__("网络层级"):
            tree_level = query.get("网络层级")
            self.browser.find_element(By.XPATH, "//*[@id='netunit_level_id']/following-sibling::span//a").click()
            tree_level_path = tree_level.split("->")
            try:
                # 第一层
                first_tree_path = tree_level_path[0]
                self.browser.find_element(
                    By.XPATH, "//*[@class='tree-title' and text()='{}']/preceding-sibling::span[2]".format(
                        first_tree_path)).click()
                # 第二层
                if len(tree_level_path) > 1:
                    self.browser.find_element(
                        By.XPATH, "//*[@class='tree-title' and text()='{}']".format(tree_level)).click()
                log.info("设置网络层级: {}".format(tree_level))
            except NoSuchElementException:
                # tree中不存在要搜索的层级，直接收起下拉框
                self.browser.find_element(By.XPATH, "//*[@id='netunit_level_id']/following-sibling::span//a").click()
                log.info("网络层级未找到匹配数据")

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
                        By.XPATH, "//*[@field='levelName']/*[text()='{}']".format(select_item)).click()
                except NoSuchElementException:
                    raise KeyError("未找到匹配数据")
                log.info("选择: {}".format(select_item))
            else:
                raise KeyError("条件不足，无法选择数据")

    def add(self, up_level, level_name, level_type, search_if_exist=True):
        """
        :param up_level: 上级层级，数组，如['2G', '3G', '4G']
        :param level_name: 层级名称
        :param level_type: 层级类型
        :param search_if_exist: 搜索是否存在，存在则修改
        """
        search_if_exist = True if search_if_exist == "是" else False
        if search_if_exist:
            self.search(query={"网元类型": level_name}, need_choose=False)
            page_wait()
            sleep(1)
            try:
                # 尝试找到一条记录并点击，点击为了修改时使用
                self.browser.find_element(
                    By.XPATH, "//*[@field='levelName']/*[text()='{}']".format(level_name)).click()
                log.info("{} 网元类型已存在，开始修改".format(level_name))
                level_type_name_ele = self.browser.find_element(
                    By.XPATH, "//*[contains(@class,'selected')]/td[@field='levelTypeName']")
                level_type_name = level_type_name_ele.get_attribute("innerText")
                if level_type_name == "分类" and level_type is None:
                    msg = "保存成功"
                    gbl.temp.set("ResultMsg", msg)
                    return
                self.update(level=None, up_level=up_level, level_name=level_name, level_type=level_type)
                return
            except NoSuchElementException:
                log.info("网元类型不存在")

        log.info("开始添加网元类型")
        self.browser.find_element(By.XPATH, "//*[@id='addBtn']").click()
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'levelInfoEdit.html')]"))
        sleep(1)
        self.level_page(up_level=up_level, level_name=level_name, level_type=level_type)

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

    def update(self, level, up_level, level_name, level_type):
        """
        :param level: 网元类型
        :param up_level: 上级层级，数组，如['2G', '3G', '4G']
        :param level_name: 层级名称
        :param level_type: 层级类型
        """
        if level:
            self.search(query={"网元类型": level}, need_choose=True)
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
            # 切到网元类型页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//*[contains(@src,'../../html/nu/levelInfo.html')]")))
            # 切换到修改账号模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'levelInfoEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='levelNameInfo']/preceding-sibling::input")))
            self.level_page(up_level=up_level, level_name=level_name, level_type=level_type)

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

    def level_page(self, up_level, level_name, level_type):
        """
        :param up_level: 上级层级，数组，如['2G', '3G', '4G']
        :param level_name: 层级名称
        :param level_type: 层级类型
        """
        # 上级层级
        if up_level:
            self.browser.find_element(
                By.XPATH, "//*[@id='add_form']//*[@id='levelUpInfo']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            for ul in up_level:
                self.browser.find_element(
                    By.XPATH, panel_xpath + "//*[@class='tree-title' and text()='{}']".format(ul)).click()
                log.info("上级层级勾选: {}".format(ul))
            self.browser.find_element(
                By.XPATH, "//*[@id='add_form']//*[@id='levelUpInfo']/following-sibling::span//a").click()

        # 层级名称
        if level_name:
            self.browser.find_element(
                By.XPATH, "//*[@id='add_form']//*[@id='levelNameInfo']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH,
                "//*[@id='add_form']//*[@id='levelNameInfo']/following-sibling::span[1]/input[1]").send_keys(level_name)
            log.info("设置层级名称: {}".format(level_name))

        # 层级类型
        if level_type:
            self.browser.find_element(
                By.XPATH, "//*[@id='add_form']//*[@id='levelType']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(level_type)).click()
            log.info("设置层级类型: {}".format(level_type))
