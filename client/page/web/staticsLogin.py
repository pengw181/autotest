# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/10 下午3:48

from time import sleep
from service.lib.log.logger import log
from selenium.webdriver.common.by import By
from client.page.browser.initBrowser import initBrowser
from client.page.func.alertBox import BeAlertBox
from client.page.func.pageMaskWait import page_wait
from client.page.handle.windows import WindowHandles
from config.loads import properties
from service.lib.variable.globalVariable import *


def login_tool(system_name, username=None, password=None, encryption=None, tokenId=None, redirect_url=None, appId=None,
               domain_detail=None, dsKey=None, custom=None, signature=None, language=None, login_type="登录"):
    """
    :param system_name: 系统
    :param username: 用户名
    :param password: 密码
    :param encryption: 密码是否密文
    :param tokenId: tokenId
    :param redirect_url: 应用跳转url
    :param appId: appId
    :param domain_detail: 领域明细
    :param dsKey: dsKey
    :param custom: 客户
    :param signature: 签名秘钥
    :param language: 语言
    :param login_type: 登录方式
    """

    # 初始化浏览器
    browser = initBrowser()
    browser.get(properties.get("systemLoginUrl"))
    browser.maximize_window()
    sleep(1)
    # https高级
    if properties.get("https"):
        browser.find_element(
            By.XPATH, "//*[text()='返回安全连接']/following-sibling::button[2][contains(text(),'高级')]").click()
        browser.find_element(By.XPATH, "//*[@id='proceed-link']").click()
    page_wait()
    log.info("***************************欢迎进入登录测试页面***************************")

    # 切换系统，自动填充默认值
    if system_name:
        browser.find_element(By.XPATH, "//*[@id='AppList']//*[@value='{0}']".format(system_name)).click()
        log.info("选择系统: {}".format(system_name))
        sleep(2)

    # 用户名
    if username:
        browser.find_element(By.XPATH, "//*[@name='userId']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='userId']/preceding-sibling::input").send_keys(username)
        log.info("设置用户名: {}".format(username))

    # 密码
    if password:
        browser.find_element(By.XPATH, "//*[@name='password']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='password']/preceding-sibling::input").send_keys(password)
        log.info("设置密码: {}".format(password))

    # 密码是否密文
    if encryption:
        browser.find_element(By.XPATH, "//*[@id='pwdEnc']").click()
        log.info("勾选密码是否密文")

    # tokenId
    if tokenId:
        # browser.find_element(By.XPATH, "//*[@name='tokenId']/preceding-sibling::input").clear()
        # browser.find_element(By.XPATH, "//*[@name='tokenId']/preceding-sibling::input").send_keys(tokenId)
        # log.info("设置tokenId: {}".format(tokenId))
        log.info("自动设置tokenId")

    # 应用跳转url
    if redirect_url:
        browser.find_element(By.XPATH, "//*[@name='appUrl']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='appUrl']/preceding-sibling::input").send_keys(redirect_url)
    else:
        browser.find_element(By.XPATH, "//*[@name='appUrl']/preceding-sibling::input").clear()
    log.info("设置应用跳转url: {}".format(redirect_url))

    # appId
    if appId:
        browser.find_element(By.XPATH, "//*[@name='appId']/preceding-sibling::input").clear()
        browser.find_element(By.XPATH, "//*[@name='appId']/preceding-sibling::input").send_keys(appId)
    else:
        browser.find_element(By.XPATH, "//*[@name='appId']/preceding-sibling::input").clear()
    log.info("设置appId: {}".format(appId))

    # 领域明细
    if domain_detail:
        browser.find_element(By.XPATH, "//*[@id='domainDetailId']/following-sibling::span/input[1]").clear()
        browser.find_element(
            By.XPATH, "//*[@id='domainDetailId']/following-sibling::span/input[1]").send_keys(domain_detail)
    else:
        browser.find_element(By.XPATH, "//*[@id='domainDetailId']/following-sibling::span/input[1]").clear()
    log.info("设置领域明细: {}".format(domain_detail))

    # dsKey
    if dsKey:
        browser.find_element(By.XPATH, "//*[@id='dsKey']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='dsKey']/following-sibling::span/input[1]").send_keys(dsKey)
    else:
        browser.find_element(By.XPATH, "//*[@id='dsKey']/following-sibling::span/input[1]").clear()
    log.info("设置dsKey: {}".format(dsKey))

    # 客户
    if custom:
        browser.find_element(By.XPATH, "//*[@id='company']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='company']/following-sibling::span/input[1]").send_keys(custom)
    else:
        browser.find_element(By.XPATH, "//*[@id='company']/following-sibling::span/input[1]").clear()
    log.info("设置客户: {}".format(custom))

    # 签名秘钥
    if signature:
        browser.find_element(By.XPATH, "//*[@id='permission']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='permission']/following-sibling::span/input[1]").send_keys(signature)
    else:
        browser.find_element(By.XPATH, "//*[@id='permission']/following-sibling::span/input[1]").clear()
    log.info("设置签名秘钥: {}".format(signature))

    # 语言
    if language:
        browser.find_element(By.XPATH, "//*[@id='locale']/following-sibling::span/input[1]").clear()
        browser.find_element(By.XPATH, "//*[@id='locale']/following-sibling::span/input[1]").send_keys(language)
    else:
        browser.find_element(By.XPATH, "//*[@id='locale']/following-sibling::span/input[1]").clear()
    log.info("设置语言: {}".format(language))

    # 登录方式
    if login_type:
        browser.find_element(By.XPATH, "//*[text()='{0}']".format(login_type)).click()
        log.info("设置登录方式: {}".format(login_type))

    alert = BeAlertBox(timeout=3)
    if alert.exist_alert:
        msg = alert.get_msg()
        log.info("登录返回: {0}".format(msg))
    else:
        log.info("登录成功...")
        current_win_handle = WindowHandles()
        log.info("进入应用后，保存新窗口句柄")
        # 切换到应用窗口
        app = get_global_var("Application")
        current_win_handle.save(app)
        current_win_handle.switch(app)


if __name__ == "__main__":
    username = "pw"
    password = "1qazXSW#"
    dsKey = ""
    system_name = "Crawler"
    login_tool(system_name=system_name, username=username, password=password, dsKey=dsKey)