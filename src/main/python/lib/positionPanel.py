# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/17 下午5:33

import re
from time import sleep
from selenium.webdriver.common.by import By
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def getPanelXpath(timeout=30):
    """
    :return: 找到则返回xpath，否则返回None
    """
    browser = gbl.service.get("browser")
    panels = browser.find_elements(By.XPATH, "//*[contains(@class,'panel-htop')]")
    panel_xpath = None
    if len(panels) == 0:
        log.error("无法定位任何panel")
    else:
        try_time = 0
        while try_time < timeout:
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
            if panel_xpath is not None:
                break
            else:
                try_time += 2
                sleep(2)
    log.debug("panel_xpath: {0}".format(panel_xpath))
    return panel_xpath
