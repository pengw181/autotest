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


class TemplatePart1(unittest.TestCase):

	log.info("装载网元模版配置测试用例（1）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ZgTempDataClear(self):
		u"""网元模版配置，数据清理"""
		action = {
			"操作": "ZgTempDataClear",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		log.info('>>>>> 网元模版配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddZgTemp(self):
		u"""网元基础信息，添加模版：auto_网元基础信息表"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元基础信息表|zg_temp_type|1|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|1|is_null|0|is_search|1|is_confirm|1|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元类型|col_ename|LEVEL_ID|col_length|10|is_primary|0|is_null|0|is_search|1|is_confirm|1|col_order|2|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元IP|col_ename|NETUNIT_IP|col_length|50|is_primary|0|is_null|0|is_search|1|is_confirm|1|col_order|3|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|生产厂家|col_ename|VENDOR_ID|col_length|10|is_primary|0|is_null|0|is_search|1|is_confirm|1|col_order|4|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|设备型号|col_ename|NETUNIT_MODEL_ID|col_length|10|is_primary|0|is_null|0|is_search|1|is_confirm|1|col_order|5|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|业务状态|col_ename|STATE_ID|col_length|2|is_primary|0|is_null|0|is_search|1|is_confirm|1|col_order|6|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元基础信息，添加模版：auto_网元基础信息表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_ZgTempDataClear(self):
		u"""网元模版配置，数据清理"""
		action = {
			"操作": "ZgTempDataClear",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料"
			}
		}
		log.info('>>>>> 网元模版配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_4_AddZgTemp(self):
		u"""网元辅助资料，添加模版：auto_网元辅助资料"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元辅助资料|zg_temp_type|2|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元辅助资料，添加模版：auto_网元辅助资料 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_SaveZgTempCol(self):
		u"""网元辅助资料：auto_网元辅助资料，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元辅助资料",
				"模版名称": "auto_网元辅助资料",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "列1",
						"业务变量": "ssip",
						"数据类型": "字符",
						"长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元辅助资料' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		GetData|${Database}.main|select zg_table_name from zg_temp_cfg where zg_temp_name='auto_网元辅助资料' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTableName
		GetData|${Database}.main|select var_id from RULERX_VAR_SERV_COL_REL where zg_table_name='${ZgTableName}' and col_id='COL_2'|VarID
		CheckData|${Database}.main.RULERX_VAR_CFG|1|var_id|${VarID}|var_name|ssip|var_desc|null|var_type|businessVar|var_mode|common_var|var_expr|auto_网元辅助资料:列1|var_json|null|is_common|1|user_id|${LoginUser}|create_time|now|update_time|now|domain_id|${DomainID}|belong_id|${BelongID}|is_down|0|hash_key|null
		"""
		log.info('>>>>> 网元辅助资料：auto_网元辅助资料，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_ZgTempDataClear(self):
		u"""网元模版配置，数据清理"""
		action = {
			"操作": "ZgTempDataClear",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 网元模版配置，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_7_AddZgTemp(self):
		u"""网元其它资料，添加模版：auto_网元其它资料"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元其它资料|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料，添加模版：auto_网元其它资料 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "列1",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列2",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列3",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列4",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列5",
						"数据类型": "字符",
						"长度": "200"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列3|col_ename|COL_4|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|4|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列4|col_ename|COL_5|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|5|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列5|col_ename|COL_6|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|6|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料，删除网元名称列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"列配置": [
					{
						"操作类型": "删除",
						"配置项": "网元名称"
					}
				]
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列3|col_ename|COL_4|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列4|col_ename|COL_5|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|4|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列5|col_ename|COL_6|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|5|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料，删除网元名称列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddZgTemp(self):
		u"""网元其它资料，添加模版：auto_测试告警表"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试告警表"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_测试告警表|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料，添加模版：auto_测试告警表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_SaveZgTempCol(self):
		u"""网元其它资料：auto_测试告警表，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试告警表",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "列1",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列2",
						"数据类型": "字符",
						"长度": "200"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_测试告警表' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_测试告警表，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_SaveZgTempCol(self):
		u"""网元其它资料：auto_测试告警表，删除网元名称列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试告警表",
				"列配置": [
					{
						"操作类型": "删除",
						"配置项": "网元名称"
					}
				]
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_测试告警表' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_测试告警表，删除网元名称列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddZgTemp(self):
		u"""网元其它资料，添加模版：auto_测试输出表"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试输出表"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_测试输出表|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料，添加模版：auto_测试输出表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_SaveZgTempCol(self):
		u"""网元其它资料：auto_测试输出表，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试输出表",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "列1",
						"数据类型": "字符",
						"长度": "200"
					},
					{
						"操作类型": "添加",
						"列名": "列2",
						"数据类型": "字符",
						"长度": "200"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_测试输出表' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_测试输出表，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_SaveZgTempCol(self):
		u"""网元其它资料：auto_测试输出表，删除网元名称列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_测试输出表",
				"列配置": [
					{
						"操作类型": "删除",
						"配置项": "网元名称"
					}
				]
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_测试输出表' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列2|col_ename|COL_3|col_length|200|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_测试输出表，删除网元名称列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddZgTemp(self):
		u"""网元其它资料，添加模版：auto_网元其它资料_多类型"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_多类型"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元其它资料_多类型|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料，添加模版：auto_网元其它资料_多类型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料_多类型，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_多类型",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "列1",
						"数据类型": "字符",
						"长度": "100"
					},
					{
						"操作类型": "添加",
						"列名": "列2",
						"数据类型": "数值",
						"小位数": "2"
					},
					{
						"操作类型": "添加",
						"列名": "列3",
						"数据类型": "日期",
						"输入格式": [
							"yyyyMMddHHmmss",
							""
						],
						"输出格式": [
							"yyyyMMddHHmmss",
							""
						]
					},
					{
						"操作类型": "添加",
						"列名": "列4",
						"数据类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_多类型' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|列2|col_ename|COL_3|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|2
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|列3|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|4|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|DATE|col_in_format|yyyyMMddHHmmss|col_out_format|yyyyMMddHHmmss|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列4|col_ename|COL_5|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|5|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|TEXT|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_多类型，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料_多类型，删除网元名称列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_多类型",
				"列配置": [
					{
						"操作类型": "删除",
						"配置项": "网元名称"
					}
				]
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_多类型' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列1|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|列2|col_ename|COL_3|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|2
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|列3|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|DATE|col_in_format|yyyyMMddHHmmss|col_out_format|yyyyMMddHHmmss|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|列4|col_ename|COL_5|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|4|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|TEXT|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_多类型，删除网元名称列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddZgTemp(self):
		u"""网元其它资料，添加模版：auto_网元其它资料_vm仪表盘"""
		action = {
			"操作": "AddZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元其它资料_vm仪表盘|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		"""
		log.info('>>>>> 网元其它资料，添加模版：auto_网元其它资料_vm仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，添加列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"列配置": [
					{
						"操作类型": "添加",
						"列名": "姓名",
						"数据类型": "字符",
						"长度": "100"
					},
					{
						"操作类型": "添加",
						"列名": "等级",
						"数据类型": "字符",
						"长度": "100"
					},
					{
						"操作类型": "添加",
						"列名": "分数",
						"数据类型": "数值",
						"小位数": "0"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME|col_length|512|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|4|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，添加列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_SaveZgTempCol(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，删除网元名称列"""
		action = {
			"操作": "SaveZgTempCol",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"列配置": [
					{
						"操作类型": "删除",
						"配置项": "网元名称"
					}
				]
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|网元名称|col_ename|NETUNIT_NAME
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|0|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，删除网元名称列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_UpdateColSearch(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置搜索条件"""
		action = {
			"操作": "UpdateColSearch",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"列名列表": [
					"姓名",
					"等级",
					"分数"
				]
			}
		}
		checks = """
		CheckMsg|
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|1|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|2|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|3|is_frozen|0|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，设置搜索条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_UpdateColFrozen(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置是否冻结"""
		action = {
			"操作": "UpdateColFrozen",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"列名列表": [
					"姓名",
					"等级",
					"分数"
				]
			}
		}
		checks = """
		CheckMsg|
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|2|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|1|is_search|1|is_confirm|0|col_order|3|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，设置是否冻结 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_UpdateColNull(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置允许为空"""
		action = {
			"操作": "UpdateColNull",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"列名列表": [
					"姓名",
					"等级",
					"分数"
				]
			}
		}
		checks = """
		CheckMsg|
		GetData|${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and belong_id='${BelongID}' and domain_id='${DomainID}'|ZgTempID
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|2|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|3|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，设置允许为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_CopyZgTemp(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，复制模版"""
		action = {
			"操作": "CopyZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘",
				"新模版名称": "auto_网元其它资料_vm仪表盘2"
			}
		}
		checks = """
		CheckMsg|复制成功
		CheckData|${Database}.main.zg_temp_cfg|1|zg_temp_name|auto_网元其它资料_vm仪表盘2|zg_temp_type|3|zg_table_name|notnull|belong_id|${BelongID}|domain_id|${DomainID}|original_user_id|${LoginUser}|original_time|now|create_user_id|${LoginUser}|create_time|now|updater_user_id|${LoginUser}|update_time|now|is_alarm|0|is_dashboard_ds|0|FetchID|zg_temp_id
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|姓名|col_ename|COL_2|col_length|100|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|1|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id||col_cname|等级|col_ename|COL_3|col_length|100|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|2|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|STRING|col_in_format|null|col_out_format|null|col_float_num|null
		CheckData|${Database}.main.zg_col_def|1|zg_temp_id|${ZgTempID}|regx_templ_id|null|col_cname|分数|col_ename|COL_4|col_length|null|is_primary|0|is_null|0|is_search|1|is_confirm|0|col_order|3|is_frozen|1|belong_id|${BelongID}|domain_id|${DomainID}|col_cls|NUMBER|col_in_format|null|col_out_format|null|col_float_num|0
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，复制模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_DeleteZgTemp(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘2，删除模版"""
		pres = """
		${Database}.main|select zg_temp_id from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘2' and zg_temp_type='3'|ZgTempID|
		"""
		action = {
			"操作": "DeleteZgTemp",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘2"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.zg_temp_cfg|0|zg_temp_name|auto_网元其它资料_vm仪表盘2|zg_temp_type|3
		CheckData|${Database}.main.zg_col_def|0|zg_temp_id|${ZgTempID}
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘2，删除模版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_ZgTempPushAlarm(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台"""
		action = {
			"操作": "ZgTempPushAlarm",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|推送成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_ZgTempSyncAlarm(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，同步告警平台"""
		action = {
			"操作": "ZgTempSyncAlarm",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|同步成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，同步告警平台 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_ZgTempRevokeAlarm(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送告警平台"""
		action = {
			"操作": "ZgTempRevokeAlarm",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|撤销成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送告警平台 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_ZgTempPushAlarm(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台"""
		action = {
			"操作": "ZgTempPushAlarm",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|推送成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_ZgTempPushDashboard(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘"""
		pres = """
		${Database}.dashboard|delete from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='2'
		"""
		action = {
			"操作": "ZgTempPushDashboard",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|推送成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_ZgTempSyncDashboard(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，同步仪表盘"""
		action = {
			"操作": "ZgTempSyncDashboard",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|同步成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，同步仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_ZgTempRevokeDashboard(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送仪表盘"""
		action = {
			"操作": "ZgTempRevokeDashboard",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|撤销成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_ZgTempPushDashboard(self):
		u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘"""
		action = {
			"操作": "ZgTempPushDashboard",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料_vm仪表盘"
			}
		}
		checks = """
		CheckMsg|推送成功
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_UpdateColSearch(self):
		u"""网元其它资料：auto_网元其它资料，设置搜索条件"""
		action = {
			"操作": "UpdateColSearch",
			"参数": {
				"模版类型": "网元其它资料",
				"模版名称": "auto_网元其它资料",
				"列名列表": [
					"列1",
					"列2",
					"列3",
					"列4",
					"列5"
				]
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> 网元其它资料：auto_网元其它资料，设置搜索条件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_ZgAddData(self):
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

	def test_37_ZgAddData(self):
		u"""网元基础信息，数据管理，添加数据，网元已添加，未二次确认"""
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
		log.info('>>>>> 网元基础信息，数据管理，添加数据，网元已添加，未二次确认 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，二次确认，确认通过"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO1}"
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

	def test_39_ZgAddData(self):
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

	def test_40_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，二次确认，确认通过"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO2}"
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

	def test_41_ZgAddData(self):
		u"""网元基础信息，数据管理，添加数据，网元已存在"""
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
		log.info('>>>>> 网元基础信息，数据管理，添加数据，网元已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_ZgUpdateData(self):
		u"""网元基础信息，数据管理，修改数据，网元已存在"""
		action = {
			"操作": "ZgUpdateData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元名称": "${NetunitAUTO1}",
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
						"192.168.88.116"
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
						"无业务"
					]
				]
			}
		}
		checks = """
		CheckMsg|网元名称已存在
		"""
		log.info('>>>>> 网元基础信息，数据管理，修改数据，网元已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_ZgUpdateData(self):
		u"""网元基础信息，数据管理，修改数据"""
		action = {
			"操作": "ZgUpdateData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元名称": "${NetunitAUTO1}",
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
						"192.168.88.116"
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
						"无业务"
					]
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，修改数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，修改数据，二次确认"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO1}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，修改数据，二次确认 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_ZgDeleteData(self):
		u"""网元基础信息，数据管理，删除数据"""
		action = {
			"操作": "ZgDeleteData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元名称": "${NetunitAUTO1}"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，删除数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_46_ZgDataRevokeSelected(self):
		u"""网元基础信息，数据管理，删除数据，取消确认"""
		action = {
			"操作": "ZgDataRevokeSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元名称": "${NetunitAUTO1}"
				},
				"网元列表": [
					"${NetunitAUTO1}"
				]
			}
		}
		checks = """
		CheckMsg|撤销成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，删除数据，取消确认 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_ZgDeleteData(self):
		u"""网元基础信息，数据管理，删除数据"""
		action = {
			"操作": "ZgDeleteData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元名称": "${NetunitAUTO1}"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，删除数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_48_ZgDataConfirmSelected(self):
		u"""网元基础信息，数据管理，删除数据，二次确认，确认所选"""
		action = {
			"操作": "ZgDataConfirmSelected",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"网元列表": [
					"${NetunitAUTO1}"
				]
			}
		}
		checks = """
		CheckMsg|确认成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，删除数据，二次确认，确认所选 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_49_ZgDeleteData(self):
		u"""网元基础信息，数据管理，删除数据"""
		action = {
			"操作": "ZgDeleteData",
			"参数": {
				"模版类型": "网元基础信息",
				"模版名称": "auto_网元基础信息表",
				"查询条件": {
					"网元名称": "${NetunitAUTO2}"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 网元基础信息，数据管理，删除数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_50_ZgDataConfirmAll(self):
		u"""网元基础信息，数据管理，删除数据，二次确认，确认全部"""
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
		log.info('>>>>> 网元基础信息，数据管理，删除数据，二次确认，确认全部 <<<<<')
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
