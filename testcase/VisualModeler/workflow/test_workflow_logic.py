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


class WorkFlowNodeLogic(unittest.TestCase):

	log.info("装载流程逻辑分支功能测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_逻辑分支"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_逻辑分支说明",
				"高级配置": {
					"节点异常终止流程": "是",
					"自定义流程变量": {
						"状态": "开启",
						"参数列表": {
							"测试变量": "1###"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"左边距": 560,
				"上边距": 102
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_NodeBusinessConf(self):
		u"""配置通用节点，第一个逻辑"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "第一个逻辑",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，第一个逻辑 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"左边距": 560,
				"上边距": 290
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeBusinessConf(self):
		u"""配置通用节点，第二个逻辑"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "第二个逻辑",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，第二个逻辑 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "文件节点",
				"左边距": 300,
				"上边距": 290
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，找不到文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "节点业务执行异常",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "9999",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"sheet页索引": "",
							"变量": "文件加载",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，找不到文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"左边距": 560,
				"上边距": 460
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置通用节点，节点后无结束节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "节点后无结束节点",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，节点后无结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeControlConf(self):
		u"""配置通用节点，第一个逻辑，开启逻辑分支控制，固定值分支"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "第一个逻辑",
				"控制配置": {
					"逻辑分支控制": {
						"状态": "开启",
						"逻辑分支类型": "固定值分支",
						"满足条件": [
							[
								"变量",
								"测试变量"
							],
							[
								"等于",
								""
							],
							[
								"自定义值",
								"1"
							]
						],
						"不满足条件": [
							[
								"变量",
								"测试变量"
							],
							[
								"等于",
								""
							],
							[
								"自定义值",
								"2"
							]
						],
						"不确定条件": [
							[
								"变量",
								"测试变量"
							],
							[
								"等于",
								""
							],
							[
								"自定义值",
								"3"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，第一个逻辑，开启逻辑分支控制，固定值分支 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeControlConf(self):
		u"""配置通用节点，第二个逻辑，开启逻辑分支控制，动态值分支"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "第二个逻辑",
				"控制配置": {
					"逻辑分支控制": {
						"状态": "开启",
						"逻辑分支类型": "动态值分支",
						"动态值": [
							[
								"变量",
								"测试变量"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，第二个逻辑，开启逻辑分支控制，动态值分支 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeOptConf(self):
		u"""操作配置，添加操作，动作，休眠"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "通用节点",
				"节点名称": "节点后无结束节点",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "动作",
							"配置": {
								"表达式": [
									[
										"休眠",
										"3"
									]
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，动作，休眠 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "结束节点",
				"左边距": 960,
				"上边距": 130
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

	def test_15_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
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

	def test_16_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "结束节点",
				"左边距": 960,
				"上边距": 190
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

	def test_17_SetEndNode(self):
		u"""设置结束节点状态为异常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"状态": "异常"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置结束节点状态为异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "结束节点",
				"左边距": 960,
				"上边距": 240
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

	def test_19_SetEndNode(self):
		u"""设置结束节点状态为未知"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"状态": "未知"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置结束节点状态为未知 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"节点类型": "结束节点",
				"左边距": 960,
				"上边距": 310
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

	def test_21_SetEndNode(self):
		u"""设置结束节点状态为自定义值：其它"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"状态": "其它"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置结束节点状态为自定义值：其它 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_LineNode(self):
		u"""开始节点文件加载开启过滤连线到节点：第一个逻辑"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "开始",
				"终止节点名称": "第一个逻辑",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点文件加载开启过滤连线到节点：第一个逻辑 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_LineNode(self):
		u"""节点第一个逻辑连线到结束节点：正常，满足条件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第一个逻辑",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第一个逻辑连线到结束节点：正常，满足条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_LineNode(self):
		u"""节点第一个逻辑连线到结束节点：异常，不满足条件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第一个逻辑",
				"终止节点名称": "异常",
				"关联关系": "不满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第一个逻辑连线到结束节点：异常，不满足条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""节点第一个逻辑连线到结束节点：未知，不确定条件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第一个逻辑",
				"终止节点名称": "未知",
				"关联关系": "不确定"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第一个逻辑连线到结束节点：未知，不确定条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_LineNode(self):
		u"""节点第一个逻辑连线到节点：第二个逻辑，default"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第一个逻辑",
				"终止节点名称": "第二个逻辑",
				"关联关系": "default"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第一个逻辑连线到节点：第二个逻辑，default <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_LineNode(self):
		u"""节点第二个逻辑连线到节点：节点业务执行异常，动态逻辑值：4"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第二个逻辑",
				"终止节点名称": "节点业务执行异常",
				"关联关系": "4"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第二个逻辑连线到节点：节点业务执行异常，动态逻辑值：4 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_LineNode(self):
		u"""节点第二个逻辑连线到节点：节点业务执行异常，动态逻辑值：5"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第二个逻辑",
				"终止节点名称": "其它",
				"关联关系": "5"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第二个逻辑连线到节点：节点业务执行异常，动态逻辑值：5 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_LineNode(self):
		u"""节点第二个逻辑连线到节点：节点后无结束节点，动态逻辑值：6"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"起始节点名称": "第二个逻辑",
				"终止节点名称": "节点后无结束节点",
				"关联关系": "6"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点第二个逻辑连线到节点：节点后无结束节点，动态逻辑值：6 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_FastRunProcess(self):
		u"""流程列表，一键启动流程，使用默认参数启动"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支"
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，使用默认参数启动 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：1"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "1"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：2"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "2"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：3"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "3"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：3 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：4"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "4"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：4 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：5"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "5"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：5 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_FastRunProcess(self):
		u"""流程列表，一键启动流程，传参数启动，变量值：6"""
		action = {
			"操作": "FastRunProcess",
			"参数": {
				"流程名称": "auto_流程_逻辑分支",
				"参数列表": {
					"测试变量": "6"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 流程列表，一键启动流程，传参数启动，变量值：6 <<<<<')
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
