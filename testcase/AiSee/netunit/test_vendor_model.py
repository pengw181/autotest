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


class VendorModel(unittest.TestCase):

	log.info("装载设备厂家测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_AddVendor(self):
		u"""添加厂家，测试"""
		action = {
			"操作": "AddVendor",
			"参数": {
				"厂家中文名": "测试",
				"厂家英文名": "TEST",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加厂家，测试 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_2_AddVendor(self):
		u"""添加厂家，图科"""
		action = {
			"操作": "AddVendor",
			"参数": {
				"厂家中文名": "图科",
				"厂家英文名": "TURK",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加厂家，图科 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddVendor(self):
		u"""添加厂家，思旗"""
		action = {
			"操作": "AddVendor",
			"参数": {
				"厂家中文名": "思旗",
				"厂家英文名": "SEARCH",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加厂家，思旗 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddVendor(self):
		u"""添加厂家，重复添加"""
		action = {
			"操作": "AddVendor",
			"参数": {
				"厂家中文名": "思旗",
				"厂家英文名": "SEARCH1"
			}
		}
		checks = """
		CheckMsg|厂家已存在
		"""
		log.info('>>>>> 添加厂家，重复添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_UpdateVendor(self):
		u"""修改厂家，思旗"""
		action = {
			"操作": "UpdateVendor",
			"参数": {
				"查询条件": {
					"厂家": "思旗"
				},
				"修改内容": {
					"厂家中文名": "思旗二代",
					"厂家英文名": "SEARCH2"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改厂家，思旗 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_UpdateVendor(self):
		u"""修改厂家，中文名已存在"""
		action = {
			"操作": "UpdateVendor",
			"参数": {
				"查询条件": {
					"厂家": "思旗二代"
				},
				"修改内容": {
					"厂家中文名": "图科",
					"厂家英文名": "SEARCH2"
				}
			}
		}
		checks = """
		CheckMsg|厂家已存在
		"""
		log.info('>>>>> 修改厂家，中文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateVendor(self):
		u"""修改厂家，英文名已存在"""
		action = {
			"操作": "UpdateVendor",
			"参数": {
				"查询条件": {
					"厂家": "思旗二代"
				},
				"修改内容": {
					"厂家中文名": "思旗",
					"厂家英文名": "TURK"
				}
			}
		}
		checks = """
		CheckMsg|厂家已存在
		"""
		log.info('>>>>> 修改厂家，英文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateVendor(self):
		u"""修改厂家，改回正常值"""
		action = {
			"操作": "UpdateVendor",
			"参数": {
				"查询条件": {
					"厂家": "思旗二代"
				},
				"修改内容": {
					"厂家中文名": "思旗",
					"厂家英文名": "SEARCH"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改厂家，改回正常值 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddModel(self):
		u"""添加设备型号，厂家：图科，设备型号：TKing"""
		action = {
			"操作": "AddModel",
			"参数": {
				"所属厂家": "图科",
				"设备型号": "TKing",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加设备型号，厂家：图科，设备型号：TKing <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddModel(self):
		u"""添加设备型号，厂家：图科，设备型号：TKea"""
		action = {
			"操作": "AddModel",
			"参数": {
				"所属厂家": "图科",
				"设备型号": "TKea",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加设备型号，厂家：图科，设备型号：TKea <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddModel(self):
		u"""添加设备型号，厂家：思旗，设备型号：Sight"""
		action = {
			"操作": "AddModel",
			"参数": {
				"所属厂家": "思旗",
				"设备型号": "Sight",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加设备型号，厂家：思旗，设备型号：Sight <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddModel(self):
		u"""添加设备型号，厂家：测试，设备型号：AutoTest"""
		action = {
			"操作": "AddModel",
			"参数": {
				"所属厂家": "测试",
				"设备型号": "AutoTest",
				"搜索是否存在": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加设备型号，厂家：测试，设备型号：AutoTest <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddModel(self):
		u"""添加设备型号，重复添加"""
		action = {
			"操作": "AddModel",
			"参数": {
				"所属厂家": "图科",
				"设备型号": "TKea"
			}
		}
		checks = """
		CheckMsg|设备型号已存在
		"""
		log.info('>>>>> 添加设备型号，重复添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_UpdateModel(self):
		u"""修改设备型号，同厂家下设备型号已存在"""
		action = {
			"操作": "UpdateModel",
			"参数": {
				"查询条件": {
					"厂家": "图科",
					"设备型号": "TKea"
				},
				"修改内容": {
					"设备型号": "TKing"
				}
			}
		}
		checks = """
		CheckMsg|设备型号已存在
		"""
		log.info('>>>>> 修改设备型号，同厂家下设备型号已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UpdateModel(self):
		u"""修改设备型号，不同厂家下设备型号已存在"""
		action = {
			"操作": "UpdateModel",
			"参数": {
				"查询条件": {
					"厂家": "图科",
					"设备型号": "TKea"
				},
				"修改内容": {
					"设备型号": "Sight"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改设备型号，不同厂家下设备型号已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UpdateModel(self):
		u"""修改设备型号，改回原值"""
		action = {
			"操作": "UpdateModel",
			"参数": {
				"查询条件": {
					"厂家": "图科",
					"设备型号": "Sight"
				},
				"修改内容": {
					"设备型号": "TKea"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 修改设备型号，改回原值 <<<<<')
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
