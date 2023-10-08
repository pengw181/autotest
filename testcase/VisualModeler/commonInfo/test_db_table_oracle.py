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


class DatabaseManagementOracle(unittest.TestCase):

	log.info("装载数据库表管理oracle测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_DBTableClear(self):
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

	def test_2_DBTableClear(self):
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

	def test_3_AddDBTable(self):
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
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，数据表名称为空"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|数据表名称不允许为空
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，数据表名称为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，表英文名为空"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": ""
			}
		}
		checks = """
		CheckMsg|数据表英文名不允许为空
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，表英文名为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，数据表名称在列表已添加过"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|表中文名或英文名已存在
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，数据表名称在列表已添加过 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，表英文名在列表已添加过"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": "auto_test_table"
			}
		}
		checks = """
		CheckMsg|表中文名或英文名已存在
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，表英文名在列表已添加过 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，数据表名称输入字符校验"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表1%",
				"表英文名": "auto_test_table1"
			}
		}
		checks = """
		CheckMsg|数据表名称不能包含特殊字符
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，数据表名称输入字符校验 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddDBTable(self):
		u"""数据管理，oracle数据库，添加表，表英文名输入字符校验"""
		action = {
			"操作": "AddDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表1",
				"表英文名": "auto_test_table%"
			}
		}
		checks = """
		CheckMsg|表英文名称只能包含字母、数字、下划线，且不能以数字开头
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表，表英文名输入字符校验 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
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
						"列名(数据库)": "consume",
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
						"列名(数据库)": "address",
						"列名(自定义)": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，列名(数据库)包含特殊字符"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col%",
						"列名(自定义)": "序号2",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，列名(数据库)包含特殊字符 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，列名(数据库)包含中文"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col名称",
						"列名(自定义)": "序号3",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，列名(数据库)包含中文 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，列名(数据库)以数字开头"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "1col",
						"列名(自定义)": "序号4",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，列名(数据库)以数字开头 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，列名(数据库)包含空格在中间"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "col name",
						"列名(自定义)": "序号5",
						"列类型": "字符",
						"长度": "10"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名(数据库)只能包含字母、数字、下划线，且不能以数字开头
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，列名(数据库)包含空格在中间 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，修改列名(自定义)"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名",
				"修改内容": {
					"列信息": {
						"列名(自定义)": "姓名2"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，修改列名(自定义) <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，修改长度，由长变短"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"长度": "10"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，修改长度，由长变短 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，修改长度，由短变长"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"长度": "200"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，修改长度，由短变长 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，还原列名(自定义)"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "姓名2",
				"修改内容": {
					"列信息": {
						"列名(自定义)": "姓名"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，还原列名(自定义) <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，修改日期格式"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "收货日期",
				"修改内容": {
					"列信息": {
						"输入格式": [
							"yyyy/MM/dd",
							""
						],
						"输出格式": [
							"yyyy/MM/dd",
							""
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，修改日期格式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_EditDBTableCol(self):
		u"""数据管理，oracle数据库，数据表修改字段，修改日期格式，改成自定义"""
		action = {
			"操作": "EditDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "收货日期",
				"修改内容": {
					"列信息": {
						"输入格式": [
							"自定义",
							"yyyy-MM-dd"
						],
						"输出格式": [
							"自定义",
							"yyyy-MM-dd"
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表修改字段，修改日期格式，改成自定义 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，字段中文名已存在"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "username",
						"列名(自定义)": "姓名",
						"列类型": "字符",
						"长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名已存在
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，字段中文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段，字段英文名已存在"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "user_name",
						"列名(自定义)": "姓名b",
						"列类型": "字符",
						"长度": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|列名已存在
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段，字段英文名已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_DeleteDBTableCol(self):
		u"""数据管理，oracle数据库，数据表删除字段"""
		action = {
			"操作": "DeleteDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列名(自定义)": "账户余额"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表删除字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表已删除字段重新添加"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表",
				"列信息": [
					{
						"列名(数据库)": "balance",
						"列名(自定义)": "账户余额",
						"列类型": "数值",
						"小位数": "0"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表已删除字段重新添加 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件为空"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "空文件.xlsx"
			}
		}
		checks = """
		CheckMsg|表字段文件不能为空
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件为空 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件只有第一行表头"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表",
				"表英文名": "auto_import_table",
				"字段文件名": "只含表头文件.xlsx"
			}
		}
		checks = """
		CheckMsg|表字段文件不能为空
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件只有第一行表头 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件字段名称缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表1",
				"表英文名": "auto_import_table1",
				"字段文件名": "字段名称缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件字段名称缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件字段英文名缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表2",
				"表英文名": "auto_import_table2",
				"字段文件名": "字段英文名缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件字段英文名缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件字段类型缺失"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表3",
				"表英文名": "auto_import_table3",
				"字段文件名": "字段类型缺失.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件字段类型缺失 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件字符类型缺失长度"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表4",
				"表英文名": "auto_import_table4",
				"字段文件名": "字符类型缺失长度.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件字符类型缺失长度 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件数值类型缺失长度"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表5",
				"表英文名": "auto_import_table5",
				"字段文件名": "数值类型缺失长度.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件数值类型缺失长度 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件日期类型缺失字段格式"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表6",
				"表英文名": "auto_import_table6",
				"字段文件名": "日期类型缺失字段格式.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件日期类型缺失字段格式 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入文件含重复字段"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表7",
				"表英文名": "auto_import_table7",
				"字段文件名": "含重复字段.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件含重复字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_ImportDBTable(self):
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
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入文件正常文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表1"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表1"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表2"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表2"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表2 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表3"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表3"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表3 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表4"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表4"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表4 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表5"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表5"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表5 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表6"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表6"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表6 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_导入表7"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入表7"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_导入表7 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_DeleteDBTable(self):
		u"""数据管理，oracle数据库，删除表：auto_测试表"""
		action = {
			"操作": "DeleteDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_测试表"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，删除表：auto_测试表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_AddDBTable(self):
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
		"""
		log.info('>>>>> 数据管理，oracle数据库，添加表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_AddDBTableCol(self):
		u"""数据管理，oracle数据库，数据表添加字段"""
		action = {
			"操作": "AddDBTableCol",
			"参数": {
				"数据库名称": "auto_oracle数据库",
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
						"列名(数据库)": "consume",
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
						"列名(数据库)": "address",
						"列名(自定义)": "详细地址",
						"列类型": "文本"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，数据表添加字段 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_DBTableClear(self):
		u"""数据管理，oracle数据库，数据表清理，清理导入表"""
		action = {
			"操作": "DBTableClear",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入超大表",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 数据管理，oracle数据库，数据表清理，清理导入表 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_46_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入超多字段，100列"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入超大表100",
				"表英文名": "auto_import_table_many100",
				"字段文件名": "超多字段_100列.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入超多字段，100列 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_ImportDBTable(self):
		u"""数据管理，oracle数据库，导入表，导入超多字段，200列"""
		action = {
			"操作": "ImportDBTable",
			"参数": {
				"数据库名称": "auto_oracle数据库",
				"数据表名称": "auto_导入超大表200",
				"表英文名": "auto_import_table_many200",
				"字段文件名": "超多字段_200列.xlsx"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 数据管理，oracle数据库，导入表，导入超多字段，200列 <<<<<')
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
