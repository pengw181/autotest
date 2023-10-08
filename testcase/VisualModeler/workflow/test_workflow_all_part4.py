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


class WorkFlowAllNodePart4(unittest.TestCase):

	log.info("装载全流程功能测试用例（4）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_150_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_151_NodeBusinessConf(self):
		u"""配置AI节点：随机森林模型，通用分类算法，随机森林模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "随机森林模型",
					"节点模式": "通用分类算法",
					"算法选择": "随机森林模型",
					"模型": "auto_AI模型随机森林",
					"输入变量": "通用算法接入数据"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点：随机森林模型，通用分类算法，随机森林模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_152_LineNode(self):
		u"""开始节点连线到参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到"参数设置" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_153_LineNode(self):
		u"""节点参数设置连线到指令节点多指令"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "指令节点多指令",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到"指令节点多指令" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_154_LineNode(self):
		u"""节点指令节点多指令连线到指令结果数组格式化"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "指令节点多指令",
				"终止节点名称": "指令结果数组格式化",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令节点多指令"连线到"指令结果数组格式化" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_155_LineNode(self):
		u"""节点指令结果数组格式化连线到将指令结果存入文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "指令结果数组格式化",
				"终止节点名称": "将指令结果存入文件",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令结果数组格式化"连线到"将指令结果存入文件" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_156_LineNode(self):
		u"""节点将指令结果存入文件连线到将文件移入临时目录"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "将指令结果存入文件",
				"终止节点名称": "将文件移入临时目录",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"将指令结果存入文件"连线到"将文件移入临时目录" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_157_LineNode(self):
		u"""节点将文件移入临时目录连线到从临时目录加载文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "将文件移入临时目录",
				"终止节点名称": "从临时目录加载文件",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"将文件移入临时目录"连线到"从临时目录加载文件" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_158_LineNode(self):
		u"""节点从临时目录加载文件连线到清除历史数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "从临时目录加载文件",
				"终止节点名称": "清除历史数据",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"从临时目录加载文件"连线到"清除历史数据" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_159_LineNode(self):
		u"""节点清除历史数据连线到将指令结果格式化存入数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "清除历史数据",
				"终止节点名称": "将指令结果格式化存入数据库",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"清除历史数据"连线到"将指令结果格式化存入数据库" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_160_LineNode(self):
		u"""节点将指令结果格式化存入数据库连线到python脚本"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "将指令结果格式化存入数据库",
				"终止节点名称": "python脚本",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"将指令结果格式化存入数据库"连线到"python脚本" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_161_LineNode(self):
		u"""节点python脚本连线到java脚本"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "python脚本",
				"终止节点名称": "java脚本",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"python脚本"连线到"java脚本" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_162_LineNode(self):
		u"""节点java脚本连线到jar脚本"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "java脚本",
				"终止节点名称": "jar脚本",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"java脚本"连线到"jar脚本" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_163_LineNode(self):
		u"""节点jar脚本连线到表格取数"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "jar脚本",
				"终止节点名称": "表格取数",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"jar脚本"连线到"表格取数" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_164_LineNode(self):
		u"""节点表格取数连线到文件下载"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "表格取数",
				"终止节点名称": "文件下载",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"表格取数"连线到"文件下载" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_165_LineNode(self):
		u"""节点文件下载连线到附件上传"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "文件下载",
				"终止节点名称": "附件上传",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"文件下载"连线到"附件上传" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_166_LineNode(self):
		u"""节点附件上传连线到restful接口"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "附件上传",
				"终止节点名称": "restful接口",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"附件上传"连线到"restful接口" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_167_LineNode(self):
		u"""节点restful接口连线到soap接口"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "restful接口",
				"终止节点名称": "soap接口",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"restful接口"连线到"soap接口" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_168_LineNode(self):
		u"""节点soap接口连线到webservice接口"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "soap接口",
				"终止节点名称": "webservice接口",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"soap接口"连线到"webservice接口" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_169_LineNode(self):
		u"""节点webservice接口连线到多网元类型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "webservice接口",
				"终止节点名称": "多网元类型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"webservice接口"连线到"多网元类型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_170_LineNode(self):
		u"""节点多网元类型连线到指令模版带参数"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "多网元类型",
				"终止节点名称": "指令模版带参数",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"多网元类型"连线到"指令模版带参数" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_171_LineNode(self):
		u"""节点指令模版带参数连线到指令模版按网元类型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "指令模版带参数",
				"终止节点名称": "指令模版按网元类型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令模版带参数"连线到"指令模版按网元类型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_172_LineNode(self):
		u"""节点指令模版按网元类型连线到数据拼盘二维表模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "指令模版按网元类型",
				"终止节点名称": "数据拼盘二维表模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令模版按网元类型"连线到"数据拼盘二维表模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_173_LineNode(self):
		u"""节点数据拼盘二维表模式连线到数据拼盘列更新模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "数据拼盘二维表模式",
				"终止节点名称": "数据拼盘列更新模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据拼盘二维表模式"连线到"数据拼盘列更新模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_174_LineNode(self):
		u"""节点数据拼盘列更新模式连线到数据拼盘分段模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "数据拼盘列更新模式",
				"终止节点名称": "数据拼盘分段模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据拼盘列更新模式"连线到"数据拼盘分段模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_175_LineNode(self):
		u"""节点数据拼盘分段模式连线到数据拼盘合并模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "数据拼盘分段模式",
				"终止节点名称": "数据拼盘合并模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据拼盘分段模式"连线到"数据拼盘合并模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_176_LineNode(self):
		u"""节点数据拼盘合并模式连线到邮件发送"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "数据拼盘合并模式",
				"终止节点名称": "邮件发送",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据拼盘合并模式"连线到"邮件发送" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_177_LineNode(self):
		u"""节点邮件发送连线到指令运行情况汇总"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "邮件发送",
				"终止节点名称": "指令运行情况汇总",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"邮件发送"连线到"指令运行情况汇总" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_178_LineNode(self):
		u"""节点指令运行情况汇总连线到流程相关信息展示"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "指令运行情况汇总",
				"终止节点名称": "流程相关信息展示",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令运行情况汇总"连线到"流程相关信息展示" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_179_LineNode(self):
		u"""节点流程相关信息展示连线到邮件接收"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "流程相关信息展示",
				"终止节点名称": "邮件接收",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"流程相关信息展示"连线到"邮件接收" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_180_LineNode(self):
		u"""节点邮件接收连线到加载AI预测数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "邮件接收",
				"终止节点名称": "加载AI预测数据",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"邮件接收"连线到"加载AI预测数据" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_181_LineNode(self):
		u"""节点加载AI预测数据连线到LSTM预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "加载AI预测数据",
				"终止节点名称": "LSTM预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"加载AI预测数据"连线到"LSTM预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_182_LineNode(self):
		u"""节点LSTM预测模型连线到SARIMA预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "LSTM预测模型",
				"终止节点名称": "SARIMA预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"LSTM预测模型"连线到"SARIMA预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_183_LineNode(self):
		u"""节点SARIMA预测模型连线到GRU预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "SARIMA预测模型",
				"终止节点名称": "GRU预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"SARIMA预测模型"连线到"GRU预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_184_LineNode(self):
		u"""节点GRU预测模型连线到xgboost预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "GRU预测模型",
				"终止节点名称": "xgboost预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"GRU预测模型"连线到"xgboost预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_185_LineNode(self):
		u"""节点xgboost预测模型连线到factorLGBM模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "xgboost预测模型",
				"终止节点名称": "factorLGBM模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"xgboost预测模型"连线到"factorLGBM模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_186_LineNode(self):
		u"""节点factorLGBM模型连线到lightgbm模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "factorLGBM模型",
				"终止节点名称": "lightgbm模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"factorLGBM模型"连线到"lightgbm模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_187_LineNode(self):
		u"""节点lightgbm模型连线到梯度提升树（GBDT）模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "lightgbm模型",
				"终止节点名称": "梯度提升树（GBDT）模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"lightgbm模型"连线到"梯度提升树（GBDT）模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_188_LineNode(self):
		u"""节点梯度提升树（GBDT）模型连线到随机森林模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "梯度提升树（GBDT）模型",
				"终止节点名称": "随机森林模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"梯度提升树（GBDT）模型"连线到"随机森林模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_189_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
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

	def test_190_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_全流程",
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

	def test_191_LineNode(self):
		u"""节点随机森林模型连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_全流程",
				"起始节点名称": "随机森林模型",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"随机森林模型"连线到结束节点 <<<<<')
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
