# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:09

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class CopyProcess(unittest.TestCase):

	log.info("装载流程复制测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_copy_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_CopyProcess(self):
		u"""复制流程，复制主流程，主流程含子流程"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_多级流程",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_多级流程",
				"子流程名称列表": [
					[
						"auto_一级子流程",
						"auto_copy_一级子流程"
					],
					[
						"auto_二级子流程",
						"auto_copy_二级子流程"
					],
					[
						"auto_二级子流程2",
						"auto_copy_二级子流程2"
					],
					[
						"auto_三级子流程",
						"auto_copy_三级子流程"
					]
				]
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程，主流程含子流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_DeleteProcess(self):
		u"""删除流程"""
		action = {
			"操作": "DeleteProcess",
			"参数": {
				"流程名称": "auto_copy_多级流程"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_CopyProcess(self):
		u"""复制流程，复制子流程，子流程含子流程"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_一级子流程",
				"流程类型": "子流程",
				"主流程名称": "auto_copy_一级子流程",
				"子流程名称列表": [
					[
						"auto_二级子流程",
						"auto_copy_二级子流程"
					],
					[
						"auto_二级子流程2",
						"auto_copy_二级子流程2"
					],
					[
						"auto_三级子流程",
						"auto_copy_三级子流程"
					]
				]
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制子流程，子流程含子流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_DeleteProcess(self):
		u"""删除流程"""
		action = {
			"操作": "DeleteProcess",
			"参数": {
				"流程名称": "auto_copy_一级子流程",
				"流程类型": "子流程"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_copy_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_7_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_指令通用功能"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_指令通用功能"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_指令通用功能 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_测试指令输入输出参数"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_测试指令输入输出参数",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_测试指令输入输出参数"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_测试指令输入输出参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_指令按网元类型"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_指令按网元类型",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_指令按网元类型"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_指令按网元类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_指令系统检查"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_指令系统检查",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_指令系统检查"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_指令系统检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_指令模版系统检查"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_指令模版系统检查"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_指令模版系统检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_指令模版通用功能"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_指令模版通用功能",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_指令模版通用功能"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_指令模版通用功能 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_爬虫表格取数"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_爬虫表格取数",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_爬虫表格取数"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_爬虫表格取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_爬虫文件下载"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_爬虫文件下载",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_爬虫文件下载"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_爬虫文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_爬虫文件上传"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_爬虫文件上传",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_爬虫文件上传"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_爬虫文件上传 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_数据处理"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_数据处理"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_数据处理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_邮件接收"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_邮件接收",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_邮件接收"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_邮件接收 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_邮件发送"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_邮件发送"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_邮件发送 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_文件存储"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_文件存储",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_文件存储"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_文件存储 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_文件拷贝移动"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_文件拷贝移动"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_文件拷贝移动 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_文件加载"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_文件加载"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_文件加载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_信息展示"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_信息展示",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_信息展示"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_信息展示 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_信息推送告警"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_信息推送告警",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_信息推送告警"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_信息推送告警 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_webservice接口"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_webservice接口",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_webservice接口"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_webservice接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_soap接口"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_soap接口",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_soap接口"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_soap接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_restful接口"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_restful接口"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_restful接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_报表链接模式"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_报表链接模式",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_报表链接模式"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_报表链接模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_报表仪表盘模式"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_报表仪表盘模式",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_报表仪表盘模式"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_报表仪表盘模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_AI预测"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_AI预测"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_AI预测 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_OCR识别"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_OCR识别",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_OCR识别"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_OCR识别 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_逻辑分支"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_逻辑分支"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_逻辑分支 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_运算操作"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_运算操作"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_运算操作 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_函数计算"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_函数计算",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_函数计算"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_函数计算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_数据库节点SQL模式"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_数据库节点SQL模式"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_数据库节点SQL模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_数据库配置模式"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_数据库配置模式"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_数据库配置模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_数据库节点权限"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_数据库节点权限",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_数据库节点权限"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_数据库节点权限 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_OuShu数据库"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_OuShu数据库",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_OuShu数据库"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_OuShu数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_CopyProcess(self):
		u"""复制流程，复制主流程：auto_流程_脚本调用"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_流程_脚本调用",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_流程_脚本调用"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_流程_脚本调用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_CopyProcess(self):
		u"""复制流程，复制主流程：auto_配置流程"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_配置流程",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_配置流程"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_配置流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_CopyProcess(self):
		u"""复制流程，复制主流程：auto_全流程"""
		action = {
			"操作": "CopyProcess",
			"参数": {
				"流程名称": "auto_全流程",
				"流程类型": "主流程",
				"主流程名称": "auto_copy_全流程"
			}
		}
		checks = """
		CheckMsg|复制流程成功
		"""
		log.info('>>>>> 复制流程，复制主流程：auto_全流程 <<<<<')
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
