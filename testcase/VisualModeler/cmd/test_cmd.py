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


class Command(unittest.TestCase):

	log.info("装载指令集测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_CmdSetDataClear(self):
		u"""指令集数据清理，删除历史数据"""
		pres = """
		${Database}.main|update tn_cmd_info set is_alive=0 where cmd_name like 'auto_%' and belong_id='${BelongID}' and domain_id='${DomainID}'
		${Database}.main|delete from tn_cmd_templ_cmd_rel where cmd_id in (select cmd_id from tn_cmd_info where cmd_name like 'auto_%' and belong_id='${BelongID}' and domain_id='${DomainID}')
		${Database}.main|delete from tn_node_nu_cmd_cfg where cmd_id in (select cmd_id from tn_cmd_info where cmd_name like 'auto_%' and belong_id='${BelongID}' and domain_id='${DomainID}')
		${Database}.main|update edata_custom_temp set cmd_id=null where table_name_ch like 'auto_%' and cmd_id is not null and belong_id='${BelongID}' and domain_id='${DomainID}'
		${Database}.main|update edata_cong_normal set cmd_id=null, analyzer_id=null where temp_id in (select temp_id from edata_custom_temp where table_name_ch like 'auto_%')  and belong_id='${BelongID}' and domain_id='${DomainID}'
		"""
		action = {
			"操作": "CmdSetDataClear",
			"参数": {
				"指令名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 指令集数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddCmdSet(self):
		u"""添加指令集，指令不带参数，ping指令，网元类型MME"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_ping",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping www.baidu.com -c 3"
				],
				"说明": "ping百度",
				"指令解析模版": [
					"auto_解析模板_解析ping"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 3|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping百度
		"""
		log.info('>>>>> 添加指令集，指令不带参数，ping指令，网元类型MME <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddCmdSet(self):
		u"""添加指令集，指令不带参数，ping指令，网元类型CSCE"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by array_positions(array['4G', 'CSCE'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,CSCE') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by find_in_set(level_name, '4G,CSCE')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,CSCE', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by instr('4G,CSCE', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_ping",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_CSCE"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping www.baidu.com -c 3"
				],
				"说明": "ping百度",
				"指令解析模版": [
					"auto_解析模板_解析ping"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='CSCE'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 3|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping百度
		"""
		log.info('>>>>> 添加指令集，指令不带参数，ping指令，网元类型CSCE <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddCmdSet(self):
		u"""添加指令集，指令不带参数，date指令"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_date",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"date"
				],
				"说明": "date获取时间",
				"指令解析模版": [
					"auto_解析模板_解析date"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_date|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|date|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|date获取时间
		"""
		log.info('>>>>> 添加指令集，指令不带参数，date指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddCmdSet(self):
		u"""添加指令集，指令单参数"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_单参数",
				"指令类别": "带参指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping <?> -c 5"
				],
				"说明": "ping指令带单参数",
				"指令解析模版": [
					"auto_解析模板_解析ping"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_单参数|cmd_type|0|cmd_use|1|cmd_category|2|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping <?> -c 5|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping指令带单参数
		"""
		log.info('>>>>> 添加指令集，指令单参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddCmdSet(self):
		u"""添加指令集，指令多参数"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_多参数",
				"指令类别": "带参指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping <?> -c <?>"
				],
				"说明": "ping指令带多参数",
				"指令解析模版": [
					"auto_解析模板_解析ping"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_多参数|cmd_type|0|cmd_use|1|cmd_category|2|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping <?> -c <?>|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping指令带多参数
		"""
		log.info('>>>>> 添加指令集，指令多参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddCmdSet(self):
		u"""添加指令集，组合指令"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_组合指令",
				"指令类别": "组合指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping www.baidu.com -c 5",
					"date"
				],
				"说明": "ping百度",
				"指令解析模版": [
					"auto_解析模板_解析date"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_组合指令|cmd_type|0|cmd_use|1|cmd_category|3|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 5~date|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping百度
		"""
		log.info('>>>>> 添加指令集，组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateCmdSetStatus(self):
		u"""启用指令集"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 3|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|1|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex|
		"""
		log.info('>>>>> 启用指令集 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_DeleteCmdSet(self):
		u"""指令已启用，无法删除"""
		action = {
			"操作": "DeleteCmdSet",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				}
			}
		}
		checks = """
		CheckMsg|所选指令集信息已启用，不能够进行删除操作
		"""
		log.info('>>>>> 指令已启用，无法删除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateCmdSetStatus(self):
		u"""禁用指令集"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "禁用"
			}
		}
		checks = """
		CheckMsg|禁用成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 3|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex|
		"""
		log.info('>>>>> 禁用指令集 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteCmdSet(self):
		u"""指令已禁用，允许删除"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "DeleteCmdSet",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				}
			}
		}
		checks = """
		CheckMsg|删除成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|0|cmd_name|auto_指令_ping|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}
		"""
		log.info('>>>>> 指令已禁用，允许删除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddCmdSet(self):
		u"""添加指令集，指令不带参数，ping指令，网元类型MME"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_ping",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping www.baidu.com -c 5"
				],
				"说明": "ping百度",
				"指令解析模版": [
					"auto_解析模板_解析ping",
					"auto_解析模板_列更新",
					"auto_解析模板_分段",
					"auto_二维表结果判断，添加变量配置"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 5|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex|
		"""
		log.info('>>>>> 添加指令集，指令不带参数，ping指令，网元类型MME <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddCmdSet(self):
		u"""添加指令集，echo指令"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_echo",
				"指令类别": "带参指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"echo 'hello, <?>'"
				],
				"说明": "echo信息",
				"指令解析模版": [],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_echo|cmd_type|0|cmd_use|1|cmd_category|2|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|echo 'hello, <?>'|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|echo信息
		"""
		log.info('>>>>> 添加指令集，echo指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddCmdSet(self):
		u"""添加指令集，ping指令，日志清洗"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_ping_日志清洗",
				"指令类别": "ping指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"ping www.baidu.com -c 5"
				],
				"说明": "ping百度",
				"指令解析模版": [
					"auto_解析模板_日志清洗"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping_日志清洗|cmd_type|0|cmd_use|1|cmd_category|4|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 5|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|0|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex||remark|ping百度
		"""
		log.info('>>>>> 添加指令集，ping指令，日志清洗 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_ping，网元类型MME"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by array_positions(array['4G', 'MME'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,MME') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by find_in_set(level_name, '4G,MME')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,MME', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'MME') order by instr('4G,MME', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='MME'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 5|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|1|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex|
		"""
		log.info('>>>>> 启用指令集：auto_指令_ping，网元类型MME <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_ping，网元类型CSCE"""
		pres = """
		${Database}.sso|select concat('#-1#', string_agg(t.level_id, '#')) as level_path from (select * from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by array_positions(array['4G', 'CSCE'],level_name ::text)) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', group_concat(t.level_id order by t.rk separator '#')) as level_path from (select level_name, level_id, find_in_set(level_name, '4G,CSCE') rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by find_in_set(level_name, '4G,CSCE')) t|LevelPath|continue
		${Database}.sso|select concat('#-1#', listagg(t.level_id, '#') within group(order by t.rk)) level_path from (select level_name, level_id, instr('4G,CSCE', level_name) as rk from nu.tn_level_info where level_id in (select level_id from nu.tn_level_rd_rela where belong_id='${BelongID}' and domain_id='${DomainID}') and level_name in ('4G', 'CSCE') order by instr('4G,CSCE', level_name)) t|LevelPath|continue
		"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping",
					"网元分类": [
						"4G,4G_CSCE"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		GetData|${Database}.nu|select VENDOR_ID from nu.vendor_info where VENDOR_CNAME='华为'|VendorID
		GetData|${Database}.nu|select t.NETUNIT_MODEL_ID from nu.TN_NETWK_VENDOR_MD_INFO t where t.VENDOR_ID=${VendorID} and t.NETUNIT_MODEL_NAME='ME60'|NetunitModelID
		GetData|${Database}.nu|select level_id from nu.tn_level_info where level_name='CSCE'|LevelID
		GetData|${Database}.nu|select login_type_id from nu.TN_NETUNIT_LOGIN_CFG where level_id=${LevelID} and login_type_name='普通模式' and belong_id='${BelongID}' and domain_id='${DomainID}'|LoginTypeID
		CheckData|${Database}.main.tn_cmd_info|1|cmd_name|auto_指令_ping|cmd_type|0|cmd_use|1|cmd_category|1|level_id|${LevelID}|level_path|${LevelPath}|vendor_id|${VendorID}|netunit_model_id|${NetunitModelID}|command|ping www.baidu.com -c 3|time_out|20|read_until||belong_id|${BelongID}|domain_id|${DomainID}|login_type_id|${LoginTypeID}|is_alive|1|is_high_risk|0|is_public_cmd|1|sensitive_cmd|0|sensitive_regex|
		"""
		log.info('>>>>> 启用指令集：auto_指令_ping，网元类型CSCE <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_date"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_date",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_date <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_单参数"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_单参数",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_单参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_多参数"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_多参数",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_多参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_组合指令"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_组合指令",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_组合指令 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_echo"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_echo",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_echo <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_CmdSetOutput(self):
		u"""指令集设置输出参数：auto_指令_单参数"""
		action = {
			"操作": "CmdSetOutput",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_单参数",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"正则参数": [
					{
						"参数名称": "result_ping",
						"参数说明": "ping解析",
						"私有参数": "否",
						"正则魔方": {
							"设置方式": "选择",
							"正则模版名称": "auto_正则模版_获取丢包率"
						},
						"取值": "取匹配到第一个值"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 指令集设置输出参数：auto_指令_单参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_CmdSetInput(self):
		u"""指令集设置输入参数：auto_指令_echo"""
		action = {
			"操作": "CmdSetInput",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_echo",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"参数信息": [
					{
						"输出参数": "result_ping"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 指令集设置输入参数：auto_指令_echo <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_CmdSetInput(self):
		u"""指令集设置输入参数：auto_指令_单参数"""
		action = {
			"操作": "CmdSetInput",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_单参数",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"参数信息": [
					{
						"变量配置": [
							{
								"变量模式": "业务变量",
								"变量名称": "ssip"
							}
						],
						"变量参数": "ssip"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 指令集设置输入参数：auto_指令_单参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_CmdSetWash(self):
		u"""指令集设置日志清洗：auto_指令_ping_日志清洗"""
		action = {
			"操作": "CmdSetWash",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping_日志清洗",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"日志清洗方向": "正向",
				"按关键字清洗": {
					"是否启用": "是",
					"关键字列表": [
						{
							"关键字": {
								"设置方式": "选择",
								"正则模版名称": "auto_正则模版_清洗ping指令"
							}
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 指令集设置日志清洗：auto_指令_ping_日志清洗 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddCmdSet(self):
		u"""添加指令集，auto_指令_磁盘利用率检查"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_磁盘利用率检查",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"df -hl"
				],
				"说明": "磁盘利用率检查",
				"指令解析模版": [
					"auto_解析模板_服务器磁盘利用率检查"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，auto_指令_磁盘利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_AddCmdSet(self):
		u"""添加指令集，auto_指令_查看Slab"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_查看Slab",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"cat /proc/meminfo | grep ^Slab"
				],
				"说明": "查看Slab",
				"指令解析模版": [
					"auto_解析模板_查看Slab解析"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，auto_指令_查看Slab <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_AddCmdSet(self):
		u"""添加指令集，auto_指令_内存利用率检查"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_内存利用率检查",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"free -m | grep Mem"
				],
				"说明": "内存利用率检查",
				"指令解析模版": [
					"auto_解析模板_内存利用率解析"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，auto_指令_内存利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_AddCmdSet(self):
		u"""添加指令集，auto_指令_服务器性能检测Top"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_服务器性能检测Top",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"top -bn 1"
				],
				"说明": "top指令监测设备性能负荷",
				"指令解析模版": [
					"auto_解析模板_cpu利用率检查"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，auto_指令_服务器性能检测Top <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_AddCmdSet(self):
		u"""添加指令集，auto_指令_服务器负载检查"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_服务器负载检查",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_MME"
				],
				"厂家": "华为",
				"设备型号": [
					"ME60"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"cat /proc/loadavg"
				],
				"说明": [
					"前三个值分别代表系统5分钟、10分钟、15分钟前的平均负载",
					"第四个值的分子是正在运行的进程数，分母为总进程数",
					"第五个值是最近运行的进程id"
				],
				"指令解析模版": [
					"auto_解析模板_服务器负载检查"
				],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，auto_指令_服务器负载检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_磁盘利用率检查"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_磁盘利用率检查",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_磁盘利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_查看Slab"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_查看Slab",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_查看Slab <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_内存利用率检查"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_内存利用率检查",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_内存利用率检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_服务器性能检测Top"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_服务器性能检测Top",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_服务器性能检测Top <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_服务器负载检查"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_服务器负载检查",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_服务器负载检查 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_UpdateCmdSetStatus(self):
		u"""启用指令集：auto_指令_ping_日志清洗"""
		action = {
			"操作": "UpdateCmdSetStatus",
			"参数": {
				"查询条件": {
					"指令名称": "auto_指令_ping_日志清洗",
					"网元分类": [
						"4G,4G_MME"
					],
					"厂家": "华为",
					"设备型号": "ME60"
				},
				"状态": "启用"
			}
		}
		checks = """
		CheckMsg|启用成功
		"""
		log.info('>>>>> 启用指令集：auto_指令_ping_日志清洗 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_AddCmdSet(self):
		u"""添加指令集，指令包含已启用的黑名单指令：auto_bl_testall"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_黑名单testall",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_AUTO"
				],
				"厂家": "图科",
				"设备型号": [
					"TKea",
					"TKing"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"echo 'auto_bl_testall'"
				],
				"说明": "包含已启用的黑名单指令",
				"指令解析模版": [],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，指令包含已启用的黑名单指令：auto_bl_testall <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_AddCmdSet(self):
		u"""添加指令集，指令内容包含已启用的黑名单指令：auto_bl_testone"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_黑名单testone",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_AUTO"
				],
				"厂家": "图科",
				"设备型号": [
					"TKea",
					"TKing"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"echo 'auto_bl_testone'"
				],
				"说明": "包含已启用的黑名单指令",
				"指令解析模版": [],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，指令内容包含已启用的黑名单指令：auto_bl_testone <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_AddCmdSet(self):
		u"""添加指令集，指令内容包含未启用的黑名单指令echo"""
		action = {
			"操作": "AddCmdSet",
			"参数": {
				"指令名称": "auto_指令_黑名单echo",
				"指令类别": "不带参数指令",
				"指令用途": "巡检类",
				"网元分类": [
					"4G,4G_AUTO"
				],
				"厂家": "图科",
				"设备型号": [
					"TKea",
					"TKing"
				],
				"登录模式": "普通模式",
				"公有指令": "是",
				"隐藏输入指令": "否",
				"个性指令": "否",
				"指令等待超时": "20",
				"指令": [
					"echo 'auto_bl_echo'"
				],
				"说明": "包含未启用的黑名单指令",
				"指令解析模版": [],
				"指令翻页符": "",
				"期待返回的结束符": "",
				"隐藏指令返回": ""
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加指令集，指令内容包含未启用的黑名单指令echo <<<<<')
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
