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


class WorkFlowAiNode(unittest.TestCase):

	log.info("装载流程AI预测测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清除"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_AI预测"
			}
		}
		log.info('>>>>> 流程数据清除 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程-测试AI节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_AI预测说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程-测试AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddNode(self):
		u"""画流程图，添加一个文件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个文件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_NodeBusinessConf(self):
		u"""配置文件节点：加载AI预测数据，输出变量：单指标接入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点",
				"节点名称": "文件节点",
				"业务配置": {
					"节点名称": "加载AI预测数据",
					"操作模式": "文件加载",
					"存储参数配置": {
						"存储类型": "本地",
						"目录": "auto_AI"
					},
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "single_predict",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"sheet页索引": "1",
							"开始读取行": "2",
							"变量": "单指标接入数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点：加载AI预测数据，输出变量：单指标接入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_NodeBusinessConf(self):
		u"""配置文件节点：加载AI预测数据，输出变量：通用算法接入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点",
				"节点名称": "加载AI预测数据",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "classical_predict",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"sheet页索引": "",
							"开始读取行": "3",
							"变量": "通用算法接入数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点：加载AI预测数据，输出变量：通用算法接入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeBusinessConf(self):
		u"""配置文件节点：加载AI预测数据，输出变量：干扰因素接入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点",
				"节点名称": "加载AI预测数据",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "factor_predict",
							"文件类型": "xlsx",
							"编码格式": "UTF-8",
							"sheet页索引": "",
							"开始读取行": "",
							"变量": "干扰因素接入数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点：加载AI预测数据，输出变量：干扰因素接入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeBusinessConf(self):
		u"""配置文件节点：加载AI预测数据，输出变量：factorXGB接入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点",
				"节点名称": "加载AI预测数据",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "factorXGB_predict",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "2",
							"分隔符": ",",
							"变量": "factorXGB接入数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点：加载AI预测数据，输出变量：factorXGB接入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_NodeBusinessConf(self):
		u"""配置文件节点：加载AI预测数据，输出变量：factorLGBM接入数据"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "文件节点",
				"节点名称": "加载AI预测数据",
				"业务配置": {
					"文件配置": [
						{
							"类型": "关键字",
							"文件名": "factorLGBM_predict",
							"文件类型": "csv",
							"编码格式": "UTF-8",
							"开始读取行": "",
							"分隔符": ",",
							"变量": "factorLGBM接入数据",
							"变量类型": "替换"
						}
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置文件节点：加载AI预测数据，输出变量：factorLGBM接入数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_NodeBusinessConf(self):
		u"""配置AI节点，单指标预测，lstm模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "LSTM预测模型",
					"节点模式": "单指标预测",
					"算法选择": "LSTM预测模型",
					"模型": "auto_AI模型lstm",
					"输入变量": "单指标接入数据",
					"预测步长": "10",
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
		log.info('>>>>> 配置AI节点，单指标预测，lstm模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_NodeBusinessConf(self):
		u"""配置AI节点，单指标预测，sarima模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "SARIMA预测模型",
					"节点模式": "单指标预测",
					"算法选择": "SARIMA预测模型",
					"模型": "auto_AI模型sarima",
					"输入变量": "单指标接入数据",
					"预测步长": "10"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，单指标预测，sarima模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_NodeBusinessConf(self):
		u"""配置AI节点，存在干扰因素的多指标预测，gru模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "GRU预测模型",
					"节点模式": "存在干扰因素的多指标预测",
					"算法选择": "GRU预测模型",
					"模型": "auto_AI模型gru",
					"输入变量": "干扰因素接入数据",
					"预测步长": "5"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，存在干扰因素的多指标预测，gru模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_NodeBusinessConf(self):
		u"""配置AI节点，存在干扰因素的多指标预测，xgboost模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "xgboost预测模型",
					"节点模式": "存在干扰因素的多指标预测",
					"算法选择": "xgboost预测模型",
					"模型": "auto_AI模型xgboost",
					"输入变量": "factorXGB接入数据",
					"预测步长": "5"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，存在干扰因素的多指标预测，xgboost模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_NodeBusinessConf(self):
		u"""配置AI节点，存在干扰因素的多指标预测，factorLGBM模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "factorLGBM模型",
					"节点模式": "存在干扰因素的多指标预测",
					"算法选择": "factorLGBM",
					"模型": "auto_AI模型factorLGBM",
					"输入变量": "factorLGBM接入数据",
					"预测步长": "5"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，存在干扰因素的多指标预测，factorLGBM模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置AI节点，通用分类算法，lightgbm模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "lightgbm模型",
					"节点模式": "通用分类算法",
					"算法选择": "lightgbm模型",
					"模型": "auto_AI模型lightgbm",
					"输入变量": "通用算法接入数据"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，通用分类算法，lightgbm模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置AI节点，通用分类算法，梯度提升树（GBDT）模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "梯度提升树（GBDT）模型",
					"节点模式": "通用分类算法",
					"算法选择": "梯度提升树（GBDT）模型",
					"模型": "auto_AI模型梯度提升树（GBDT）",
					"输入变量": "通用算法接入数据"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，通用分类算法，梯度提升树（GBDT）模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddNode(self):
		u"""画流程图,添加一个AI节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个AI节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置AI节点，通用分类算法，随机森林模型"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "AI节点",
				"业务配置": {
					"节点名称": "随机森林模型",
					"节点模式": "通用分类算法",
					"算法选择": "随机森林模型",
					"模型": "auto_AI模型随机森林",
					"输入变量": "通用算法接入数据"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点，通用分类算法，随机森林模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_NodeBusinessConf(self):
		u"""配置AI节点：LSTM预测模型，设置对应关系"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "LSTM预测模型",
				"业务配置": {
					"对应关系配置": {
						"状态": "开启",
						"1": "time(时间列)",
						"2": "online_number(预测列)"
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置AI节点：LSTM预测模型，设置对应关系 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_NodeBusinessConf(self):
		u"""配置AI节点：LSTM预测模型，开启高级配置"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "LSTM预测模型",
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
		log.info('>>>>> 配置AI节点：LSTM预测模型，开启高级配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_NodeFetchConf(self):
		u"""节点LSTM预测模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "LSTM预测模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "LSTM预测模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"LSTM预测模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_NodeFetchConf(self):
		u"""节点SARIMA预测模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "SARIMA预测模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "SARIMA预测模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"SARIMA预测模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_NodeFetchConf(self):
		u"""节点GRU预测模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "GRU预测模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "GRU预测模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"GRU预测模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_NodeFetchConf(self):
		u"""节点xgboost预测模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "xgboost预测模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "xgboost预测模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"xgboost预测模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_NodeFetchConf(self):
		u"""节点factorLGBM模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "factorLGBM模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "factorLGBM模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"factorLGBM模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_NodeFetchConf(self):
		u"""节点lightgbm模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "lightgbm模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "lightgbm模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"lightgbm模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_NodeFetchConf(self):
		u"""节点梯度提升树（GBDT）模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "梯度提升树（GBDT）模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "梯度提升树（GBDT）模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"梯度提升树（GBDT）模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_NodeFetchConf(self):
		u"""节点随机森林模型添加取数配置"""
		action = {
			"操作": "NodeFetchConf",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "AI节点",
				"节点名称": "随机森林模型",
				"取数配置": {
					"操作": "添加",
					"变量名称": "随机森林模型预测结果",
					"赋值方式": "替换"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"随机森林模型"添加取数配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_LineNode(self):
		u"""开始节点连线到节点加载AI预测数据"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "开始",
				"终止节点名称": "加载AI预测数据",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 开始节点连线到节点"加载AI预测数据" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_LineNode(self):
		u"""节点加载AI预测数据连线到节点LSTM预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "加载AI预测数据",
				"终止节点名称": "LSTM预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"加载AI预测数据"连线到节点"LSTM预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_LineNode(self):
		u"""节点LSTM预测模型连线到节点SARIMA预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "LSTM预测模型",
				"终止节点名称": "SARIMA预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"LSTM预测模型"连线到节点"SARIMA预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_LineNode(self):
		u"""节点SARIMA预测模型连线到节点GRU预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "SARIMA预测模型",
				"终止节点名称": "GRU预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"SARIMA预测模型"连线到节点"GRU预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_LineNode(self):
		u"""节点GRU预测模型连线到节点xgboost预测模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "GRU预测模型",
				"终止节点名称": "xgboost预测模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"GRU预测模型"连线到节点"xgboost预测模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_LineNode(self):
		u"""节点xgboost预测模型连线到节点factorLGBM模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "xgboost预测模型",
				"终止节点名称": "factorLGBM模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"xgboost预测模型"连线到节点"factorLGBM模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_LineNode(self):
		u"""节点factorLGBM模型连线到节点lightgbm模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "factorLGBM模型",
				"终止节点名称": "lightgbm模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"factorLGBM模型"连线到节点"lightgbm模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_LineNode(self):
		u"""节点lightgbm模型连线到节点梯度提升树（GBDT）模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "lightgbm模型",
				"终止节点名称": "梯度提升树（GBDT）模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"lightgbm模型"连线到节点"梯度提升树（GBDT）模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_LineNode(self):
		u"""节点梯度提升树（GBDT）模型连线到节点随机森林模型"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "梯度提升树（GBDT）模型",
				"终止节点名称": "随机森林模型",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"梯度提升树（GBDT）模型"连线到节点"随机森林模型" <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_44_AddNode(self):
		u"""画流程图,添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"节点类型": "结束节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图,添加一个结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
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

	def test_46_LineNode(self):
		u"""节点随机森林模型连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_AI预测",
				"起始节点名称": "随机森林模型",
				"终止节点名称": "正常",
				"关联关系": "无条件"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点"随机森林模型"连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_47_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_AI预测"
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
