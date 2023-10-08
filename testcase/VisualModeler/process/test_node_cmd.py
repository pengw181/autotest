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


class CmdNode(unittest.TestCase):

	log.info("装载指令节点测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_指令节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试指令节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_指令节点流程说明",
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_指令节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程-测试指令节点 <<<<<')
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
				"流程名称": "auto_指令节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_指令节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
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
				"流程名称": "auto_指令节点流程",
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
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "参数1"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|参数1|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"参数1","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","name":"时间","value":"时间","type":"var","desc":"变量","var_type":"user_defined"}],"condition":{}}|var_expr|${时间}，输出列:*|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置指令节点,指令不带参数"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令不带参数",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_date": {
								"解析模版": "auto_解析模板_解析date",
								"参数设置": ""
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令不带参数|node_desc|指令不带参数_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|1|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析date'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		"""
		log.info('>>>>> 配置指令节点,指令不带参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置指令节点,指令带参数,独立模式"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令带参数，独立模式",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_多参数": {
								"解析模版": "auto_解析模板_解析ping",
								"参数设置": {
									"模式": "独立模式",
									"参数": "时间,地点"
								}
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令带参数，独立模式'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令带参数，独立模式|node_desc|指令带参数，独立模式_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|1|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_多参数'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析ping'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='时间' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='地点' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|2|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='时间' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='地点' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|2|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,指令带参数,独立模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置指令节点,指令带参数,二维表模式"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令带参数，二维表模式",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_多参数": {
								"解析模版": "auto_解析模板_解析ping",
								"参数设置": {
									"模式": "二维表模式",
									"参数": {
										"选择变量": "名字",
										"对象设置": "[1]",
										"参数1": "[2],a",
										"参数2": "[3],b"
									}
								}
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令带参数，二维表模式'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令带参数，二维表模式|node_desc|指令带参数，二维表模式_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|1|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_多参数'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析ping'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='名字' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|1|param_cfg|{"obj_index":"1","obj_name":"netunit_id","param_list":[{"param_name":"a","index":"2","param_order":1},{"param_name":"b","index":"3","param_order":2}]}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|1|param_cfg|{"obj_index":"1","obj_name":"netunit_id","param_list":[{"param_name":"a","index":"2","param_order":1},{"param_name":"b","index":"3","param_order":2}]}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,指令带参数,二维表模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置指令节点,组合指令"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令节点,组合指令",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_组合指令": {
								"解析模版": "auto_解析模板_解析date"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,组合指令'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,组合指令|node_desc|指令节点,组合指令_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|1|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_组合指令'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析date'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		"""
		log.info('>>>>> 配置指令节点,组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置指令节点,多指令"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令节点多指令",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"层级成员": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元": [
							"${NetunitMME1}",
							"${NetunitMME2}"
						],
						"指令": {
							"auto_指令_date": {
								"解析模版": "auto_解析模板_解析date"
							},
							"auto_指令_多参数": {
								"解析模版": "auto_解析模板_解析ping",
								"参数设置": {
									"模式": "独立模式",
									"参数": "时间,地点"
								}
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点多指令'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点多指令|node_desc|指令节点多指令_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|1|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析date'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_多参数'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析ping'|AnalyzerID
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME1}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='时间' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='地点' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|2|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select netunit_id from nu.tn_netunit_info where netunit_name='${NetunitMME2}'|NetunitID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|child_level_id|${LevelID}|child_level_path||child_netunit_id|${NetunitID}|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|null|state_id||vendor_id|null|netunit_model_id|null
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='时间' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|1|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='地点' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cmd_var_rela|1|node_id|${NodeID}|cmd_id|${CmdID}|param_order|2|param_mode|0|param_cfg||level_id|${LevelID}|level_path|${LevelPath}|netunit_id|${NetunitID}|var_id|${VarID}|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,多指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图,添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_指令节点流程|json|contains("name":"指令节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置指令节点,按网元类型添加"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "指令节点,按网元类型",
					"成员选择": "",
					"网元选择": "",
					"选择方式": "网元类型",
					"场景标识": "无",
					"配置": {
						"层级": "4G,4G_MME",
						"成员名称": "MME",
						"状态": "带业务",
						"层级成员个数": "是",
						"网元类型": "MME",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元个数": "是",
						"指令": {
							"auto_指令_date": {
								"解析模版": "auto_解析模板_解析date"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,按网元类型'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,按网元类型|node_desc|指令节点,按网元类型_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|2|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select level_id as l2 from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name='MME'|LevelID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		GetData|${Database}.main|select analyzer_id from rulerx_analyzer where analyzer_name='auto_解析模板_解析date'|AnalyzerID
		GetData|${Database}.main|select vendor_id from nu.vendor_info where vendor_cname='华为'|VendorID
		GetData|${Database}.main|select netunit_model_id from nu.TN_NETWK_VENDOR_MD_INFO where netunit_model_name='ME60'|ModelID
		CheckData|${Database}.main.tn_node_nu_cmd_cfg|1|node_id|${NodeID}|level_id|${LevelID}|level_path|${LevelPath}|netunit_id|null|child_level_id|${LevelID}|child_level_path||child_netunit_id|null|cmd_id|${CmdID}|analyzer_id|${AnalyzerID}|attr_sel_id|${VendorID},${ModelID}|attr_sel_name|华为,ME60|belong_id|${BelongID}|domain_id|${DomainID}|netunit_name|MME|state_id|1|vendor_id|${VendorID}|netunit_model_id|${ModelID}
		"""
		log.info('>>>>> 配置指令节点,按网元类型添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置指令节点,开启高级模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点,按网元类型",
				"业务配置": {
					"节点名称": "指令节点,按网元类型",
					"成员选择": "",
					"网元选择": "",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,按网元类型'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,按网元类型|node_desc|指令节点,按网元类型_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|2|cmd_timeout|600|try_time|2|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,开启高级模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置指令节点,关闭高级模式"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点,按网元类型",
				"业务配置": {
					"节点名称": "指令节点,按网元类型",
					"成员选择": "",
					"网元选择": "",
					"高级配置": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,按网元类型'|NodeID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,按网元类型|node_desc|指令节点,按网元类型_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var||filter_var||sel_mode|2|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,关闭高级模式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置指令节点,设置成员选择"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点,按网元类型",
				"业务配置": {
					"节点名称": "指令节点,按网元类型",
					"成员选择": "参数1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,按网元类型'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='参数1' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,按网元类型|node_desc|指令节点,按网元类型_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var|${VarID}|filter_var||sel_mode|2|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,设置成员选择 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeBusinessConf(self):
		u"""配置指令节点,设置网元选择"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点,按网元类型",
				"业务配置": {
					"节点名称": "指令节点,按网元类型",
					"网元选择": "参数1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令节点,按网元类型'|NodeID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where var_name='参数1' and process_id='${ProcessID}'|VarID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|指令节点,按网元类型|node_desc|指令节点,按网元类型_节点说明|node_type_id|3|node_mode_id|300|scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_node_cmd_cfg|1|node_id|${NodeID}|filter_mbr_var|${VarID}|filter_var|${VarID}|sel_mode|2|cmd_timeout|null|try_time|null|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置指令节点,设置网元选择 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeFetchConf(self):
		u"""节点添加取数配置,成员-解析结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-成员-解析结果",
					"对象类型": "成员",
					"结果类型": "解析结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-成员-解析结果|var_json|cmd|var_expr|${CmdID}|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|1|obj_type|1|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,成员-解析结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeFetchConf(self):
		u"""节点添加取数配置,网元-原始结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-原始结果",
					"对象类型": "网元",
					"结果类型": "原始结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-原始结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|0|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-原始结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeFetchConf(self):
		u"""节点添加取数配置,网元-解析结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-解析结果",
					"对象类型": "网元",
					"结果类型": "解析结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-解析结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|1|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-解析结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeFetchConf(self):
		u"""节点添加取数配置,网元-清洗结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-清洗结果",
					"对象类型": "网元",
					"结果类型": "清洗结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-清洗结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|2|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-清洗结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeFetchConf(self):
		u"""节点添加取数配置,网元-格式化二维表结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-格式化二维表结果",
					"对象类型": "网元",
					"结果类型": "格式化二维表结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-格式化二维表结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|3|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-格式化二维表结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeFetchConf(self):
		u"""节点添加取数配置,网元-异常结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-异常结果",
					"对象类型": "网元",
					"结果类型": "异常结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-异常结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|4|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-异常结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeFetchConf(self):
		u"""节点添加取数配置,网元-所有结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-所有结果",
					"对象类型": "网元",
					"结果类型": "所有结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-所有结果|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|5|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-所有结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeFetchConf(self):
		u"""节点添加取数配置,网元-解析模版变量值"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-解析模版变量值",
					"对象类型": "网元",
					"结果类型": "解析模版变量值",
					"变量名": "全部变量",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-解析模版变量值|var_json|cmd|var_expr|*|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|6|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-解析模版变量值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeFetchConf(self):
		u"""节点添加取数配置,变量名称已存在"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-解析模版变量值",
					"对象类型": "网元",
					"结果类型": "解析模版变量值",
					"变量名": "全部变量",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|该变量已存在
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_name|指令节点-网元-解析模版变量值|create_time|now
		"""
		log.info('>>>>> 节点添加取数配置,变量名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeFetchConf(self):
		u"""节点修改取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "修改",
					"目标变量": "指令节点-网元-清洗结果",
					"变量名称": "指令节点-网元-清洗结果1",
					"对象类型": "网元",
					"结果类型": "清洗结果",
					"指令": "auto_指令_date",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-清洗结果1|var_json|cmd|var_expr|${CmdID}|var_type|6|value_type|replace|input_var_id||array_index||oprt_type||result_type|2|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|notnull|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点修改取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeFetchConf(self):
		u"""节点删除取数配置"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='指令节点-网元-清洗结果1' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID|
		"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "删除",
					"目标变量": "指令节点-网元-清洗结果1"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_id|${VarID}|var_name|指令节点-网元-清洗结果1|process_id|${ProcessID}
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

	def test_33_NodeFetchConf(self):
		u"""节点添加取数配置,网元-清洗结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"节点类型": "指令节点",
				"节点名称": "指令不带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令节点-网元-清洗结果",
					"对象类型": "网元",
					"结果类型": "清洗结果",
					"指令": "auto_指令_date",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_指令节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='指令不带参数'|NodeID
		GetData|${Database}.main|select cmd_id from tn_cmd_info where cmd_name='auto_指令_date'|CmdID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|指令节点-网元-清洗结果|var_json|cmd|var_expr|${CmdID}|var_type|6|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|2|obj_type|2|var_desc|指令变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置,网元-清洗结果 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_LineNode(self):
		u"""开始节点连线到节点“参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点“参数设置" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_LineNode(self):
		u"""节点参数设置连线到节点指令不带参数"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "指令不带参数",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"指令不带参数" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_LineNode(self):
		u"""节点指令不带参数连线到节点指令带参数，独立模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令不带参数",
				"终止节点名称": "指令带参数，独立模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令不带参数"连线到节点"指令带参数，独立模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_LineNode(self):
		u"""节点指令带参数，独立模式连线到节点指令带参数，二维表模式"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令带参数，独立模式",
				"终止节点名称": "指令带参数，二维表模式",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令带参数，独立模式"连线到节点"指令带参数，二维表模式" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_LineNode(self):
		u"""节点指令带参数，二维表模式连线到节点指令节点,组合指令"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令带参数，二维表模式",
				"终止节点名称": "指令节点,组合指令",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令带参数，二维表模式"连线到节点"指令节点,组合指令" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_LineNode(self):
		u"""节点指令节点,组合指令连线到节点指令节点多指令"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令节点,组合指令",
				"终止节点名称": "指令节点多指令",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令节点,组合指令"连线到节点"指令节点多指令" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_LineNode(self):
		u"""节点指令节点多指令连线到节点指令节点,按网元类型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令节点多指令",
				"终止节点名称": "指令节点,按网元类型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令节点多指令"连线到节点"指令节点,按网元类型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
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

	def test_42_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
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

	def test_43_LineNode(self):
		u"""节点指令节点,按网元类型连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_指令节点流程",
				"起始节点名称": "指令节点,按网元类型",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"指令节点,按网元类型"连线到结束节点 <<<<<')
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
