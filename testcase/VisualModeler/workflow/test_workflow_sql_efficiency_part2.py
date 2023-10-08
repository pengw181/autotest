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


class WorkFlowSqlNodeEfficiencyPart2(unittest.TestCase):

	log.info("装载流程数据库节点大数据效率测试用例（2）")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_51_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_52_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，pg数据库，批量提交行数不为空，2w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库2w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_异常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，pg数据库，批量提交行数不为空，2w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_53_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_54_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，2w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库2w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_异常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，2w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_55_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_56_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，2w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库2w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据2w_异常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，2w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_57_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_58_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，pg数据库，批量提交行数不为空，5w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库5w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_异常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，pg数据库，批量提交行数不为空，5w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_59_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_60_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，5w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库5w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_异常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，5w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_61_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_62_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，5w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库5w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据5w_异常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，5w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_63_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_64_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，pg数据库，批量提交行数不为空，10w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部pg数据库10w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_异常",
						"数据库": "auto_postgres数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，pg数据库，批量提交行数不为空，10w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_65_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_66_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，10w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部oracle数据库10w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_异常",
						"数据库": "auto_oracle数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，oracle数据库，批量提交行数不为空，10w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_67_AddNode(self):
		u"""画流程图，添加一个数据库节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个数据库节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_68_NodeBusinessConf(self):
		u"""配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，10w部分异常"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"节点类型": "数据库节点",
				"节点名称": "数据库节点",
				"业务配置": {
					"节点名称": "导入外部mysql数据库10w部分成功",
					"操作模式": "配置模式",
					"sql配置": {
						"变量": "大数据10w_异常",
						"数据库": "auto_mysql数据库",
						"存储模式": "",
						"高级配置": {
							"状态": "开启",
							"跳过行数": "",
							"批量提交行数": "1000"
						},
						"表选择": "auto_测试表",
						"字段映射": {
							"序号": {
								"值类型": "索引",
								"字段值": "1"
							},
							"姓名": {
								"值类型": "索引",
								"字段值": "2"
							},
							"消费金额": {
								"值类型": "索引",
								"字段值": "3"
							},
							"账户余额": {
								"值类型": "索引",
								"字段值": "4"
							},
							"订单时间": {
								"值类型": "索引",
								"字段值": "5"
							},
							"收货日期": {
								"值类型": "索引",
								"字段值": "6"
							},
							"详细地址": {
								"值类型": "索引",
								"字段值": "7"
							}
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置数据库节点，配置模式，mysql数据库，批量提交行数不为空，10w部分异常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_69_LineNode(self):
		u"""开始节点连线到节点：加载大数据入库数据1w"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "开始",
				"终止节点名称": "加载大数据入库数据1w",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点：加载大数据入库数据1w <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_70_LineNode(self):
		u"""节点加载大数据入库数据1w连线到节点：加载大数据入库数据2w"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "加载大数据入库数据1w",
				"终止节点名称": "加载大数据入库数据2w",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载大数据入库数据1w连线到节点：加载大数据入库数据2w <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_71_LineNode(self):
		u"""节点加载大数据入库数据2w连线到节点：加载大数据入库数据5w"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "加载大数据入库数据2w",
				"终止节点名称": "加载大数据入库数据5w",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载大数据入库数据2w连线到节点：加载大数据入库数据5w <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_72_LineNode(self):
		u"""节点加载大数据入库数据5w连线到节点：加载大数据入库数据10w"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "加载大数据入库数据5w",
				"终止节点名称": "加载大数据入库数据10w",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载大数据入库数据5w连线到节点：加载大数据入库数据10w <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_73_LineNode(self):
		u"""节点加载大数据入库数据10w连线到节点：postgres外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "加载大数据入库数据10w",
				"终止节点名称": "postgres外部表数据清理",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点加载大数据入库数据10w连线到节点：postgres外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_74_LineNode(self):
		u"""节点postgres外部表数据清理连线到节点：oracle外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "postgres外部表数据清理",
				"终止节点名称": "oracle外部表数据清理",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点postgres外部表数据清理连线到节点：oracle外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_75_LineNode(self):
		u"""节点oracle外部表数据清理连线到节点：mysql外部表数据清理"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "oracle外部表数据清理",
				"终止节点名称": "mysql外部表数据清理",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点oracle外部表数据清理连线到节点：mysql外部表数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_76_LineNode(self):
		u"""节点mysql外部表数据清理连线到节点：导入外部pg数据库1w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "mysql外部表数据清理",
				"终止节点名称": "导入外部pg数据库1w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点mysql外部表数据清理连线到节点：导入外部pg数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_77_LineNode(self):
		u"""节点导入外部pg数据库1w正常连线到节点：导入外部oracle数据库1w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库1w正常",
				"终止节点名称": "导入外部oracle数据库1w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库1w正常连线到节点：导入外部oracle数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_78_LineNode(self):
		u"""节点导入外部oracle数据库1w正常连线到节点：导入外部mysql数据库1w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库1w正常",
				"终止节点名称": "导入外部mysql数据库1w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库1w正常连线到节点：导入外部mysql数据库1w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_79_LineNode(self):
		u"""节点导入外部mysql数据库1w正常连线到节点：导入外部pg数据库2w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库1w正常",
				"终止节点名称": "导入外部pg数据库2w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库1w正常连线到节点：导入外部pg数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_80_LineNode(self):
		u"""节点导入外部pg数据库2w正常连线到节点：导入外部oracle数据库2w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库2w正常",
				"终止节点名称": "导入外部oracle数据库2w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库2w正常连线到节点：导入外部oracle数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_81_LineNode(self):
		u"""节点导入外部oracle数据库2w正常连线到节点：导入外部mysql数据库2w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库2w正常",
				"终止节点名称": "导入外部mysql数据库2w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库2w正常连线到节点：导入外部mysql数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_82_LineNode(self):
		u"""节点导入外部mysql数据库2w正常连线到节点：导入外部mysql数据库2w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库2w正常",
				"终止节点名称": "导入外部pg数据库5w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库2w正常连线到节点：导入外部mysql数据库2w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_83_LineNode(self):
		u"""节点导入外部mysql数据库2w正常连线到节点：导入外部oracle数据库5w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库2w正常",
				"终止节点名称": "导入外部oracle数据库5w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库2w正常连线到节点：导入外部oracle数据库5w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_84_LineNode(self):
		u"""节点导入外部oracle数据库5w正常连线到节点：导入外部mysql数据库5w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库5w正常",
				"终止节点名称": "导入外部mysql数据库5w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库5w正常连线到节点：导入外部mysql数据库5w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_85_LineNode(self):
		u"""节点导入外部mysql数据库5w正常连线到节点：导入外部pg数据库10w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库5w正常",
				"终止节点名称": "导入外部pg数据库10w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库5w正常连线到节点：导入外部pg数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_86_LineNode(self):
		u"""节点导入外部pg数据库10w正常连线到节点：导入外部oracle数据库10w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库10w正常",
				"终止节点名称": "导入外部oracle数据库10w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库10w正常连线到节点：导入外部oracle数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_87_LineNode(self):
		u"""节点导入外部oracle数据库10w正常连线到节点：导入外部mysql数据库10w正常"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库10w正常",
				"终止节点名称": "导入外部mysql数据库10w正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库10w正常连线到节点：导入外部mysql数据库10w正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_88_LineNode(self):
		u"""节点导入外部mysql数据库10w正常连线到节点：导入外部pg数据库1w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库10w正常",
				"终止节点名称": "导入外部pg数据库1w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库10w正常连线到节点：导入外部pg数据库1w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_89_LineNode(self):
		u"""节点导入外部pg数据库1w部分成功连线到节点：导入外部oracle数据库1w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库1w部分成功",
				"终止节点名称": "导入外部oracle数据库1w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库1w部分成功连线到节点：导入外部oracle数据库1w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_90_LineNode(self):
		u"""节点导入外部oracle数据库1w部分成功连线到节点：导入外部mysql数据库1w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库1w部分成功",
				"终止节点名称": "导入外部mysql数据库1w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库1w部分成功连线到节点：导入外部mysql数据库1w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_91_LineNode(self):
		u"""节点导入外部mysql数据库1w部分成功连线到节点：导入外部pg数据库2w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库1w部分成功",
				"终止节点名称": "导入外部pg数据库2w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库1w部分成功连线到节点：导入外部pg数据库2w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_92_LineNode(self):
		u"""节点导入外部pg数据库2w部分成功连线到节点：导入外部oracle数据库2w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库2w部分成功",
				"终止节点名称": "导入外部oracle数据库2w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库2w部分成功连线到节点：导入外部oracle数据库2w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_93_LineNode(self):
		u"""节点导入外部oracle数据库2w部分成功连线到节点：导入外部mysql数据库2w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库2w部分成功",
				"终止节点名称": "导入外部mysql数据库2w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库2w部分成功连线到节点：导入外部mysql数据库2w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_94_LineNode(self):
		u"""节点导入外部mysql数据库2w部分成功连线到节点：导入外部pg数据库5w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库2w部分成功",
				"终止节点名称": "导入外部pg数据库5w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库2w部分成功连线到节点：导入外部pg数据库5w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_95_LineNode(self):
		u"""节点导入外部pg数据库5w部分成功连线到节点：导入外部oracle数据库5w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库5w部分成功",
				"终止节点名称": "导入外部oracle数据库5w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库5w部分成功连线到节点：导入外部oracle数据库5w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_96_LineNode(self):
		u"""节点导入外部oracle数据库5w部分成功连线到节点：导入外部mysql数据库5w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库5w部分成功",
				"终止节点名称": "导入外部mysql数据库5w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库5w部分成功连线到节点：导入外部mysql数据库5w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_97_LineNode(self):
		u"""节点导入外部mysql数据库5w部分成功连线到节点：导入外部pg数据库10w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部mysql数据库5w部分成功",
				"终止节点名称": "导入外部pg数据库10w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部mysql数据库5w部分成功连线到节点：导入外部pg数据库10w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_98_LineNode(self):
		u"""节点导入外部pg数据库10w部分成功连线到节点：导入外部oracle数据库10w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部pg数据库10w部分成功",
				"终止节点名称": "导入外部oracle数据库10w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部pg数据库10w部分成功连线到节点：导入外部oracle数据库10w部分成功 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_99_LineNode(self):
		u"""节点导入外部oracle数据库10w部分成功连线到节点：导入外部mysql数据库10w部分成功"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_外部库导入效率",
				"起始节点名称": "导入外部oracle数据库10w部分成功",
				"终止节点名称": "导入外部mysql数据库10w部分成功",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点导入外部oracle数据库10w部分成功连线到节点：导入外部mysql数据库10w部分成功 <<<<<')
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
