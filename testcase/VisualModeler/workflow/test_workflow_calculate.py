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


class WorkFlowCommonNodeCalculate(unittest.TestCase):

	log.info("装载流程运算功能测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_运算操作"
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
				"流程名称": "auto_流程_运算操作",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_运算操作说明"
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
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
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
				"流程名称": "auto_流程_运算操作",
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
		u"""操作配置，添加变量：表格数据"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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
											"a1,1,15,100",
											"a2,2,11,600",
											"b1,3,20,1000",
											"c1,4,19,150",
											"c1,6,29,1500"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "原始数据"
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
		log.info('>>>>> 操作配置，添加变量：表格数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""操作配置，添加变量：文本数据"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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
											"2022-03-10 11:23:42,549 - elastalert.py:1230:INFO - hhelastalert0 - -----------------		本周期实例开始		-----------------",
											"2022-03-10 11:23:42,552 - elastalert.py:1858:DEBUG - hhelastalert0 - 执行查询语句：{'sort': {'alert_time': {'order': 'asc'}}, 'query': {'bool': {'filter': {'range': {'alert_time': {'to': '2022-03-10T03:23:42.552493Z', 'from': '2022-03-08T03:23:42.552361Z'}}}, 'must': {'query_string': {'query': '!_exists_:aggregate_id AND alert_sent:false'}}}}}",
											"2022-03-10 11:23:42,595 - databases.py:94 - databases - Modified 0 lines.",
											"2022-03-10 11:23:42,596 - databases.py:95 - databases - Finished Running SQLs.",
											"2022-03-10 11:23:42,600 - elastalert.py:1232:INFO - hhelastalert0 - ---------  本周期实例执行完成，休眠等待下一个运行周期  ---------"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "文本数据"
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
		log.info('>>>>> 操作配置，添加变量：文本数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""操作配置，添加变量：日志类别"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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
											"hhelastalert0"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "日志类别"
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
		log.info('>>>>> 操作配置，添加变量：日志类别 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "文件节点"
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

	def test_9_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载函数测试数据：清洗日志"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载测试数据",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "清洗日志",
							"文件类型": "txt",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"分隔符": "",
							"变量": "清洗日志",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载函数测试数据：清洗日志 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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

	def test_11_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "运算",
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

	def test_12_NodeOptConf(self):
		u"""操作配置，添加操作，正则运算，正则拆分"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "原始数据",
								"输出变量": "表格数据",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "4",
									"拆分方式": "正则",
									"正则配置": {
										"设置方式": "选择",
										"正则模版名称": "auto_正则模版_匹配逗号"
									},
									"样例数据": [
										"a1,1,2,3",
										"a2,1,2,3",
										"a3,1,2,3",
										"a4,1,2,3",
										"a5,1,2,3"
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
		log.info('>>>>> 操作配置，添加操作，正则运算，正则拆分 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeOptConf(self):
		u"""操作配置，添加操作，正则运算，正则匹配数据列"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "文本数据",
								"输出变量": "正则运算结果-正则匹配数据列",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "是",
									"正则配置": {
										"设置方式": "选择",
										"正则模版名称": "auto_正则模版_匹配清洗日志"
									},
									"样例数据": [
										"2022-03-10 11:23:42,595 - databases.py:94 - databases - Modified 1 lines",
										"2022-03-10 11:23:57,589 - elastalert.py:924:DEBUG - hhelastalert0 - 开始时间传参：None"
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
		log.info('>>>>> 操作配置，添加操作，正则运算，正则匹配数据列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeOptConf(self):
		u"""操作配置，添加操作，过滤运算"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "过滤运算",
							"配置": {
								"选择变量": "表格数据",
								"过滤条件": [
									[
										"变量索引",
										"4"
									],
									[
										"大于",
										""
									],
									[
										"自定义值",
										"500"
									],
									[
										"与",
										""
									],
									[
										"变量索引",
										"1"
									],
									[
										"开头",
										""
									],
									[
										"自定义值",
										[
											"a"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "过滤运算结果"
								},
								"输出列": "1,2,4,3",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，过滤运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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

	def test_16_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "聚合运算",
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

	def test_17_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，总计"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"总计(sum)",
										"4"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算总计结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，总计 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，计数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"计数(count)",
										"1"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算计数结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，计数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，最大值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"最大值(max)",
										"4"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算最大值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，最大值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，最小值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"最小值(min)",
										"3"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算最小值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，最小值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，平均值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"平均值(avg)",
										"3"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算平均值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，平均值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，分组连接"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "1",
								"表达式": [
									[
										"分组连接",
										"2,&"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算分组连接结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，分组连接 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeOptConf(self):
		u"""操作配置，添加操作，聚合运算，统计行数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"配置": {
								"选择变量": "表格数据",
								"分组依据": "0",
								"表达式": [
									[
										"计数(count)",
										"1"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算统计行数结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，聚合运算，统计行数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeOptConf(self):
		u"""操作配置，添加操作，网络地址运算，子网掩码方式"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "网络地址运算",
							"配置": {
								"输入方式": "子网掩码",
								"输入地址": "255.255.0.0",
								"TCP/IP地址": "192.168.88.123",
								"输出名称": {
									"类型": "输入",
									"变量名": "网络地址运算结果-子网掩码输入方式"
								},
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，网络地址运算，子网掩码方式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeOptConf(self):
		u"""操作配置，添加操作，网络地址运算，位元数方式"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "网络地址运算",
							"配置": {
								"输入方式": "位元数",
								"输入地址": "11",
								"输出名称": {
									"类型": "输入",
									"变量名": "网络地址运算结果-位元数方式"
								},
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，网络地址运算，位元数方式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeOptConf(self):
		u"""操作配置，添加操作，分段拆分运算，只配置开始特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"配置": {
								"变量名称": "分段拆分运算结果-开始特征行",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"开始特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_匹配日期"
								},
								"样例数据": [
									"2020-11-15 12:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤",
									"2020-11-15 13:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤"
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
		log.info('>>>>> 操作配置，添加操作，分段拆分运算，只配置开始特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeOptConf(self):
		u"""操作配置，添加操作，分段拆分运算，只配置结束特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"配置": {
								"变量名称": "分段拆分运算结果-结束特征行",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"结束特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_清洗结束符"
								},
								"样例数据": [
									"2022-03-10 11:23:42,549 - elastalert.py:1230:INFO - hhelastalert0 - -----------------		本周期实例开始		-----------------",
									"2022-03-10 11:23:42,598 - elastalert.py:1209:DEBUG - hhelastalert0 -	es告警规则-oracle-vm",
									"2022-03-10 11:23:42,600 - elastalert.py:1232:INFO - hhelastalert0 - ---------  本周期实例执行完成，休眠等待下一个运行周期  ---------",
									"2022-03-10 11:23:42,602 - elastalert.py:1483:INFO - hhelastalert0 - 休眠 14.946905 秒",
									"2022-03-10 11:23:57,554 - elastalert.py:1230:INFO - hhelastalert0 - -----------------		本周期实例开始		-----------------"
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
		log.info('>>>>> 操作配置，添加操作，分段拆分运算，只配置结束特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeOptConf(self):
		u"""操作配置，添加操作，分段拆分运算，同时配置开始特征行和结束特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"配置": {
								"变量名称": "分段拆分运算结果-开始结束特征行",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"开始特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_匹配日期"
								},
								"结束特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_清洗结束符"
								},
								"样例数据": [
									"2022-03-10 11:23:42,549 - elastalert.py:1230:INFO - hhelastalert0 - -----------------		本周期实例开始		-----------------",
									"2022-03-10 11:23:42,598 - elastalert.py:1209:DEBUG - hhelastalert0 -	es告警规则-oracle-vm",
									"2022-03-10 11:23:42,600 - elastalert.py:1232:INFO - hhelastalert0 - ---------  本周期实例执行完成，休眠等待下一个运行周期  ---------",
									"2022-03-10 11:23:42,602 - elastalert.py:1483:INFO - hhelastalert0 - 休眠 14.946905 秒",
									"2022-03-10 11:23:57,554 - elastalert.py:1230:INFO - hhelastalert0 - -----------------		本周期实例开始		-----------------"
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
		log.info('>>>>> 操作配置，添加操作，分段拆分运算，同时配置开始特征行和结束特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeOptConf(self):
		u"""操作配置，添加操作，排序运算"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "排序运算",
							"配置": {
								"选择变量": "表格数据",
								"排序配置": [
									{
										"操作": "添加",
										"列索引": "1",
										"排序方式": "升序"
									},
									{
										"操作": "添加",
										"列索引": "2",
										"排序方式": "降序"
									}
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "排序运算结果"
								},
								"输出列": "*",
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置，添加操作，排序运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeOptConf(self):
		u"""操作配置，添加操作，清洗筛选运算，按时间筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-按时间筛选",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"筛选方向": "正向",
								"按时间筛选": {
									"状态": "开启",
									"时间格式": "yyyy-MM-dd HH:mm:ss",
									"间隔": "-1",
									"单位": "年",
									"语言": "中文"
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
		log.info('>>>>> 操作配置，添加操作，清洗筛选运算，按时间筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeOptConf(self):
		u"""操作配置，添加操作，清洗筛选运算，按时间筛选，反向筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-按时间筛选-反向",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"筛选方向": "反向",
								"按时间筛选": {
									"状态": "开启",
									"时间格式": "yyyy-MM-dd HH:mm:ss",
									"间隔": "-1",
									"单位": "年",
									"语言": "中文"
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
		log.info('>>>>> 操作配置，添加操作，清洗筛选运算，按时间筛选，反向筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeOptConf(self):
		u"""操作配置，添加操作，清洗筛选运算，按关键字/变量筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-按关键字/变量筛选",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"筛选方向": "正向",
								"按关键字/变量筛选": {
									"状态": "开启",
									"筛选配置": [
										{
											"类型": "变量",
											"值": "日志类别"
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "选择",
												"正则模版名称": "auto_正则模版_匹配日期"
											}
										}
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
		log.info('>>>>> 操作配置，添加操作，清洗筛选运算，按关键字/变量筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_NodeOptConf(self):
		u"""操作配置，添加操作，清洗筛选运算，同时按时间筛选和按关键字/变量筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-同时筛选",
								"输入变量": "清洗日志",
								"赋值方式": "替换",
								"筛选方向": "正向",
								"按时间筛选": {
									"状态": "开启",
									"时间格式": "yyyy-MM-dd HH:mm:ss",
									"间隔": "-1",
									"单位": "年",
									"语言": "中文"
								},
								"按关键字/变量筛选": {
									"状态": "开启",
									"筛选配置": [
										{
											"类型": "变量",
											"值": "日志类别"
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "选择",
												"正则模版名称": "auto_正则模版_匹配日期"
											}
										}
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
		log.info('>>>>> 操作配置，添加操作，清洗筛选运算，同时按时间筛选和按关键字/变量筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_NodeOptConf(self):
		u"""操作配置，添加操作，动作，休眠"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
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

	def test_35_NodeOptConf(self):
		u"""操作配置，添加操作，动作，置空"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "动作",
							"配置": {
								"表达式": [
									[
										"置空",
										"原始数据"
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
		log.info('>>>>> 操作配置，添加操作，动作，置空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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

	def test_37_LineNode(self):
		u"""节点参数设置连线到节点：加载测试数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"起始节点名称": "参数设置",
				"终止节点名称": "加载测试数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：加载测试数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_LineNode(self):
		u"""节点加载测试数据连线到节点：运算"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"起始节点名称": "加载测试数据",
				"终止节点名称": "运算",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载测试数据连线到节点：运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_LineNode(self):
		u"""节点运算连线到节点：聚合运算"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"起始节点名称": "运算",
				"终止节点名称": "聚合运算",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点运算连线到节点：聚合运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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

	def test_41_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
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

	def test_42_LineNode(self):
		u"""节点聚合运算连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_运算操作",
				"起始节点名称": "聚合运算",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点聚合运算连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_运算操作"
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
