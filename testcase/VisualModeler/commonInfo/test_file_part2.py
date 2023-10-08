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


class FilePart2(unittest.TestCase):

	log.info("装载文件目录管理测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_MkDir(self):
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

	def test_52_MkDir(self):
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

	def test_53_MkDir(self):
		u"""系统目录创建一级目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "system",
				"目标目录": "system",
				"目录名": "auto_系统一级目录"
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

	def test_54_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "data.xlsx"
			}
		}
		checks = """
		CheckFile|data.xlsx
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "清洗日志.txt"
			}
		}
		checks = """
		CheckFile|清洗日志.txt
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "新冠统计表.xlsx"
			}
		}
		checks = """
		CheckFile|新冠统计表.xlsx
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "weather.xlsx"
			}
		}
		checks = """
		CheckFile|weather.xlsx
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据1w_正常.csv"
			}
		}
		checks = """
		CheckFile|大数据1w_正常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据1w_异常.csv"
			}
		}
		checks = """
		CheckFile|大数据1w_异常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据2w_正常.csv"
			}
		}
		checks = """
		CheckFile|大数据2w_正常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据2w_异常.csv"
			}
		}
		checks = """
		CheckFile|大数据2w_异常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据5w_正常.csv"
			}
		}
		checks = """
		CheckFile|大数据5w_正常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据5w_异常.csv"
			}
		}
		checks = """
		CheckFile|大数据5w_异常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据10w_正常.csv"
			}
		}
		checks = """
		CheckFile|大数据10w_正常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_UploadFile(self):
		u"""个人目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_一级目录",
				"文件名": "大数据10w_异常.csv"
			}
		}
		checks = """
		CheckFile|大数据10w_异常.csv
		"""
		log.info('>>>>> 个人目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_UploadFile(self):
		u"""系统目录上传文件"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "system",
				"目标目录": "auto_系统一级目录",
				"文件名": "request.txt"
			}
		}
		checks = """
		CheckFile|request.txt
		"""
		log.info('>>>>> 系统目录上传文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_DirDataClear(self):
		u"""删除个人目录auto_ocr目录"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录"
			}
		}
		log.info('>>>>> 删除个人目录"auto_ocr目录" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_69_MkDir(self):
		u"""个人目录创建：auto_ocr目录"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "personal",
				"目录名": "auto_ocr目录"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建：auto_ocr目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件012.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "012.jpg"
			}
		}
		checks = """
		CheckFile|012.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件012.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件021.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "021.jpg"
			}
		}
		checks = """
		CheckFile|021.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件021.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件032.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "032.jpg"
			}
		}
		checks = """
		CheckFile|032.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件032.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件034.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "034.jpg"
			}
		}
		checks = """
		CheckFile|034.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件034.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件034_compress.jPG"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "034_compress.jPG"
			}
		}
		checks = """
		CheckFile|034_compress.jPG
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件034_compress.jPG <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件4301.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "4301.jpg"
			}
		}
		checks = """
		CheckFile|4301.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件4301.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件4302.png"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "4302.png"
			}
		}
		checks = """
		CheckFile|4302.png
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件4302.png <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件4303.jpeg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "4303.jpeg"
			}
		}
		checks = """
		CheckFile|4303.jpeg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件4303.jpeg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件034-3.4M.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "034-3.4M.jpg"
			}
		}
		checks = """
		CheckFile|034-3.4M.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件034-3.4M.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件034-70dpi.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "034-70dpi.jpg"
			}
		}
		checks = """
		CheckFile|034-70dpi.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件034-70dpi.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件034-500px.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "034-500px.jpg"
			}
		}
		checks = """
		CheckFile|034-500px.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件034-500px.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_UploadFile(self):
		u"""个人目录auto_ocr目录上传文件047_7000.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"文件类别": "ocr",
				"文件名": "047_7000.jpg"
			}
		}
		checks = """
		CheckFile|047_7000.jpg
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"上传文件047_7000.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_MkDir(self):
		u"""个人目录auto_ocr目录创建二级目录：auto_普通发票"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"目录名": "auto_普通发票"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"创建二级目录：auto_普通发票 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_MkDir(self):
		u"""个人目录auto_ocr目录创建二级目录：auto_专用发票"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_ocr目录",
				"目录名": "auto_专用发票"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录"auto_ocr目录"创建二级目录：auto_专用发票 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_84_UploadFile(self):
		u"""个人目录auto_普通发票上传文件201.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_普通发票",
				"文件类别": "ocr",
				"文件名": "201.jpg"
			}
		}
		checks = """
		CheckFile|201.jpg
		"""
		log.info('>>>>> 个人目录"auto_普通发票"上传文件201.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_85_UploadFile(self):
		u"""个人目录auto_普通发票上传文件222.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_普通发票",
				"文件类别": "ocr",
				"文件名": "222.jpg"
			}
		}
		checks = """
		CheckFile|222.jpg
		"""
		log.info('>>>>> 个人目录"auto_普通发票"上传文件222.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_UploadFile(self):
		u"""个人目录auto_普通发票上传文件225.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_普通发票",
				"文件类别": "ocr",
				"文件名": "225.jpg"
			}
		}
		checks = """
		CheckFile|225.jpg
		"""
		log.info('>>>>> 个人目录"auto_普通发票"上传文件225.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_UploadFile(self):
		u"""个人目录auto_普通发票上传文件226.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_普通发票",
				"文件类别": "ocr",
				"文件名": "226.jpg"
			}
		}
		checks = """
		CheckFile|226.jpg
		"""
		log.info('>>>>> 个人目录"auto_普通发票"上传文件226.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_88_UploadFile(self):
		u"""个人目录auto_普通发票上传文件235.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_普通发票",
				"文件类别": "ocr",
				"文件名": "235.jpg"
			}
		}
		checks = """
		CheckFile|235.jpg
		"""
		log.info('>>>>> 个人目录"auto_普通发票"上传文件235.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_89_UploadFile(self):
		u"""个人目录auto_专用发票上传文件105.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_专用发票",
				"文件类别": "ocr",
				"文件名": "105.jpg"
			}
		}
		checks = """
		CheckFile|105.jpg
		"""
		log.info('>>>>> 个人目录"auto_专用发票"上传文件105.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_90_UploadFile(self):
		u"""个人目录auto_专用发票上传文件109.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_专用发票",
				"文件类别": "ocr",
				"文件名": "109.jpg"
			}
		}
		checks = """
		CheckFile|109.jpg
		"""
		log.info('>>>>> 个人目录"auto_专用发票"上传文件109.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_91_UploadFile(self):
		u"""个人目录auto_专用发票上传文件110.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_专用发票",
				"文件类别": "ocr",
				"文件名": "110.jpg"
			}
		}
		checks = """
		CheckFile|110.jpg
		"""
		log.info('>>>>> 个人目录"auto_专用发票"上传文件110.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_92_UploadFile(self):
		u"""个人目录auto_专用发票上传文件116.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_专用发票",
				"文件类别": "ocr",
				"文件名": "116.jpg"
			}
		}
		checks = """
		CheckFile|116.jpg
		"""
		log.info('>>>>> 个人目录"auto_专用发票"上传文件116.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_93_UploadFile(self):
		u"""个人目录auto_专用发票上传文件122.jpg"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_专用发票",
				"文件类别": "ocr",
				"文件名": "122.jpg"
			}
		}
		checks = """
		CheckFile|122.jpg
		"""
		log.info('>>>>> 个人目录"auto_专用发票"上传文件122.jpg <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_94_DirDataClear(self):
		u"""删除个人目录"""
		action = {
			"操作": "DirDataClear",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI"
			}
		}
		log.info('>>>>> 删除个人目录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_95_MkDir(self):
		u"""个人目录创建目录：auto_AI"""
		action = {
			"操作": "MkDir",
			"参数": {
				"目录分类": "personal",
				"目标目录": "personal",
				"目录名": "auto_AI"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 个人目录创建目录：auto_AI <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_96_UploadFile(self):
		u"""个人目录auto_AI上传文件factorLGBM_predict.csv"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "factorLGBM_predict.csv"
			}
		}
		checks = """
		CheckFile|factorLGBM_predict.csv
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件factorLGBM_predict.csv <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_97_UploadFile(self):
		u"""个人目录auto_AI上传文件factorXGB_predict.csv"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "factorXGB_predict.csv"
			}
		}
		checks = """
		CheckFile|factorXGB_predict.csv
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件factorXGB_predict.csv <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_98_UploadFile(self):
		u"""个人目录auto_AI上传文件factorLGBM_predict.csv"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "factorLGBM_predict.csv"
			}
		}
		checks = """
		CheckFile|factorLGBM_predict.csv
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件factorLGBM_predict.csv <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_99_UploadFile(self):
		u"""个人目录auto_AI上传文件single_predict.xlsx"""
		action = {
			"操作": "UploadFile",
			"参数": {
				"目录分类": "personal",
				"目标目录": "auto_AI",
				"文件类别": "predict",
				"文件名": "single_predict.xlsx"
			}
		}
		checks = """
		CheckFile|single_predict.xlsx
		"""
		log.info('>>>>> 个人目录"auto_AI"上传文件single_predict.xlsx <<<<<')
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
