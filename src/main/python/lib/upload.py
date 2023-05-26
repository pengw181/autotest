# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:31

from selenium.webdriver.common.by import By
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def upload(file_name, catalog=None, input_id='filebox_file_id_2'):
    browser = gbl.service.get("browser")
    uploadPath = gbl.service.get("ProjectPath") + '/src/main/resources/upload/'
    if not uploadPath.endswith("/"):
        uploadPath += "/"
    if catalog:
        path = uploadPath + catalog + "/" + file_name
    else:
        path = uploadPath + file_name
    log.info("上传文件路径: {0}".format(path))
    browser.find_element(By.XPATH, "//*[@id='{0}']".format(input_id)).send_keys(path)
