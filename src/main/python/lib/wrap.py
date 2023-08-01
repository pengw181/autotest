# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/2/8 上午11:05

from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from src.main.python.core.loginPage import login
from src.main.python.core.staticsLogin import login_tool
from src.main.python.core.mainPage import AiSee
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.lib.windows import WindowHandles
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl
from src.main.python.lib.css import setVisible


class Wrap:

    def __init__(self, wrap_func, param=None):
        self.wrap_func = wrap_func
        self.param = param

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.wrap_func == "auto_enter_vm":
                auto_enter_vm(*args)
            elif self.wrap_func == "auto_login_aisee":
                auto_login_aisee(*args)
            elif self.wrap_func == "auto_login_tool":
                auto_login_tool()
            elif self.wrap_func == "enter_platform":
                enter_platform(self.param)
            elif self.wrap_func == "close_enter_dashboard":
                close_enter_dashboard()
            return func(*args, **kwargs)

        return wrapper


# 自动登录vm
def auto_enter_vm(*args):
    if args[0] in ['LoginAiSee', 'EnterDomain']:
        pass
    elif args[0].find("Dashboard") == 0:
        # 如果方法名是Dashboard开头，表示是仪表盘操作，需要在上一步用例使用AccessReportDashboard进入仪表盘
        pass
    else:
        browser = gbl.service.get("browser")
        try:
            browser.find_element(By.XPATH, "//*[@id='userName']")
        except AttributeError:
            log.info("当前未登录，自动执行登录操作")

            username = gbl.service.get("LoginUser")
            password = gbl.service.get("LoginPwd")
            login(username, password)

            action = AiSee()
            action.close_tips()
            belong = gbl.service.get("Belong")
            domain = gbl.service.get("Domain")
            action.enter_domain(belong, domain)
        except NoSuchWindowException:
            username = gbl.service.get("LoginUser")
            password = gbl.service.get("LoginPwd")
            login(username, password)

            action = AiSee()
            action.close_tips()
            belong = gbl.service.get("Belong")
            domain = gbl.service.get("Domain")
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
            elif browser.current_window_handle == windows.win_handles.get("数据管理"):
                log.info("当前处于数据管理窗口")
            elif browser.current_window_handle == windows.win_handles.get("一键启动"):
                log.info("当前处于一键启动窗口")
            elif browser.current_window_handle == windows.win_handles.get("数据库管理"):
                log.info("当前处于数据库管理窗口")
            else:
                log.info("当前已登录，未进入领域，自动进入{0}".format(gbl.service.get("Domain")))

                action = AiSee()
                belong = gbl.service.get("Belong")
                domain = gbl.service.get("Domain")
                action.enter_domain(belong, domain)


# 自动登录aisee
def auto_login_aisee(*args):
    if args[0] in ['LoginAiSee']:
        pass
    else:
        browser = gbl.service.get("browser")
        try:
            browser.find_element(By.XPATH, "//*[@id='userName']")
        except AttributeError:
            log.info("当前未登录，自动执行登录操作")

            username = gbl.service.get("LoginUser")
            password = gbl.service.get("LoginPwd")
            login(username, password)
        except NoSuchElementException:
            log.info("用户当前已登录")


# 测试登录页面登录
def auto_login_tool():
    browser = gbl.service.get("browser")
    try:
        browser.find_element(By.XPATH, "//*[@menuid='CrawlerApp1000']")
    except AttributeError:
        log.info("当前未登录，自动执行登录操作")
        arg1 = {
            "系统": gbl.service.get("application"),
            "用户名": gbl.login.get("username"),
            "密码": gbl.login.get("password"),
            "应用跳转url": gbl.login.get("redirect_url"),
            "appId": gbl.login.get("appid"),
            "领域明细": gbl.login.get("domain_detail"),
            "dsKey": gbl.login.get("dskey"),
            "客户": gbl.login.get("custom"),
            "签名秘钥": gbl.login.get("signature"),
            "语言": gbl.login.get("language"),
            "登录方式": gbl.login.get("login_type")
        }
        login_tool(system_name=arg1.get("系统"), username=arg1.get("用户名"), password=arg1.get("密码"),
                   redirect_url=arg1.get("应用跳转url"), appId=arg1.get("appId"), domain_detail=arg1.get("领域明细"),
                   dsKey=arg1.get("dsKey"), custom=arg1.get("客户"), signature=arg1.get("签名秘钥"),
                   language=arg1.get("语言"))


# 自动从vm进入告警平台等其它平台
def enter_platform(platform):
    browser = gbl.service.get("browser")
    menu_map = {
        "告警平台": "告警-告警平台",
        "数据接入": "数据接入-数据接入平台",
        "云平台": "云平台-云平台",
        "OA审批": "OA审批-OA审批平台",
    }
    if browser.current_window_handle == gbl.service.get("WinHandles").get(platform):
        log.info("已登录【{}】".format(platform))
    else:
        dw = DoctorWho()
        log.info("开始从vm登录{}".format(platform))
        dw.choose_menu(menu_map.get(platform))


# 关闭并进入仪表盘配置页面
def close_enter_dashboard():
    browser = gbl.service.get("browser")
    while True:
        # noinspection PyBroadException
        try:
            sleep(1)
            browser.find_element(By.XPATH, "//*[@class='tabs-title' and text()='仪表盘列表']")
            break
        except Exception:
            class_name = "index-menu"
            setVisible(browser, class_name)
            browser.find_element(By.XPATH, "//*[@class='index-menu']/a[@class='close']").click()

#
# class LoadCaseWrap:
#
#     def __init__(self, case_file):
#         self.case_file = case_file
#         global_config()
#         initiation_work()
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             application = gbl.service.get("application")
#             case_file_path = gbl.service.get("TestCasePath") + application + self.case_file
#             if not os.path.exists(case_file_path):
#                 raise FileNotFoundError("无法找到测试用例文件, {}".format(case_file_path))
#             workbook = xlrd.open_workbook(case_file_path, formatting_info=True)
#             sheets = workbook.sheet_by_index(0)
#             gbl.service.set("CaseSheets", sheets)
#             log.info("设置CaseSheets")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#
# class ConstructCaseWrap:
#
#     def __init__(self, case_order):
#         self.case_order = case_order
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             sheet_case = gbl.service.get("CaseSheets")
#             self.case_rows = sheet_case.row_values(self.case_order+1)
#             # 用例名称
#             case_name = self.case_rows[0]
#             # 预置条件
#             case_pres = self.case_rows[2]
#             # 操作步骤
#             case_action = self.case_rows[3]
#             case_action = json.dumps(json.loads(case_action), indent=4, ensure_ascii=False)
#             # 预期结果
#             case_checks = self.case_rows[4]
#             gbl.service.set("CaseConstruct", [case_name, case_pres, case_action, case_checks])
#             log.info("分解CaseSheets，得到CaseConstruct")
#             return func(*args, **kwargs)
#
#         return wrapper
