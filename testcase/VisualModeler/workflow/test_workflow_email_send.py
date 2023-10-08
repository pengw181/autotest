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


class WorkFlowEmailNodeSend(unittest.TestCase):

	log.info("装载流程邮件发送测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ProcessDataClear(self):
		u"""流程数据清理，删除历史数据"""
		action = {
			"操作": "ProcessDataClear",
			"参数": {
				"流程名称": "auto_流程_邮件发送"
			}
		}
		log.info('>>>>> 流程数据清理，删除历史数据 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_2_AddProcess(self):
		u"""添加流程，测试邮件节点"""
		action = {
			"操作": "AddProcess",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"专业领域": [
					"AiSee",
					"auto域"
				],
				"流程类型": "主流程",
				"流程说明": "auto_流程_邮件发送说明"
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加流程，测试邮件节点 <<<<<')
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
				"流程名称": "auto_流程_邮件发送",
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
				"流程名称": "auto_流程_邮件发送",
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
		u"""通用节点，添加一个自定义变量，文字信息"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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
											"Hello world."
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "文字信息"
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
		log.info('>>>>> 通用节点，添加一个自定义变量，文字信息 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，接收人"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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
											"pw@henghaodata.com"
										]
									],
									[
										"并集",
										""
									],
									[
										"自定义值",
										[
											"aireade.p@outlook.com"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "接收人"
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
		log.info('>>>>> 通用节点，添加一个自定义变量，接收人 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_NodeOptConf(self):
		u"""通用节点，添加一个自定义变量，标题"""
		action = {
			"操作": "NodeOptConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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
											"自动化测试"
										]
									]
								],
								"输出名称": {
									"类型": "输入",
									"变量名": "标题"
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
		log.info('>>>>> 通用节点，添加一个自定义变量，标题 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，不带附件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "普通邮件发送",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com",
								"aireade.p@outlook.com"
							]
						},
						"标题": "auto_流程_测试邮件(1)",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：普通邮件发送测试"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，不带附件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，收件人为变量"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "收件人为变量",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "变量",
							"值": "接收人"
						},
						"标题": "auto_流程_测试邮件(2)",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：收件人为变量"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，收件人为变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，抄送人从列表选择"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "抄送人从列表选择",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com"
							]
						},
						"抄送人": {
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com",
								"aireade.p@outlook.com"
							]
						},
						"标题": "auto_流程_测试邮件(3)",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：抄送人从列表选择"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，抄送人从列表选择 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，抄送人为变量"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "抄送人为变量",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com"
							]
						},
						"抄送人": {
							"方式": "变量",
							"值": "接收人"
						},
						"标题": "auto_流程_测试邮件(4)",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：抄送人为变量"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，抄送人为变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，标题引用变量"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "标题引用变量",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com",
								"aireade.p@outlook.com"
							]
						},
						"标题": "auto_流程_测试邮件(5)_${标题}",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：标题引用变量"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，标题引用变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddNode(self):
		u"""画流程图，添加一个邮件节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 画流程图，添加一个邮件节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，带附件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "邮件节点",
				"业务配置": {
					"节点名称": "带附件邮件发送",
					"邮件模式": "发送",
					"参数配置": {
						"发件人": "pw@henghaodata.com",
						"收件人": {
							"类型": "自定义",
							"方式": "请选择",
							"值": [
								"pw@henghaodata.com",
								"aireade.p@outlook.com"
							]
						},
						"标题": "auto_流程_测试邮件(6)",
						"正文": [
							{
								"类型": "自定义值",
								"自定义值": "节点：带附件邮件发送"
							},
							{
								"类型": "快捷键",
								"快捷键": "换行"
							},
							{
								"类型": "变量",
								"变量分类": "自定义变量",
								"变量名": "文字信息"
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，带附件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，携带附件，动态生成"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "带附件邮件发送",
				"业务配置": {
					"参数配置": {
						"附件": [
							{
								"操作类型": "添加",
								"附件配置": {
									"附件来源": "动态生成",
									"附件标题": "动态生成标题",
									"附件内容": "动态生成内容",
									"附件类型": "csv"
								}
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，携带附件，动态生成 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，携带附件，本地上传"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "带附件邮件发送",
				"业务配置": {
					"参数配置": {
						"附件": [
							{
								"操作类型": "添加",
								"附件配置": {
									"附件来源": "本地上传",
									"文件名": "factor.xlsx"
								}
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，携带附件，本地上传 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，携带附件，远程加载，本地文件，关键字匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "带附件邮件发送",
				"业务配置": {
					"参数配置": {
						"附件": [
							{
								"操作类型": "添加",
								"附件配置": {
									"附件来源": "远程加载",
									"存储类型": "本地",
									"变量引用": "否",
									"目录": "auto_一级目录",
									"过滤类型": "关键字",
									"文件名": "加载文件",
									"附件类型": "docx"
								}
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，携带附件，远程加载，本地文件，关键字匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，携带附件，远程加载，个人目录，正则匹配"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "带附件邮件发送",
				"业务配置": {
					"参数配置": {
						"附件": [
							{
								"操作类型": "添加",
								"附件配置": {
									"附件来源": "远程加载",
									"存储类型": "本地",
									"目录": "auto_普通发票",
									"变量引用": "否",
									"过滤类型": "正则",
									"文件名": {
										"设置方式": "选择",
										"正则模版名称": "auto_正则模版_匹配数字"
									},
									"附件类型": "jpg"
								}
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，携带附件，远程加载，个人目录，正则匹配 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_NodeBusinessConf(self):
		u"""配置邮件节点，邮件发送，携带附件，远程加载，ftp，正则匹配文件"""
		action = {
			"操作": "NodeBusinessConf",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"节点类型": "邮件节点",
				"节点名称": "带附件邮件发送",
				"业务配置": {
					"参数配置": {
						"附件": [
							{
								"操作类型": "添加",
								"附件配置": {
									"附件来源": "远程加载",
									"存储类型": "远程",
									"远程服务器": "auto_ftp",
									"目录": "根目录-pw-1",
									"变量引用": "否",
									"过滤类型": "正则",
									"文件名": {
										"设置方式": "添加",
										"正则模版名称": "auto_正则模版",
										"标签配置": [
											{
												"标签": "任意中文字符",
												"长度": "1到多个",
												"是否取值": "无"
											},
											{
												"标签": "字母",
												"长度": "1到多个",
												"是否取值": "无"
											}
										]
									},
									"附件类型": "pdf"
								}
							}
						]
					}
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 配置邮件节点，邮件发送，携带附件，远程加载，ftp，正则匹配文件 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_25_LineNode(self):
		u"""开始节点连线到节点：参数设置"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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

	def test_26_LineNode(self):
		u"""节点参数设置连线到：普通邮件发送"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "参数设置",
				"终止节点名称": "普通邮件发送",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点参数设置连线到：普通邮件发送 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_27_LineNode(self):
		u"""节点普通邮件发送连线到：收件人为变量"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "普通邮件发送",
				"终止节点名称": "收件人为变量",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点普通邮件发送连线到：收件人为变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_LineNode(self):
		u"""节点收件人为变量连线到：抄送人从列表选择"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "收件人为变量",
				"终止节点名称": "抄送人从列表选择",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点收件人为变量连线到：抄送人从列表选择 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_LineNode(self):
		u"""节点抄送人从列表选择连线到：抄送人为变量"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "抄送人从列表选择",
				"终止节点名称": "抄送人为变量",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点抄送人从列表选择连线到：抄送人为变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_LineNode(self):
		u"""节点抄送人为变量连线到：标题引用变量"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "抄送人为变量",
				"终止节点名称": "标题引用变量",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点抄送人为变量连线到：标题引用变量 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_LineNode(self):
		u"""节点标题引用变量连线到：带附件邮件发送"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "标题引用变量",
				"终止节点名称": "带附件邮件发送",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点标题引用变量连线到：带附件邮件发送 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_AddNode(self):
		u"""画流程图，添加一个结束节点"""
		action = {
			"操作": "AddNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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

	def test_33_SetEndNode(self):
		u"""设置结束节点状态为正常"""
		action = {
			"操作": "SetEndNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
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

	def test_34_LineNode(self):
		u"""节点带附件邮件发送连线到结束节点"""
		action = {
			"操作": "LineNode",
			"参数": {
				"流程名称": "auto_流程_邮件发送",
				"起始节点名称": "带附件邮件发送",
				"终止节点名称": "正常",
				"关联关系": "满足"
			}
		}
		checks = """
		CheckMsg|操作成功
		"""
		log.info('>>>>> 节点带附件邮件发送连线到结束节点 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_TestProcess(self):
		u"""流程列表，测试流程"""
		action = {
			"操作": "TestProcess",
			"参数": {
				"流程名称": "auto_流程_邮件发送"
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
