# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:50

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.windows import WindowHandles
from src.main.python.lib.tab import TabHandles
from src.main.python.static.visualmodeler_menu import *
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def get_menu_xpath(level, menu):
    """
    # 获取菜单xpath
    :param level: 层级，first/second/third
    :param menu: 菜单名
    :return: xpath or None
    """
    if level == "first":
        xpath_object = first_menu_xpath
    elif level == "second":
        xpath_object = second_menu_xpath
    else:
        xpath_object = third_menu_xpath
    result = xpath_object.get(menu)
    if result is None:
        raise Exception("菜单【{0}】未定义".format(menu))
    return result


class DoctorWho:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        self.current_win_handle = WindowHandles()
        log.info("进入领域页面")

        # 关闭多余窗口
        self.current_win_handle.close(title="流程图编辑器")
        self.current_win_handle.close(title="告警平台")
        self.current_win_handle.close(title="仪表盘主配置页")
        self.current_win_handle.close(title="数据管理")
        self.current_win_handle.close(title="一键启动")
        self.current_win_handle.close(title="数据库管理")
        sleep(1)

        # 切换到vm窗口
        self.current_win_handle.save("vm")
        self.current_win_handle.switch("vm")
        # log.info("tab : {}".format(get_global_var("TableHandles")))

        # 重置tab
        gbl.service.set("TableHandles", None)
        # if bool(get_global_var("TableHandles")):
        #     # 刷新页面可以关闭打开的tab，
        #     self.browser.refresh()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@mid='PersonalCenter1001']//*[text()='个人中心']")))

    def choose_menu(self, menu_path):
        menu_list = str(menu_path).split("-")
        first_menu = menu_list[0]
        second_menu = menu_list[1]
        current_tab_handle = TabHandles()

        try:
            first_menu_element = self.browser.find_element(By.XPATH, get_menu_xpath("first", first_menu))
            self.browser.execute_script("arguments[0].scrollIntoView(true);", first_menu_element)
            first_menu_element.click()
            log.info("点击一级菜单: {0}".format(first_menu))
            sleep(1)

            if second_menu:
                second_menu_element = self.browser.find_element(By.XPATH, get_menu_xpath("second", second_menu))
                self.browser.execute_script("arguments[0].scrollIntoView(true);", second_menu_element)
                second_menu_element.click()
                log.info("点击二级菜单: {0}".format(second_menu))
                sleep(1)

                # 如果打开的二级菜单是在当前页面，在点击二级菜单后需要保存tab句柄
                if second_menu not in ("云平台", "告警平台", "数据接入平台", "OA审批平台"):
                    if second_menu not in ["文件目录管理"]:
                        current_tab_handle.save(second_menu)
                        current_tab_handle.switch(second_menu)
                    else:
                        # 文件目录管理特殊处理
                        third_menu = menu_list[2]
                        third_menu_element = self.browser.find_element(By.XPATH, get_menu_xpath("third", third_menu))
                        self.browser.execute_script("arguments[0].scrollIntoView(true);", third_menu_element)
                        third_menu_element.click()
                        log.info("点击三级菜单: {0}".format(third_menu))
                        sleep(1)
                        current_tab_handle.save(third_menu)
                        current_tab_handle.switch(third_menu)
                else:
                    # 如果打开的二级菜单是新开标签，如：告警、OA审批平台、云平台，在点击二级菜单后需要保存windows句柄
                    log.info("进入【{}】".format(second_menu))
                    self.current_win_handle.save(second_menu)
                    self.current_win_handle.switch(second_menu)
                    sleep(1)
            return True
        except NoSuchElementException:
            return False

    def logout(self):

        try:
            self.browser.find_element(By.XPATH, "//*[@id='logout']").click()
        except NoSuchElementException:
            raise
