# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/10 下午5:10

import traceback
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.main.python.lib.logger import log


def initBrowser(chrome_driver_path, download_path=None, background=True):
    log.info("开始初始化浏览器.")
    # noinspection PyBroadException
    try:
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': download_path,
                 'credentials_enable_service': False,  # 防弹窗保存密码
                 'profile.password_manager_enabled': False}  # 防弹窗保存密码
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('disable-infobars')  # 不弹出chrome正在受到自动测试软件的控制

        # 后台运行
        if background:
            options.add_argument('headless')
            browser_width, browser_height = pyautogui.size()
            options.add_argument('--window-size={}x{}'.format(browser_width, browser_height))

        chrome_server = Service(chrome_driver_path)
        browser = webdriver.Chrome(service=chrome_server, options=options)
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': download_path}}
        browser.execute("send_command", params)
        log.info("浏览器初始化完成，webdriver: {0}".format(browser))
    except Exception as e:
        traceback.print_exc()
        log.error("浏览器初始化失败！！！{}".format(str(e)))
        return None
    return browser
