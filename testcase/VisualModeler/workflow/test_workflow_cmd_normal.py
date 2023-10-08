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


class WorkFlowCmdNodeNormal(unittest.TestCase):

	log.info("装载流程指令通用功能测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_指令通用功能"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试指令节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_指令通用功能流程说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试指令节点 <<<<<')
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
				"流程名称": "auto_流程_指令通用功能",
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
				"流程名称": "auto_流程_指令通用功能",
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
		u"""通用节点，添加变量网元列表"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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
										"${NetunitMME1}"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"${NetunitMME2}"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"${NetunitMME3}"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "网元列表"
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
		log.info('>>>>> 通用节点，添加变量网元列表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""通用节点，添加变量指令参数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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
											"${NetunitMME1},www.baidu.com,3",
											"${NetunitMME1},www.sina.com,2",
											"${NetunitMME2},www.baidu.com,5",
											"${NetunitMME3},www.sina.com,6"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "指令参数"
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
		log.info('>>>>> 通用节点，添加变量指令参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点，拆分指令参数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "指令参数",
								"输出变量": "指令参数",
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
										"${NetunitMME1},www.baidu.com,3",
										"${NetunitMME1},www.sina.com,2",
										"${NetunitMME2},www.baidu.com,5",
										"${NetunitMME3},www.sina.com,6"
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
		log.info('>>>>> 通用节点，拆分指令参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeOptConf(self):
		u"""通用节点，添加变量ip列表"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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
										"www.baidu.com"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"www.sina.com"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"www.huya.com"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"www.douyu.com"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "ip列表"
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
		log.info('>>>>> 通用节点，添加变量ip列表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeOptConf(self):
		u"""通用节点，添加变量packages个数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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
										"1"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"2"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"3"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"4"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "packages个数"
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
		log.info('>>>>> 通用节点，添加变量packages个数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置指令节点，指令不带参数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令不带参数",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_date": {
								"解析模版": "auto_解析模板_解析date"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点，指令不带参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置指令节点，指令带参数，独立模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令带参数，独立模式",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_多参数": {
								"解析模版": "auto_解析模板_解析ping",
								"参数设置": {
									"模式": "独立模式",
									"参数": "ip列表,packages个数"
								}
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点，指令带参数，独立模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置指令节点，指令带参数，二维表模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令带参数，二维表模式",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_多参数": {
								"解析模版": "auto_解析模板_解析ping",
								"参数设置": {
									"模式": "二维表模式",
									"参数": {
										"选择变量": "指令参数",
										"对象设置": "[1]",
										"参数1": "[2],ip",
										"参数2": "[3],packages"
									}
								}
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点，指令带参数，二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置指令节点，组合指令"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令节点，组合指令",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_组合指令": {
								"解析模版": "auto_解析模板_解析date"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点，组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置指令节点，多指令"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令节点多指令",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_date": {
								"解析模版": "auto_解析模板_解析date"
							},
							"auto_指令_ping": {
								"解析模版": "auto_二维表结果判断，添加变量配置"
							},
							"auto_指令_ping_日志清洗": {
								"解析模版": "auto_解析模板_日志清洗"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点，多指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeFetchConf(self):
		u"""节点添加取数配置，成员解析结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "成员解析结果",
					"对象类型": "成员",
					"结果类型": "解析结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，成员解析结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeFetchConf(self):
		u"""节点添加取数配置，网元原始结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元原始结果",
					"对象类型": "网元",
					"结果类型": "原始结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元原始结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeFetchConf(self):
		u"""节点添加取数配置，网元解析结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元解析结果",
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
		log.info('>>>>> 节点添加取数配置，网元解析结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeFetchConf(self):
		u"""节点添加取数配置，网元清洗结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元清洗结果",
					"对象类型": "网元",
					"结果类型": "清洗结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元清洗结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeFetchConf(self):
		u"""节点添加取数配置，网元格式化二维表结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元格式化二维表结果",
					"对象类型": "网元",
					"结果类型": "格式化二维表结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元格式化二维表结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeFetchConf(self):
		u"""节点添加取数配置，网元异常结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元异常结果",
					"对象类型": "网元",
					"结果类型": "异常结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元异常结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeFetchConf(self):
		u"""节点添加取数配置，网元所有结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元所有结果",
					"对象类型": "网元",
					"结果类型": "所有结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元所有结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeFetchConf(self):
		u"""节点添加取数配置，网元解析模版变量值"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"节点类型": "指令节点",
				"节点名称": "指令节点多指令",
				"取数配置": {
					"操作": "添加",
					"变量名称": "网元解析模版变量值",
					"对象类型": "网元",
					"结果类型": "解析模版变量值",
					"变量名": "全部变量",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，网元解析模版变量值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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

	def test_29_LineNode(self):
		u"""节点参数设置连线到节点：指令不带参数"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "参数设置",
				"终止节点名称": "指令不带参数",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：指令不带参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_LineNode(self):
		u"""节点指令不带参数连线到节点：指令带参数，独立模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "指令不带参数",
				"终止节点名称": "指令带参数，独立模式",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点指令不带参数连线到节点：指令带参数，独立模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_LineNode(self):
		u"""节点指令带参数，独立模式连线到节点：指令带参数，二维表模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "指令带参数，独立模式",
				"终止节点名称": "指令带参数，二维表模式",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点指令带参数，独立模式连线到节点：指令带参数，二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_LineNode(self):
		u"""节点指令带参数，二维表模式连线到节点：指令节点，组合指令"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "指令带参数，二维表模式",
				"终止节点名称": "指令节点，组合指令",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点指令带参数，二维表模式连线到节点：指令节点，组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_LineNode(self):
		u"""节点指令节点，组合指令连线到节点：指令节点多指令"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "指令节点，组合指令",
				"终止节点名称": "指令节点多指令",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点指令节点，组合指令连线到节点：指令节点多指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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

	def test_35_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
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

	def test_36_LineNode(self):
		u"""节点指令节点多指令连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_指令通用功能",
				"起始节点名称": "指令节点多指令",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点指令节点多指令连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_指令通用功能"
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
