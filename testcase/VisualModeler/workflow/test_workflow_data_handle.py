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


class WorkFlowHandleNode(unittest.TestCase):

	log.info("装载流程数据比对更新测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_数据处理"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试数据处理节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_数据处理说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试数据处理节点 <<<<<')
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
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点"
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
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "参数设置",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，变量a"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"自定义值",
										[
											"java,v1,100",
											"python,v1,200",
											"jar,v1,150"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量a"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个自定义变量，变量a <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""操作配置，添加操作，正则运算，得到二维数组"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "变量a",
								"输出变量": "变量a",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "3",
									"拆分方式": "文本",
									"拆分符": ",",
									"样例数据": [
										"java,v1,100",
										"python,v1,200",
										"jar,v1,150"
									]
								}
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，正则运算，得到二维数组 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，变量b"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"自定义值",
										[
											"java,v1,100,a1",
											"python,v1,200,a2",
											"jar,v1,150,a3",
											"c,v1,150,a4"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量b"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个自定义变量，变量b <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeOptConf(self):
		u"""操作配置，添加操作，正则运算，得到二维数组"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "变量b",
								"输出变量": "变量b",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "4",
									"拆分方式": "文本",
									"拆分符": ",",
									"样例数据": [
										"java,v1,100,a1",
										"python,v1,200,a2",
										"jar,v1,150,a3",
										"c,v1,150,a4"
									]
								}
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，正则运算，得到二维数组 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeOptConf(self):
		u"""通用节点，添加一个一维数组，变量c"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"自定义值",
										"java"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"python"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量c"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个一维数组，变量c <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置数据处理节点，数据比对模式，取关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据比对取关联结果",
					"处理模式": "数据比对",
					"变量1": "变量a",
					"变量2": "变量b",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量1",
					"输出类型": "关联结果",
					"输出变量名称": "关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据处理节点，数据比对模式，取关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置数据处理节点，数据比对模式，取未关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据比对取非关联结果",
					"处理模式": "数据比对",
					"变量1": "变量a",
					"变量2": "变量b",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量2",
					"输出类型": "未关联结果",
					"输出变量名称": "未关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据处理节点，数据比对模式，取未关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置数据处理节点，数据比对模式，二维表与一维表比对，取关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "二维表与一维表比对",
					"处理模式": "数据比对",
					"变量1": "变量a",
					"变量2": "变量c",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量1",
					"输出类型": "关联结果",
					"输出变量名称": "二维表与一维表比对关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据处理节点，数据比对模式，二维表与一维表比对，取关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置数据处理节点，数据更新模式，更新已存在列"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "更新已存在列",
					"处理模式": "数据更新",
					"变量1": "变量a",
					"变量2": "变量b",
					"关联列": [
						[
							"1",
							"1"
						],
						[
							"2",
							"2"
						]
					],
					"更新列": [
						[
							"3",
							"4"
						]
					],
					"基准变量": "变量1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据处理节点，数据更新模式，更新已存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图，添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置数据处理节点，数据更新模式，更新不存在列"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "更新不存在列",
					"处理模式": "数据更新",
					"变量1": "变量a",
					"变量2": "变量b",
					"关联列": [
						[
							"1",
							"1"
						],
						[
							"2",
							"2"
						]
					],
					"更新列": [
						[
							"4",
							"4"
						],
						[
							"6",
							"3"
						]
					],
					"基准变量": "变量1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据处理节点，数据更新模式，更新不存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点：参数设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_LineNode(self):
		u"""节点参数设置连线到节点：数据比对取关联结果"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "参数设置",
				"终止节点名称": "数据比对取关联结果",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：数据比对取关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_LineNode(self):
		u"""节点数据比对取关联结果连线到节点：数据比对取非关联结果"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "数据比对取关联结果",
				"终止节点名称": "数据比对取非关联结果",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点数据比对取关联结果连线到节点：数据比对取非关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_LineNode(self):
		u"""节点数据比对取非关联结果连线到节点：二维表与一维表比对"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "数据比对取非关联结果",
				"终止节点名称": "二维表与一维表比对",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点数据比对取非关联结果连线到节点：二维表与一维表比对 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_LineNode(self):
		u"""节点二维表与一维表比对连线到节点：更新已存在列"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "二维表与一维表比对",
				"终止节点名称": "更新已存在列",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点二维表与一维表比对连线到节点：更新已存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""节点更新已存在列连线到节点：更新不存在列"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "更新已存在列",
				"终止节点名称": "更新不存在列",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点更新已存在列连线到节点：更新不存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
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

	def test_27_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
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

	def test_28_LineNode(self):
		u"""节点更新不存在列连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据处理",
				"起始节点名称": "更新不存在列",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点更新不存在列连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_数据处理"
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
