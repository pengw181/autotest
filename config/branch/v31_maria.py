# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午3:21

from common.variable.globalVariable import *
from datetime import datetime
from config.loads import db_config
from common.tools.localAddr import getLocalAddress
from database.SQLHelper import SQLUtil


def serviceInit():

    Environment = get_global_var("Environment")
    local_ip = getLocalAddress()
    db_type = db_config.get(Environment).get("type")

    # 根据当前时间设置时间
    now = datetime.now()
    set_global_var("Y", now.strftime('%Y'))
    set_global_var("YM", now.strftime('%Y%m'))
    set_global_var("YMD", now.strftime('%Y%m%d'))

    # 网元设置
    set_global_var("NetunitMME1", "pw_华为_MME_ME60_00")
    set_global_var("NetunitMME2", "pw_华为_MME_ME60_01")
    set_global_var("NetunitMME3", "pw_华为_MME_ME60_02")

    # 登录信息
    set_global_var("PageUrl", "http://192.168.88.116:9311/AiSee/html/login/login.html")
    set_global_var("SystemLoginUrl", "https://192.168.88.116:9109/statics/html/login.html#")
    set_global_var("BelongID", "440100")
    set_global_var("DomainID", "AiSeeCore")
    set_global_var("LoginUser", "pw")
    set_global_var("LoginPwd", "1qazXSW@")
    set_global_var("Belong", "广州市")
    set_global_var("Domain", "广州核心网")

    # 设置当前默认数据库
    set_global_var("Database", Environment)

    # 第三方系统测试系统ip
    set_global_var("ThirdSystem", "http://192.168.88.116:9311")
    set_global_var("ThirdSystemHttps", "https://192.168.88.116:9317")
    # 第三方系统平台网络标识
    """
    3.2爬虫服务使用，低于3。2使用内部网/外部网标识
    """
    # noinspection PyBroadException
    try:
        sql_util = SQLUtil(Environment, "main")
        sql = "select platform_nw_name from tn_platform_nw_tag_init where belong_id='{0}' and domain_id='{1}'".format(
            get_global_var("BelongID"), get_global_var("DomainID"))
        platform_nw_name = sql_util.select(sql)
    except Exception:
        platform_nw_name = None
    if platform_nw_name is None:
        platform_nw_name = "内部网"
    set_global_var("PlatformNwName", platform_nw_name)

    # 第三方接口模拟ip
    set_global_var("MockIp", local_ip)

    # 当前数据库类型
    set_global_var("DatabaseType", db_type)

    # 邮箱密码
    set_global_var("EmailPwd", "P!w0401030990")
    set_global_var("EmailPwd2", "Pw0401030990")  # outlook邮箱

    # 告警平台用告警规则表名，根据数据库类型自动选择
    if get_global_var("DatabaseType") == "oracle":
        set_global_var("AlarmTableName", get_global_var("AlarmTableNameO"), "service")
    elif get_global_var("DatabaseType") == "mysql":
        set_global_var("AlarmTableName", get_global_var("AlarmTableNameM"), "service")
    else:
        set_global_var("AlarmTableName", get_global_var("AlarmTableNameP"), "service")

    # 告警平台用告警规则表名，根据数据库类型自动选择
    set_global_var("AlarmRuleTableName", get_global_var("AlarmTableName"), "service")
