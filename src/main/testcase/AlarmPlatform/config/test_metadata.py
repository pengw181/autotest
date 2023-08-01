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


class MetaDataConfig(unittest.TestCase):

	log.info("装载告警元数据测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警配置/告警元数据.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_MetaDataDataClear(self):
		u"""告警元数据数据清理"""
		action = {
			"操作": "MetaDataDataClear",
			"参数": {
				"元数据名称": "auto_元数据",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 告警元数据数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddMetaData(self):
		u"""添加告警元数据，日表"""
		pres = """
		${Database}.alarm|delete from alarm_metadata_field_info where metadata_id in (select metadata_id from  alarm_metadata_info where metadata_name like 'auto_元数据%' and is_delete_tag=1)
		${Database}.alarm|delete from alarm_metadata_info where metadata_name like 'auto_元数据%' and is_delete_tag=1
		"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_告警日表",
				"数据库": "auto_数据库_postgres",
				"表中文名": "auto_表归属_告警日表",
				"数据时延": "0",
				"备注": "auto_元数据_告警日表",
				"时间字段": "col_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3",
					"col_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_告警日表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_告警日表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_告警日表|time_field|col_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_4|field_english_name|col_4|field_english_nick_name|col_4|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，日表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddMetaData(self):
		u"""添加告警元数据，月表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_告警月表",
				"数据库": "auto_数据库_postgres",
				"表中文名": "auto_表归属_告警月表",
				"数据时延": "0",
				"备注": "auto_元数据_告警月表",
				"时间字段": "col_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3",
					"col_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_告警月表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_告警月表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_告警月表|time_field|col_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_4|field_english_name|col_4|field_english_nick_name|col_4|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，月表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddMetaData(self):
		u"""添加告警元数据，年表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_告警年表",
				"数据库": "auto_数据库_postgres",
				"表中文名": "auto_表归属_告警年表",
				"数据时延": "0",
				"备注": "auto_元数据_告警年表",
				"时间字段": "col_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3",
					"col_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_告警年表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_告警年表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_告警年表|time_field|col_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_4|field_english_name|col_4|field_english_nick_name|col_4|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，年表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddMetaData(self):
		u"""添加告警元数据，在网元其它资料页面已添加，但未手动推送"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_vm告警表",
				"数据库": "${DefaultDBName}",
				"表中文名": "auto_表归属_网元其它资料告警表",
				"数据时延": "0",
				"备注": "auto_元数据_vm告警表",
				"时间字段": "update_date",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_2",
					"col_3",
					"update_date"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_网元其它资料告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_vm告警表|time_field|update_date|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|update_date|field_english_name|update_date|field_english_nick_name|update_date|field_type|${TimeDataType}
		"""
		log.info('>>>>> 添加告警元数据，在网元其它资料页面已添加，但未手动推送 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddMetaData(self):
		u"""添加告警元数据，表名对p_result_obj_info"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_info告警表",
				"数据库": "${DefaultDBName}",
				"表中文名": "auto_表归属_流程运行结果",
				"数据时延": "0",
				"备注": "auto_元数据_info告警表",
				"时间字段": "data_time",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"obj_info",
					"obj_result",
					"obj_status",
					"obj_desc",
					"data_time"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_流程运行结果' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_info告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_info告警表|time_field|data_time|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_info|field_english_name|obj_info|field_english_nick_name|obj_info|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_result|field_english_name|obj_result|field_english_nick_name|obj_result|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_status|field_english_name|obj_status|field_english_nick_name|obj_status|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_desc|field_english_name|obj_desc|field_english_nick_name|obj_desc|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|data_time|field_english_name|data_time|field_english_nick_name|data_time|field_type|${TimeDataType}
		"""
		log.info('>>>>> 添加告警元数据，表名对p_result_obj_info <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddMetaData(self):
		u"""添加告警元数据，选择postgres的自定义告警表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_postgres告警表",
				"数据库": "auto_数据库_postgres",
				"表中文名": "auto_表归属_postgres自定义告警表",
				"数据时延": "0",
				"备注": "auto_元数据_postgres告警表",
				"时间字段": "col_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3",
					"col_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_postgres自定义告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_postgres告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_postgres告警表|time_field|col_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_4|field_english_name|col_4|field_english_nick_name|col_4|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，选择postgres的自定义告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddMetaData(self):
		u"""添加告警元数据，选择oracle的自定义告警表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_oracle告警表",
				"数据库": "auto_数据库_oracle",
				"表中文名": "auto_表归属_oracle自定义告警表",
				"数据时延": "0",
				"备注": "auto_元数据_oracle告警表",
				"时间字段": "COL_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"COL_1",
					"COL_2",
					"COL_3",
					"COL_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_oracle自定义告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_oracle告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_oracle告警表|time_field|COL_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_1|field_english_name|COL_1|field_english_nick_name|COL_1|field_type|VARCHAR2
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_2|field_english_name|COL_2|field_english_nick_name|COL_2|field_type|VARCHAR2
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_3|field_english_name|COL_3|field_english_nick_name|COL_3|field_type|VARCHAR2
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_4|field_english_name|COL_4|field_english_nick_name|COL_4|field_type|DATE
		"""
		log.info('>>>>> 添加告警元数据，选择oracle的自定义告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddMetaData(self):
		u"""添加告警元数据，选择mysql的自定义告警表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_mysql告警表",
				"数据库": "auto_数据库_mysql",
				"表中文名": "auto_表归属_mysql自定义告警表",
				"数据时延": "0",
				"备注": "auto_元数据_mysql告警表",
				"时间字段": "col_4",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3",
					"col_4"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_mysql自定义告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_mysql告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_mysql告警表|time_field|col_4|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_4|field_english_name|col_4|field_english_nick_name|col_4|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，选择mysql的自定义告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateMetaData(self):
		u"""修改告警元数据，修改字段显示名称和别名"""
		action = {
			"操作": "UpdateMetaData",
			"参数": {
				"元数据名称": "auto_元数据_vm告警表",
				"修改内容": {
					"元数据名称": "auto_元数据_vm告警表_设置别名",
					"数据时延": "5",
					"备注": "auto_元数据_vm告警表_设置别名",
					"待选字段": [
						"col_2",
						"col_3",
						"domain_id",
						"belong_id",
						"update_date"
					],
					"已选字段": {
						"domain_id": {
							"字段别名": "domain",
							"显示名称": "domain_d"
						},
						"belong_id": {
							"字段别名": "belong",
							"显示名称": "belong_d"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_网元其它资料告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表_设置别名|table_belong_id|${TableBelongID}|data_delay|5|remark|auto_元数据_vm告警表_设置别名|time_field|update_date|time_field_type|1|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|domain_d|field_english_name|domain_id|field_english_nick_name|domain|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|belong_d|field_english_name|belong_id|field_english_nick_name|belong|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|update_date|field_english_name|update_date|field_english_nick_name|update_date|field_type|${TimeDataType}
		"""
		log.info('>>>>> 修改告警元数据，修改字段显示名称和别名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteMetaData(self):
		u"""删除告警元数据"""
		action = {
			"操作": "DeleteMetaData",
			"参数": {
				"元数据名称": "auto_元数据_vm告警表_设置别名"
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_网元其它资料告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表_设置别名|table_belong_id|${TableBelongID}|data_delay|5|remark|auto_元数据_vm告警表_设置别名|time_field_type|1|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull|is_delete_tag|1|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|5|metadata_id|${MetadataID}
		"""
		log.info('>>>>> 删除告警元数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddMetaData(self):
		u"""删除告警元数据后，使用原名称重新添加"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_vm告警表_设置别名",
				"数据库": "${DefaultDBName}",
				"表中文名": "auto_表归属_网元其它资料告警表",
				"数据时延": "0",
				"备注": "auto_元数据_vm告警表_设置别名",
				"时间字段": "update_date",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_2",
					"col_3",
					"domain_id",
					"belong_id",
					"update_date"
				],
				"已选字段": {
					"domain_id": {
						"字段别名": "domain",
						"显示名称": "domain_d"
					},
					"belong_id": {
						"字段别名": "belong",
						"显示名称": "belong_d"
					}
				}
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_网元其它资料告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表_设置别名|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_vm告警表_设置别名|time_field|update_date|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|domain_d|field_english_name|domain_id|field_english_nick_name|domain|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|belong_d|field_english_name|belong_id|field_english_nick_name|belong|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|update_date|field_english_name|update_date|field_english_nick_name|update_date|field_type|${TimeDataType}
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表_设置别名|table_belong_id|${TableBelongID}|data_delay|5|remark|auto_元数据_vm告警表_设置别名|time_field|update_date|time_field_type|1|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull|is_delete_tag|1
		"""
		log.info('>>>>> 删除告警元数据后，使用原名称重新添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddMetaData(self):
		u"""添加告警元数据，在网元其它资料页面添加的表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_vm告警表",
				"数据库": "${DefaultDBName}",
				"表中文名": "auto_表归属_网元其它资料告警表",
				"数据时延": "0",
				"备注": "auto_元数据_vm告警表",
				"时间字段": "update_date",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_2",
					"col_3",
					"update_date"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_网元其它资料告警表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_vm告警表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_vm告警表|time_field|update_date|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|${StrDataType}
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|update_date|field_english_name|update_date|field_english_nick_name|update_date|field_type|${TimeDataType}
		"""
		log.info('>>>>> 添加告警元数据，在网元其它资料页面添加的表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddMetaData(self):
		u"""添加告警元数据，postgres多字段类型表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_postgres多字段类型表",
				"数据库": "auto_数据库_postgres",
				"表中文名": "auto_表归属_postgres多字段类型表",
				"数据时延": "0",
				"备注": "auto_元数据_postgres多字段类型表",
				"时间字段": "col_3",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_postgres多字段类型表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_postgres多字段类型表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_postgres多字段类型表|time_field|col_3|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|NUMERIC
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|TIMESTAMP
		"""
		log.info('>>>>> 添加告警元数据，postgres多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddMetaData(self):
		u"""添加告警元数据，oracle多字段类型表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_oracle多字段类型表",
				"数据库": "auto_数据库_oracle",
				"表中文名": "auto_表归属_oracle多字段类型表",
				"数据时延": "0",
				"备注": "auto_元数据_oracle多字段类型表",
				"时间字段": "COL_3",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"COL_1",
					"COL_2",
					"COL_3"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_oracle多字段类型表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_oracle多字段类型表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_oracle多字段类型表|time_field|COL_3|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_1|field_english_name|COL_1|field_english_nick_name|COL_1|field_type|VARCHAR2
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_2|field_english_name|COL_2|field_english_nick_name|COL_2|field_type|NUMBER
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|COL_3|field_english_name|COL_3|field_english_nick_name|COL_3|field_type|DATE
		"""
		log.info('>>>>> 添加告警元数据，oracle多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddMetaData(self):
		u"""添加告警元数据，mysql多字段类型表"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_mysql多字段类型表",
				"数据库": "auto_数据库_mysql",
				"表中文名": "auto_表归属_mysql多字段类型表",
				"数据时延": "0",
				"备注": "auto_元数据_mysql多字段类型表",
				"时间字段": "col_3",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"col_1",
					"col_2",
					"col_3"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_mysql多字段类型表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_mysql多字段类型表|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_mysql多字段类型表|time_field|col_3|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_1|field_english_name|col_1|field_english_nick_name|col_1|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_2|field_english_name|col_2|field_english_nick_name|col_2|field_type|INT
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|col_3|field_english_name|col_3|field_english_nick_name|col_3|field_type|DATETIME
		"""
		log.info('>>>>> 添加告警元数据，mysql多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddMetaData(self):
		u"""添加告警元数据，mysql流程运行结果"""
		action = {
			"操作": "AddMetaData",
			"参数": {
				"元数据名称": "auto_元数据_流程运行结果",
				"数据库": "auto_数据库_mysql_v32",
				"表中文名": "auto_表归属_流程运行结果表",
				"数据时延": "0",
				"备注": "auto_元数据_流程运行结果",
				"时间字段": "data_time",
				"时间格式": "默认(时间类型)",
				"待选字段": [
					"obj_info",
					"obj_result",
					"obj_status",
					"obj_desc",
					"data_time"
				]
			}
		}
		checks = """
		CheckMsg|提交成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_流程运行结果表' and is_delete_tag=0|TableBelongID
		CheckData|${Database}.alarm.alarm_metadata_info|1|metadata_name|auto_元数据_流程运行结果|table_belong_id|${TableBelongID}|data_delay|0|remark|auto_元数据_流程运行结果|time_field|data_time|time_field_type|1|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now|is_delete_tag|0|FetchID|metadata_id
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_info|field_english_name|obj_info|field_english_nick_name|obj_info|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_result|field_english_name|obj_result|field_english_nick_name|obj_result|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_status|field_english_name|obj_status|field_english_nick_name|obj_status|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|obj_desc|field_english_name|obj_desc|field_english_nick_name|obj_desc|field_type|VARCHAR
		CheckData|${Database}.alarm.alarm_metadata_field_info|1|metadata_id|${MetadataID}|field_chinese_name|data_time|field_english_name|data_time|field_english_nick_name|data_time|field_type|DATETIME
		"""
		log.info('>>>>> 添加告警元数据，mysql流程运行结果 <<<<<')
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
