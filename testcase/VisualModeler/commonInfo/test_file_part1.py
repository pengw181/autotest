# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:10

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class FilePart1(unittest.TestCase):

	log.info("装载文件目录管理测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_DirDataClear(self):
		u"""个人目录清理"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录"
			}
		}
		log.info('>>>>> 个人目录清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_DirDataClear(self):
		u"""系统目录清理"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录"
			}
		}
		log.info('>>>>> 系统目录清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_3_MkDir(self):
		u"""个人目录创建一级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "personal",
				"目录名": "auto_一级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建一级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_MkDir(self):
		u"""同级下创建同名目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "personal",
				"目录名": "auto_一级目录"
			}
		}
		checks = """
		CheckMsg|目录已经存在
		"""
		log.info('>>>>> 同级下创建同名目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_MkDir(self):
		u"""个人目录创建二级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"目录名": "auto_二级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建二级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_MkDir(self):
		u"""个人目录创建三级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "auto_三级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建三级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_MkDir(self):
		u"""个人目录一次创建三级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"目录名": "auto_a级目录/auto_b级目录/auto_c级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录一次创建三级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_MkDir(self):
		u"""不同层级下创建同名目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "auto_b级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 不同层级下创建同名目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_MkDir(self):
		u"""个人目录创建，目录名格式为./目录名"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "./auto_三级目录2"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建，目录名格式为./目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_MkDir(self):
		u"""个人目录创建，目录名格式为../目录名"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "../auto_二级目录2"
			}
		}
		checks = """
		CheckMsg|请输入正确的目录名称
		"""
		log.info('>>>>> 个人目录创建，目录名格式为../目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_UpdateDir(self):
		u"""修改一级目录名"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"目录名": "auto_一级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改一级目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_UpdateDir(self):
		u"""修改二级目录名,同级下目录名已存在"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "auto_a级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改二级目录名,同级下目录名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_UpdateDir(self):
		u"""修改二级目录名,同级下目录名不存在"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录",
				"目录名": "auto_二级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改二级目录名,同级下目录名不存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_UpdateDir(self):
		u"""修改三级目录名"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_三级目录",
				"目录名": "auto_三级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改三级目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UploadFile(self):
		u"""在一级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 在一级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UploadFile(self):
		u"""在一级目录下上传文件,该目录下文件已存在"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 在一级目录下上传文件,该目录下文件已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_UploadFile(self):
		u"""在二级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_二级目录新",
				"文件名": "disturb_file_test.csv"
			}
		}
		checks = """
		CheckFile|disturb_file_test.csv
		"""
		log.info('>>>>> 在二级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_UploadFile(self):
		u"""在三级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_三级目录新",
				"文件名": "factor.xlsx"
			}
		}
		checks = """
		CheckFile|factor.xlsx
		"""
		log.info('>>>>> 在三级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_DownloadFile(self):
		u"""下载文件"""
		action = {
			"操作": "DownloadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckDownloadFile|request|txt
		"""
		log.info('>>>>> 下载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_DeleteFile(self):
		u"""删除文件"""
		action = {
			"操作": "DeleteFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckMsg|删除文件成功
		"""
		log.info('>>>>> 删除文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_UploadFile(self):
		u"""在一级目录下上传xlsx文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "factor.xlsx"
			}
		}
		checks = """
		CheckFile|factor.xlsx
		"""
		log.info('>>>>> 在一级目录下上传xlsx文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_UploadFile(self):
		u"""在一级目录下上传csv文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": "disturb_file_test.csv"
			}
		}
		checks = """
		CheckFile|disturb_file_test.csv
		"""
		log.info('>>>>> 在一级目录下上传csv文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_DownloadFileBatch(self):
		u"""批量下载文件"""
		action = {
			"操作": "DownloadFileBatch",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": [
					"factor.xlsx",
					"disturb_file_test.csv"
				]
			}
		}
		checks = """
		CheckDownloadFile|批量下载文件|zip
		"""
		log.info('>>>>> 批量下载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_DeleteFileBatch(self):
		u"""批量删除文件"""
		action = {
			"操作": "DeleteFileBatch",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新",
				"文件名": [
					"factor.xlsx",
					"disturb_file_test.csv"
				]
			}
		}
		checks = """
		CheckMsg|批量删除文件成功
		"""
		log.info('>>>>> 批量删除文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_DeleteDir(self):
		u"""删除目录,目录下无子目录"""
		action = {
			"操作": "DeleteDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_c级目录"
			}
		}
		checks = """
		CheckMsg|删除目录成功
		"""
		log.info('>>>>> 删除目录,目录下无子目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_DeleteDir(self):
		u"""删除目录,目录下有子目录"""
		action = {
			"操作": "DeleteDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录新"
			}
		}
		checks = """
		CheckMsg|删除目录成功
		"""
		log.info('>>>>> 删除目录,目录下有子目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_MkDir(self):
		u"""系统目录创建一级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "system",
				"目录名": "auto_一级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 系统目录创建一级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_MkDir(self):
		u"""同级下创建同名目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "system",
				"目录名": "auto_一级目录"
			}
		}
		checks = """
		CheckMsg|目录已经存在
		"""
		log.info('>>>>> 同级下创建同名目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_MkDir(self):
		u"""系统目录创建二级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录",
				"目录名": "auto_二级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 系统目录创建二级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_MkDir(self):
		u"""系统目录创建三级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_二级目录",
				"目录名": "auto_三级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 系统目录创建三级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_MkDir(self):
		u"""系统目录一次创建三级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录",
				"目录名": "auto_a级目录/auto_b级目录/auto_c级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 系统目录一次创建三级目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_MkDir(self):
		u"""不同层级下创建同名目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_二级目录",
				"目录名": "auto_b级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 不同层级下创建同名目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_UpdateDir(self):
		u"""修改一级目录名"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录",
				"目录名": "auto_一级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改一级目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_UpdateDir(self):
		u"""修改二级目录名,同级下目录名已存在"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_二级目录",
				"目录名": "auto_a级目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改二级目录名,同级下目录名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_UpdateDir(self):
		u"""修改二级目录名,同级下目录名不存在"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_二级目录",
				"目录名": "auto_二级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改二级目录名,同级下目录名不存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_UpdateDir(self):
		u"""修改三级目录名"""
		action = {
			"操作": "UpdateDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_三级目录",
				"目录名": "auto_三级目录新"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改三级目录名 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_UploadFile(self):
		u"""在一级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 在一级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_UploadFile(self):
		u"""在一级目录下上传文件,该目录下文件已存在"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 在一级目录下上传文件,该目录下文件已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_UploadFile(self):
		u"""在二级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_二级目录新",
				"文件名": "disturb_file_test.csv"
			}
		}
		checks = """
		CheckFile|disturb_file_test.csv
		"""
		log.info('>>>>> 在二级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_UploadFile(self):
		u"""在三级目录下上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_三级目录新",
				"文件名": "factor.xlsx"
			}
		}
		checks = """
		CheckFile|factor.xlsx
		"""
		log.info('>>>>> 在三级目录下上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_DownloadFile(self):
		u"""下载文件"""
		action = {
			"操作": "DownloadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckDownloadFile|request|txt
		"""
		log.info('>>>>> 下载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_DeleteFile(self):
		u"""删除文件"""
		action = {
			"操作": "DeleteFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckMsg|删除文件成功
		"""
		log.info('>>>>> 删除文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_UploadFile(self):
		u"""在一级目录下上传xlsx文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "factor.xlsx"
			}
		}
		checks = """
		CheckFile|factor.xlsx
		"""
		log.info('>>>>> 在一级目录下上传xlsx文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_UploadFile(self):
		u"""在一级目录下上传csv文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": "disturb_file_test.csv"
			}
		}
		checks = """
		CheckFile|disturb_file_test.csv
		"""
		log.info('>>>>> 在一级目录下上传csv文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_DownloadFileBatch(self):
		u"""批量下载文件"""
		action = {
			"操作": "DownloadFileBatch",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": [
					"factor.xlsx",
					"disturb_file_test.csv"
				]
			}
		}
		checks = """
		CheckDownloadFile|批量下载文件|zip
		"""
		log.info('>>>>> 批量下载文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_DeleteFileBatch(self):
		u"""批量删除文件"""
		action = {
			"操作": "DeleteFileBatch",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新",
				"文件名": [
					"factor.xlsx",
					"disturb_file_test.csv"
				]
			}
		}
		checks = """
		CheckMsg|批量删除文件成功
		"""
		log.info('>>>>> 批量删除文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_DeleteDir(self):
		u"""删除目录,目录下无子目录"""
		action = {
			"操作": "DeleteDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_c级目录"
			}
		}
		checks = """
		CheckMsg|删除目录成功
		"""
		log.info('>>>>> 删除目录,目录下无子目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_DeleteDir(self):
		u"""删除目录,目录下有子目录"""
		action = {
			"操作": "DeleteDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_一级目录新"
			}
		}
		checks = """
		CheckMsg|删除目录成功
		"""
		log.info('>>>>> 删除目录,目录下有子目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_DirDataClear(self):
		u"""删除个人目录"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录"
			}
		}
		log.info('>>>>> 删除个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_50_DirDataClear(self):
		u"""删除系统目录"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_系统一级目录"
			}
		}
		log.info('>>>>> 删除系统目录 <<<<<')
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
