# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/10/19 下午6:33

import traceback
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from client.page.func.waitElement import WaitElement


class TreeNode:

    def __init__(self, browser, root_xpath):
        self.browser = browser
        self.root = root_xpath

    def _expand(self, tree_node_xpath):
        """
        # 展开
        :param tree_node_xpath: 节点xpath
        """
        try:
            self.browser.find_element(By.XPATH, tree_node_xpath + "/span[contains(@class,'tree-collapsed')]").click()
        except NoSuchElementException:
            traceback.print_exc()

    def _collapse(self, tree_node_xpath):
        """
        # 折叠
        :param tree_node_xpath: 节点xpath
        """
        try:
            self.browser.find_element(By.XPATH, tree_node_xpath + "/span[contains(@class,'tree-expanded')]").click()
        except NoSuchElementException:
            traceback.print_exc()

    def expandAll(self, until=None):
        """
        # 展开所有，直至节点可见
        :param: until: 条件，元素xpath
        """
        tree_nodes_xpath = self.root + "//*[contains(@class,'tree-node')]"
        nodes = self.browser.find_elements(By.XPATH, tree_nodes_xpath + "/span[contains(@class,'tree-collapsed')]")
        exist = len(nodes)
        while exist > 0:
            for node in nodes:
                if node.is_displayed():
                    node.click()
                    sleep(1)
                    if WaitElement().until_displayed(until):
                        exist = 0
                        break

                    nodes = self.browser.find_elements(By.XPATH, tree_nodes_xpath + "/span[contains(@class,'tree-collapsed')]")
                    exist = len(nodes)
                    break

    def _locateNode(self, node_name):
        """
        :param node_name:节点名称
        :return: 元素对象
        """
        base_xpath = self.root + "//*[contains(@class,'tree-node')]/span[@class='tree-title' and text()='{0}']".format(
            node_name)
        sleep(1)
        nodes = self.browser.find_elements(By.XPATH, base_xpath)
        node = None
        if len(nodes) > 0:
            # 找到元素
            for element in nodes:
                if element.is_displayed():
                    node = element
                    break
        if node is None:
            # 展开所有
            self.expandAll(base_xpath)
            nodes = self.browser.find_elements(By.XPATH, base_xpath)
            # noinspection PyBroadException
            try:
                node = nodes[0]
                if not node.is_displayed():
                    raise Exception
            except Exception:
                node = None
        return node

    def click(self, node_name):
        """
        :param node_name: 节点名称
        :return: 左键单击
        """
        node = self._locateNode(node_name)
        if node:
            ActionChains(self.browser).move_to_element(node).click().perform()
        else:
            raise KeyError("节点 {0} 不存在".format(node_name))

    def contextClick(self, node_name):
        """
        :param node_name: 节点名称
        :return: 右键单击
        """
        node = self._locateNode(node_name)
        if node:
            ActionChains(self.browser).move_to_element(node).context_click().perform()
        else:
            raise KeyError("节点 {0} 不存在".format(node_name))
