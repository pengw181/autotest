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


class FTP(unittest.TestCase):

	log.info("装载远程FTP服务器管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_FTPDataClear(self):
		u"""远程FTP服务器管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_ftp_server_cfg where server_name like 'auto_%'
		"""
		action = {
			"操作": "FTPDataClear",
			"参数": {
				"服务器名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 远程FTP服务器管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddFTP(self):
		u"""添加远程FTP服务器"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_ftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass",
				"服务器类型": "ftp",
				"服务器编码": "UTF-8",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_ftp|server_ip|192.168.88.132|server_port|21|server_type|0|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|data_origin|2|data_type_id|1|server_encoding|UTF-8
		"""
		log.info('>>>>> 添加远程FTP服务器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddFTP(self):
		u"""添加远程FTP服务器,服务器名称在本领域存在"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_ftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass",
				"服务器类型": "ftp",
				"服务器编码": "UTF-8",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加远程FTP服务器,服务器名称在本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddFTP(self):
		u"""添加远程FTP服务器"""
		pres = """
		${Database}.main|delete from tn_ftp_server_cfg where server_name='auto_ftp' 
		${Database}.main|insert into tn_ftp_server_cfg(server_id, data_type_id, server_name, server_ip, server_port, server_type, server_user, server_pwd, belong_id, domain_id, data_origin, server_encoding, create_time, update_time, create_by, update_by) values (uuid(),1,'auto_ftp','192.168.88.132','21','0','viper.catalog','8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5','440100','AiSeeCN','2','UTF-8',now(),now(),'pw','pw')
		"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_ftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass",
				"服务器类型": "ftp",
				"服务器编码": "UTF-8",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_ftp|server_ip|192.168.88.132|server_port|21|server_type|0|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|data_origin|2|data_type_id|1|server_encoding|UTF-8
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_ftp|server_ip|192.168.88.132|server_port|21|server_type|0|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|notnull|update_time|notnull|create_by|pw|update_by|pw|belong_id|440100|domain_id|AiSeeCN|data_origin|2|data_type_id|1|server_encoding|UTF-8
		"""
		log.info('>>>>> 添加远程FTP服务器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestFTP(self):
		u"""测试ftp连通性"""
		action = {
			"操作": "TestFTP",
			"参数": {
				"服务器名称": "auto_ftp"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试ftp连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddFTP(self):
		u"""添加远程FTP服务器,密码错误"""
		pres = """
		${Database}.main|delete from tn_ftp_server_cfg where server_name='auto_sftp'
		"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_sftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "22",
				"用户名": "viper.catalog",
				"密码": "viper.catalog",
				"服务器类型": "sftp",
				"服务器编码": "UTF-8",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|用户名或密码错误
		CheckData|${Database}.main.tn_ftp_server_cfg|0|server_name|auto_sftp|server_ip|192.168.88.132|server_port|22
		"""
		log.info('>>>>> 添加远程FTP服务器,密码错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateFTP(self):
		u"""修改ftp"""
		pres = """
		${Database}.main|delete from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"服务器名称": "auto_ftp",
				"修改内容": {
					"服务器名称": "auto_sftp",
					"服务器IP": "192.168.88.132",
					"服务器端口": "22",
					"用户名": "viper.catalog",
					"密码": "viper.catalog_pass",
					"服务器类型": "sftp",
					"服务器编码": "GBK",
					"数据类型": "私有"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_sftp|server_ip|192.168.88.132|server_port|22|server_type|1|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|data_origin|2|data_type_id|0|server_encoding|GBK
		"""
		log.info('>>>>> 修改ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_TestFTP(self):
		u"""测试sftp连通性"""
		action = {
			"操作": "TestFTP",
			"参数": {
				"服务器名称": "auto_sftp"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试sftp连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_DeleteFTP(self):
		u"""删除远程FTP服务器"""
		action = {
			"操作": "DeleteFTP",
			"参数": {
				"服务器名称": "auto_sftp"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_ftp_server_cfg|0|server_name|auto_sftp
		"""
		log.info('>>>>> 删除远程FTP服务器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_FTPDataClear(self):
		u"""远程FTP服务器管理,数据清理,ftp"""
		action = {
			"操作": "FTPDataClear",
			"参数": {
				"服务器名称": "auto_ftp"
			}
		}
		log.info('>>>>> 远程FTP服务器管理,数据清理,ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_11_AddFTP(self):
		u"""添加远程FTP服务器"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_ftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass",
				"服务器类型": "ftp",
				"服务器编码": "UTF-8",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_ftp|server_ip|192.168.88.132|server_port|21|server_type|0|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|data_origin|2|data_type_id|0|server_encoding|UTF-8
		"""
		log.info('>>>>> 添加远程FTP服务器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_FTPDataClear(self):
		u"""远程FTP服务器管理,数据清理,sftp"""
		action = {
			"操作": "FTPDataClear",
			"参数": {
				"服务器名称": "auto_sftp"
			}
		}
		log.info('>>>>> 远程FTP服务器管理,数据清理,sftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_13_AddFTP(self):
		u"""添加远程SFTP服务器"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"服务器名称": "auto_sftp",
				"服务器IP": "192.168.88.132",
				"服务器端口": "22",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass",
				"服务器类型": "sftp",
				"服务器编码": "UTF-8",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_ftp_server_cfg|1|server_name|auto_sftp|server_ip|192.168.88.132|server_port|22|server_type|1|server_user|viper.catalog|server_pwd|8pI614D9vn3+jqO4NFK5cSPu8b5b7cc5|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|data_origin|2|data_type_id|0|server_encoding|UTF-8
		"""
		log.info('>>>>> 添加远程SFTP服务器 <<<<<')
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
