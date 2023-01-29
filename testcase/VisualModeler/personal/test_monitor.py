# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/13 下午6:18

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class MyMonitor(unittest.TestCase):

    log.info("装载我的监控配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_dashboard_clear(self):
        u"""仪表盘数据清理"""
        action = {
            "操作": "ClearDashboard",
            "参数": {
                "仪表盘名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_dashboard_add(self):
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
        CheckData|${Database}.dashboard.dashboard_main|1|dashboard_name|auto_我的监控_仪表盘
        """
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)
        result = self.worker.check(checks)
        assert result

    def test_3_dashboard_edit(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_dashboard_delete(self):
        u"""删除仪表盘"""
        action = {
            "操作": "DeleteDashboard",
            "参数": {
                "仪表盘名称": "auto_我的监控_仪表盘2"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_dashboard_add(self):
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
        CheckData|${Database}.dashboard.dashboard_main|1|dashboard_name|auto_我的监控_仪表盘
        """
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)
        result = self.worker.check(checks)
        assert result

    def test_6_field_classify(self):
        u"""选择网元其它资料推送表格，数据字段分类"""
        pres = """
        ${Database}.main|select zg_table_name from zg_temp_cfg where zg_temp_name='auto_网元其它资料_vm仪表盘' and zg_temp_type='3'|TableNameEn
        ${Database}.dashboard|delete from dashboard_table_col_rel where table_name_en='${TableNameEn}'
        """
        action = {
            "操作": "FieldClassify",
            "参数": {
                "表中文名称": "auto_网元其它资料_vm仪表盘",
                "维度字段": ["姓名"],
                "度量字段": ["分数"],
                "分组字段": ["等级"]
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_dictionary_clear(self):
        u"""清除字典"""
        action = {
            "操作": "ClearDictionary",
            "参数": {
                "字典名": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_8_dictionary_add(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_dictionary_add(self):
        u"""添加字典，名称已存在"""
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
        msg = "字典名称重复"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_dictionary_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_dictionary_delete(self):
        u"""删除字典"""
        action = {
            "操作": "DeleteDictionary",
            "参数": {
                "字典名": "auto_字典_风向2"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_dictionary_add(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_image_clear(self):
        u"""图像，数据清理"""
        action = {
            "操作": "ClearImage",
            "参数": {
                "图像名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_14_image_add(self):
        u"""添加图像，数据表格图"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_image_add(self):
        u"""添加图像，柱状图"""
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
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_image_add(self):
        u"""添加图像，折线图"""
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
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_image_add(self):
        u"""添加图像，饼图"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_image_add(self):
        u"""添加图像，雷达图"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_image_add(self):
        u"""添加图像，仪表图"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_image_add(self):
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
        msg = "该图像名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_image_delete(self):
        u"""删除图像"""
        action = {
            "操作": "DeleteImage",
            "参数": {
                "图像名称": "auto_我的监控_仪表图"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_image_add(self):
        u"""添加图像，仪表图"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_dashboard_mage_show(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_image_delete(self):
        u"""删除图像，图像已被仪表盘绑定"""
        action = {
            "操作": "DeleteImage",
            "参数": {
                "图像名称": "auto_我的监控_仪表图"
            }
        }
        msg = "删除可视化图像信息失败，图像已经被仪表盘使用！"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
