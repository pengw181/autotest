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


class WorkFlowSqlNodeAdvanceModePart2(unittest.TestCase):

	log.info("装载流程数据库节点SQL模式测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_NodeFetchConf(self):
		u"""节点添加取数配置，含列名"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "添加",
					"变量名": "查询结果_含列名",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，含列名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeFetchConf(self):
		u"""节点添加取数配置，取部分列"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "添加",
					"变量名": "查询结果_取部分列",
					"赋值方式": "替换",
					"输出列": "1,2,3",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，取部分列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_NodeFetchConf(self):
		u"""节点添加取数配置，mysql外部库select数据"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "mysql外部库select数据",
				"取数配置": {
					"操作": "添加",
					"变量名": "mysql外部库select查询结果",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，mysql外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_NodeFetchConf(self):
		u"""节点添加取数配置，oracle外部库select数据"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "oracle外部库select数据",
				"取数配置": {
					"操作": "添加",
					"变量名": "oracle外部库select查询结果",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，oracle外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_NodeFetchConf(self):
		u"""节点添加取数配置，postgres外部库select数据"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"节点类型": "数据库节点",
				"节点名称": "postgres外部库select数据",
				"取数配置": {
					"操作": "添加",
					"变量名": "postgres外部库select查询结果",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，postgres外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_57_LineNode(self):
		u"""节点参数设置连线到节点：加载入库数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "参数设置",
				"终止节点名称": "加载入库数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：加载入库数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_LineNode(self):
		u"""节点加载入库数据连线到节点：删除历史数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "加载入库数据",
				"终止节点名称": "删除历史数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载入库数据连线到节点：删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_LineNode(self):
		u"""节点删除历史数据连线到节点：查询内部库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "删除历史数据",
				"终止节点名称": "查询内部库",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点删除历史数据连线到节点：查询内部库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_LineNode(self):
		u"""节点查询内部库连线到节点：insert网元其它资料表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "查询内部库",
				"终止节点名称": "对表数据进行insert",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点查询内部库连线到节点：insert网元其它资料表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_LineNode(self):
		u"""节点对表数据进行insert连线到节点：对表数据进行update"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "对表数据进行insert",
				"终止节点名称": "对表数据进行update",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点对表数据进行insert连线到节点：对表数据进行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_LineNode(self):
		u"""节点对表数据进行update连线到节点：对表数据进行delete"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "对表数据进行update",
				"终止节点名称": "对表数据进行delete",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点对表数据进行update连线到节点：对表数据进行delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_LineNode(self):
		u"""节点对表数据进行delete连线到节点：mysql外部库drop表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "对表数据进行delete",
				"终止节点名称": "mysql外部库drop表",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点对表数据进行delete连线到节点：mysql外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_LineNode(self):
		u"""节点mysql外部库drop表连线到节点：mysql外部库create表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "mysql外部库drop表",
				"终止节点名称": "mysql外部库create表",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部库drop表连线到节点：mysql外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_LineNode(self):
		u"""节点mysql外部库create表连线到节点：mysql外部库insert数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "mysql外部库create表",
				"终止节点名称": "mysql外部库insert数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部库create表连线到节点：mysql外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_LineNode(self):
		u"""节点mysql外部库insert数据连线到节点：mysql外部库select数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "mysql外部库insert数据",
				"终止节点名称": "mysql外部库select数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部库insert数据连线到节点：mysql外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_LineNode(self):
		u"""节点mysql外部库select数据连线到节点：oracle外部库drop表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "mysql外部库select数据",
				"终止节点名称": "oracle外部库drop表",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部库select数据连线到节点：oracle外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_LineNode(self):
		u"""节点oracle外部库drop表连线到节点：oracle外部库create表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "oracle外部库drop表",
				"终止节点名称": "oracle外部库create表",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部库drop表连线到节点：oracle外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_LineNode(self):
		u"""节点oracle外部库create表连线到节点：oracle外部库insert数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "oracle外部库create表",
				"终止节点名称": "oracle外部库insert数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部库create表连线到节点：oracle外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_LineNode(self):
		u"""节点oracle外部库insert数据连线到节点：oracle外部库select数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "oracle外部库insert数据",
				"终止节点名称": "oracle外部库select数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部库insert数据连线到节点：oracle外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_LineNode(self):
		u"""节点oracle外部库select数据连线到节点：postgres外部库drop表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "oracle外部库select数据",
				"终止节点名称": "postgres外部库drop表",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部库select数据连线到节点：postgres外部库drop表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_LineNode(self):
		u"""节点postgres外部库drop表连线到节点：postgres外部库create表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "postgres外部库drop表",
				"终止节点名称": "postgres外部库create表",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部库drop表连线到节点：postgres外部库create表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_LineNode(self):
		u"""节点postgres外部库create表连线到节点：postgres外部库insert数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "postgres外部库create表",
				"终止节点名称": "postgres外部库insert数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部库create表连线到节点：postgres外部库insert数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_LineNode(self):
		u"""节点postgres外部库insert数据连线到节点：postgres外部库select数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "postgres外部库insert数据",
				"终止节点名称": "postgres外部库select数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部库insert数据连线到节点：postgres外部库select数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_LineNode(self):
		u"""节点postgres外部库select数据连线到节点：删除备用表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "postgres外部库select数据",
				"终止节点名称": "删除备用表",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部库select数据连线到节点：删除备用表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_LineNode(self):
		u"""节点删除备用表连线到节点：使用create as select创建表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "删除备用表",
				"终止节点名称": "使用create as select创建表",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点删除备用表连线到节点：使用create as select创建表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_LineNode(self):
		u"""节点使用create as select创建表连线到节点：使用insert into select插入数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "使用create as select创建表",
				"终止节点名称": "使用insert into select插入数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点使用create as select创建表连线到节点：使用insert into select插入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_79_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
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

	def test_80_LineNode(self):
		u"""节点使用insert into select插入数据连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式",
				"起始节点名称": "使用insert into select插入数据",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点使用insert into select插入数据连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_数据库节点SQL模式"
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
