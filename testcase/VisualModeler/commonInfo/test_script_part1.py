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


class ScriptPart1(unittest.TestCase):

	log.info("装载脚本管理测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ScriptDataClear(self):
		u"""脚本管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
		${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
		${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python'
		${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java')
		${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java')
		${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java'
		${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar')
		${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar')
		${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar'
		"""
		action = {
			"操作": "ScriptDataClear",
			"参数": {
				"脚本名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 脚本管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddScript(self):
		u"""添加脚本,类型python"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本python",
				"脚本类型": "python",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python|script_type|2|data_type_id|1|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型python <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddScript(self):
		u"""添加脚本,类型java"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本java",
				"脚本类型": "java",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本java|script_type|1|data_type_id|1|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型java <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddScript(self):
		u"""添加脚本,类型jar"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"脚本类型": "jar",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本jar|script_type|3|data_type_id|1|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型jar <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddScript(self):
		u"""添加脚本,脚本名称在本领域存在"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本python",
				"脚本类型": "python",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加脚本,脚本名称在本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddScript(self):
		u"""添加脚本,脚本名称在本领域不存在,在其他领域存在"""
		pres = """
		${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
		${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
		${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python' 
		${Database}.main|insert into tn_script_cfg(script_id,script_name,script_type,data_type_id,create_time,update_time,creater,updater,original_user_id,original_time,belong_id,domain_id) values(uuid(),'auto_脚本python',2,1,now(),now(),'pw','pw','pw',now(),'440100','AiSeeCN')
		"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本python",
				"脚本类型": "python",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python|script_type|2|data_type_id|1|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python|script_type|2|data_type_id|1|belong_id|440100|domain_id|AiSeeCN|original_user_id|pw|create_time|notnull|update_time|notnull|original_time|notnull|creater|pw|updater|pw
		"""
		log.info('>>>>> 添加脚本,脚本名称在本领域不存在,在其他领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_UpdateScript(self):
		u"""修改脚本"""
		pres = """
		${Database}.main|delete from tn_script_cfg where script_name='auto_脚本python' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "UpdateScript",
			"参数": {
				"脚本名称": "auto_脚本python",
				"修改内容": {
					"脚本名称": "auto_脚本python新",
					"数据类型": "私有"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|now|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		"""
		log.info('>>>>> 修改脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddScriptParams(self):
		u"""修改脚本,添加参数"""
		action = {
			"操作": "AddScriptParams",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本参数": [
					"param1",
					"param2"
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|1|param_name|param1|param_pattern|1|param_type|1|param_order|1
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|1|param_name|param2|param_pattern|1|param_type|1|param_order|2
		"""
		log.info('>>>>> 修改脚本,添加参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_UpdateScriptParams(self):
		u"""修改脚本,修改参数"""
		action = {
			"操作": "UpdateScriptParams",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本参数": [
					[
						1,
						"parama"
					],
					[
						2,
						"paramb"
					]
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|1|param_name|parama|param_pattern|1|param_type|1|param_order|1
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|1|param_name|paramb|param_pattern|1|param_type|1|param_order|2
		"""
		log.info('>>>>> 修改脚本,修改参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UploadScriptFile(self):
		u"""上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "test_time.py"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|test_time.py|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> 上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_UploadScriptFile(self):
		u"""python类型脚本,上传java脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "readfile1.java"
			}
		}
		checks = """
		CheckMsg|文件格式不正确，请选择py格式的文件
		"""
		log.info('>>>>> python类型脚本,上传java脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_UploadScriptFile(self):
		u"""python类型脚本,上传jar脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "CompareDataUtil.jar"
			}
		}
		checks = """
		CheckMsg|文件格式不正确，请选择py格式的文件
		"""
		log.info('>>>>> python类型脚本,上传jar脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_UploadScriptFile(self):
		u"""java类型脚本,上传python脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1",
				"脚本文件名": "fa.py"
			}
		}
		checks = """
		CheckMsg|文件格式不正确，请选择java或jar格式的文件
		"""
		log.info('>>>>> java类型脚本,上传python脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_UploadScriptFile(self):
		u"""java类型脚本,上传jar脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1",
				"脚本文件名": "CompareDataUtil.jar"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|CompareDataUtil.jar|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> java类型脚本,上传jar脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UploadScriptFile(self):
		u"""jar类型脚本,上传python脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"版本号": "1",
				"脚本文件名": "test_time.py"
			}
		}
		checks = """
		CheckMsg|文件格式不正确，请选择jar格式的文件
		"""
		log.info('>>>>> jar类型脚本,上传python脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UploadScriptFile(self):
		u"""jar类型脚本,上传java脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本jar",
				"版本号": "1",
				"脚本文件名": "readfile1.java"
			}
		}
		checks = """
		CheckMsg|文件格式不正确，请选择jar格式的文件
		"""
		log.info('>>>>> jar类型脚本,上传java脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_ScriptFileRClick(self):
		u"""设置主脚本"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "test_time.py",
				"右键": "设置为主脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|test_time.py|file_path|notnull|is_main|1|update_time|notnull|updater|${LoginUser}
		"""
		log.info('>>>>> 设置主脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_SaveScriptVersion(self):
		u"""保存当前版本"""
		action = {
			"操作": "SaveScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|test_time.py|file_path|notnull|is_main|1|update_time|notnull|updater|${LoginUser}
		"""
		log.info('>>>>> 保存当前版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_DownloadScriptVersion(self):
		u"""下载版本"""
		action = {
			"操作": "DownloadScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1"
			}
		}
		checks = """
		CheckDownloadFile|auto_脚本python新_1|zip
		"""
		log.info('>>>>> 下载版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_ScriptFileRClick(self):
		u"""下载脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "test_time.py",
				"右键": "下载脚本"
			}
		}
		checks = """
		CheckDownloadFile|test_time|py
		"""
		log.info('>>>>> 下载脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_SaveNewScriptVersion(self):
		u"""保存新版本"""
		action = {
			"操作": "SaveNewScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|2|version_status|01|version_desc|编辑版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|2|file_name|test_time.py|file_path|notnull|is_main|1|update_time|now|updater|${LoginUser}
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|2|param_name|parama|param_pattern|1|param_type|1|param_order|1
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|2|param_name|paramb|param_pattern|1|param_type|1|param_order|2
		"""
		log.info('>>>>> 保存新版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_UpdateScriptFileContent(self):
		u"""修改脚本内容"""
		action = {
			"操作": "UpdateScriptFileContent",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "test_time.py",
				"脚本内容": "print('hello world')"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 修改脚本内容 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_ScriptFileRClick(self):
		u"""删除脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "1",
				"脚本文件名": "test_time.py",
				"右键": "删除脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|1|file_name|test_time.py
		"""
		log.info('>>>>> 删除脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_DeleteScriptVersion(self):
		u"""删除版本"""
		action = {
			"操作": "DeleteScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python新",
				"版本号": "2"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python新|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|notnull|update_time|notnull|original_time|notnull|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|0|script_id|${ScriptID}|version_no|2
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|2
		CheckData|${Database}.main.tn_script_param_cfg|0|script_id|${ScriptID}|version_no|2
		CheckData|${Database}.main.tn_script_param_cfg|0|script_id|${ScriptID}|version_no|2
		"""
		log.info('>>>>> 删除版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_DeleteScriptVersion(self):
		u"""删除版本,当前只有1个版本"""
		action = {
			"操作": "DeleteScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|脚本至少保留一条版本信息，该条信息不可删除
		"""
		log.info('>>>>> 删除版本,当前只有1个版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_DeleteScript(self):
		u"""删除脚本python"""
		action = {
			"操作": "DeleteScript",
			"参数": {
				"脚本名称": "auto_脚本python新"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_script_cfg|0|script_name|auto_脚本python新
		"""
		log.info('>>>>> 删除脚本python <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_DeleteScript(self):
		u"""删除脚本java"""
		action = {
			"操作": "DeleteScript",
			"参数": {
				"脚本名称": "auto_脚本java"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_script_cfg|0|script_name|auto_脚本java
		"""
		log.info('>>>>> 删除脚本java <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_DeleteScript(self):
		u"""删除脚本jar"""
		action = {
			"操作": "DeleteScript",
			"参数": {
				"脚本名称": "auto_脚本jar"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_script_cfg|0|script_name|auto_脚本jar
		"""
		log.info('>>>>> 删除脚本jar <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_ScriptDataClear(self):
		u"""脚本管理,数据清理,清除python脚本"""
		action = {
			"操作": "ScriptDataClear",
			"参数": {
				"脚本名称": "auto_脚本python"
			}
		}
		log.info('>>>>> 脚本管理,数据清理,清除python脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_30_AddScript(self):
		u"""添加脚本,类型python"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本python",
				"脚本类型": "python",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本python|script_type|2|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型python <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_UploadScriptFile(self):
		u"""不带参python脚本上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "1",
				"脚本文件名": "test_no_param.py"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|test_no_param.py|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> 不带参python脚本上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_SubmitScriptApproval(self):
		u"""python脚本版本1提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> python脚本版本1提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_SaveNewScriptVersion(self):
		u"""python脚本保存新版本"""
		action = {
			"操作": "SaveNewScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|2|version_status|01|version_desc|编辑版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> python脚本保存新版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_ScriptFileRClick(self):
		u"""带参python脚本删除版本2的脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2",
				"脚本文件名": "test_no_param.py",
				"右键": "删除脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|2
		"""
		log.info('>>>>> 带参python脚本删除版本2的脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_UploadScriptFile(self):
		u"""带参python脚本上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2",
				"脚本文件名": "fa.py"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|2|file_name|fa.py|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> 带参python脚本上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_UploadScriptFile(self):
		u"""带参python脚本上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2",
				"脚本文件名": "fb.py"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|2|file_name|fb.py|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> 带参python脚本上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_ScriptFileRClick(self):
		u"""带参python脚本设置主脚本"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2",
				"脚本文件名": "fb.py",
				"右键": "设置为主脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|2|file_name|fb.py|file_path|notnull|is_main|1|update_time|notnull|updater|${LoginUser}
		"""
		log.info('>>>>> 带参python脚本设置主脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_AddScriptParams(self):
		u"""带参python脚本添加参数"""
		action = {
			"操作": "AddScriptParams",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2",
				"脚本参数": [
					"param1",
					"param2"
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|2|param_name|param1|param_pattern|1|param_type|1|param_order|1
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|2|param_name|param2|param_pattern|1|param_type|1|param_order|2
		"""
		log.info('>>>>> 带参python脚本添加参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_SubmitScriptApproval(self):
		u"""python脚本版本2提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "2"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> python脚本版本2提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_SaveNewScriptVersion(self):
		u"""python脚本保存新版本"""
		action = {
			"操作": "SaveNewScriptVersion",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|3|version_status|01|version_desc|编辑版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> python脚本保存新版本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_ScriptFileRClick(self):
		u"""带参python脚本删除版本3的脚本文件"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "3",
				"脚本文件名": "test_no_param.py",
				"右键": "删除脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|0|script_id|${ScriptID}|version_no|3
		"""
		log.info('>>>>> 带参python脚本删除版本3的脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_UploadScriptFile(self):
		u"""带参python脚本上传脚本文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "3",
				"脚本文件名": "readfile.py"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|3|file_name|readfile.py|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> 带参python脚本上传脚本文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_ScriptFileRClick(self):
		u"""带参python脚本设置主脚本"""
		action = {
			"操作": "ScriptFileRClick",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "3",
				"脚本文件名": "readfile.py",
				"右键": "设置为主脚本"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|3|file_name|readfile.py|file_path|notnull|is_main|1|update_time|notnull|updater|${LoginUser}
		"""
		log.info('>>>>> 带参python脚本设置主脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_AddScriptParams(self):
		u"""带参python脚本添加参数"""
		action = {
			"操作": "AddScriptParams",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "3",
				"脚本参数": [
					"param1",
					"param2",
					"param3"
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本python'|ScriptID
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|3|param_name|param1|param_pattern|1|param_type|1|param_order|1
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|3|param_name|param2|param_pattern|1|param_type|1|param_order|2
		CheckData|${Database}.main.tn_script_param_cfg|1|script_id|${ScriptID}|version_no|3|param_name|param3|param_pattern|1|param_type|1|param_order|3
		"""
		log.info('>>>>> 带参python脚本添加参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_SubmitScriptApproval(self):
		u"""python脚本版本3提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本python",
				"版本号": "3"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> python脚本版本3提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_ScriptDataClear(self):
		u"""脚本管理,数据清理,清除java脚本"""
		action = {
			"操作": "ScriptDataClear",
			"参数": {
				"脚本名称": "auto_脚本java"
			}
		}
		log.info('>>>>> 脚本管理,数据清理,清除java脚本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_47_AddScript(self):
		u"""添加脚本,类型java"""
		action = {
			"操作": "AddScript",
			"参数": {
				"脚本名称": "auto_脚本java",
				"脚本类型": "java",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_script_cfg|1|script_name|auto_脚本java|script_type|1|data_type_id|0|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|create_time|now|update_time|now|original_time|now|creater|${LoginUser}|updater|${LoginUser}|FetchID|script_id
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|1|version_status|01|version_desc|新建版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加脚本,类型java <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_UploadScriptFile(self):
		u"""java脚本上传脚本文件,读取personal目录下的文件"""
		action = {
			"操作": "UploadScriptFile",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1",
				"脚本文件名": "readfile1.java"
			}
		}
		checks = """
		CheckMsg|文件上传成功
		GetData|${Database}.main|select script_id from tn_script_cfg where script_name='auto_脚本java'|ScriptID
		CheckData|${Database}.main.tn_script_file|1|script_id|${ScriptID}|version_no|1|file_name|readfile1.java|file_path|notnull|is_main|0|update_time|now|updater|${LoginUser}
		"""
		log.info('>>>>> java脚本上传脚本文件,读取personal目录下的文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_SubmitScriptApproval(self):
		u"""java脚本版本1提交审批"""
		action = {
			"操作": "SubmitScriptApproval",
			"参数": {
				"脚本名称": "auto_脚本java",
				"版本号": "1"
			}
		}
		checks = """
		CheckMsg|提交成功
		"""
		log.info('>>>>> java脚本版本1提交审批 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_SaveNewScriptVersion(self):
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
		CheckData|${Database}.main.tn_script_version|1|script_id|${ScriptID}|version_no|2|version_status|01|version_desc|编辑版本|create_time|now|update_time|now|creater|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> java脚本保存新版本 <<<<<')
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
