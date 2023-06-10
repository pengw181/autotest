# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/8/17 下午3:44

import os
import shutil
from datetime import datetime
from src.main.python.lib.logger import log
from src.main.python.db.SQLHelper import SQLUtil
from src.main.python.lib.globals import gbl
from src.main.python.lib.localAddr import getLocalAddress


class Initiation:

    def __init__(self):
        self.inited = False

    @staticmethod
    def clear_var():

        # 清空过程变量值
        gbl.temp.clear()
        log.info("清理流程过程变量")

    @staticmethod
    def remove_download_file():

        # 清空下载目录里的文件
        download_path = gbl.service.get("ProjectPath") + '/src/main/python/download/'
        for f in os.listdir(download_path):
            file_data = download_path + f
            if os.path.isfile(file_data):
                os.remove(file_data)
        log.info("清理临时下载文件")

    @staticmethod
    def remove_screen_shot():

        # 清空截图文件
        screen_shot_path = gbl.service.get("ProjectPath") + '/src/main/python/screenShot/'
        for f in os.listdir(screen_shot_path):
            file_data = screen_shot_path + f
            if os.path.isfile(file_data):   # 删除文件
                os.remove(file_data)
            elif os.path.isdir(file_data):      # 文件夹
                shutil.rmtree(file_data)
        log.info("清理截图文件")

    @staticmethod
    def init_zg_table(db, server_var_name, table_zh_name, temp_type):

        # 根据中文名，获取表英文名
        sql_util = SQLUtil(db, "main")
        sql = "select zg_table_name from zg_temp_cfg where zg_temp_name='{0}' and zg_temp_type='{1}'".format(
            table_zh_name, temp_type)
        table_en_name = sql_util.select(sql)
        if table_en_name is None:
            log.warning("表【{0}】不存在".format(table_zh_name))
        # 赋值给业务变量
        gbl.service.set(server_var_name, table_en_name)

    @staticmethod
    def init_cust_table(db, server_var_name, table_zh_name, update_mode):

        # 根据中文名，获取表英文名
        sql_util = SQLUtil(db, "main")
        sql = "select table_name_en from edata_custom_temp where table_name_ch='{0}' and update_mode='{1}'".format(
            table_zh_name, update_mode)
        table_en_name = sql_util.select(sql)
        if table_en_name is None:
            log.warning("{0} 表【{1}】不存在".format(db, table_zh_name))
        # 赋值给业务变量
        gbl.service.set(server_var_name, table_en_name)


def initiation_work():

    init = Initiation()
    gbl.service.set("RunEnd", False)

    # 文件清理
    if not gbl.service.get("ServerInit"):
        init.remove_download_file()
        init.remove_screen_shot()
    init.clear_var()

    # 关闭浏览器
    if gbl.service.get("browser"):
        gbl.service.get("browser").quit()
        gbl.service.set("browser", None)
        gbl.service.set("WinHandles", None)

    gbl.temp.set("ErrorMsg", "")

    environment = gbl.service.get("environment")
    application = gbl.service.get("application")

    # 根据当前时间设置时间
    now = datetime.now()
    gbl.service.set('Y', now.strftime('%Y'))
    gbl.service.set('YM', now.strftime('%Y%m'))
    gbl.service.set('YMD', now.strftime('%Y%m%d'))

    # 设置当前默认数据库
    gbl.service.set('Database', environment)
    gbl.service.set('DatabaseType', gbl.db.get(environment).get("type"))

    if application == "VisualModeler":

        # 业务变量赋值
        init.init_zg_table(environment, "BasicInfoTableName", "auto_网元基础信息表", "1")
        init.init_zg_table(environment, "SupplyInfoTableName", "auto_网元辅助资料", "2")
        init.init_zg_table(environment, "OtherInfoTableName", "auto_网元其它资料", "3")

        init.init_cust_table(environment, "Edata1TableName", "auto_数据拼盘_二维表模式", "2D_TABLE_MODE")
        init.init_cust_table(environment, "Edata2TableName", "auto_数据拼盘_列更新模式", "NORMAL_MODE")
        init.init_cust_table(environment, "Edata3TableName", "auto_数据拼盘_分段模式", "SUBSECTION_MODE")
        init.init_cust_table(environment, "Edata4TableName", "auto_数据拼盘_数据模式", "DATA_MODE")
        init.init_cust_table(environment, "Edata5TableName", "auto_数据拼盘_合并模式join", "JOIN_MODE")

        # 邮箱密码
        gbl.service.set('EmailPwd', "P!w0401030990")
        gbl.service.set('EmailPwd2', "Pw0401030990")  # outlook邮箱

        gbl.service.set('MockIp', getLocalAddress())
        # 第三方系统平台网络标识, 3.2爬虫服务使用，低于3.2使用内部网/外部网标识
        if gbl.service.get("crawlerVersion") == 'cmcc':
            # noinspection PyBroadException
            try:
                sql_util = SQLUtil(environment, "main")
                sql = "select platform_nw_name from tn_platform_nw_tag_init where belong_id='{0}' and domain_id='{1}'".format(
                    gbl.service.get("BelongID"), gbl.service.get("DomainID"))
                platform_nw_name = sql_util.select(sql)
            except Exception:
                platform_nw_name = None
            if platform_nw_name is None:
                platform_nw_name = "内部网"
        else:
            platform_nw_name = "内部网"
        gbl.service.set('PlatformNwName', platform_nw_name)

        # 数据库管理建大数据表表名配置
        gbl.service.set('BigImportTable', "AUTO_BIG_IMPORT")

    if application == "AlarmPlatform":

        gbl.service.set('DatabaseP', "v31.postgres")
        gbl.service.set('DatabaseO', "v31.oracle")
        gbl.service.set('DatabaseM', "v31.maria")

        # 告警平台用告警表名
        init.init_zg_table(environment, "AlarmTableName", "auto_测试告警表", "3")
        # 告警平台用输出表名
        init.init_zg_table(environment, "OutputTableName", "auto_测试输出表", "3")
        gbl.service.set('AlarmRuleTableName', gbl.service.get('AlarmTableName'))
        sql_util = SQLUtil(environment, "alarm")
        sql = "SELECT database_name FROM alarm_database_info WHERE database_info_id = 'default-{}'".format(
            gbl.service.get("BelongID"))
        default_database_id = sql_util.select(sql)
        gbl.service.set('DefaultDBName', default_database_id)

        # 告警推送计划接收人
        sql_util = SQLUtil(environment, "sso")
        sql = "select user_name from tn_user where user_id='{0}'".format(gbl.service.get("LoginUser"))
        current_user_name = sql_util.select(sql)
        gbl.service.set("TreeUser", current_user_name)
        gbl.service.set("TreeOrg1", "海珠区事业办")
        gbl.service.set("TreeOrg2", "鱼珠办公室")

    # 业务初始化完成
    gbl.service.set("ServerInit", True)
