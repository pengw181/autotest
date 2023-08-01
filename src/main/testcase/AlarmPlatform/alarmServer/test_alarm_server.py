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


class AlarmServerConfig(unittest.TestCase):

	log.info("装载执行告警测试用例")
	worker = CaseWorker()
	case = CaseEngine(worker=worker)
	case.load(case_file="/告警服务/执行告警.xls")

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_BatchEnableRule(self):
		u"""启用所有告警规则"""
		action = {
			"操作": "BatchEnableRule",
			"参数": {
				"查询条件": {
					"告警规则名称": "auto_告警规则"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 启用所有告警规则 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_mysql同比"""
		pres = """
		${DatabaseM}.sso|update pw_agg_table set col_3 = now() - interval 1 day where 1=1
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_mysql同比",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_mysql同比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_mysql环比"""
		pres = """
		${DatabaseM}.sso|update pw_agg_table set col_3 = now() - interval 1 day where 1=1
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_mysql环比",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_mysql环比 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_流程运行结果"""
		pres = """
		${Database}.main|update p_result_obj_info set DATA_TIME = now()::timestamp + interval '8 hour' where 1=1||continue
		${Database}.main|update p_result_obj_info set DATA_TIME = now()-1/24 where 1=1||continue
		${Database}.main|update p_result_obj_info set DATA_TIME = sysdate - interval '1' minute where 1=1||continue
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_流程运行结果",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_流程运行结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_网元其它资料表"""
		pres = """
		${Database}.main|update ${AlarmTableName} set update_date = now()::timestamp + interval '8 hour' where 1=1||continue
		${Database}.main|update ${AlarmTableName} set update_date = now()-1/24 where 1=1||continue
		${Database}.main|update ${AlarmTableName} set update_date = sysdate - interval '1' minute where 1=1||continue
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_网元其它资料表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_网元其它资料表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_SetDefaultMsgTemplate(self):
		u"""设置告警规则"auto_告警规则_oracle告警表"默认消息模版"""
		action = {
			"操作": "SetDefaultMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版_oracle告警表",
				"默认模版": "是"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置告警规则"auto_告警规则_oracle告警表"默认消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_oracle告警表"""
		pres = """
		${DatabaseO}.sso|update pw_alarm_table set col_4 = sysdate-1/24/12 where 1=1
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_oracle告警表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_oracle告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_SetDefaultMsgTemplate(self):
		u"""取消设置告警规则"auto_告警规则_oracle告警表"默认消息模版"""
		action = {
			"操作": "SetDefaultMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版_oracle告警表",
				"默认模版": "否"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 取消设置告警规则"auto_告警规则_oracle告警表"默认消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_SetDefaultMsgTemplate(self):
		u"""设置告警规则"auto_消息模版_启用共字典"默认消息模版"""
		action = {
			"操作": "SetDefaultMsgTemplate",
			"参数": {
				"消息模版名称": "auto_消息模版_启用共字典",
				"默认模版": "是"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置告警规则"auto_消息模版_启用共字典"默认消息模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_RedoAlarmRule(self):
		u"""重调告警规则：auto_告警规则_oracle告警表"""
		pres = """
		${DatabaseO}.sso|update pw_alarm_table set col_4 = sysdate-1/24/12 where 1=1
		"""
		action = {
			"操作": "RedoAlarmRule",
			"参数": {
				"告警规则名称": "auto_告警规则_oracle告警表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警规则：auto_告警规则_oracle告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_RedoAlarmPlan(self):
		u"""重调告警计划：auto_告警计划_mysql多字段类型表"""
		pres = """
		${DatabaseM}.sso|update pw_agg_table set col_3 = now() - interval 1 day where 1=1
		"""
		action = {
			"操作": "RedoAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_mysql多字段类型表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警计划：auto_告警计划_mysql多字段类型表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_RedoAlarmPlan(self):
		u"""重调告警计划：auto_告警计划_流程运行结果"""
		pres = """
		${Database}.main|update p_result_obj_info set DATA_TIME = now()::timestamp + interval '8 hour' where 1=1||continue
		${Database}.main|update p_result_obj_info set DATA_TIME = now()-1/24 where 1=1||continue
		${Database}.main|update p_result_obj_info set DATA_TIME = sysdate - interval '1' minute where 1=1||continue
		"""
		action = {
			"操作": "RedoAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_流程运行结果",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警计划：auto_告警计划_流程运行结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_RedoAlarmPlan(self):
		u"""重调告警计划：auto_告警计划_网元其它资料告警表"""
		pres = """
		${Database}.main|update ${AlarmTableName} set update_date = now()::timestamp + interval '8 hour' where 1=1||continue
		${Database}.main|update ${AlarmTableName} set update_date = now()-1/24 where 1=1||continue
		${Database}.main|update ${AlarmTableName} set update_date = sysdate - interval '1' minute where 1=1||continue
		"""
		action = {
			"操作": "RedoAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_网元其它资料告警表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警计划：auto_告警计划_网元其它资料告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_RedoAlarmPlan(self):
		u"""重调告警计划：auto_告警计划_oracle告警表"""
		pres = """
		${DatabaseO}.sso|update pw_alarm_table set col_4 = sysdate-1/24/12 where 1=1
		"""
		action = {
			"操作": "RedoAlarmPlan",
			"参数": {
				"告警计划名称": "auto_告警计划_oracle告警表",
				"开始时间": {
					"间隔": "-1",
					"单位": "天"
				},
				"结束时间": {
					"间隔": "1",
					"单位": "天"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 重调告警计划：auto_告警计划_oracle告警表 <<<<<')
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
