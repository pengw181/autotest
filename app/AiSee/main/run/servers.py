# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/29 下午4:39

from app.AiSee.main.mainPage import AiSee
from app.AiSee.netunit.netunitInfo import NetUnit
from app.AiSee.netunit.account import AccountTemp
from app.AiSee.netunit.connectReport import ConnectTestReport
from common.log.logger import log
from common.wrapper.autoLogin import auto_login_aisee
from app.AiSee.netunit.menu import choose_domain


@auto_login_aisee
def actions(func, param):

    # 从menu进入
    aisee = AiSee()
    menu_name = "网元管理"
    if not aisee.in_menu(menu_name):
        aisee.choose_menu_func(func=menu_name)
        log.info("进入 >> {}".format(menu_name))
        choose_domain(domain="广州核心网")
    run_flag = True

    if func == "AddNetUnit":
        action = NetUnit()
        action.add(netunit_name=param.get("网元名称"), netunit_type=param.get("网元类型"), ip=param.get("网元IP"),
                   vendor=param.get("生产厂家"), netunit_model=param.get("设备型号"), state=param.get("业务状态"),
                   maxCocurrentNum=param.get("最大并发数"))

    elif func == "NetUnitLoginConfig":
        action = NetUnit()
        config = param.get("登录信息配置")
        action.login_config(obj_netunit=param.get("目标网元"), login_model_name=config.get("登录模式"),
                            terminal=config.get("终端配置"), cmd_config=config.get("指令配置"))

    elif func == "NetUnitDataClear":
        action = NetUnit()
        action.data_clear(obj_netunit=param.get("目标网元"))

    elif func == "UpdateNetUnit":
        action = NetUnit()
        update_map = param.get("修改内容")
        action.update(obj_netunit=param.get("目标网元"), netunit_name=update_map.get("网元名称"),
                      netunit_type=update_map.get("网元类型"), ip=update_map.get("网元IP"),
                      vendor=update_map.get("生产厂家"), netunit_model=update_map.get("设备型号"),
                      state=update_map.get("业务状态"), maxCocurrentNum=update_map.get("最大并发数"))

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

    elif func == "GetConnectReport":
        action = ConnectTestReport()
        action.choose(test_user=param.get("触发用户"), connect_type=param.get("测试类型"))

    else:
        log.error("无效的动作函数")
        run_flag = False

    return run_flag


"""
{
    "操作": "AddAccountTemp",
    "参数": {
        "账号模版名称": "pw自动化账号模版",
        "账号模版类型": "本身",
        "账号模版用途": "登录123"
    }
}


{
    "操作": "SetAccount",
    "参数": {
        "目标账号模版": "pw自动化账号模版",
        "账号信息": {
            "账号操作类型": "添加",
            "账号作用域": "公有",
            "用户名": "u_normal",
            "密码": "u_normal_pass"
        }
    } 
}


"""