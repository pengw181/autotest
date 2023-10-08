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


class InfoNode(unittest.TestCase):

	log.info("装载信息处理节点测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_信息处理节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试信息处理节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_信息处理节点流程说明",
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_信息处理节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_信息处理节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试信息处理节点 <<<<<')
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
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_信息处理节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_信息处理节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
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
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
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
											"hello world"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "测试数据"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|测试数据|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"测试数据","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"hello world","name":"hello world","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
		u"""画流程图,添加一个信息处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_信息处理节点流程|json|contains("name":"信息处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个信息处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置信息处理节点,结果呈现/下载模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "信息处理节点",
				"业务配置": {
					"节点名称": "数据呈现",
					"操作模式": "结果呈现/下载",
					"信息描述": "运行结果",
					"显示在运行信息的标题": "是",
					"信息明细": [
						{
							"类型": "自定义值",
							"自定义值": "地点:"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "流程定义变量",
							"变量名": "地点"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "自定义值",
							"自定义值": "流程实例id:"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "系统内置变量",
							"变量名": "流程实例ID"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='数据呈现'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|数据呈现|node_desc|数据呈现_节点说明|node_type_id|12|node_mode_id|1201|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"result_desc":"运行结果","result_detail":"地点:\\n${地点}\\n流程实例id:\\n${AiSee_inst_id}","isDownLoad":"0","downloadCfg":[]}|is_show|1
		"""
		log.info('>>>>> 配置信息处理节点,结果呈现/下载模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图,添加一个信息处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_信息处理节点流程|json|contains("name":"信息处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个信息处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置信息处理节点,结果呈现/下载模式,启用下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "信息处理节点",
				"业务配置": {
					"节点名称": "启用下载功能",
					"操作模式": "结果呈现/下载",
					"信息描述": "运行结果",
					"显示在运行信息的标题": "是",
					"信息明细": [
						{
							"类型": "自定义值",
							"自定义值": "地点:"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "流程定义变量",
							"变量名": "地点"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "自定义值",
							"自定义值": "流程实例id:"
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "系统内置变量",
							"变量名": "流程实例ID"
						}
					],
					"启用下载": {
						"状态": "开启",
						"文件配置": [
							{
								"目录": "auto_一级目录",
								"文件名": "aaa.xlsx"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='启用下载功能'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|启用下载功能|node_desc|启用下载功能_节点说明|node_type_id|12|node_mode_id|1201|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"result_desc":"运行结果","result_detail":"地点:\\n${地点}\\n流程实例id:\\n${AiSee_inst_id}","isDownLoad":"1","downloadCfg":[{"catalog_id":"个人目录/${LoginUser}/auto_一级目录","catalog_name":"个人目录/${LoginUser}/auto_一级目录","file_name":"aaa.xlsx","catalog_type":"2"}]}|is_show|1
		"""
		log.info('>>>>> 配置信息处理节点,结果呈现/下载模式,启用下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置信息处理节点,结果呈现/下载模式,启用下载,增加一条配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "启用下载功能",
				"业务配置": {
					"启用下载": {
						"状态": "开启",
						"文件配置": [
							{
								"目录": "auto_二级目录",
								"文件名": "bbb.csv"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='启用下载功能'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|启用下载功能|node_desc|启用下载功能_节点说明|node_type_id|12|node_mode_id|1201|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"result_desc":"运行结果","result_detail":"地点:\\n${地点}\\n流程实例id:\\n${AiSee_inst_id}","isDownLoad":"1","downloadCfg":[{"catalog_id":"个人目录/${LoginUser}/auto_一级目录","catalog_name":"个人目录/${LoginUser}/auto_一级目录","file_name":"aaa.xlsx","catalog_type":"2"},{"catalog_id":"个人目录/${LoginUser}/auto_一级目录/auto_二级目录","catalog_name":"个人目录/${LoginUser}/auto_一级目录/auto_二级目录","file_name":"bbb.csv","catalog_type":"2"}]}|is_show|1
		"""
		log.info('>>>>> 配置信息处理节点,结果呈现/下载模式,启用下载,增加一条配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置信息处理节点,结果呈现/下载模式,禁用下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "启用下载功能",
				"业务配置": {
					"启用下载": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='启用下载功能'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|启用下载功能|node_desc|启用下载功能_节点说明|node_type_id|12|node_mode_id|1201|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"result_desc":"运行结果","result_detail":"地点:\\n${地点}\\n流程实例id:\\n${AiSee_inst_id}","isDownLoad":"0","downloadCfg":[]}|is_show|1
		"""
		log.info('>>>>> 配置信息处理节点,结果呈现/下载模式,禁用下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeBusinessConf(self):
		u"""配置信息处理节点,结果呈现/下载模式,启用下载,增加一条配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "启用下载功能",
				"业务配置": {
					"启用下载": {
						"状态": "开启",
						"文件配置": [
							{
								"目录": "auto_一级目录",
								"文件名": "aaa.txt"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='启用下载功能'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|启用下载功能|node_desc|启用下载功能_节点说明|node_type_id|12|node_mode_id|1201|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"result_desc":"运行结果","result_detail":"地点:\\n${地点}\\n流程实例id:\\n${AiSee_inst_id}","isDownLoad":"1","downloadCfg":[{"catalog_id":"个人目录/${LoginUser}/auto_一级目录","catalog_name":"个人目录/${LoginUser}/auto_一级目录","file_name":"aaa.txt","catalog_type":"2"}]}|is_show|1
		"""
		log.info('>>>>> 配置信息处理节点,结果呈现/下载模式,启用下载,增加一条配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddNode(self):
		u"""画流程图,添加一个信息处理节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_信息处理节点流程|json|contains("name":"信息处理节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个信息处理节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeBusinessConf(self):
		u"""配置信息处理节点,告警推送模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"节点类型": "信息处理节点",
				"节点名称": "信息处理节点",
				"业务配置": {
					"节点名称": "告警推送",
					"操作模式": "告警推送",
					"变量选择": "测试数据"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_信息处理节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|告警推送|node_desc|告警推送_节点说明|node_type_id|12|node_mode_id|1203|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='测试数据' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='告警推送'|NodeID
		CheckData|${Database}.main.tn_node_info_cfg|1|node_id|${NodeID}|config|{"input_var":"${VarID}","input_var_name":"测试数据"}|is_show|0
		"""
		log.info('>>>>> 配置信息处理节点,告警推送模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_LineNode(self):
		u"""开始节点连线到节点参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
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

	def test_16_LineNode(self):
		u"""节点参数设置连线到节点数据呈现"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "数据呈现",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"数据呈现" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_LineNode(self):
		u"""节点数据呈现连线到节点启用下载功能"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"起始节点名称": "数据呈现",
				"终止节点名称": "启用下载功能",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"数据呈现"连线到节点"启用下载功能" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_LineNode(self):
		u"""节点启用下载功能连线到节点告警推送"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"起始节点名称": "启用下载功能",
				"终止节点名称": "告警推送",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"启用下载功能"连线到节点"告警推送" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
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

	def test_20_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
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

	def test_21_LineNode(self):
		u"""节点告警推送连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_信息处理节点流程",
				"起始节点名称": "告警推送",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"告警推送"连线到结束节点 <<<<<')
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
