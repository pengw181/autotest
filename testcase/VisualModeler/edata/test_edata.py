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


class Edata(unittest.TestCase):

	log.info("装载数据拼盘测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_TaskDataClear(self):
		u"""任务数据清理，删除历史数据"""
		pres = """
		${Database}.main|update tn_node_edata_custom_temp set temp_id = '0' where temp_id in (select temp_id from edata_custom_temp where table_name_ch like 'auto_数据拼盘%')
		"""
		action = {
			"操作": "TaskDataClear",
			"参数": {
				"查询条件": {
					"任务名称": "auto_数据拼盘任务"
				},
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 任务数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_EDataDataClear(self):
		u"""数据拼盘，二维表模式，数据清理"""
		action = {
			"操作": "EDataDataClear",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据拼盘，二维表模式，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_3_AddEDataTpl(self):
		u"""数据拼盘，添加二维表模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_二维表模式，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddEDataTpl(self):
		u"""数据拼盘，添加二维表模式，名称已存在"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_二维表模式，勿删"
			}
		}
		checks = """
		CheckMsg|表名已存在
		"""
		log.info('>>>>> 数据拼盘，添加二维表模式，名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_DeleteEDataTpl(self):
		u"""数据拼盘，删除二维表模式"""
		action = {
			"操作": "DeleteEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据拼盘，删除二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddEDataTpl(self):
		u"""数据拼盘，添加二维表模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_二维表模式，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_EDataSetCol(self):
		u"""数据拼盘，二维表模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "200"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列2",
						"列类型": "字符",
						"字符长度": "200"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列3",
						"列类型": "字符",
						"字符长度": "200"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_EDataConfigUpdateRule(self):
		u"""数据拼盘，二维表模式配置更新规则"""
		action = {
			"操作": "EDataConfigUpdateRule",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"取参指令": {
					"关键字": "auto_指令_date",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"指令解析模版": "auto_解析模板_解析date",
				"二维表结果绑定": [
					"列1",
					"列2",
					"列3"
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式配置更新规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddEDataTpl(self):
		u"""数据拼盘，添加二维表模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式2",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_二维表模式2，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_EDataSetCol(self):
		u"""数据拼盘，二维表模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式2",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "200"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列2",
						"列类型": "字符",
						"字符长度": "200"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列3",
						"列类型": "字符",
						"字符长度": "200"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_EDataConfigUpdateRule(self):
		u"""数据拼盘，二维表模式配置更新规则"""
		action = {
			"操作": "EDataConfigUpdateRule",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式2",
				"取参指令": {
					"关键字": "auto_指令_date",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"指令解析模版": "auto_解析模板_解析date",
				"二维表结果绑定": [
					"列1",
					"列2",
					"列3"
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式配置更新规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_EDataDataClear(self):
		u"""数据拼盘，列更新模式，数据清理"""
		action = {
			"操作": "EDataDataClear",
			"参数": {
				"模版类型": "列更新模式",
				"数据表名称": "auto_数据拼盘",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据拼盘，列更新模式，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_13_AddEDataTpl(self):
		u"""数据拼盘，添加列更新模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "列更新模式",
				"数据表名称": "auto_数据拼盘_列更新模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_列更新模式，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加列更新模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_EDataSetCol(self):
		u"""数据拼盘，列更新模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "列更新模式",
				"数据表名称": "auto_数据拼盘_列更新模式",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "200",
						"取参指令": {
							"关键字": "auto_指令_ping"
						},
						"指令解析模版": "auto_解析模板_列更新"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，列更新模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_EDataDataClear(self):
		u"""数据拼盘，分段模式，数据清理"""
		action = {
			"操作": "EDataDataClear",
			"参数": {
				"模版类型": "分段模式",
				"数据表名称": "auto_数据拼盘",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据拼盘，分段模式，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_16_AddEDataTpl(self):
		u"""数据拼盘，添加分段模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "分段模式",
				"数据表名称": "auto_数据拼盘_分段模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_分段模式，勿删",
				"取参指令": {
					"关键字": "auto_指令_ping"
				},
				"段开始特征行": {
					"设置方式": "选择",
					"正则模版名称": "auto_正则模版_time特征行"
				},
				"样例数据": "ping_sample.txt"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加分段模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_EDataSetCol(self):
		u"""数据拼盘，分段模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "分段模式",
				"数据表名称": "auto_数据拼盘_分段模式",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "200",
						"指令解析模版": "auto_解析模板_分段"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，分段模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_EDataDataClear(self):
		u"""数据拼盘，数据模式，数据清理"""
		action = {
			"操作": "EDataDataClear",
			"参数": {
				"模版类型": "数据模式",
				"数据表名称": "auto_数据拼盘",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据拼盘，数据模式，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_19_AddEDataTpl(self):
		u"""数据拼盘，添加数据模式"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "数据模式",
				"数据表名称": "auto_数据拼盘_数据模式",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据拼盘_数据模式，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加数据模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_EDataSetCol(self):
		u"""数据拼盘，数据模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "数据模式",
				"数据表名称": "auto_数据拼盘_数据模式",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "100"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列2",
						"列类型": "字符",
						"字符长度": "100"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列3",
						"列类型": "字符",
						"字符长度": "100"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列4",
						"列类型": "字符",
						"字符长度": "100"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列5",
						"列类型": "字符",
						"字符长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，数据模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddEDataTpl(self):
		u"""数据拼盘，添加数据模式，多数据类型列"""
		action = {
			"操作": "AddEDataTpl",
			"参数": {
				"模版类型": "数据模式",
				"数据表名称": "auto_数据模式_多数据类型",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"备注": "auto_数据模式_多数据类型，勿删"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加数据模式，多数据类型列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_EDataSetCol(self):
		u"""数据拼盘，数据模式添加列配置"""
		action = {
			"操作": "EDataSetCol",
			"参数": {
				"模版类型": "数据模式",
				"数据表名称": "auto_数据模式_多数据类型",
				"列配置": [
					{
						"操作类型": "添加",
						"列名(自定义)": "列1",
						"列类型": "字符",
						"字符长度": "100"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列2",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列3",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列4",
						"列类型": "文本"
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列5",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyyMMddHHmmss",
							""
						]
					},
					{
						"操作类型": "添加",
						"列名(自定义)": "列6",
						"列类型": "日期",
						"输入格式": [
							"自定义",
							"yyyy-MM-dd"
						],
						"输出格式": [
							"yyyyMMddHHmmss",
							""
						]
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，数据模式添加列配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_EDataDataClear(self):
		u"""数据拼盘，合并模式，数据清理"""
		action = {
			"操作": "EDataDataClear",
			"参数": {
				"模版类型": "合并模式",
				"数据表名称": "auto_数据拼盘",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据拼盘，合并模式，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_24_AddJoinEDataTpl(self):
		u"""数据拼盘，添加合并模式，join"""
		action = {
			"操作": "AddJoinEDataTpl",
			"参数": {
				"模版类型": "合并模式",
				"合并表名称": [
					"auto_数据拼盘_二维表模式",
					"auto_数据拼盘_二维表模式2"
				],
				"关联方式": "左关联",
				"左表配置": [
					{
						"列名": "网元名称",
						"合并后显示": "是",
						"关联列": "1"
					},
					{
						"列名": "指令内容",
						"合并后显示": "是"
					},
					{
						"列名": "列1",
						"合并后显示": "否"
					},
					{
						"列名": "列2",
						"合并后显示": "是"
					},
					{
						"列名": "列3",
						"合并后显示": "是"
					}
				],
				"右表配置": [
					{
						"列名": "网元名称",
						"合并后显示": "否",
						"关联列": "1"
					},
					{
						"列名": "列1",
						"合并后显示": "是"
					}
				],
				"数据表名称": "auto_数据拼盘_合并模式join",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"新表配置": [
					{
						"表名": "auto_数据拼盘_二维表模式",
						"原列名": "网元名称",
						"新列名": "netunit",
						"搜索条件": "是"
					},
					{
						"表名": "auto_数据拼盘_二维表模式",
						"原列名": "指令内容",
						"新列名": "command",
						"搜索条件": "是"
					},
					{
						"表名": "auto_数据拼盘_二维表模式",
						"原列名": "列2",
						"新列名": "col_2",
						"搜索条件": "是"
					},
					{
						"表名": "auto_数据拼盘_二维表模式",
						"原列名": "列3",
						"新列名": "col_3",
						"搜索条件": "是"
					},
					{
						"表名": "auto_数据拼盘_二维表模式2",
						"原列名": "列1",
						"新列名": "col_1",
						"搜索条件": "是"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加合并模式，join <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_AddUnionEDataTpl(self):
		u"""数据拼盘，添加合并模式，union"""
		action = {
			"操作": "AddUnionEDataTpl",
			"参数": {
				"模版类型": "合并模式",
				"合并表名称": [
					"auto_数据拼盘_二维表模式",
					"auto_数据拼盘_二维表模式2"
				],
				"关联方式": "UNION",
				"合并表配置": [
					{
						"表名": "auto_数据拼盘_二维表模式",
						"合并列": [
							"网元名称",
							"指令内容",
							"列1",
							"列2",
							"列3"
						]
					},
					{
						"表名": "auto_数据拼盘_二维表模式2",
						"合并列": [
							"网元名称",
							"指令内容",
							"列1",
							"列2",
							"列3"
						]
					}
				],
				"数据表名称": "auto_数据拼盘_合并模式union",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"新表配置": [
					{
						"原列名": "网元名称",
						"新列名": "netunit",
						"搜索条件": "是"
					},
					{
						"原列名": "指令内容",
						"新列名": "command",
						"搜索条件": "是"
					},
					{
						"原列名": "列1",
						"新列名": "col_1",
						"搜索条件": "是"
					},
					{
						"原列名": "列2",
						"新列名": "col_2",
						"搜索条件": "是"
					},
					{
						"原列名": "列3",
						"新列名": "col_3",
						"搜索条件": "是"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加合并模式，union <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddUnionEDataTpl(self):
		u"""数据拼盘，添加合并模式，union all"""
		action = {
			"操作": "AddUnionEDataTpl",
			"参数": {
				"模版类型": "合并模式",
				"合并表名称": [
					"auto_数据拼盘_二维表模式",
					"auto_数据拼盘_二维表模式2"
				],
				"关联方式": "UNION ALL",
				"合并表配置": [
					{
						"表名": "auto_数据拼盘_二维表模式",
						"合并列": [
							"网元名称",
							"指令内容",
							"列1",
							"列2",
							"列3"
						]
					},
					{
						"表名": "auto_数据拼盘_二维表模式2",
						"合并列": [
							"网元名称",
							"指令内容",
							"列1",
							"列2",
							"列3"
						]
					}
				],
				"数据表名称": "auto_数据拼盘_合并模式unionall",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"新表配置": [
					{
						"原列名": "网元名称",
						"新列名": "netunit",
						"搜索条件": "是"
					},
					{
						"原列名": "指令内容",
						"新列名": "command",
						"搜索条件": "是"
					},
					{
						"原列名": "列1",
						"新列名": "col_1",
						"搜索条件": "是"
					},
					{
						"原列名": "列2",
						"新列名": "col_2",
						"搜索条件": "是"
					},
					{
						"原列名": "列3",
						"新列名": "col_3",
						"搜索条件": "是"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，添加合并模式，union all <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_EDataUpdateStatus(self):
		u"""数据拼盘，启用二维表模式，未绑定网元"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|该模版未绑定网元，不能启动
		"""
		log.info('>>>>> 数据拼盘，启用二维表模式，未绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_EDataBindNE(self):
		u"""数据拼盘，二维表模式绑定网元"""
		action = {
			"操作": "EDataBindNE",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"网元列表": [
					{
						"网元名称": "${NetunitMME1}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME2}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME3}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_EDataBindNE(self):
		u"""数据拼盘，二维表模式绑定网元"""
		action = {
			"操作": "EDataBindNE",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式2",
				"网元列表": [
					{
						"网元名称": "${NetunitMME1}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME2}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME3}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，二维表模式绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_EDataBindNE(self):
		u"""数据拼盘，列更新模式绑定网元"""
		action = {
			"操作": "EDataBindNE",
			"参数": {
				"模版类型": "列更新模式",
				"数据表名称": "auto_数据拼盘_列更新模式",
				"网元列表": [
					{
						"网元名称": "${NetunitMME1}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME2}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME3}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，列更新模式绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_EDataBindNE(self):
		u"""数据拼盘，分段模式绑定网元"""
		action = {
			"操作": "EDataBindNE",
			"参数": {
				"模版类型": "分段模式",
				"数据表名称": "auto_数据拼盘_分段模式",
				"网元列表": [
					{
						"网元名称": "${NetunitMME1}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME2}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME3}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据拼盘，分段模式绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_EDataUpdateStatus(self):
		u"""数据拼盘，启用二维表模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_UpdateEDataTpl(self):
		u"""数据拼盘，二维表模式已启用，修改数据拼盘"""
		action = {
			"操作": "UpdateEDataTpl",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"修改内容": {
					"数据表名称": "auto_数据拼盘_二维表模式",
					"专业领域": [
						"AiSee",
						"auto域"
					],
					"备注": "auto_数据拼盘_二维表模式，勿删"
				}
			}
		}
		checks = """
		CheckMsg|请先禁用该模版后再修改
		"""
		log.info('>>>>> 数据拼盘，二维表模式已启用，修改数据拼盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_EDataBindNE(self):
		u"""数据拼盘，二维表模式已启用，绑定网元"""
		action = {
			"操作": "EDataBindNE",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"网元列表": [
					{
						"网元名称": "${NetunitMME1}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME2}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					},
					{
						"网元名称": "${NetunitMME3}",
						"网元分类": [
							"4G,4G_MME"
						],
						"厂家": "华为",
						"设备型号": "ME60"
					}
				]
			}
		}
		checks = """
		CheckMsg|请先禁用该模版后再修改
		"""
		log.info('>>>>> 数据拼盘，二维表模式已启用，绑定网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_EDataUpdateStatus(self):
		u"""数据拼盘，禁用二维表模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|禁用成功
		"""
		log.info('>>>>> 数据拼盘，禁用二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_EDataUpdateStatus(self):
		u"""数据拼盘，启用二维表模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_EDataUpdateStatus(self):
		u"""数据拼盘，启用二维表模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "二维表模式",
				"数据表名称": "auto_数据拼盘_二维表模式2",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_EDataUpdateStatus(self):
		u"""数据拼盘，启用列更新模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "列更新模式",
				"数据表名称": "auto_数据拼盘_列更新模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用列更新模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_EDataUpdateStatus(self):
		u"""数据拼盘，启用分段模式"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "分段模式",
				"数据表名称": "auto_数据拼盘_分段模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用分段模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_EDataUpdateStatus(self):
		u"""数据拼盘，启用合并模式，join"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "合并模式",
				"数据表名称": "auto_数据拼盘_合并模式join",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用合并模式，join <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_EDataUpdateStatus(self):
		u"""数据拼盘，启用合并模式，union"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "合并模式",
				"数据表名称": "auto_数据拼盘_合并模式union",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用合并模式，union <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_EDataUpdateStatus(self):
		u"""数据拼盘，启用合并模式，union all"""
		action = {
			"操作": "EDataUpdateStatus",
			"参数": {
				"模版类型": "合并模式",
				"数据表名称": "auto_数据拼盘_合并模式unionall",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用模版成功
		"""
		log.info('>>>>> 数据拼盘，启用合并模式，union all <<<<<')
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
