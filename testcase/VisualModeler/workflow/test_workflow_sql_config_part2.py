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


class WorkFlowSqlNodeConfigModePart2(unittest.TestCase):

	log.info("装载流程数据库节点配置模式测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，pg数据库，部分成功，取异常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部pg数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部pg数据库部分成功_异常条数",
					"输出内容": "异常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，pg数据库，部分成功，取异常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取总条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部oracle数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部oracle数据库部分成功_总条数",
					"输出内容": "总条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，oracle数据库，部分成功，取总条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取正常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部oracle数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部oracle数据库部分成功_正常条数",
					"输出内容": "正常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，oracle数据库，部分成功，取正常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取异常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部oracle数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部oracle数据库部分成功_异常条数",
					"输出内容": "异常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，oracle数据库，部分成功，取异常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取总条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库部分成功_总条数",
					"输出内容": "总条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，mysql数据库，部分成功，取总条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取正常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库部分成功_正常条数",
					"输出内容": "正常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，mysql数据库，部分成功，取正常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取异常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库部分成功",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库部分成功_异常条数",
					"输出内容": "异常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，mysql数据库，部分成功，取异常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，跳过行数不为空，取总条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库跳过部分行",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库跳过部分行_总条数",
					"输出内容": "总条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，跳过行数不为空，取总条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，跳过行数不为空，取正常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库跳过部分行",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库跳过部分行_正常条数",
					"输出内容": "正常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，跳过行数不为空，取正常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，跳过行数不为空，取异常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库跳过部分行",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库跳过部分行_异常条数",
					"输出内容": "异常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，跳过行数不为空，取异常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
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

	def test_62_LineNode(self):
		u"""节点参数设置连线到节点：删除历史数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "参数设置",
				"终止节点名称": "删除历史数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_LineNode(self):
		u"""节点删除历史数据连线到节点：加载入库数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "删除历史数据",
				"终止节点名称": "加载入库数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点删除历史数据连线到节点：加载入库数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_LineNode(self):
		u"""节点加载入库数据连线到节点：数据插入网元其它资料"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "加载入库数据",
				"终止节点名称": "数据插入网元其它资料",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载入库数据连线到节点：数据插入网元其它资料 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_LineNode(self):
		u"""节点数据插入网元其它资料连线到节点：查询内部库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "数据插入网元其它资料",
				"终止节点名称": "查询内部库",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点数据插入网元其它资料连线到节点：查询内部库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_LineNode(self):
		u"""节点查询内部库连线到节点：数据插入数据拼盘"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "查询内部库",
				"终止节点名称": "数据插入数据拼盘",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点查询内部库连线到节点：数据插入数据拼盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_LineNode(self):
		u"""节点数据插入数据拼盘连线到节点：加载大数据入库数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "数据插入数据拼盘",
				"终止节点名称": "加载大数据入库数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点数据插入数据拼盘连线到节点：加载大数据入库数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_LineNode(self):
		u"""节点加载大数据入库数据连线到节点：postgres外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "加载大数据入库数据",
				"终止节点名称": "postgres外部表数据清理",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载大数据入库数据连线到节点：postgres外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_LineNode(self):
		u"""节点postgres外部表数据清理连线到节点：oracle外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "postgres外部表数据清理",
				"终止节点名称": "oracle外部表数据清理",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部表数据清理连线到节点：oracle外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_LineNode(self):
		u"""节点oracle外部表数据清理连线到节点：mysql外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "oracle外部表数据清理",
				"终止节点名称": "mysql外部表数据清理",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部表数据清理连线到节点：mysql外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_LineNode(self):
		u"""节点mysql外部表数据清理连线到节点：导入外部pg数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "mysql外部表数据清理",
				"终止节点名称": "导入外部pg数据库",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部表数据清理连线到节点：导入外部pg数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_LineNode(self):
		u"""节点导入外部pg数据库连线到节点：导入外部oracle数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部pg数据库",
				"终止节点名称": "导入外部oracle数据库",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库连线到节点：导入外部oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_LineNode(self):
		u"""节点导入外部oracle数据库连线到节点：导入外部mysql数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部oracle数据库",
				"终止节点名称": "导入外部mysql数据库",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库连线到节点：导入外部mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_LineNode(self):
		u"""节点导入外部mysql数据库连线到节点：批量提交行数为空存在异常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部mysql数据库",
				"终止节点名称": "批量提交行数为空存在异常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库连线到节点：批量提交行数为空存在异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_LineNode(self):
		u"""节点批量提交行数为空存在异常连线到节点：批量提交行数不为空且全部成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "批量提交行数为空存在异常",
				"终止节点名称": "批量提交行数不为空且全部成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点批量提交行数为空存在异常连线到节点：批量提交行数不为空且全部成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_LineNode(self):
		u"""节点批量提交行数不为空且全部成功连线到节点：导入外部pg数据库部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "批量提交行数不为空且全部成功",
				"终止节点名称": "导入外部pg数据库部分成功",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点批量提交行数不为空且全部成功连线到节点：导入外部pg数据库部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_LineNode(self):
		u"""节点导入外部pg数据库部分成功连线到节点：导入外部oracle数据库部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部pg数据库部分成功",
				"终止节点名称": "导入外部oracle数据库部分成功",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库部分成功连线到节点：导入外部oracle数据库部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_LineNode(self):
		u"""节点导入外部oracle数据库部分成功连线到节点：导入外部mysql数据库部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部oracle数据库部分成功",
				"终止节点名称": "导入外部mysql数据库部分成功",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库部分成功连线到节点：导入外部mysql数据库部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_LineNode(self):
		u"""节点导入外部mysql数据库部分成功连线到节点：导入外部mysql数据库跳过部分行"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部mysql数据库部分成功",
				"终止节点名称": "导入外部mysql数据库跳过部分行",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库部分成功连线到节点：导入外部mysql数据库跳过部分行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
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

	def test_81_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
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

	def test_82_LineNode(self):
		u"""节点导入外部mysql数据库跳过部分行连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式",
				"起始节点名称": "导入外部mysql数据库跳过部分行",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库跳过部分行连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_数据库配置模式"
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
