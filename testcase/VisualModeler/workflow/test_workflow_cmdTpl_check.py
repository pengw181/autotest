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


class WorkFlowCmdTplNodeCheck(unittest.TestCase):

	log.info("装载流程指令模版系统检查测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试指令模版节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_指令模版系统检查说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_NodeBusinessConf(self):
		u"""配置指令模版节点，磁盘利用率检查"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "磁盘利用率检查",
					"指令任务模版": "auto_指令模版_磁盘利用率检查",
					"应用指令模版名称": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点，磁盘利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeBusinessConf(self):
		u"""配置指令模版节点，查看Slab"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "查看Slab",
					"指令任务模版": "auto_指令模版_查看Slab",
					"应用指令模版名称": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点，查看Slab <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置指令模版节点，内存利用率检查"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "内存利用率检查",
					"指令任务模版": "auto_指令模版_内存利用率检查",
					"应用指令模版名称": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点，内存利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置指令模版节点，服务器性能检测Top"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "服务器性能检测Top",
					"指令任务模版": "auto_指令模版_服务器性能检测Top",
					"应用指令模版名称": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点，服务器性能检测Top <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeBusinessConf(self):
		u"""配置指令模版节点，服务器负载检查"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "服务器负载检查",
					"指令任务模版": "auto_指令模版_服务器负载检查",
					"应用指令模版名称": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点，服务器负载检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeFetchConf(self):
		u"""节点添加取数配置，磁盘利用率检查结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "磁盘利用率检查",
				"取数配置": {
					"操作": "添加",
					"变量名称": "磁盘利用率检查结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，磁盘利用率检查结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeFetchConf(self):
		u"""节点添加取数配置，查看Slab结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "查看Slab",
				"取数配置": {
					"操作": "添加",
					"变量名称": "查看Slab结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，查看Slab结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeFetchConf(self):
		u"""节点添加取数配置，内存利用率检查"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "内存利用率检查",
				"取数配置": {
					"操作": "添加",
					"变量名称": "内存利用率检查结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，内存利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NodeFetchConf(self):
		u"""节点添加取数配置，服务器性能检测Top结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "服务器性能检测Top",
				"取数配置": {
					"操作": "添加",
					"变量名称": "服务器性能检测Top结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，服务器性能检测Top结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeFetchConf(self):
		u"""节点添加取数配置，服务器负载检查结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "指令模版节点",
				"节点名称": "服务器负载检查",
				"取数配置": {
					"操作": "添加",
					"变量名称": "服务器负载检查结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，服务器负载检查结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_LineNode(self):
		u"""开始节点连线到节点：磁盘利用率检查"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "开始",
				"终止节点名称": "磁盘利用率检查",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点：磁盘利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_LineNode(self):
		u"""节点磁盘利用率检查连线到节点：查看Slab"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "磁盘利用率检查",
				"终止节点名称": "查看Slab",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点磁盘利用率检查连线到节点：查看Slab <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_LineNode(self):
		u"""节点查看Slab连线到节点：内存利用率检查"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "查看Slab",
				"终止节点名称": "内存利用率检查",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点查看Slab连线到节点：内存利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_LineNode(self):
		u"""节点内存利用率检查连线到节点：服务器性能检测Top"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "内存利用率检查",
				"终止节点名称": "服务器性能检测Top",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点内存利用率检查连线到节点：服务器性能检测Top <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_LineNode(self):
		u"""节点服务器性能检测Top连线到节点：服务器负载检查"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "服务器性能检测Top",
				"终止节点名称": "服务器负载检查",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点服务器性能检测Top连线到节点：服务器负载检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"节点类型": "结束节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"状态": "正常"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置结束节点状态为正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""节点服务器负载检查连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查",
				"起始节点名称": "服务器负载检查",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点服务器负载检查连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_指令模版系统检查"
			}
		}
		checks = """
		CheckMsg|调用测试流程成功,请到流程运行日志中查看
		"""
		log.info('>>>>> 流程列表，测试流程 <<<<<')
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
