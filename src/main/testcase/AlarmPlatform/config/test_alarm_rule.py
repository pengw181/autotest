# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/07/31 PM06:41

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.case import CaseEngine
from src.main.python.lib.screenShot import saveScreenShot


class AlarmRuleConfig(unittest.TestCase):

	log.info("装载告警规则测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警配置/告警规则.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AlarmRuleDataClear(self):
		u"""告警规则配置数据清理"""
		action = {
			"操作": "AlarmRuleDataClear",
			"参数": {
				"告警规则名称": "auto_告警规则",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 告警规则配置数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	@unittest.skip
	def test_2_AddAlarmRule(self):
		u"""UNTEST,添加告警规则，配置正确"""
		pres = """
		${Database}.alarm|delete from alarm_storage_field_rel where storage_relation_id in (select storage_relation_id from alarm_storage_relation where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%'))
		${Database}.alarm|delete from alarm_storage_relation where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%')
		${Database}.alarm|delete from alarm_storage_file_info where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%')
		${Database}.alarm|delete from alarm_rule_info where alarm_rule_name  like 'auto_告警规则%' and is_delete_tag=1
		${DatabaseM}.main|update p_result_obj_info set DATA_TIME = now()-1/24 where OBJ_INFO like '%_alarm'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_流程运行结果_v32",
				"基本信息配置": {
					"规则名称": "auto_告警规则",
					"规则描述": "auto_告警规则描述",
					"告警等级": "低级",
					"有效开始时间": "2022-02-01 00:00:00",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"告警维度配置": {
					"领域": [
						"核心网",
						"系统管理"
					]
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "OBJ_RESULT",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "异常"
							}
						}
					],
					"告警区域配置": {
						"OBJ_INFO": {},
						"OBJ_RESULT": {},
						"OBJ_DESC": {},
						"OBJ_STATUS": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"OBJ_INFO",
						"OBJ_RESULT",
						"OBJ_DESC",
						"OBJ_STATUS"
					]
				},
				"告警存储配置": {
					"FTP存储": {
						"状态": "打开",
						"FTP名称": "auto_ftp",
						"存储目录": "pw/alarm",
						"文件名称": "alarm1",
						"文件类型": "txt",
						"时间单位": "小时",
						"保存间隔": "1",
						"保存方式": "追加写入"
					},
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表_postgres自定义输出表",
						"字段映射": [
							[
								"OBJ_INFO",
								"col_1"
							],
							[
								"OBJ_RESULT",
								"col_2"
							],
							[
								"OBJ_DESC",
								"col_3"
							],
							[
								"OBJ_STATUS",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select alarm_plan_id from alarm_plan_info where alarm_plan_name='auto_告警计划_流程运行结果_v32' and is_delete_tag=0|AlarmPlanID
		CheckData|${Database}.alarm.alarm_rule_info|1|alarm_rule_name|auto_告警规则|alarm_plan_id|${AlarmPlanID}|alarm_rule_desc|auto_告警规则描述|alarm_level_id|3|alarm_start_time|2022-02-01 00:00:00|alarm_finish_time|2023-12-31 00:00:00|alarm_trigger_times|now|ym_o_ym|null|is_series|1|alarm_detect_rate|10|alarm_detect_rate_unit|1|dimension_id|notnull|trigger_condition_cntent|notnull|select_sql|notnull|lable_content_json|notnull|result_field_json|notnull|column_field_json|notnull|storage_object_type|4|rule_conf_status|1|is_delete_tag|0|creator|${LoginUser}|create_date|now|updater|${LoginUser}|modif_date|now|FetchID|alarm_rule_id
		GetData|${Database}.alarm|select ftp_config_id from alarm_ftp_config where ftp_name='auto_ftp'|FtpConfigID
		CheckData|${Database}.alarm.alarm_storage_file_info|1|alarm_rule_id|${AlarmRuleID}|storage_file_name|alarm1|storage_file_type|txt|path_url|pw/alarm|storage_period|1|storage_period_unit|2|operate_type|1|ftp_config_id|${FtpConfigID}
		GetData|${Database}.alarm|select storage_relation_id from alarm_storage_relation where alarm_rule_id='${AlarmRuleID}'|StorageRelationID
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_INFO|storage_field_name_en|col_1|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_RESULT|storage_field_name_en|col_2|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_DESC|storage_field_name_en|col_3|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_STATUS|storage_field_name_en|col_4|storage_field_type|TIMESTAMP
		"""
		log.info('>>>>> UNTEST,添加告警规则，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddAlarmRule(self):
		u"""添加告警规则，配置正确"""
		pres = """
		${Database}.alarm|delete from alarm_storage_field_rel where storage_relation_id in (select storage_relation_id from alarm_storage_relation where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%'))
		${Database}.alarm|delete from alarm_storage_relation where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%')
		${Database}.alarm|delete from alarm_storage_file_info where alarm_rule_id in (select alarm_rule_id from alarm_rule_info where alarm_rule_name like 'auto_告警规则%')
		${Database}.alarm|delete from alarm_rule_info where alarm_rule_name  like 'auto_告警规则%' and is_delete_tag=1
		${DatabaseM}.main|update p_result_obj_info set DATA_TIME = now()-1/24 where OBJ_INFO like '%_alarm'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_流程运行结果",
				"基本信息配置": {
					"规则名称": "auto_告警规则",
					"规则描述": "auto_告警规则描述",
					"告警等级": "低级",
					"有效开始时间": "2022-02-01 00:00:00",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "OBJ_RESULT",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "异常"
							}
						}
					],
					"告警区域配置": {
						"OBJ_INFO": {},
						"OBJ_RESULT": {},
						"OBJ_DESC": {},
						"OBJ_STATUS": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"OBJ_INFO",
						"OBJ_RESULT",
						"OBJ_DESC",
						"OBJ_STATUS"
					]
				},
				"告警存储配置": {
					"FTP存储": {
						"状态": "打开",
						"FTP名称": "auto_ftp",
						"存储目录": "pw/alarm",
						"文件名称": "alarm1",
						"文件类型": "txt",
						"时间单位": "小时",
						"保存间隔": "1",
						"保存方式": "追加写入"
					},
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"OBJ_INFO",
								"col_1"
							],
							[
								"OBJ_RESULT",
								"col_2"
							],
							[
								"OBJ_DESC",
								"col_3"
							],
							[
								"OBJ_STATUS",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select alarm_plan_id from alarm_plan_info where alarm_plan_name='auto_告警计划_流程运行结果' and is_delete_tag=0|AlarmPlanID
		CheckData|${Database}.alarm.alarm_rule_info|1|alarm_rule_name|auto_告警规则|alarm_plan_id|${AlarmPlanID}|alarm_rule_desc|auto_告警规则描述|alarm_level_id|3|alarm_start_time|2022-02-01 00:00:00|alarm_finish_time|2023-12-31 00:00:00|alarm_trigger_times|now|ym_o_ym|null|is_series|1|alarm_detect_rate|10|alarm_detect_rate_unit|1|dimension_id|notnull|trigger_condition_cntent|notnull|select_sql|notnull|lable_content_json|notnull|result_field_json|notnull|column_field_json|notnull|storage_object_type|4|rule_conf_status|1|is_delete_tag|0|creator|${LoginUser}|create_date|now|updater|${LoginUser}|modif_date|now|FetchID|alarm_rule_id
		GetData|${Database}.alarm|select ftp_config_id from alarm_ftp_config where ftp_name='auto_ftp'|FtpConfigID
		CheckData|${Database}.alarm.alarm_storage_file_info|1|alarm_rule_id|${AlarmRuleID}|storage_file_name|alarm1|storage_file_type|txt|path_url|pw/alarm|storage_period|1|storage_period_unit|2|operate_type|1|ftp_config_id|${FtpConfigID}
		GetData|${Database}.alarm|select storage_relation_id from alarm_storage_relation where alarm_rule_id='${AlarmRuleID}'|StorageRelationID
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_INFO|storage_field_name_en|col_1|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_RESULT|storage_field_name_en|col_2|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_DESC|storage_field_name_en|col_3|storage_field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_storage_field_rel|1|storage_relation_id|${StorageRelationID}|result_field_name_en|OBJ_STATUS|storage_field_name_en|col_4|storage_field_type|VARCHAR
		"""
		log.info('>>>>> 添加告警规则，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddAlarmRule(self):
		u"""添加告警规则，流程运行结果表"""
		pres = """
		${Database}.main|delete from p_result_obj_info where obj_info like '%_alarm'
		${Database}.main|insert into p_result_obj_info (inst_id, parent_inst_id, obj_info, obj_result, obj_status, obj_desc, extra_info, data_time, belong_id, domain_id, process_id, parent_process_id) VALUES (uuid(), '-1', 'PW_MME_001_alarm', '正常', '带业务', '指标正常', null, now(), '440100', 'AiSeeCore', 1901, -1)
		${Database}.main|insert into p_result_obj_info (inst_id, parent_inst_id, obj_info, obj_result, obj_status, obj_desc, extra_info, data_time, belong_id, domain_id, process_id, parent_process_id) VALUES (uuid(), '-1', 'PW_MME_002_alarm', '异常', '带业务', '指标异常', null, now(), '440100', 'AiSeeCore', 1901, -1)
		${Database}.main|insert into p_result_obj_info (inst_id, parent_inst_id, obj_info, obj_result, obj_status, obj_desc, extra_info, data_time, belong_id, domain_id, process_id, parent_process_id) VALUES (uuid(), '-1', 'PW_MME_003_alarm', '异常', '带业务', '指标异常', null, now(), '440100', 'AiSeeCore', 1901, -1)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_流程运行结果",
				"基本信息配置": {
					"规则名称": "auto_告警规则_流程运行结果",
					"规则描述": "auto_告警规则_流程运行结果描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "obj_result",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "异常"
							}
						}
					],
					"告警区域配置": {
						"obj_info": {},
						"obj_result": {},
						"obj_status": {},
						"data_time": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"obj_info",
						"obj_result",
						"obj_status",
						"data_time"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"obj_info",
								"col_1"
							],
							[
								"obj_result",
								"col_2"
							],
							[
								"obj_status",
								"col_3"
							],
							[
								"data_time",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，流程运行结果表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddAlarmRule(self):
		u"""添加告警规则，自定义日表"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table1_${YMD}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|create table pw_output_table1_${YMD}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|delete from pw_alarm_table1_${YMD} where 1=1
		${DatabaseP}.sso|insert into pw_output_table1_${YMD}(col_1, col_2, col_3, col_4) values ('db', 'version1', '20', now())
		${DatabaseP}.sso|insert into pw_alarm_table1_${YMD}(col_1, col_2, col_3, col_4) values ('db', 'version2', '30', now())
		${DatabaseP}.sso|insert into pw_alarm_table1_${YMD}(col_1, col_2, col_3, col_4) values ('db', 'version3', '50', now())
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_告警日表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_日表",
					"规则描述": "auto_告警规则_日表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {},
						"col_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3",
						"col_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_3"
							],
							[
								"col_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，自定义日表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddAlarmRule(self):
		u"""添加告警规则，自定义月表"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table2_${YM}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|create table pw_output_table2_${YM}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|delete from pw_alarm_table2_${YM} where 1=1
		${DatabaseP}.sso|insert into pw_alarm_table2_${YM}(col_1, col_2, col_3, col_4) values ('db', 'version1', '20', now())
		${DatabaseP}.sso|insert into pw_alarm_table2_${YM}(col_1, col_2, col_3, col_4) values ('db', 'version2', '30', now())
		${DatabaseP}.sso|insert into pw_alarm_table2_${YM}(col_1, col_2, col_3, col_4) values ('db', 'version3', '50', now())
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_告警月表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_月表",
					"规则描述": "auto_告警规则_月表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {},
						"col_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3",
						"col_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_3"
							],
							[
								"col_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，自定义月表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddAlarmRule(self):
		u"""添加告警规则，自定义年表"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table3_${Y}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|create table pw_output_table3_${Y}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		${DatabaseP}.sso|delete from pw_alarm_table3_${Y} where 1=1
		${DatabaseP}.sso|insert into pw_alarm_table3_${Y}(col_1, col_2, col_3, col_4) values ('db', 'version1', '20', now())
		${DatabaseP}.sso|insert into pw_alarm_table3_${Y}(col_1, col_2, col_3, col_4) values ('db', 'version2', '30', now())
		${DatabaseP}.sso|insert into pw_alarm_table3_${Y}(col_1, col_2, col_3, col_4) values ('db', 'version3', '50', now())
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_告警年表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_年表",
					"规则描述": "auto_告警规则_年表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {},
						"col_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3",
						"col_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_3"
							],
							[
								"col_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，自定义年表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddAlarmRule(self):
		u"""添加告警规则，网元其它资料告警表"""
		pres = """
		${Database}.main|delete from ${AlarmTableName} where 1=1
		${Database}.main|insert into ${AlarmTableName} (pk, aisee_batch_tag, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3) VALUES (uuid(), '0', 'pw', '0', now(), '440100', 'AiSeeCore', 'alarm1', '20')
		${Database}.main|insert into ${AlarmTableName} (pk, aisee_batch_tag, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3) VALUES (uuid(), '0', 'pw', '0', now(), '440100', 'AiSeeCore', 'alarm2', '50')
		${Database}.main|insert into ${AlarmTableName} (pk, aisee_batch_tag, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3) VALUES (uuid(), '0', 'pw', '0', now(), '440100', 'AiSeeCore', 'alarm3', '0')
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_网元其它资料告警表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_网元其它资料表",
					"规则描述": "auto_告警规则_网元其它资料表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_2": {},
						"col_3": {},
						"update_date": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_2",
						"col_3",
						"update_date"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_2",
								"col_1"
							],
							[
								"col_3",
								"col_2"
							],
							[
								"update_date",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，网元其它资料告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddAlarmRule(self):
		u"""添加告警规则，postgres自定义表"""
		pres = """
		${DatabaseP}.sso|delete from pw_alarm_table where col_1='postgres'
		${DatabaseP}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('postgres', 'version1', '10', now())
		${DatabaseP}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('postgres', 'version2', '20', now())
		${DatabaseP}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('postgres', 'version3', '0', now())
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres告警表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_postgres告警表",
					"规则描述": "auto_告警规则_postgres告警表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {},
						"col_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3",
						"col_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_3"
							],
							[
								"col_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，postgres自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddAlarmRule(self):
		u"""添加告警规则，oracle自定义表"""
		pres = """
		${DatabaseO}.sso|delete from pw_alarm_table where col_1='oracle'
		${DatabaseO}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('oracle', 'version1', '10', sysdate)
		${DatabaseO}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('oracle', 'version2', '20', sysdate)
		${DatabaseO}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('oracle', 'version3', '0', sysdate)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_oracle告警表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_oracle告警表",
					"规则描述": "auto_告警规则_oracle告警表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "COL_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"COL_1": {},
						"COL_2": {},
						"COL_3": {},
						"COL_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"COL_1",
						"COL_2",
						"COL_3",
						"COL_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"COL_1",
								"col_1"
							],
							[
								"COL_2",
								"col_2"
							],
							[
								"COL_3",
								"col_3"
							],
							[
								"COL_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，oracle自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddAlarmRule(self):
		u"""添加告警规则，mysql自定义表"""
		pres = """
		${DatabaseM}.sso|delete from pw_alarm_table where col_1='mysql'
		${DatabaseM}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('mysql', 'version1', '10', now())
		${DatabaseM}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('mysql', 'version2', '20', now())
		${DatabaseM}.sso|insert into pw_alarm_table(col_1, col_2, col_3, col_4) values ('mysql', 'version3', '0', now())
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_mysql告警表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_mysql告警表",
					"规则描述": "auto_告警规则_mysql告警表描述",
					"告警等级": "低级",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_3",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "字符",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {},
						"col_4": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3",
						"col_4"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_3"
							],
							[
								"col_4",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，mysql自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddAlarmRule(self):
		u"""添加告警规则，postgress数据表，同比（查前一周期的数据）"""
		pres = """
		${DatabaseP}.sso|delete from pw_agg_table where 1=1
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', statement_timestamp() - (interval '1 day'))
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', statement_timestamp() - (interval '1 day'))
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_postgres同比",
					"规则描述": "auto_告警规则_postgres同比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "同比",
					"同/环比字段": "col_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "0"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，postgress数据表，同比（查前一周期的数据） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddAlarmRule(self):
		u"""添加告警规则，oracle数据表，同比"""
		pres = """
		${DatabaseO}.sso|delete from pw_agg_table where 1=1
		${DatabaseO}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', sysdate-1)
		${DatabaseO}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', sysdate-1)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_oracle多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_oracle同比",
					"规则描述": "auto_告警规则_oracle同比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "同比",
					"同/环比字段": "COL_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "COL_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"COL_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "20"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，oracle数据表，同比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddAlarmRule(self):
		u"""添加告警规则，mysql数据表，同比"""
		pres = """
		${DatabaseM}.sso|delete from pw_agg_table where 1=1
		${DatabaseM}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', now() - interval 1 day)
		${DatabaseM}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', now() - interval 1 day)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_mysql多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_mysql同比",
					"规则描述": "auto_告警规则_mysql同比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "同比",
					"同/环比字段": "col_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "10"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，mysql数据表，同比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddAlarmRule(self):
		u"""添加告警规则，postgress数据表，环比"""
		pres = """
		${DatabaseP}.sso|delete from pw_agg_table where 1=1
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', statement_timestamp() - (interval '1 day'))
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', statement_timestamp() - (interval '1 day'))
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_postgres环比",
					"规则描述": "auto_告警规则_postgres环比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "环比",
					"同/环比字段": "col_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "0"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，postgress数据表，环比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddAlarmRule(self):
		u"""添加告警规则，oracle数据表，环比"""
		pres = """
		${DatabaseO}.sso|delete from pw_agg_table where 1=1
		${DatabaseO}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', sysdate-1)
		${DatabaseO}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', sysdate-1)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_oracle多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_oracle环比",
					"规则描述": "auto_告警规则_oracle环比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "环比",
					"同/环比字段": "COL_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "COL_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"COL_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "20"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，oracle数据表，环比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddAlarmRule(self):
		u"""添加告警规则，mysql数据表，环比"""
		pres = """
		${DatabaseM}.sso|delete from pw_agg_table where 1=1
		${DatabaseM}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', now())
		${DatabaseM}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', now() - interval 1 day)
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_mysql多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_mysql环比",
					"规则描述": "auto_告警规则_mysql环比描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"同比/环比": "环比",
					"同/环比字段": "col_2",
					"字段基值": "10",
					"周期单位": "日"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "10"
						}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，mysql数据表，环比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddAlarmRule(self):
		u"""添加告警规则，不配置维度"""
		pres = """
		${DatabaseM}.main|update p_result_obj_info set DATA_TIME = now()-1/24 where OBJ_INFO like '%_alarm'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_流程运行结果",
				"基本信息配置": {
					"规则名称": "auto_告警规则_不配置维度",
					"规则描述": "auto_告警规则_不配置维度描述",
					"告警等级": "低级",
					"有效开始时间": "2022-02-01 00:00:00",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "OBJ_RESULT",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "异常"
							}
						}
					],
					"告警区域配置": {
						"OBJ_INFO": {},
						"OBJ_RESULT": {},
						"OBJ_DESC": {},
						"OBJ_STATUS": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"OBJ_INFO",
						"OBJ_RESULT",
						"OBJ_DESC",
						"OBJ_STATUS"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，不配置维度 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddAlarmRule(self):
		u"""添加告警规则，设置聚合函数，COUNT"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_3=statement_timestamp() + (interval '8 hour') where 1=1
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_COUNT",
					"规则描述": "auto_告警规则_COUNT描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {
							"聚合函数": "COUNT",
							"结果名称": "次数",
							"阈值条件": "大于",
							"告警阈值": "0"
						},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_3",
						"次数"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置聚合函数，COUNT <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddAlarmRule(self):
		u"""添加告警规则，设置聚合函数，MAX"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_3=statement_timestamp() + (interval '8 hour') where 1=1
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_MAX",
					"规则描述": "auto_告警规则_MAX描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {
							"聚合函数": "MAX",
							"结果名称": "最大值",
							"阈值条件": "大于",
							"告警阈值": "10"
						},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_3",
						"最大值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置聚合函数，MAX <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddAlarmRule(self):
		u"""添加告警规则，设置聚合函数，MIN"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_3=statement_timestamp() + (interval '8 hour') where 1=1
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_MIN",
					"规则描述": "auto_告警规则_MIN描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {
							"聚合函数": "MIN",
							"结果名称": "最小值",
							"阈值条件": "大于",
							"告警阈值": "10"
						},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_3",
						"最小值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置聚合函数，MIN <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddAlarmRule(self):
		u"""添加告警规则，设置聚合函数，SUM"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_3=statement_timestamp() + (interval '8 hour') where 1=1
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_SUM",
					"规则描述": "auto_告警规则_SUM描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {
							"聚合函数": "SUM",
							"结果名称": "求和",
							"阈值条件": "大于",
							"告警阈值": "10"
						},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_3",
						"求和"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置聚合函数，SUM <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddAlarmRule(self):
		u"""添加告警规则，设置聚合函数，AVG"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_3=statement_timestamp() + (interval '8 hour') where 1=1
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_AVG",
					"规则描述": "auto_告警规则_AVG描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "0"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {
							"聚合函数": "AVG",
							"结果名称": "平均值",
							"阈值条件": "大于",
							"告警阈值": "10"
						},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_3",
						"平均值"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置聚合函数，AVG <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：大于"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='50', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件大于",
					"规则描述": "auto_告警规则_过滤条件大于描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "50"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：大于 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：大于等于"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='50', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件大于等于",
					"规则描述": "auto_告警规则_过滤条件大于等于描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于等于",
								"字段类型": "数值",
								"字段值": "50"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：大于等于 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：小于"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='50', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件小于",
					"规则描述": "auto_告警规则_过滤条件小于描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "小于",
								"字段类型": "数值",
								"字段值": "100"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：小于 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：小于等于"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='100', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件小于等于",
					"规则描述": "auto_告警规则_过滤条件小于等于描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "小于等于",
								"字段类型": "数值",
								"字段值": "100"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：小于等于 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：不等于"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='100', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件不等于",
					"规则描述": "auto_告警规则_过滤条件不等于描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "不等于",
								"字段类型": "数值",
								"字段值": "100"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：不等于 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：为空"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2=null, col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件为空",
					"规则描述": "auto_告警规则_过滤条件为空描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "为空"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：非空"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2=null, col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件非空",
					"规则描述": "auto_告警规则_过滤条件非空描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "非空"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：非空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：包含"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='100', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件包含",
					"规则描述": "auto_告警规则_过滤条件包含描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_1",
							"标签属性": {
								"逻辑条件": "包含",
								"字段类型": "字符",
								"字段值": "db1"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：包含 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddAlarmRule(self):
		u"""添加告警规则，设置过滤条件：在列表"""
		pres = """
		${DatabaseP}.sso|update pw_agg_table set col_2='100', col_3=statement_timestamp() + (interval '8 hour') where col_1='db1'
		${DatabaseP}.sso|update pw_agg_table set col_2='200', col_3=statement_timestamp() + (interval '8 hour') where col_1='db2'
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_过滤条件在列表",
					"规则描述": "auto_告警规则_过滤条件在列表描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_1",
							"标签属性": {
								"逻辑条件": "在列表",
								"字段类型": "字符",
								"字段值": "db1,db2,db3"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置过滤条件：在列表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_AddAlarmRule(self):
		u"""添加告警规则，设置自定义过滤条件"""
		pres = """
		${DatabaseP}.sso|delete from pw_agg_table where 1=1
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db1', '100', statement_timestamp() + (interval '8 hour'))
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '200', statement_timestamp() + (interval '8 hour'))
		${DatabaseP}.sso|insert into pw_agg_table(col_1, col_2, col_3) values ('db2', '300', statement_timestamp() + (interval '8 hour'))
		"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_自定义过滤条件",
					"规则描述": "auto_告警规则_自定义过滤条件描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "公共标签",
							"标签名": "自定义过滤条件",
							"标签属性": {
								"自定义sql": "col_1='db2' and col_2>200"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置自定义过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddAlarmRule(self):
		u"""添加告警规则，设置多个过滤条件"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_多过滤条件",
					"规则描述": "auto_告警规则_多过滤条件描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_1",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "db2"
							}
						},
						{
							"标签类型": "公共标签",
							"标签名": "AND"
						},
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "200"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，设置多个过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_AddAlarmRule(self):
		u"""添加告警规则，FTP存储"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_结果存储ftp",
					"规则描述": "auto_告警规则_结果存储ftp描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_1",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "db2"
							}
						},
						{
							"标签类型": "公共标签",
							"标签名": "AND"
						},
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "200"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				},
				"告警存储配置": {
					"FTP存储": {
						"状态": "打开",
						"FTP名称": "auto_ftp",
						"存储目录": "pw/alarm",
						"文件名称": "alarmResult",
						"文件类型": "txt",
						"时间单位": "小时",
						"保存间隔": "1",
						"保存方式": "追加写入"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，FTP存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_AddAlarmRule(self):
		u"""添加告警规则，数据库存储"""
		action = {
			"操作": "AddAlarmRule",
			"参数": {
				"告警类型": "结构化数据",
				"告警计划": "auto_告警计划_postgres多字段类型表",
				"基本信息配置": {
					"规则名称": "auto_告警规则_结果存储数据库",
					"规则描述": "auto_告警规则_结果存储数据库描述",
					"告警等级": "信息",
					"有效开始时间": "now",
					"有效结束时间": "2023-12-31 00:00:00",
					"开始时间": "now",
					"连续次数": "1",
					"检测频率": "10",
					"检测频率单位": "分钟"
				},
				"过滤条件配置": {
					"过滤条件": [
						{
							"标签类型": "字段标签",
							"标签名": "col_1",
							"标签属性": {
								"逻辑条件": "等于",
								"字段类型": "字符",
								"字段值": "db2"
							}
						},
						{
							"标签类型": "公共标签",
							"标签名": "AND"
						},
						{
							"标签类型": "字段标签",
							"标签名": "col_2",
							"标签属性": {
								"逻辑条件": "大于",
								"字段类型": "数值",
								"字段值": "200"
							}
						}
					],
					"告警区域配置": {
						"col_1": {},
						"col_2": {},
						"col_3": {}
					},
					"配置预览": "是",
					"规则测试": "是"
				},
				"告警结果配置": {
					"告警字段英文名": [
						"col_1",
						"col_2",
						"col_3"
					]
				},
				"告警存储配置": {
					"数据库存储": {
						"状态": "打开",
						"选择数据库": "auto_数据库_postgres",
						"选择表": "auto_表归属_postgres自定义输出表",
						"字段映射": [
							[
								"col_1",
								"col_1"
							],
							[
								"col_2",
								"col_2"
							],
							[
								"col_3",
								"col_4"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加告警规则，数据库存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_UpdateAlarmRule(self):
		u"""修改告警规则，关闭FTP存储"""
		action = {
			"操作": "UpdateAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_结果存储ftp",
				"修改内容": {
					"过滤条件配置": {
						"配置预览": "是",
						"规则测试": "是"
					},
					"告警存储配置": {
						"FTP存储": {
							"状态": "关闭"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改告警规则，关闭FTP存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_UpdateAlarmRule(self):
		u"""修改告警规则，关闭数据库存储"""
		action = {
			"操作": "UpdateAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_结果存储数据库",
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
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改告警规则，关闭数据库存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_UpdateAlarmRule(self):
		u"""修改告警规则，开启FTP存储"""
		action = {
			"操作": "UpdateAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_结果存储ftp",
				"修改内容": {
					"过滤条件配置": {
						"配置预览": "是",
						"规则测试": "是"
					},
					"告警存储配置": {
						"FTP存储": {
							"状态": "打开",
							"FTP名称": "auto_ftp",
							"存储目录": "pw/alarm",
							"文件名称": "alarmResult",
							"文件类型": "txt",
							"时间单位": "小时",
							"保存间隔": "1",
							"保存方式": "追加写入"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改告警规则，开启FTP存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_UpdateAlarmRule(self):
		u"""修改告警规则，开启数据库存储"""
		action = {
			"操作": "UpdateAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_结果存储数据库",
				"修改内容": {
					"过滤条件配置": {
						"配置预览": "是",
						"规则测试": "是"
					},
					"告警存储配置": {
						"数据库存储": {
							"状态": "打开",
							"选择数据库": "auto_数据库_postgres",
							"选择表": "auto_表归属_postgres自定义输出表",
							"字段映射": [
								[
									"col_1",
									"col_1"
								],
								[
									"col_2",
									"col_2"
								],
								[
									"col_3",
									"col_4"
								]
							]
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改告警规则，开启数据库存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_BatchEnableRule(self):
		u"""批量启用告警规则"""
		action = {
			"操作": "BatchEnableRule",
			"参数": {
				"查询条件": {
					"告警规则名称": "auto_告警规则"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量启用告警规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_BatchDisableRule(self):
		u"""批量禁用告警规则"""
		action = {
			"操作": "BatchDisableRule",
			"参数": {
				"查询条件": {
					"告警规则名称": "auto_告警规则"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量禁用告警规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_BatchEnableRule(self):
		u"""批量启用告警规则"""
		action = {
			"操作": "BatchEnableRule",
			"参数": {
				"查询条件": {
					"告警规则名称": "auto_告警规则"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量启用告警规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
