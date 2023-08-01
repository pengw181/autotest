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


class DataClearWorker(unittest.TestCase):

	log.info("装载数据清理测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/测试准备/数据清理.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AlarmPlanDataClear(self):
		u"""删除告警计划，联并删除绑定的告警规则、消息模版、推送计划（逻辑删除，is_delete_tag=1）"""
		action = {
			"操作": "AlarmPlanDataClear",
			"参数": {
				"告警计划名称": "auto_告警计划",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 删除告警计划，联并删除绑定的告警规则、消息模版、推送计划（逻辑删除，is_delete_tag=1） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_MetaDataDataClear(self):
		u"""删除告警元数据"""
		action = {
			"操作": "MetaDataDataClear",
			"参数": {
				"元数据名称": "auto_元数据",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 删除告警元数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_3_TableBelongDataClear(self):
		u"""删除表归属配置"""
		action = {
			"操作": "TableBelongDataClear",
			"参数": {
				"表中文名称": "auto_表归属",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 删除表归属配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
