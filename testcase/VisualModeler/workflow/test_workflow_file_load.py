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


class WorkFlowFileNodeLoad(unittest.TestCase):

	log.info("装载流程文件加载测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_文件加载"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试文件节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_文件加载说明",
				"高级配置": {
					"节点异常终止流程": "否"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试文件节点 <<<<<')
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
				"流程名称": "auto_流程_文件加载",
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
				"流程名称": "auto_流程_文件加载",
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
		u"""配置通用节点，添加一个变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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
											"图像结果"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "文件名关键字"
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
		log.info('>>>>> 配置通用节点，添加一个变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_7_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，分别加载不同类型文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载不同类型文件",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "网元解析结果2",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"sheet页索引": "",
							"变量": "文件加载xlsx",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，分别加载不同类型文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置txt"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果txt2",
							"文件类型": "txt",
							"编码格式": "GBK",
							"开始读取行": "1",
							"分隔符": "",
							"变量": "文件加载txt"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置txt <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置csv"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果csv3",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"分隔符": ",",
							"变量": "文件加载csv"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置csv <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置xls"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果xls",
							"文件类型": "xls",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"sheet页索引": "",
							"变量": "文件加载xls",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置xls <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置csv，匹配多个文本文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果csv",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"分隔符": ",",
							"变量": "文件加载多个csv"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置csv，匹配多个文本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置pdf，文件类型配置在文件名内"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "图像结果pdf.pdf",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"变量": "文件加载pdf"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置pdf，文件类型配置在文件名内 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，添加一条配置xlsx，匹配多个表格文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "加载不同类型文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果xlsx",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"sheet页索引": "",
							"变量": "文件加载xlsx",
							"变量类型": "追加"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，添加一条配置xlsx，匹配多个表格文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_15_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，加载指定sheet页数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载指定sheet页数据",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "拷贝表格结果",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"sheet页索引": "2",
							"变量": "加载指定sheet页数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，加载指定sheet页数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_17_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，文件名使用正则匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "使用正则匹配文件名加载文件",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_数字中文"
							},
							"文件类型": "xls",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"sheet页索引": "",
							"变量": "正则匹配文件名加载_前缀",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，文件名使用正则匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，文件名使用正则匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "使用正则匹配文件名加载文件",
				"业务配置": {
					"文件配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "添加",
								"正则模版名称": "auto_正则模版",
								"标签配置": [
									{
										"标签": "自定义文本",
										"自定义值": "网元结果_",
										"是否取值": "无"
									},
									{
										"标签": "日期",
										"时间格式": "2014-05-28",
										"是否取值": "无"
									}
								]
							},
							"文件类型": "xls",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"sheet页索引": "",
							"变量": "正则匹配文件名加载_后缀",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，文件名使用正则匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_20_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从ftp加载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "从ftp加载文件",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "远程",
						"远程服务器": "auto_ftp",
						"目录": "根目录-pw-1",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "${文件名关键字}",
							"编码格式": "GBK",
							"开始读取行": "1",
							"变量": "ftp文件加载",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从ftp加载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_22_NodeBusinessConf(self):
		u"""配置文件节点，文件加载模式，开启过滤，选择正则"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "文件加载开启过滤",
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
							"编码格式": "GBK",
							"开始读取行": "",
							"分隔符": "",
							"变量": "文件加载过滤",
							"变量类型": "替换",
							"开启过滤": {
								"状态": "开启",
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_匹配日期"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载模式，开启过滤，选择正则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_24_NodeBusinessConf(self):
		u"""配置文件节点，文件加载模式，匹配到多个不同类型文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配到多个不同类型文件",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "结果",
							"文件类型": "",
							"编码格式": "UTF-8",
							"开始读取行": "1",
							"变量": "匹配到多个不同类型文件",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载模式，匹配到多个不同类型文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_26_LineNode(self):
		u"""节点参数设置连线到节点：加载不同类型文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "参数设置",
				"终止节点名称": "加载不同类型文件",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：加载不同类型文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_LineNode(self):
		u"""节点加载不同类型文件连线到节点：加载指定sheet页数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "加载不同类型文件",
				"终止节点名称": "加载指定sheet页数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载不同类型文件连线到节点：加载指定sheet页数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_LineNode(self):
		u"""节点加载指定sheet页数据连线到节点：使用正则匹配文件名加载文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "加载指定sheet页数据",
				"终止节点名称": "使用正则匹配文件名加载文件",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载指定sheet页数据连线到节点：使用正则匹配文件名加载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_LineNode(self):
		u"""节点使用正则匹配文件名加载文件连线到节点：从ftp加载文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "使用正则匹配文件名加载文件",
				"终止节点名称": "从ftp加载文件",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点使用正则匹配文件名加载文件连线到节点：从ftp加载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_LineNode(self):
		u"""节点从ftp加载文件连线到节点：文件加载开启过滤"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "从ftp加载文件",
				"终止节点名称": "文件加载开启过滤",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点从ftp加载文件连线到节点：文件加载开启过滤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_LineNode(self):
		u"""节点文件加载开启过滤连线到节点：匹配到多个不同类型文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "文件加载开启过滤",
				"终止节点名称": "匹配到多个不同类型文件",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点文件加载开启过滤连线到节点：匹配到多个不同类型文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_33_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
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

	def test_34_LineNode(self):
		u"""节点匹配到多个不同类型文件连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件加载",
				"起始节点名称": "匹配到多个不同类型文件",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点匹配到多个不同类型文件连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_文件加载"
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
