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


class CrawlerNodePart3(unittest.TestCase):

	log.info("装载可视化操作模拟节点测试用例（3）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	@unittest.skip
	def test_100_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "跳转iframe",
							"元素名称": "跳转iframe_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_101_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe，返回上层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "跳转iframe_返回上层iframe",
							"元素名称": "跳转iframe_返回上层iframe_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe，返回上层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_102_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe，返回最外层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "跳转iframe_返回最外层iframe",
							"元素名称": "跳转iframe_返回最外层iframe_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：跳转iframe，返回最外层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_103_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：休眠-刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "休眠-刷新页面",
							"元素名称": "休眠-刷新页面_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：休眠-刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_104_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：休眠-不刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "休眠-不刷新页面",
							"元素名称": "休眠-不刷新页面_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：休眠-不刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_105_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：悬停"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "悬停",
							"元素名称": "悬停_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：悬停 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_106_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：重复步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "重复步骤",
							"元素名称": "重复步骤_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：重复步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_107_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素，元素名称已存在"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "复制元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "复制",
							"节点名称": "添加多种动作",
							"复制元素": "重复步骤",
							"元素名称": "重复步骤_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素，元素名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_108_AddNode(self):
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

	def test_109_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,节点名称：修改元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "修改元素",
					"目标系统": "auto_第三方系统"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		CheckData|${Database}.main.tn_node_cfg_info|1|process_id|${ProcessID}|node_name|修改元素|node_desc|修改元素_节点说明|node_type_id|13|node_mode_id||scene_flag||belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		"""
		log.info('>>>>> 配置可视化操作模拟节点,节点名称：修改元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_110_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "点击按钮-修改",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-修改|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|xpath|element_label|//*[@id='btn']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_111_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮, ok"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-ok|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|alert|element_label|ok|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮, ok <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_112_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮, cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-cancel|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|alert|element_label|cancel|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮, cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_113_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮, OK"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮, OK <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_114_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮, Cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮, Cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_115_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮, 非ok、cancel"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮, 非ok、cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_116_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮,标识类型:class"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-class|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|class|element_label|username|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮,标识类型:class <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_117_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:点击按钮,标识类型:name"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|点击按钮-name|element_desc|点击按钮动作|exec_types|3|exec_action|1|label_type|name|element_label|btn|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:点击按钮,标识类型:name <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_118_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:输入框输入"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|输入框输入|element_desc|输入框输入动作|exec_types|1|exec_action|4|label_type|xpath|element_label|//*[@id='input']/*[text()='${元素名称}']|fill_in_content|abc|is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:输入框输入 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_119_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:输入框输入敏感信息"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|输入框输入敏感信息|element_desc|输入框输入动作|exec_types|1|exec_action|4|label_type|xpath|element_label|//*[@id='input']|fill_in_content|${元素}|is_sensitive|1|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:输入框输入敏感信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_120_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:文本取数-设置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "文本取数-设置期待值",
							"元素类型": "文本",
							"动作": "取数",
							"标识类型": "xpath",
							"元素标识": "//*[@id='text']",
							"描述": "文本取数动作",
							"是否配置期待值": {
								"状态": "开启",
								"期待值": "成功_${元素名称}",
								"尝试次数": "3",
								"等待时间": "5"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文本取数-设置期待值|element_desc|文本取数动作|exec_types|7|exec_action|2|label_type|xpath|element_label|//*[@id='text']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|1|expected_value|成功_${元素名称}|try_time|3|wait_time|5|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:文本取数-设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_121_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:文本取数-不设置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "文本取数-不设置期待值",
							"元素类型": "文本",
							"动作": "取数",
							"标识类型": "xpath",
							"元素标识": "//*[@id='text']/@name",
							"描述": "文本取数动作",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文本取数-不设置期待值|element_desc|文本取数动作|exec_types|7|exec_action|2|label_type|xpath|element_label|//*[@id='text']/@name|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:文本取数-不设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_122_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:表格取数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "表格取数",
							"元素类型": "表格",
							"动作": "取数",
							"标识类型": "xpath",
							"元素标识": "//*[@id='text']",
							"描述": "表格取数动作",
							"取数模式": "追加",
							"下一页元素标识": "//*[@name='next']",
							"下一页标识类型": "xpath",
							"休眠时间": "5",
							"表格页数": "3",
							"是否配置期待值": {
								"状态": "开启",
								"期待值": "成功",
								"尝试次数": "3",
								"等待时间": "5"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|表格取数|element_desc|表格取数动作|exec_types|4|exec_action|2|label_type|xpath|element_label|//*[@id='text']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|5|is_fresh|0|repeat_step||is_expected|1|expected_value|成功|try_time|3|wait_time|5|attach_cfg|null|next_element_label|//*[@name='next']|next_label_type|xpath|page_count|3|access_mode|append
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:表格取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_123_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,修改元素:form表单取数，配置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "form表单取数",
							"元素类型": "表单",
							"动作": "取数",
							"标识类型": "id",
							"元素标识": "login_form",
							"描述": "form表单取数",
							"取数模式": "替换",
							"是否配置期待值": {
								"状态": "开启",
								"期待值": "成功",
								"尝试次数": "3",
								"等待时间": "5"
							},
							"变量名": "form表单取数变量名"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,修改元素:form表单取数，配置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_124_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,修改元素:form表单取数，不配置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "form表单取数-不配置期待值",
							"元素类型": "表单",
							"动作": "取数",
							"标识类型": "id",
							"元素标识": "login_form",
							"描述": "form表单取数-不配置期待值",
							"取数模式": "替换",
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
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,修改元素:form表单取数，不配置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_125_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,修改元素:等待元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "等待元素",
							"元素类型": "文本",
							"动作": "等待元素",
							"等待元素标识类型": "id",
							"等待元素标识": "userName",
							"描述": "等待元素",
							"最大等待时间": "10",
							"期待值": "成功",
							"变量名": "等待元素变量名"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,修改元素:等待元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_126_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-动态生成"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "附件上传-动态生成",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "动态生成",
								"附件标题": "动态csv",
								"附件内容": "我们都是中国人",
								"附件类型": "csv"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-动态生成|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"attach_title":"动态csv","attach_type":"csv","attach_content":"我们都是中国人"},"attach_source":"1"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-动态生成 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_127_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-动态生成-变量引用"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "附件上传-动态生成-变量引用",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "动态生成",
								"附件标题": "${名字}",
								"附件内容": "${元素}",
								"附件类型": "csv"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-动态生成-变量引用|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"attach_title":"${名字}","attach_type":"csv","attach_content":"${元素}"},"attach_source":"1"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-动态生成-变量引用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_128_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-本地上传"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "附件上传-本地上传",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "本地上传",
								"附件名称": "factor.xlsx"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-本地上传|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"fileName":"factor.xlsx","attach_content":"${AttachID}","attach_source":"2"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-本地上传 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_129_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-远程加载-本地"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
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
								"文件名": "test_",
								"文件类型": "xls"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-本地|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"","catalog_path":"个人目录/${LoginUser}/auto_一级目录","catalog_isKeyword":"0","file":"test_","fileType":"xls","file_choose_type":"0","file_regex_templ_id":"","file_regex_expr":"","file_regex_json":"","catalog_type":"2"},"attach_source":"3"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-远程加载-本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_130_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-远程加载-远程,文件名使用关键字"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "附件上传-远程加载-远程FTP",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "远程加载",
								"存储类型": "远程",
								"远程服务器": "auto_ftp",
								"目录": "根目录-pw-1",
								"变量引用": "否",
								"文件过滤方式": "关键字",
								"文件名": "test_",
								"文件类型": "csv"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-远程FTP|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"${ServerID}","catalog_path":"/pw/1","catalog_isKeyword":"0","file":"test_","fileType":"csv","file_choose_type":"0","file_regex_templ_id":"","file_regex_expr":"","file_regex_json":""},"attach_source":"4"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-远程加载-远程,文件名使用关键字 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_131_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:附件上传-远程加载-远程,文件名使用正则匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "附件上传-远程加载-远程FTP-正则匹配文件名",
							"元素类型": "输入框",
							"动作": "附件上传",
							"标识类型": "xpath",
							"元素标识": "//*[@id='filebox_file_id_2']",
							"描述": "附件上传动作",
							"附件": {
								"附件来源": "远程加载",
								"存储类型": "远程",
								"远程服务器": "auto_ftp",
								"目录": "根目录-pw-1",
								"变量引用": "否",
								"文件过滤方式": "正则匹配",
								"文件名": {
									"设置方式": "添加",
									"正则模版名称": "auto_正则模版",
									"标签配置": [
										{
											"标签": "自定义文本",
											"自定义值": "pw",
											"是否取值": "绿色"
										},
										{
											"标签": "任意字符",
											"长度": "1到多个",
											"是否取值": "绿色"
										}
									]
								},
								"文件类型": "csv"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|${RegularName}|regx_expr|(pw.+)|creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|regx_templ_id
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-远程FTP-正则匹配文件名|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"${ServerID}","catalog_path":"/pw/1","catalog_isKeyword":"0","file":"","fileType":"csv","file_choose_type":"1","file_regex_templ_id":"${RegxTemplID}","file_regex_expr":"","file_regex_json":""},"attach_source":"4"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:附件上传-远程加载-远程,文件名使用正则匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_132_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:文件下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "文件下载",
							"元素类型": "按钮",
							"动作": "下载",
							"标识类型": "xpath",
							"元素标识": "//*[text()='data.xlsx']/../following-sibling::td[2]//a[@funcid='systemFile_down']",
							"描述": "文件下载动作",
							"下载目录": "auto_一级目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|xpath|element_label|//*[text()='data.xlsx']/../following-sibling::td[2]//a[@funcid='systemFile_down']|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_133_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:文件下载，使用url下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "文件下载-url",
							"元素类型": "按钮",
							"动作": "下载",
							"标识类型": "url",
							"元素标识": "http://192.168.88.116:9200/VisualModeler/VisualModelerHelps/VariableInstruction.pdf",
							"描述": "文件下载动作",
							"下载目录": "auto_一级目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载-url|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|url|element_label|http://192.168.88.116:9200/VisualModeler/VisualModelerHelps/VariableInstruction.pdf|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:文件下载，使用url下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_134_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:文件下载，使用.do下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "文件下载-do",
							"元素类型": "按钮",
							"动作": "下载",
							"标识类型": "url",
							"元素标识": "http://192.168.88.116:9200/approval/restful/downloadFile.do?fileId=a641b1d5-7583-4fa9-8086-9c4d1792891d",
							"描述": "文件下载动作",
							"下载目录": "auto_一级目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载-do|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|url|element_label|http://192.168.88.116:9200/approval/restful/downloadFile.do?fileId=a641b1d5-7583-4fa9-8086-9c4d1792891d|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:文件下载，使用.do下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_135_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "跳转iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "xpath",
							"元素标识": "//iframe[@src='catalogDefUpload.html']",
							"描述": "跳转iframe动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='catalogDefUpload.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_136_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:跳转iframe，返回上层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "跳转iframe_返回上层iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "id",
							"元素标识": "parent",
							"描述": "跳转iframe动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe_返回上层iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|id|element_label|parent|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:跳转iframe，返回上层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_137_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:跳转iframe，返回最外层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "跳转iframe_返回最外层iframe",
							"元素类型": "Iframe",
							"动作": "跳转iframe",
							"标识类型": "id",
							"元素标识": "default",
							"描述": "跳转iframe动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe_返回最外层iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|id|element_label|default|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:跳转iframe，返回最外层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_138_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:关闭当前窗口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "关闭当前窗口",
							"动作": "关闭当前窗口",
							"描述": "关闭当前窗口动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|关闭当前窗口|element_desc|关闭当前窗口动作|exec_types|null|exec_action|11|label_type|null|element_label|//*[@id='btn']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:关闭当前窗口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_139_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:休眠-刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "休眠-刷新页面",
							"动作": "休眠",
							"描述": "休眠动作",
							"循环次数": "3",
							"_休眠时间": "5",
							"刷新页面": "是"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠-刷新页面|element_desc|休眠动作|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|3|sleep|5|is_fresh|1|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:休眠-刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_140_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:休眠-不刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "休眠-不刷新页面",
							"动作": "休眠",
							"描述": "休眠动作",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠-不刷新页面|element_desc|休眠动作|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|1|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:休眠-不刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_141_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:悬停"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "悬停",
							"元素类型": "文本",
							"动作": "悬停",
							"标识类型": "xpath",
							"元素标识": "//*[@class='title']",
							"描述": "悬停动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|悬停|element_desc|悬停动作|exec_types|7|exec_action|9|label_type|xpath|element_label|//*[@class='title']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:悬停 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_142_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:重复步骤"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID|
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID|
		${Database}.main|select string_agg(t.indexs, ',') from (select * from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '文件下载', '输入框输入') order by array_positions(array['表格取数', '悬停', '文件下载', '输入框输入'],element_name ::text)) t|RepeatStep|continue
		${Database}.main|select group_concat(t.indexs order by t.rk separator ',') from (select element_name, indexs, find_in_set(element_name, '表格取数,悬停,文件下载,输入框输入') rk from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '文件下载', '输入框输入') order by find_in_set(element_name, '表格取数,悬停,文件下载,输入框输入')) t|RepeatStep|continue
		${Database}.main|select listagg(t.indexs, ',') within group(order by t.rk) repeat_step from (select element_name, indexs, instr('表格取数,悬停,文件下载,输入框输入', element_name) as rk from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '文件下载', '输入框输入') order by instr('表格取数,悬停,文件下载,输入框输入', element_name)) t|RepeatStep|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "重复步骤",
							"动作": "重复步骤",
							"描述": "重复步骤动作",
							"重复步骤": [
								"表格取数",
								"悬停",
								"文件下载",
								"输入框输入"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|重复步骤|element_desc|重复步骤动作|exec_types|null|exec_action|7|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step|${RepeatStep}|is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:重复步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_143_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:回车"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "回车",
							"元素类型": "按钮",
							"动作": "回车",
							"标识类型": "name",
							"元素标识": "btn",
							"描述": "回车动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|回车|element_desc|回车动作|exec_types|3|exec_action|13|label_type|name|element_label|btn|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:回车 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_144_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,修改元素:重复步骤，名称已存在"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "修改",
							"目标元素": "点击按钮",
							"元素名称": "重复步骤",
							"动作": "重复步骤",
							"描述": "重复步骤动作",
							"重复步骤": [
								"表格取数",
								"悬停",
								"文件下载",
								"输入框输入"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点,修改元素:重复步骤，名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_145_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,删除元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "修改元素",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@id='btn']",
							"描述": "点击按钮动作"
						},
						{
							"操作类型": "删除",
							"目标元素": "点击按钮"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='修改元素'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|0|node_id|${NodeID}|element_name|点击按钮
		"""
		log.info('>>>>> 配置可视化操作模拟节点,删除元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_146_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加条件"""
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
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|2|step_id|null|condition_type|IF|loop_type|null|oprt_cfg|{"expr":"${时间} != null&&${地点} like abc ddd","data":[{"id":"","name":"时间","value":"时间","type":"var","desc":"变量","var_type":"user_defined"},{"id":"","name":"!=","value":"!=","type":"oprt","desc":"操作符"},{"id":"","name":"","value":"","type":"null","desc":"空值"},{"id":"","name":"&&","value":"&&","type":"logic","desc":"逻辑运算符"},{"id":"","name":"地点","value":"地点","type":"var","desc":"变量","var_type":"user_defined"},{"id":"","name":"like","value":"like","type":"oprt","desc":"操作符"},{"id":"","value":"abc ddd","name":"abc ddd","type":"constant","desc":"自定义常量"}]}|oprt_order|1|group_tag|notnull|FetchID|group_tag
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|OprtID
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|2|step_id|null|condition_type|ELSE|loop_type|null|oprt_cfg||oprt_order|2|group_tag|${GroupTag}|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|-1|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_147_NodeBusinessConf(self):
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
							"对象": "if",
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
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|ParentOprtID
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='休眠-不刷新页面'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|1|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='点击按钮'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|2|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		GetData|${Database}.main|select step_id from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name='表格取数'|StepID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|node_id|${NodeID}|oprt_type|1|step_id|${StepID}|condition_type|null|loop_type|null|oprt_cfg|null|oprt_order|3|group_tag|null|FetchID|oprt_id
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_148_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加循环,按变量列表"""
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
							"右键操作": "添加循环",
							"循环配置": {
								"循环类型": "变量列表",
								"变量选择": "名字",
								"循环行变量名称": "loop_a",
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
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1'|ParentOprtID
		GetData|${Database}.main|select var_id from tn_node_var_cfg where process_id='${ProcessID}' and var_name='名字'|VarID1
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|loop_a|var_json|null|var_expr|null|var_type|17|value_type|replace|input_var_id|${VarID1}|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|循环体变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '3' and loop_type= '0' and (step_id = '' or step_id is null) and oprt_order = '4' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|3|step_id||condition_type|null|loop_type|0|oprt_cfg|{"circle":{"circleVarId":"${VarID}","value_type":"replace","inputVarName":"名字","inputVarId":"${VarID1}","circleVarName":"loop_a","is_getValueByCol":false}}|oprt_order|4|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加循环,按变量列表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_149_NodeBusinessConf(self):
		u"""可视化操作模拟节点操作树添加循环,按次数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"操作树": [
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
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='ELSE' and group_tag=(select group_tag from tn_node_vos_oprt_cfg where node_id='${NodeID}' and condition_type='IF' and oprt_order='1')|ParentOprtID
		CheckData|${Database}.main.tn_node_var_cfg|1|var_name|ki|var_json|null|var_expr|3|var_type|17|value_type|append|input_var_id|null|array_index|null|oprt_type|null|result_type|null|obj_type|null|var_desc|循环体执行次数变量|process_id|${ProcessID}|var_order|null|create_time|now|reference_value|null|var_classification|1|FetchID|var_id
		CheckData|${Database}.main.tn_node_var_rela|1|node_id|${NodeID}|var_id|${VarID}
		GetData|${Database}.main|select oprt_id from tn_node_vos_oprt_cfg where node_id = '${NodeID}' and oprt_type = '3' and loop_type= '1' and (step_id = '' or step_id is null) and oprt_order = '1' and oprt_id in (select oprt_id from tn_node_oprt_rela where parent_oprt_id='${ParentOprtID}')|OprtID
		CheckData|${Database}.main.tn_node_vos_oprt_cfg|1|oprt_id|${OprtID}|node_id|${NodeID}|oprt_type|3|step_id||condition_type|null|loop_type|1|oprt_cfg|contains("times":"3" &&& "circleVarName":"ki" &&& "value_type":"append" &&& "nextCondition":"${时间} != null&&${地点} like abc ddd" &&& "endCondition":"${时间} != null&&${地点} like abc ddd")|oprt_order|1|group_tag|null
		CheckData|${Database}.main.tn_node_oprt_rela|1|oprt_id|${OprtID}|parent_oprt_id|${ParentOprtID}|node_id|${NodeID}
		"""
		log.info('>>>>> 可视化操作模拟节点操作树添加循环,按次数 <<<<<')
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
