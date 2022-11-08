# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午3:21

from service.lib.variable.globalVariable import *
from config.loads import db_config
from service.lib.tools.localAddr import getLocalAddress


def serviceInit():

    Environment = get_global_var("Environment")
    local_ip = getLocalAddress()
    db_type = db_config.get(Environment).get("type")

    # 网元设置
    set_global_var("NetunitMME1", "auto_MME_001")
    set_global_var("NetunitMME2", "auto_MME_002")
    set_global_var("NetunitMME3", "auto_MME_003")

    # 登录信息
    set_global_var("PageUrl", "http://192.168.88.50/AiSee/html/login/login.html")
    set_global_var("SystemLoginUrl", "https://192.168.88.116:9109/statics/html/login.html#")
    set_global_var("BelongID", "440300")
    set_global_var("DomainID", "AiSeeWY")
    set_global_var("LoginUser", "pw")
    set_global_var("LoginPwd", "1qazXSW@")
    set_global_var("Belong", "深圳市")
    set_global_var("Domain", "深圳市网络优化")

    # 第三方系统测试系统ip
    set_global_var("ThirdSystem", "http://192.168.88.50")
    set_global_var("ThirdSystemHttps", "https://192.168.88.116:9317")

    # 第三方接口模拟ip
    set_global_var("MockIp", local_ip)

    # 当前数据库类型
    set_global_var("DatabaseType", db_type)

    # 告警平台用告警规则表名，根据数据库类型自动选择
    set_global_var("AlarmRuleTableName", get_global_var("AlarmTableName"), "service")
    set_global_var("DefaultDBName", "AiSee-" + get_global_var("Domain"), "service")
