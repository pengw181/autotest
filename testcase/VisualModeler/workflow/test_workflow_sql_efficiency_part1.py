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


class WorkFlowSqlNodeEfficiencyPart1(unittest.TestCase):

	log.info("装载流程数据库节点大数据效率测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试数据库节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_外部库导入效率说明",
				"高级配置": {
					"节点异常终止流程": "否"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
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

	def test_4_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据1w_正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载大数据入库数据1w",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据1w_正常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据1w_正常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据1w_正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据1w_异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "加载大数据入库数据1w",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据1w_异常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据1w_异常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据1w_异常 <<<<<')
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
				"流程名称": "auto_流程_外部库导入效率",
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
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据2w_正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载大数据入库数据2w",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据2w_正常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据2w_正常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据2w_正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据2w_异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "加载大数据入库数据2w",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据2w_异常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据2w_异常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据2w_异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
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

	def test_10_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据5w_正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载大数据入库数据5w",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据5w_正常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据5w_正常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据5w_正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据5w_异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "加载大数据入库数据5w",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据5w_异常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据5w_异常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据5w_异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
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

	def test_13_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据10w_正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载大数据入库数据10w",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据10w_正常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据10w_正常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据10w_正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeBusinessConf(self):
		u"""配置文件节点，文件加载，从本地加载测试数据：大数据10w_异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "文件节点",
				"节点名称": "加载大数据入库数据10w",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "大数据10w_异常",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "大数据10w_异常",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据：大数据10w_异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NodeBusinessConf(self):
		u"""配置数据库节点，删除历史数据，pg数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "postgres外部表数据清理",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_postgres数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${BigImportTable}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，删除历史数据，pg数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置数据库节点，删除历史数据，oracle数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "oracle外部表数据清理",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_oracle数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${BigImportTable}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，删除历史数据，oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置数据库节点，删除历史数据，mysql数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "mysql外部表数据清理",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${BigImportTable}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，删除历史数据，mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部pg数据库1w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库1w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_正常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部pg数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部oracle数据库1w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库1w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_正常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部oracle数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部mysql数据库1w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库1w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_正常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部mysql数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部pg数据库2w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库2w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_正常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部pg数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部oracle数据库2w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库2w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_正常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部oracle数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部mysql数据库2w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库2w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_正常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部mysql数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部pg数据库5w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库5w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_正常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部pg数据库5w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部oracle数据库5w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库5w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_正常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部oracle数据库5w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部mysql数据库5w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库5w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_正常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部mysql数据库5w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部pg数据库10w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库10w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_正常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部pg数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部oracle数据库10w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库10w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_正常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部oracle数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，导入外部mysql数据库10w正常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库10w正常",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_正常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，导入外部mysql数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，pg数据库，批量提交行数不为空，1w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库1w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_异常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，pg数据库，批量提交行数不为空，1w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，1w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库1w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_异常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，1w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，1w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库1w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据1w_异常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，1w部分异常 <<<<<')
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
