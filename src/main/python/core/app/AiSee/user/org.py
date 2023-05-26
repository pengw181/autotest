# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/10/19 下午6:11

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.core.mainPage import AiSee
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.treeNode import TreeNode
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class Organization:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        AiSee().choose_menu_func(menu="用户管理")
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/AiSee/html/user/userInfoMgt.html')]")))
        page_wait()
        sleep(1)
        # 实例化组织树
        self.org_tree = TreeNode(self.browser, "//*[@id='orgTree']")

    def addOrg(self, node_name, org_name, parent_org_name=None):
        """
        :param node_name: 节点名称
        :param parent_org_name: 上级组织
        :param org_name: 组织名称
        """
        self.org_tree.contextClick(node_name=node_name)
        log.info("选择组织: {0}，添加下级组织".format(node_name))
        add_elements = self.browser.find_elements(By.XPATH, "//*[text()='添加下级组织']")
        for element in add_elements:
            if element.is_displayed():
                element.click()
                break
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'orgEditWin.html')]")))
        sleep(1)

        # 上级组织
        if parent_org_name:
            self.browser.find_element(By.XPATH, "//*[@id='pOrg']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            new_tree = TreeNode(self.browser, panel_xpath)
            new_tree.click(parent_org_name)
            log.info("设置上级组织: {0}".format(parent_org_name))

        # 组织名称
        if org_name:
            self.browser.find_element(By.XPATH, "//*[@id='orgName']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='orgName']/following-sibling::span//input[1]").send_keys(org_name)
            log.info("设置组织名称: {0}".format(org_name))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='org-form-submit']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox(timeout=3)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("添加组织 {0} 成功".format(org_name))
        else:
            log.warning("添加组织 {0} 失败，失败原因: {1}".format(org_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def updateOrg(self, node_name, org_name, parent_org_name=None):
        """
        :param node_name: 节点名称
        :param parent_org_name: 上级组织
        :param org_name: 组织名称
        """
        self.org_tree.contextClick(node_name=node_name)
        log.info("选择组织: {0}，修改选中组织".format(node_name))
        add_elements = self.browser.find_elements(By.XPATH, "//*[text()='修改选中组织']")
        for element in add_elements:
            if element.is_displayed():
                element.click()
                break
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'orgEditWin.html')]")))
        sleep(1)

        # 上级组织
        if parent_org_name:
            self.browser.find_element(By.XPATH, "//*[@id='pOrg']/following-sibling::span//a").click()
            panel_xpath = getPanelXpath()
            new_tree = TreeNode(self.browser, panel_xpath)
            new_tree.click(parent_org_name)
            log.info("设置上级组织: {0}".format(parent_org_name))

        # 组织名称
        if org_name:
            self.browser.find_element(By.XPATH, "//*[@id='orgName']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='orgName']/following-sibling::span//input[1]").send_keys(org_name)
            log.info("设置组织名称: {0}".format(org_name))

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='org-form-submit']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox(timeout=3)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("修改组织 {0} 成功".format(org_name))
        else:
            log.warning("修改组织 {0} 失败，失败原因: {1}".format(org_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def deleteOrg(self, node_name):
        """
        :param node_name: 节点名称
        """
        self.org_tree.contextClick(node_name=node_name)
        log.info("选择组织: {0}，删除选中组织".format(node_name))
        add_elements = self.browser.find_elements(By.XPATH, "//*[text()='删除选中组织']")
        for element in add_elements:
            if element.is_displayed():
                element.click()
                alert = BeAlertBox(timeout=1)
                msg = alert.get_msg()
                if alert.title_contains("您确定要删除{0}，及其下属组织吗".format(node_name), auto_click_ok=False):
                    alert.click_ok()
                    alert = BeAlertBox(timeout=10, back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("删除成功"):
                        log.info("删除组织 {0} 成功".format(node_name))
                    else:
                        log.warning("删除组织 {0} 失败，失败原因: {1}".format(node_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break

    def clearOrg(self, node_name):
        """
        # 清理组织，如果不存在则无需清理；
        # 如果存在多个，只删除第一个，人为避免出现多个同名的情况
        :param node_name: 节点名称
        """
        try:
            self.org_tree.contextClick(node_name=node_name)
        except KeyError:
            log.info("组织 {0} 不存在，无需清理".format(node_name))
            return
        log.info("选择组织: {0}，删除组织".format(node_name))
        delete_elements = self.browser.find_elements(By.XPATH, "//*[text()='删除选中组织']")
        for element in delete_elements:
            if element.is_displayed():
                element.click()
                alert = BeAlertBox(timeout=1)
                msg = alert.get_msg()
                if alert.title_contains("您确定要删除{0}，及其下属组织吗".format(node_name), auto_click_ok=False):
                    alert.click_ok()
                    alert = BeAlertBox(timeout=10, back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("删除成功"):
                        log.info("删除组织 {0} 成功".format(node_name))
                    else:
                        log.warning("删除组织 {0} 失败，失败原因: {1}".format(node_name, msg))
                gbl.temp.set("ResultMsg", msg)
                break
