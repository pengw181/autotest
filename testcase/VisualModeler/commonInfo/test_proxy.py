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


class Proxy(unittest.TestCase):

	log.info("装载代理管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProxyDataClear(self):
		u"""代理管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_proxy_cfg where proxy_name like 'auto_%'
		"""
		action = {
			"操作": "ProxyDataClear",
			"参数": {
				"代理名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 代理管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddProxy(self):
		u"""添加代理"""
		action = {
			"操作": "AddProxy",
			"参数": {
				"代理名称": "auto_代理",
				"代理服务器": "192.168.88.1",
				"代理端口": "8080",
				"代理用户名": "proxy",
				"代理密码": "proxy_pass",
				"代理协议": "socks",
				"是否有效": "有效",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_proxy_cfg|1|proxy_name|auto_代理|proxy_ip|192.168.88.1|proxy_port|8080|proxy_user|proxy|proxy_pwd|notnull|proxy_type|socks|is_alive|1|data_type_id|1|user_id|${LoginUser}|create_time|now|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_UpdateProxy(self):
		u"""修改代理"""
		action = {
			"操作": "UpdateProxy",
			"参数": {
				"代理名称": "auto_代理",
				"修改内容": {
					"代理名称": "auto_代理1",
					"代理服务器": "192.168.88.2",
					"代理端口": "8081",
					"代理用户名": "proxy1",
					"代理密码": "proxy_pass1",
					"代理协议": "http",
					"是否有效": "无效",
					"数据类型": "私有"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_proxy_cfg|1|proxy_name|auto_代理1|proxy_ip|192.168.88.2|proxy_port|8081|proxy_user|proxy1|proxy_pwd|notnull|proxy_type|http|is_alive|0|data_type_id|0|user_id|${LoginUser}|create_time|notnull|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}
		"""
		log.info('>>>>> 修改代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_DeleteProxy(self):
		u"""删除代理"""
		action = {
			"操作": "DeleteProxy",
			"参数": {
				"代理名称": "auto_代理1"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_proxy_cfg|0|proxy_name|auto_代理1
		"""
		log.info('>>>>> 删除代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddProxy(self):
		u"""添加代理"""
		action = {
			"操作": "AddProxy",
			"参数": {
				"代理名称": "auto_代理",
				"代理服务器": "192.168.88.1",
				"代理端口": "8080",
				"代理用户名": "proxy",
				"代理密码": "proxy_pass",
				"代理协议": "socks",
				"是否有效": "有效",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_proxy_cfg|1|proxy_name|auto_代理|proxy_ip|192.168.88.1|proxy_port|8080|proxy_user|proxy|proxy_pwd|notnull|proxy_type|socks|is_alive|1|data_type_id|0|user_id|${LoginUser}|create_time|now|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_ListProxy(self):
		u"""查询代理配置，按代理名称查询"""
		action = {
			"操作": "ListProxy",
			"参数": {
				"查询条件": {
					"代理名称": "auto"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询代理配置，按代理名称查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_ListProxy(self):
		u"""查询代理配置，按代理服务器/端口查询，ip"""
		action = {
			"操作": "ListProxy",
			"参数": {
				"查询条件": {
					"代理服务器/端口": "192.168.88"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询代理配置，按代理服务器/端口查询，ip <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_ListProxy(self):
		u"""查询代理配置，按代理服务器/端口查询，端口"""
		action = {
			"操作": "ListProxy",
			"参数": {
				"查询条件": {
					"代理服务器/端口": "8080"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询代理配置，按代理服务器/端口查询，端口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_ListProxy(self):
		u"""查询代理配置，按有效状态查询，有效"""
		action = {
			"操作": "ListProxy",
			"参数": {
				"查询条件": {
					"是否有效": "是"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询代理配置，按有效状态查询，有效 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_ListProxy(self):
		u"""查询代理配置，按有效状态查询，无效"""
		action = {
			"操作": "ListProxy",
			"参数": {
				"查询条件": {
					"是否有效": "否"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 查询代理配置，按有效状态查询，无效 <<<<<')
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
