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


class DatabaseConfig(unittest.TestCase):

	log.info("装载关系型数据库配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AddDatabase(self):
		u"""添加postgres数据库"""
		pres = """
		${Database}.alarm|delete from alarm_database_info where database_name like 'auto_数据库%'
		"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库类型": "Postgresql",
				"数据库名称": "auto_数据库_postgres",
				"服务名/SID": "postgres",
				"连接地址": "192.168.88.116",
				"端口": "4310",
				"用户名": "sso",
				"密码": "sso_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_database_info|1|database_name|auto_数据库_postgres|database_type|4|database_sid|postgres|database_address|192.168.88.116|database_port|4310|database_username|sso|database_password|notnull|creator|${LoginUser}|updater|${LoginUser}|is_delete_tag|0|data_origin|2|create_date|now|update_date|now
		"""
		log.info('>>>>> 添加postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_AddDatabase(self):
		u"""添加postgres数据库，数据库名称已存在"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库类型": "Postgresql",
				"数据库名称": "auto_数据库_postgres",
				"服务名/SID": "postgres",
				"连接地址": "192.168.88.116",
				"端口": "4310",
				"用户名": "sso",
				"密码": "sso_pass"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加postgres数据库，数据库名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_TestDatabase(self):
		u"""测试postgres数据库"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_数据库_postgres"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddDatabase(self):
		u"""添加oracle数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库类型": "Oracle",
				"数据库名称": "auto_数据库_oracle",
				"服务名/SID": "AiSee",
				"连接地址": "192.168.88.116",
				"端口": "2310",
				"用户名": "sso",
				"密码": "sso_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_database_info|1|database_name|auto_数据库_oracle|database_type|1|database_sid|AiSee|database_address|192.168.88.116|database_port|2310|database_username|sso|database_password|notnull|creator|${LoginUser}|updater|${LoginUser}|is_delete_tag|0|data_origin|2|create_date|now|update_date|now
		"""
		log.info('>>>>> 添加oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestDatabase(self):
		u"""测试oracle数据库"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_数据库_oracle"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddDatabase(self):
		u"""添加mysql数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库类型": "MySQL",
				"数据库名称": "auto_数据库_mysql",
				"服务名/SID": "alarm",
				"连接地址": "192.168.88.116",
				"端口": "3310",
				"用户名": "alarm",
				"密码": "alarm_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_database_info|1|database_name|auto_数据库_mysql|database_type|3|database_sid|alarm|database_address|192.168.88.116|database_port|3310|database_username|alarm|database_password|notnull|creator|${LoginUser}|updater|${LoginUser}|is_delete_tag|0|data_origin|2|create_date|now|update_date|now
		"""
		log.info('>>>>> 添加mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_TestDatabase(self):
		u"""测试mysql数据库"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_数据库_oracle"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateDatabase(self):
		u"""修改数据库"""
		action = {
			"操作": "UpdateDatabase",
			"参数": {
				"数据库名称": "auto_数据库_mysql",
				"修改内容": {
					"数据库类型": "MySQL",
					"数据库名称": "auto_数据库_mysql",
					"服务名/SID": "sso",
					"连接地址": "192.168.88.116",
					"端口": "3310",
					"用户名": "sso",
					"密码": "sso_pass"
				}
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_database_info|1|database_name|auto_数据库_mysql|database_type|3|database_sid|sso|database_address|192.168.88.116|database_port|3310|database_username|sso|database_password|notnull|creator|${LoginUser}|updater|${LoginUser}|is_delete_tag|0|data_origin|2|create_date|notnull|update_date|now
		"""
		log.info('>>>>> 修改数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_TestDatabase(self):
		u"""测试mysql数据库"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_数据库_mysql"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_10_AddDatabase(self):
		u"""UNTEST,添加v32 mysql数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库类型": "MySQL",
				"数据库名称": "auto_数据库_mysql_v32",
				"服务名/SID": "aisee1",
				"连接地址": "192.168.88.116",
				"端口": "3306",
				"用户名": "aisee1",
				"密码": "aisee1_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_database_info|1|database_name|auto_数据库_mysql_v32|database_type|3|database_sid|aisee1|database_address|192.168.88.116|database_port|3306|database_username|aisee1|database_password|notnull|creator|${LoginUser}|updater|${LoginUser}|is_delete_tag|0|data_origin|2|create_date|now|update_date|now
		"""
		log.info('>>>>> UNTEST,添加v32 mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_TestDatabase(self):
		u"""测试mysql数据库"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_数据库_mysql_v32"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试mysql数据库 <<<<<')
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
