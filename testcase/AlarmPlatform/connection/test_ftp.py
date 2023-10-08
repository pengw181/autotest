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


class FTPConfig(unittest.TestCase):

	log.info("装载FTP配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_FTPDataClear(self):
		u"""ftp配置数据清理，同时将引用ftp的告警规则的文件存储的ftp_config_id置为9999"""
		pres = """
		${Database}.alarm|update alarm_storage_file_info set ftp_config_id='9999' where ftp_config_id in (select ftp_config_id from alarm_ftp_config where ftp_name like 'auto_ftp%')
		"""
		action = {
			"操作": "FTPDataClear",
			"参数": {
				"FTP名称": "auto_ftp",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> ftp配置数据清理，同时将引用ftp的告警规则的文件存储的ftp_config_id置为9999 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddFTP(self):
		u"""添加ftp配置，配置正确"""
		pres = """
		${Database}.alarm|delete from alarm_ftp_config where ftp_name like 'auto_ftp%' and is_delete_tag=1
		"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp",
				"连接地址": "192.168.88.132",
				"端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_ftp_config|1|ftp_name|auto_ftp|ftp_hostname|192.168.88.132|ftp_port|21|ftp_username|viper.catalog|ftp_password|notnull|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加ftp配置，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddFTP(self):
		u"""添加ftp配置，地址错误"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp1",
				"连接地址": "192.168.88.130",
				"端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass"
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 添加ftp配置，地址错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddFTP(self):
		u"""添加ftp配置，端口错误"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp1",
				"连接地址": "192.168.88.132",
				"端口": "22",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass"
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 添加ftp配置，端口错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddFTP(self):
		u"""添加ftp配置，用户名错误"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp1",
				"连接地址": "192.168.88.132",
				"端口": "21",
				"用户名": "viper.catalog1",
				"密码": "viper.catalog_pass"
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 添加ftp配置，用户名错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddFTP(self):
		u"""添加ftp配置，密码错误"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp1",
				"连接地址": "192.168.88.132",
				"端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass1"
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 添加ftp配置，密码错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateFTP(self):
		u"""修改ftp配置，配置正确"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"FTP名称": "auto_ftp",
				"修改内容": {
					"FTP名称": "auto_ftp2",
					"连接地址": "192.168.88.132",
					"端口": "21",
					"用户名": "viper.catalog",
					"密码": "viper.catalog_pass"
				}
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_ftp_config|1|ftp_name|auto_ftp2|ftp_hostname|192.168.88.132|ftp_port|21|ftp_username|viper.catalog|ftp_password|notnull|creator|${LoginUser}|updater|${LoginUser}|create_date|notnull|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 修改ftp配置，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateFTP(self):
		u"""修改ftp配置，地址错误"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"FTP名称": "auto_ftp2",
				"修改内容": {
					"FTP名称": "auto_ftp2",
					"连接地址": "192.168.88.130",
					"端口": "21",
					"用户名": "viper.catalog",
					"密码": "viper.catalog_pass"
				}
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 修改ftp配置，地址错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateFTP(self):
		u"""修改ftp配置，端口错误"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"FTP名称": "auto_ftp2",
				"修改内容": {
					"FTP名称": "auto_ftp2",
					"连接地址": "192.168.88.132",
					"端口": "22",
					"用户名": "viper.catalog",
					"密码": "viper.catalog_pass"
				}
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 修改ftp配置，端口错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateFTP(self):
		u"""修改ftp配置，用户名错误"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"FTP名称": "auto_ftp2",
				"修改内容": {
					"FTP名称": "auto_ftp2",
					"连接地址": "192.168.88.132",
					"端口": "21",
					"用户名": "viper.catalog1",
					"密码": "viper.catalog_pass"
				}
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 修改ftp配置，用户名错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_UpdateFTP(self):
		u"""修改ftp配置，密码错误"""
		action = {
			"操作": "UpdateFTP",
			"参数": {
				"FTP名称": "auto_ftp2",
				"修改内容": {
					"FTP名称": "auto_ftp2",
					"连接地址": "192.168.88.132",
					"端口": "21",
					"用户名": "viper.catalog",
					"密码": "viper.catalog_pass1"
				}
			}
		}
		checks = """
		CheckMsg|连接失败
		"""
		log.info('>>>>> 修改ftp配置，密码错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_TestFTP(self):
		u"""测试ftp配置"""
		action = {
			"操作": "TestFTP",
			"参数": {
				"FTP名称": "auto_ftp2"
			}
		}
		checks = """
		CheckMsg|连接成功
		"""
		log.info('>>>>> 测试ftp配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_DeleteFTP(self):
		u"""删除ftp配置"""
		action = {
			"操作": "DeleteFTP",
			"参数": {
				"FTP名称": "auto_ftp2"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_ftp_config|1|ftp_name|auto_ftp2|is_delete_tag|1
		"""
		log.info('>>>>> 删除ftp配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddFTP(self):
		u"""添加ftp配置，配置正确"""
		action = {
			"操作": "AddFTP",
			"参数": {
				"FTP名称": "auto_ftp",
				"连接地址": "192.168.88.132",
				"端口": "21",
				"用户名": "viper.catalog",
				"密码": "viper.catalog_pass"
			}
		}
		checks = """
		CheckData|${Database}.alarm.alarm_ftp_config|1|ftp_name|auto_ftp|ftp_hostname|192.168.88.132|ftp_port|21|ftp_username|viper.catalog|ftp_password|notnull|creator|${LoginUser}|updater|${LoginUser}|create_date|now|update_date|now|is_delete_tag|0
		"""
		log.info('>>>>> 添加ftp配置，配置正确 <<<<<')
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
