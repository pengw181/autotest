# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:08

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class TaskManager(unittest.TestCase):

	log.info("装载任务模版配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_TaskDataClear(self):
		u"""任务数据清理，删除历史数据"""
		action = {
			"操作": "TaskDataClear",
			"参数": {
				"查询条件": {
					"任务名称": "auto_"
				},
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 任务数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddTask(self):
		u"""添加任务，手动任务"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_date",
				"配置定时任务": "关闭",
				"任务说明": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|2|task_status|0|bind_task_id|${TemplID}|first_exec_date|null|interval_cyc|null|interval_unit|null|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，手动任务 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_UpdateTask(self):
		u"""修改任务，定时任务，按月"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "1",
						"间隔周期单位": "月"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|1|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，按月 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_UpdateTask(self):
		u"""修改任务，定时任务，按周"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "1",
						"间隔周期单位": "周"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|2|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，按周 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateTask(self):
		u"""修改任务，定时任务，按天"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "1",
						"间隔周期单位": "天"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，按天 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_UpdateTask(self):
		u"""修改任务，定时任务，按小时"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "12",
						"间隔周期单位": "小时"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|12|interval_unit|4|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，按小时 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateTask(self):
		u"""修改任务，定时任务，按分钟"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "30",
						"间隔周期单位": "分钟"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|30|interval_unit|5|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，按分钟 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateTask(self):
		u"""修改任务，定时任务，启用高级模式"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "开启",
						"Cron表达式": "0 0/30 9,18 * * ?"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|null|interval_unit|null|is_high|1|cron_exp|0 0/30 9,18 * * ?|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，启用高级模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateTask(self):
		u"""修改任务，定时任务，关闭高级模式"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "3",
						"间隔周期单位": "小时"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|3|interval_unit|4|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务，关闭高级模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateTask(self):
		u"""修改任务，定时任务改成手动任务"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "关闭",
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|2|task_status|0|bind_task_id|${TemplID}|first_exec_date|null|interval_cyc|null|interval_unit|null|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 修改任务，定时任务改成手动任务 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteTask(self):
		u"""删除任务，任务未启用"""
		action = {
			"操作": "DeleteTask",
			"参数": {
				"任务名称": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|0|task_name|auto_指令任务_date|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 删除任务，任务未启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddTask(self):
		u"""添加任务，指令任务：auto_指令任务_date"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_date",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，指令任务：auto_指令任务_date <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddTask(self):
		u"""添加任务，指令任务：auto_指令任务_指令带参数"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_指令带参数",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_指令带参数",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_指令任务_指令带参数"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_指令带参数' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_指令带参数|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_指令带参数|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，指令任务：auto_指令任务_指令带参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddTask(self):
		u"""添加任务，指令任务：auto_指令任务_组合指令"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_组合指令",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_组合指令",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_指令任务_组合指令"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_组合指令' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_组合指令|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_组合指令|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，指令任务：auto_指令任务_组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddTask(self):
		u"""添加任务，指令任务：auto_指令任务_多指令"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_多指令",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_多指令",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_指令任务_多指令"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_多指令' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_多指令|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_多指令|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，指令任务：auto_指令任务_多指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddTask(self):
		u"""添加任务，指令任务：auto_指令任务_按网元类型"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_指令任务_按网元类型",
				"模版类型": "指令任务",
				"绑定任务名称": "auto_指令模版_按网元类型",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_指令任务_按网元类型"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_按网元类型' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_按网元类型|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_按网元类型|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，指令任务：auto_指令任务_按网元类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_二维表模式"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_二维表模式",
				"模版类型": "数据拼盘任务",
				"绑定任务名称": "auto_数据拼盘_二维表模式",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_数据拼盘任务_二维表模式"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_二维表模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_二维表模式|task_temp_type|3|task_type|1|task_status|0|bind_task_id|${TempID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_二维表模式|trigger_user_id|null|register_status|0|interface_id|default-edata-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_分段模式"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_分段模式",
				"模版类型": "数据拼盘任务",
				"绑定任务名称": "auto_数据拼盘_分段模式",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_数据拼盘任务_分段模式"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_分段模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_分段模式|task_temp_type|3|task_type|1|task_status|0|bind_task_id|${TempID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_分段模式|trigger_user_id|null|register_status|0|interface_id|default-edata-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_分段模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_列更新模式"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_列更新模式",
				"模版类型": "数据拼盘任务",
				"绑定任务名称": "auto_数据拼盘_列更新模式",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "now",
					"高级模式": "关闭",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_数据拼盘任务_列更新模式"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_列更新模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_列更新模式|task_temp_type|3|task_type|1|task_status|0|bind_task_id|${TempID}|first_exec_date|now|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_列更新模式|trigger_user_id|null|register_status|0|interface_id|default-edata-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_列更新模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式join"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_合并模式join",
				"模版类型": "数据拼盘(合并表)任务",
				"绑定任务名称": "auto_数据拼盘_合并模式join",
				"配置定时任务": "关闭",
				"任务说明": "auto_数据拼盘任务_合并模式join"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_合并模式join' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_合并模式join|task_temp_type|4|task_type|2|task_status|0|bind_task_id|${TempID}|first_exec_date|null|interval_cyc|null|interval_unit|null|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_合并模式join|trigger_user_id|null|register_status|0|interface_id|default-edataMerge-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式join <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式union"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_合并模式union",
				"模版类型": "数据拼盘(合并表)任务",
				"绑定任务名称": "auto_数据拼盘_合并模式union",
				"配置定时任务": "关闭",
				"任务说明": "auto_数据拼盘任务_合并模式union"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_合并模式union' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_合并模式union|task_temp_type|4|task_type|2|task_status|0|bind_task_id|${TempID}|first_exec_date|null|interval_cyc|null|interval_unit|null|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_合并模式union|trigger_user_id|null|register_status|0|interface_id|default-edataMerge-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式union <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddTask(self):
		u"""添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式unionall"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_合并模式unionall",
				"模版类型": "数据拼盘(合并表)任务",
				"绑定任务名称": "auto_数据拼盘_合并模式unionall",
				"配置定时任务": "关闭",
				"任务说明": "auto_数据拼盘任务_合并模式unionall"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_合并模式unionall' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_合并模式unionall|task_temp_type|4|task_type|2|task_status|0|bind_task_id|${TempID}|first_exec_date|null|interval_cyc|null|interval_unit|null|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_合并模式unionall|trigger_user_id|null|register_status|0|interface_id|default-edataMerge-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加任务，数据拼盘任务：auto_数据拼盘任务_合并模式unionall <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_UpdateTaskStatus(self):
		u"""更新任务状态，启用"""
		action = {
			"操作": "UpdateTaskStatus",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|1|bind_task_id|${TemplID}|first_exec_date|notnull|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|0|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 更新任务状态，启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_UpdateTask(self):
		u"""修改任务，任务已启用"""
		action = {
			"操作": "UpdateTask",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"修改内容": {
					"任务名称": "auto_指令任务_date",
					"配置定时任务": "开启",
					"定时配置": {
						"首次执行时间": "now",
						"高级模式": "关闭",
						"间隔周期": "1",
						"间隔周期单位": "月"
					},
					"任务说明": "auto_指令任务_date"
				}
			}
		}
		checks = """
		CheckMsg|任务已经启用
		"""
		log.info('>>>>> 修改任务，任务已启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_DeleteTask(self):
		u"""删除任务，任务已启用"""
		action = {
			"操作": "DeleteTask",
			"参数": {
				"任务名称": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|任务已经启用
		"""
		log.info('>>>>> 删除任务，任务已启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_UpdateTaskStatus(self):
		u"""更新任务状态，禁用"""
		action = {
			"操作": "UpdateTaskStatus",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|0|bind_task_id|${TemplID}|first_exec_date|notnull|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|1|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 更新任务状态，禁用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_TriggerTask(self):
		u"""触发任务，任务未启用"""
		action = {
			"操作": "TriggerTask",
			"参数": {
				"任务名称": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|任务未启用
		"""
		log.info('>>>>> 触发任务，任务未启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_UpdateTaskStatus(self):
		u"""更新任务状态，启用"""
		action = {
			"操作": "UpdateTaskStatus",
			"参数": {
				"任务名称": "auto_指令任务_date",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select templ_id from tn_cmd_template_cfg_info where templ_name='auto_指令模版_date' and belong_id='${BelongID}' and domain_id='${DomainID}'|TemplID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_指令任务_date|task_temp_type|2|task_type|1|task_status|1|bind_task_id|${TemplID}|first_exec_date|notnull|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_指令任务_date|trigger_user_id|null|register_status|1|interface_id|default-cmdTempl-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 更新任务状态，启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_TriggerTask(self):
		u"""触发任务，任务已启用"""
		action = {
			"操作": "TriggerTask",
			"参数": {
				"任务名称": "auto_指令任务_date"
			}
		}
		checks = """
		CheckMsg|运行成功
		GetData|${Database}.main|select task_id from tn_task_man_conf_info where task_name='auto_指令任务_date' and domain_detail_id='${BelongID}_${DomainID}'|TaskID
		CheckData|${Database}.main.tn_task_man_run_inst_${YM}|1|task_id|${TaskID}|run_start_date|now|run_stop_date|now|inst_run_statu|1|task_type|2|run_log|参数正常异步方法|trigger_user_id|${LoginUser}|interface_url|${ThirdSystem}/CmdWorker/api/runTempletJobTaskManager|domain_detail_id|${BelongID}_${DomainID}|belong_id|${BelongID}
		"""
		log.info('>>>>> 触发任务，任务已启用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_UpdateTaskStatus(self):
		u"""启用数据拼盘任务"""
		action = {
			"操作": "UpdateTaskStatus",
			"参数": {
				"任务名称": "auto_数据拼盘任务_二维表模式",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_二维表模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_二维表模式|task_temp_type|3|task_type|1|task_status|1|bind_task_id|${TempID}|first_exec_date|notnull|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_二维表模式|trigger_user_id|null|register_status|notnull|interface_id|default-edata-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 启用数据拼盘任务 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_TriggerTask(self):
		u"""任务已启用，运行数据拼盘任务（register_status更新有延迟，应该是定时任务来更新）"""
		action = {
			"操作": "TriggerTask",
			"参数": {
				"任务名称": "auto_数据拼盘任务_二维表模式"
			}
		}
		checks = """
		CheckMsg|运行成功
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_二维表模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|TempID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_数据拼盘任务_二维表模式|task_temp_type|3|task_type|1|task_status|1|bind_task_id|${TempID}|first_exec_date|notnull|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_数据拼盘任务_二维表模式|trigger_user_id|${LoginUser}|register_status|notnull|interface_id|default-edata-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}
		GetData|${Database}.main|select task_id from tn_task_man_conf_info where task_name='auto_数据拼盘任务_二维表模式' and domain_detail_id='${BelongID}_${DomainID}'|TaskID
		CheckData|${Database}.main.tn_task_man_run_inst_${YM}|1|task_id|${TaskID}|run_start_date|now|run_stop_date|now|inst_run_statu|1|task_type|2|run_log|参数正常异步方法|trigger_user_id|${LoginUser}|interface_url|${ThirdSystem}/CmdWorker/api/runTempletJobTaskManager|domain_detail_id|${BelongID}_${DomainID}|belong_id|${BelongID}
		"""
		log.info('>>>>> 任务已启用，运行数据拼盘任务（register_status更新有延迟，应该是定时任务来更新） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_ProcessApproval(self):
		u"""流程提交审批"""
		action = {
			"操作": "ProcessApproval",
			"参数": {
				"流程名称": "auto_全流程"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 流程提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_UpdateProcessStatus(self):
		u"""流程审批通过，启用流程"""
		pres = """
		wait|60
		"""
		action = {
			"操作": "UpdateProcessStatus",
			"参数": {
				"流程名称": "auto_全流程",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用流程成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_全流程|is_alive|1|create_time|notnull|user_id|${LoginUser}|remark|auto_全流程说明|json|notnull|start_time|notnull|original_user_id|${LoginUser}|original_time|notnull|parent_process_id|-1|check_tag|20|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 流程审批通过，启用流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddTask(self):
		u"""添加流程任务"""
		action = {
			"操作": "AddTask",
			"参数": {
				"任务名称": "auto_流程任务_全流程",
				"模版类型": "流程任务",
				"绑定任务名称": "auto_全流程",
				"配置定时任务": "开启",
				"定时配置": {
					"首次执行时间": "2022-06-16 10:00:00",
					"间隔周期": "1",
					"间隔周期单位": "天"
				},
				"任务说明": "auto_流程任务_全流程"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_全流程' and belong_id='${BelongID}' and domain_id='${DomainID}'|ProcessID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_流程任务_全流程|task_temp_type|1|task_type|1|task_status|0|bind_task_id|${ProcessID}|first_exec_date|2022-06-16 10:00:00|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_流程任务_全流程|trigger_user_id|null|register_status|notnull|interface_id|default-workflow-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|now|domain_detail_id|${BelongID}_${DomainID}
		"""
		log.info('>>>>> 添加流程任务 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_UpdateTaskStatus(self):
		u"""启用流程任务"""
		action = {
			"操作": "UpdateTaskStatus",
			"参数": {
				"任务名称": "auto_流程任务_全流程",
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_全流程' and belong_id='${BelongID}' and domain_id='${DomainID}'|ProcessID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_流程任务_全流程|task_temp_type|1|task_type|1|task_status|1|bind_task_id|${ProcessID}|first_exec_date|2022-06-16 10:00:00|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_流程任务_全流程|trigger_user_id|null|register_status|notnull|interface_id|default-workflow-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}|updater|${LoginUser}|update_date|now
		"""
		log.info('>>>>> 启用流程任务 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_TriggerTask(self):
		u"""任务已启用，运行任务"""
		action = {
			"操作": "TriggerTask",
			"参数": {
				"任务名称": "auto_流程任务_全流程"
			}
		}
		checks = """
		Wait|10
		CheckMsg|运行成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_全流程' and belong_id='${BelongID}' and domain_id='${DomainID}'|ProcessID
		CheckData|${Database}.main.tn_task_man_conf_info|1|task_name|auto_流程任务_全流程|task_temp_type|1|task_type|1|task_status|1|bind_task_id|${ProcessID}|first_exec_date|2022-06-16 10:00:00|interval_cyc|1|interval_unit|3|is_high|0|cron_exp|null|task_desc|auto_流程任务_全流程|trigger_user_id|${LoginUser}|register_status|notnull|interface_id|default-workflow-${BelongID}_${DomainID}|user_id|${LoginUser}|create_date|notnull|domain_detail_id|${BelongID}_${DomainID}|updater|${LoginUser}|update_date|notnull
		GetData|${Database}.main|select task_id from tn_task_man_conf_info where task_name='auto_流程任务_全流程' and domain_detail_id='${BelongID}_${DomainID}'|TaskID
		CheckData|${Database}.main.tn_task_man_run_inst_${YM}|1|task_id|${TaskID}|run_start_date|now|run_stop_date|now|inst_run_statu|1|task_type|2|run_log|运行成功！|trigger_user_id|${LoginUser}|interface_url|${ThirdSystem}/aisee-workflow-server/process/runProcess|domain_detail_id|${BelongID}_${DomainID}|belong_id|${BelongID}
		"""
		log.info('>>>>> 任务已启用，运行任务 <<<<<')
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
