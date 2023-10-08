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


class OrgManager(unittest.TestCase):

	log.info("装载组织机构管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_UserDataClear(self):
		u"""用户数据清理，删除历史数据"""
		action = {
			"操作": "UserDataClear",
			"参数": {
				"登录账号": "auto",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 用户数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_ClearOrganization(self):
		u"""用户管理，组织机构配置，数据清理"""
		action = {
			"操作": "ClearOrganization",
			"参数": {
				"节点名称": "广州事业部"
			}
		}
		log.info('>>>>> 用户管理，组织机构配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_3_AddOrganization(self):
		u"""用户管理，添加组织机构：广州事业部"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "${Belong}",
				"组织名称": "广州事业部"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：广州事业部 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddOrganization(self):
		u"""用户管理，添加组织机构：海珠区事业办"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "广州事业部",
				"组织名称": "海珠区事业办"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：海珠区事业办 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddOrganization(self):
		u"""用户管理，添加组织机构，同级下名称已存在"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "广州事业部",
				"组织名称": "海珠区事业办"
			}
		}
		checks = """
		CheckMsg|该组织名称已存在，请重新命名
		"""
		log.info('>>>>> 用户管理，添加组织机构，同级下名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddOrganization(self):
		u"""用户管理，添加组织机构：黄埔区事业办"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "广州事业部",
				"组织名称": "黄埔区事业办"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：黄埔区事业办 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddOrganization(self):
		u"""用户管理，添加组织机构：广州塔办公室"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "海珠区事业办",
				"组织名称": "广州塔办公室"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：广州塔办公室 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddOrganization(self):
		u"""用户管理，添加组织机构：鱼珠办公室，指定上层组织"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "海珠区事业办",
				"上级组织": "黄埔区事业办",
				"组织名称": "鱼珠办公室"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：鱼珠办公室，指定上层组织 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateOrganization(self):
		u"""用户管理，修改组织机构，指定上层组织"""
		action = {
			"操作": "UpdateOrganization",
			"参数": {
				"节点名称": "广州塔办公室",
				"上级组织": "黄埔区事业办",
				"组织名称": "广州塔办公室2"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，修改组织机构，指定上层组织 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_DeleteOrganization(self):
		u"""用户管理，删除组织机构"""
		action = {
			"操作": "DeleteOrganization",
			"参数": {
				"节点名称": "广州塔办公室2"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 用户管理，删除组织机构 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddOrganization(self):
		u"""用户管理，添加组织机构：广州塔办公室"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "海珠区事业办",
				"组织名称": "广州塔办公室"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：广州塔办公室 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddOrganization(self):
		u"""用户管理，添加组织机构：中山大学办公室"""
		action = {
			"操作": "AddOrganization",
			"参数": {
				"节点名称": "海珠区事业办",
				"组织名称": "中山大学办公室"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 用户管理，添加组织机构：中山大学办公室 <<<<<')
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
