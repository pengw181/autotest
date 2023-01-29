# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/29 下午4:39

from client.app.AiSee.netunit.netunitInfo import NetUnit
from client.app.AiSee.netunit.account import AccountTemp
from client.app.AiSee.netunit.report import ConnectTestReport
from client.app.AiSee.user.org import Organization
from client.app.AiSee.user.user import User
from service.lib.log.logger import log
from client.page.wrapper.autoLogin import auto_login_aisee


@auto_login_aisee
def actions(func, param):

    run_flag = True

    # 网元信息(自身)
    if func == "AddNetUnit":
        action = NetUnit()
        action.add(netunit_name=param.get("网元名称"), netunit_type=param.get("网元类型"), ip=param.get("网元IP"),
                   vendor=param.get("生产厂家"), netunit_model=param.get("设备型号"), state=param.get("业务状态"),
                   maxCocurrentNum=param.get("最大并发数"))

    elif func == "NetUnitLoginConfig":
        action = NetUnit()
        config = param.get("登录信息配置")
        action.login_config(netunit_name=param.get("目标网元"), login_model_name=config.get("登录模式"),
                            terminal=config.get("终端配置"), cmd_config=config.get("指令配置"))

    elif func == "NetUnitDataClear":
        action = NetUnit()
        action.data_clear(netunit_name=param.get("网元名称"))

    elif func == "UpdateNetUnit":
        action = NetUnit()
        update_map = param.get("修改内容")
        action.update(netunit=param.get("目标网元"), netunit_name=update_map.get("网元名称"),
                      netunit_type=update_map.get("网元类型"), ip=update_map.get("网元IP"),
                      vendor=update_map.get("生产厂家"), netunit_model=update_map.get("设备型号"),
                      state=update_map.get("业务状态"), maxCocurrentNum=update_map.get("最大并发数"))

    elif func == "DeleteNetUnit":
        action = NetUnit()
        action.delete(netunit_name=param.get("网元名称"))

    # 统一账号配置
    elif func == "AddAccountTemp":
        action = AccountTemp()
        action.add(account_temp_name=param.get("账号模版名称"), account_temp_type=param.get("账号模版类型"),
                   remark=param.get("账号模版用途"))

    elif func == "UpdateAccountTemp":
        action = AccountTemp()
        update_map = param.get("修改内容")
        action.update(obj_account_temp=param.get("目标账号模版"), account_temp_name=update_map.get("账号模版名称"),
                      account_temp_type=update_map.get("账号模版类型"), remark=update_map.get("账号模版用途"))

    elif func == "SetAccount":
        action = AccountTemp()
        account_info = param.get("账号信息")
        action.set_account(obj_account_temp=param.get("目标账号模版"), operation=account_info.get("账号操作类型"),
                           account_scope=account_info.get("账号作用域"), username=account_info.get("用户名"),
                           password=account_info.get("密码"))

    # 连通性测试报告
    elif func == "GetConnectReport":
        action = ConnectTestReport()
        action.choose(test_user=param.get("触发用户"), connect_type=param.get("测试类型"))

    # 用户管理
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
        action.delete(user=param.get("用户"))

    elif func == "ClearUser":
        action = User()
        action.clear(user=param.get("用户名称"), fuzzy_match=param.get("模糊匹配"))

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