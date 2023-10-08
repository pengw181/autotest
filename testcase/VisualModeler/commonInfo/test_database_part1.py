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


class DatabasePart1(unittest.TestCase):

	log.info("装载数据库管理测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_DBDataClear(self):
		u"""数据库管理,数据清理"""
		action = {
			"操作": "DBDataClear",
			"参数": {
				"数据库名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据库管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddDatabase(self):
		u"""添加mysql数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据库驱动": "mysql",
				"数据库URL": "jdbc:mysql://192.168.88.116:3310/aisee1",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_mysql数据库|db_url|jdbc:mysql://192.168.88.116:3310/aisee1|db_driver|com.mysql.jdbc.Driver|username|aisee1|pwd|0lNWyyAzmfcPQvUlnAVq6g==|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|0
		"""
		log.info('>>>>> 添加mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddDatabase(self):
		u"""添加数据库,名称本领域存在"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据库驱动": "mysql",
				"数据库URL": "jdbc:mysql://192.168.88.116:3310/aisee1",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加数据库,名称本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddDatabase(self):
		u"""添加数据库,名称本领域不存在,在其他领域存在"""
		pres = """
		${Database}.main|delete from tn_db_cfg where db_name='auto_mysql数据库'
		${Database}.main|insert into tn_db_cfg(db_id,db_name,db_url,db_driver,username,pwd,create_time,update_time,del_flag,data_type_id,create_by,update_by,belong_id,domain_id,belong_type,data_origin) values(uuid(),'auto_mysql数据库','jdbc:mysql://192.168.88.26:3306/lwb','com.mysql.jdbc.Driver','lwb','Xq6SDnCFKpo=',now(),now(),null,0,'pw','pw','440100','AiSeeCN',1,2)
		"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据库驱动": "mysql",
				"数据库URL": "jdbc:mysql://192.168.88.116:3310/aisee1",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_mysql数据库|db_url|jdbc:mysql://192.168.88.116:3310/aisee1|db_driver|com.mysql.jdbc.Driver|username|aisee1|pwd|0lNWyyAzmfcPQvUlnAVq6g==|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|0
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_mysql数据库|db_url|jdbc:mysql://192.168.88.26:3306/lwb|db_driver|com.mysql.jdbc.Driver|username|lwb|pwd|Xq6SDnCFKpo=|del_flag|null|belong_id|440100|domain_id|AiSeeCN|create_by|pw|create_time|notnull|update_time|notnull|update_by|pw|belong_type|1|data_origin|2|data_type_id|0
		"""
		log.info('>>>>> 添加数据库,名称本领域不存在,在其他领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestDatabase(self):
		u"""测试mysql数据库连通性"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试mysql数据库连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddDatabase(self):
		u"""添加oracle数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据库驱动": "oracle",
				"数据库URL": "jdbc:oracle:thin:@192.168.88.116:2310/AiSee",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_oracle数据库|db_url|jdbc:oracle:thin:@192.168.88.116:2310/AiSee|db_driver|oracle.jdbc.driver.OracleDriver|username|aisee1|pwd|notnull|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|1
		"""
		log.info('>>>>> 添加oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_TestDatabase(self):
		u"""测试oracle数据库连通性"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_oracle数据库"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试oracle数据库连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddDatabase(self):
		u"""添加postgres数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据库驱动": "postgresql",
				"数据库URL": "jdbc:postgresql://192.168.88.116:4310/postgres",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_postgres数据库|db_url|jdbc:postgresql://192.168.88.116:4310/postgres|db_driver|org.postgresql.Driver|username|aisee1|pwd|notnull|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|1
		"""
		log.info('>>>>> 添加postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_TestDatabase(self):
		u"""测试postgres数据库连通性"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_postgres数据库"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试postgres数据库连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateDatabase(self):
		u"""修改数据库"""
		pres = """
		${Database}.main|delete from tn_db_cfg where db_name='auto_mysql数据库' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "UpdateDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"修改内容": {
					"数据库名称": "auto_mysql数据库",
					"数据库驱动": "mysql",
					"数据库URL": "jdbc:mysql://192.168.88.116:3310/aisee1",
					"用户名": "aisee1",
					"密码": "aisee2_pass",
					"归属类型": "外部库",
					"数据类型": "公有"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_mysql数据库|db_url|jdbc:mysql://192.168.88.116:3310/aisee1|db_driver|com.mysql.jdbc.Driver|username|aisee1|pwd|notnull|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|1
		"""
		log.info('>>>>> 修改数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_TestDatabase(self):
		u"""测试mysql数据库连通性.密码错误"""
		action = {
			"操作": "TestDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库"
			}
		}
		checks = """
		CheckMsg|测试失败：数据库URL、用户名或密码错误
		"""
		log.info('>>>>> 测试mysql数据库连通性.密码错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_DeleteDatabase(self):
		u"""删除oracle数据库"""
		action = {
			"操作": "DeleteDatabase",
			"参数": {
				"数据库名称": "auto_oracle数据库"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_db_cfg|0|db_name|auto_oracle数据库
		"""
		log.info('>>>>> 删除oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_DeleteDatabase(self):
		u"""删除mysql数据库"""
		action = {
			"操作": "DeleteDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_db_cfg|0|db_name|auto_mysql数据库
		"""
		log.info('>>>>> 删除mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_DeleteDatabase(self):
		u"""删除postgres数据库"""
		action = {
			"操作": "DeleteDatabase",
			"参数": {
				"数据库名称": "auto_postgres数据库"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_db_cfg|0|db_name|auto_postgres数据库
		"""
		log.info('>>>>> 删除postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddDatabase(self):
		u"""添加数据库,oracle数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据库驱动": "oracle",
				"数据库URL": "jdbc:oracle:thin:@192.168.88.116:2310/AiSee",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_oracle数据库|db_url|jdbc:oracle:thin:@192.168.88.116:2310/AiSee|db_driver|oracle.jdbc.driver.OracleDriver|username|aisee1|pwd|notnull|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|1
		"""
		log.info('>>>>> 添加数据库,oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddDatabase(self):
		u"""添加数据库,mysql数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据库驱动": "mysql",
				"数据库URL": "jdbc:mysql://192.168.88.116:3310/aisee1",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_mysql数据库|db_url|jdbc:mysql://192.168.88.116:3310/aisee1|db_driver|com.mysql.jdbc.Driver|username|aisee1|pwd|0lNWyyAzmfcPQvUlnAVq6g==|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|0
		"""
		log.info('>>>>> 添加数据库,mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddDatabase(self):
		u"""添加数据库,postgres数据库"""
		action = {
			"操作": "AddDatabase",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据库驱动": "postgresql",
				"数据库URL": "jdbc:postgresql://192.168.88.116:4310/postgres",
				"用户名": "aisee1",
				"密码": "aisee1_pass",
				"归属类型": "外部库",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_db_cfg|1|db_name|auto_postgres数据库|db_url|jdbc:postgresql://192.168.88.116:4310/postgres|db_driver|org.postgresql.Driver|username|aisee1|pwd|notnull|del_flag|null|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|belong_type|1|data_origin|2|data_type_id|0
		"""
		log.info('>>>>> 添加数据库,postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_ListDatabase(self):
		u"""查询数据库配置，按数据库名称查询"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库名称": "auto"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库名称查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_ListDatabase(self):
		u"""查询数据库配置，按数据库URL查询"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库URL": "192.168.88.116"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库URL查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，oracle"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "oracle"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，oracle <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，mysql"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "mysql"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，mysql <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，sql server"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "sql server"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，sql server <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，postgresql"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "postgresql"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，postgresql <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，mariadb"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "mariadb"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，mariadb <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_ListDatabase(self):
		u"""查询数据库配置，按数据库驱动查询，sqlserver-jtds"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"数据库驱动": "sqlserver-jtds"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按数据库驱动查询，sqlserver-jtds <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_ListDatabase(self):
		u"""查询数据库配置，按归属类型查询"""
		action = {
			"操作": "ListDatabase",
			"参数": {
				"查询条件": {
					"归属类型": "外部库"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询数据库配置，按归属类型查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_DBTableClear(self):
		u"""数据管理，mysql数据库，数据表清理，清理测试表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"模糊匹配": "否"
			}
		}
		log.info('>>>>> 数据管理，mysql数据库，数据表清理，清理测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_28_DBTableClear(self):
		u"""数据管理，mysql数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据管理，mysql数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_29_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，数据表名称为空"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|数据表名称不允许为空
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_en_name|auto_test_table1|tab_type|0|is_alive|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，数据表名称为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，表英文名为空"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": ""
			}
		}
		checks = """
		CheckMsg|数据表英文名不允许为空
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表1|tab_type|0|is_alive|1|remark|auto_测试表1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，表英文名为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，数据表名称在列表已添加过"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|表中文名或英文名已存在
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table1|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，数据表名称在列表已添加过 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，表英文名在列表已添加过"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|表中文名或英文名已存在
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表1|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，表英文名在列表已添加过 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，数据表名称输入字符校验"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表1%",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|数据表名称不能包含特殊字符
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表1%|tab_en_name|auto_test_table1|tab_type|0|is_alive|1|remark|auto_测试表1%|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，数据表名称输入字符校验 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表，表英文名输入字符校验"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": "auto_test_table%"
			}
		}
		checks = """
		CheckMsg|表英文名称只能包含字母、数字、下划线，且不能以数字开头
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表1|tab_en_name|auto_test_table%|tab_type|0|is_alive|1|remark|auto_测试表1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表，表英文名输入字符校验 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col_index",
						"列名(自定义)": "序号",
						"列类型": "字符",
						"长度": "10"
					},
					{
						"列名(数据库)": "user_name",
						"列名(自定义)": "姓名",
						"列类型": "字符",
						"长度": "100"
					},
					{
						"列名(数据库)": "comsume",
						"列名(自定义)": "消费金额",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"列名(数据库)": "balance",
						"列名(自定义)": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"列名(数据库)": "order_time",
						"列名(自定义)": "订单时间",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						]
					},
					{
						"列名(数据库)": "accept_date",
						"列名(自定义)": "收货日期",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd",
							""
						],
						"输出格式": [
							"yyyy-MM-dd",
							""
						]
					},
					{
						"列名(数据库)": "adddress",
						"列名(自定义)": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，列名(数据库)包含特殊字符"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col%",
						"列名(自定义)": "序号2",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|序号2|column_en_name|col%|column_id|col%|column_type|STRING|remark|序号2|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，列名(数据库)包含特殊字符 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，列名(数据库)包含中文"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col名称",
						"列名(自定义)": "序号3",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|序号3|column_en_name|col名称|column_id|col名称|column_type|STRING|remark|序号3|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，列名(数据库)包含中文 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，列名(数据库)以数字开头"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "1col",
						"列名(自定义)": "序号4",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|序号4|column_en_name|1col|column_id|1col|column_type|STRING|remark|序号4|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，列名(数据库)以数字开头 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，列名(数据库)包含空格在中间"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col name",
						"列名(自定义)": "序号5",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|序号5|column_en_name|col name|column_id|col name|column_type|STRING|remark|序号5|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，列名(数据库)包含空格在中间 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，修改修改列名(自定义)"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名",
				"修改内容": {
					"列信息": {
						"列名(自定义)": "姓名2"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名2|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名2|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，修改修改列名(自定义) <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，修改长度，由长变短"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"长度": "10"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名2|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名2|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，修改长度，由长变短 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，修改长度，由短变长"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"长度": "200"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名2|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名2|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，修改长度，由短变长 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，还原列名(自定义)"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"列名(自定义)": "姓名"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，还原列名(自定义) <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，修改日期格式"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "收货日期",
				"修改内容": {
					"列信息": {
						"输入格式": [
							"yyyy/MM/dd",
							""
						],
						"输出格式": [
							"yyyy/MM/dd",
							""
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy/MM/dd|col_out_format|yyyy/MM/dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，修改日期格式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_EditDBTableCol(self):
		u"""数据管理，mysql数据库，数据表修改字段，修改日期格式，改成自定义"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "收货日期",
				"修改内容": {
					"列信息": {
						"输入格式": [
							"自定义",
							"yyyy-MM-dd"
						],
						"输出格式": [
							"自定义",
							"yyyy-MM-dd"
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表修改字段，修改日期格式，改成自定义 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，字段中文名已存在"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "username",
						"列名(自定义)": "姓名",
						"列类型": "字符",
						"长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名已存在
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|姓名|column_en_name|username|column_id|username|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，字段中文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段，字段英文名已存在"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "user_name",
						"列名(自定义)": "姓名b",
						"列类型": "字符",
						"长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名已存在
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|姓名b|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名b|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段，字段英文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_DeleteDBTableCol(self):
		u"""数据管理，mysql数据库，数据表删除字段"""
		action = {
			"操作": "DeleteDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "账户余额"
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}|column_chi_name|账户余额
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表删除字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表已删除字段重新添加"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "balance",
						"列名(自定义)": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|200|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|notnull|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表已删除字段重新添加 <<<<<')
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
