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


class CommonNodePart1(unittest.TestCase):

	log.info("装载通用节点测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""数据清理,删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_通用节点流程"
			}
		}
		log.info('>>>>> 数据清理,删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试通用节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_通用节点流程说明",
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_通用节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_通用节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试通用节点 <<<<<')
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
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_通用节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_通用节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
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
		u"""配置通用节点，添加一个变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
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
										"时间"
									],
									[
										"并集",
										""
									],
									[
										"变量",
										"名字"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "数据"
								},
								"输出列": "*",
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|数据|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"数据","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","name":"时间","value":"时间","type":"var","desc":"变量","var_type":"user_defined"},{"id":"","name":"∪","value":"∪","type":"union","desc":"集合运算符"},{"id":"","name":"名字","value":"名字","type":"var","desc":"变量","var_type":"user_defined"}],"condition":{}}|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1
		"""
		log.info('>>>>> 配置通用节点，添加一个变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_通用节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "条件依赖",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|条件依赖|node_desc|条件依赖_节点说明|node_type_id|99|node_mode_id|null|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeControlConf(self):
		u"""配置通用节点，控制配置，关闭条件依赖"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"条件依赖": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|0|is_loop|0|loop_type|null|is_logic|0|logic_cnd|{}|loop_cnd|{"circle":{"is_getValueByCol":false}}|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，关闭条件依赖 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启条件依赖"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"条件依赖": {
						"状态": "开启"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|0|loop_type|null|is_logic|0|logic_cnd|{}|loop_cnd|{"circle":{"is_getValueByCol":false}}|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启条件依赖 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启循环，变量列表循环，自定义模式"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"开启循环": {
						"状态": "开启",
						"循环条件": [
							"操作配置"
						],
						"循环类型": "变量列表",
						"循环内容": {
							"模式": "自定义模式",
							"变量名称": "数据",
							"循环行变量名称": "i",
							"赋值方式": "替换"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|1|loop_type|0|is_logic|0|logic_cnd|{}|loop_cnd|{"circle":{"isRecordCycle":false,"loop_businessConfig":false,"loop_fatchConfig":false,"loop_oprtConfig":true,"mode":"custom_mode","is_getValueByCol":false}}|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启循环，变量列表循环，自定义模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启循环，次数循环"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"开启循环": {
						"状态": "开启",
						"循环条件": [
							"操作配置"
						],
						"循环类型": "次数",
						"循环内容": {
							"循环次数": "5",
							"循环变量名称": "num",
							"赋值方式": "替换",
							"跳至下一轮条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"名字"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									"abc ddd"
								]
							],
							"结束循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"名字"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									"abc ddd"
								]
							]
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|num|var_json|null|var_expr|5|var_type|1|value_type|replace|var_desc|循环体执行次数变量|process_id|${ProcessID}|create_time|now|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|1|loop_type|1|is_logic|0|logic_cnd|{}|loop_cnd|contains("times":"5" &&& "type":"count" &&& "circleVarId":"${VarID}" &&& "nextCondition":"${时间} != null&&${名字} like abc ddd" &&& "endCondition":"${时间} != null&&${名字} like abc ddd")|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启循环，次数循环 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启循环，条件循环"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"开启循环": {
						"状态": "开启",
						"循环条件": [
							"操作配置"
						],
						"循环类型": "条件",
						"循环内容": {
							"循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"名字"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									"abc ddd"
								]
							],
							"跳至下一轮条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"名字"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									"abc ddd"
								]
							],
							"结束循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"名字"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									"abc ddd"
								]
							]
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_name|num|var_json|null|var_expr|5|var_type|1|value_type|replace|var_desc|循环体执行次数变量|process_id|${ProcessID}
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|1|loop_type|2|is_logic|0|logic_cnd|{}|loop_cnd|contains("type":"condition" &&& "cycleCondition":"${时间} != null&&${名字} like abc ddd" &&& "nextCondition":"${时间} != null&&${名字} like abc ddd" &&& "endCondition":"${时间} != null&&${名字} like abc ddd")|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启循环，条件循环 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeControlConf(self):
		u"""配置通用节点，控制配置，关闭循环"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"开启循环": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|0|loop_type|null|is_logic|0|logic_cnd|{}|loop_cnd|{"circle":{"is_getValueByCol":false}}|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，关闭循环 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启逻辑分支控制，固定值分支"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"逻辑分支控制": {
						"状态": "开启",
						"逻辑分支类型": "固定值分支",
						"满足条件": [
							[
								"变量",
								"时间"
							],
							[
								"不等于",
								""
							],
							[
								"空值",
								""
							],
							[
								"与",
								""
							],
							[
								"变量",
								"名字"
							],
							[
								"包含",
								""
							],
							[
								"自定义值",
								"abc ddd"
							]
						],
						"不满足条件": [
							[
								"变量",
								"时间"
							],
							[
								"不等于",
								""
							],
							[
								"空值",
								""
							],
							[
								"与",
								""
							],
							[
								"变量",
								"名字"
							],
							[
								"包含",
								""
							],
							[
								"自定义值",
								"abc ddd"
							]
						],
						"不确定条件": [
							[
								"变量",
								"时间"
							],
							[
								"不等于",
								""
							],
							[
								"空值",
								""
							],
							[
								"与",
								""
							],
							[
								"变量",
								"名字"
							],
							[
								"包含",
								""
							],
							[
								"自定义值",
								"abc ddd"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|0|loop_type|null|is_logic|1|logic_cnd|contains("fit":"${时间} != null&&${名字} like abc ddd" &&& "nofit":"${时间} != null&&${名字} like abc ddd" &&& "unsure":"${时间} != null&&${名字} like abc ddd")|loop_cnd|{"circle":{"is_getValueByCol":false}}|branch_type|1
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启逻辑分支控制，固定值分支 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeControlConf(self):
		u"""配置通用节点，控制配置，开启逻辑分支控制，动态值分支"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"逻辑分支控制": {
						"状态": "开启",
						"逻辑分支类型": "动态值分支",
						"动态值": [
							[
								"变量",
								"时间"
							],
							[
								"+",
								""
							],
							[
								"自定义值",
								"1"
							]
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|0|loop_type|null|is_logic|1|logic_cnd|contains("valueExpr":"${时间} + 1")|branch_type|2
		"""
		log.info('>>>>> 配置通用节点，控制配置，开启逻辑分支控制，动态值分支 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NodeControlConf(self):
		u"""配置通用节点，控制配置，关闭逻辑分支控制"""
		action = {
			"操作": "NodeControlConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件依赖",
				"控制配置": {
					"逻辑分支控制": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_通用节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='条件依赖'|NodeID
		CheckData|${Database}.main.tn_node_ctrl_cfg|1|node_id|${NodeID}|is_cnd_rely|1|is_loop|0|loop_type|null|is_logic|0|logic_cnd|{}|loop_cnd|{"circle":{"is_getValueByCol":false}}|branch_type|
		"""
		log.info('>>>>> 配置通用节点，控制配置，关闭逻辑分支控制 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddNode(self):
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "条件和循环",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeOptConf(self):
		u"""操作配置,添加条件"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加条件",
						"条件配置": {
							"if": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"else": "是"
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeOptConf(self):
		u"""操作配置,添加循环,按变量列表,自定义模式"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加循环",
						"循环配置": {
							"循环类型": "变量列表",
							"变量选择": "名字",
							"模式": "自定义模式",
							"循环行变量名称": "loop_a",
							"赋值方式": "替换"
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加循环,按变量列表,自定义模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeOptConf(self):
		u"""操作配置,添加循环,按次数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "else",
						"右键操作": "添加循环",
						"循环配置": {
							"循环类型": "次数",
							"循环次数": "3",
							"循环变量名称": "ki",
							"赋值方式": "追加",
							"跳至下一轮条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"结束循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							]
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加循环,按次数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeOptConf(self):
		u"""操作配置,添加循环,按条件"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "列表循环",
						"右键操作": "添加循环",
						"循环配置": {
							"循环类型": "条件",
							"循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"跳至下一轮条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"结束循环条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							]
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加循环,按条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeOptConf(self):
		u"""操作配置,添加操作,基础运算"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"表达式": [
									[
										"变量",
										"时间"
									],
									[
										"并集",
										""
									],
									[
										"变量",
										"地点"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "普通运算结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,基础运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeOptConf(self):
		u"""操作配置,基础运算,勾选转置"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"表达式": [
									[
										"变量",
										"时间"
									],
									[
										"并集",
										""
									],
									[
										"变量",
										"地点"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "普通运算转置结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "是",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,基础运算,勾选转置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeOptConf(self):
		u"""操作配置,复制"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "普通运算结果",
						"右键操作": "复制"
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,复制 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeOptConf(self):
		u"""操作配置,删除"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "条件和循环",
				"操作配置": [
					{
						"对象": "普通运算结果",
						"右键操作": "删除"
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,删除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddNode(self):
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "运算",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeOptConf(self):
		u"""操作配置,添加操作,正则运算,正则拆分"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "时间",
								"输出变量": "正则运算结果-正则拆分",
								"赋值方式": "替换",
								"数组索引": "2,3,5",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "否",
									"列总数": "4",
									"拆分方式": "正则",
									"正则配置": {
										"设置方式": "选择",
										"正则模版名称": "auto_正则模版_匹配逗号"
									},
									"样例数据": [
										"a1,1,2,3",
										"a2,1,2,3",
										"a3,1,2,3",
										"a4,1,2,3",
										"a5,1,2,3"
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
		"""
		log.info('>>>>> 操作配置,添加操作,正则运算,正则拆分 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeOptConf(self):
		u"""操作配置,添加操作,正则运算,正则匹配数据列"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "正则运算",
							"配置": {
								"输入变量": "时间",
								"输出变量": "正则运算结果-正则匹配数据列",
								"赋值方式": "替换",
								"数组索引": "2,3,5",
								"是否转置": "否",
								"解析配置": {
									"解析开始行": "1",
									"通过正则匹配数据列": "是",
									"正则配置": {
										"设置方式": "添加",
										"正则模版名称": "auto_正则模版",
										"标签配置": [
											{
												"标签": "自定义文本",
												"自定义值": "pw",
												"是否取值": "黄色"
											},
											{
												"标签": "任意字符",
												"长度": "1到多个",
												"是否取值": "绿色"
											},
											{
												"标签": "自定义文本",
												"自定义值": "test",
												"是否取值": "无"
											}
										]
									},
									"样例数据": [
										"pw 001 test",
										"pw 002 test",
										"pw 003 test",
										"pw 004 test",
										"pw 005 test"
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
		"""
		log.info('>>>>> 操作配置,添加操作,正则运算,正则匹配数据列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeOptConf(self):
		u"""操作配置,添加操作,过滤运算"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "过滤运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "名字",
								"过滤条件": [
									[
										"变量索引",
										"1"
									],
									[
										"包含",
										""
									],
									[
										"变量",
										"时间"
									],
									[
										"或",
										""
									],
									[
										"变量",
										"名字"
									],
									[
										"开头",
										""
									],
									[
										"自定义值",
										[
											"张三"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "过滤运算结果"
								},
								"输出列": "1,2,4,3",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,过滤运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddNode(self):
		u"""画流程图,添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "聚合运算",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,总计"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"总计(sum)",
										"2"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算总计结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,总计 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,计数"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"计数(count)",
										"1"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算计数结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,计数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,最大值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"最大值(max)",
										"2"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算最大值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,最大值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,最小值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"最小值(min)",
										"2"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算最小值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,最小值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,平均值"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"平均值(avg)",
										"3"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算平均值结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,平均值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_NodeOptConf(self):
		u"""操作配置,添加操作,聚合运算,分组连接"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "聚合运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "聚合运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "时间",
								"分组依据": "1",
								"表达式": [
									[
										"分组连接",
										"2,&"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "聚合运算分组连接结果"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否",
								"批量修改所有相同的变量名": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,聚合运算,分组连接 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_NodeOptConf(self):
		u"""操作配置,添加操作,网络地址运算,子网掩码方式"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "网络地址运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"输入方式": "子网掩码",
								"输入地址": "255.255.0.0",
								"TCP/IP地址": "192.168.88.123",
								"输出名称": {
									"类型": "输入",
									"变量名": "网络地址运算结果-子网掩码输入方式"
								},
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,网络地址运算,子网掩码方式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_NodeOptConf(self):
		u"""操作配置,添加操作,网络地址运算,位元数方式"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "网络地址运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"输入方式": "位元数",
								"输入地址": "11",
								"输出名称": {
									"类型": "输入",
									"变量名": "网络地址运算结果-位元数方式"
								},
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,网络地址运算,位元数方式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_NodeOptConf(self):
		u"""操作配置,添加操作,分段拆分运算,只配置开始特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"变量名称": "分段拆分运算结果-开始特征行",
								"输入变量": "地点",
								"赋值方式": "追加",
								"开始特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_匹配日期"
								},
								"样例数据": [
									"2020-11-15 12:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤",
									"2020-11-15 13:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤"
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,分段拆分运算,只配置开始特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_NodeOptConf(self):
		u"""操作配置,添加操作,分段拆分运算,只配置结束特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"配置": {
								"变量名称": "分段拆分运算结果-结束特征行",
								"输入变量": "地点",
								"赋值方式": "追加",
								"结束特征行": {
									"状态": "开启",
									"设置方式": "添加",
									"正则模版名称": "auto_正则模版",
									"标签配置": [
										{
											"标签": "自定义文本",
											"自定义值": "pw",
											"是否取值": "黄色"
										},
										{
											"标签": "任意字符",
											"长度": "1到多个",
											"是否取值": "绿色"
										},
										{
											"标签": "自定义文本",
											"自定义值": "test",
											"是否取值": "无"
										}
									]
								},
								"样例数据": [
									"pw 001 test",
									"pw 002 test",
									"pw 003 test",
									"pw 004 test",
									"pw 005 test"
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,分段拆分运算,只配置结束特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_NodeOptConf(self):
		u"""操作配置,添加操作,分段拆分运算,同时配置开始特征行和结束特征行"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "分段拆分运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"变量名称": "分段拆分运算结果-开始结束特征行",
								"输入变量": "地点",
								"赋值方式": "追加",
								"开始特征行": {
									"状态": "开启",
									"设置方式": "选择",
									"正则模版名称": "auto_正则模版_匹配日期"
								},
								"结束特征行": {
									"状态": "开启",
									"设置方式": "添加",
									"正则模版名称": "auto_正则模版",
									"标签配置": [
										{
											"标签": "自定义文本",
											"自定义值": "END",
											"是否取值": "无"
										}
									]
								},
								"样例数据": [
									"2020-11-15 12:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤 END",
									"2020-11-15 13:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤 END"
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,分段拆分运算,同时配置开始特征行和结束特征行 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_NodeOptConf(self):
		u"""操作配置,添加操作,排序运算"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "排序运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"选择变量": "地点",
								"排序配置": [
									{
										"操作": "添加",
										"列索引": "1",
										"排序方式": "升序"
									},
									{
										"操作": "添加",
										"列索引": "2",
										"排序方式": "降序"
									},
									{
										"操作": "添加",
										"列索引": "4",
										"排序方式": "升序"
									},
									{
										"操作": "修改",
										"已排序索引": "4",
										"列索引": "3",
										"排序方式": "降序"
									},
									{
										"操作": "删除",
										"已排序索引": "3"
									}
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "排序运算结果"
								},
								"输出列": "*",
								"赋值方式": "替换"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,排序运算 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_NodeOptConf(self):
		u"""操作配置,添加操作,清洗筛选运算,按时间筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"条件": [
								[
									"变量",
									"时间"
								],
								[
									"不等于",
									""
								],
								[
									"空值",
									""
								],
								[
									"与",
									""
								],
								[
									"变量",
									"地点"
								],
								[
									"包含",
									""
								],
								[
									"自定义值",
									[
										"abc ddd"
									]
								]
							],
							"配置": {
								"变量名称": "清洗筛选运算结果-按时间筛选",
								"输入变量": "时间",
								"赋值方式": "替换",
								"筛选方向": "正向",
								"按时间筛选": {
									"状态": "开启",
									"时间格式": "yyyy-MM-dd",
									"间隔": "-1",
									"单位": "日",
									"语言": "中文"
								}
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,清洗筛选运算,按时间筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_NodeOptConf(self):
		u"""操作配置,添加操作,清洗筛选运算,按关键字/变量筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-按关键字/变量筛选",
								"输入变量": "时间",
								"赋值方式": "替换",
								"筛选方向": "反向",
								"按关键字/变量筛选": {
									"状态": "开启",
									"筛选配置": [
										{
											"类型": "变量",
											"值": "时间"
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "选择",
												"正则模版名称": "auto_正则模版_匹配日期"
											}
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "添加",
												"正则模版名称": "auto_正则模版",
												"标签配置": [
													{
														"标签": "自定义文本",
														"自定义值": "pw",
														"是否取值": "黄色"
													},
													{
														"标签": "任意字符",
														"长度": "1到多个",
														"是否取值": "绿色"
													},
													{
														"标签": "自定义文本",
														"自定义值": "test",
														"是否取值": "无"
													}
												]
											}
										}
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
		"""
		log.info('>>>>> 操作配置,添加操作,清洗筛选运算,按关键字/变量筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_NodeOptConf(self):
		u"""操作配置,添加操作,清洗筛选运算,同时按时间筛选和按关键字/变量筛选"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "清洗筛选运算",
							"配置": {
								"变量名称": "清洗筛选运算结果-同时筛选",
								"输入变量": "时间",
								"赋值方式": "替换",
								"筛选方向": "正向",
								"按时间筛选": {
									"状态": "开启",
									"时间格式": "yyyy-MM-dd",
									"间隔": "-1",
									"单位": "日",
									"语言": "中文"
								},
								"按关键字/变量筛选": {
									"状态": "开启",
									"筛选配置": [
										{
											"类型": "变量",
											"值": "时间"
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "选择",
												"正则模版名称": "auto_正则模版_匹配日期"
											}
										},
										{
											"类型": "关键字",
											"值": {
												"设置方式": "添加",
												"正则模版名称": "auto_正则模版",
												"标签配置": [
													{
														"标签": "自定义文本",
														"自定义值": "pw",
														"是否取值": "黄色"
													},
													{
														"标签": "任意字符",
														"长度": "1到多个",
														"是否取值": "绿色"
													},
													{
														"标签": "自定义文本",
														"自定义值": "test",
														"是否取值": "无"
													}
												]
											}
										}
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
		"""
		log.info('>>>>> 操作配置,添加操作,清洗筛选运算,同时按时间筛选和按关键字/变量筛选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_NodeOptConf(self):
		u"""操作配置,添加操作,动作,休眠"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "动作",
							"配置": {
								"表达式": [
									[
										"休眠",
										"3"
									]
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,动作,休眠 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_NodeOptConf(self):
		u"""操作配置,添加操作,动作,置空"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_通用节点流程",
				"节点类型": "通用节点",
				"节点名称": "运算",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "动作",
							"配置": {
								"表达式": [
									[
										"置空",
										"时间"
									]
								]
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 操作配置,添加操作,动作,置空 <<<<<')
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
