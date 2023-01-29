# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:13

from client.page.wrapper.autoLogin import auto_enter_vm, enter_platform
from client.app.AlarmPlatform.connection.database import DatabaseConfig
from client.app.AlarmPlatform.connection.tableBelong import TableBelong
from client.app.AlarmPlatform.connection.ftp import FTP
from client.app.AlarmPlatform.config.metadata import MetaData
from client.app.AlarmPlatform.config.dictionary import Dictionary
from client.app.AlarmPlatform.config.alarmPlan import AlarmPlan
from client.app.AlarmPlatform.config.alarmRule import AlarmRule
from client.app.AlarmPlatform.config.msgTemplate import MsgTemplate
from client.app.AlarmPlatform.send.plan import SendPlan


@auto_enter_vm
@enter_platform(platform="告警平台")
def actions(func, param):

    run_flag = True

    # 关系型数据库配置
    if func == "AddDatabase":
        action = DatabaseConfig()
        action.add(database_type=param.get("数据库类型"), database_name=param.get("数据库名称"),
                   database_sid=param.get("服务名/SID"), address=param.get("连接地址"), port=param.get("端口"),
                   username=param.get("用户名"), password=param.get("密码"))

    elif func == "UpdateDatabase":
        action = DatabaseConfig()
        update_map = param.get("修改内容")
        action.update(obj=param.get("数据库名称"), database_type=update_map.get("数据库类型"),
                      database_name=update_map.get("数据库名称"), database_sid=update_map.get("服务名/SID"),
                      address=update_map.get("连接地址"), port=update_map.get("端口"), username=update_map.get("用户名"),
                      password=update_map.get("密码"))

    elif func == "TestDatabase":
        action = DatabaseConfig()
        action.test(database_name=param.get("数据库名称"))

    # 表归属配置
    elif func == "AddTableBelong":
        action = TableBelong()
        action.add(database_name=param.get("数据库名称"), table_en_ame=param.get("表英文名称"),
                   table_cn_Name=param.get("表中文名称"), table_object=param.get("表使用对象"),
                   table_period=param.get("表周期"), remark=param.get("备注"))

    elif func == "UpdateTableBelong":
        action = TableBelong()
        update_map = param.get("修改内容")
        action.update(obj=param.get("表中文名称"), table_cn_Name=update_map.get("表中文名称"), remark=update_map.get("备注"))

    elif func == "DeleteTableBelong":
        action = TableBelong()
        action.delete(table_cn_name=param.get("表中文名称"))

    elif func == "TableBelongDataClear":
        action = TableBelong()
        action.data_clear(table_cn_name=param.get("表中文名称"), fuzzy_match=param.get("模糊匹配"))

    # FTP配置
    elif func == "AddFTP":
        action = FTP()
        action.add(ftp_name=param.get("FTP名称"), host=param.get("连接地址"), port=param.get("端口"),
                   username=param.get("用户名"), password=param.get("密码"))

    elif func == "UpdateFTP":
        action = FTP()
        update_map = param.get("修改内容")
        action.update(obj=param.get("FTP名称"), ftp_name=update_map.get("FTP名称"), host=update_map.get("连接地址"),
                      port=update_map.get("端口"), username=update_map.get("用户名"), password=update_map.get("密码"))

    elif func == "TestFTP":
        action = FTP()
        action.test(ftp_name=param.get("FTP名称"))

    elif func == "DeleteFTP":
        action = FTP()
        action.delete(ftp_name=param.get("FTP名称"))

    elif func == "FTPDataClear":
        action = FTP()
        action.data_clear(ftp_name=param.get("FTP名称"), fuzzy_match=param.get("模糊匹配"))

    # 告警元数据配置
    elif func == "AddMetaData":
        action = MetaData()
        action.add(metadata_name=param.get("元数据名称"), database=param.get("数据库"), table_belong=param.get("表中文名"),
                   data_delay=param.get("数据时延"), remark=param.get("备注"), time_field=param.get("时间字段"),
                   time_field_format=param.get("时间格式"), prepare_field=param.get("待选字段"),
                   selected_field=param.get("已选字段"))

    elif func == "UpdateMetaData":
        action = MetaData()
        update_map = param.get("修改内容")
        action.update(obj=param.get("元数据名称"), metadata_name=update_map.get("元数据名称"),
                      data_delay=update_map.get("数据时延"), remark=update_map.get("备注"),
                      prepare_field=update_map.get("待选字段"), selected_field=update_map.get("已选字段"))

    elif func == "DeleteMetaData":
        action = MetaData()
        action.delete(metadata_name=param.get("元数据名称"))

    elif func == "MetaDataDataClear":
        action = MetaData()
        action.data_clear(metadata_name=param.get("元数据名称"), fuzzy_match=param.get("模糊匹配"))

    # 字典管理
    elif func == "AddDictionary":
        action = Dictionary()
        action.add(dict_name=param.get("字典组名称"), comment=param.get("字典描述"), dict_type=param.get("字典类型"),
                   table_belong=param.get("字典表名称"), item_key=param.get("关键字"), item_value=param.get("值"),
                   filter_set=param.get("过滤条件"))

    elif func == "UpdateDictionary":
        action = Dictionary()
        update_map = param.get("修改内容")
        action.update(obj=param.get("字典组名称"), dict_name=update_map.get("字典组名称"), comment=update_map.get("字典描述"),
                      filter_set=update_map.get("过滤条件"))

    elif func == "SetDictionaryDetail":
        action = Dictionary()
        action.set_dict_detail(dict_name=param.get("字典组名称"), detail=param.get("字典明细"))

    # 告警计划
    elif func == "AddAlarmPlan":
        action = AlarmPlan()
        action.add(plan_name=param.get("告警计划名称"), alarm_type=param.get("告警类型"), data_source=param.get("数据源名称"),
                   region_tag=param.get("标签分类"), domain_tag=param.get("领域标签"), plan_desc=param.get("计划描述"))

    elif func == "UpdateAlarmPlan":
        action = AlarmPlan()
        update_map = param.get("修改内容")
        action.update(obj=param.get("告警计划名称"), plan_name=update_map.get("告警计划名称"),
                      alarm_type=update_map.get("告警类型"), data_source=update_map.get("数据源名称"),
                      region_tag=update_map.get("标签分类"), domain_tag=update_map.get("领域标签"),
                      plan_desc=update_map.get("计划描述"))

    elif func == "UpdateAlarmPlanStatus":
        action = AlarmPlan()
        action.update_status(plan_name=param.get("告警计划名称"), set_status=param.get("状态"))

    elif func == "RedoAlarmPlan":
        action = AlarmPlan()
        action.redo(plan_name=param.get("告警计划名称"), start_time=param.get("开始时间"), end_time=param.get("结束时间"))

    elif func == "DeleteAlarmPlan":
        action = AlarmPlan()
        action.delete(plan_name=param.get("告警计划名称"))

    elif func == "RedoAlarmPlan":
        action = AlarmPlan()
        action.redo(plan_name=param.get("告警计划名称"))

    elif func == "AlarmPlanDataClear":
        action = AlarmPlan()
        action.data_clear(plan_name=param.get("告警计划名称"), fuzzy_match=param.get("模糊匹配"))

    # 告警规则
    elif func == "AddAlarmRule":
        action = AlarmRule()
        action.add(alarm_type=param.get("告警类型"), alarm_plan=param.get("告警计划"), basic_conf=param.get("基本信息配置"),
                   dimension_conf=param.get("告警维度配置"), filter_conf=param.get("过滤条件配置"),
                   result_conf=param.get("告警结果配置"), storage_conf=param.get("告警存储配置"))

    elif func == "UpdateAlarmRule":
        action = AlarmRule()
        update_map = param.get("修改内容")
        action.update(obj=param.get("规则名称"), basic_conf=update_map.get("基本信息配置"),
                      dimension_conf=update_map.get("告警维度配置"), filter_conf=update_map.get("过滤条件配置"),
                      result_conf=update_map.get("告警结果配置"), storage_conf=update_map.get("告警存储配置"))

    elif func == "UpdateAlarmRuleStatus":
        action = AlarmRule()
        action.update_status(rule_name=param.get("规则名称"), set_status=param.get("状态"))

    elif func == "DeleteAlarmRule":
        action = AlarmRule()
        action.delete(rule_name=param.get("规则名称"))

    elif func == "RedoAlarmRule":
        action = AlarmRule()
        action.redo(rule_name=param.get("规则名称"), start_time=param.get("开始时间"), end_time=param.get("结束时间"))

    elif func == "AlarmRuleDataClear":
        action = AlarmRule()
        action.data_clear(rule_name=param.get("规则名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "BatchEnableRule":
        action = AlarmRule()
        action.batch_enable(query=param.get("查询条件"))

    elif func == "BatchDisableRule":
        action = AlarmRule()
        action.batch_disable(query=param.get("查询条件"))

    # 消息模版
    elif func == "AddMsgTemplate":
        action = MsgTemplate()
        action.add(rule_name=param.get("告警规则名称"), msg_temp_name=param.get("消息模版名称"), title=param.get("模版标题"),
                   remark=param.get("消息模版描述"), config_model=param.get("配置模式"), result_tag=param.get("结果标签"),
                   tag_config=param.get("模版配置"), input_template=param.get("模版输入"))

    elif func == "UpdateMsgTemplate":
        action = MsgTemplate()
        update_map = param.get("修改内容")
        action.update(obj=param.get("消息模版名称"), msg_temp_name=update_map.get("消息模版名称"),
                      title=update_map.get("模版标题"), remark=update_map.get("消息模版描述"),
                      config_model=update_map.get("配置模式"), result_tag=update_map.get("结果标签"),
                      tag_config=update_map.get("模版配置"), input_template=update_map.get("模版输入"))

    elif func == "UpdateMsgTemplateStatus":
        action = MsgTemplate()
        action.update_status(msg_temp_name=param.get("消息模版名称"), set_status=param.get("状态"))

    elif func == "SetDefaultMsgTemplate":
        action = MsgTemplate()
        action.set_default_template(msg_temp_name=param.get("消息模版名称"), set_default=param.get("默认模版"))

    elif func == "DeleteMsgTemplate":
        action = MsgTemplate()
        action.delete(msg_temp_name=param.get("消息模版名称"))

    elif func == "MsgTemplateDataClear":
        action = MsgTemplate()
        action.data_clear(msg_temp_name=param.get("消息模版名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "BatchEnableMsgTemplate":
        action = MsgTemplate()
        action.batch_enable(query=param.get("查询条件"))

    elif func == "BatchDisableMsgTemplate":
        action = MsgTemplate()
        action.batch_disable(query=param.get("查询条件"))

    # 推送计划
    elif func == "AddSendPlan":
        action = SendPlan()
        action.add(plan_name=param.get("推送计划名称"), send_type=param.get("推送类型"), msg_template=param.get("消息模版"),
                   receiver=param.get("接收对象"), send_date=param.get("推送日期"), effect_start_date=param.get("有效开始日期"),
                   effect_end_date=param.get("有效结束日期"), send_start_time=param.get("有效开始时段"),
                   send_end_time=param.get("有效结束时段"), remark=param.get("备注"))

    elif func == "UpdateSendPlan":
        action = SendPlan()
        update_map = param.get("修改内容")
        action.update(obj=param.get("推送计划名称"), plan_name=update_map.get("推送计划名称"), send_type=update_map.get("推送类型"),
                      msg_template=update_map.get("消息模版"), receiver=update_map.get("接收对象"),
                      send_date=update_map.get("推送日期"), effect_start_date=update_map.get("有效开始日期"),
                      effect_end_date=update_map.get("有效结束日期"), send_start_time=update_map.get("有效开始时段"),
                      send_end_time=update_map.get("有效结束时段"), remark=update_map.get("备注"))

    elif func == "DeleteSendPlan":
        action = SendPlan()
        action.delete(plan_name=param.get("推送计划名称"))

    elif func == "UpdateSendPlanStatus":
        action = SendPlan()
        action.update_status(plan_name=param.get("推送计划名称"), set_status=param.get("状态"))

    elif func == "SendPlanDataClear":
        action = SendPlan()
        action.data_clear(plan_name=param.get("推送计划名称"), fuzzy_match=param.get("模糊匹配"))

    return run_flag


""" 
    {  
        "操作": "AddSendPlan",
        "参数": {
            "推送计划名称": "auto_推送计划",
            "推送类型": ["微信", "短信", "邮件"],
            "消息模版": "auto_消息模版_网元其它资料表",
            "接收对象": {
                "接收类型": "用户",
                "接收人": ["彭为", "厂家运维"]
            },
            "推送日期": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
            "有效开始日期": "2020-01-01",
            "有效结束日期": "2099-12-31",
            "有效开始时段": "08:00:00",
            "有效结束时段": "17:59:59",
            "备注": "auto_推送计划_备注"
        }   
    }

    
    {  
        "操作": "UpdateSendPlan",
        "参数": {
            "推送计划名称": "auto_推送计划",
            "修改内容": {
                "推送计划名称": "auto_推送计划",
                "推送类型": ["邮件"],
                "消息模版": "auto_消息模版_流程运行结果",
                "接收对象": {
                    "接收类型": "组织",
                    "接收人": ["auto"]
                },
                "推送日期": "",
                "有效开始日期": "",
                "有效结束日期": "",
                "有效开始时段": "",
                "有效结束时段": "",
                "备注": ""
            }
        }   
    }
    
    {  
        "操作": "UpdateSendPlanStatus",
        "参数": {
            "推送计划名称": "auto_字典_表字典",
            "状态": "启用"
        }   
    }
    
    {  
        "操作": "DeleteSendPlan",
        "参数": {
            "推送计划名称": "auto_字典_表字典"
        }   
    }
    
    {  
        "操作": "SendPlanDataClear",
        "参数": {
            "推送计划名称": "auto_字典_表字典",
            "模糊匹配": "是"
        }   
    }
"""