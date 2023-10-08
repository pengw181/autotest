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


class SqlNodePart1(unittest.TestCase):

	log.info("装载sql节点测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_数据库节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试数据库节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_数据库节点流程说明",
				"高级配置": {
					"节点异常终止流程": "否",
					"自定义流程变量": {
						"状态": "开启",
						"参数列表": {
							"时间": "2020-10-20###必填",
							"地点": "广州###",
							"名字": "pw###必填"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_数据库节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|0|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "参数设置",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|参数设置|node_desc|参数设置_节点说明|node_type_id|99|node_mode_id|null|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_NodeOptConf(self):
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,内置变量,时间变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"变量",
										{
											"变量名称": "时间变量",
											"时间格式": "yyyy-MM-dd HH:mm:ss",
											"间隔": "0",
											"单位": "日",
											"语言": "中文"
										}
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "当前时间"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|当前时间|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"当前时间","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","var_type":"built_in","type":"var","desc":"变量","value":"time","name":"时间变量","data":{"format":"yyyy-MM-dd HH:mm:ss","interval":"0","unit":"day","language":"zh"}}],"condition":{}}|var_expr|contains(${yyyy-MM-dd HH:mm:ss &&& interval: 0 day} &&& 输出列:*)|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,内置变量,时间变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
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

	def test_7_NodeBusinessConf(self):
		u"""配置数据库节点,删除历史数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "删除历史数据",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='删除历史数据'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|delete from ${OtherInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图,添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "文件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据库节点流程|json|contains("name":"文件节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置文件节点,文件加载,从本地加载测试数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载入库数据",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_一级目录",
						"变量引用": "否"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "data",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"sheet页索引": "2",
							"变量": "加载数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='加载入库数据'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|加载入库数据|node_desc|加载入库数据_节点说明|node_type_id|15|node_mode_id|1503|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|加载数据|var_json|notnull|var_expr|null|var_type|14|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|文件变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		CheckData|${Database}.main.tn_node_file_oprt_cfg|1|node_id|${NodeID}|src_server_id||src_path|个人目录/${LoginUser}/auto_一级目录|src_path_mode|0|src_catalog_type|2|dest_server_id|null|dest_path|null|dest_path_mode|null|dest_catalog_type|null|file_oprt_cfg|[{"startRedLine":"","sheetName":"2","file_choose_type":"0","fileCode":"UTF-8","regex_templ_id":"","file":"data","oprtId":"","isFilter":"0","valueType":"replace","var_id":"${VarID}","fileType":"xlsx","var_name":"加载数据","order":1}]|src_is_keyword|0|dest_is_keyword|null|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置文件节点,文件加载,从本地加载测试数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
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

	def test_11_NodeBusinessConf(self):
		u"""配置数据库节点,普通模式,数据插入内部库,网元其它资料"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "普通模式数据插入网元其它资料",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "加载数据",
						"数据库": "AiSee",
						"存储模式": "",
						"表选择": "auto_网元其它资料",
						"字段映射": {
							"列1": {
								"值类型": "索引",
								"字段值": "1"
							},
							"列2": {
								"值类型": "索引",
								"字段值": "2"
							},
							"列3": {
								"值类型": "索引",
								"字段值": "3"
							},
							"列4": {
								"值类型": "自定义值",
								"字段值": "美好的一天"
							},
							"列5": {
								"值类型": "变量名",
								"字段值": "名字"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通模式数据插入网元其它资料'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='加载数据' and process_id='${ProcessID}'|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='名字' and process_id='${ProcessID}'|VarID2
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料'|ZgTempID
		GetData|${Database}.main|select zg_table_name from zg_temp_cfg where zg_temp_name='auto_网元其它资料'|ZgTableName
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|null|oprt_mode|1|sql_content|null|sql_cfg|[{"var_id":"${VarID1}","var_name":"加载数据","db_id":"${DbID}","db_name":"AiSee","storageMode":"","batch_submit_row_number":"","skip_row_number":"","table_id":"${ZgTempID}","table_name":"${ZgTableName}","table_zh_name":"auto_网元其它资料","channelId":1,"cols":[{"chi_name":"列1","en_name":"COL_2","type":"index","var_index":"1"},{"chi_name":"列2","en_name":"COL_3","type":"index","var_index":"2"},{"chi_name":"列3","en_name":"COL_4","type":"index","var_index":"3"},{"chi_name":"列4","en_name":"COL_5","type":"text","value":"美好的一天"},{"chi_name":"列5","en_name":"COL_6","type":"var","var_id":"${VarID2}","var_name":"名字"}]}]|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,普通模式,数据插入内部库,网元其它资料 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
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

	def test_13_NodeBusinessConf(self):
		u"""配置数据库节点,查询语句"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "查询内部库",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${OtherInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${OtherInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,查询语句 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
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

	def test_15_NodeBusinessConf(self):
		u"""配置数据库节点,insert网元其它资料表"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "insert网元其它资料表",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into ${OtherInfoTableName} (pk, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3, col_4, col_5, col_6, aisee_batch_tag) values(uuid(), 'pw', 0, now(), '440100', 'AiSeeCore', '张三', '张三', '张三', '张三', '张三', '0')"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='insert网元其它资料表'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|insert into ${OtherInfoTableName} (pk, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3, col_4, col_5, col_6, aisee_batch_tag) values(uuid(), 'pw', 0, now(), '440100', 'AiSeeCore', '张三', '张三', '张三', '张三', '张三', '0')|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,insert网元其它资料表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
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

	def test_17_NodeBusinessConf(self):
		u"""配置数据库节点,insert外部库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "数据插入到外部数据库",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "insert into pw_test_data values(1, 'zhangsan', 200, 5000, '"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "当前时间"
							},
							{
								"类型": "自定义值",
								"自定义值": "')"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据插入到外部数据库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='auto_mysql数据库' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|insert into pw_test_data values(1, 'zhangsan', 200, 5000, '${当前时间}')|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,insert外部库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
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

	def test_19_NodeBusinessConf(self):
		u"""配置数据库节点,select外部库"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "查询外部数据库",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "auto_mysql数据库",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from pw_test_data"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询外部数据库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='auto_mysql数据库' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from pw_test_data|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,select外部库 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddNode(self):
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

	def test_21_NodeBusinessConf(self):
		u"""配置数据库节点,普通模式,数据插入内部库,数据拼盘数据模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "普通模式数据插入数据拼盘",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "加载数据",
						"数据库": "AiSee",
						"存储模式": "",
						"表选择": "auto_数据拼盘_数据模式",
						"字段映射": {
							"列1": {
								"值类型": "索引",
								"字段值": "1"
							},
							"列2": {
								"值类型": "索引",
								"字段值": "2"
							},
							"列3": {
								"值类型": "索引",
								"字段值": "3"
							},
							"列4": {
								"值类型": "索引",
								"字段值": "4"
							},
							"列5": {
								"值类型": "索引",
								"字段值": "5"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通模式数据插入数据拼盘'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='加载数据' and process_id='${ProcessID}'|VarID
		GetData|${Database}.main|select temp_id from edata_custom_temp where table_name_ch='auto_数据拼盘_数据模式'|ZgTempID
		GetData|${Database}.main|select table_name_en from edata_custom_temp where table_name_ch='auto_数据拼盘_数据模式'|ZgTableName
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|null|oprt_mode|1|sql_content|null|sql_cfg|[{"var_id":"${VarID}","var_name":"加载数据","db_id":"${DbID}","db_name":"AiSee","storageMode":"","batch_submit_row_number":"","skip_row_number":"","table_id":"${ZgTempID}","table_name":"${ZgTableName}","table_zh_name":"auto_数据拼盘_数据模式","channelId":2,"cols":[{"chi_name":"列1","en_name":"COL_1","type":"index","var_index":"1"},{"chi_name":"列2","en_name":"COL_2","type":"index","var_index":"2"},{"chi_name":"列3","en_name":"COL_3","type":"index","var_index":"3"},{"chi_name":"列4","en_name":"COL_4","type":"index","var_index":"4"},{"chi_name":"列5","en_name":"COL_5","type":"index","var_index":"5"}]}]|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,普通模式,数据插入内部库,数据拼盘数据模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置数据库节点,开启高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"业务配置": {
					"高级配置": {
						"状态": "开启",
						"超时时间": "600",
						"超时重试次数": "2"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${OtherInfoTableName}|sql_cfg|null|time_out|600|try_time|2
		"""
		log.info('>>>>> 配置数据库节点,开启高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeBusinessConf(self):
		u"""配置数据库节点,关闭高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"业务配置": {
					"高级配置": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${OtherInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,关闭高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeFetchConf(self):
		u"""节点添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "添加",
					"变量名": "查询结果",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|查询结果|var_json|{"outCol":"*","isGetColumnName":true}|var_expr|*|var_type|4|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|sql输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeFetchConf(self):
		u"""节点修改取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "修改",
					"目标变量": "查询结果",
					"变量名": "查询结果1",
					"赋值方式": "替换",
					"输出列": "1,2,3",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|查询结果1|var_json|{"outCol":"1,2,3","isGetColumnName":false}|var_expr|1,2,3|var_type|4|value_type|replace|input_var_id||array_index||oprt_type||result_type|null|obj_type|null|var_desc|sql输出变量|process_id|${ProcessID}|var_order|null|create_time|notnull|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点修改取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeFetchConf(self):
		u"""节点删除取数配置"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='查询结果1' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID|
		"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "删除",
					"目标变量": "查询结果1"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_id|${VarID}|var_name|查询结果1|var_desc|sql输出变量|process_id|${ProcessID}
		CheckData|${Database}.main.tn_node_var_rela|0|var_id|${VarID}|node_id|${NodeID}
		"""
		log.info('>>>>> 节点删除取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeFetchConf(self):
		u"""节点添加取数配置，不含列名"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "查询内部库",
				"取数配置": {
					"操作": "添加",
					"变量名": "查询结果_不含列名",
					"赋值方式": "替换",
					"输出列": "*",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|查询结果_不含列名|var_json|{"outCol":"*","isGetColumnName":false}|var_expr|*|var_type|4|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|sql输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置，不含列名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeFetchConf(self):
		u"""节点添加取数配置，含列名"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|查询结果_含列名|var_json|{"outCol":"*","isGetColumnName":true}|var_expr|*|var_type|4|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|sql输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置，含列名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeFetchConf(self):
		u"""节点添加取数配置，取部分列"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='查询内部库'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|查询结果_取部分列|var_json|{"outCol":"1,2,3","isGetColumnName":false}|var_expr|1,2,3|var_type|4|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|sql输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置，取部分列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_LineNode(self):
		u"""开始节点连线到节点参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点"参数设置" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_LineNode(self):
		u"""节点参数设置连线到节点删除历史数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "删除历史数据",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"删除历史数据" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_LineNode(self):
		u"""节点删除历史数据连线到节点加载入库数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "删除历史数据",
				"终止节点名称": "加载入库数据",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"删除历史数据"连线到节点"加载入库数据" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_LineNode(self):
		u"""节点加载入库数据连线到节点普通模式数据插入网元其它资料"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "加载入库数据",
				"终止节点名称": "普通模式数据插入网元其它资料",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"加载入库数据"连线到节点"普通模式数据插入网元其它资料" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_LineNode(self):
		u"""节点普通模式数据插入网元其它资料连线到节点查询内部库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "普通模式数据插入网元其它资料",
				"终止节点名称": "查询内部库",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"普通模式数据插入网元其它资料"连线到节点"查询内部库" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_LineNode(self):
		u"""节点查询内部库连线到节点insert网元其它资料表"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "查询内部库",
				"终止节点名称": "insert网元其它资料表",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"查询内部库"连线到节点"insert网元其它资料表" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_LineNode(self):
		u"""节点insert网元其它资料表连线到节点数据插入到外部数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "insert网元其它资料表",
				"终止节点名称": "数据插入到外部数据库",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"insert网元其它资料表"连线到节点"数据插入到外部数据库" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_LineNode(self):
		u"""节点数据插入到外部数据库连线到节点查询外部数据库"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "数据插入到外部数据库",
				"终止节点名称": "查询外部数据库",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据插入到外部数据库"连线到节点"查询外部数据库" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_LineNode(self):
		u"""节点查询外部数据库连线到节点普通模式数据插入数据拼盘"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"起始节点名称": "查询外部数据库",
				"终止节点名称": "普通模式数据插入数据拼盘",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"查询外部数据库"连线到节点"普通模式数据插入数据拼盘" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_AddNode(self):
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

	def test_40_NodeBusinessConf(self):
		u"""配置数据库节点,对网元基础信息表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元基础信息表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${BasicInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元基础信息表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${BasicInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元基础信息表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_AddNode(self):
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

	def test_42_NodeBusinessConf(self):
		u"""配置数据库节点,对网元基础信息表执行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元基础信息表执行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${BasicInfoTableName} set is_delete=0 where netunit_ip = '192.168.88.123'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元基础信息表执行update'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|update ${BasicInfoTableName} set is_delete=0 where netunit_ip = '192.168.88.123'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元基础信息表执行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_AddNode(self):
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

	def test_44_NodeBusinessConf(self):
		u"""配置数据库节点,对网元基础信息表执行delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元基础信息表执行delete",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${BasicInfoTableName} where netunit_name='PW_MME_ME60_100'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元基础信息表执行delete'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|delete from ${BasicInfoTableName} where netunit_name='PW_MME_ME60_100'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元基础信息表执行delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_AddNode(self):
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

	def test_46_NodeBusinessConf(self):
		u"""配置数据库节点,对网元辅助资料表执行select"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元辅助资料表执行select",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "select * from ${SupplyInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元辅助资料表执行select'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|select * from ${SupplyInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元辅助资料表执行select <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_AddNode(self):
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

	def test_48_NodeBusinessConf(self):
		u"""配置数据库节点,对网元辅助资料表执行update"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元辅助资料表执行update",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "update ${SupplyInfoTableName} set update_date=now() where col_2='www.baidu.com'"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元辅助资料表执行update'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|update ${SupplyInfoTableName} set update_date=now() where col_2='www.baidu.com'|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元辅助资料表执行update <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_AddNode(self):
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

	def test_50_NodeBusinessConf(self):
		u"""配置数据库节点,对网元辅助资料表执行delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据库节点流程",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "对网元辅助资料表执行delete",
					"操作模式": "SQL模式",
					"sql配置": {
						"数据库": "AiSee",
						"编写sql": [
							{
								"类型": "自定义值",
								"自定义值": "delete from ${SupplyInfoTableName}"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据库节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='对网元辅助资料表执行delete'|NodeID
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name='AiSee' and belong_id='${BelongID}' and domain_id='${DomainID}'|DbID
		CheckData|${Database}.main.tn_node_sql_cfg|1|node_id|${NodeID}|process_id|${ProcessID}|db_id|${DbID}|oprt_mode|null|sql_content|delete from ${SupplyInfoTableName}|sql_cfg|null|time_out|null|try_time|null
		"""
		log.info('>>>>> 配置数据库节点,对网元辅助资料表执行delete <<<<<')
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
