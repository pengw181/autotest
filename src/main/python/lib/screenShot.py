# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/12 下午3:53

import os
from datetime import datetime
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def saveScreenShot():
    if gbl.temp.get("SkipCase") is True:
        log.info("本用例不截图")
        return
    browser = gbl.service.get("browser")
    if gbl.service.get("ScreenShotPath") is None:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/screenShot/'
        folder_id = gbl.service.get("FolderID")
        screenShot_file_path = base_path + folder_id + "/"
        if not os.path.exists(screenShot_file_path):
            os.mkdir(screenShot_file_path)
        gbl.service.set("ScreenShotPath", screenShot_file_path)
    else:
        screenShot_file_path = gbl.service.get("ScreenShotPath")
    log.info(screenShot_file_path)
    timestamp = datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S") + str(datetime.now().microsecond)
    suffix = ".png"
    file_name = "Webdriver_" + timestamp + suffix
    screenShot_file = screenShot_file_path + file_name
    browser.save_screenshot(screenShot_file)
    log.info("保存截图: {0}".format(file_name))
    print("screenshot: {}".format(screenShot_file))     # 这一行必须要，生成报告用
