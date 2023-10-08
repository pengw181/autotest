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


class CrawlerNodePart1(unittest.TestCase):

	log.info("装载可视化操作模拟节点测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试可视化操作模拟节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_可视化操作模拟节点流程说明",
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_可视化操作模拟节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试可视化操作模拟节点 <<<<<')
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
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_可视化操作模拟节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
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
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:个人目录"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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
											"/auto_一级目录"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "个人目录"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|个人目录|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"个人目录","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"/auto_一级目录","name":"/auto_一级目录","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:元素"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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
											"//span[text()='个人目录']"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "元素"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|元素|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"元素","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"//span[text()='个人目录']","name":"//span[text()='个人目录']","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:元素名称"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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
											"常用信息管理"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "元素名称"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|元素名称|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"元素名称","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"常用信息管理","name":"常用信息管理","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量,变量名:元素名称 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图,添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|json|contains("name":"可视化操作模拟节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:点击进入领域"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "表格取数",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击进入领域",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[text()='${Belong}>${Domain}']",
							"描述": "点击进入领域"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|表格取数|node_desc|表格取数_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击进入领域|element_desc|点击进入领域|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[text()='${Belong}>${Domain}']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:点击进入领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:点击流程编辑器"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击流程编辑器",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//span[text()='流程编辑器']",
							"描述": "点击流程编辑器"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击流程编辑器|element_desc|点击流程编辑器|exec_types|3|exec_action|1|label_type|xpath|element_label|//span[text()='流程编辑器']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:点击流程编辑器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:点击流程配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击流程配置",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@class='my-menu sub-menu']//span[text()='流程配置']",
							"描述": "点击流程配置"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击流程配置|element_desc|点击流程配置|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[@class='my-menu sub-menu']//span[text()='流程配置']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:点击流程配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "跳转iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "xpath",
							"元素标识": "//iframe[@src='/VisualModeler/html/gooflow/queryProcessInfo.html']",
							"描述": "跳转iframe"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe|element_desc|跳转iframe|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='/VisualModeler/html/gooflow/queryProcessInfo.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "休眠5秒",
							"动作": "休眠",
							"描述": "休眠5秒",
							"循环次数": "1",
							"_休眠时间": "5",
							"刷新页面": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠5秒|element_desc|休眠5秒|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|1|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,表格取数场景,添加元素:流程取数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "流程取数",
							"元素类型": "表格",
							"动作": "取数",
							"标识类型": "xpath",
							"元素标识": "//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]/table[@class='datagrid-btable']",
							"描述": "表格取数动作",
							"取数模式": "替换",
							"下一页元素标识": "//*[@id='tb']/following-sibling::div[2]//span[@class='l-btn-icon pagination-next']",
							"下一页标识类型": "xpath",
							"休眠时间": "5",
							"表格页数": "3",
							"是否配置期待值": {
								"状态": "关闭"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|流程取数|element_desc|表格取数动作|exec_types|4|exec_action|2|label_type|xpath|element_label|//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]/table[@class='datagrid-btable']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label|//*[@id='tb']/following-sibling::div[2]//span[@class='l-btn-icon pagination-next']|next_label_type|xpath|page_count|3|access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,表格取数场景,添加元素:流程取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击进入领域",
								"休眠5秒",
								"点击流程编辑器",
								"点击流程配置",
								"跳转iframe",
								"休眠5秒",
								"流程取数"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击进入领域'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠5秒'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击流程编辑器'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击流程配置'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|4|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='跳转iframe'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|5|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠5秒'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|6|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='流程取数'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|7|group_tag|null
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图,添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|json|contains("name":"可视化操作模拟节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:点击进入领域"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "文件下载",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击进入领域",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[text()='${Belong}>${Domain}']",
							"描述": "点击进入领域"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|文件下载|node_desc|文件下载_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击进入领域|element_desc|点击进入领域|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[text()='${Belong}>${Domain}']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:点击进入领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:点击常用信息管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击常用信息管理",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//span[text()='${元素名称}']",
							"描述": "点击常用信息管理"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击常用信息管理|element_desc|点击常用信息管理|exec_types|3|exec_action|1|label_type|xpath|element_label|//span[text()='${元素名称}']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:点击常用信息管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:点击文件目录管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击文件目录管理",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//span[text()='文件目录管理']",
							"描述": "点击文件目录管理"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击文件目录管理|element_desc|点击文件目录管理|exec_types|3|exec_action|1|label_type|xpath|element_label|//span[text()='文件目录管理']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:点击文件目录管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:点击个人目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击个人目录",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "${元素}",
							"描述": "点击个人目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击个人目录|element_desc|点击个人目录|exec_types|3|exec_action|1|label_type|xpath|element_label|${元素}|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:点击个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:单击选择目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "单击选择目录",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']",
							"描述": "单击选择目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|单击选择目录|element_desc|单击选择目录|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:单击选择目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "跳转iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "xpath",
							"元素标识": "//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']",
							"描述": "跳转iframe"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe|element_desc|跳转iframe|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:输入文件名"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "输入文件名",
							"元素类型": "输入框",
							"动作": "输入",
							"标识类型": "xpath",
							"元素标识": "//*[@name='fileName']/preceding-sibling::input",
							"描述": "输入文件名",
							"值输入": "request.txt",
							"敏感信息": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|输入文件名|element_desc|输入文件名|exec_types|1|exec_action|4|label_type|xpath|element_label|//*[@name='fileName']/preceding-sibling::input|fill_in_content|request.txt|is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:输入文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:点击查询按钮"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击查询按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='queryBtn']",
							"描述": "点击查询按钮"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击查询按钮|element_desc|点击查询按钮|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[@id='queryBtn']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:点击查询按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:文件下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "文件下载",
							"元素类型": "按钮",
							"动作": "下载",
							"标识类型": "xpath",
							"元素标识": "//*[@field='fileName']/*[text()='request.txt']/../following-sibling::td[2]//a[1]",
							"描述": "文件下载",
							"下载目录": "auto_一级目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载|element_desc|文件下载|exec_types|3|exec_action|5|label_type|xpath|element_label|//*[@field='fileName']/*[text()='request.txt']/../following-sibling::td[2]//a[1]|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,文件下载场景,添加元素:休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "休眠5秒",
							"动作": "休眠",
							"描述": "休眠5秒",
							"循环次数": "1",
							"_休眠时间": "5",
							"刷新页面": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠5秒|element_desc|休眠5秒|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|1|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,文件下载场景,添加元素:休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击进入领域",
								"休眠5秒",
								"点击常用信息管理",
								"点击文件目录管理",
								"点击个人目录",
								"跳转iframe",
								"单击选择目录",
								"输入文件名",
								"点击查询按钮",
								"文件下载"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='文件下载'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击进入领域'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠5秒'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击常用信息管理'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击文件目录管理'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|4|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击个人目录'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|5|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='跳转iframe'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|6|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='单击选择目录'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|7|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='输入文件名'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|8|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击查询按钮'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|9|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='文件下载'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|10|group_tag|null
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_AddNode(self):
		u"""画流程图,添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|json|contains("name":"可视化操作模拟节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:点击进入领域"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "附件上传",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击进入领域",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[text()='${Belong}>${Domain}']",
							"描述": "点击进入领域"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|附件上传|node_desc|附件上传_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击进入领域|element_desc|点击进入领域|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[text()='${Belong}>${Domain}']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:点击进入领域 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:点击常用信息管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击常用信息管理",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//span[text()='${元素名称}']",
							"描述": "点击常用信息管理"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击常用信息管理|element_desc|点击常用信息管理|exec_types|3|exec_action|1|label_type|xpath|element_label|//span[text()='${元素名称}']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:点击常用信息管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:点击文件目录管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击文件目录管理",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//span[text()='文件目录管理']",
							"描述": "点击文件目录管理"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击文件目录管理|element_desc|点击文件目录管理|exec_types|3|exec_action|1|label_type|xpath|element_label|//span[text()='文件目录管理']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:点击文件目录管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:点击个人目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击个人目录",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "${元素}",
							"描述": "点击个人目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击个人目录|element_desc|点击个人目录|exec_types|3|exec_action|1|label_type|xpath|element_label|${元素}|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:点击个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:单击选择目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "单击选择目录",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']",
							"描述": "单击选择目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|单击选择目录|element_desc|单击选择目录|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:单击选择目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "跳转iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "xpath",
							"元素标识": "//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']",
							"描述": "跳转iframe"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe|element_desc|跳转iframe|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:点击上传文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击上传文件",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='uploadBtn']",
							"描述": "点击上传文件"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击上传文件|element_desc|点击上传文件|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[@id='uploadBtn']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:点击上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:跳转iframe2"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "跳转iframe2",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "xpath",
							"元素标识": "//iframe[@src='catalogDefUpload.html']",
							"描述": "跳转iframe2"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe2|element_desc|跳转iframe2|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='catalogDefUpload.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:跳转iframe2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:附件上传-远程加载-本地"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "附件上传-远程加载-本地",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "远程加载",
								"存储类型": "本地",
								"目录": "auto_一级目录",
								"变量引用": "否",
								"文件过滤方式": "关键字",
								"文件名": "data",
								"文件类型": "xlsx"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-本地|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"","catalog_path":"个人目录/${LoginUser}/auto_一级目录","catalog_isKeyword":"0","file":"data","fileType":"xlsx","file_choose_type":"0","file_regex_templ_id":"","file_regex_expr":"","file_regex_json":"","catalog_type":"2"},"attach_source":"3"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:附件上传-远程加载-本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,附件上传场景,添加元素:休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "休眠5秒",
							"动作": "休眠",
							"描述": "休眠5秒",
							"循环次数": "1",
							"_休眠时间": "5",
							"刷新页面": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠5秒|element_desc|休眠5秒|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|1|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,附件上传场景,添加元素:休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击进入领域",
								"休眠5秒",
								"点击常用信息管理",
								"点击文件目录管理",
								"点击个人目录",
								"跳转iframe",
								"单击选择目录",
								"点击上传文件",
								"跳转iframe2",
								"附件上传-远程加载-本地"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='附件上传'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击进入领域'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠5秒'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击常用信息管理'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击文件目录管理'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|4|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击个人目录'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|5|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='跳转iframe'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|6|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='单击选择目录'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|7|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击上传文件'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|8|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='跳转iframe2'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|9|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='附件上传-远程加载-本地'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|step_id|${StepID}|node_id|${NodeID}|oprt_type|1|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|10|group_tag|null
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_AddNode(self):
		u"""画流程图,添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_可视化操作模拟节点流程|json|contains("name":"可视化操作模拟节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "添加多种动作",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|添加多种动作|node_desc|添加多种动作_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[@id='btn']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮, ok"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-ok",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "alert",
							"元素标识": "ok",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-ok|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|alert|element_label|ok|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮, ok <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮, cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-cancel",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "alert",
							"元素标识": "cancel",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-cancel|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|alert|element_label|cancel|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮, cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮, OK"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-点击OK",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "alert",
							"元素标识": "OK",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|元素标识类型为alert时，元素标识只能输入ok或cancel
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮, OK <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮, Cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-点击Cancel",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "alert",
							"元素标识": "Cancel",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|元素标识类型为alert时，元素标识只能输入ok或cancel
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮, Cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮, 非ok、cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-点击success",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "alert",
							"元素标识": "success",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|元素标识类型为alert时，元素标识只能输入ok或cancel
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮, 非ok、cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮,标识类型:class"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-class",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "class",
							"元素标识": "username",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-class|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|class|element_label|username|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮,标识类型:class <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:点击按钮,标识类型:name"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮-name",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "name",
							"元素标识": "btn",
							"描述": "点击按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-name|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|name|element_label|btn|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:点击按钮,标识类型:name <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:输入框输入"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "输入框输入",
							"元素类型": "输入框",
							"动作": "输入",
							"标识类型": "xpath",
							"元素标识": "//*[@id='input']/*[text()='${元素名称}']",
							"描述": "输入框输入动作",
							"值输入": "abc",
							"敏感信息": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|输入框输入|element_desc|输入框输入动作|exec_types|1|exec_action|4|label_type|xpath|element_label|//*[@id='input']/*[text()='${元素名称}']|fill_in_content|abc|is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:输入框输入 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:输入框输入敏感信息"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "输入框输入敏感信息",
							"元素类型": "输入框",
							"动作": "输入",
							"标识类型": "xpath",
							"元素标识": "//*[@id='input']",
							"描述": "输入框输入动作",
							"值输入": "${元素}",
							"敏感信息": "是"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|输入框输入敏感信息|element_desc|输入框输入动作|exec_types|1|exec_action|4|label_type|xpath|element_label|//*[@id='input']|fill_in_content|${元素}|is_sensitive|1|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:输入框输入敏感信息 <<<<<')
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
