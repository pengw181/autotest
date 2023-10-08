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


class ScriptPart2(unittest.TestCase):

	log.info("装载脚本管理测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_ScriptFileRClick(self):
		u"""java脚本删除版本2的脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "2",
				"脚本文件名": "readfile1.java",
				"右键": "删除脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|2
		"""
		log.info('>>>>> java脚本删除版本2的脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_UploadScriptFile(self):
		u"""java脚本上传脚本文件,读取system目录下的文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "2",
				"脚本文件名": "readfile2.java"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|2|file_name|readfile2.java|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> java脚本上传脚本文件,读取system目录下的文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_SubmitScriptApproval(self):
		u"""java脚本版本2提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "2"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> java脚本版本2提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_SaveNewScriptVersion(self):
		u"""java脚本保存新版本"""
		action = {
			"操作": "SaveNewScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|3|version_status|01|version_desc|编辑版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> java脚本保存新版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_ScriptFileRClick(self):
		u"""java脚本删除版本3的脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "3",
				"脚本文件名": "readfile1.java",
				"右键": "删除脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|3
		"""
		log.info('>>>>> java脚本删除版本3的脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_UploadScriptFile(self):
		u"""java脚本上传脚本文件,读取绝对路径下的文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "3",
				"脚本文件名": "readfilejd.java"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|3|file_name|readfilejd.java|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> java脚本上传脚本文件,读取绝对路径下的文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_SubmitScriptApproval(self):
		u"""java脚本版本3提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "3"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> java脚本版本3提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_ScriptDataClear(self):
		u"""脚本管理,数据清理,清除jar脚本"""
		action = {
			"操作": "ScriptDataClear",
			"参数": {
				"脚本名称": "auto_脚本jar"
			}
		}
		log.info('>>>>> 脚本管理,数据清理,清除jar脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_59_AddScript(self):
		u"""添加脚本,类型jar"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"脚本类型": "jar",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本jar|script_type|3|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型jar <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_UploadScriptFile(self):
		u"""jar脚本上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"版本号": "1",
				"脚本文件名": "CompareDataUtil.jar"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本jar'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|CompareDataUtil.jar|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> jar脚本上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_SubmitScriptApproval(self):
		u"""jar脚本版本1提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> jar脚本版本1提交审批 <<<<<')
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
