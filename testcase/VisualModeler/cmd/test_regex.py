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


class RegexTpl(unittest.TestCase):

	log.info("装载正则模版管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_RegexpDataClear(self):
		u"""正则模版管理,数据清理"""
		pres = """
		${Database}.main|delete from rulerx_regx_templ where regx_templ_name like 'auto_正则模版_%' and domain_id='${DomainID}' and belong_id='${BelongID}'
		"""
		action = {
			"操作": "RegexpDataClear",
			"参数": {
				"正则模版名称": "auto_正则模版_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 正则模版管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_匹配日期"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_匹配日期",
				"模版描述": "auto_正则模版_匹配日期，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "日期",
							"时间格式": "2014-05-28 12:30:00",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_匹配日期|regx_templ_desc|auto_正则模版_匹配日期，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_匹配日期 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_分段"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_分段",
				"模版描述": "auto_正则模版_分段，勿删",
				"正则魔方": {
					"高级模式": "是",
					"表达式": "time=(\\d+\\.?\\d*)\\s+ms"
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_分段|regx_templ_desc|auto_正则模版_分段，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_分段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_ping延迟时间"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_ping延迟时间",
				"模版描述": "auto_正则模版_ping延迟时间，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": "time=",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"匹配小数": "是",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "ms",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_ping延迟时间|regx_templ_desc|auto_正则模版_ping延迟时间，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_ping延迟时间 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_匹配数字"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_匹配数字",
				"模版描述": "auto_正则模版_匹配数字，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_匹配数字|regx_templ_desc|auto_正则模版_匹配数字，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_匹配数字 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_匹配逗号"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_匹配逗号",
				"模版描述": "auto_正则模版_匹配逗号，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": ",",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_匹配逗号|regx_templ_desc|auto_正则模版_匹配逗号，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_匹配逗号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_匹配成员文件名"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_匹配成员文件名",
				"模版描述": "auto_正则模版_匹配成员文件名，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": "成员-",
							"是否取值": "无"
						},
						{
							"标签": "任意中文字符",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_匹配成员文件名|regx_templ_desc|auto_正则模版_匹配成员文件名，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_匹配成员文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_获取丢包率"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_获取丢包率",
				"模版描述": "auto_正则模版_获取丢包率，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "任意非空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"长度": "1到多个",
							"匹配%": "是",
							"是否取值": "绿色"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "packet loss",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_获取丢包率|regx_templ_desc|auto_正则模版_获取丢包率，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_获取丢包率 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_time特征行"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_time特征行",
				"模版描述": "auto_正则模版_time特征行，勿删",
				"正则魔方": {
					"高级模式": "是",
					"表达式": "time=(\\d+\\.?\\d*)\\s+ms",
					"开启验证": "是",
					"样例数据": "ping_sample.txt"
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_time特征行|regx_templ_desc|auto_正则模版_time特征行，勿删|regx_json|notnull|sample_data|notnull|match_result|notnull|creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_time特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_password"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_password",
				"模版描述": "auto_正则模版_password，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "字母",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "字母",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": ":",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "绿色"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_password|regx_templ_desc|auto_正则模版_password，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_password <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_measInfoId段开始"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_measInfoId段开始",
				"模版描述": "auto_正则模版_measInfoId段开始，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": "measInfo measInfoId=\"",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "\"",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_measInfoId段开始|regx_templ_desc|auto_正则模版_measInfoId段开始，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_measInfoId段开始 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_measInfoId段结束"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_measInfoId段结束",
				"模版描述": "auto_正则模版_measInfoId段结束，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": "</measInfo>",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_measInfoId段结束|regx_templ_desc|auto_正则模版_measInfoId段结束，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_measInfoId段结束 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_数字中文"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_数字中文",
				"模版描述": "auto_正则模版_数字中文，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "任意中文字符",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_数字中文|regx_templ_desc|auto_正则模版_数字中文，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_数字中文 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_数字中文带后缀"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_数字中文带后缀",
				"模版描述": "auto_正则模版_数字中文带后缀，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "任意中文字符",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": ".xls",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_数字中文带后缀|regx_templ_desc|auto_正则模版_数字中文带后缀，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_数字中文带后缀 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_匹配清洗日志"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_匹配清洗日志",
				"模版描述": "auto_正则模版_匹配清洗日志，勿删",
				"正则魔方": {
					"高级模式": "是",
					"表达式": "(\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d,\\d{3})\\s+-\\s+(\\S+)\\s+-\\s+(\\S+)\\s+-\\s+(.+)"
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_匹配清洗日志|regx_templ_desc|auto_正则模版_匹配清洗日志，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_匹配清洗日志 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_横杠拆分符"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_横杠拆分符",
				"模版描述": "auto_正则模版_横杠拆分符，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "-",
							"是否取值": "无"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_横杠拆分符|regx_templ_desc|auto_正则模版_横杠拆分符，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_横杠拆分符 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_清洗结束符"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_清洗结束符",
				"模版描述": "auto_正则模版_清洗结束符，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "本周期实例执行完成，休眠等待下一个运行周期",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_清洗结束符|regx_templ_desc|auto_正则模版_清洗结束符，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_清洗结束符 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_查看Slab"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_查看Slab",
				"模版描述": "auto_正则模版_查看Slab，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "数字",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "kB",
							"是否取值": "绿色"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_查看Slab|regx_templ_desc|auto_正则模版_查看Slab，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_查看Slab <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_内存利用率"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_内存利用率",
				"模版描述": "auto_正则模版_内存利用率，勿删",
				"正则魔方": {
					"高级模式": "是",
					"表达式": "(.+):\\s+(\\d+)\\s+(\\d+)\\s+(\\d+)\\s*(\\d*)\\s*(\\d*)\\s*(\\d*)\\s*",
					"开启验证": "是",
					"样例数据": "free_sample.txt"
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_内存利用率|regx_templ_desc|auto_正则模版_内存利用率，勿删|regx_json|notnull|sample_data|notnull|match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_内存利用率 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_cpu空闲率值提取"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_cpu空闲率值提取",
				"模版描述": "auto_正则模版_cpu空闲率值提取，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "自定义文本",
							"自定义值": "Cpu(s)",
							"是否取值": "无"
						},
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": ",",
							"是否取值": "无"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "无"
						},
						{
							"标签": "数字",
							"匹配小数": "是",
							"长度": "1到多个",
							"是否取值": "黄色"
						},
						{
							"标签": "空格",
							"长度": "0到多个",
							"是否取值": "无"
						},
						{
							"标签": "自定义文本",
							"自定义值": "id,",
							"是否取值": "无"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_cpu空闲率值提取|regx_templ_desc|auto_正则模版_cpu空闲率值提取，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_cpu空闲率值提取 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddRegexpTemp(self):
		u"""添加正则模版，auto_正则模版_清洗ping指令"""
		action = {
			"操作": "AddRegexpTemp",
			"参数": {
				"正则模版名称": "auto_正则模版_清洗ping指令",
				"模版描述": "auto_正则模版_清洗ping指令，勿删",
				"正则魔方": {
					"标签配置": [
						{
							"标签": "任意字符",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": "time=",
							"是否取值": "绿色"
						},
						{
							"标签": "数字",
							"匹配小数": "是",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "空格",
							"长度": "1到多个",
							"是否取值": "绿色"
						},
						{
							"标签": "自定义文本",
							"自定义值": "ms",
							"是否取值": "绿色"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|正则模版保存成功
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|auto_正则模版_清洗ping指令|regx_templ_desc|auto_正则模版_清洗ping指令，勿删|regx_json|notnull|sample_data||match_result||creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|regx_expr|notnull
		"""
		log.info('>>>>> 添加正则模版，auto_正则模版_清洗ping指令 <<<<<')
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
