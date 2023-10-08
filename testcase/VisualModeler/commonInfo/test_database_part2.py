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


class DatabasePart2(unittest.TestCase):

	log.info("装载数据库管理测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件为空"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "空文件.xlsx"
			}
		}
		checks = """
		CheckMsg|表字段文件不能为空
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件只有第一行表头"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "只含表头文件.xlsx"
			}
		}
		checks = """
		CheckMsg|表字段文件不能为空
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件只有第一行表头 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件字段名称缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表1",
				"表英文名": "auto_import_table1",
				"字段文件名": "字段名称缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表1|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表1|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表1' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|6|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件字段名称缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件字段英文名缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表2",
				"表英文名": "auto_import_table2",
				"字段文件名": "字段英文名缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表2|tab_en_name|auto_import_table2|tab_type|0|is_alive|1|remark|auto_导入表2|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表2' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|6|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件字段英文名缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件字段类型缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表3",
				"表英文名": "auto_import_table3",
				"字段文件名": "字段类型缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表3|tab_en_name|auto_import_table3|tab_type|0|is_alive|1|remark|auto_导入表3|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表3' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|6|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件字段类型缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件字符类型缺失长度"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表4",
				"表英文名": "auto_import_table4",
				"字段文件名": "字符类型缺失长度.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表4|tab_en_name|auto_import_table4|tab_type|0|is_alive|1|remark|auto_导入表4|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表1' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|6|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件字符类型缺失长度 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件数值类型缺失长度"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表5",
				"表英文名": "auto_import_table5",
				"字段文件名": "数值类型缺失长度.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表5|tab_en_name|auto_import_table5|tab_type|0|is_alive|1|remark|auto_导入表5|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表5' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件数值类型缺失长度 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件日期类型缺失字段格式"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表6",
				"表英文名": "auto_import_table6",
				"字段文件名": "日期类型缺失字段格式.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表6|tab_en_name|auto_import_table6|tab_type|0|is_alive|1|remark|auto_导入表6|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表6' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件日期类型缺失字段格式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件含重复字段"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表7",
				"表英文名": "auto_import_table7",
				"字段文件名": "含重复字段.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表7|tab_en_name|auto_import_table7|tab_type|0|is_alive|1|remark|auto_导入表7|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表7' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件含重复字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入文件正常文件"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "正常文件.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入文件正常文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表1"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表1' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表1"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表1|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表1|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表2"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表2' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表2"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表2|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表2|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表3"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表3' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表3"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表3|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表3|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表3 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表4"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表4' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表4"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表4|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表4|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表4 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表5"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表5' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表5"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表5|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表5|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表5 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表6"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表6' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表6"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表6|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表6|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表6 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_导入表7"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表7' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入表7"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表7|tab_en_name|auto_import_table1|tab_type|0|is_alive|1|remark|auto_导入表7|belong_id|${BelongID}|domain_id|${DomainID}
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_导入表7 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_DBTableClear(self):
		u"""数据管理，mysql数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入超大表",
				"模糊匹配": "否"
			}
		}
		log.info('>>>>> 数据管理，mysql数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_69_ImportDBTable(self):
		u"""数据管理，mysql数据库，导入表，导入超多字段"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_导入超大表",
				"表英文名": "auto_import_table_many",
				"字段文件名": "超多字段.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入超大表|tab_en_name|auto_import_table_many|tab_type|0|is_alive|1|remark|auto_导入超大表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入超大表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|100|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，导入表，导入超多字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_DeleteDBTable(self):
		u"""数据管理，mysql数据库，删除表：auto_测试表"""
		pres = """
		${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'||DBID
		${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'||TabID
		"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_tab_def_info|0|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|0|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，删除表：auto_测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_AddDBTable(self):
		u"""数据管理，mysql数据库，添加表"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，mysql数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_AddDBTableCol(self):
		u"""数据管理，mysql数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_mysql数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col_index",
						"列名(自定义)": "序号",
						"列类型": "字符",
						"长度": "10"
					},
					{
						"列名(数据库)": "user_name",
						"列名(自定义)": "姓名",
						"列类型": "字符",
						"长度": "100"
					},
					{
						"列名(数据库)": "comsume",
						"列名(自定义)": "消费金额",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"列名(数据库)": "balance",
						"列名(自定义)": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"列名(数据库)": "order_time",
						"列名(自定义)": "订单时间",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						]
					},
					{
						"列名(数据库)": "accept_date",
						"列名(自定义)": "收货日期",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd",
							""
						],
						"输出格式": [
							"yyyy-MM-dd",
							""
						]
					},
					{
						"列名(数据库)": "adddress",
						"列名(自定义)": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_mysql数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，mysql数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_DBTableClear(self):
		u"""数据管理，oracle数据库，数据表清理，清理测试表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"模糊匹配": "否"
			}
		}
		log.info('>>>>> 数据管理，oracle数据库，数据表清理，清理测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_74_DBTableClear(self):
		u"""数据管理，oracle数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据管理，oracle数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_75_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oracle数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(自定义)": "col_index",
						"列中文名": "序号",
						"列类型": "字符",
						"长度": "10"
					},
					{
						"列名(自定义)": "user_name",
						"列中文名": "姓名",
						"列类型": "字符",
						"长度": "100"
					},
					{
						"列名(自定义)": "comsume",
						"列中文名": "消费金额",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"列名(自定义)": "balance",
						"列中文名": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"列名(自定义)": "order_time",
						"列中文名": "订单时间",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						]
					},
					{
						"列名(自定义)": "accept_date",
						"列中文名": "收货日期",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd",
							""
						],
						"输出格式": [
							"yyyy-MM-dd",
							""
						]
					},
					{
						"列名(自定义)": "adddress",
						"列中文名": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oracle数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件正常文件"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "正常文件.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oracle数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件正常文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_DBTableClear(self):
		u"""数据管理，pg数据库，数据表清理，清理测试表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据表名称": "auto_测试表",
				"模糊匹配": "否"
			}
		}
		log.info('>>>>> 数据管理，pg数据库，数据表清理，清理测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_79_DBTableClear(self):
		u"""数据管理，pg数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据表名称": "auto_导入表",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据管理，pg数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_80_AddDBTable(self):
		u"""数据管理，pg数据库，添加表"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_postgres数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，pg数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_AddDBTableCol(self):
		u"""数据管理，pg数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(自定义)": "col_index",
						"列中文名": "序号",
						"列类型": "字符",
						"长度": "10"
					},
					{
						"列名(自定义)": "user_name",
						"列中文名": "姓名",
						"列类型": "字符",
						"长度": "100"
					},
					{
						"列名(自定义)": "comsume",
						"列中文名": "消费金额",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"列名(自定义)": "balance",
						"列中文名": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"列名(自定义)": "order_time",
						"列中文名": "订单时间",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						]
					},
					{
						"列名(自定义)": "accept_date",
						"列中文名": "收货日期",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd",
							""
						],
						"输出格式": [
							"yyyy-MM-dd",
							""
						]
					},
					{
						"列名(自定义)": "adddress",
						"列中文名": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_postgres数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，pg数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_ImportDBTable(self):
		u"""数据管理，pg数据库，导入表，导入文件正常文件"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_postgres数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "正常文件.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_postgres数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，pg数据库，导入表，导入文件正常文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_DBTableClear(self):
		u"""数据管理，oushu数据库，数据表清理，清理测试表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_oushu数据库",
				"数据表名称": "auto_测试表",
				"模糊匹配": "否"
			}
		}
		log.info('>>>>> 数据管理，oushu数据库，数据表清理，清理测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_84_DBTableClear(self):
		u"""数据管理，oushu数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_oushu数据库",
				"数据表名称": "auto_导入表",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据管理，oushu数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_85_AddDBTable(self):
		u"""数据管理，oushu数据库，添加表"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oushu数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oushu数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		"""
		log.info('>>>>> 数据管理，oushu数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_AddDBTableCol(self):
		u"""数据管理，oushu数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oushu数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(自定义)": "col_index",
						"列中文名": "序号",
						"列类型": "字符",
						"长度": "10"
					},
					{
						"列名(自定义)": "user_name",
						"列中文名": "姓名",
						"列类型": "字符",
						"长度": "100"
					},
					{
						"列名(自定义)": "comsume",
						"列中文名": "消费金额",
						"列类型": "数值",
						"小位数": "2"
					},
					{
						"列名(自定义)": "balance",
						"列中文名": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					},
					{
						"列名(自定义)": "order_time",
						"列中文名": "订单时间",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						],
						"输出格式": [
							"yyyy-MM-dd HH:mm:ss",
							""
						]
					},
					{
						"列名(自定义)": "accept_date",
						"列中文名": "收货日期",
						"列类型": "日期",
						"输入格式": [
							"yyyy-MM-dd",
							""
						],
						"输出格式": [
							"yyyy-MM-dd",
							""
						]
					},
					{
						"列名(自定义)": "adddress",
						"列中文名": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oushu数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_测试表|tab_en_name|auto_test_table|tab_type|0|is_alive|1|remark|auto_测试表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_测试表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|100|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|null|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|null|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|null
		"""
		log.info('>>>>> 数据管理，oushu数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_ImportDBTable(self):
		u"""数据管理，oushu数据库，导入表，导入文件正常文件"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oushu数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "正常文件.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		GetData|${Database}.main|select db_id from tn_db_cfg where db_name = 'auto_oushu数据库'|DBID
		CheckData|${Database}.main.tn_tab_def_info|1|db_id|${DBID}|channel_id|3|tab_chi_name|auto_导入表|tab_en_name|auto_import_table|tab_type|0|is_alive|1|remark|auto_导入表|belong_id|${BelongID}|domain_id|${DomainID}
		GetData|${Database}.main|select tab_id  from tn_tab_def_info where tab_chi_name = 'auto_导入表' and db_id = '${DBID}'|TabID
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|序号|column_en_name|col_index|column_id|col_index|column_type|STRING|remark|序号|col_length|10|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|1
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|姓名|column_en_name|user_name|column_id|user_name|column_type|STRING|remark|姓名|col_length|64|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|2
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|消费金额|column_en_name|comsume|column_id|comsume|column_type|NUMBER|remark|消费金额|col_length|10|col_float_num|2| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|3
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|账户余额|column_en_name|balance|column_id|balance|column_type|NUMBER|remark|账户余额|col_length|10|col_float_num|0| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|4
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|订单时间|column_en_name|order_time|column_id|order_time|column_type|DATE|remark|订单时间|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd HH:mm:ss|col_out_format|yyyy-MM-dd HH:mm:ss|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|5
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|收货日期|column_en_name|accept_date|column_id|accept_date|column_type|DATE|remark|收货日期|col_length|null|col_float_num|null| col_in_format|yyyy-MM-dd|col_out_format|yyyy-MM-dd|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|6
		CheckData|${Database}.main.tn_tab_col_def_info|1|tab_id|${TabID}|column_chi_name|详细地址|column_en_name|adddress|column_id|adddress|column_type|TEXT|remark|详细地址|col_length|null|col_float_num|null| col_in_format|null|col_out_format|null|belong_id|${BelongID}|domain_id|${DomainID}|create_time|now|indexs|7
		CheckData|${Database}.main.tn_tab_col_def_info|7|tab_id|${TabID}
		"""
		log.info('>>>>> 数据管理，oushu数据库，导入表，导入文件正常文件 <<<<<')
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
