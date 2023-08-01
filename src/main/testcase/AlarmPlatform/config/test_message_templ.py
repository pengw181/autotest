# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/07/31 PM06:41

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.case import CaseEngine
from src.main.python.lib.screenShot import saveScreenShot


class MessageTemplConfig(unittest.TestCase):

	log.info("装载消息模版测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警配置/消息模版.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_MsgTemplateDataClear(self):
		u"""消息模版配置数据清理"""
		action = {
			"操作": "MsgTemplateDataClear",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 消息模版配置数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddMsgTemplate(self):
		u"""添加消息模版，配置正确"""
		pres = """
		${Database}.alarm|delete from alarm_message_template where template_name like 'auto_消息模版%' and is_delete_tag=1
		"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则",
				"消息模版名称": "auto_消息模版",
				"模版标题": "auto_消息模版标题",
				"消息模版描述": "auto_消息模版描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "网元名称："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_info"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，指令结果："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_result"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，网元状态："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_status"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，说明："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_desc"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				],
				"模版输入": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|1|is_delete_tag|0|template_state|2|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|modify_date|now
		"""
		log.info('>>>>> 添加消息模版，配置正确 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_UpdateMsgTemplateStatus(self):
		u"""启用消息模版"""
		action = {
			"操作": "UpdateMsgTemplateStatus",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|1|is_delete_tag|0|template_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|now
		"""
		log.info('>>>>> 启用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_UpdateMsgTemplate(self):
		u"""修改已启用的消息模版"""
		action = {
			"操作": "UpdateMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"修改内容": {
					"消息模版名称": "auto_消息模版_高级模式",
					"模版标题": "auto_消息模版_高级模式标题",
					"消息模版描述": "auto_消息模版_高级模式描述",
					"配置模式": "高级模式",
					"模版输入": "网元名称：${obj_info}，指令结果：${obj_result}，状态：${obj_status}，备注：{obj_desc}"
				}
			}
		}
		checks = """
		CheckMsg|请先禁用，再修改消息模版
		"""
		log.info('>>>>> 修改已启用的消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateMsgTemplateStatus(self):
		u"""禁用消息模版"""
		action = {
			"操作": "UpdateMsgTemplateStatus",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|0|is_delete_tag|0|template_state|2|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|notnull
		"""
		log.info('>>>>> 禁用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_SetDefaultMsgTemplate(self):
		u"""选择已禁用的消息模版，设置为默认模版"""
		action = {
			"操作": "SetDefaultMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"默认模版": "是"
			}
		}
		checks = """
		CheckMsg|模版已禁用，不能设置为默认消息模版
		"""
		log.info('>>>>> 选择已禁用的消息模版，设置为默认模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateMsgTemplate(self):
		u"""修改消息模版，使用高级模式"""
		action = {
			"操作": "UpdateMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"修改内容": {
					"消息模版名称": "auto_消息模版_高级模式",
					"模版标题": "auto_消息模版_高级模式标题",
					"消息模版描述": "auto_消息模版_高级模式描述",
					"配置模式": "高级模式",
					"模版输入": "网元名称：${obj_info}，指令结果：${obj_result}，状态：${obj_status}，备注：{obj_desc}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版_高级模式|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版_高级模式标题|alarm_desc|auto_消息模版_高级模式描述|design_content|{"source":"网元名称：@#basehhddata#@，指令结果：@#basehhddata#@，状态：@#basehhddata#@，备注：{obj_desc}","baseList":[{"obj_info":{"tag":"field","isTranslate":false,"chineseName":"obj_info"}},{"obj_result":{"tag":"field","isTranslate":false,"chineseName":"obj_result"}},{"obj_status":{"tag":"field","isTranslate":false,"chineseName":"obj_status"}}],"dicList":[]}|config_model_type|2|is_default|1|is_delete_tag|0|template_state|2|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|notnull
		"""
		log.info('>>>>> 修改消息模版，使用高级模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateMsgTemplateStatus(self):
		u"""启用消息模版"""
		action = {
			"操作": "UpdateMsgTemplateStatus",
			"参数": {
				"消息模版名称": "auto_消息模版_高级模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版_高级模式|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版_高级模式标题|alarm_desc|auto_消息模版_高级模式描述|design_content|{"source":"网元名称：@#basehhddata#@，指令结果：@#basehhddata#@，状态：@#basehhddata#@，备注：{obj_desc}","baseList":[{"obj_info":{"tag":"field","isTranslate":false,"chineseName":"obj_info"}},{"obj_result":{"tag":"field","isTranslate":false,"chineseName":"obj_result"}},{"obj_status":{"tag":"field","isTranslate":false,"chineseName":"obj_status"}}],"dicList":[]}|config_model_type|2|is_default|1|is_delete_tag|0|template_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|notnull
		"""
		log.info('>>>>> 启用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddMsgTemplate(self):
		u"""同一个告警规则下，添加多个消息模版"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则",
				"消息模版名称": "auto_消息模版",
				"模版标题": "auto_消息模版标题",
				"消息模版描述": "auto_消息模版描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "网元名称："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_info"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，指令结果："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_result"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，网元状态："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_status"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "，说明："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_desc"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				],
				"模版输入": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|0|is_delete_tag|0|template_state|2|creator|${LoginUser}|create_date|now|modifier|${LoginUser}|modify_date|now
		"""
		log.info('>>>>> 同一个告警规则下，添加多个消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateMsgTemplateStatus(self):
		u"""启用消息模版"""
		action = {
			"操作": "UpdateMsgTemplateStatus",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|0|is_delete_tag|0|template_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|now
		"""
		log.info('>>>>> 启用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_SetDefaultMsgTemplate(self):
		u"""选择已启用的消息模版，设置为默认模版"""
		action = {
			"操作": "SetDefaultMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版",
				"默认模版": "是"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select alarm_rule_id from alarm_rule_info where alarm_rule_name='auto_告警规则' and is_delete_tag=0|AlarmRuleID
		CheckData|${Database}.alarm.alarm_message_template|1|template_name|auto_消息模版|alarm_rule_id|${AlarmRuleID}|template_subject|auto_消息模版标题|alarm_desc|auto_消息模版描述|design_content|[{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"网元名称："}},{"obj_info":{"tag":"field","fieldChineseName":"obj_info","fieldEnglishName":"obj_info"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，指令结果："}},{"obj_result":{"tag":"field","fieldChineseName":"obj_result","fieldEnglishName":"obj_result"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，网元状态："}},{"obj_status":{"tag":"field","fieldChineseName":"obj_status","fieldEnglishName":"obj_status"}},{"comCustomText":{"tag":"common","fieldChineseName":"自定义文本","fieldEnglishName":"comCustomText","chineseName":"，说明："}},{"obj_desc":{"tag":"field","fieldChineseName":"obj_desc","fieldEnglishName":"obj_desc"}},{"comNewLine":{"tag":"common","fieldChineseName":"换行","fieldEnglishName":"comNewLine"}}]|config_model_type|1|is_default|1|is_delete_tag|0|template_state|1|creator|${LoginUser}|create_date|notnull|modifier|${LoginUser}|modify_date|now
		"""
		log.info('>>>>> 选择已启用的消息模版，设置为默认模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_mysql同比"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_mysql同比",
				"消息模版名称": "auto_消息模版_mysql同比",
				"模版标题": "auto_消息模版_mysql同比标题",
				"消息模版描述": "auto_消息模版_mysql同比描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "结果标签",
						"标签名称": "最大值"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_mysql同比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_mysql环比"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_mysql环比",
				"消息模版名称": "auto_消息模版_mysql环比",
				"模版标题": "auto_消息模版_mysql环比标题",
				"消息模版描述": "auto_消息模版_mysql环比描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "结果标签",
						"标签名称": "最大值"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_mysql环比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_oracle告警表"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_oracle告警表",
				"消息模版名称": "auto_消息模版_oracle告警表",
				"模版标题": "auto_消息模版_oracle告警表标题",
				"消息模版描述": "auto_消息模版_oracle告警表描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列1："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_1"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列2："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_2"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列3："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_3"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列4："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_4"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_oracle告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_流程运行结果"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_流程运行结果",
				"消息模版名称": "auto_消息模版_流程运行结果",
				"模版标题": "auto_消息模版_流程运行结果标题",
				"消息模版描述": "auto_消息模版_流程运行结果描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "网元名称："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_info"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "异常状态："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_result"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "业务状态："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "obj_status"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "生成时间："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "data_time"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_流程运行结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_网元其它资料表"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_网元其它资料表",
				"消息模版名称": "auto_消息模版_网元其它资料表",
				"模版标题": "auto_消息模版_网元其它资料表标题",
				"消息模版描述": "auto_消息模版_网元其它资料表描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列2："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_2"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列3："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_3"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "时间："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "UPDATE_DATE"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_网元其它资料表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_日表"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_日表",
				"消息模版名称": "auto_消息模版_日表",
				"模版标题": "auto_消息模版_日表标题",
				"消息模版描述": "auto_消息模版_日表描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列1："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_1"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列2："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_2"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列3："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_3"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列4："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_4"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_日表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_MAX"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_MAX",
				"消息模版名称": "auto_消息模版_MAX",
				"模版标题": "auto_消息模版_MAX标题",
				"消息模版描述": "auto_消息模版_MAX描述",
				"配置模式": "标签模式",
				"结果标签": [],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列1："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_1"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列3："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "col_3"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "最大值："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "最大值"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_MAX <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddMsgTemplate(self):
		u"""添加消息模版：auto_消息模版_oracle告警表，启用字典，公共字典"""
		action = {
			"操作": "AddMsgTemplate",
			"参数": {
				"告警规则名称": "auto_告警规则_oracle告警表",
				"消息模版名称": "auto_消息模版_启用共字典",
				"模版标题": "auto_消息模版_启用共字典标题",
				"消息模版描述": "auto_消息模版_启用共字典描述",
				"配置模式": "标签模式",
				"结果标签": [
					[
						"COL_2",
						"auto_字典_公共字典"
					]
				],
				"模版配置": [
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列1："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_1"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列2："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_2",
						"已配置": "是"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列3："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_3"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "自定义文本",
						"自定义值": "列4："
					},
					{
						"标签类型": "结果标签",
						"标签名称": "COL_4"
					},
					{
						"标签类型": "公共标签",
						"标签名称": "换行"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加消息模版：auto_消息模版_oracle告警表，启用字典，公共字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_BatchEnableMsgTemplate(self):
		u"""批量启用消息模版"""
		action = {
			"操作": "BatchEnableMsgTemplate",
			"参数": {
				"查询条件": {
					"消息模版名称": "auto_消息模版"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量启用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_BatchDisableMsgTemplate(self):
		u"""批量禁用消息模版"""
		action = {
			"操作": "BatchDisableMsgTemplate",
			"参数": {
				"查询条件": {
					"消息模版名称": "auto_消息模版"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量禁用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_BatchEnableMsgTemplate(self):
		u"""批量启用消息模版"""
		action = {
			"操作": "BatchEnableMsgTemplate",
			"参数": {
				"查询条件": {
					"消息模版名称": "auto_消息模版"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 批量启用消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
