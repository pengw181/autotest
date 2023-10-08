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


class ConnectTestReport(unittest.TestCase):

	log.info("装载连通测试报告测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_GetConnectReport(self):
		u"""连通测试报告，获取测试结果汇总"""
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
		CheckMsg|正常：3条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 连通测试报告，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_GetConnectDetailLog(self):
		u"""连通测试报告，查看登录日志详情"""
		action = {
			"操作": "GetConnectDetailLog",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				},
				"网元名称": "auto_TURK_TKea1"
			}
		}
		log.info('>>>>> 连通测试报告，查看登录日志详情 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_3_ConnectRetest(self):
		u"""连通测试报告，重新测试"""
		action = {
			"操作": "ConnectRetest",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|请5分钟后重试
		"""
		log.info('>>>>> 连通测试报告，重新测试 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_ConnectRetest(self):
		u"""连通测试报告，休眠后重新测试"""
		pres = """
		wait|300
		"""
		action = {
			"操作": "ConnectRetest",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通测试报告，休眠后重新测试 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_ConnectDetailRetest(self):
		u"""连通测试报告，登录详情页重新测试"""
		action = {
			"操作": "ConnectDetailRetest",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				},
				"网元名称": "auto_TURK_TKea1"
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通测试报告，登录详情页重新测试 <<<<<')
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
