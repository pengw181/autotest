# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/29 下午4:39

from src.main.python.core.app.AiSee.netunit.netunitInfo import NetUnit
from src.main.python.core.app.AiSee.netunit.netunitInfo import LoginConfig
from src.main.python.core.app.AiSee.netunit.netunitInfo import NetunitRelation
from src.main.python.core.app.AiSee.netunit.vendor import Vendor
from src.main.python.core.app.AiSee.netunit.level import LevelInfo
from src.main.python.core.app.AiSee.netunit.mode import LoginMode
from src.main.python.core.app.AiSee.netunit.account import AccountTemp
from src.main.python.core.app.AiSee.netunit.account import Account
from src.main.python.core.app.AiSee.netunit.terminal import Terminal
from src.main.python.core.app.AiSee.netunit.jump import JumpCmd
from src.main.python.core.app.AiSee.netunit.template import Template
from src.main.python.core.app.AiSee.netunit.confirm import Confirm
from src.main.python.core.app.AiSee.netunit.connect import ConnectTest
from src.main.python.core.app.AiSee.netunit.report import ConnectTestReport
from src.main.python.core.app.AiSee.user.org import Organization
from src.main.python.core.app.AiSee.user.user import User
from src.main.python.core.app.AiSee.user.user import DataAssign
from src.main.python.lib.logger import log
from src.main.python.lib.wrap import Wrap


@Wrap(wrap_func='auto_login_aisee')
def actions(func, param):

    run_flag = True

    # 网元信息(自身)
    if func == "AddNetUnit":
        action = NetUnit()
        action.add(netunit_name=param.get("网元名称"), netunit_type=param.get("网元类型"), ip=param.get("网元IP"),
                   vendor=param.get("生产厂家"), netunit_model=param.get("设备型号"), state=param.get("业务状态"),
                   max_concurrent_num=param.get("最大并发数"))

    elif func == "UpdateNetUnit":
        action = NetUnit()
        update_map = param.get("修改内容")
        action.update(netunit=param.get("网元名称"), netunit_name=update_map.get("网元名称"),
                      netunit_type=update_map.get("网元类型"), ip=update_map.get("网元IP"),
                      vendor=update_map.get("生产厂家"), netunit_model=update_map.get("设备型号"),
                      state=update_map.get("业务状态"), max_concurrent_num=update_map.get("最大并发数"))

    elif func == "DeleteNetUnit":
        action = NetUnit()
        action.delete(netunit_name=param.get("网元名称"))

    elif func == "NetUnitDataClear":
        action = NetUnit()
        action.data_clear(netunit_name=param.get("网元名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "NELoginConfigSetTerminal":
        action = LoginConfig(netunit_name=param.get("网元名称"))
        action.set_terminal(login_model_name=param.get("登录模式"), terminal=param.get("终端配置"))

    elif func == "NELoginConfigSetCmd":
        action = LoginConfig(netunit_name=param.get("网元名称"))
        action.set_login_cmd(login_model_name=param.get("登录模式"), login_command=param.get("指令配置"))

    elif func == "NEAssignRela":
        action = NetunitRelation(netunit_name=param.get("网元名称"))
        action.assign_rela(rela_type=param.get("关系类型"), ne_list=param.get("网元列表"), keyword=param.get("关键字"))

    # 设备厂家
    elif func == "AddVendor":
        action = Vendor()
        action.add_vendor(vendor_cname=param.get("厂家中文名"), vendor_ename=param.get("厂家英文名"),
                          search_if_exist=param.get("搜索是否存在"))

    elif func == "AddModel":
        action = Vendor()
        action.add_model(belong_vendor=param.get("所属厂家"), model=param.get("设备型号"),
                         search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateVendor":
        action = Vendor()
        update_map = param.get("修改内容")
        action.update_vendor(query=param.get("查询条件"), vendor_cname=update_map.get("厂家中文名"),
                             vendor_ename=update_map.get("厂家英文名"))

    elif func == "UpdateModel":
        action = Vendor()
        update_map = param.get("修改内容")
        action.update_model(query=param.get("查询条件"), model=update_map.get("设备型号"))

    # 网元类型
    elif func == "AddLevel":
        action = LevelInfo()
        action.add(up_level=param.get("上级层级"), level_name=param.get("层级名称"), level_type=param.get("层级类型"),
                   search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateLevel":
        action = LevelInfo()
        update_map = param.get("修改内容")
        action.update(level=param.get("网元类型"), up_level=update_map.get("上级层级"),
                      level_name=update_map.get("层级名称"), level_type=update_map.get("层级类型"))

    # 网元登录模式
    elif func == "AddLoginMode":
        action = LoginMode()
        action.add(cfg_level_type=param.get("网元类型"), login_type_name=param.get("登录模式名称"),
                   remark=param.get("登录模式描述"), search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateLoginMode":
        action = LoginMode()
        update_map = param.get("修改内容")
        action.update(query=param.get("查询条件"), login_type_name=update_map.get("登录模式名称"),
                      remark=update_map.get("登录模式描述"))

    # 统一账号配置
    elif func == "AddAccountTemp":
        action = AccountTemp()
        action.add(account_temp_name=param.get("账号模版名称"), account_temp_type=param.get("账号模版类型"),
                   remark=param.get("账号模版用途"), search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateAccountTemp":
        action = AccountTemp()
        update_map = param.get("修改内容")
        action.update(account_temp=param.get("账号模版名称"), account_temp_name=update_map.get("账号模版名称"),
                      account_temp_type=update_map.get("账号模版类型"), remark=update_map.get("账号模版用途"))

    elif func == "AddAccount":
        action = Account(account_temp_name=param.get("账号模版名称"))
        action.add(account_scope=param.get("账号作用域"), username=param.get("用户名"), password=param.get("密码"))

    elif func == "UpdateAccount":
        action = Account(account_temp_name=param.get("账号模版名称"))
        update_map = param.get("修改内容")
        action.update(account_scope=param.get("账号作用域"), creator=param.get("创建人"), username=update_map.get("用户名"),
                      password=update_map.get("密码"))

    elif func == "DeleteAccount":
        action = Account(account_temp_name=param.get("账号模版名称"))
        action.delete(account_scope=param.get("账号作用域"), creator=param.get("创建人"))

    elif func == "IssueAccount":
        action = Account(account_temp_name=param.get("账号模版名称"))
        action.issue_account(account_scope=param.get("账号作用域"), creator=param.get("创建人"),
                             issue_scope=param.get("下发对象类型"), query=param.get("查询条件"),
                             issue_obj=param.get("下发对象"), issue_type=param.get("下发方式"))

    elif func == "AccountDataClear":
        action = Account(account_temp_name=param.get("账号模版名称"))
        action.data_clear(creator=param.get("创建人"))

    # 统一终端配置
    elif func == "AddTerminal":
        action = Terminal()
        action.add(terminal_name=param.get("终端名称"), terminal_type=param.get("终端类型"),
                   account_temp=param.get("账号名称"), charset=param.get("字符集"),
                   expect_return=param.get("期待返回符"), fail_return=param.get("失败返回符"),
                   terminal_ip=param.get("终端IP"), terminal_port=param.get("终端端口"),
                   remark=param.get("用途"), login_cmd=param.get("登录指令"),
                   search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateTerminal":
        action = Terminal()
        update_map = param.get("修改内容")
        action.update(terminal=param.get("终端名称"), terminal_name=update_map.get("终端名称"),
                      terminal_type=update_map.get("终端类型"), account_temp=update_map.get("账号名称"),
                      charset=update_map.get("字符集"), expect_return=update_map.get("期待返回符"),
                      fail_return=update_map.get("失败返回符"), terminal_ip=update_map.get("终端IP"),
                      terminal_port=update_map.get("终端端口"), remark=update_map.get("用途"),
                      login_cmd=update_map.get("登录指令"))

    elif func == "TestTerminal":
        action = Terminal()
        action.test_terminal(query=param.get("查询条件"))

    elif func == "TestAllTerminal":
        action = Terminal()
        action.test_all_terminal(query=param.get("查询条件"))

    # 统一登录指令配置
    elif func == "AddJumpCmdTemp":
        action = JumpCmd()
        action.add(cmd_temp_name=param.get("登录指令名称"), remark=param.get("登录指令用途"), command=param.get("指令配置"),
                   search_if_exist=param.get("搜索是否存在"))

    elif func == "UpdateJumpCmdTemp":
        action = JumpCmd()
        update_map = param.get("修改内容")
        action.update(cmd_temp=param.get("登录指令名称"), cmd_temp_name=update_map.get("登录指令名称"),
                      remark=update_map.get("登录指令用途"), command=update_map.get("指令配置"))

    # 统一网元配置
    elif func == "AddTemplate":
        action = Template()
        action.add(template_name=param.get("模版名称"), netunit_type=param.get("网元类型"),
                   login_type=param.get("登录模式"), remark=param.get("用途说明"), login_step=param.get("登录配置"))

    elif func == "UpdateTemplate":
        action = Template()
        update_map = param.get("修改内容")
        action.update(template=param.get("模版名称"), template_name=update_map.get("模版名称"),
                      remark=update_map.get("用途说明"), login_step=update_map.get("登录配置"))

    elif func == "DeleteTemplate":
        action = Template()
        action.delete(template_name=param.get("模版名称"))

    elif func == "TemplateDataClear":
        action = Template()
        action.data_clear(template_name=param.get("模版名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "TemplateBindNE":
        action = Template()
        action.bind_netunit(template_name=param.get("模版名称"), netunit_name=param.get("网元名称"),
                            vendor=param.get("厂家"), model=param.get("设备型号"),
                            to_assigned_list=param.get("待分配网元"), to_unassigned_list=param.get("待移除网元"),
                            assign_type=param.get("分配方式"))

    elif func == "TemplateDelivery":
        action = Template()
        action.delivery(template_name=param.get("模版名称"))

    # 登录配置确认
    elif func == "ConfirmAll":
        action = Confirm()
        action.confirm_all(query=param.get("查询条件"))

    elif func == "ConfirmSelected":
        action = Confirm()
        action.confirm_selected(query=param.get("查询条件"), netunit_list=param.get("网元列表"))

    elif func == "CancelSelected":
        action = Confirm()
        action.cancel_selected(query=param.get("查询条件"), netunit_list=param.get("网元列表"))

    # 连通性测试
    elif func == "TestSelectedNetunit":
        action = ConnectTest()
        action.test_selected(query=param.get("查询条件"), netunit_list=param.get("网元列表"))

    elif func == "TestAllNetunit":
        action = ConnectTest()
        action.test_all(query=param.get("查询条件"))

    # 连通性测试报告
    elif func == "GetConnectReport":
        action = ConnectTestReport()
        action.get_connect_result(query=param.get("查询条件"))

    elif func == "GetConnectDetailLog":
        action = ConnectTestReport()
        action.get_connect_result_detail(query=param.get("查询条件"), netunit_name=param.get("网元名称"))

    elif func == "ConnectRetest":
        action = ConnectTestReport()
        action.connect_retest(query=param.get("查询条件"))

    elif func == "ConnectDetailRetest":
        action = ConnectTestReport()
        action.connect_detail_retest(query=param.get("查询条件"), netunit_name=param.get("网元名称"))

    # 组织结构管理
    elif func == "AddOrganization":
        action = Organization()
        action.addOrg(node_name=param.get("节点名称"), parent_org_name=param.get("上级组织"),
                      org_name=param.get("组织名称"))

    elif func == "UpdateOrganization":
        action = Organization()
        action.updateOrg(node_name=param.get("节点名称"), parent_org_name=param.get("上级组织"),
                         org_name=param.get("组织名称"))

    elif func == "DeleteOrganization":
        action = Organization()
        action.deleteOrg(node_name=param.get("节点名称"))

    elif func == "ClearOrganization":
        action = Organization()
        action.clearOrg(node_name=param.get("节点名称"))

    # 用户管理
    elif func == "AddUser":
        action = User()
        action.add(user_id=param.get("登录账号"), user_name=param.get("用户名称"), sex=param.get("性别"),
                   password=param.get("用户密码"), belong_org=param.get("所属组织"), phone=param.get("电话号码"),
                   email=param.get("邮箱"), wechat=param.get("portal号"), is_alive=param.get("启用状态"),
                   is_lock=param.get("锁定状态"), pwd_overdue=param.get("密码有效期(天)"),
                   pwd_warn_days=param.get("密码过期预警天数"))

    elif func == "UpdateUser":
        action = User()
        update_map = param.get("修改内容")
        action.update(user=param.get("用户"), user_name=update_map.get("用户名称"), sex=update_map.get("性别"),
                      password=update_map.get("用户密码"), belong_org=update_map.get("所属组织"),
                      phone=update_map.get("电话号码"), email=update_map.get("邮箱"), wechat=update_map.get("portal号"),
                      is_alive=update_map.get("启用状态"), is_lock=update_map.get("锁定状态"),
                      pwd_overdue=update_map.get("密码有效期(天)"), pwd_warn_days=update_map.get("密码过期预警天数"))

    elif func == "DeleteUser":
        action = User()
        action.delete(user_id=param.get("登录账号"))

    elif func == "UserDataClear":
        action = User()
        action.data_clear(user_id=param.get("登录账号"), fuzzy_match=param.get("模糊匹配"))

    elif func == "AssignDataPermissions":
        action = DataAssign(user_id=param.get("登录账号"))
        action.assign_data_permissions(query=param.get("查询条件"), data_info=param.get("数据信息"),
                                       assign_type=param.get("分配类型"))

    else:
        log.error("无效的动作函数")
        run_flag = False

    return run_flag


"""
    {
        "操作": "AddUser",
        "参数": {
            "登录账号": "autom",
            "用户名称": "自动化测试1",
            "性别": "男",
            "用户密码": "12345678",
            "所属组织": "海珠区事业办",
            "电话号码": "13000000000",
            "邮箱": "auto1@125.com",
            "portal号": "auto1@125",
            "启用状态": "启用",
            "锁定状态": "未锁定",
            "密码有效期(天)": "60",
            "密码过期预警天数": "1"
        }
    }
    
    {
        "操作": "UpdateUser",
        "参数": {
            "用户": "autom",
            "修改内容": {
                "用户": "自动化测试2",
                "性别": "nv",
                "用户密码": "11111111",
                "所属组织": "黄浦区区事业办",
                "电话号码": "13100000000",
                "邮箱": "auto1@115.com",
                "portal号": "auto1@115",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "80",
                "密码过期预警天数": "3"
            }
        }
    }

    {
        "操作": "DeleteUser",
        "参数": {
            "用户": "autom"
        }
    }

    {
        "操作": "ClearUser",
        "参数": {
            "用户名称": "自动化测试",
            "模糊匹配": "是"
        }
    }

"""