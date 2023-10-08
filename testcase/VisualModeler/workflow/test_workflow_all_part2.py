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


class WorkFlowAllNodePart2(unittest.TestCase):

	log.info("装载全流程功能测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：表格取数，添加元素：点击流程配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：表格取数，添加元素：点击流程配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：表格取数，添加元素：跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：表格取数，添加元素：跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：表格取数，添加元素：休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "休眠5秒",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：表格取数，添加元素：休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：表格取数，添加元素：流程取数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：表格取数，添加元素：流程取数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：表格取数，将元素加入操作树中"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "表格取数",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击核心网",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：表格取数，将元素加入操作树中 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_NodeFetchConf(self):
		u"""节点表格取数添加取数配置：流程列表"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 节点"表格取数"添加取数配置：流程列表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_AddNode(self):
		u"""画流程图，添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：点击核心网"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "文件下载",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击核心网",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[text()='${Belong}>${Domain}']",
							"描述": "点击核心网"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：点击核心网 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：点击常用信息管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：点击常用信息管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：点击文件目录管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：点击文件目录管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：点击个人目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：点击个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：单击选择目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：单击选择目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：输入文件名"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
							"值输入": "${文件名}",
							"敏感信息": "否"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：输入文件名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：点击查询按钮"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：点击查询按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：文件下载"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "文件下载",
							"元素类型": "按钮",
							"动作": "下载",
							"标识类型": "xpath",
							"元素标识": "//*[@field='fileName']/*[text()='${文件名}']/../following-sibling::td[2]//a[1]",
							"描述": "文件下载",
							"下载目录": "auto_一级目录"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：文件下载 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：关闭当前窗口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：关闭当前窗口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，添加元素：重复步骤"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "重复步骤",
							"动作": "重复步骤",
							"描述": "重复步骤动作",
							"重复步骤": [
								"点击核心网",
								"休眠5秒"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，添加元素：重复步骤 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：文件下载，将元素加入操作树中"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "文件下载",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击核心网",
								"休眠5秒",
								"关闭当前窗口",
								"重复步骤",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：文件下载，将元素加入操作树中 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_AddNode(self):
		u"""画流程图，添加一个可视化操作模拟节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个可视化操作模拟节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击核心网"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "可视化操作模拟节点",
				"业务配置": {
					"节点名称": "附件上传",
					"目标系统": "auto_第三方系统",
					"元素配置": [
						{
							"元素名称": "点击核心网",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[text()='${Belong}>${Domain}']",
							"描述": "点击核心网"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击核心网 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击常用信息管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击常用信息管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击文件目录管理"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击文件目录管理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击个人目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：单击选择目录"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：单击选择目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：跳转iframe"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：跳转iframe <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击上传文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：跳转iframe2"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
							"描述": "跳转iframe"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：跳转iframe2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：上传附件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "上传附件",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：上传附件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：休眠5秒"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
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
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：休眠5秒 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，添加元素：点击上传按钮"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"元素配置": [
						{
							"元素名称": "点击上传按钮",
							"元素类型": "按钮",
							"动作": "单击",
							"标识类型": "xpath",
							"元素标识": "//*[@onclick='uploadFiles()']",
							"描述": "点击上传按钮动作"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，添加元素：点击上传按钮 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_NodeBusinessConf(self):
		u"""配置可视化操作模拟节点：附件上传，将元素加入操作树中"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "可视化操作模拟节点",
				"节点名称": "附件上传",
				"业务配置": {
					"操作树": [
						{
							"对象": "操作",
							"右键操作": "添加步骤",
							"元素名称": [
								"点击核心网",
								"休眠5秒",
								"点击常用信息管理",
								"点击文件目录管理",
								"点击个人目录",
								"跳转iframe",
								"单击选择目录",
								"点击上传文件",
								"跳转iframe2",
								"上传附件",
								"点击上传按钮"
							]
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置可视化操作模拟节点：附件上传，将元素加入操作树中 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_84_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_85_NodeBusinessConf(self):
		u"""配置接口节点：restful接口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "restful接口",
					"接口": "auto_第三方restful接口_notify"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：restful接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_NodeFetchConf(self):
		u"""配置接口节点：restful接口，取数配置，添加变量：restful接口返回"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "restful接口",
				"取数配置": {
					"操作": "添加",
					"变量名称": "restful接口返回",
					"表达式": "",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：restful接口，取数配置，添加变量：restful接口返回 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_NodeFetchConf(self):
		u"""配置接口节点：restful接口，取数配置，添加变量：restful接口返回_code"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "restful接口",
				"取数配置": {
					"操作": "添加",
					"变量名称": "restful接口返回_code",
					"表达式": "$.code",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：restful接口，取数配置，添加变量：restful接口返回_code <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_88_NodeFetchConf(self):
		u"""配置接口节点：restful接口，取数配置，添加变量：restful接口返回_message"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "restful接口",
				"取数配置": {
					"操作": "添加",
					"变量名称": "restful接口返回_message",
					"表达式": "$.message",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：restful接口，取数配置，添加变量：restful接口返回_message <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_89_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_90_NodeBusinessConf(self):
		u"""配置接口节点：soap接口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "soap接口",
					"接口": "auto_第三方soap接口",
					"请求体内容": "soap_interface_sample.txt"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：soap接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_91_NodeFetchConf(self):
		u"""配置接口节点：soap接口，取数配置，添加变量：soap接口返回sessionid"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "soap接口",
				"取数配置": {
					"操作": "添加",
					"变量名称": "soap接口返回sessionid",
					"表达式": "//soapenv:Body/sam:loginResponse/sessionid",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：soap接口，取数配置，添加变量：soap接口返回sessionid <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_92_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_93_NodeBusinessConf(self):
		u"""配置接口节点：webservice接口"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "webservice接口",
					"接口": "auto_用户密码期限检测"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点：webservice接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_94_AddNode(self):
		u"""画流程图，添加一个指令节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_95_NodeBusinessConf(self):
		u"""配置指令节点：多网元类型，按网元类型添加，添加MME类型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令节点",
				"节点名称": "指令节点",
				"业务配置": {
					"节点名称": "多网元类型",
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
		"""
		log.info('>>>>> 配置指令节点：多网元类型，按网元类型添加，添加MME类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_96_NodeBusinessConf(self):
		u"""配置指令节点：多网元类型，按网元类型添加，添加CSCE类型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令节点",
				"节点名称": "多网元类型",
				"业务配置": {
					"配置": {
						"层级": "4G,4G_CSCE",
						"成员名称": "CSCE",
						"状态": "带业务",
						"层级成员个数": "是",
						"网元类型": "CSCE",
						"厂家": "华为",
						"设备型号": "ME60",
						"网元个数": "是",
						"指令": {
							"auto_指令_ping": {
								"解析模版": "auto_解析模板_解析ping"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令节点：多网元类型，按网元类型添加，添加CSCE类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_97_AddNode(self):
		u"""画流程图，添加一个指令模版节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令模版节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个指令模版节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_98_NodeBusinessConf(self):
		u"""配置指令模版节点：指令模版带参数"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版节点",
				"业务配置": {
					"节点名称": "指令模版带参数",
					"指令任务模版": "auto_指令模版_指令带参数",
					"应用指令模版名称": "否",
					"高级配置": {
						"状态": "开启",
						"超时时间": "600"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点：指令模版带参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_99_NodeFetchConf(self):
		u"""配置指令模版节点：指令模版带参数，取数配置，添加变量：指令模版-格式化二维表结果"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_全流程",
				"节点类型": "指令模版节点",
				"节点名称": "指令模版带参数",
				"取数配置": {
					"操作": "添加",
					"变量名称": "指令模版-格式化二维表结果",
					"对象类型": "网元",
					"结果类型": "格式化二维表结果",
					"指令": "全部指令",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置指令模版节点：指令模版带参数，取数配置，添加变量：指令模版-格式化二维表结果 <<<<<')
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
