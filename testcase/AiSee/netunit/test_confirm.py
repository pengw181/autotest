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


class LoginConfirm(unittest.TestCase):

	log.info("装载登录配置确认测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					"auto_TURK_TKea1",
					"auto_TURK_TKea2",
					"auto_TURK_TKea3"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_ConfirmAll(self):
		u"""登录配置确认，确认全部"""
		action = {
			"操作": "ConfirmAll",
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
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认全部 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_CancelSelected(self):
		u"""登录配置确认，取消配置下发"""
		action = {
			"操作": "CancelSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					"auto_TURK_TKea1",
					"auto_TURK_TKea2",
					"auto_TURK_TKea3"
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 登录配置确认，取消配置下发 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_ConfirmAll(self):
		u"""登录配置确认，无登录配置信息需要确认，确认全部"""
		action = {
			"操作": "ConfirmAll",
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
		CheckMsg|无登录配置确认信息
		"""
		log.info('>>>>> 登录配置确认，无登录配置信息需要确认，确认全部 <<<<<')
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
