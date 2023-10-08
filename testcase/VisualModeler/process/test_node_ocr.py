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


class OcrNode(unittest.TestCase):

	log.info("装载ocr节点测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_OCR节点流程"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程,测试OCR节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_OCR节点流程说明",
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
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|is_alive|0|create_time|now|user_id|${LoginUser}|remark|auto_OCR节点流程说明|json|null|start_time|null|original_user_id|${LoginUser}|original_time|now|parent_process_id|-1|check_tag|01|process_type_id|process_main|belong_id|${BelongID}|domain_id|${DomainID}|updater|${LoginUser}|update_date|now|is_node_exp_end|1|is_process_var_config|1|is_output_error|0|alarm_type||FetchID|process_id
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|AiSee|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_template_type|1|temp_type_name|auto域|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|temp_type_id
		CheckData|${Database}.main.tn_templ_obj_rel|1|obj_id|${ProcessID}|temp_type_id|${TempTypeID}|belong_id|${BelongID}|domain_id|${DomainID}|obj_type|3
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|时间|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"2020-10-20"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|1|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|地点|var_json|{"MUST_FILL":"0","DEFAULT_PARAM_NAME":"广州"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|2|create_time|now|reference_value|null|var_classification|2
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|名字|var_json|{"MUST_FILL":"1","DEFAULT_PARAM_NAME":"pw"}|var_expr|null|var_type|21|value_type|null|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|流程外部变量|process_id|${ProcessID}|var_order|3|create_time|now|reference_value|null|var_classification|2
		"""
		log.info('>>>>> 添加流程,测试OCR节点 <<<<<')
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
				"流程名称": "auto_OCR节点流程",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"通用节点")|belong_id|${BelongID}|domain_id|${DomainID}
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
				"流程名称": "auto_OCR节点流程",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
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
		u"""通用节点,操作配置,添加操作,基础运算,添加一个自定义变量，本地目录"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
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
										"/auto_一级目录"
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "本地目录"
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='参数设置'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|本地目录|var_json|{"group":null,"oprtType":"base","inputVarId":null,"inputName":null,"outputName":"本地目录","outCol":"*","processId":"${ProcessID}","nodeId":"${NodeID}","valueType":"replace","data":[{"id":"","value":"/auto_一级目录","name":"/auto_一级目录","type":"constant","desc":"自定义常量"}],"condition":{}}|var_expr|notnull|var_type|2|value_type|replace|input_var_id||array_index|null|oprt_type|base|result_type|null|obj_type|null|var_desc|基本运算变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1
		"""
		log.info('>>>>> 通用节点,操作配置,添加操作,基础运算,添加一个自定义变量，本地目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置OCR节点,普通发票"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "普通发票",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_普通发票",
						"变量引用": "否"
					},
					"启用过滤配置": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录/auto_普通发票|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|null|enable_filter_cfg|0|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,普通发票 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置OCR节点,专用发票"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "专用发票",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_专用发票",
						"变量引用": "否"
					},
					"启用过滤配置": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='专用发票'|NodeID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录/auto_专用发票|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|null|enable_filter_cfg|0|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,专用发票 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置OCR节点,关键字识别图片名"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "关键字识别图片名",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_ocr目录",
						"变量引用": "否"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "关键字",
							"文件名": "03",
							"文件类型": "全部"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='关键字识别图片名'|NodeID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|[{"file_choose_type":"0","file":"03","fileType":"","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,关键字识别图片名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置OCR节点,识别jpg"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "识别jpg",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_ocr目录",
						"变量引用": "否"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "添加",
								"正则模版名称": "auto_正则模版",
								"标签配置": [
									{
										"标签": "数字",
										"长度": "1到多个",
										"是否取值": "无"
									}
								]
							},
							"文件类型": "jpg"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='识别jpg'|NodeID
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|${RegularName}|regx_expr|\\d+|creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|regx_templ_id
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|[{"file_choose_type":"1","file_regex_templ_id":"${RegxTemplID}","file_regex_expr":"","file_regex_json":[],"fileType":"jpg","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,识别jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置OCR节点,识别jpeg"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "识别jpeg",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_ocr目录",
						"变量引用": "否"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_匹配数字"
							},
							"文件类型": "jpeg"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='识别jpeg'|NodeID
		GetData|${Database}.main|select regx_templ_id from rulerx_regx_templ where regx_templ_name='auto_正则模版_匹配数字' and belong_id='${BelongID}' and domain_id='${DomainID}'|RegxTemplID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|[{"file_choose_type":"1","file_regex_templ_id":"${RegxTemplID}","file_regex_expr":"","file_regex_json":[],"fileType":"jpeg","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,识别jpeg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置OCR节点,识别png"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "识别png",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_ocr目录",
						"变量引用": "否"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "正则匹配",
							"文件名": {
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_匹配数字"
							},
							"文件类型": "png"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='识别png'|NodeID
		GetData|${Database}.main|select regx_templ_id from rulerx_regx_templ where regx_templ_name='auto_正则模版_匹配数字' and belong_id='${BelongID}' and domain_id='${DomainID}'|RegxTemplID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|个人目录/${LoginUser}/auto_ocr目录|src_path_mode|0|src_catalog_type|2|src_is_keyword|0|file_oprt_cfg|[{"file_choose_type":"1","file_regex_templ_id":"${RegxTemplID}","file_regex_expr":"","file_regex_json":[],"fileType":"png","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,识别png <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置OCR节点,从远程服务器加载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "远程加载文件",
					"存储参数配置": {
						"存储类型": "远程",
						"远程服务器": "auto_ftp",
						"目录": "根目录-pw-ocr",
						"变量引用": "否"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "关键字",
							"文件名": "03",
							"文件类型": "全部"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='远程加载文件'|NodeID
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id|${ServerID}|src_path|/pw/ocr|src_path_mode|1|src_catalog_type|null|src_is_keyword|0|file_oprt_cfg|[{"file_choose_type":"0","file":"03","fileType":"","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,从远程服务器加载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddNode(self):
		u"""画流程图,添加一个OCR节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_process_conf_info|1|process_name|auto_OCR节点流程|json|contains("name":"OCR节点")|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 画流程图,添加一个OCR节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeBusinessConf(self):
		u"""配置OCR节点,目录使用变量"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "OCR节点",
				"业务配置": {
					"节点名称": "目录使用变量",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "${本地目录}",
						"变量引用": "是"
					},
					"启用过滤配置": "开启",
					"过滤配置": [
						{
							"类型": "关键字",
							"文件名": "03",
							"文件类型": "全部"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='目录使用变量'|NodeID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id||src_path|${本地目录}|src_path_mode|0|src_catalog_type|null|src_is_keyword|1|file_oprt_cfg|[{"file_choose_type":"0","file":"03","fileType":"","order":1}]|enable_filter_cfg|1|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,目录使用变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置OCR节点,关闭过滤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "远程加载文件",
				"业务配置": {
					"启用过滤配置": "关闭"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='远程加载文件'|NodeID
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id|${ServerID}|src_path|/pw/ocr|src_path_mode|1|src_catalog_type|null|src_is_keyword|0|file_oprt_cfg|null|enable_filter_cfg|0|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,关闭过滤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeBusinessConf(self):
		u"""配置OCR节点,开启高级设置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "远程加载文件",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='远程加载文件'|NodeID
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|600|try_time|2|src_server_id|${ServerID}|src_path|/pw/ocr|src_path_mode|1|src_catalog_type|null|src_is_keyword|0|file_oprt_cfg|null|enable_filter_cfg|0|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,开启高级设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置OCR节点,关闭高级设置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "远程加载文件",
				"业务配置": {
					"高级配置": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='远程加载文件'|NodeID
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_ai_ocr_cfg|1|node_id|${NodeID}|algorithm_id|ocr_add_tax_elec|ai_timeout|null|try_time|null|src_server_id|${ServerID}|src_path|/pw/ocr|src_path_mode|1|src_catalog_type|null|src_is_keyword|0|file_oprt_cfg|null|enable_filter_cfg|0|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 配置OCR节点,关闭高级设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeFetchConf(self):
		u"""节点添加取数配置-基本信息"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "普通发票_基本信息",
					"取值类型": "基本信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|普通发票_基本信息|var_json|{"isGetColumnName":true}|var_expr|null|var_type|22|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|vat_invoice_basic|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置-基本信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeFetchConf(self):
		u"""节点添加取数配置-明细信息"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "普通发票_明细信息",
					"取值类型": "明细信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|普通发票_明细信息|var_json|{"isGetColumnName":true}|var_expr|null|var_type|22|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|vat_invoice_detail|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置-明细信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeFetchConf(self):
		u"""节点修改取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "修改",
					"目标变量": "普通发票_基本信息",
					"变量名": "普通发票_基本信息1",
					"取值类型": "基本信息",
					"赋值方式": "追加",
					"获取列名": "否"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|普通发票_基本信息1|var_json|{"isGetColumnName":false}|var_expr|null|var_type|22|value_type|append|input_var_id||array_index||oprt_type||result_type|vat_invoice_basic|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|notnull|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点修改取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeFetchConf(self):
		u"""节点删除取数配置"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='普通发票_基本信息1' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID|
		"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "删除",
					"目标变量": "普通发票_基本信息1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_id|${VarID}|var_name|普通发票_基本信息1|var_type|22|process_id|${ProcessID}
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

	def test_29_NodeFetchConf(self):
		u"""节点普通发票添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "普通发票_基本信息",
					"取值类型": "基本信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='普通发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|普通发票_基本信息|var_json|{"isGetColumnName":true}|var_expr|null|var_type|22|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|vat_invoice_basic|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点"普通发票"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeFetchConf(self):
		u"""节点普通发票添加取数配置,变量名已存在"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "普通发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "普通发票_基本信息",
					"取值类型": "基本信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|该变量已存在
		"""
		log.info('>>>>> 节点"普通发票"添加取数配置,变量名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeFetchConf(self):
		u"""节点专用发票添加取数配置-基本信息"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "专用发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "专用发票_基本信息",
					"取值类型": "基本信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='专用发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|专用发票_基本信息|var_json|{"isGetColumnName":true}|var_expr|null|var_type|22|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|vat_invoice_basic|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点"专用发票"添加取数配置-基本信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeFetchConf(self):
		u"""节点专用发票添加取数配置-明细信息"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"节点类型": "OCR节点",
				"节点名称": "专用发票",
				"取数配置": {
					"操作": "添加",
					"变量名": "专用发票_明细信息",
					"取值类型": "明细信息",
					"赋值方式": "替换",
					"获取列名": "是"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_OCR节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='专用发票'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|专用发票_明细信息|var_json|{"isGetColumnName":true}|var_expr|null|var_type|22|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|vat_invoice_detail|obj_type|null|var_desc|OCR节点输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点"专用发票"添加取数配置-明细信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_LineNode(self):
		u"""开始节点连线到节点参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
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

	def test_34_LineNode(self):
		u"""节点参数设置连线到节点普通发票"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "普通发票",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"普通发票" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_LineNode(self):
		u"""节点普通发票连线到节点专用发票"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "普通发票",
				"终止节点名称": "专用发票",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"普通发票"连线到节点"专用发票" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_LineNode(self):
		u"""节点专用发票连线到节点关键字识别图片名"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "专用发票",
				"终止节点名称": "关键字识别图片名",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"专用发票"连线到节点"关键字识别图片名" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_LineNode(self):
		u"""节点关键字识别图片名连线到节点识别jpg"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "关键字识别图片名",
				"终止节点名称": "识别jpg",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"关键字识别图片名"连线到节点"识别jpg" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_LineNode(self):
		u"""节点识别jpg连线到节点识别jpeg"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "识别jpg",
				"终止节点名称": "识别jpeg",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"识别jpg"连线到节点"识别jpeg" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_LineNode(self):
		u"""节点识别jpeg连线到节点识别png"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "识别jpeg",
				"终止节点名称": "识别png",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"识别jpeg"连线到节点"识别png" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_LineNode(self):
		u"""节点识别png连线到节点远程加载文件"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "识别png",
				"终止节点名称": "远程加载文件",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"识别png"连线到节点"远程加载文件" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_LineNode(self):
		u"""节点远程加载文件连线到节点目录使用变量"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "远程加载文件",
				"终止节点名称": "目录使用变量",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"远程加载文件"连线到节点"目录使用变量" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
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

	def test_43_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
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

	def test_44_LineNode(self):
		u"""节点目录使用变量连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_OCR节点流程",
				"起始节点名称": "目录使用变量",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"目录使用变量"连线到结束节点 <<<<<')
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
