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


class WorkFlowInterfaceNodeRestful(unittest.TestCase):

	log.info("装载流程restful接口调用测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_restful接口"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试接口节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_restful接口说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图，添加一个通用节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "通用节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_NodeBusinessConf(self):
		u"""配置通用节点"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "通用节点",
				"节点名称": "通用节点",
				"业务配置": {
					"节点名称": "参数设置",
					"场景标识": "无"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置通用节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，自定义文本"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"自定义值",
										[
											"hello"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "文本参数"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个自定义变量，自定义文本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，自定义文本"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"自定义值",
										[
											"guangzhou"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "姓名"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个自定义变量，自定义文本 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，内置变量，时间变量"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "通用节点",
				"节点名称": "参数设置",
				"操作配置": [
					{
						"对象": "操作",
						"右键操作": "添加操作",
						"运算配置": {
							"运算类型": "基础运算",
							"配置": {
								"表达式": [
									[
										"变量",
										{
											"变量名称": "时间变量",
											"时间格式": "yyyyMMddHHmmss",
											"间隔": "0",
											"单位": "日",
											"语言": "中文"
										}
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "当前时间"
								},
								"输出列": "*",
								"赋值方式": "替换",
								"是否转置": "否"
							}
						}
					}
				]
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 通用节点，添加一个自定义变量，内置变量，时间变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置接口节点，restful接口，请求方式post"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "post请求",
					"接口": "auto_万能mock_post",
					"请求体内容": [
						{
							"类型": "自定义值",
							"自定义值": "请求体："
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "自定义变量",
							"变量名": "当前时间"
						}
					],
					"请求头列表": {
						"param1": {
							"设置方式": "变量",
							"参数值": "文本参数"
						},
						"param2": {
							"设置方式": "固定值",
							"参数值": "2020-10-20 10:00:00"
						},
						"param3": {
							"设置方式": "固定值",
							"参数值": "hello world"
						}
					},
					"参数列表": {
						"name": {
							"设置方式": "变量",
							"参数值": "姓名"
						},
						"age": {
							"设置方式": "固定值",
							"参数值": "18"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，restful接口，请求方式post <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置接口节点，restful接口，请求方式get"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "get请求",
					"接口": "auto_万能mock_get",
					"请求体内容": [
						{
							"类型": "自定义值",
							"自定义值": "请求体："
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "自定义变量",
							"变量名": "当前时间"
						}
					],
					"请求头列表": {
						"param1": {
							"设置方式": "变量",
							"参数值": "文本参数"
						},
						"param2": {
							"设置方式": "固定值",
							"参数值": "2020-10-20 10:00:00"
						}
					},
					"参数列表": {
						"name": {
							"设置方式": "变量",
							"参数值": "姓名"
						},
						"age": {
							"设置方式": "固定值",
							"参数值": "18"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，restful接口，请求方式get <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置接口节点，restful接口，请求方式put"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "put请求",
					"接口": "auto_万能mock_put",
					"请求体内容": [
						{
							"类型": "自定义值",
							"自定义值": "请求体："
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "自定义变量",
							"变量名": "当前时间"
						}
					],
					"请求头列表": {
						"param1": {
							"设置方式": "变量",
							"参数值": "文本参数"
						},
						"param2": {
							"设置方式": "固定值",
							"参数值": "2020-10-20 10:00:00"
						}
					},
					"参数列表": {
						"age": {
							"设置方式": "固定值",
							"参数值": "18"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，restful接口，请求方式put <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置接口节点，restful接口，请求方式delete"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "delete请求",
					"接口": "auto_万能mock_delete",
					"请求体内容": [
						{
							"类型": "自定义值",
							"自定义值": "请求体："
						},
						{
							"类型": "快捷键",
							"快捷键": "换行"
						},
						{
							"类型": "变量",
							"变量分类": "自定义变量",
							"变量名": "当前时间"
						}
					],
					"请求头列表": {
						"param1": {
							"设置方式": "变量",
							"参数值": "文本参数"
						},
						"param2": {
							"设置方式": "固定值",
							"参数值": "2020-10-20 10:00:00"
						}
					},
					"参数列表": {
						"name": {
							"设置方式": "变量",
							"参数值": "姓名"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，restful接口，请求方式delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NodeBusinessConf(self):
		u"""配置接口节点，开启高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "post请求",
				"业务配置": {
					"高级配置": {
						"状态": "开启",
						"超时时间": "600",
						"超时重试次数": "2"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，开启高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddNode(self):
		u"""画流程图，添加一个接口节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个接口节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置接口节点，restful接口_notify"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "接口节点",
				"业务配置": {
					"节点名称": "restful接口_notify",
					"接口": "auto_第三方restful接口_notify"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置接口节点，restful接口_notify <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeFetchConf(self):
		u"""节点添加取数配置，返回内容为字符串"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "接口节点",
				"节点名称": "restful接口_notify",
				"取数配置": {
					"操作": "添加",
					"变量名称": "restful接口_notify返回",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点添加取数配置，返回内容为字符串 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "开始",
				"终止节点名称": "参数设置",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点：参数设置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_LineNode(self):
		u"""节点参数设置连线到节点：post请求"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "参数设置",
				"终止节点名称": "post请求",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到节点：post请求 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_LineNode(self):
		u"""节点post请求连线到节点：get请求"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "post请求",
				"终止节点名称": "get请求",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点post请求连线到节点：get请求 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_LineNode(self):
		u"""节点get请求连线到节点：put请求"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "get请求",
				"终止节点名称": "put请求",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点get请求连线到节点：put请求 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_LineNode(self):
		u"""节点put请求连线到节点：delete请求"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "put请求",
				"终止节点名称": "delete请求",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点put请求连线到节点：delete请求 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""节点delete请求连线到节点：restful接口_notify"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "delete请求",
				"终止节点名称": "restful接口_notify",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点delete请求连线到节点：restful接口_notify <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"节点类型": "结束节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"状态": "正常"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 设置结束节点状态为正常 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_LineNode(self):
		u"""节点restful接口_notify连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_restful接口",
				"起始节点名称": "restful接口_notify",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点restful接口_notify连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_restful接口"
			}
		}
		checks = """
		CheckMsg|调用测试流程成功,请到流程运行日志中查看
		"""
		log.info('>>>>> 流程列表，测试流程 <<<<<')
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
