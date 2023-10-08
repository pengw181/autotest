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


class MyMonitor(unittest.TestCase):

	log.info("装载我的监控测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ClearDashboard(self):
		u"""我的监控仪表盘，数据清理"""
		pres = """
		${Database}.dashboard|delete from dashboard_visual_image where visual_image_name like 'auto_%' and interface_id not in (select interface_id from dashboard_data_interface)
		"""
		action = {
			"操作": "ClearDashboard",
			"参数": {
				"仪表盘名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 我的监控仪表盘，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddDashboard(self):
		u"""添加仪表盘"""
		action = {
			"操作": "AddDashboard",
			"参数": {
				"仪表盘配置": {
					"仪表盘名称": "auto_我的监控_仪表盘",
					"仪表盘副标题": "自动化仪表盘${yyyyMMdd}",
					"备注": "auto_我的监控_仪表盘",
					"主题样式": "四季主题",
					"显示标题": "显示",
					"启用轮播": "启用",
					"轮播间隔": "5"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_main|1|dashboard_name|auto_我的监控_仪表盘|dashboard_sub_name|自动化仪表盘${yyyyMMdd}|remark|auto_我的监控_仪表盘|dashboard_cfg|{"themeStyle":"seasons","showTitle":true,"carouselAuto":true,"carouselInterval":"5","blocks":[]}|default_dashboard|0|theme_id|${BelongID}_${DomainID}_VisualModeler|is_share|0|share_time|null|dashboard_from|1|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now
		"""
		log.info('>>>>> 添加仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_EditDashboard(self):
		u"""编辑仪表盘"""
		action = {
			"操作": "EditDashboard",
			"参数": {
				"仪表盘名称": "auto_我的监控_仪表盘",
				"修改内容": {
					"仪表盘配置": {
						"仪表盘名称": "auto_我的监控_仪表盘2",
						"仪表盘副标题": "自动化仪表盘${yyyy-MM-dd}",
						"备注": "auto_我的监控_仪表盘2",
						"主题样式": "冰淇淋主题",
						"显示标题": "隐藏",
						"启用轮播": "禁用",
						"轮播间隔": ""
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 编辑仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_DeleteDashboard(self):
		u"""删除仪表盘"""
		action = {
			"操作": "DeleteDashboard",
			"参数": {
				"仪表盘名称": "auto_我的监控_仪表盘2"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddDashboard(self):
		u"""添加仪表盘"""
		action = {
			"操作": "AddDashboard",
			"参数": {
				"仪表盘配置": {
					"仪表盘名称": "auto_我的监控_仪表盘",
					"仪表盘副标题": "自动化仪表盘${yyyyMMdd}",
					"备注": "auto_我的监控_仪表盘",
					"主题样式": "四季主题",
					"显示标题": "显示",
					"启用轮播": "启用",
					"轮播间隔": "5"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_main|1|dashboard_name|auto_我的监控_仪表盘|dashboard_sub_name|自动化仪表盘${yyyyMMdd}|remark|auto_我的监控_仪表盘|dashboard_cfg|{"themeStyle":"seasons","showTitle":true,"carouselAuto":true,"carouselInterval":"5","blocks":[]}|default_dashboard|0|theme_id|${BelongID}_${DomainID}_VisualModeler|is_share|0|share_time|null|dashboard_from|1|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now
		"""
		log.info('>>>>> 添加仪表盘 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_FieldClassify(self):
		u"""选择网元其它资料推送表格，数据字段分类"""
		pres = """
		${Database}.main|select zg_table_name from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and zg_temp_type='3'|TableNameEn
		${Database}.dashboard|delete from dashboard_table_col_rel where table_name_en='${TableNameEn}'
		"""
		action = {
			"操作": "FieldClassify",
			"参数": {
				"表中文名称": "auto_网元其它资料_vm仪表盘",
				"维度字段": [
					"姓名"
				],
				"度量字段": [
					"分数"
				],
				"分组字段": [
					"等级"
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_table_col_rel|1|col_name_en|COL_2|col_name_ch|姓名|col_data_type|VARCHAR|col_type|X|remark||data_format||table_name_en|${TableNameEn}|database_id|${BelongID}_${DomainID}|import_data_type|网元其它资料
		CheckData|${Database}.dashboard.dashboard_table_col_rel|1|col_name_en|COL_3|col_name_ch|等级|col_data_type|VARCHAR|col_type|G|remark||data_format||table_name_en|${TableNameEn}|database_id|${BelongID}_${DomainID}|import_data_type|网元其它资料
		CheckData|${Database}.dashboard.dashboard_table_col_rel|1|col_name_en|COL_4|col_name_ch|分数|col_data_type|NUMBER|col_type|Y|remark||data_format||table_name_en|${TableNameEn}|database_id|${BelongID}_${DomainID}|import_data_type|网元其它资料
		"""
		log.info('>>>>> 选择网元其它资料推送表格，数据字段分类 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_ClearDictionary(self):
		u"""字典管理，数据清理"""
		action = {
			"操作": "ClearDictionary",
			"参数": {
				"字典名": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 字典管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_8_AddDictionary(self):
		u"""添加字典"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典配置": [
					{
						"字典名称": "auto_字典_风向",
						"主题分类": "基础分类",
						"数据接口": "auto_网元其它资料_vm仪表盘",
						"字典项": "wind.txt"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddDictionary(self):
		u"""添加字典，字典名称已存在"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典配置": [
					{
						"字典名称": "auto_字典_风向",
						"主题分类": "基础分类",
						"数据接口": "auto_网元其它资料_vm仪表盘",
						"字典项": "wind.txt"
					}
				]
			}
		}
		checks = """
		CheckMsg|字典名称重复
		"""
		log.info('>>>>> 添加字典，字典名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateDictionary(self):
		u"""编辑字典"""
		action = {
			"操作": "UpdateDictionary",
			"参数": {
				"字典名": "auto_字典_风向",
				"修改内容": {
					"字典配置": {
						"字典名称": "auto_字典_风向2",
						"主题分类": "基础分类",
						"数据接口": "auto_网元其它资料_vm仪表盘",
						"字典项": "wind.txt"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 编辑字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteDictionary(self):
		u"""删除字典"""
		action = {
			"操作": "DeleteDictionary",
			"参数": {
				"字典名": "auto_字典_风向2"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddDictionary(self):
		u"""添加字典"""
		action = {
			"操作": "AddDictionary",
			"参数": {
				"字典配置": [
					{
						"字典名称": "auto_字典_风向",
						"主题分类": "基础分类",
						"数据接口": "auto_网元其它资料_vm仪表盘",
						"字典项": "wind.txt"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		"""
		log.info('>>>>> 添加字典 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_ClearImage(self):
		u"""可视化图像管理，数据清理"""
		action = {
			"操作": "ClearImage",
			"参数": {
				"图像名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 可视化图像管理，数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_14_AddImage(self):
		u"""添加图像，数据表格图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_数据表格",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "数据表格",
					"数据源配置": {
						"数据列": [
							{
								"列选择": "姓名",
								"自定义名称": "姓名",
								"自定义列颜色": "#40E0D0"
							},
							{
								"列选择": "等级",
								"自定义名称": "等级",
								"自定义列颜色": "#9370DB"
							},
							{
								"列选择": "分数",
								"自定义名称": "分数",
								"自定义列颜色": "#808080"
							}
						]
					},
					"样式配置": {
						"主题样式": "青春主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "26",
						"每页展示条数": "50",
						"列对齐方式": "居中",
						"列宽度": "自适应列宽",
						"冻结列": "姓名"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_数据表格|visual_image_type|table|visual_image_cfg|{"ds":{"sort":[],"dictionaryEscape":[],"filterColumns":[],"y":[{"colNameEN":"COL_2","colNameCH":"姓名","color":"#40e0d0"},{"colNameEN":"COL_3","colNameCH":"等级","color":"#9370db"},{"colNameEN":"COL_4","colNameCH":"分数","color":"#808080"}]},"style":{"theme":"youth","whetherCustomBgColor":"y","backgroundColor":"#ffdead","pageSize":50,"colAlign":"center","colWidth":"auto","frozenColumn":"COL_2","titleVisible":true,"titleAlign":"center","titleFontSize":26}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，数据表格图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddImage(self):
		u"""添加图像，柱状图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_柱状图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "柱状图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数"
							}
						],
						"x轴": {
							"维度": "姓名",
							"自定义名称": "姓名"
						},
						"排序": [
							{
								"排序字段": "姓名",
								"排序方式": "升序"
							}
						]
					},
					"样式配置": {
						"主题样式": "自定义主题",
						"自定义主题色彩": [
							"#40E0D0",
							"#9370DB",
							"#808080"
						],
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"数据展示方向": "横向",
						"是否显示度量": "显示",
						"度量字体大小": "12",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "25",
						"坐标轴名称字体大小": "12",
						"坐标轴刻度标签字体大小": "11",
						"X轴区域缩放": {
							"状态": "开启",
							"X轴起始百分比": "0",
							"X轴结束百分比": "100"
						},
						"Y轴区域缩放": {
							"状态": "开启",
							"Y轴起始百分比": "0",
							"Y轴结束百分比": "100"
						},
						"图像类型": "柱状图"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_柱状图|visual_image_type|bar|visual_image_cfg|{"ds":{"sort":[{"colNameEN":"COL_2","order":"ASC"}],"dictionaryEscape":[],"filterColumns":[],"y":[{"colNameEN":"COL_4","colNameCH":"分数"}],"x":{"colNameEN":"COL_2","colNameCH":"姓名","isDynamicShow":false},"g":{},"drill":[]},"style":{"legendDirection":"vertical","legendAlign":"left-up","titleAlign":"center","dataDirection":"horizontal","style":"ns","series":{"分数":{"imageType":"bar"}},"theme":"custom","themeColorList":["#40e0d0","#9370db","#808080"],"whetherCustomBgColor":"y","backgroundColor":"#ffdead","showMeasure":true,"labelFontSize":12,"titleVisible":true,"titleFontSize":25,"nameTextStyleFontSize":12,"axisLabelFontSize":11,"dataZoom":{"xDataZoom":{"show":true,"start":0,"end":100},"yDataZoom":{"show":true,"start":0,"end":100}},"legendVisible":true,"legendFontSize":12,"legendSortable":false}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，柱状图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddImage(self):
		u"""添加图像，折线图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_折线图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "折线图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数"
							}
						],
						"x轴": {
							"维度": "姓名",
							"自定义名称": "姓名"
						},
						"排序": [
							{
								"排序字段": "姓名",
								"排序方式": "升序"
							}
						]
					},
					"样式配置": {
						"主题样式": "自定义主题",
						"自定义主题色彩": [
							"#40E0D0",
							"#9370DB",
							"#808080"
						],
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"区域填充颜色": "不填充",
						"是否显示度量": "显示",
						"度量字体大小": "10",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "20",
						"坐标轴名称字体大小": "12",
						"坐标轴刻度标签字体大小": "10",
						"X轴区域缩放": {
							"状态": "开启",
							"X轴起始百分比": "0",
							"X轴结束百分比": "100"
						},
						"Y轴区域缩放": {
							"状态": "开启",
							"Y轴起始百分比": "0",
							"Y轴结束百分比": "100"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_折线图|visual_image_type|line|visual_image_cfg|{"ds":{"sort":[{"colNameEN":"COL_2","order":"ASC"}],"dictionaryEscape":[],"filterColumns":[],"y":[{"colNameEN":"COL_4","colNameCH":"分数"}],"x":{"colNameEN":"COL_2","colNameCH":"姓名","isDynamicShow":false},"g":{},"drill":[]},"style":{"legendDirection":"vertical","legendAlign":"left-up","titleAlign":"center","color":"n","style":"ns","theme":"custom","themeColorList":["#40e0d0","#9370db","#808080"],"series":{},"whetherCustomBgColor":"y","backgroundColor":"#ffdead","showMeasure":true,"labelFontSize":10,"titleVisible":true,"titleFontSize":20,"nameTextStyleFontSize":12,"axisLabelFontSize":10,"dataZoom":{"xDataZoom":{"show":true,"start":0,"end":100},"yDataZoom":{"show":true,"start":0,"end":100}},"legendVisible":true,"legendFontSize":12}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，折线图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_AddImage(self):
		u"""添加图像，饼图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_饼图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "饼状图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数"
							}
						],
						"x轴": {
							"维度": "姓名",
							"自定义名称": "姓名"
						},
						"排序": [
							{
								"排序字段": "分数",
								"排序方式": "升序"
							}
						]
					},
					"样式配置": {
						"主题样式": "默认主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"饼图样式": "饼图",
						"半径": "75",
						"是否显示图例": "显示",
						"图例标示方向": "竖向",
						"图例对齐方式": "左对齐",
						"图例字体大小": "15",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "25",
						"启用图例拖拽排序": "开启"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_饼图|visual_image_type|pie|visual_image_cfg|{"ds":{"sort":[{"colNameEN":"COL_4","order":"ASC"}],"dictionaryEscape":[],"filterColumns":[],"y":[{"colNameEN":"COL_4","colNameCH":"分数"}],"x":{"colNameEN":"COL_2","colNameCH":"姓名"},"g":{},"drill":[]},"style":{"legendDirection":"vertical","legendAlign":"left-up","titleAlign":"center","style":"normal","radius":75,"innerRadius":60,"outerRadius":80,"theme":"default","themeColorList":[],"series":{},"whetherCustomBgColor":"y","backgroundColor":"#ffdead","legendVisible":true,"legendFontSize":15,"titleVisible":true,"titleFontSize":25,"legendSortable":true,"legendSort":["moserah","luna","mcclamroch","naismith","haveman","gaouette","jabara","barkdull","yearsley","handelman","kysha","shehan","kehoe","bolam","theophilus"]}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，饼图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_AddImage(self):
		u"""添加图像，雷达图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_雷达图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "雷达图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数"
							}
						],
						"x轴": {
							"维度": "姓名",
							"自定义名称": "姓名"
						},
						"排序": [
							{
								"排序字段": "分数",
								"排序方式": "升序"
							}
						]
					},
					"样式配置": {
						"主题样式": "青春主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"是否显示图例": "显示",
						"图例标示方向": "竖向",
						"图例对齐方式": "左对齐",
						"图例字体大小": "20",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "26",
						"半径": "70",
						"最小值": "1",
						"最大值": "100"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_雷达图|visual_image_type|radar|visual_image_cfg|{"ds":{"sort":[{"colNameEN":"COL_4","order":"ASC"}],"dictionaryEscape":[],"filterColumns":[],"y":[{"colNameEN":"COL_4","colNameCH":"分数"}],"x":{"colNameEN":"COL_2","colNameCH":"姓名"},"g":{},"drill":[]},"style":{"legendDirection":"vertical","legendAlign":"left-up","titleAlign":"center","dataDirection":"vertical","series":{"moserah":{"min":1,"max":100},"luna":{"min":1,"max":100},"mcclamroch":{"min":1,"max":100},"naismith":{"min":1,"max":100},"haveman":{"min":1,"max":100},"gaouette":{"min":1,"max":100},"jabara":{"min":1,"max":100},"barkdull":{"min":1,"max":100},"yearsley":{"min":1,"max":100},"handelman":{"min":1,"max":100},"kysha":{"min":1,"max":100},"shehan":{"min":1,"max":100},"kehoe":{"min":1,"max":100},"bolam":{"min":1,"max":100},"theophilus":{"min":1,"max":100}},"theme":"youth","themeColorList":[],"whetherCustomBgColor":"y","backgroundColor":"#ffdead","legendVisible":true,"legendFontSize":20,"titleVisible":true,"titleFontSize":26,"radius":70}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，雷达图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_AddImage(self):
		u"""添加图像，仪表图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_仪表图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "仪表图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数",
								"度量单位": "分数"
							}
						],
						"数据过滤": [
							{
								"过滤字段": "姓名",
								"自定义名称": "姓名",
								"逻辑关系": "等于",
								"动态查询": "启用",
								"作用范围": "图像"
							}
						]
					},
					"样式配置": {
						"主题样式": "青春主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "26",
						"上边距": "50",
						"左边距": "50",
						"半径": "79",
						"开始角度": "228",
						"角度大小": "276",
						"低阈比例": "60",
						"高阈比例": "90",
						"最小值": "0",
						"最大值": "100"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_仪表图|visual_image_type|gauge|visual_image_cfg|{"ds":{"sort":[],"dictionaryEscape":[],"filterColumns":[{"colNameEN":"COL_2","aliases":"姓名","operand":"{EQUALS}","value":"","isDynamic":true,"range":"image","isOptional":true}],"y":[{"colNameEN":"COL_4","colNameCH":"分数","unit":"分数"}]},"style":{"titleAlign":"center","series":{"分数":{"top":50,"left":50,"radius":79,"startAngle":227,"angle":275,"threshold1":60,"threshold2":90,"min":0,"max":100}},"theme":"youth","themeColorList":[],"whetherCustomBgColor":"y","backgroundColor":"#ffdead","titleVisible":true,"titleFontSize":26}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，仪表图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddImage(self):
		u"""添加图像，图像名称已存在"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_仪表图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "仪表图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数",
								"度量单位": "分数"
							}
						],
						"数据过滤": [
							{
								"过滤字段": "姓名",
								"自定义名称": "姓名",
								"逻辑关系": "等于",
								"动态查询": "启用",
								"作用范围": "图像"
							}
						]
					},
					"样式配置": {
						"主题样式": "青春主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "26",
						"上边距": "50",
						"左边距": "50",
						"半径": "79",
						"开始角度": "228",
						"角度大小": "276",
						"低阈比例": "60",
						"高阈比例": "90",
						"最小值": "0",
						"最大值": "100"
					}
				}
			}
		}
		checks = """
		CheckMsg|该图像名称已存在
		"""
		log.info('>>>>> 添加图像，图像名称已存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_DeleteImage(self):
		u"""删除图像"""
		action = {
			"操作": "DeleteImage",
			"参数": {
				"图像名称": "auto_我的监控_仪表图"
			}
		}
		checks = """
		CheckMsg|删除成功
		"""
		log.info('>>>>> 删除图像 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_AddImage(self):
		u"""添加图像，仪表图"""
		pres = """
		${Database}.dashboard|select interface_id from dashboard_data_interface where interface_name='auto_网元其它资料_vm仪表盘' and save_type='1'|InterfaceId|
		"""
		action = {
			"操作": "AddImage",
			"参数": {
				"图像配置": {
					"图像名称": "auto_我的监控_仪表图",
					"数据接口": "auto_网元其它资料_vm仪表盘",
					"图像类型": "仪表图",
					"数据源配置": {
						"y轴": [
							{
								"度量": "分数",
								"自定义名称": "分数",
								"度量单位": "分数"
							}
						],
						"数据过滤": [
							{
								"过滤字段": "姓名",
								"自定义名称": "姓名",
								"逻辑关系": "等于",
								"动态查询": "启用",
								"作用范围": "图像"
							}
						]
					},
					"样式配置": {
						"主题样式": "青春主题",
						"自定义背景颜色": "是",
						"背景颜色": "#FFDEAD",
						"是否显示标题": "显示",
						"标题对齐方式": "居中",
						"标题字体大小": "26",
						"上边距": "50",
						"左边距": "50",
						"半径": "79",
						"开始角度": "228",
						"角度大小": "276",
						"低阈比例": "60",
						"高阈比例": "90",
						"最小值": "0",
						"最大值": "100"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.dashboard.dashboard_visual_image|1|visual_image_name|auto_我的监控_仪表图|visual_image_type|gauge|visual_image_cfg|{"ds":{"sort":[],"dictionaryEscape":[],"filterColumns":[{"colNameEN":"COL_2","aliases":"姓名","operand":"{EQUALS}","value":"","isDynamic":true,"range":"image","isOptional":true}],"y":[{"colNameEN":"COL_4","colNameCH":"分数","unit":"分数"}]},"style":{"titleAlign":"center","series":{"分数":{"top":50,"left":50,"radius":79,"startAngle":227,"angle":275,"threshold1":60,"threshold2":90,"min":0,"max":100}},"theme":"youth","themeColorList":[],"whetherCustomBgColor":"y","backgroundColor":"#ffdead","titleVisible":true,"titleFontSize":26}}|user_id|${LoginUser}|create_time|now|original_user_id|${LoginUser}|original_time|now|update_time|now|interface_id|${InterfaceId}|visual_from|1
		"""
		log.info('>>>>> 添加图像，仪表图 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_AddInImage(self):
		u"""仪表盘添加图像"""
		action = {
			"操作": "AddInImage",
			"参数": {
				"仪表盘名称": "auto_我的监控_仪表盘",
				"图像列表": [
					"auto_我的监控_柱状图",
					"auto_我的监控_折线图",
					"auto_我的监控_饼图",
					"auto_我的监控_仪表图",
					"auto_我的监控_数据表格",
					"auto_我的监控_雷达图"
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.dashboard|select dashboard_id from dashboard_main where dashboard_name='auto_我的监控_仪表盘'|DashboardID
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_柱状图'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_0"}
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_折线图'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_1"}
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_饼图'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_2"}
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_仪表图'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_3"}
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_数据表格'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_4"}
		GetData|${Database}.dashboard|select visual_image_id from dashboard_visual_image where visual_image_name='auto_我的监控_雷达图'|VisualImageID
		CheckData|${Database}.dashboard.dashboard_visual_image_rel|1|dashboard_id|${DashboardID}|visual_image_id|${VisualImageID}|forward_data|{"objectId":"block_5"}
		"""
		log.info('>>>>> 仪表盘添加图像 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_DeleteImage(self):
		u"""删除图像，图像已被仪表盘引用"""
		action = {
			"操作": "DeleteImage",
			"参数": {
				"图像名称": "auto_我的监控_仪表图"
			}
		}
		checks = """
		CheckMsg|删除可视化图像信息失败，图像已经被仪表盘使用
		"""
		log.info('>>>>> 删除图像，图像已被仪表盘引用 <<<<<')
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
