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


class AlarmPlanConfig(unittest.TestCase):

	log.info("装载告警计划测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警配置/告警计划.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AlarmPlanDataClear(self):
		u"""告警计划配置数据清理"""
		action = {
			"操作": "AlarmPlanDataClear",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 告警计划配置数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddAlarmPlan(self):
		u"""添加告警计划，配置正确"""
		pres = """
		${Database}.alarm|delete from alarm_plan_info where alarm_plan_name like 'auto_告警计划%' and is_delete_tag=1
		${Database}.alarm|delete from alarm_tag where 1=1
		${Database}.alarm|INSERT INTO alarm_tag (alarm_tag_id, alarm_tag_name, alarm_tag_type) VALUES ('10000001', 'tag_name1', '1')
		${Database}.alarm|INSERT INTO alarm_tag (alarm_tag_id, alarm_tag_name, alarm_tag_type) VALUES ('10000002', 'tag_region1', '2')
		${Database}.alarm|INSERT INTO alarm_tag (alarm_tag_id, alarm_tag_name, alarm_tag_type) VALUES ('10000003', 'tag_name2', '1')
		"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_info告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_UpdateAlarmPlanStatus(self):
		u"""启用告警计划"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_RedoAlarmPlan(self):
		u"""重调告警计划"""
		action = {
			"操作": "RedoAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateAlarmPlanStatus(self):
		u"""禁用告警计划"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划|alarm_plan_state|0|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 禁用告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_UpdateAlarmPlan(self):
		u"""修改告警计划"""
		action = {
			"操作": "UpdateAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"修改内容": {
					"告警计划名称": "auto_告警计划_更新版",
					"告警类型": "结构化数据",
					"数据源名称": "auto_元数据_info告警表",
					"标签分类": "tag_region1",
					"领域标签": "tag_name2",
					"计划描述": "auto_告警计划_更新版"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_更新版|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name2|alarm_plan_desc|auto_告警计划_更新版|alarm_plan_state|0|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 修改告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_DeleteAlarmPlan(self):
		u"""删除告警计划"""
		action = {
			"操作": "DeleteAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_更新版"
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_更新版|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name2|alarm_plan_desc|auto_告警计划_更新版|alarm_plan_state|0|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|notnull|is_delete_tag|1
		"""
		log.info('>>>>> 删除告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddAlarmPlan(self):
		u"""使用已删除的告警计划名称重新添加告警计划"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_更新版",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_info告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_更新版"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_更新版|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_更新版|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_更新版|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name2|alarm_plan_desc|auto_告警计划_更新版|alarm_plan_state|0|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|notnull|is_delete_tag|1
		"""
		log.info('>>>>> 使用已删除的告警计划名称重新添加告警计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddAlarmPlan(self):
		u"""添加告警计划，告警日表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_告警日表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_告警日表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_告警日表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警日表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警日表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警日表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，告警日表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddAlarmPlan(self):
		u"""添加告警计划，告警月表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_告警月表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_告警月表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_告警月表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警月表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警月表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警月表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，告警月表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddAlarmPlan(self):
		u"""添加告警计划，告警年表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_告警年表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_告警年表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_告警年表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警年表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警年表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警年表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，告警年表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddAlarmPlan(self):
		u"""添加告警计划，流程运行结果表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_流程运行结果",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_info告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_流程运行结果"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_流程运行结果|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_流程运行结果|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，流程运行结果表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddAlarmPlan(self):
		u"""添加告警计划，网元其它资料告警表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_网元其它资料告警表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_vm告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_网元其它资料告警表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_vm告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_网元其它资料告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_网元其它资料告警表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，网元其它资料告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddAlarmPlan(self):
		u"""添加告警计划，postgres告警表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_postgres告警表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_postgres告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_postgres告警表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_postgres告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_postgres告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_postgres告警表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，postgres告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddAlarmPlan(self):
		u"""添加告警计划，oracle告警表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_oracle告警表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_oracle告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_oracle告警表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_oracle告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_oracle告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_oracle告警表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，oracle告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddAlarmPlan(self):
		u"""添加告警计划，mysql告警表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_mysql告警表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_mysql告警表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_mysql告警表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_mysql告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_mysql告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_mysql告警表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，mysql告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddAlarmPlan(self):
		u"""添加告警计划，postgres告警表，多字段类型表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_postgres多字段类型表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_postgres多字段类型表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_postgres多字段类型表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_postgres多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_postgres多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_postgres多字段类型表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，postgres告警表，多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddAlarmPlan(self):
		u"""添加告警计划，oracle告警表，多字段类型表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_oracle多字段类型表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_oracle多字段类型表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_oracle多字段类型表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_oracle多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_oracle多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_oracle多字段类型表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，oracle告警表，多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddAlarmPlan(self):
		u"""添加告警计划，mysql告警表，多字段类型表"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_mysql多字段类型表",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_mysql多字段类型表",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_mysql多字段类型表"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_mysql多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_mysql多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_mysql多字段类型表|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，mysql告警表，多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddAlarmPlan(self):
		u"""添加告警计划，mysql告警表，流程运行结果_v32"""
		action = {
			"操作": "AddAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_流程运行结果_v32",
				"告警类型": "结构化数据",
				"数据源名称": "auto_元数据_流程运行结果",
				"标签分类": "tag_region1",
				"领域标签": "tag_name1",
				"计划描述": "auto_告警计划_流程运行结果_v32"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_流程运行结果' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_流程运行结果_v32|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_流程运行结果_v32|alarm_plan_state|0|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加告警计划，mysql告警表，流程运行结果_v32 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_告警日表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_告警日表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警日表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警日表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警日表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_告警日表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_告警月表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_告警月表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警月表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警月表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警月表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_告警月表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_告警年表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_告警年表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_告警年表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_告警年表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_告警年表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_告警年表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_流程运行结果"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_流程运行结果",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_info告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_流程运行结果|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_流程运行结果|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_流程运行结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_网元其它资料告警表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_网元其它资料告警表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_vm告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_网元其它资料告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_网元其它资料告警表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_网元其它资料告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_postgres告警表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_postgres告警表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_postgres告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_postgres告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_postgres告警表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_postgres告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_oracle告警表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_oracle告警表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_oracle告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_oracle告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_oracle告警表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_oracle告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_mysql告警表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_mysql告警表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_mysql告警表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_mysql告警表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_mysql告警表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_mysql告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_postgres多字段类型表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_postgres多字段类型表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_postgres多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_postgres多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_postgres多字段类型表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_postgres多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_oracle多字段类型表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_oracle多字段类型表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_oracle多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_oracle多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_oracle多字段类型表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_oracle多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_mysql多字段类型表"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_mysql多字段类型表",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_mysql多字段类型表' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_mysql多字段类型表|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_mysql多字段类型表|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_mysql多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_UpdateAlarmPlanStatus(self):
		u"""启用告警计划：auto_告警计划_流程运行结果_v32"""
		action = {
			"操作": "UpdateAlarmPlanStatus",
			"参数": {
				"告警计划名称": "auto_告警计划_流程运行结果_v32",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select metadata_id from alarm_metadata_info where metadata_name='auto_元数据_流程运行结果' and is_delete_tag=0|MetadataID
		CheckData|${Database}.alarm.alarm_plan_info|1|data_source_id|${MetadataID}|metadata_id|${MetadataID}|alarm_plan_name|auto_告警计划_流程运行结果_v32|alarm_type_id|1|alarm_tag_content|tag_region1,tag_name1|alarm_plan_desc|auto_告警计划_流程运行结果_v32|alarm_plan_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 启用告警计划：auto_告警计划_流程运行结果_v32 <<<<<')
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
