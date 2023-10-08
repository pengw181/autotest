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


class SqlNodePart2(unittest.TestCase):

	log.info("装载sql节点测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeBusinessConf(self):
		u"""配置数据库节点,对网元其它资料表执行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元其它资料表执行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${OtherInfoTableName} set is_delete=0 where col_2='时间'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元其它资料表执行update'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|update ${OtherInfoTableName} set is_delete=0 where col_2='时间'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元其它资料表执行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_NodeBusinessConf(self):
		u"""配置数据库节点,对网元其它资料表执行truncate"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元其它资料表执行truncate",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "truncate table ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元其它资料表执行truncate'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|truncate table ${OtherInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元其它资料表执行truncate <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_NodeBusinessConf(self):
		u"""配置数据库节点,对网元其它资料表执行drop"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元其它资料表执行drop",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元其它资料表执行drop'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|drop table ${OtherInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元其它资料表执行drop <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘二维表模式表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘二维表模式表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${Edata1TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘二维表模式表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${Edata1TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘二维表模式表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘二维表模式表执行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘二维表模式表执行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${Edata1TableName} set version='0' where command='1'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘二维表模式表执行update'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|update ${Edata1TableName} set version='0' where command='1'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘二维表模式表执行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘二维表模式表执行delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘二维表模式表执行delete",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${Edata1TableName} where 1=1"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘二维表模式表执行delete'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|delete from ${Edata1TableName} where 1=1|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘二维表模式表执行delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘列更新模式表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘列更新模式表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${Edata2TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘列更新模式表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${Edata2TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘列更新模式表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘分段模式表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘分段模式表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${Edata3TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘分段模式表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${Edata3TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘分段模式表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘数据模式表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘数据模式表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${Edata4TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘数据模式表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${Edata4TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘数据模式表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘数据模式表执行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘数据模式表执行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${Edata4TableName} set version='0' where col_2='1'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘数据模式表执行update'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|update ${Edata4TableName} set version='0' where col_2='1'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘数据模式表执行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘数据模式表执行delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘数据模式表执行delete",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${Edata4TableName} where col_2='1'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘数据模式表执行delete'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|delete from ${Edata4TableName} where col_2='1'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘数据模式表执行delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘数据模式表执行truncate"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘数据模式表执行truncate",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "truncate table ${Edata4TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘数据模式表执行truncate'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|truncate table ${Edata4TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘数据模式表执行truncate <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘数据模式表执行drop"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘数据模式表执行drop",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "drop table ${Edata4TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘数据模式表执行drop'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|drop table ${Edata4TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘数据模式表执行drop <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_NodeBusinessConf(self):
		u"""配置数据库节点,对数据拼盘合并模式表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对数据拼盘合并模式表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${Edata5TableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对数据拼盘合并模式表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${Edata5TableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对数据拼盘合并模式表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_NodeBusinessConf(self):
		u"""配置数据库节点,对系统内部表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对系统内部表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from tn_process_conf_info"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对系统内部表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from tn_process_conf_info|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对系统内部表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_NodeBusinessConf(self):
		u"""配置数据库节点,普通模式,导入外部数据库，mysql数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "加载数据",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='导入外部mysql数据库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='auto_mysql数据库' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		GetData|${Database}.main|select tab_id from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TabID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='加载数据' and process_id='${ProcessID}'|VarID
		GetData|${Database}.main|select tab_en_name from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TableEnName
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|null|oprt_mode|1|sql_content|null|sql_cfg|[{"var_id":"${VarID}","var_name":"加载数据","db_id":"${DbID}","db_name":"auto_mysql数据库","storageMode":"","batch_submit_row_number":"1000","skip_row_number":"","table_id":"${TabID}","table_name":"${TableEnName}","table_zh_name":"auto_测试表","channelId":3,"cols":[{"chi_name":"序号","en_name":"col_index","type":"index","var_index":"1"},{"chi_name":"姓名","en_name":"user_name","type":"index","var_index":"2"},{"chi_name":"消费金额","en_name":"comsume","type":"index","var_index":"3"},{"chi_name":"账户余额","en_name":"balance","type":"index","var_index":"4"},{"chi_name":"订单时间","en_name":"order_time","type":"index","var_index":"5"},{"chi_name":"收货日期","en_name":"accept_date","type":"index","var_index":"6"},{"chi_name":"详细地址","en_name":"adddress","type":"index","var_index":"7"}]}]|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,普通模式,导入外部数据库，mysql数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_84_NodeBusinessConf(self):
		u"""配置数据库节点,普通模式,导入外部数据库，oracle数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "加载数据",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='导入外部oracle数据库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='auto_oracle数据库' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		GetData|${Database}.main|select tab_id from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TabID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='加载数据' and process_id='${ProcessID}'|VarID
		GetData|${Database}.main|select tab_en_name from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TableEnName
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|null|oprt_mode|1|sql_content|null|sql_cfg|[{"var_id":"${VarID}","var_name":"加载数据","db_id":"${DbID}","db_name":"auto_oracle数据库","storageMode":"","batch_submit_row_number":"","skip_row_number":"","table_id":"${TabID}","table_name":"${TableEnName}","table_zh_name":"auto_测试表","channelId":3,"cols":[{"chi_name":"序号","en_name":"col_index","type":"index","var_index":"1"},{"chi_name":"姓名","en_name":"user_name","type":"index","var_index":"2"},{"chi_name":"消费金额","en_name":"comsume","type":"index","var_index":"3"},{"chi_name":"账户余额","en_name":"balance","type":"index","var_index":"4"},{"chi_name":"订单时间","en_name":"order_time","type":"index","var_index":"5"},{"chi_name":"收货日期","en_name":"accept_date","type":"index","var_index":"6"},{"chi_name":"详细地址","en_name":"adddress","type":"index","var_index":"7"}]}]|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,普通模式,导入外部数据库，oracle数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_85_AddNode(self):
		u"""画流程图,添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"数据库节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_NodeBusinessConf(self):
		u"""配置数据库节点,普通模式,导入外部数据库，postgres数据库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "加载数据",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "3",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='导入外部pg数据库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='auto_postgres数据库' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		GetData|${Database}.main|select tab_id from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TabID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='加载数据' and process_id='${ProcessID}'|VarID
		GetData|${Database}.main|select tab_en_name from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DbID}'|TableEnName
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|null|oprt_mode|1|sql_content|null|sql_cfg|[{"var_id":"${VarID}","var_name":"加载数据","db_id":"${DbID}","db_name":"auto_postgres数据库","storageMode":"","batch_submit_row_number":"1000","skip_row_number":"3","table_id":"${TabID}","table_name":"${TableEnName}","table_zh_name":"auto_测试表","channelId":3,"cols":[{"chi_name":"序号","en_name":"col_index","type":"index","var_index":"1"},{"chi_name":"姓名","en_name":"user_name","type":"index","var_index":"2"},{"chi_name":"消费金额","en_name":"comsume","type":"index","var_index":"3"},{"chi_name":"账户余额","en_name":"balance","type":"index","var_index":"4"},{"chi_name":"订单时间","en_name":"order_time","type":"index","var_index":"5"},{"chi_name":"收货日期","en_name":"accept_date","type":"index","var_index":"6"},{"chi_name":"详细地址","en_name":"adddress","type":"index","var_index":"7"}]}]|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,普通模式,导入外部数据库，postgres数据库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，取总条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库_总条数",
					"输出内容": "总条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，取总条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_88_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，取正常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库_正常条数",
					"输出内容": "正常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，取正常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_89_NodeFetchConf(self):
		u"""节点添加取数配置，配置模式，取异常条数"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "导入外部mysql数据库",
				"取数配置": {
					"操作": "添加",
					"变量名": "导入外部mysql数据库_异常条数",
					"输出内容": "异常条数"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，配置模式，取异常条数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_90_LineNode(self):
		u"""节点普通模式数据插入数据拼盘连线到对网元基础信息表执行select节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "普通模式数据插入数据拼盘",
				"终止节点名称": "对网元基础信息表执行select",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"普通模式数据插入数据拼盘"连线到"对网元基础信息表执行select"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_91_LineNode(self):
		u"""节点对网元基础信息表执行select连线到对网元基础信息表执行update节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元基础信息表执行select",
				"终止节点名称": "对网元基础信息表执行update",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元基础信息表执行select"连线到"对网元基础信息表执行update"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_92_LineNode(self):
		u"""节点对网元基础信息表执行update连线到对网元基础信息表执行delete节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元基础信息表执行update",
				"终止节点名称": "对网元基础信息表执行delete",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元基础信息表执行update"连线到"对网元基础信息表执行delete"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_93_LineNode(self):
		u"""节点对网元基础信息表执行delete连线到对网元辅助资料表执行select节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元基础信息表执行delete",
				"终止节点名称": "对网元辅助资料表执行select",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元基础信息表执行delete"连线到"对网元辅助资料表执行select"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_94_LineNode(self):
		u"""节点对网元辅助资料表执行select连线到对网元辅助资料表执行update节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元辅助资料表执行select",
				"终止节点名称": "对网元辅助资料表执行update",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元辅助资料表执行select"连线到"对网元辅助资料表执行update"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_95_LineNode(self):
		u"""节点对网元辅助资料表执行update连线到对网元辅助资料表执行delete节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元辅助资料表执行update",
				"终止节点名称": "对网元辅助资料表执行delete",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元辅助资料表执行update"连线到"对网元辅助资料表执行delete"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_96_LineNode(self):
		u"""节点对网元辅助资料表执行delete连线到对网元其它资料表执行update节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元辅助资料表执行delete",
				"终止节点名称": "对网元其它资料表执行update",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元辅助资料表执行delete"连线到"对网元其它资料表执行update"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_97_LineNode(self):
		u"""节点对网元其它资料表执行update连线到对网元其它资料表执行truncate节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元其它资料表执行update",
				"终止节点名称": "对网元其它资料表执行truncate",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元其它资料表执行update"连线到"对网元其它资料表执行truncate"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_98_LineNode(self):
		u"""节点对网元其它资料表执行truncate连线到对网元其它资料表执行drop节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元其它资料表执行truncate",
				"终止节点名称": "对网元其它资料表执行drop",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元其它资料表执行truncate"连线到"对网元其它资料表执行drop"节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_99_LineNode(self):
		u"""节点对网元其它资料表执行drop连线到对数据拼盘二维表模式表执行select节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "对网元其它资料表执行drop",
				"终止节点名称": "对数据拼盘二维表模式表执行select",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"对网元其它资料表执行drop"连线到"对数据拼盘二维表模式表执行select"节点 <<<<<')
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
