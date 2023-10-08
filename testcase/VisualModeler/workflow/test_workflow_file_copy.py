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


class WorkFlowFileNodeCopy(unittest.TestCase):

	log.info("装载流程文件拷贝移动测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动"
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
				"流程名称": "auto_流程_文件拷贝移动",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_文件拷贝移动说明",
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
				"流程名称": "auto_流程_文件拷贝移动",
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
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "参数设置",
					"场景标识": "无"
				}
			}
		}
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_5_NodeOptConf(self):
		u"""配置通用节点，添加一个变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
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
		log.info('>>>>> 配置通用节点，添加一个变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_6_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，不同类型文件匹配，txt"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "不同类型文件匹配",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果txt2",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，不同类型文件匹配，txt <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，不同类型文件匹配，csv"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "不同类型文件匹配",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，不同类型文件匹配，csv <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，不同类型文件匹配，xls"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "不同类型文件匹配",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果xls",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，不同类型文件匹配，xls <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，不同类型文件匹配，xlsx"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "不同类型文件匹配",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果xlsx",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，不同类型文件匹配，xlsx <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，不同类型文件匹配，pdf"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "不同类型文件匹配",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "${文件名关键字}",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，不同类型文件匹配，pdf <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，使用关键字过滤文件，匹配多个同类型文本文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配多个文本文件",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果txt",
							"目标文件": "拷贝文本结果.txt",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，使用关键字过滤文件，匹配多个同类型文本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，匹配多个表格文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配多个表格文件",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果xlsx",
							"目标文件": "拷贝表格结果.xlsx",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，匹配多个表格文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，使用正则匹配过滤文件，添加正则"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "使用正则匹配文件名",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
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
									},
									{
										"标签": "自定义文本",
										"自定义值": ".xls",
										"是否取值": "无"
									}
								]
							},
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，使用正则匹配过滤文件，添加正则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，使用正则匹配过滤文件，选择已有正则"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "使用正则匹配文件名",
				"业务配置": {
					"文件配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_数字中文"
							},
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，使用正则匹配过滤文件，选择已有正则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_19_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置文件节点，文件移动，从本地移动到ftp"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "从本地移动到ftp",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "远程",
						"远程服务器": "auto_ftp",
						"目录": "根目录-pw-1",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "${文件名关键字}",
							"目标文件": "",
							"模式": "移动"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件移动，从本地移动到ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_21_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置文件节点，文件移动，从ftp移动到本地"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "从ftp移动到本地",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "远程",
						"远程服务器": "auto_ftp",
						"目录": "根目录-pw-1",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_临时目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "${文件名关键字}",
							"目标文件": "",
							"模式": "移动"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件移动，从ftp移动到本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_23_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置文件节点，文件移动，从本地拷贝到ftp"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "从本地拷贝到ftp",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "远程",
						"远程服务器": "auto_ftp",
						"目录": "根目录-pw-1",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "${文件名关键字}",
							"目标文件": "",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件移动，从本地拷贝到ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_25_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_26_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，匹配不同类型文件，目标文件名不为空"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配不同类型文件且指定目标文件名",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "结果",
							"目标文件": "结果集合.txt",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，匹配不同类型文件，目标文件名不为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_27_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_28_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，匹配不同文本类型文件，目标文件名不为空"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配不同文本类型文件且指定目标文件名",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "文本结果",
							"目标文件": "拷贝结果集合2.txt",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，匹配不同文本类型文件，目标文件名不为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_29_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点"
			}
		}
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_30_NodeBusinessConf(self):
		u"""配置文件节点，文件拷贝，匹配不同表格类型文件，目标文件名不为空"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "匹配不同表格类型文件且指定目标文件名",
					"操作模式": "文件拷贝或移动",
					"源": {
						"存储类型": "本地",
						"目录": "auto_二级目录",
						"变量引用": "否"
					},
					"目标": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "表格结果",
							"目标文件": "拷贝表格集合2.txt",
							"模式": "拷贝"
						}
					]
				}
			}
		}
		log.info('>>>>> 配置文件节点，文件拷贝，匹配不同表格类型文件，目标文件名不为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_31_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 开始节点连线到节点：参数设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_32_LineNode(self):
		u"""节点参数设置连线到节点：不同类型文件匹配"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "参数设置",
				"终止节点名称": "不同类型文件匹配",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点参数设置连线到节点：不同类型文件匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_33_LineNode(self):
		u"""节点不同类型文件匹配连线到节点：匹配多个文本文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "不同类型文件匹配",
				"终止节点名称": "匹配多个文本文件",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点不同类型文件匹配连线到节点：匹配多个文本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_34_LineNode(self):
		u"""节点匹配多个文本文件连线到节点：匹配多个表格文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "匹配多个文本文件",
				"终止节点名称": "匹配多个表格文件",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点匹配多个文本文件连线到节点：匹配多个表格文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_35_LineNode(self):
		u"""节点匹配多个表格文件连线到节点：使用正则匹配文件名"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "匹配多个表格文件",
				"终止节点名称": "使用正则匹配文件名",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点匹配多个表格文件连线到节点：使用正则匹配文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_36_LineNode(self):
		u"""节点使用正则匹配文件名连线到节点：从本地移动到ftp"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "使用正则匹配文件名",
				"终止节点名称": "从本地移动到ftp",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点使用正则匹配文件名连线到节点：从本地移动到ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_37_LineNode(self):
		u"""节点从本地移动到ftp连线到节点：从ftp移动到本地"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "从本地移动到ftp",
				"终止节点名称": "从ftp移动到本地",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点从本地移动到ftp连线到节点：从ftp移动到本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_38_LineNode(self):
		u"""节点从ftp移动到本地连线到节点：从本地拷贝到ftp"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "从ftp移动到本地",
				"终止节点名称": "从本地拷贝到ftp",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点从ftp移动到本地连线到节点：从本地拷贝到ftp <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_39_LineNode(self):
		u"""节点从本地拷贝到ftp连线到节点：匹配不同类型文件且指定目标文件名"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "从本地拷贝到ftp",
				"终止节点名称": "匹配不同类型文件且指定目标文件名",
				"关联关系": "满足"
			}
		}
		log.info('>>>>> 节点从本地拷贝到ftp连线到节点：匹配不同类型文件且指定目标文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_40_LineNode(self):
		u"""节点匹配不同类型文件且指定目标文件名连线到节点：匹配不同文本类型文件且指定目标文件名"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "匹配不同类型文件且指定目标文件名",
				"终止节点名称": "匹配不同文本类型文件且指定目标文件名",
				"关联关系": "无条件"
			}
		}
		log.info('>>>>> 节点匹配不同类型文件且指定目标文件名连线到节点：匹配不同文本类型文件且指定目标文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_41_LineNode(self):
		u"""节点匹配不同文本类型文件且指定目标文件名连线到节点：匹配不同表格类型文件且指定目标文件名"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "匹配不同文本类型文件且指定目标文件名",
				"终止节点名称": "匹配不同表格类型文件且指定目标文件名",
				"关联关系": "无条件"
			}
		}
		log.info('>>>>> 节点匹配不同文本类型文件且指定目标文件名连线到节点：匹配不同表格类型文件且指定目标文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_42_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
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

	def test_43_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
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

	def test_44_LineNode(self):
		u"""节点匹配不同表格类型文件且指定目标文件名连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动",
				"起始节点名称": "匹配不同表格类型文件且指定目标文件名",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点匹配不同表格类型文件且指定目标文件名连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_文件拷贝移动"
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
