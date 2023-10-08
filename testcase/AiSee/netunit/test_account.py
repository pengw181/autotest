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


class Account(unittest.TestCase):

	log.info("装载统一账号配置测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AddAccountTemp(self):
		u"""添加账号模版，auto_账号_常用账号"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号模版类型": "本身",
				"账号模版用途": "登录系统",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加账号模版，auto_账号_常用账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_AddAccountTemp(self):
		u"""添加账号模版，auto_账号_测试异常账号"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_测试异常账号",
				"账号模版类型": "中转",
				"账号模版用途": "测试异常情况",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加账号模版，auto_账号_测试异常账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddAccountTemp(self):
		u"""添加账号模版，重复添加"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_测试异常账号",
				"账号模版类型": "中转",
				"账号模版用途": "登录系统"
			}
		}
		checks = """
		CheckMsg|账号名称已存在
		"""
		log.info('>>>>> 添加账号模版，重复添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AccountDataClear(self):
		u"""账号清理，账号模版：auto_账号_常用账号"""
		action = {
			"操作": "AccountDataClear",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"创建人": "${CurrentUser}"
			}
		}
		log.info('>>>>> 账号清理，账号模版：auto_账号_常用账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_5_AddAccount(self):
		u"""添加账号，公有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "公有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddAccount(self):
		u"""添加账号，私有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "私有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddAccount(self):
		u"""添加账号，当前账号模版存在公有账号，且本人已创建过私有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "私有",
				"用户名": "u_normal2",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加失败，您的公有、私有账号均已存在
		"""
		log.info('>>>>> 添加账号，当前账号模版存在公有账号，且本人已创建过私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateAccount(self):
		u"""修改账号，修改公有账号"""
		action = {
			"操作": "UpdateAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "公有",
				"修改内容": {
					"用户名": "u_normal1",
					"密码": "u_normal_pass1"
				}
			}
		}
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改账号，修改公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateAccount(self):
		u"""修改账号，修改私有账号"""
		action = {
			"操作": "UpdateAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "私有",
				"创建人": "${CurrentUser}",
				"修改内容": {
					"用户名": "u_normal2",
					"密码": "u_normal_pass2"
				}
			}
		}
		checks = """
		CheckMsg|修改成功
		"""
		log.info('>>>>> 修改账号，修改私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_DeleteAccount(self):
		u"""删除账号，公有账号"""
		action = {
			"操作": "DeleteAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "公有",
				"创建人": "${CurrentUser}"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除账号，公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteAccount(self):
		u"""删除账号，私有账号"""
		action = {
			"操作": "DeleteAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "私有",
				"创建人": "${CurrentUser}"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除账号，私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddAccount(self):
		u"""添加账号，公有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "公有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddAccount(self):
		u"""添加账号，私有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_常用账号",
				"账号作用域": "私有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AccountDataClear(self):
		u"""账号清理，账号模版：auto_账号_测试异常账号"""
		action = {
			"操作": "AccountDataClear",
			"参数": {
				"账号模版名称": "auto_账号_测试异常账号",
				"创建人": "${CurrentUser}"
			}
		}
		log.info('>>>>> 账号清理，账号模版：auto_账号_测试异常账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_15_AddAccount(self):
		u"""添加账号，公有账号，错误用户名"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_测试异常账号",
				"账号作用域": "公有",
				"用户名": "u_normal1",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，公有账号，错误用户名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddAccount(self):
		u"""添加账号，私有账号，错误密码"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_测试异常账号",
				"账号作用域": "私有",
				"用户名": "u_normal",
				"密码": "u_normal_pass1"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，私有账号，错误密码 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddAccountTemp(self):
		u"""添加账号模版，auto_账号_空账号模版"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_空账号模版",
				"账号模版类型": "中转",
				"账号模版用途": "空账号模版",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加账号模版，auto_账号_空账号模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AccountDataClear(self):
		u"""账号清理，账号模版：auto_账号_空账号模版"""
		action = {
			"操作": "AccountDataClear",
			"参数": {
				"账号模版名称": "auto_账号_空账号模版",
				"创建人": "${CurrentUser}"
			}
		}
		log.info('>>>>> 账号清理，账号模版：auto_账号_空账号模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_19_AddAccountTemp(self):
		u"""添加账号模版，auto_账号_公有账号"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_公有账号",
				"账号模版类型": "中转",
				"账号模版用途": "只含公有账号",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加账号模版，auto_账号_公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AccountDataClear(self):
		u"""账号清理，账号模版：auto_账号_公有账号"""
		action = {
			"操作": "AccountDataClear",
			"参数": {
				"账号模版名称": "auto_账号_公有账号",
				"创建人": "${CurrentUser}"
			}
		}
		log.info('>>>>> 账号清理，账号模版：auto_账号_公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_21_AddAccount(self):
		u"""添加账号，公有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_公有账号",
				"账号作用域": "公有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，公有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddAccountTemp(self):
		u"""添加账号模版，auto_账号_私有账号"""
		action = {
			"操作": "AddAccountTemp",
			"参数": {
				"账号模版名称": "auto_账号_私有账号",
				"账号模版类型": "中转",
				"账号模版用途": "只含私有账号",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加账号模版，auto_账号_私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AccountDataClear(self):
		u"""账号清理，账号模版：auto_账号_私有账号"""
		action = {
			"操作": "AccountDataClear",
			"参数": {
				"账号模版名称": "auto_账号_私有账号",
				"创建人": "${CurrentUser}"
			}
		}
		log.info('>>>>> 账号清理，账号模版：auto_账号_私有账号 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_24_AddAccount(self):
		u"""添加账号，私有账号"""
		action = {
			"操作": "AddAccount",
			"参数": {
				"账号模版名称": "auto_账号_私有账号",
				"账号作用域": "私有",
				"用户名": "u_normal",
				"密码": "u_normal_pass"
			}
		}
		checks = """
		CheckMsg|添加成功
		"""
		log.info('>>>>> 添加账号，私有账号 <<<<<')
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
