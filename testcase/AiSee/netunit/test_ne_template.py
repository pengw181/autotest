# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:07

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class Template(unittest.TestCase):

	log.info("装载统一网元配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_TemplateDataClear(self):
		u"""统一网元配置，数据清理"""
		action = {
			"操作": "TemplateDataClear",
			"参数": {
				"模版名称": "auto_网元模版",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 统一网元配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_SSH终端"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_SSH终端",
				"网元类型": "AUTO",
				"登录模式": "SSH模式",
				"用途说明": "ssh连接终端",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_SSH"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_SSH终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_TELNET终端"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_TELNET终端",
				"网元类型": "AUTO",
				"登录模式": "TELNET模式",
				"用途说明": "telnet连接终端",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_TELNET"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_TELNET终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_SSH终端"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_SSH终端",
				"网元名称": "auto_TURK",
				"厂家": "图科",
				"设备型号": "TKea",
				"待分配网元": [
					"auto_TURK_TKea1",
					"auto_TURK_TKea2",
					"auto_TURK_TKea3"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_SSH终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_SSH终端"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					"auto_TURK_TKea1",
					"auto_TURK_TKea2",
					"auto_TURK_TKea3"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_TestSelectedNetunit(self):
		u"""连通性测试，测试所选"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKea"
				},
				"网元列表": [
					{
						"网元名称": "auto_TURK_TKea1",
						"登录模式": "SSH模式"
					},
					{
						"网元名称": "auto_TURK_TKea2",
						"登录模式": "SSH模式"
					},
					{
						"网元名称": "auto_TURK_TKea3",
						"登录模式": "SSH模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，测试所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_GetConnectReport(self):
		u"""休眠后，获取测试结果汇总"""
		pres = """
		wait|30
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：3条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 休眠后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_TELNET终端"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_TELNET终端",
				"网元名称": "auto_TURK",
				"厂家": "图科",
				"设备型号": "TKing",
				"待分配网元": [
					"auto_TURK_TKing1",
					"auto_TURK_TKing2"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_TELNET终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_TELNET终端"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKing"
				},
				"网元列表": [
					"auto_TURK_TKing1",
					"auto_TURK_TKing2"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_TestSelectedNetunit(self):
		u"""连通性测试，测试所选"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_TURK",
					"网元类型": "AUTO",
					"生产厂家": "图科",
					"设备型号": "TKing"
				},
				"网元列表": [
					{
						"网元名称": "auto_TURK_TKing1",
						"登录模式": "TELNET模式"
					},
					{
						"网元名称": "auto_TURK_TKing2",
						"登录模式": "TELNET模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，测试所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_GetConnectReport(self):
		u"""休眠30秒后，获取测试结果汇总"""
		pres = """
		wait|30
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：2条，异常：0条，测试中：0条
		"""
		log.info('>>>>> 休眠30秒后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_异常跳转指令"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_异常跳转指令",
				"网元类型": "POP",
				"登录模式": "普通模式",
				"用途说明": "登录异常",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_TELNET"
					},
					{
						"操作类型": "添加",
						"步骤信息": "auto_登录指令_异常跳转指令"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_异常跳转指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_异常跳转指令"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_异常跳转指令",
				"网元名称": "auto_SEARCH",
				"厂家": "思旗",
				"设备型号": "Sight",
				"待分配网元": [
					"auto_SEARCH_Sight1"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_异常跳转指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_异常跳转指令"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_SEARCH",
					"网元类型": "POP",
					"生产厂家": "思旗",
					"设备型号": "Sight"
				},
				"网元列表": [
					"auto_SEARCH_Sight1"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_TestSelectedNetunit(self):
		u"""连通性测试，测试所选"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_SEARCH",
					"网元类型": "POP",
					"生产厂家": "思旗",
					"设备型号": "Sight"
				},
				"网元列表": [
					{
						"网元名称": "auto_SEARCH_Sight1",
						"登录模式": "普通模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，测试所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_GetConnectReport(self):
		u"""休眠后，获取测试结果汇总"""
		pres = """
		wait|90
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：0条，异常：1条，测试中：0条
		"""
		log.info('>>>>> 休眠后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_异常终端"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_异常终端",
				"网元类型": "POP",
				"登录模式": "普通模式",
				"用途说明": "登录异常",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_异常终端"
					},
					{
						"操作类型": "添加",
						"步骤信息": "auto_登录指令_跳转指令"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_异常终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_异常终端"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_异常终端",
				"网元名称": "auto_SEARCH",
				"厂家": "思旗",
				"设备型号": "Sight",
				"待分配网元": [
					"auto_SEARCH_Sight2"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_异常终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_异常终端"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_SEARCH",
					"网元类型": "POP",
					"生产厂家": "思旗",
					"设备型号": "Sight"
				},
				"网元列表": [
					"auto_SEARCH_Sight2"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_TestSelectedNetunit(self):
		u"""连通性测试，测试所选"""
		action = {
			"操作": "TestSelectedNetunit",
			"参数": {
				"查询条件": {
					"网元名称": "auto_SEARCH",
					"网元类型": "POP",
					"生产厂家": "思旗",
					"设备型号": "Sight"
				},
				"网元列表": [
					{
						"网元名称": "auto_SEARCH_Sight2",
						"登录模式": "普通模式"
					}
				]
			}
		}
		checks = """
		CheckMsg|设备测试中,请等待
		"""
		log.info('>>>>> 连通性测试，测试所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_GetConnectReport(self):
		u"""休眠后，获取测试结果汇总"""
		pres = """
		wait|90
		"""
		action = {
			"操作": "GetConnectReport",
			"参数": {
				"查询条件": {
					"触发用户": "${CurrentUser}",
					"测试类型": "网元设备"
				}
			}
		}
		checks = """
		CheckMsg|正常：0条，异常：1条，测试中：0条
		"""
		log.info('>>>>> 休眠后，获取测试结果汇总 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_MME模版"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_MME模版",
				"网元类型": "MME",
				"登录模式": "普通模式",
				"用途说明": "MME普通模式连接",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_TELNET"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_MME模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_MME模版"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_MME模版",
				"网元名称": "auto_mme_",
				"厂家": "华为",
				"设备型号": "ME60",
				"待分配网元": [
					"${NetunitMME1}",
					"${NetunitMME2}",
					"${NetunitMME3}"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_MME模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_MME模版"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_mme_",
					"网元类型": "MME",
					"生产厂家": "华为",
					"设备型号": "ME60"
				},
				"网元列表": [
					"${NetunitMME1}",
					"${NetunitMME2}",
					"${NetunitMME3}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddTemplate(self):
		u"""添加统一网元配置，auto_网元模版_CSCE模版"""
		action = {
			"操作": "AddTemplate",
			"参数": {
				"模版名称": "auto_网元模版_CSCE模版",
				"网元类型": "CSCE",
				"登录模式": "普通模式",
				"用途说明": "CSCE普通模式连接",
				"登录配置": [
					{
						"操作类型": "添加",
						"步骤信息": "auto_终端_TELNET"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一网元配置，auto_网元模版_CSCE模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_TemplateBindNE(self):
		u"""统一网元配置网元绑定，模版名称：auto_网元模版_CSCE模版"""
		action = {
			"操作": "TemplateBindNE",
			"参数": {
				"模版名称": "auto_网元模版_CSCE模版",
				"网元名称": "auto_csce_",
				"厂家": "华为",
				"设备型号": "ME60",
				"待分配网元": [
					"${NetunitCSCE1}",
					"${NetunitCSCE2}",
					"${NetunitCSCE3}"
				],
				"分配方式": "分配所选"
			}
		}
		checks = """
		CheckMsg|分配成功
		"""
		log.info('>>>>> 统一网元配置网元绑定，模版名称：auto_网元模版_CSCE模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_TemplateDelivery(self):
		u"""统一网元配置下发配置"""
		action = {
			"操作": "TemplateDelivery",
			"参数": {
				"模版名称": "auto_网元模版_CSCE模版"
			}
		}
		checks = """
		CheckMsg|请到“登录配置确认”页面确认更改内容
		"""
		log.info('>>>>> 统一网元配置下发配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_ConfirmSelected(self):
		u"""登录配置确认，确认所选"""
		action = {
			"操作": "ConfirmSelected",
			"参数": {
				"查询条件": {
					"网元名称": "auto_csce_",
					"网元类型": "CSCE",
					"生产厂家": "华为",
					"设备型号": "ME60"
				},
				"网元列表": [
					"${NetunitCSCE1}",
					"${NetunitCSCE2}",
					"${NetunitCSCE3}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 登录配置确认，确认所选 <<<<<')
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
