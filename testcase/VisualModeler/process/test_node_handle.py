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


class HandleNode(unittest.TestCase):

	log.info("装载数据处理节点测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_数据处理节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试数据处理节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_数据处理节点流程说明",
				"高级配置": {
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_数据处理节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试数据处理节点 <<<<<')
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
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_数据处理节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
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
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量a"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
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
										"自定义值",
										[
											"java,v1,100",
											"python,v1,200",
											"jar,v1,150"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量a"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|变量a|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"变量a","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"java,v1,100\\\\npython,v1,200\\\\njar,v1,150","name":"java,v1,100\\\\npython,v1,200\\\\njar,v1,150","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量a <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""操作配置,添加操作,正则运算,得到二维数组"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "变量a",
								"输出变量": "变量aa",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "3",
									"拆分方式": "文本",
									"拆分符": ",",
									"样例数据": [
										"java,v1,100",
										"python,v1,200",
										"jar,v1,150"
									]
								}
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量a' and oprt_type='base' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|变量aa|var_json|{"begin":"1","cols":"3","split":",","isAdv":"0","expr":"","json":"","outRow":"*","outCol":"*","sampleData":"java,v1,100\\npython,v1,200\\njar,v1,150","formatResult":"","valueType":"replace","oprtType":"regex","inputVarId":"${VarID}","inputName":"变量a","inputVarIndex":"","outputName":"变量aa","outputVarId":"","processId":"${ProcessID}","nodeId":"${NodeID}","condition":{},"default":{"default_value":"","row":"","col":""},"advCfg":{"isExport":"0","trimString":"0","omitEmptyStrings":"0","isAutoFill":"0","autoFillSelect":"","selfDefiningVal":"","deduplication":"0","removeHeader":"0","headerRows":0,"removeFooter":"0","footerRows":0}}|var_expr||var_type|2|value_type|replace|input_var_id|${VarID}|array_index|null|oprt_type|regex|result_type|null|obj_type|null|var_desc|正则运算结果变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 操作配置,添加操作,正则运算,得到二维数组 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量b"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
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
										"自定义值",
										[
											"java,v1,100,a1",
											"python,v1,200,a2",
											"jar,v1,150,a3",
											"c,v1,150,a4"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量b"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|变量b|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"变量b","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"java,v1,100,a1\\\\npython,v1,200,a2\\\\njar,v1,150,a3\\\\nc,v1,150,a4","name":"java,v1,100,a1\\\\npython,v1,200,a2\\\\njar,v1,150,a3\\\\nc,v1,150,a4","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量b <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeOptConf(self):
		u"""操作配置,添加操作,正则运算,得到二维数组"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "变量b",
								"输出变量": "变量bb",
								"赋值方式": "替换",
								"数组索引": "",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "4",
									"拆分方式": "文本",
									"拆分符": ",",
									"样例数据": [
										"java,v1,100,a1",
										"python,v1,200,a2",
										"jar,v1,150,a3",
										"c,v1,150,a4"
									]
								}
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量b' and oprt_type='base' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|变量bb|var_json|{"begin":"1","cols":"4","split":",","isAdv":"0","expr":"","json":"","outRow":"*","outCol":"*","sampleData":"java,v1,100,a1\\npython,v1,200,a2\\njar,v1,150,a3\\nc,v1,150,a4","formatResult":"","valueType":"replace","oprtType":"regex","inputVarId":"${VarID}","inputName":"变量b","inputVarIndex":"","outputName":"变量bb","outputVarId":"","processId":"${ProcessID}","nodeId":"${NodeID}","condition":{},"default":{"default_value":"","row":"","col":""},"advCfg":{"isExport":"0","trimString":"0","omitEmptyStrings":"0","isAutoFill":"0","autoFillSelect":"","selfDefiningVal":"","deduplication":"0","removeHeader":"0","headerRows":0,"removeFooter":"0","footerRows":0}}|var_expr||var_type|2|value_type|replace|input_var_id|${VarID}|array_index|null|oprt_type|regex|result_type|null|obj_type|null|var_desc|正则运算结果变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 操作配置,添加操作,正则运算,得到二维数组 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeOptConf(self):
		u"""通用节点,操作配置,添加操作,基础运算,添加一个一维数组,变量c"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
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
										"自定义值",
										"java"
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										"python"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "变量c"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|变量c|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"变量c","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"java","name":"java","type":"constant","desc":"自定义常量"},{"id":"","name":"∪","value":"∪","type":"union","desc":"集合运算符"},{"id":"","value":"python","name":"python","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个一维数组,变量c <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图,添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"数据处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置数据处理节点,数据比对模式,取关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据比对,取关联结果",
					"处理模式": "数据比对",
					"变量1": "变量aa",
					"变量2": "变量bb",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量1",
					"输出类型": "关联结果",
					"输出变量名称": "数据比对-关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量aa' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量bb' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID2
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据比对,取关联结果'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|数据比对-关联结果|var_json|{"outCol":"*"}|var_expr|*|var_type|7|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|数据处理输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		CheckData|${Database}.main.tn_node_data_oprt_cfg|1|node_id|${NodeID}|var1|${VarID1}|rela_col1|1|update_col1|null|rela_col2|1|update_col2|null|var2|${VarID2}|base|1|var_id|${VarID}|output_type|1
		"""
		log.info('>>>>> 配置数据处理节点,数据比对模式,取关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图,添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"数据处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置数据处理节点,数据比对模式,取未关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据比对,取非关联结果",
					"处理模式": "数据比对",
					"变量1": "变量aa",
					"变量2": "变量bb",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量1",
					"输出类型": "未关联结果",
					"输出变量名称": "数据比对-未关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量aa' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量bb' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID2
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据比对,取非关联结果'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|数据比对-未关联结果|var_json|{"outCol":"*"}|var_expr|*|var_type|7|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|数据处理输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		CheckData|${Database}.main.tn_node_data_oprt_cfg|1|node_id|${NodeID}|var1|${VarID1}|rela_col1|1|update_col1|null|rela_col2|1|update_col2|null|var2|${VarID2}|base|1|var_id|${VarID}|output_type|2
		"""
		log.info('>>>>> 配置数据处理节点,数据比对模式,取未关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图,添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"数据处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置数据处理节点,数据比对模式,二维表与一维表比对，取关联结果"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "二维表与一维表比对,取关联结果",
					"处理模式": "数据比对",
					"变量1": "变量aa",
					"变量2": "变量c",
					"关联列": [
						[
							"1",
							"1"
						]
					],
					"基准变量": "变量1",
					"输出类型": "关联结果",
					"输出变量名称": "二维表与一维表比对-关联结果",
					"输出列": "*",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量aa' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量c' and oprt_type='base' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID2
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='二维表与一维表比对,取关联结果'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|二维表与一维表比对-关联结果|var_json|{"outCol":"*"}|var_expr|*|var_type|7|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|数据处理输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		CheckData|${Database}.main.tn_node_data_oprt_cfg|1|node_id|${NodeID}|var1|${VarID1}|rela_col1|1|update_col1|null|rela_col2|1|update_col2|null|var2|${VarID2}|base|1|var_id|${VarID}|output_type|1
		"""
		log.info('>>>>> 配置数据处理节点,数据比对模式,二维表与一维表比对，取关联结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图,添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"数据处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置数据处理节点,数据更新模式,更新已存在列"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据更新,更新已存在列",
					"处理模式": "数据更新",
					"变量1": "变量aa",
					"变量2": "变量bb",
					"关联列": [
						[
							"1",
							"1"
						],
						[
							"2",
							"2"
						]
					],
					"更新列": [
						[
							"3",
							"4"
						]
					],
					"基准变量": "变量1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量aa' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量bb' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID2
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据更新,更新已存在列'|NodeID
		CheckData|${Database}.main.tn_node_data_oprt_cfg|1|node_id|${NodeID}|var1|${VarID1}|rela_col1|1,2|update_col1|3|rela_col2|1,2|update_col2|4|var2|${VarID2}|base|1|var_id|null|output_type|null
		"""
		log.info('>>>>> 配置数据处理节点,数据更新模式,更新已存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图,添加一个数据处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_数据处理节点流程|json|contains("name":"数据处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个数据处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置数据处理节点,数据更新模式,更新不存在列"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "数据处理节点",
				"节点名称": "数据处理节点",
				"业务配置": {
					"节点名称": "数据更新,更新不存在列",
					"处理模式": "数据更新",
					"变量1": "变量aa",
					"变量2": "变量bb",
					"关联列": [
						[
							"1",
							"1"
						],
						[
							"2",
							"2"
						]
					],
					"更新列": [
						[
							"4",
							"4"
						],
						[
							"6",
							"3"
						]
					],
					"基准变量": "变量1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_数据处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量aa' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID1
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='变量bb' and oprt_type='regex' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID2
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据更新,更新不存在列'|NodeID
		CheckData|${Database}.main.tn_node_data_oprt_cfg|1|node_id|${NodeID}|var1|${VarID1}|rela_col1|1,2|update_col1|4,6|rela_col2|1,2|update_col2|4,3|var2|${VarID2}|base|1|var_id|null|output_type|null
		"""
		log.info('>>>>> 配置数据处理节点,数据更新模式,更新不存在列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_LineNode(self):
		u"""开始节点连线到节点参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
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

	def test_21_LineNode(self):
		u"""节点参数设置连线到节点数据比对,取关联结果"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "数据比对,取关联结果",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"数据比对,取关联结果" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_LineNode(self):
		u"""节点数据比对,取关联结果连线到节点数据比对,取非关联结果"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "数据比对,取关联结果",
				"终止节点名称": "数据比对,取非关联结果",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据比对,取关联结果"连线到节点"数据比对,取非关联结果" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_LineNode(self):
		u"""节点数据比对,取非关联结果连线到节点二维表与一维表比对,取关联结果"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "数据比对,取非关联结果",
				"终止节点名称": "二维表与一维表比对,取关联结果",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据比对,取非关联结果"连线到节点"二维表与一维表比对,取关联结果" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_LineNode(self):
		u"""节点二维表与一维表比对,取关联结果连线到节点数据更新,更新已存在列"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "二维表与一维表比对,取关联结果",
				"终止节点名称": "数据更新,更新已存在列",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"二维表与一维表比对,取关联结果"连线到节点"数据更新,更新已存在列" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""节点数据更新,更新已存在列连线到节点数据更新,更新不存在列"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "数据更新,更新已存在列",
				"终止节点名称": "数据更新,更新不存在列",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据更新,更新已存在列"连线到节点"数据更新,更新不存在列" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"节点类型": "结束节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
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

	def test_28_LineNode(self):
		u"""节点数据更新,更新不存在列连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_数据处理节点流程",
				"起始节点名称": "数据更新,更新不存在列",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据更新,更新不存在列"连线到结束节点 <<<<<')
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
