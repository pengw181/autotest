# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/29 下午5:14

from common.log.logger import log
from app.AiSee.main.loginPage import login
from common.variable.globalVariable import *
from common.login.loads import login_config
from common.login.staticsLogin import login_tool
from app.AiSee.main.mainPage import AiSee
from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from common.page.handle.windows import WindowHandles
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# 定义一个自动检测登录vm的装饰器
def auto_enter_vm(func):
    def wrapper(*args, **kwargs):
        if args[0] in ['LoginAiSee', 'EnterDomain']:
            pass
        elif args[0].find("Dashboard") == 0:
            # 如果方法名是Dashboard开头，表示是仪表盘操作，需要在上一步用例使用AccessReportDashboard进入仪表盘
            pass
        else:
            browser = get_global_var("browser")
            try:
                browser.find_element(By.XPATH, "//*[@id='userName']")
            except AttributeError:
                log.info("当前未登录，自动执行登录操作")
                arg1 = {
                    "用户名": get_global_var("LoginUser"),
                    "密码": get_global_var("LoginPwd")
                }
                username = arg1.get("用户名")
                password = arg1.get("密码")
                login(username, password)

                arg2 = {
                    "归属": get_global_var("Belong"),
                    "领域明细": get_global_var("Domain")
                }
                action = AiSee()
                action.close_tips()
                belong = arg2.get("归属")
                domain = arg2.get("领域明细")
                action.enter_domain(belong, domain)
            except NoSuchElementException:
                windows = WindowHandles()
                if browser.current_window_handle == windows.win_handles.get("流程图编辑器"):
                    log.info("当前处于流程图编辑器窗口")
                elif browser.current_window_handle == windows.win_handles.get("告警平台"):
                    log.info("当前处于告警平台")
                elif browser.current_window_handle == windows.win_handles.get("仪表盘主配置页"):
                    log.info("当前处于仪表盘主配置页窗口")
                    windows.close("仪表盘主配置页")
                else:
                    log.info("当前已登录，未进入领域，自动进入{0}".format(get_global_var("Domain")))
                    arg2 = {
                        "归属": get_global_var("Belong"),
                        "领域明细": get_global_var("Domain")
                    }
                    action = AiSee()
                    belong = arg2.get("归属")
                    domain = arg2.get("领域明细")
                    action.enter_domain(belong, domain)
        return func(*args, **kwargs)
    return wrapper


# 定义一个自动检测登录aisee的装饰器
def auto_login_aisee(func):
    def wrapper(*args, **kwargs):
        if args[0] in ['LoginAiSee']:
            pass
        else:
            browser = get_global_var("browser")
            try:
                browser.find_element(By.XPATH, "//*[@id='userName']")
            except AttributeError:
                log.info("当前未登录，自动执行登录操作")
                arg1 = {
                    "用户名": get_global_var("LoginUser"),
                    "密码": get_global_var("LoginPwd")
                }
                username = arg1.get("用户名")
                password = arg1.get("密码")
                login(username, password)
            except NoSuchElementException:
                log.info("用户当前已登录")
        return func(*args, **kwargs)
    return wrapper


# 定义一个自动检测登录的装饰器
def auto_login_tool(func):
    def wrapper(*args, **kwargs):
        browser = get_global_var("browser")
        try:
            browser.find_element(By.XPATH, "//*[@menuid='CrawlerApp1000']")
        except AttributeError:
            log.info("当前未登录，自动执行登录操作")
            arg1 = {
                "系统": get_global_var("Application"),
                "用户名": login_config.get("username"),
                "密码": login_config.get("password"),
                "应用跳转url": login_config.get("redirect_url"),
                "appId": login_config.get("appid"),
                "领域明细": login_config.get("domain_detail"),
                "dsKey": login_config.get("dskey"),
                "客户": login_config.get("custom"),
                "签名秘钥": login_config.get("signature"),
                "语言": login_config.get("language"),
                "登录方式": login_config.get("login_type")
            }
            login_tool(system_name=arg1.get("系统"), username=arg1.get("用户名"), password=arg1.get("密码"),
                       redirect_url=arg1.get("应用跳转url"), appId=arg1.get("appId"), domain_detail=arg1.get("领域明细"),
                       dsKey=arg1.get("dsKey"), custom=arg1.get("客户"), signature=arg1.get("签名秘钥"),
                       language=arg1.get("语言"))
        return func(*args, **kwargs)
    return wrapper


# 定义一个自动从vm进入告警平台等其它平台的装饰器
def enter_platform(platform):
    def login_via_vm(func):
        def wrapper(*args, **kwargs):
            browser = get_global_var("browser")
            menu_map = {
                "告警平台": "告警-告警平台",
                "数据接入": "数据接入-数据接入平台",
                "云平台": "云平台-云平台",
                "OA审批": "OA审批-OA审批平台",
            }
            if browser.current_window_handle == get_global_var("WinHandles").get(platform):
                log.info("已登录【{}】".format(platform))
            else:
                dw = DoctorWho()
                log.info("开始从vm登录{}".format(platform))
                dw.choose_menu(menu_map.get(platform))
            return func(*args, **kwargs)
        return wrapper
    return login_via_vm
