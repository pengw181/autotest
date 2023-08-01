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


class DictionaryConfig(unittest.TestCase):

	log.info("装载字典配置测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警配置/字典配置.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AddDictionary(self):
		u"""字典配置，添加字典，公共字典"""
		pres = """
		${Database}.alarm|delete from alarm_dict_item where dict_group_id in (select dict_group_id from alarm_dict_group_info where dict_group_name like 'auto_字典_%')
		${Database}.alarm|delete from alarm_dict_group_info where dict_group_name like 'auto_字典_%'
		"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典描述": "auto_字典_公共字典描述",
				"字典类型": "公共字典"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.alarm.alarm_dict_group_info|1|dict_group_name|auto_字典_公共字典|dict_group_comment|auto_字典_公共字典描述|dict_group_type|1|table_belong_id|ALARM_DICT_ITEM|dict_item_key_col|null|dict_item_val_col|null|creator|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|dict_query_condition|null
		"""
		log.info('>>>>> 字典配置，添加字典，公共字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_AddDictionary(self):
		u"""字典配置，添加字典，表字典，未设置过滤条件"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典组名称": "auto_字典_表字典",
				"字典描述": "auto_字典_表字典描述",
				"字典类型": "表字典",
				"字典表名称": "auto_表归属_字典表",
				"关键字": "col_1",
				"值": "col_2"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_字典表' and is_delete_tag='0'|TableBelongID
		CheckData|${Database}.alarm.alarm_dict_group_info|1|dict_group_name|auto_字典_表字典|dict_group_comment|auto_字典_表字典描述|dict_group_type|2|table_belong_id|${TableBelongID}|dict_item_key_col|col_1|dict_item_val_col|col_2|creator|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|dict_query_condition|[]
		"""
		log.info('>>>>> 字典配置，添加字典，表字典，未设置过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddDictionary(self):
		u"""字典配置，添加字典，表字典，设置过滤条件"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典组名称": "auto_字典_表字典_带过滤条件",
				"字典描述": "auto_字典_表字典_带过滤条件描述",
				"字典类型": "表字典",
				"字典表名称": "auto_表归属_字典表",
				"关键字": "col_1",
				"值": "col_2",
				"过滤条件": {
					"操作": "添加",
					"条件": [
						{
							"过虑字段": "col_1",
							"操作关系": "LIKE",
							"比较值": "星期",
							"值类型": "文本"
						},
						{
							"过虑字段": "col_2",
							"操作关系": "!=",
							"比较值": "周四",
							"值类型": "文本"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_字典表' and is_delete_tag='0'|TableBelongID
		CheckData|${Database}.alarm.alarm_dict_group_info|1|dict_group_name|auto_字典_表字典_带过滤条件|dict_group_comment|auto_字典_表字典_带过滤条件描述|dict_group_type|2|table_belong_id|${TableBelongID}|dict_item_key_col|col_1|dict_item_val_col|col_2|creator|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|dict_query_condition|notnull
		"""
		log.info('>>>>> 字典配置，添加字典，表字典，设置过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_UpdateDictionary(self):
		u"""字典配置，修改字典，表字典，修改过滤条件"""
		action = {
			"操作": "UpdateDictionary",
			"参数": {
				"字典组名称": "auto_字典_表字典_带过滤条件",
				"修改内容": {
					"字典组名称": "auto_字典_表字典_带过滤条件2",
					"字典描述": "auto_字典_表字典_带过滤条件描述2",
					"过滤条件": {
						"操作": "修改",
						"序号": "2",
						"条件": {
							"过虑字段": "col_3",
							"操作关系": ">",
							"比较值": "col_3",
							"值类型": "日期"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_字典表' and is_delete_tag='0'|TableBelongID
		CheckData|${Database}.alarm.alarm_dict_group_info|1|dict_group_name|auto_字典_表字典_带过滤条件2|dict_group_comment|auto_字典_表字典_带过滤条件描述2|dict_group_type|2|table_belong_id|${TableBelongID}|dict_item_key_col|col_1|dict_item_val_col|col_2|creator|${LoginUser}|create_time|notnull|updater|${LoginUser}|update_time|now|dict_query_condition|notnull
		"""
		log.info('>>>>> 字典配置，修改字典，表字典，修改过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateDictionary(self):
		u"""字典配置，修改字典，表字典，删除过滤条件"""
		action = {
			"操作": "UpdateDictionary",
			"参数": {
				"字典组名称": "auto_字典_表字典_带过滤条件2",
				"修改内容": {
					"字典组名称": "auto_字典_表字典_带过滤条件",
					"字典描述": "auto_字典_表字典_带过滤条件描述",
					"过滤条件": {
						"操作": "删除",
						"序号": "2"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select table_belong_id from alarm_table_belong where table_name_ch='auto_表归属_字典表' and is_delete_tag='0'|TableBelongID
		CheckData|${Database}.alarm.alarm_dict_group_info|1|dict_group_name|auto_字典_表字典_带过滤条件|dict_group_comment|auto_字典_表字典_带过滤条件描述|dict_group_type|2|table_belong_id|${TableBelongID}|dict_item_key_col|col_1|dict_item_val_col|col_2|creator|${LoginUser}|create_time|notnull|updater|${LoginUser}|update_time|now|dict_query_condition|notnull
		"""
		log.info('>>>>> 字典配置，修改字典，表字典，删除过滤条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_SetDictionaryDetail(self):
		u"""字典配置，公共字典添加键值对"""
		action = {
			"操作": "SetDictionaryDetail",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典明细": {
					"操作": "添加",
					"键值对": [
						[
							"GD",
							"广东省"
						],
						[
							"HN",
							"湖南省"
						]
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select dict_group_id from alarm_dict_group_info where dict_group_name='auto_字典_公共字典'|DictGroupID
		CheckData|${Database}.alarm.alarm_dict_item|1|dict_group_id|${DictGroupID}|dict_item_key|GD|dict_item_value|广东省|creator|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now
		CheckData|${Database}.alarm.alarm_dict_item|1|dict_group_id|${DictGroupID}|dict_item_key|HN|dict_item_value|湖南省|creator|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now
		"""
		log.info('>>>>> 字典配置，公共字典添加键值对 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_SetDictionaryDetail(self):
		u"""字典配置，公共字典修改键值对"""
		action = {
			"操作": "SetDictionaryDetail",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典明细": {
					"操作": "编辑",
					"关键字": "GD",
					"键值对": [
						"BJ",
						"北京市"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select dict_group_id from alarm_dict_group_info where dict_group_name='auto_字典_公共字典'|DictGroupID
		CheckData|${Database}.alarm.alarm_dict_item|1|dict_group_id|${DictGroupID}|dict_item_key|BJ|dict_item_value|北京市|creator|${LoginUser}|create_time|notnull|updater|${LoginUser}|update_time|now
		CheckData|${Database}.alarm.alarm_dict_item|1|dict_group_id|${DictGroupID}|dict_item_key|HN|dict_item_value|湖南省|creator|${LoginUser}|create_time|notnull|updater|${LoginUser}|update_time|notnull
		"""
		log.info('>>>>> 字典配置，公共字典修改键值对 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_SetDictionaryDetail(self):
		u"""字典配置，公共字典删除键值对"""
		action = {
			"操作": "SetDictionaryDetail",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典明细": {
					"操作": "删除",
					"关键字": "BJ"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.alarm|select dict_group_id from alarm_dict_group_info where dict_group_name='auto_字典_公共字典'|DictGroupID
		CheckData|${Database}.alarm.alarm_dict_item|1|dict_group_id|${DictGroupID}|dict_item_key|HN|dict_item_value|湖南省|creator|${LoginUser}|create_time|notnull|updater|${LoginUser}|update_time|notnull
		"""
		log.info('>>>>> 字典配置，公共字典删除键值对 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_SetDictionaryDetail(self):
		u"""字典配置，公共字典添加键值对，关键字为空"""
		action = {
			"操作": "SetDictionaryDetail",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典明细": {
					"操作": "添加",
					"键值对": [
						[
							"",
							"广东省"
						]
					]
				}
			}
		}
		checks = """
		CheckMsg|必填项需正确填写或选择
		"""
		log.info('>>>>> 字典配置，公共字典添加键值对，关键字为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_SetDictionaryDetail(self):
		u"""字典配置，公共字典添加键值对，值为空"""
		action = {
			"操作": "SetDictionaryDetail",
			"参数": {
				"字典组名称": "auto_字典_公共字典",
				"字典明细": {
					"操作": "添加",
					"键值对": [
						[
							"GD",
							""
						]
					]
				}
			}
		}
		checks = """
		CheckMsg|必填项需正确填写或选择
		"""
		log.info('>>>>> 字典配置，公共字典添加键值对，值为空 <<<<<')
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
