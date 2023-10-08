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


class CrawlerNodePart2(unittest.TestCase):

	log.info("装载可视化操作模拟节点测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:文本取数-设置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文本取数-设置期待值|element_desc|文本取数动作|exec_types|7|exec_action|2|label_type|xpath|element_label|//*[@id='text']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|1|expected_value|成功_${元素名称}|try_time|3|wait_time|5|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:文本取数-设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:文本取数-不设置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文本取数-不设置期待值|element_desc|文本取数动作|exec_types|7|exec_action|2|label_type|xpath|element_label|//*[@id='text']/@name|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:文本取数-不设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:表格取数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|表格取数|element_desc|表格取数动作|exec_types|4|exec_action|2|label_type|xpath|element_label|//*[@id='text']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|5|is_fresh|0|repeat_step||is_expected|1|expected_value|成功|try_time|3|wait_time|5|attach_cfg|null|next_element_label|//*[@name='next']|next_label_type|xpath|page_count|3|access_mode|append
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:表格取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_54_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,添加动作:form表单取数，配置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,添加动作:form表单取数，配置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_55_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,添加动作:form表单取数，不配置期待值"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,添加动作:form表单取数，不配置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_56_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,添加动作:等待元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,添加动作:等待元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-动态生成"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-动态生成|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"attach_title":"动态csv","attach_type":"csv","attach_content":"我们都是中国人"},"attach_source":"1"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-动态生成 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-动态生成-变量引用"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-动态生成-变量引用|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"attach_title":"${名字}","attach_type":"csv","attach_content":"${元素}"},"attach_source":"1"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-动态生成-变量引用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-本地上传"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-本地上传|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"fileName":"factor.xlsx","attach_content":"${AttachID}","attach_source":"2"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-本地上传 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-远程加载-本地"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-本地|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"","catalog_path":"个人目录/${LoginUser}/auto_一级目录","catalog_isKeyword":"0","file":"test_","fileType":"xls","file_choose_type":"0","file_regex_templ_id":"","file_regex_expr":"","file_regex_json":"","catalog_type":"2"},"attach_source":"3"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-远程加载-本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-远程加载-远程,文件名使用关键字"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-远程FTP|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"${ServerID}","catalog_path":"/pw/1","catalog_isKeyword":"0","file":"test_","fileType":"csv","file_choose_type":"0","file_regex_templ_id":"","file_regex_expr":"","file_regex_json":""},"attach_source":"4"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-远程加载-远程,文件名使用关键字 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:附件上传-远程加载-远程,文件名使用正则匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetData|${Database}.main|select server_id from tn_ftp_server_cfg where server_name='auto_ftp' and belong_id='${BelongID}' and domain_id='${DomainID}'|ServerID
		CheckData|${Database}.main.rulerx_regx_templ|1|regx_templ_name|${RegularName}|regx_expr|(pw.+)|creater|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|belong_id|${BelongID}|domain_id|${DomainID}|FetchID|regx_templ_id
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|附件上传-远程加载-远程FTP-正则匹配文件名|element_desc|附件上传动作|exec_types|1|exec_action|10|label_type|xpath|element_label|//*[@id='filebox_file_id_2']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|{"attach_content":{"ftp_server_cfg_id":"${ServerID}","catalog_path":"/pw/1","catalog_isKeyword":"0","file":"","fileType":"csv","file_choose_type":"1","file_regex_templ_id":"${RegxTemplID}","file_regex_expr":"","file_regex_json":""},"attach_source":"4"}|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:附件上传-远程加载-远程,文件名使用正则匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:文件下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|xpath|element_label|//*[text()='data.xlsx']/../following-sibling::td[2]//a[@funcid='systemFile_down']|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:文件下载，使用url下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载-url|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|url|element_label|http://192.168.88.116:9200/VisualModeler/VisualModelerHelps/VariableInstruction.pdf|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:文件下载，使用url下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:文件下载，使用.do下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|文件下载-do|element_desc|文件下载动作|exec_types|3|exec_action|5|label_type|url|element_label|http://192.168.88.116:9200/approval/restful/downloadFile.do?fileId=a641b1d5-7583-4fa9-8086-9c4d1792891d|fill_in_content||is_sensitive|0|catalog_path|个人目录/${LoginUser}/auto_一级目录|catalog_type|2|loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:文件下载，使用.do下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|xpath|element_label|//iframe[@src='catalogDefUpload.html']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:跳转iframe，返回上层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe_返回上层iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|id|element_label|parent|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:跳转iframe，返回上层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:跳转iframe，返回最外层iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|跳转iframe_返回最外层iframe|element_desc|跳转iframe动作|exec_types|6|exec_action|3|label_type|id|element_label|default|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:跳转iframe，返回最外层iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:关闭当前窗口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|关闭当前窗口|element_desc|关闭当前窗口动作|exec_types|null|exec_action|11|label_type|null|element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:关闭当前窗口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:休眠-刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠-刷新页面|element_desc|休眠动作|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|3|sleep|5|is_fresh|1|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:休眠-刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:休眠-不刷新页面"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|休眠-不刷新页面|element_desc|休眠动作|exec_types|null|exec_action|6|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|1|sleep|5|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:休眠-不刷新页面 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:悬停"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|悬停|element_desc|悬停动作|exec_types|7|exec_action|9|label_type|xpath|element_label|//*[@class='title']|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:悬停 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:重复步骤"""
		pres = """
		${Database}.main|select process_id from tn_process_conf_info where process_name='auto_可视化操作模拟节点流程'|ProcessID|
		${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID|
		${Database}.main|select string_agg(t.indexs, ',') from (select * from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '点击按钮', '输入框输入') order by array_positions(array['表格取数', '悬停', '点击按钮', '输入框输入'],element_name ::text)) t|RepeatStep|continue
		${Database}.main|select group_concat(t.indexs order by t.rk separator ',') from (select element_name, indexs, find_in_set(element_name, '表格取数,悬停,点击按钮,输入框输入') rk from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '点击按钮', '输入框输入') order by find_in_set(element_name, '表格取数,悬停,点击按钮,输入框输入')) t|RepeatStep|continue
		${Database}.main|select listagg(t.indexs, ',') within group(order by t.rk) repeat_step from (select element_name, indexs, instr('表格取数,悬停,点击按钮,输入框输入', element_name) as rk from tn_node_vos_step_cfg where node_id='${NodeID}' and element_name in ('表格取数', '悬停', '点击按钮', '输入框输入') order by instr('表格取数,悬停,点击按钮,输入框输入', element_name)) t|RepeatStep|continue
		"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "重复步骤",
							"动作": "重复步骤",
							"描述": "重复步骤动作",
							"重复步骤": [
								"表格取数",
								"悬停",
								"点击按钮",
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|重复步骤|element_desc|重复步骤动作|exec_types|null|exec_action|7|label_type||element_label||fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step|${RepeatStep}|is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:重复步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点,添加动作:回车"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "添加多种动作",
				"业务配置": {
					"元素配置": [
						{
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
		GetData|${Database}.main|select node_id from tn_node_cfg_info where process_id='${ProcessID}' and node_name='添加多种动作'|NodeID
		GetData|${Database}.main|select platform_login_cfg_id from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='${BelongID}' and domain_id='${DomainID}'|PlatformLoginCfgID
		CheckData|${Database}.main.tn_node_visual_simulate_cfg|1|node_id|${NodeID}|platform_login_cfg_id|${PlatformLoginCfgID}|vs_timeout|null|try_time|null
		CheckData|${Database}.main.tn_node_vos_step_cfg|1|node_id|${NodeID}|element_name|回车|element_desc|回车动作|exec_types|3|exec_action|13|label_type|name|element_label|btn|fill_in_content||is_sensitive|0|catalog_path||catalog_type||loop_num|null|sleep|null|is_fresh|0|repeat_step||is_expected|0|expected_value||try_time|null|wait_time|null|attach_cfg|null|next_element_label||next_label_type|xpath|page_count||access_mode|replace
		"""
		log.info('>>>>> 配置可视化操作模拟节点,添加动作:回车 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_75_AddNode(self):
		u"""UNTEST,画流程图,添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,画流程图,添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_76_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,节点名称：复制元素"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_可视化操作模拟节点流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "复制元素",
					"目标系统": "auto_第三方系统"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,节点名称：复制元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_77_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：点击按钮"""
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
							"复制元素": "点击按钮",
							"元素名称": "点击按钮_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：点击按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_78_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-ok"""
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
							"复制元素": "点击按钮-ok",
							"元素名称": "点击按钮-ok_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-ok <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_79_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-cancel"""
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
							"复制元素": "点击按钮-cancel",
							"元素名称": "点击按钮-cancel_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-cancel <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_80_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-class"""
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
							"复制元素": "点击按钮-class",
							"元素名称": "点击按钮-class_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-class <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_81_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-name"""
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
							"复制元素": "点击按钮-name",
							"元素名称": "点击按钮-name_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：点击按钮-name <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_82_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：输入框输入"""
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
							"复制元素": "输入框输入",
							"元素名称": "输入框输入_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：输入框输入 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_83_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：输入框输入敏感信息"""
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
							"复制元素": "输入框输入敏感信息",
							"元素名称": "输入框输入敏感信息_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：输入框输入敏感信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_84_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：文本取数-设置期待值"""
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
							"复制元素": "文本取数-设置期待值",
							"元素名称": "文本取数-设置期待值_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：文本取数-设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_85_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：文本取数-不设置期待值"""
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
							"复制元素": "文本取数-不设置期待值",
							"元素名称": "文本取数-不设置期待值_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：文本取数-不设置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_86_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：表格取数"""
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
							"复制元素": "表格取数",
							"元素名称": "表格取数_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：表格取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_87_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：form表单取数"""
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
							"复制元素": "form表单取数",
							"元素名称": "form表单取数_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：form表单取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_88_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：form表单取数-不配置期待值"""
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
							"复制元素": "form表单取数-不配置期待值",
							"元素名称": "form表单取数-不配置期待值_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：form表单取数-不配置期待值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_89_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：等待元素"""
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
							"复制元素": "等待元素",
							"元素名称": "等待元素_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：等待元素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_90_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-动态生成"""
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
							"复制元素": "附件上传-动态生成",
							"元素名称": "附件上传-动态生成_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-动态生成 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_91_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-动态生成-变量引用"""
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
							"复制元素": "附件上传-动态生成-变量引用",
							"元素名称": "附件上传-动态生成-变量引用_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-动态生成-变量引用 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_92_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-本地上传"""
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
							"复制元素": "附件上传-本地上传",
							"元素名称": "附件上传-本地上传_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-本地上传 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_93_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-本地"""
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
							"复制元素": "附件上传-远程加载-本地",
							"元素名称": "附件上传-远程加载-本地_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-本地 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_94_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-远程FTP"""
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
							"复制元素": "附件上传-远程加载-远程FTP",
							"元素名称": "附件上传-远程加载-远程FTP_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-远程FTP <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_95_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-远程FTP-正则匹配文件名"""
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
							"复制元素": "附件上传-远程加载-远程FTP-正则匹配文件名",
							"元素名称": "附件上传-远程加载-远程FTP-正则匹配文件名_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：附件上传-远程加载-远程FTP-正则匹配文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_96_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：文件下载"""
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
							"复制元素": "文件下载",
							"元素名称": "文件下载_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_97_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：文件下载-url"""
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
							"复制元素": "文件下载-url",
							"元素名称": "文件下载-url_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：文件下载-url <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_98_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：文件下载-do"""
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
							"复制元素": "文件下载-do",
							"元素名称": "文件下载-do_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：文件下载-do <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_99_NodeBusinessConf(self):
		u"""UNTEST,配置可视化操作模拟节点,复制元素：关闭当前窗口"""
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
							"复制元素": "关闭当前窗口",
							"元素名称": "关闭当前窗口_复制"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> UNTEST,配置可视化操作模拟节点,复制元素：关闭当前窗口 <<<<<')
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
