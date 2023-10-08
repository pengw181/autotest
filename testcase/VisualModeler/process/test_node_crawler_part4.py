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


class CrawlerNodePart4(unittest.TestCase):

	log.info("装载可视化操作模拟节点测试用例（4）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_150_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加循环,按条件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
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
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and oprt_type='3' and loop_type='0' and oprt_order='4'|ParentOprtID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '3' and loop_type= '2' and (step_id = '' or step_id is null) and oprt_order = '1' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|3|step_id||condition_type|null|loop_type|2|oprt_cfg|contains("cycleCondition":"${时间} != null&&${地点} like abc ddd" &&& "nextCondition":"${时间} != null&&${地点} like abc ddd" &&& "endCondition":"${时间} != null&&${地点} like abc ddd")|oprt_order|1|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加循环,按条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_151_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "条件循环",
							"右键操作": "添加步骤",
							"元素名称": [
								"休眠-不刷新页面",
								"点击按钮",
								"表格取数"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and oprt_type='3' and loop_type='2' and oprt_order='1'|ParentOprtID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠-不刷新页面'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '1' and step_id = '${StepID}' and oprt_order = '1' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击按钮'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '1' and step_id = '${StepID}' and oprt_order = '2' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '1' and step_id = '${StepID}' and oprt_order = '3' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_152_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加循环,按步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "条件循环",
							"右键操作": "添加循环",
							"循环配置": {
								"循环类型": "步骤",
								"步骤选择": "表格取数",
								"循环变量名称": "mi",
								"赋值方式": "替换"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and oprt_type='3' and loop_type='2' and oprt_order='1'|ParentOprtID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|mi|var_json|null|var_expr|null|var_type|17|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|循环体执行步骤变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '3' and step_id = '${StepID}' and loop_type = '3' and oprt_order = '4' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|3|step_id|${StepID}|condition_type|null|loop_type|3|oprt_cfg|{"circle":{"inputStepName":"表格取数","circleVarId":"${VarID}","value_type":"replace","circleVarName":"mi","type":"step","inputStepId":"${StepID}","is_getValueByCol":false}}|oprt_order|4|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加循环,按步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_153_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树删除步骤"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|ParentOprtID|
		${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and oprt_type='1' and step_id=(select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠-不刷新页面') and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}' and node_id='${NodeID}')|OprtID
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "休眠-不刷新页面",
							"右键操作": "删除"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|ParentOprtID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠-不刷新页面'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|0|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}
		CheckData|${Database}.main.tn_node_oprt_rela|0|oprt_id|${OprtID}|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击按钮'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '1' and step_id = '${StepID}' and oprt_order = '2' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '1' and step_id = '${StepID}' and oprt_order = '3' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null
		"""
		log.info('>>>>> 可视化操作模拟节点操作树删除步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_154_NodeBusinessConf(self):
		u"""可视化操作模拟节点元素列表删除被操作数引用的元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "删除",
							"目标元素": "点击按钮"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|业务配置中操作树步骤引用
		"""
		log.info('>>>>> 可视化操作模拟节点元素列表删除被操作数引用的元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_155_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树删除循环"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and oprt_type='3' and loop_type='2' and oprt_order='1'|OprtID|
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "条件循环",
							"右键操作": "删除"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|0|node_id|${NodeID}|oprt_type|3|loop_type|2|oprt_order|1|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|0|oprt_id|${OprtID}|node_id|${NodeID}
		CheckData|${Database}.main.tn_node_oprt_rela|0|parent_oprt_id|${OprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树删除循环 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_156_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树删除条件"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|OprtID|
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "if",
							"右键操作": "删除"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|0|node_id|${NodeID}
		CheckData|${Database}.main.tn_node_oprt_rela|0|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树删除条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_157_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"休眠-不刷新页面",
								"点击按钮",
								"表格取数"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠-不刷新页面'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击按钮'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_158_NodeBusinessConf(self):
		u"""可视化操作模拟节点开启高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
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
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|添加多种动作|node_desc|添加多种动作_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|600|try_time|2
		"""
		log.info('>>>>> 可视化操作模拟节点开启高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_159_NodeBusinessConf(self):
		u"""可视化操作模拟节点关闭高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"高级配置": {
						"状态": "关闭"
					}
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
		"""
		log.info('>>>>> 可视化操作模拟节点关闭高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_160_NodeFetchConf(self):
		u"""节点添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"取数配置": {
					"操作": "添加",
					"变量名": "流程-表格取数",
					"元素名称": "表格取数",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|流程-表格取数|var_json|{"name":"表格取数","value":"${StepID}"}|var_expr|${StepID}|var_type|9|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|可视化操作输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_161_NodeFetchConf(self):
		u"""节点修改取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"取数配置": {
					"操作": "修改",
					"目标变量": "流程-表格取数",
					"变量名": "流程-表格取数1",
					"元素名称": "表格取数",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|流程-表格取数1|var_json|{"name":"表格取数","value":"${StepID}"}|var_expr|${StepID}|var_type|9|value_type|replace|input_var_id||array_index||oprt_type||result_type|null|obj_type|null|var_desc|可视化操作输出变量|process_id|${ProcessID}|var_order|null|create_time|notnull|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点修改取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_162_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树删除步骤，该步骤已被取数配置引用"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "表格取数",
							"右键操作": "删除"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作步骤被取数配置引用，请及时修改取数配置项
		"""
		log.info('>>>>> 可视化操作模拟节点操作树删除步骤，该步骤已被取数配置引用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_163_NodeFetchConf(self):
		u"""节点删除取数配置"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='流程-表格取数1' and var_id in (select var_id from tn_node_var_rela where node_id='${NodeID}')|VarID|
		"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"取数配置": {
					"操作": "删除",
					"目标变量": "流程-表格取数1"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		CheckData|${Database}.main.tn_node_var_cfg|0|var_id|${VarID}|var_name|流程-表格取数1|var_type|16|process_id|${ProcessID}
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

	def test_164_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"表格取数"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_165_NodeFetchConf(self):
		u"""节点添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"取数配置": {
					"操作": "添加",
					"变量名": "流程列表",
					"元素名称": "流程取数",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='表格取数'|NodeID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='流程取数'|StepID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|流程列表|var_json|{"name":"流程取数","value":"${StepID}"}|var_expr|${StepID}|var_type|9|value_type|replace|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|可视化操作输出变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		"""
		log.info('>>>>> 节点添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_166_NodeFetchConf(self):
		u"""节点添加取数配置,变量名已存在"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"取数配置": {
					"操作": "添加",
					"变量名": "流程列表",
					"元素名称": "流程取数",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|该变量已存在
		"""
		log.info('>>>>> 节点添加取数配置,变量名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_167_LineNode(self):
		u"""开始节点连线到节点参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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

	def test_168_LineNode(self):
		u"""节点参数设置连线到节点表格取数"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "参数设置",
				"终止节点名称": "表格取数",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"参数设置"连线到节点"表格取数" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_169_LineNode(self):
		u"""节点表格取数连线到节点文件下载"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "表格取数",
				"终止节点名称": "文件下载",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"表格取数"连线到节点"文件下载" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_170_LineNode(self):
		u"""节点文件下载连线到节点附件上传"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "文件下载",
				"终止节点名称": "附件上传",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"文件下载"连线到节点"附件上传" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_171_LineNode(self):
		u"""节点附件上传连线到节点添加多种动作"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "附件上传",
				"终止节点名称": "添加多种动作",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"附件上传"连线到节点"添加多种动作" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_172_LineNode(self):
		u"""节点添加多种动作连线到节点修改元素"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "添加多种动作",
				"终止节点名称": "修改元素",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"添加多种动作"连线到节点"修改元素" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_173_LineNode(self):
		u"""UNTEST,节点复制元素连线到节点修改元素"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "复制元素",
				"终止节点名称": "修改元素",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,节点"复制元素"连线到节点"修改元素" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_174_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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

	def test_175_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
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

	def test_176_LineNode(self):
		u"""节点修改元素连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"起始节点名称": "修改元素",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"修改元素"连线到结束节点 <<<<<')
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
