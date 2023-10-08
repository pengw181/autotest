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


class MidJumpCmd(unittest.TestCase):

	log.info("装载统一登录指令测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_ssh直连网元"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_ssh直连网元",
				"登录指令用途": "ssh直连网元",
				"指令配置": [
					{
						"操作类型": "删除"
					},
					{
						"操作类型": "添加",
						"指令信息": {
							"指令内容": "%USERNAME",
							"账号名称": "auto_账号_常用账号",
							"期待返回符": "assword",
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_ssh直连网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_telnet直连网元"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_telnet直连网元",
				"登录指令用途": "telnet直连网元",
				"指令配置": [
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_telnet直连网元 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_错误账号"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_错误账号",
				"登录指令用途": "终端使用错误账号",
				"指令配置": [
					{
						"操作类型": "删除"
					},
					{
						"操作类型": "添加",
						"指令信息": {
							"指令内容": "%USERNAME",
							"账号名称": "auto_账号_测试异常账号",
							"期待返回符": "assword",
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
							"账号名称": "auto_账号_测试异常账号",
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_错误账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_空账号"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_空账号",
				"登录指令用途": "终端使用空账号",
				"指令配置": [
					{
						"操作类型": "删除"
					},
					{
						"操作类型": "添加",
						"指令信息": {
							"指令内容": "%USERNAME",
							"账号名称": "auto_账号_空账号模版",
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
							"账号名称": "auto_账号_空账号模版",
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_空账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_跳转指令"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_跳转指令",
				"登录指令用途": "跳转指令",
				"指令配置": [
					{
						"操作类型": "删除"
					},
					{
						"操作类型": "添加",
						"指令信息": {
							"指令内容": "telnet %IP",
							"账号名称": "auto_账号_常用账号",
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_跳转指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddJumpCmdTemp(self):
		u"""添加统一登录指令，auto_登录指令_异常跳转指令"""
		action = {
			"操作": "AddJumpCmdTemp",
			"参数": {
				"登录指令名称": "auto_登录指令_异常跳转指令",
				"登录指令用途": "异常跳转指令",
				"指令配置": [
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
							"隐藏输入指令": "否",
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
							"账号名称": "auto_账号_测试异常账号",
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
							"账号名称": "auto_账号_测试异常账号",
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
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加统一登录指令，auto_登录指令_异常跳转指令 <<<<<')
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
