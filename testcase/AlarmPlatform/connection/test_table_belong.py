# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:08

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class TableBelongConfig(unittest.TestCase):

	log.info("装载表归属配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_TableBelongDataClear(self):
		u"""表归属配置，数据清理"""
		action = {
			"操作": "TableBelongDataClear",
			"参数": {
				"表中文名称": "auto_表归属",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 表归属配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddTableBelong(self):
		u"""数据库添加告警表，表来自网元其它资料表（目前根据表英文名查表是否已存在）"""
		pres = """
		${Database}.alarm|delete from alarm_table_belong where table_name_ch like 'auto_表归属%' and is_delete_tag=1
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "${AlarmTableName}",
				"表中文名称": "auto_表归属_网元其它资料告警表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_网元其它资料告警表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='${DefaultDBName}'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|${AlarmTableName}|table_name_ch|auto_表归属_网元其它资料告警表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_网元其它资料告警表
		"""
		log.info('>>>>> 数据库添加告警表，表来自网元其它资料表（目前根据表英文名查表是否已存在） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddTableBelong(self):
		u"""数据库添加告警表，p_result_obj_info"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_流程运行结果",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres_p_result_obj_info"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='${DefaultDBName}'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|p_result_obj_info|table_name_ch|auto_表归属_流程运行结果|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_postgres_p_result_obj_info
		"""
		log.info('>>>>> 数据库添加告警表，p_result_obj_info <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddTableBelong(self):
		u"""数据库添加输出表，表来自网元其它资料表"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "${OutputTableName}",
				"表中文名称": "auto_表归属_网元其它资料输出表",
				"表使用对象": "输出表",
				"表周期": "普通",
				"备注": "auto_表归属_网元其它资料输出表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='${DefaultDBName}'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|${OutputTableName}|table_name_ch|auto_表归属_网元其它资料输出表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_网元其它资料输出表
		"""
		log.info('>>>>> 数据库添加输出表，表来自网元其它资料表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddTableBelong(self):
		u"""postgres数据库添加告警表，表来自自定义表"""
		pres = """
		${DatabaseP}.sso|create table if not exists pw_alarm_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_alarm_table",
				"表中文名称": "auto_表归属_postgres自定义告警表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres自定义告警表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table|table_name_ch|auto_表归属_postgres自定义告警表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_postgres自定义告警表
		"""
		log.info('>>>>> postgres数据库添加告警表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddTableBelong(self):
		u"""postgres数据库添加输出表，表来自自定义表"""
		pres = """
		${DatabaseP}.sso|create table if not exists pw_output_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_output_table",
				"表中文名称": "auto_表归属_postgres自定义输出表",
				"表使用对象": "输出表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres自定义输出表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table|table_name_ch|auto_表归属_postgres自定义输出表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_postgres自定义输出表
		"""
		log.info('>>>>> postgres数据库添加输出表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_7_AddTableBelong(self):
		u"""UNTEST,oracle数据库添加告警表，p_result_obj_info"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "9990",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_oracle_info",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_oracle_p_result_obj_info"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='9990'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|p_result_obj_info|table_name_ch|auto_表归属_oracle_info|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_oracle_p_result_obj_info
		"""
		log.info('>>>>> UNTEST,oracle数据库添加告警表，p_result_obj_info <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddTableBelong(self):
		u"""oracle数据库添加告警表，表来自自定义表"""
		pres = """
		${DatabaseO}.sso|create table pw_alarm_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 date)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_oracle",
				"表英文名称": "pw_alarm_table",
				"表中文名称": "auto_表归属_oracle自定义告警表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_oracle自定义告警表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_oracle'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table|table_name_ch|auto_表归属_oracle自定义告警表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_oracle自定义告警表
		"""
		log.info('>>>>> oracle数据库添加告警表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddTableBelong(self):
		u"""oracle数据库添加输出表，表来自自定义表"""
		pres = """
		${DatabaseO}.sso|create table pw_output_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 date)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_oracle",
				"表英文名称": "pw_output_table",
				"表中文名称": "auto_表归属_oracle自定义输出表",
				"表使用对象": "输出表",
				"表周期": "普通",
				"备注": "auto_表归属_oracle自定义输出表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_oracle'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table|table_name_ch|auto_表归属_oracle自定义输出表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_oracle自定义输出表
		"""
		log.info('>>>>> oracle数据库添加输出表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_10_AddTableBelong(self):
		u"""UNTEST,mysql数据库添加告警表，p_result_obj_info"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "9100",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_mysql_info",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_mysql_p_result_obj_info"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='9100'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|p_result_obj_info|table_name_ch|auto_表归属_oracle_info|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_oracle_p_result_obj_info
		"""
		log.info('>>>>> UNTEST,mysql数据库添加告警表，p_result_obj_info <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddTableBelong(self):
		u"""mysql数据库添加告警表，表来自自定义表"""
		pres = """
		${DatabaseM}.sso|create table if not exists pw_alarm_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_mysql",
				"表英文名称": "pw_alarm_table",
				"表中文名称": "auto_表归属_mysql自定义告警表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_mysql自定义告警表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_mysql'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table|table_name_ch|auto_表归属_mysql自定义告警表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_mysql自定义告警表
		"""
		log.info('>>>>> mysql数据库添加告警表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddTableBelong(self):
		u"""mysql数据库添加输出表，表来自自定义表"""
		pres = """
		${DatabaseM}.sso|create table if not exists pw_output_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_mysql",
				"表英文名称": "pw_output_table",
				"表中文名称": "auto_表归属_mysql自定义输出表",
				"表使用对象": "输出表",
				"表周期": "普通",
				"备注": "auto_表归属_mysql自定义输出表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_mysql'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table|table_name_ch|auto_表归属_mysql自定义输出表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_mysql自定义输出表
		"""
		log.info('>>>>> mysql数据库添加输出表，表来自自定义表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddTableBelong(self):
		u"""添加告警表，表周期：日"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table1_${YMD}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_alarm_table1",
				"表中文名称": "auto_表归属_告警日表",
				"表使用对象": "告警表",
				"表周期": "日",
				"备注": "auto_表归属_告警日表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table1|table_name_ch|auto_表归属_告警日表|database_info_id|${DatabaseInfoID}|table_period|1|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_告警日表
		"""
		log.info('>>>>> 添加告警表，表周期：日 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddTableBelong(self):
		u"""添加告警表，表周期：月"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table2_${YM}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_alarm_table2",
				"表中文名称": "auto_表归属_告警月表",
				"表使用对象": "告警表",
				"表周期": "月",
				"备注": "auto_表归属_告警月表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table2|table_name_ch|auto_表归属_告警月表|database_info_id|${DatabaseInfoID}|table_period|2|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_告警月表
		"""
		log.info('>>>>> 添加告警表，表周期：月 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddTableBelong(self):
		u"""添加告警表，表周期：年"""
		pres = """
		${DatabaseP}.sso|create table pw_alarm_table3_${Y}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_alarm_table3",
				"表中文名称": "auto_表归属_告警年表",
				"表使用对象": "告警表",
				"表周期": "年",
				"备注": "auto_表归属_告警年表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_alarm_table3|table_name_ch|auto_表归属_告警年表|database_info_id|${DatabaseInfoID}|table_period|3|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_告警年表
		"""
		log.info('>>>>> 添加告警表，表周期：年 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddTableBelong(self):
		u"""添加输出表，表周期：日"""
		pres = """
		${DatabaseP}.sso|create table pw_output_table1_${YMD}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_output_table1",
				"表中文名称": "auto_表归属_输出日表",
				"表使用对象": "输出表",
				"表周期": "日",
				"备注": "auto_表归属_输出日表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table1|table_name_ch|auto_表归属_输出日表|database_info_id|${DatabaseInfoID}|table_period|1|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_输出日表
		"""
		log.info('>>>>> 添加输出表，表周期：日 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddTableBelong(self):
		u"""添加输出表，表周期：月"""
		pres = """
		${DatabaseP}.sso|create table pw_output_table2_${YM}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_output_table2",
				"表中文名称": "auto_表归属_输出月表",
				"表使用对象": "输出表",
				"表周期": "月",
				"备注": "auto_表归属_输出月表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table2|table_name_ch|auto_表归属_输出月表|database_info_id|${DatabaseInfoID}|table_period|2|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_输出月表
		"""
		log.info('>>>>> 添加输出表，表周期：月 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddTableBelong(self):
		u"""添加输出表，表周期：年"""
		pres = """
		${DatabaseP}.sso|create table pw_output_table3_${Y}(col_1 varchar(200) null, col_2 varchar(200) null, col_3 varchar(200) null, col_4 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_output_table3",
				"表中文名称": "auto_表归属_输出年表",
				"表使用对象": "输出表",
				"表周期": "年",
				"备注": "auto_表归属_输出年表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_output_table3|table_name_ch|auto_表归属_输出年表|database_info_id|${DatabaseInfoID}|table_period|3|table_object|3|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_输出年表
		"""
		log.info('>>>>> 添加输出表，表周期：年 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddTableBelong(self):
		u"""添加字典表"""
		pres = """
		${DatabaseP}.sso|create table pw_dict_table(col_1 varchar(200) null, col_2 varchar(200) null, col_3 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_dict_table",
				"表中文名称": "auto_表归属_字典表",
				"表使用对象": "字典表",
				"表周期": "普通",
				"备注": "auto_表归属_字典表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_dict_table|table_name_ch|auto_表归属_字典表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|2|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_字典表
		"""
		log.info('>>>>> 添加字典表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddTableBelong(self):
		u"""添加告警表，表英文名存在，中文名不存在"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_流程运行结果1",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres_p_result_obj_info1"
			}
		}
		checks = """
		CheckMsg|表名称已存在
		"""
		log.info('>>>>> 添加告警表，表英文名存在，中文名不存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddTableBelong(self):
		u"""添加告警表，表英文名存在，中文名也存在"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_流程运行结果1",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres_p_result_obj_info1"
			}
		}
		checks = """
		CheckMsg|表名称已存在
		"""
		log.info('>>>>> 添加告警表，表英文名存在，中文名也存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddTableBelong(self):
		u"""添加告警表，表英文名不存在，中文名不存在"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_9312_info",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_9312_p_result_obj_info"
			}
		}
		checks = """
		CheckMsg|表名称已存在
		"""
		log.info('>>>>> 添加告警表，表英文名不存在，中文名不存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddTableBelong(self):
		u"""添加告警表，当前数据库无此表"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "${DefaultDBName}",
				"表英文名称": "p_result_obj_info1",
				"表中文名称": "auto_表归属_流程运行结果1",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres_p_result_obj_info1"
			}
		}
		checks = """
		CheckMsg|表名称不存在
		"""
		log.info('>>>>> 添加告警表，当前数据库无此表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_UpdateTableBelong(self):
		u"""修改表（只能修改表中文名和备注）"""
		action = {
			"操作": "UpdateTableBelong",
			"参数": {
				"表中文名称": "auto_表归属_字典表",
				"修改内容": {
					"表中文名称": "auto_表归属_字典表2",
					"备注": "auto_表归属_字典表2"
				}
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_dict_table|table_name_ch|auto_表归属_字典表2|database_info_id|${DatabaseInfoID}|table_period|4|table_object|2|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|notnull|update_date|now|is_delete_tag|0|remark|auto_表归属_字典表2
		"""
		log.info('>>>>> 修改表（只能修改表中文名和备注） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_DeleteTableBelong(self):
		u"""删除表"""
		pres = """
		${Database}.alarm|delete from alarm_table_belong where table_name_ch = 'auto_表归属_字典表2' and is_delete_tag=1
		"""
		action = {
			"操作": "DeleteTableBelong",
			"参数": {
				"表中文名称": "auto_表归属_字典表2"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_ch|auto_表归属_字典表2|is_delete_tag|1
		"""
		log.info('>>>>> 删除表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddTableBelong(self):
		u"""添加字典表"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_dict_table",
				"表中文名称": "auto_表归属_字典表",
				"表使用对象": "字典表",
				"表周期": "普通",
				"备注": "auto_表归属_字典表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_dict_table|table_name_ch|auto_表归属_字典表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|2|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_字典表
		"""
		log.info('>>>>> 添加字典表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddTableBelong(self):
		u"""postgres数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段（decimal自动转成numeric）"""
		pres = """
		${DatabaseP}.sso|create table pw_agg_table(col_1 varchar(200) null, col_2 numeric, col_3 timestamp)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_postgres",
				"表英文名称": "pw_agg_table",
				"表中文名称": "auto_表归属_postgres多字段类型表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_postgres多字段类型表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_postgres'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_agg_table|table_name_ch|auto_表归属_postgres多字段类型表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_postgres多字段类型表
		"""
		log.info('>>>>> postgres数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段（decimal自动转成numeric） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_AddTableBelong(self):
		u"""oracle数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段（integel自动转成number）"""
		pres = """
		${DatabaseO}.sso|create table pw_agg_table(col_1 varchar2(200) null, col_2 integer, col_3 date)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_oracle",
				"表英文名称": "pw_agg_table",
				"表中文名称": "auto_表归属_oracle多字段类型表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_oracle多字段类型表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_oracle'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_agg_table|table_name_ch|auto_表归属_oracle多字段类型表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_oracle多字段类型表
		"""
		log.info('>>>>> oracle数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段（integel自动转成number） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_AddTableBelong(self):
		u"""mysql数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段"""
		pres = """
		${DatabaseM}.sso|create table pw_agg_table(col_1 varchar(200), col_2 int, col_3 datetime)||continue
		wait|10
		"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_mysql",
				"表英文名称": "pw_agg_table",
				"表中文名称": "auto_表归属_mysql多字段类型表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_mysql多字段类型表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_mysql'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|pw_agg_table|table_name_ch|auto_表归属_mysql多字段类型表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_mysql多字段类型表
		"""
		log.info('>>>>> mysql数据库添加告警表，表来自自定义表，带字符串、数值、时间三个字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddTableBelong(self):
		u"""mysql数据库添加告警表，表来自p_result_obj_info"""
		action = {
			"操作": "AddTableBelong",
			"参数": {
				"数据库名称": "auto_数据库_mysql_v32",
				"表英文名称": "p_result_obj_info",
				"表中文名称": "auto_表归属_流程运行结果表",
				"表使用对象": "告警表",
				"表周期": "普通",
				"备注": "auto_表归属_流程运行结果表"
			}
		}
		checks = """
		GetData|${Database}.alarm|select database_info_id from alarm_database_info where database_name='auto_数据库_mysql_v32'|DatabaseInfoID
		CheckData|${Database}.alarm.alarm_table_belong|1|table_name_en|p_result_obj_info|table_name_ch|auto_表归属_流程运行结果表|database_info_id|${DatabaseInfoID}|table_period|4|table_object|1|data_origin|2|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0|remark|auto_表归属_流程运行结果表
		"""
		log.info('>>>>> mysql数据库添加告警表，表来自p_result_obj_info <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		success = Result(self).run_success()
		if not success:
			saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
