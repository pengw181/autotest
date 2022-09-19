# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/12/24 下午3:13

from common.wrapper.autoLogin import auto_enter_vm, enter_platform
from app.AlarmPlatform.connection.databaseConfig import DatabaseConfig
from app.AlarmPlatform.connection.tableBelong import TableBelong
from app.AlarmPlatform.connection.ftp import FTP
from app.AlarmPlatform.config.metadata import MetaData
from app.AlarmPlatform.config.alarmPlan import AlarmPlan
from app.AlarmPlatform.config.alarmRule import AlarmRule
from app.AlarmPlatform.config.msgTemplate import MsgTemplate


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
    if func == "AddTableBelong":
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
        action.delete(obj=param.get("表中文名称"))

    elif func == "TableBelongDataClear":
        action = TableBelong()
        action.data_clear(obj=param.get("表中文名称"), fuzzy_match=param.get("模糊匹配"))

    # FTP配置
    if func == "AddFTP":
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
        action.delete(obj=param.get("FTP名称"))

    elif func == "FTPDataClear":
        action = FTP()
        action.data_clear(obj=param.get("FTP名称"), fuzzy_match=param.get("模糊匹配"))

    # 告警元数据配置
    if func == "AddMetaData":
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
        action.delete(obj=param.get("元数据名称"))

    elif func == "MetaDataDataClear":
        action = MetaData()
        action.data_clear(obj=param.get("元数据名称"), fuzzy_match=param.get("模糊匹配"))

    # 告警计划
    if func == "AddAlarmPlan":
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
        action.update_status(obj=param.get("告警计划名称"), set_status=param.get("状态"))

    elif func == "RedoAlarmPlan":
        action = AlarmPlan()
        action.redo(obj=param.get("告警计划名称"), start_time=param.get("开始时间"), end_time=param.get("结束时间"))

    elif func == "DeleteAlarmPlan":
        action = AlarmPlan()
        action.delete(obj=param.get("告警计划名称"))

    elif func == "RedoAlarmPlan":
        action = AlarmPlan()
        action.redo(obj=param.get("告警计划名称"))

    elif func == "AlarmPlanDataClear":
        action = AlarmPlan()
        action.data_clear(obj=param.get("告警计划名称"), fuzzy_match=param.get("模糊匹配"))

    # 告警规则
    if func == "AddAlarmRule":
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
        action.update_status(obj=param.get("规则名称"), set_status=param.get("状态"))

    elif func == "DeleteAlarmRule":
        action = AlarmRule()
        action.delete(obj=param.get("规则名称"))

    elif func == "RedoAlarmRule":
        action = AlarmRule()
        action.redo(obj=param.get("规则名称"), start_time=param.get("开始时间"), end_time=param.get("结束时间"))

    elif func == "AlarmRuleDataClear":
        action = AlarmRule()
        action.data_clear(obj=param.get("规则名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "BatchEnableRule":
        action = AlarmRule()
        action.batch_enable(query=param.get("查询条件"))

    elif func == "BatchDisableRule":
        action = AlarmRule()
        action.batch_disable(query=param.get("查询条件"))

    # 消息模版
    if func == "AddMsgTemplate":
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
        action.update_status(obj=param.get("消息模版名称"), set_status=param.get("状态"))

    elif func == "SetDefaultMsgTemplate":
        action = MsgTemplate()
        action.set_default_template(obj=param.get("消息模版名称"), set_default=param.get("默认模版"))

    elif func == "DeleteMsgTemplate":
        action = MsgTemplate()
        action.delete(obj=param.get("消息模版名称"))

    elif func == "MsgTemplateDataClear":
        action = MsgTemplate()
        action.data_clear(obj=param.get("消息模版名称"), fuzzy_match=param.get("模糊匹配"))

    elif func == "BatchEnableMsgTemplate":
        action = MsgTemplate()
        action.batch_enable(query=param.get("查询条件"))

    elif func == "BatchDisableMsgTemplate":
        action = MsgTemplate()
        action.batch_disable(query=param.get("查询条件"))

    return run_flag


""" 
    {  
        "操作": "RedoAlarmRule",
        "参数": {
            "规则名称": "pw自动化测试告警规则_mysql同比",
            "开始时间": {
                "间隔": "-1",
                "单位": "天"
            },
            "开始时间": {
                "间隔": "1",
                "结束时间": "天"
            }
        }   
    }
    
    
    
    
    {  
        "操作": "AddMsgTemplate",
        "参数": {
            "告警规则名称": "pw自动化测试_告警规则",
            "消息模版名称": "pw自动化测试消息模版",
            "模版标题": "pw自动化测试消息模版标题",
            "消息模版描述": "pw自动化测试消息模版描述",
            "配置模式": "标签模式",
            "结果标签": [],
            "模版配置": [
                {
                    "标签类型": "公共标签",
                    "标签名称": "自定义文本",
                    "自定义值": "网元名称："
                },
                {
                    "标签类型": "结果标签",
                    "标签名称": "OBJ_INFO"
                },
                {
                    "标签类型": "公共标签",
                    "标签名称": "自定义文本",
                    "自定义值": "指令结果："
                },
                {
                    "标签类型": "结果标签",
                    "标签名称": "OBJ_RESULT"
                },
                {
                    "标签类型": "公共标签",
                    "标签名称": "自定义文本",
                    "自定义值": "网元状态："
                },
                {
                    "标签类型": "结果标签",
                    "标签名称": "OBJ_STATUS"
                },
                {
                    "标签类型": "公共标签",
                    "标签名称": "自定义文本",
                    "自定义值": "说明："
                },
                {
                    "标签类型": "结果标签",
                    "标签名称": "OBJ_DESC"
                },
                {
                    "标签类型": "公共标签",
                    "标签名称": "换行"
                }
            ],
            "模版输入": ""
        }   
    }
    
        elif func == "UpdateAlarmRule":
        action = AlarmRule()
        update_map = param.get("修改内容")
        action.update(obj=param.get("规则名称"), basic_conf=update_map.get("基本信息配置"),
                      dimension_conf=update_map.get("告警维度配置"), filter_conf=update_map.get("过滤条件配置"),
                      result_conf=update_map.get("告警结果配置"), storage_conf=update_map.get("告警存储配置"))
    
    {  
        "操作": "UpdateAlarmRule",
        "参数": {
            "规则名称": "pw自动化测试告警规则_结果存储数据库",
            "修改内容": {
                "过滤条件配置": {
                    "配置预览": "是",
                    "规则测试": "是"
                },
                "告警存储配置": {
                    "数据库存储": {
                        "状态": "关闭"
                    }
                }
            }
        }   
    }
    
    {  
        "操作": "DeleteMsgTemplate",
        "参数": {
            "消息模版名称": "pw自动化测试消息模版"
        }   
    }
    
    {  
        "操作": "UpdateAlarmRuleStatus",
        "参数": {
            "规则名称": "pw自动化测试消息模版",
            "状态": "启用"
        }   
    }
    
    {  
        "操作": "SetDefaultMsgTemplate",
        "参数": {
            "消息模版名称": "pw自动化测试消息模版",
            "默认模版": "是"
        }   
    }
    
    
    
    {  
        "操作": "TestFTP",
        "参数": {
            "FTP名称": "pw自动化测试ftp2"
        }   
    }
    
    
    {  
        "操作": "RedoAlarmPlan",
        "参数": {
            "告警计划名称": "pw自动化测试告警计划1"
        }   
    }
    
    
    
    {  
        "操作": "MsgTemplateDataClear",
        "参数": {
            "消息模版名称": "pw自动化测试消息模版",
            "模糊匹配": "是"
        }   
    }
    
    {  
        "操作": "BatchEnable",
        "参数": {
            "查询条件": {
                "告警规则名称": "pw自动化测试告警规则",
                "状态": "否"
            }
        }   
    }
    
"""