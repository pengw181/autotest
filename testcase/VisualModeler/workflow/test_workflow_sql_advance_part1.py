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


class WorkFlowSqlNodeAdvanceModePart1(unittest.TestCase):

	log.info("装载流程数据库节点SQL模式测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式"
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
				"流程名称": "auto_流程_数据库节点SQL模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_数据库节点SQL模式说明",
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
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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
				"流程名称": "auto_流程_数据库节点SQL模式",
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
		u"""通用节点，添加一个自定义变量，内置变量，时间变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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
										"变量",
										{
											"变量名称": "时间变量",
											"时间格式": "yyyy-MM-dd HH:mm:ss",
											"间隔": "0",
											"单位": "日",
											"语言": "中文"
										}
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "当前时间"
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
		log.info('>>>>> 通用节点，添加一个自定义变量，内置变量，时间变量 <<<<<')
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
				"流程名称": "auto_流程_数据库节点SQL模式",
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
		u"""配置文件节点，文件加载，从本地加载测试数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载入库数据",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "data",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"sheet页索引": "2",
							"变量": "加载数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点，文件加载，从本地加载测试数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_9_NodeBusinessConf(self):
		u"""配置数据库节点，删除历史数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "删除历史数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_11_NodeBusinessConf(self):
		u"""配置数据库节点，查询语句"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "查询内部库",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，查询语句 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_13_NodeBusinessConf(self):
		u"""配置数据库节点，对表数据进行insert"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对表数据进行insert",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into ${OtherInfoTableName} (pk, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3, col_4, col_5, col_6, aisee_batch_tag) values(uuid(), 'pw', 0, now(), '440100', 'AiSeeCore', '张三', '张三', '张三', '张三', '张三', '0')"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，对表数据进行insert <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启循环"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "对表数据进行insert",
				"控制配置": {
					"开启循环": {
						"状态": "开启",
						"循环条件": [
							"业务配置",
							"操作配置"
						],
						"循环类型": "变量列表",
						"循环内容": {
							"模式": "自定义模式",
							"变量名称": "加载数据",
							"循环行变量名称": "loop_加载数据",
							"赋值方式": "替换"
						}
					},
					"按列取数": {
						"是否开启按列取数": "开启",
						"变量列表": [
							{
								"变量名称": "列1",
								"赋值方式": "替换",
								"数据索引": "1"
							},
							{
								"变量名称": "列2",
								"赋值方式": "替换",
								"数据索引": "2"
							},
							{
								"变量名称": "列3",
								"赋值方式": "替换",
								"数据索引": "3"
							},
							{
								"变量名称": "列4",
								"赋值方式": "替换",
								"数据索引": "4"
							},
							{
								"变量名称": "列5",
								"赋值方式": "替换",
								"数据索引": "5"
							}
						]
					},
					"高级配置": {
						"是否记录循环日志": "是",
						"循环日志记录条数": "50",
						"输出日志打印规则": "1-5"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启循环 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置数据库节点，insert网元其它资料表，重新整理sql内容，引用变量"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "对表数据进行insert",
				"业务配置": {
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into ${OtherInfoTableName} (pk, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3, col_4, col_5, col_6, aisee_batch_tag) values(uuid(), 'pw', 0, now(), '440100', 'AiSeeCore', '${列1}', '${列2}', '${列3}', '${列4}', '${列5}', '0')"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，insert网元其它资料表，重新整理sql内容，引用变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_17_NodeBusinessConf(self):
		u"""配置数据库节点，对表数据进行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对表数据进行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${OtherInfoTableName} set col_5 = 'high' where col_5 > 10000"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，对表数据进行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_19_NodeBusinessConf(self):
		u"""配置数据库节点，对表数据进行delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对表数据进行delete",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${OtherInfoTableName} where col_5 = 'high'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，对表数据进行delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_21_NodeBusinessConf(self):
		u"""配置数据库节点，mysql外部库drop表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "mysql外部库drop表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，mysql外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_23_NodeBusinessConf(self):
		u"""配置数据库节点，mysql外部库create表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "mysql外部库create表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "create table auto_test_sql_data("
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   stats_date varchar(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   netunit varchar(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   hv int,"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   cv int,"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   category varchar(64),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   insert_date date"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": ")"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，mysql外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_25_NodeBusinessConf(self):
		u"""配置数据库节点，mysql外部库insert数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "mysql外部库insert数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into auto_test_sql_data values('2019', 'GZ001', 122, 1222, '101', now())"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，mysql外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_27_NodeBusinessConf(self):
		u"""配置数据库节点，mysql外部库select数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "mysql外部库select数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，mysql外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_29_NodeBusinessConf(self):
		u"""配置数据库节点，oracle外部库drop表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "oracle外部库drop表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_oracle数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，oracle外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_31_NodeBusinessConf(self):
		u"""配置数据库节点，oracle外部库create表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "oracle外部库create表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_oracle数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "create table auto_test_sql_data("
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   stats_date varchar2(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   netunit varchar2(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   hv number(20,0),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   cv number(20,0),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   category varchar2(64),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   insert_date date"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": ")"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，oracle外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_33_NodeBusinessConf(self):
		u"""配置数据库节点，oracle外部库insert数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "oracle外部库insert数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_oracle数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into auto_test_sql_data values('2019', 'GZ001', 122, 1222, '101', sysdate)"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，oracle外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_35_NodeBusinessConf(self):
		u"""配置数据库节点，oracle外部库select数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "oracle外部库select数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_oracle数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，oracle外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_37_NodeBusinessConf(self):
		u"""配置数据库节点，postgres外部库drop表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "postgres外部库drop表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_postgres数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，postgres外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_39_NodeBusinessConf(self):
		u"""配置数据库节点，postgres外部库create表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "postgres外部库create表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_postgres数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "create table auto_test_sql_data("
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   stats_date varchar(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   netunit varchar(100),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   hv numeric,"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   cv numeric,"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   category varchar(64),"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": "   insert_date timestamp"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "自定义值",
								"自定义值": ")"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，postgres外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_41_NodeBusinessConf(self):
		u"""配置数据库节点，postgres外部库insert数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "postgres外部库insert数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_postgres数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into auto_test_sql_data values('2019', 'GZ001', 122, 1222, '101', now())"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，postgres外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_43_NodeBusinessConf(self):
		u"""配置数据库节点，postgres外部库select数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "postgres外部库select数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_postgres数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，postgres外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_45_NodeBusinessConf(self):
		u"""配置数据库节点，mysql外部库drop表：auto_test_sql_data2"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "删除备用表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table auto_test_sql_data2"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，mysql外部库drop表：auto_test_sql_data2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_47_NodeBusinessConf(self):
		u"""配置数据库节点，使用create as select创建表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "使用create as select创建表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "create table auto_test_sql_data2 as select * from auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，使用create as select创建表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_49_NodeBusinessConf(self):
		u"""配置数据库节点，使用insert into select插入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "使用insert into select插入数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into auto_test_sql_data2 select * from auto_test_sql_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，使用insert into select插入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_NodeFetchConf(self):
		u"""节点添加取数配置，不含列名"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "添加",
					"变量名": "查询结果_不含列名",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，不含列名 <<<<<')
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
