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


class SendPlanConfig(unittest.TestCase):

	log.info("装载推送计划测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/推送计划/推送计划.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_SendPlanDataClear(self):
		u"""推送计划，数据清理"""
		pres = """
		${Database}.alarm|delete from alarm_send_plan where send_plan_name like 'auto_推送计划%' and is_delete_tag='1'
		"""
		action = {
			"操作": "SendPlanDataClear",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 推送计划，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddSendPlan(self):
		u"""添加推送计划"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "AddSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"推送类型": [
					"微信",
					"短信",
					"邮件"
				],
				"消息模版": "auto_消息模版_网元其它资料表",
				"接收对象": {
					"接收类型": "用户",
					"接收人": [
						"${TreeUser}"
					]
				},
				"推送日期": [
					"周一",
					"周二",
					"周三",
					"周四",
					"周五",
					"周六",
					"周日"
				],
				"有效开始日期": "2020-01-01",
				"有效结束日期": "2099-12-31",
				"有效开始时段": "08:00:00",
				"有效结束时段": "17:59:59",
				"备注": "auto_推送计划_备注"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|1,2,3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3,4,5,6,7|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 添加推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddSendPlan(self):
		u"""添加推送计划，推送计划名称已存在"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "AddSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"推送类型": [
					"微信",
					"短信",
					"邮件"
				],
				"消息模版": "auto_消息模版_网元其它资料表",
				"接收对象": {
					"接收类型": "用户",
					"接收人": [
						"${TreeUser}"
					]
				},
				"推送日期": [
					"周一",
					"周二",
					"周三",
					"周四",
					"周五",
					"周六",
					"周日"
				],
				"有效开始日期": "2020-01-01",
				"有效结束日期": "2099-12-31",
				"有效开始时段": "08:00:00",
				"有效结束时段": "17:59:59",
				"备注": "auto_推送计划_备注"
			}
		}
		checks = """
		CheckMsg|推送计划名称重复
		"""
		log.info('>>>>> 添加推送计划，推送计划名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_UpdateSendPlan(self):
		u"""修改推送计划，修改推送类型"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3,4,5,6,7|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改推送类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateSendPlan(self):
		u"""修改推送计划，修改消息模版"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					],
					"消息模版": "auto_消息模版_流程运行结果"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3,4,5,6,7|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_UpdateSendPlan(self):
		u"""修改推送计划，修改接收对象，接收类型为组织，非叶子节点"""
		pres = """
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select string_agg(org_id, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_id from tn_org where org_name='${TreeOrg1}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select group_concat(org_id order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_id from tn_org where org_name='${TreeOrg1}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select listagg(org_id, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_id from tn_org where org_name='${TreeOrg1}') end from dual|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select string_agg(org_name, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_name from tn_org where org_name='${TreeOrg1}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select group_concat(org_name order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_name from tn_org where org_name='${TreeOrg1}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) then (select listagg(org_name, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg1}')) else (select org_name from tn_org where org_name='${TreeOrg1}') end from dual|ReceiveObjectName|continue
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					],
					"消息模版": "auto_消息模版_流程运行结果",
					"接收对象": {
						"接收类型": "组织",
						"接收人": [
							"${TreeOrg1}"
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|2|send_date|1,2,3,4,5,6,7|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改接收对象，接收类型为组织，非叶子节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateSendPlan(self):
		u"""修改推送计划，修改接收对象，接收类型为组织，叶子节点"""
		pres = """
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_id, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_id order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_id, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_name, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_name order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_name, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObjectName|continue
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					],
					"消息模版": "auto_消息模版_流程运行结果",
					"接收对象": {
						"接收类型": "组织",
						"接收人": [
							"${TreeOrg2}"
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|2|send_date|1,2,3,4,5,6,7|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改接收对象，接收类型为组织，叶子节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateSendPlan(self):
		u"""修改推送计划，修改推送日期"""
		pres = """
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_id, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_id order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_id, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_name, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_name order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_name, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObjectName|continue
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					],
					"消息模版": "auto_消息模版_流程运行结果",
					"接收对象": {
						"接收类型": "组织",
						"接收人": [
							"${TreeOrg2}"
						]
					},
					"推送日期": [
						"周一",
						"周二",
						"周三"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|2|send_date|1,2,3|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|17:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改推送日期 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateSendPlan(self):
		u"""修改推送计划，修改有效时间"""
		pres = """
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_id, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_id order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_id, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_name, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_name order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_name, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObjectName|continue
		"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划2",
					"推送类型": [
						"邮件"
					],
					"消息模版": "auto_消息模版_流程运行结果",
					"接收对象": {
						"接收类型": "组织",
						"接收人": [
							"${TreeOrg2}"
						]
					},
					"推送日期": [
						"周一",
						"周二",
						"周三"
					],
					"有效开始日期": "2022-01-01",
					"有效结束日期": "2059-12-31",
					"有效开始时段": "09:00:00",
					"有效结束时段": "10:59:59",
					"备注": "auto_推送计划2_备注"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划2|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|2|send_date|1,2,3|effect_start_date|2022-01-01|effect_end_date|2059-12-31|send_start_time|09:00:00|send_end_time|10:59:59|remark|auto_推送计划2_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 修改推送计划，修改有效时间 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_DeleteSendPlan(self):
		u"""删除推送计划"""
		pres = """
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_id, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_id order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_id, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_id from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObject|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select string_agg(org_name, ',' order by convert_to(org_name, 'gbk')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select group_concat(org_name order by convert(org_name using gbk) separator ',') from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end|ReceiveObjectName|continue
		${Database}.sso|select case when exists(select org_name from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) then (select listagg(org_name, ',') within group(order by NLSSORT(org_name, 'NLS_SORT=SCHINESE_PINYIN_M')) from tn_org where p_org_id = (select org_id from tn_org where org_name = '${TreeOrg2}')) else (select org_name from tn_org where org_name='${TreeOrg2}') end from dual|ReceiveObjectName|continue
		"""
		action = {
			"操作": "DeleteSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划2"
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_流程运行结果' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划2|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|2|send_date|1,2,3|effect_start_date|2022-01-01|effect_end_date|2059-12-31|send_start_time|09:00:00|send_end_time|10:59:59|remark|auto_推送计划2_备注|send_plan_status|0|is_delete_tag|1|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull
		"""
		log.info('>>>>> 删除推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddSendPlan(self):
		u"""添加推送计划"""
		pres = """
		${Database}.alarm|delete from alarm_send_plan where send_plan_name like 'auto_推送计划%'
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "AddSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"推送类型": [
					"邮件"
				],
				"消息模版": "auto_消息模版_网元其它资料表",
				"接收对象": {
					"接收类型": "用户",
					"接收人": [
						"${TreeUser}"
					]
				},
				"推送日期": [
					"周一",
					"周二",
					"周三"
				],
				"有效开始日期": "2020-01-01",
				"有效结束日期": "2099-12-31",
				"有效开始时段": "08:00:00",
				"有效结束时段": "08:59:59",
				"备注": "auto_推送计划_备注"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|08:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|now|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 添加推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_UpdateSendPlanStatus(self):
		u"""启用推送计划"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "UpdateSendPlanStatus",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|08:59:59|remark|auto_推送计划_备注|send_plan_status|1|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull
		"""
		log.info('>>>>> 启用推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_UpdateSendPlan(self):
		u"""推送计划已启用，修改推送计划"""
		action = {
			"操作": "UpdateSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"修改内容": {
					"推送计划名称": "auto_推送计划",
					"推送类型": [
						"邮件"
					]
				}
			}
		}
		checks = """
		CheckMsg|不允许修改启用状态的推送计划
		"""
		log.info('>>>>> 推送计划已启用，修改推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_DeleteSendPlan(self):
		u"""推送计划已启用，删除推送计划"""
		action = {
			"操作": "DeleteSendPlan",
			"参数": {
				"推送计划名称": "auto_推送计划"
			}
		}
		checks = """
		CheckMsg|不允许删除启用状态的推送计划
		"""
		log.info('>>>>> 推送计划已启用，删除推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UpdateSendPlanStatus(self):
		u"""禁用推送计划"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "UpdateSendPlanStatus",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|08:59:59|remark|auto_推送计划_备注|send_plan_status|0|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull
		"""
		log.info('>>>>> 禁用推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UpdateSendPlanStatus(self):
		u"""启用推送计划"""
		pres = """
		${Database}.sso|select concat('u', user_id) from tn_user where user_name='${TreeUser}' and is_alive='1'|ReceiveObject
		${Database}.sso|select user_name from sso.tn_user where user_name = '${TreeUser}' and is_alive='1'|ReceiveObjectName
		"""
		action = {
			"操作": "UpdateSendPlanStatus",
			"参数": {
				"推送计划名称": "auto_推送计划",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.alarm|select message_template_id from alarm_message_template where template_name='auto_消息模版_网元其它资料表' and is_delete_tag='0'|MessageTemplateID
		CheckData|${Database}.alarm.alarm_send_plan|1|send_plan_name|auto_推送计划|send_type|3|message_template_id|${MessageTemplateID}|receive_object|${ReceiveObject}|receive_object_name|${ReceiveObjectName}|receive_object_type|1|send_date|1,2,3|effect_start_date|2020-01-01|effect_end_date|2099-12-31|send_start_time|08:00:00|send_end_time|08:59:59|remark|auto_推送计划_备注|send_plan_status|1|is_delete_tag|0|creator|${LoginUser}|create_date|notnull|updater|${LoginUser}|update_date|notnull
		"""
		log.info('>>>>> 启用推送计划 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
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
