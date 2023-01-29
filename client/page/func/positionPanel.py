# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/17 下午5:33

from time import sleep
from selenium.webdriver.common.by import By
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


def getPanelXpath():
    """
    :return: 找到则返回xpath，否则返回None
    """
    browser = get_global_var("browser")
    panels = browser.find_elements(By.XPATH, "//*[contains(@class,'panel-htop')]")
    panel_xpath = None
    if len(panels) == 0:
        log.error("无法定位任何panel")
    else:
        sleep(1)
        for panel in panels:
            if panel.is_displayed():
                panel_attr_style = panel.get_attribute("style")
                patt = r'.+(z-index: \d+).+'
                match_obj = re.match(patt, panel_attr_style)
                if not match_obj:
                    continue
                else:
                    z_index = match_obj.group(1)
                    panel_xpath = "//*[contains(@class,'panel-htop') and contains(@style, '{0}')]".format(z_index)
                    break
    log.debug("panel_xpath: {0}".format(panel_xpath))
    return panel_xpath


def getPanelXpath1():
    """
    :return: 找到则返回xpath，否则返回None
    """
    browser = get_global_var("browser")
    panels = browser.find_elements(By.XPATH, "//*[contains(@class,'panel-htop')]")
    if len(panels) == 0:
        log.error("无法定位任何panel")
        panel_xpath = None
    else:
        element = None
        for panel in panels:
            if panel.is_displayed():
                element = panel
                break
        if element:
            panel_attr_style = element.get_attribute("style")
            patt = r'.+(z-index: \d+).+'
            match_obj = re.match(patt, panel_attr_style)
            if not match_obj:
                log.error("正则匹配style，找不到z-index")
                panel_xpath = None
            else:
                z_index = match_obj.group(1)
                panel_xpath = "//*[contains(@class,'panel-htop') and contains(@style, '{0}')]".format(z_index)
        else:
            log.error("找到panel，但不可见")
            panel_xpath = None
    log.info("panel_xpath: {0}".format(panel_xpath))
    return panel_xpath