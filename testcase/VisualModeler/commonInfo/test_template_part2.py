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


class TemplatePart2(unittest.TestCase):

	log.info("装载网元模版配置测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_ZgAddData(self):
		u"""网元基础信息，数据管理，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"数据信息": [
					[
						"网元名称",
						"${NetunitAUTO1}"
					],
					[
						"网元类型",
						"MME"
					],
					[
						"网元IP",
						"192.168.88.123"
					],
					[
						"生产厂家",
						"华为"
					],
					[
						"设备型号",
						"ME60"
					],
					[
						"业务状态",
						"带业务"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_ZgAddData(self):
		u"""网元基础信息，数据管理，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"数据信息": [
					[
						"网元名称",
						"${NetunitAUTO2}"
					],
					[
						"网元类型",
						"MME"
					],
					[
						"网元IP",
						"192.168.88.123"
					],
					[
						"生产厂家",
						"华为"
					],
					[
						"设备型号",
						"ME60"
					],
					[
						"业务状态",
						"带业务"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_ZgAddData(self):
		u"""网元基础信息，数据管理，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"数据信息": [
					[
						"网元名称",
						"${NetunitAUTO3}"
					],
					[
						"网元类型",
						"MME"
					],
					[
						"网元IP",
						"192.168.88.123"
					],
					[
						"生产厂家",
						"华为"
					],
					[
						"设备型号",
						"ME60"
					],
					[
						"业务状态",
						"带业务"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，二次确认，确认通过"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO1}",
					"${NetunitAUTO2}",
					"${NetunitAUTO3}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，二次确认，确认通过 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_ZgDownloadTempl(self):
		u"""网元基础信息，数据管理，导入数据，下载模版"""
		action = {
			"操作": "ZgDownloadTempl",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		checks = """
		CheckDownloadFile|网元基础信息auto_网元基础信息表模板文件|xlsx
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据，下载模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_ZgUploadData(self):
		u"""网元基础信息，数据管理，导入数据"""
		action = {
			"操作": "ZgUploadData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"文件路径": "网元基础信息auto_网元基础信息表.xlsx"
			}
		}
		checks = """
		CheckMsg|文件导入成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_ZgDataRevokeAll(self):
		u"""网元基础信息，数据管理，导入数据，二次确认，撤销所有"""
		action = {
			"操作": "ZgDataRevokeAll",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		checks = """
		CheckMsg|撤销成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据，二次确认，撤销所有 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_ZgUploadData(self):
		u"""网元基础信息，数据管理，导入数据，数据正常"""
		action = {
			"操作": "ZgUploadData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"文件路径": "网元基础信息auto_网元基础信息表.xlsx"
			}
		}
		checks = """
		CheckMsg|文件导入成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据，数据正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，导入数据，二次确认，确认部分"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO4}",
					"${NetunitAUTO5}",
					"${NetunitAUTO6}",
					"${NetunitAUTO7}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据，二次确认，确认部分 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_ZgDataConfirmAll(self):
		u"""网元基础信息，数据管理，导入数据，二次确认，确认所有"""
		action = {
			"操作": "ZgDataConfirmAll",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，导入数据，二次确认，确认所有 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_ZgExportData(self):
		u"""网元基础信息，导出数据"""
		action = {
			"操作": "ZgExportData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		checks = """
		CheckDownloadFile|auto_网元基础信息表网元基础信息|csv
		"""
		log.info('>>>>> 网元基础信息，导出数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_ZgListData(self):
		u"""网元基础信息，数据管理，按网元名称查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元名称": "${NetunitAUTO2}"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按网元名称查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_ZgListData(self):
		u"""网元基础信息，数据管理，按网元IP查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元IP": "192.168.88.123"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按网元IP查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_ZgListData(self):
		u"""网元基础信息，数据管理，按业务状态查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"业务状态": "带业务"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按业务状态查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_ZgListData(self):
		u"""网元基础信息，数据管理，按网元类型查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元类型": "AUTO"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按网元类型查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_ZgListData(self):
		u"""网元基础信息，数据管理，按生产厂家查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"生产厂家": "华为"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按生产厂家查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_ZgListData(self):
		u"""网元基础信息，数据管理，按生产厂家、设备型号查询"""
		action = {
			"操作": "ZgListData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"生产厂家": "华为",
					"设备型号": "ME60"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元基础信息，数据管理，按生产厂家、设备型号查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_ZgAddData(self):
		u"""网元辅助资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME1}"
					],
					[
						"列1",
						"www.baidu.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_ZgAddData(self):
		u"""网元辅助资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME1}"
					],
					[
						"列1",
						"www.sina.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_ZgAddData(self):
		u"""网元辅助资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME2}"
					],
					[
						"列1",
						"www.huya.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_ZgAddData(self):
		u"""网元辅助资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME3}"
					],
					[
						"列1",
						"www.baidu.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_ZgUpdateData(self):
		u"""网元辅助资料，修改数据"""
		action = {
			"操作": "ZgUpdateData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"网元名称": "${NetunitMME3}",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME2}"
					],
					[
						"列1",
						"www.douyu.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，修改数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_ZgAddData(self):
		u"""网元辅助资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"数据信息": [
					[
						"网元名称",
						"${NetunitMME3}"
					],
					[
						"列1",
						"www.baidu.com"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元辅助资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_ZgDeleteData(self):
		u"""网元辅助资料，删除数据"""
		action = {
			"操作": "ZgDeleteData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"查询条件": {
					"网元名称": "${NetunitMME3}"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元辅助资料，删除数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_ZgDownloadTempl(self):
		u"""网元辅助资料，数据管理，导入数据，下载模版"""
		action = {
			"操作": "ZgDownloadTempl",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料"
			}
		}
		checks = """
		CheckDownloadFile|网元辅助资料auto_网元辅助资料模板文件|xlsx
		"""
		log.info('>>>>> 网元辅助资料，数据管理，导入数据，下载模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_ZgUploadData(self):
		u"""网元辅助资料，导入数据"""
		action = {
			"操作": "ZgUploadData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"文件路径": "网元辅助资料auto_网元辅助资料.xlsx"
			}
		}
		checks = """
		CheckMsg|文件导入成功
		"""
		log.info('>>>>> 网元辅助资料，导入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_ZgExportData(self):
		u"""网元辅助资料，导出数据"""
		action = {
			"操作": "ZgExportData",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料"
			}
		}
		checks = """
		CheckDownloadFile|auto_网元辅助资料网元辅助资料|csv
		"""
		log.info('>>>>> 网元辅助资料，导出数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_ZgClearData(self):
		u"""网元其它资料，清空数据"""
		action = {
			"操作": "ZgClearData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元其它资料，清空数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_ZgAddData(self):
		u"""网元其它资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"数据信息": [
					[
						"列1",
						"theophilus"
					],
					[
						"列2",
						"c01"
					],
					[
						"列3",
						"88"
					],
					[
						"列4",
						"95"
					],
					[
						"列5",
						"90"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元其它资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_ZgAddData(self):
		u"""网元其它资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"数据信息": [
					[
						"列1",
						"theophilus"
					],
					[
						"列2",
						"c02"
					],
					[
						"列3",
						"81"
					],
					[
						"列4",
						"85"
					],
					[
						"列5",
						"70"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元其它资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_ZgAddData(self):
		u"""网元其它资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"数据信息": [
					[
						"列1",
						"jabara"
					],
					[
						"列2",
						"c01"
					],
					[
						"列3",
						"83"
					],
					[
						"列4",
						"91"
					],
					[
						"列5",
						"97"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元其它资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_ZgAddData(self):
		u"""网元其它资料，添加数据"""
		action = {
			"操作": "ZgAddData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"数据信息": [
					[
						"列1",
						"luna"
					],
					[
						"列2",
						"c01"
					],
					[
						"列3",
						"82"
					],
					[
						"列4",
						"81"
					],
					[
						"列5",
						"87"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元其它资料，添加数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_ZgDeleteData(self):
		u"""网元其它资料，数据管理，删除数据"""
		action = {
			"操作": "ZgDeleteData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"查询条件": {
					"列1": "theophilus"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元其它资料，数据管理，删除数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_84_ZgClearData(self):
		u"""网元其它资料，数据管理，清空数据"""
		action = {
			"操作": "ZgClearData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元其它资料，数据管理，清空数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_85_ZgDownloadTempl(self):
		u"""网元其它资料，数据管理，导入数据，下载模版"""
		action = {
			"操作": "ZgDownloadTempl",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckDownloadFile|网元其它资料auto_网元其它资料_vm仪表盘模板文件|xlsx
		"""
		log.info('>>>>> 网元其它资料，数据管理，导入数据，下载模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_ZgUploadData(self):
		u"""网元其它资料，数据管理，导入数据"""
		action = {
			"操作": "ZgUploadData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"文件路径": "网元其它资料auto_网元其它资料_vm仪表盘.xlsx"
			}
		}
		checks = """
		CheckMsg|文件导入成功
		"""
		log.info('>>>>> 网元其它资料，数据管理，导入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_ZgExportData(self):
		u"""网元其它资料，导出数据"""
		action = {
			"操作": "ZgExportData",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckDownloadFile|auto_网元其它资料_vm仪表盘网元其它资料|csv
		"""
		log.info('>>>>> 网元其它资料，导出数据 <<<<<')
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
