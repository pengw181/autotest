# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:10

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class Field(unittest.TestCase):

	log.info("装载专业领域管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_FieldDataClear(self):
		u"""专业领域管理,数据清理"""
		action = {
			"操作": "FieldDataClear",
			"参数": {
				"专业领域名称": "pw领域"
			}
		}
		log.info('>>>>> 专业领域管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddField(self):
		u"""添加专业领域"""
		action = {
			"操作": "AddField",
			"参数": {
				"专业领域名称": "pw领域"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|pw领域|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|update_date|now|updater|${LoginUser}
		"""
		log.info('>>>>> 添加专业领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddField(self):
		u"""添加专业领域,专业名称本领域存在"""
		action = {
			"操作": "AddField",
			"参数": {
				"专业领域名称": "pw领域"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加专业领域,专业名称本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddField(self):
		u"""添加专业领域,专业名称本领域不存在,在其他领域存在"""
		pres = """
		${Database}.main|delete from tn_template_type where temp_type_name='pw领域' 
		${Database}.main|insert into tn_template_type(temp_type_id, temp_type_name, domain_id, belong_id,user_id,create_time,updater,update_date) values(uuid(), 'pw领域', 'AiSeeCN','440100','pw',now(),'pw',now())
		"""
		action = {
			"操作": "AddField",
			"参数": {
				"专业领域名称": "pw领域"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|pw领域|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|update_date|now|updater|${LoginUser}
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|pw领域|belong_id|440100|domain_id|AiSeeCN|user_id|pw|create_time|notnull|update_date|notnull|updater|pw
		"""
		log.info('>>>>> 添加专业领域,专业名称本领域不存在,在其他领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateField(self):
		u"""修改领域名称"""
		pres = """
		${Database}.main|delete from tn_template_type where temp_type_name='pw领域' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "UpdateField",
			"参数": {
				"专业领域名称": "pw领域",
				"修改内容": {
					"专业领域名称": "pw领域新"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|pw领域新|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|notnull|update_date|now|updater|${LoginUser}
		"""
		log.info('>>>>> 修改领域名称 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_DeleteField(self):
		u"""删除领域"""
		action = {
			"操作": "DeleteField",
			"参数": {
				"专业领域名称": "pw领域新"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_template_type|0|temp_type_name|pw领域新
		"""
		log.info('>>>>> 删除领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_FieldDataClear(self):
		u"""专业领域管理,数据清理"""
		action = {
			"操作": "FieldDataClear",
			"参数": {
				"专业领域名称": "auto域"
			}
		}
		log.info('>>>>> 专业领域管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_8_AddField(self):
		u"""添加专业领域"""
		action = {
			"操作": "AddField",
			"参数": {
				"专业领域名称": "auto域"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|update_date|now|updater|${LoginUser}
		"""
		log.info('>>>>> 添加专业领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_ListField(self):
		u"""查询专业领域，按专业领域名称查询"""
		action = {
			"操作": "ListField",
			"参数": {
				"查询条件": {
					"专业领域名称": "auto"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询专业领域，按专业领域名称查询 <<<<<')
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
