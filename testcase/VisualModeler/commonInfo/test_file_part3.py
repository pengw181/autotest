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


class FilePart3(unittest.TestCase):

	log.info("装载文件目录管理测试用例（3）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_100_UploadFile(self):
		u"""个人目录auto_AI上传文件factor_predict.xlsx"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "factor_predict.xlsx"
			}
		}
		checks = """
		CheckFile|factor_predict.xlsx
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件factor_predict.xlsx <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_101_UploadFile(self):
		u"""个人目录auto_AI上传文件classical_predict.xlsx"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "classical_predict.xlsx"
			}
		}
		checks = """
		CheckFile|classical_predict.xlsx
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件classical_predict.xlsx <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_102_DirDataClear(self):
		u"""删除个人目录"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_全流程"
			}
		}
		log.info('>>>>> 删除个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_103_MkDir(self):
		u"""个人目录创建一级目录：auto_全流程"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "personal",
				"目录名": "auto_全流程"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建一级目录：auto_全流程 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_104_MkDir(self):
		u"""个人目录创建二级目录：auto_临时目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_全流程",
				"目录名": "auto_临时目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建二级目录：auto_临时目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_105_MkDir(self):
		u"""添加目录，目录名包含./"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_临时目录",
				"目录名": "./back"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 添加目录，目录名包含./ <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_106_MkDir(self):
		u"""添加目录，目录名包含../"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_临时目录",
				"目录名": "../back"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 添加目录，目录名包含../ <<<<<')
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
