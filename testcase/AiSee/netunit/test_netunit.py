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


class NetUnit(unittest.TestCase):

	log.info("装载网元管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_manual"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_manual",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNetUnit(self):
		u"""添加网元，网元名称已存在"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_manual",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.122",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|网元名称已存在
		"""
		log.info('>>>>> 添加网元，网元名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_UpdateNetUnit(self):
		u"""修改网元"""
		action = {
			"操作": "UpdateNetUnit",
			"参数": {
				"网元名称": "auto_manual",
				"修改内容": {
					"网元名称": "auto_manual_bak",
					"登录模式": "POP",
					"网元IP": "192.168.88.122",
					"生产厂家": "思旗",
					"设备型号": "Sight",
					"业务状态": "无业务",
					"最大并发数": "10"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateNetUnit(self):
		u"""修改网元，恢复正确数据"""
		action = {
			"操作": "UpdateNetUnit",
			"参数": {
				"网元名称": "auto_manual_bak",
				"修改内容": {
					"网元名称": "auto_manual",
					"网元类型": "AUTO",
					"网元IP": "192.168.88.123",
					"生产厂家": "图科",
					"设备型号": "TKea",
					"业务状态": "带业务",
					"最大并发数": "1"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改网元，恢复正确数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_DeleteNetUnit(self):
		u"""删除网元"""
		action = {
			"操作": "DeleteNetUnit",
			"参数": {
				"网元名称": "auto_manual"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_manual_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_8_AddNetUnit(self):
		u"""添加网元，auto_manual_s_ssh"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_manual_s_ssh",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_manual_s_ssh <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，普通模式，自身，SSH"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual_s_ssh",
				"登录模式": "普通模式",
				"终端配置": {
					"终端名称": "自身",
					"登录方式": "SSH",
					"用户名": "u_normal",
					"密码": "u_normal_pass",
					"IP": "192.168.88.123",
					"端口": "22",
					"期待返回符": "",
					"失败返回符": "",
					"字符集": "GBK"
				},
				"是否覆盖终端指令": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，普通模式，自身，SSH <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNetUnit(self):
		u"""添加网元，auto_manual_s_telnet"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_manual_s_telnet",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_manual_s_telnet <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddNetUnit(self):
		u"""添加网元，auto_manual"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_manual",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_manual <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，普通模式，自身，TELNET"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual_s_telnet",
				"登录模式": "普通模式",
				"终端配置": {
					"终端名称": "自身",
					"登录方式": "TELNET",
					"用户名": "",
					"密码": "",
					"IP": "192.168.88.123",
					"端口": "23",
					"期待返回符": "",
					"失败返回符": "",
					"字符集": "GBK"
				},
				"是否覆盖终端指令": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，普通模式，自身，TELNET <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NELoginConfigSetCmd(self):
		u"""网元设置登录信息，普通模式，指令设置"""
		action = {
			"操作": "NELoginConfigSetCmd",
			"参数": {
				"网元名称": "auto_manual_s_telnet",
				"登录模式": "普通模式",
				"指令配置": {
					"登录指令": [
						{
							"操作类型": "删除"
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "%USERNAME",
								"账号名称": "auto_账号_常用账号",
								"期待返回符": "assword:",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n",
								"指令类型": "私有指令"
							}
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "%PASSWORD",
								"账号名称": "auto_账号_常用账号",
								"期待返回符": "",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n",
								"指令类型": "私有指令"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，普通模式，指令设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，SSH模式，使用终端"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual",
				"登录模式": "SSH模式",
				"终端配置": {
					"终端名称": "auto_终端_SSH",
					"是否覆盖终端指令": "是"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，SSH模式，使用终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，TELNET模式，使用终端"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual",
				"登录模式": "TELNET模式",
				"终端配置": {
					"终端名称": "auto_终端_TELNET",
					"是否覆盖终端指令": "是"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，TELNET模式，使用终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，异常模式，使用终端"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual",
				"登录模式": "异常模式",
				"终端配置": {
					"终端名称": "auto_终端_异常终端",
					"是否覆盖终端指令": "是"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，异常模式，使用终端 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NELoginConfigSetTerminal(self):
		u"""网元设置登录信息，普通模式，自定义登录信息"""
		action = {
			"操作": "NELoginConfigSetTerminal",
			"参数": {
				"网元名称": "auto_manual",
				"登录模式": "普通模式",
				"终端配置": {
					"终端名称": "auto_终端_SSH",
					"是否覆盖终端指令": "是"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，普通模式，自定义登录信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NELoginConfigSetCmd(self):
		u"""网元设置登录信息，普通模式，指令设置"""
		action = {
			"操作": "NELoginConfigSetCmd",
			"参数": {
				"网元名称": "auto_manual",
				"登录模式": "普通模式",
				"指令配置": {
					"终端指令": [
						{
							"操作类型": "删除"
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "date",
								"账号名称": "",
								"期待返回符": "",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n"
							}
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "ping %IP -c 5",
								"账号名称": "",
								"期待返回符": "",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n"
							}
						}
					],
					"终端指令设为私有指令": "否",
					"登录指令": [
						{
							"操作类型": "删除"
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "telnet %IP",
								"账号名称": "",
								"期待返回符": "ogin:",
								"失败返回符": "",
								"隐藏输入指令": "是",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "3",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n"
							}
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "%USERNAME",
								"账号名称": "auto_账号_常用账号",
								"期待返回符": "assword:",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n"
							}
						},
						{
							"操作类型": "添加",
							"指令信息": {
								"指令内容": "%PASSWORD",
								"账号名称": "auto_账号_常用账号",
								"期待返回符": "",
								"失败返回符": "",
								"隐藏输入指令": "否",
								"隐藏指令返回": "",
								"退出命令": "",
								"执行后等待时间": "",
								"是否适配网元": "是",
								"字符集": "GBK",
								"换行符": "\\n"
							}
						}
					],
					"登录指令设为私有指令": "否"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元设置登录信息，普通模式，指令设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_TURK",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_20_AddNetUnit(self):
		u"""添加网元，auto_TURK_TKea1"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_TURK_TKea1",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_TURK_TKea1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddNetUnit(self):
		u"""添加网元，auto_TURK_TKea2"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_TURK_TKea2",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_TURK_TKea2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddNetUnit(self):
		u"""添加网元，auto_TURK_TKea3"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_TURK_TKea3",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKea",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_TURK_TKea3 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddNetUnit(self):
		u"""添加网元，auto_TURK_TKing1"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_TURK_TKing1",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKing",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_TURK_TKing1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_AddNetUnit(self):
		u"""添加网元，auto_TURK_TKing2"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_TURK_TKing2",
				"网元类型": "AUTO",
				"网元IP": "192.168.88.123",
				"生产厂家": "图科",
				"设备型号": "TKing",
				"业务状态": "无业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_TURK_TKing2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_SEARCH",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_26_AddNetUnit(self):
		u"""添加网元，auto_SEARCH_Sight1"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_SEARCH_Sight1",
				"网元类型": "POP",
				"网元IP": "192.168.88.123",
				"生产厂家": "思旗",
				"设备型号": "Sight",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_SEARCH_Sight1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddNetUnit(self):
		u"""添加网元，auto_SEARCH_Sight2"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "auto_SEARCH_Sight2",
				"网元类型": "POP",
				"网元IP": "192.168.88.123",
				"生产厂家": "思旗",
				"设备型号": "Sight",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元，auto_SEARCH_Sight2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_mme_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_29_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitMME1}",
				"网元类型": "MME",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitMME2}",
				"网元类型": "MME",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitMME3}",
				"网元类型": "MME",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_csce_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_33_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitCSCE1}",
				"网元类型": "CSCE",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitCSCE2}",
				"网元类型": "CSCE",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "带业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_AddNetUnit(self):
		u"""添加网元"""
		action = {
			"操作": "AddNetUnit",
			"参数": {
				"网元名称": "${NetunitCSCE3}",
				"网元类型": "CSCE",
				"网元IP": "192.168.88.123",
				"生产厂家": "华为",
				"设备型号": "ME60",
				"业务状态": "无业务",
				"最大并发数": "1"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_NetUnitDataClear(self):
		u"""网元管理，数据清理"""
		action = {
			"操作": "NetUnitDataClear",
			"参数": {
				"网元名称": "auto_test_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		success = Result(self).run_success()
		if not success:
			saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
