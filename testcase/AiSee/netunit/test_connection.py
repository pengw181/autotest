# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:07

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class ConnectTest(unittest.TestCase):

	log.info("装载网元连通性测试测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_TestSelectedNetunit(self):
		u"""连通性测试，网元名称：auto_manual，登录模式：普通模式"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_manual",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					{
						"网元名称": "auto_manual",
						"登录模式": "普通模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，网元名称：auto_manual，登录模式：普通模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_GetConnectReport(self):
		u"""休眠30秒后，获取测试结果汇总"""
		pres = """
		wait|30
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：1条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 休眠30秒后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_TestSelectedNetunit(self):
		u"""连通性测试，网元名称：auto_manual，登录模式：异常模式"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_manual",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					{
						"网元名称": "auto_manual",
						"登录模式": "异常模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，网元名称：auto_manual，登录模式：异常模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_GetConnectReport(self):
		u"""休眠后，获取测试结果汇总"""
		pres = """
		wait|90
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：0条，异常：1条，测试中：0条
		"""
		log.info('>>>>> 休眠后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestSelectedNetunit(self):
		u"""连通性测试，网元名称：auto_manual，登录模式：SSH模式"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_manual",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					{
						"网元名称": "auto_manual",
						"登录模式": "SSH模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，网元名称：auto_manual，登录模式：SSH模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_GetConnectReport(self):
		u"""休眠30秒后，获取测试结果汇总"""
		pres = """
		wait|30
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：1条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 休眠30秒后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_TestSelectedNetunit(self):
		u"""连通性测试，网元名称：auto_manual，登录模式：TELNET模式"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_manual",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					{
						"网元名称": "auto_manual",
						"登录模式": "TELNET模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，网元名称：auto_manual，登录模式：TELNET模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_GetConnectReport(self):
		u"""休眠30秒后，获取测试结果汇总"""
		pres = """
		wait|30
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：1条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 休眠30秒后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_TestAllNetunit(self):
		u"""连通性测试，测试全部"""
		action = {
			"操作": "TestAllNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				}
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，测试全部 <<<<<')
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
