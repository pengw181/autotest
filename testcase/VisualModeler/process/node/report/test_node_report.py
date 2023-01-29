# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/6 下午2:54

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class ReportNode(unittest.TestCase):

    log.info("装载流程报表节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_报表节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试报表节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_报表节点流程说明",
                "高级配置": {
                    "自定义流程变量": {
                        "状态": "开启",
                        "参数列表": {
                            "时间": "2020-10-20###必填",
                            "地点": "广州###",
                            "名字": "pw###必填"
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

    def test_3_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "报表数据",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_process_node_opt_conf(self):
        u"""操作配置，添加操作，基础运算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "通用节点",
                "节点名称": "报表数据",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["自定义值", ["a1,1,15", "a2,2,11", "b1,3,20", "c1,4,19"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "数据"
                                }
                            }
                        }
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_opt_conf(self):
        u"""操作配置，添加操作，正则运算，正则拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "通用节点",
                "节点名称": "报表数据",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "数据",
                                "输出变量": "数据",
                                "赋值方式": "替换",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "否",
                                    "列总数": "3",
                                    "拆分方式": "文本",
                                    "拆分符": ",",
                                    "样例数据": ["a1,1,23", "a2,2,30", "a3,3,11"]
                                }
                            }
                        }
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_add(self):
        u"""画流程图，添加一个报表节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置报表节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点",
                "节点名称": "报表节点",
                "业务配置": {
                    "节点名称": "通用报表",
                    "操作方式": "添加",
                    "变量选择": "数据",
                    "变量索引配置": [
                        ["1", "名称", "字符", "", "X轴(维度)"],
                        ["2", "等级", "字符", "", "分组"],
                        ["3", "分数", "数字", "", "Y轴(度量)"]
                    ],
                    "数据接口名称": "通用报表数据",
                    "备注": "通用报表数据",
                    "样例数据": "report_sample.txt"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_access_dashboard(self):
        u"""从报表节点进入仪表盘"""
        action = {
            "操作": "AccessReportDashboard",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点名称": "通用报表"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_dashboard_conf(self):
        u"""添加仪表盘"""
        pres = """
        ${Database}.dashboard|delete from dashboard_dictionary where interface_id=(select interface_id from dashboard_data_interface where interface_name='通用报表数据')
        ${Database}.dashboard|delete from dashboard_visual_image where interface_id=(select interface_id from dashboard_data_interface where interface_name='通用报表数据')
        ${Database}.dashboard|delete from dashboard_main where dashboard_name='通用仪表盘'
        """
        action = {
            "操作": "DashboardConf",
            "参数": {
                "仪表盘配置": {
                    "仪表盘名称": "通用仪表盘",
                    "仪表盘副标题": "自动化仪表盘${yyyyMMdd}",
                    "备注": "通用仪表盘",
                    "主题样式": "四季主题",
                    "显示标题": "显示",
                    "启用轮播": "启用",
                    "轮播间隔": "5"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_dashboard_image_conf(self):
        u"""添加图像，柱状图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_柱状图",
                    "图像类型": "柱状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "分组": "等级",
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ],
                        "数据过滤": [
                            {
                                "过滤字段": "名称",
                                "自定义名称": "name",
                                "逻辑关系": "包含",
                                "过滤值": "a"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_dashboard_image_conf(self):
        u"""添加图像，柱状图，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_柱状图2",
                    "图像类型": "柱状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "分数"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "名称"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080", "#C0FF3E"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "数据展示方向": "竖向",
                        "是否显示度量": "显示",
                        "度量字体大小": "15",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "坐标轴名称字体大小": "20",
                        "坐标轴刻度标签字体大小": "17",
                        "X轴区域缩放": {
                            "状态": "开启",
                            "X轴起始百分比": "20",
                            "X轴结束百分比": "75"
                        },
                        "Y轴区域缩放": {
                            "状态": "开启",
                            "Y轴起始百分比": "30",
                            "Y轴结束百分比": "100"
                        },
                        "图像类型": "折线图",
                        "区域填充颜色": "填充"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_dashboard_image_conf(self):
        u"""添加图像，折线图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_折线图",
                    "图像类型": "折线图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "分组": "等级",
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ],
                        "数据过滤": [
                            {
                                "过滤字段": "名称",
                                "自定义名称": "name",
                                "逻辑关系": "包含",
                                "过滤值": "a"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_dashboard_image_conf(self):
        u"""添加图像，折线图，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_折线图2",
                    "图像类型": "折线图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "分数"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "名称"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080", "#C0FF3E"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "区域填充颜色": "填充",
                        "是否显示度量": "显示",
                        "度量字体大小": "15",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "坐标轴名称字体大小": "20",
                        "坐标轴刻度标签字体大小": "17",
                        "X轴区域缩放": {
                            "状态": "开启",
                            "X轴起始百分比": "20",
                            "X轴结束百分比": "75"
                        },
                        "Y轴区域缩放": {
                            "状态": "开启",
                            "Y轴起始百分比": "20",
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

    def test_15_dashboard_image_conf(self):
        u"""添加图像，饼状图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_饼状图",
                    "图像类型": "饼状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ],
                        "数据过滤": [
                            {
                                "过滤字段": "名称",
                                "自定义名称": "name",
                                "逻辑关系": "包含",
                                "过滤值": "a"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_dashboard_image_conf(self):
        u"""添加图像，饼状图，带样式配置，饼图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_饼状_饼图",
                    "图像类型": "饼状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080", "#C0FF3E"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "饼图样式": "饼图",
                        "半径": "75",
                        "是否显示图例": "显示",
                        "图例标示方向": "横向",
                        "图例对齐方式": "居中",
                        "图例字体大小": "20",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
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

    def test_17_dashboard_image_conf(self):
        u"""添加图像，饼状图，带样式配置，环形图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_饼状_环形图",
                    "图像类型": "饼状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080", "#C0FF3E"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "饼图样式": "环形图",
                        "外半径": "75",
                        "内半径": "35",
                        "是否显示图例": "显示",
                        "图例标示方向": "横向",
                        "图例对齐方式": "居中",
                        "图例字体大小": "20",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
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

    def test_18_dashboard_image_conf(self):
        u"""添加图像，饼状图，带样式配置，玫瑰图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_饼状_玫瑰图",
                    "图像类型": "饼状图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB", "#808080", "#C0FF3E"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "饼图样式": "玫瑰图",
                        "半径": "65",
                        "是否显示图例": "显示",
                        "图例标示方向": "横向",
                        "图例对齐方式": "居中",
                        "图例字体大小": "20",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
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

    def test_19_dashboard_image_conf(self):
        u"""添加图像，仪表图，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_仪表图",
                    "图像类型": "仪表图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score",
                                "度量单位": "分数"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "青春主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "上边距": "50",
                        "左边距": "50",
                        "半径": "80",
                        "开始角度": "250",
                        "角度大小": "318",
                        "低阈比例": "30",
                        "高阈比例": "85",
                        "最小值": "10",
                        "最大值": "90"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_dashboard_image_conf(self):
        u"""添加图像，数据表格"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_数据表格",
                    "图像类型": "数据表格",
                    "数据源配置": {
                        "数据列": [
                            {
                                "列选择": "名称",
                                "自定义名称": "name",
                                "自定义列颜色": "#40E0D0"
                            },
                            {
                                "列选择": "等级",
                                "自定义名称": "level",
                                "自定义列颜色": "#9370DB"
                            },
                            {
                                "列选择": "分数",
                                "自定义名称": "score",
                                "自定义列颜色": "#808080"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_dashboard_image_conf(self):
        u"""添加图像，数据表格，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_数据表格2",
                    "图像类型": "数据表格",
                    "数据源配置": {
                        "数据列": [
                            {
                                "列选择": "名称",
                                "自定义名称": "name",
                                "自定义列颜色": "#40E0D0"
                            },
                            {
                                "列选择": "等级",
                                "自定义名称": "level",
                                "自定义列颜色": "#9370DB"
                            },
                            {
                                "列选择": "分数",
                                "自定义名称": "score",
                                "自定义列颜色": "#808080"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "青春主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "每页展示条数": "50",
                        "列对齐方式": "居中",
                        "列宽度": "自适应列宽",
                        "冻结列": "name"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_dashboard_image_conf(self):
        u"""添加图像，雷达图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_雷达图",
                    "图像类型": "雷达图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "分数"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "名称"
                        },
                        "分组": "等级",
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ],
                        "数据过滤": [
                            {
                                "过滤字段": "名称",
                                "自定义名称": "name",
                                "逻辑关系": "包含",
                                "过滤值": "a"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_dashboard_image_conf(self):
        u"""添加图像，雷达图，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_雷达图2",
                    "图像类型": "雷达图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "分数"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "名称"
                        },
                        "排序": [
                            {
                                "排序字段": "分数",
                                "排序方式": "降序"
                            },
                            {
                                "排序字段": "名称",
                                "排序方式": "升序"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "青春主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示图例": "显示",
                        "图例标示方向": "横向",
                        "图例对齐方式": "居中",
                        "图例字体大小": "20",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "半径": "70",
                        "最小值": "1",
                        "最大值": "50"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_dashboard_image_conf(self):
        u"""添加图像，矩形树图"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_矩形树图",
                    "图像类型": "矩形树图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "score"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "name"
                        },
                        "分组": "等级",
                        "数据过滤": [
                            {
                                "过滤字段": "名称",
                                "自定义名称": "name",
                                "逻辑关系": "包含",
                                "过滤值": "a"
                            }
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_dashboard_image_conf(self):
        u"""添加图像，矩形树图，带样式配置"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_矩形树图2",
                    "图像类型": "矩形树图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "分数",
                                "自定义名称": "分数"
                            }
                        ],
                        "x轴": {
                            "维度": "名称",
                            "自定义名称": "名称"
                        }
                    },
                    "样式配置": {
                        "主题样式": "青春主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_dashboard_image_display(self):
        u"""仪表盘添加图像"""
        action = {
            "操作": "DashboardAddImage",
            "参数": {
                "图像列表": [
                    "auto_柱状图2",
                    "auto_折线图2",
                    "auto_饼状_饼图",
                    "auto_饼状_环形图",
                    "auto_饼状_玫瑰图",
                    "auto_仪表图",
                    "auto_数据表格2",
                    "auto_雷达图2",
                    "auto_矩形树图2"
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_business_conf(self):
        u"""配置文件节点，文件加载，新冠统计表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载定制报表数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_一级目录"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "新冠统计表",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "2",
                            "sheet页索引": "1",
                            "变量": "新冠统计",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_business_conf(self):
        u"""配置文件节点，文件加载，weather"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "文件节点",
                "节点名称": "加载定制报表数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "weather",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "1",
                            "sheet页索引": "1",
                            "变量": "天气预报",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_add(self):
        u"""画流程图，添加一个报表节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_business_conf(self):
        u"""配置报表节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点",
                "节点名称": "报表节点",
                "业务配置": {
                    "节点名称": "天气预报展示",
                    "操作方式": "添加",
                    "变量选择": "天气预报",
                    "变量索引配置": [
                        ["1", "城市", "字符", "", "分组"],
                        ["2", "日期", "字符", "", "X轴(维度)"],
                        ["3", "白天天气", "字符", "", "Y轴(度量)"],
                        ["4", "夜晚天气", "字符", "", "Y轴(度量)"],
                        ["5", "天气", "字符", "", "Y轴(度量)"],
                        ["6", "最高温度", "数字", "", "Y轴(度量)"],
                        ["7", "最低温度", "数字", "", "Y轴(度量)"],
                        ["8", "白天风向", "字符", "", "Y轴(度量)"],
                        ["9", "夜晚风向", "字符", "", "Y轴(度量)"],
                        ["10", "风速", "字符", "", "Y轴(度量)"]
                    ],
                    "数据接口名称": "天气预报",
                    "备注": "7天天气预报",
                    "样例数据": "weather_sample.txt"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_access_dashboard(self):
        u"""从报表节点进入仪表盘"""
        action = {
            "操作": "AccessReportDashboard",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点名称": "天气预报展示"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_dashboard_conf(self):
        u"""添加仪表盘"""
        pres = """
        ${Database}.dashboard|delete from dashboard_dictionary where interface_id=(select interface_id from dashboard_data_interface where interface_name='天气预报')
        ${Database}.dashboard|delete from dashboard_visual_image where interface_id=(select interface_id from dashboard_data_interface where interface_name='天气预报')
        ${Database}.dashboard|delete from dashboard_main where dashboard_name='天气预报仪表盘'
        """
        action = {
            "操作": "DashboardConf",
            "参数": {
                "仪表盘配置": {
                    "仪表盘名称": "天气预报仪表盘",
                    "仪表盘副标题": "自动化仪表盘${yyyyMMdd}",
                    "备注": "天气预报仪表盘",
                    "主题样式": "四季主题",
                    "显示标题": "显示",
                    "启用轮播": "启用",
                    "轮播间隔": "5"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_dashboard_dictionary_add(self):
        u"""添加字典"""
        action = {
            "操作": "DashboardDictAdd",
            "参数": {
                "字典配置": [
                    {
                        "字典名称": "风向字典",
                        "主题分类": "auto_报表节点流程_天气预报展示",
                        "数据接口": "天气预报",
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

    def test_35_dashboard_image_conf(self):
        u"""添加图像，天气预报"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_天气预报",
                    "图像类型": "折线图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "最高温度",
                                "自定义名称": "最高温度"
                            },
                            {
                                "度量": "最低温度",
                                "自定义名称": "最低温度"
                            }
                        ],
                        "x轴": {
                            "维度": "日期",
                            "自定义名称": "日期"
                        },
                        "分组": "城市",
                        "排序": [
                            {
                                "排序字段": "日期",
                                "排序方式": "升序"
                            }
                        ],
                        "字典转义": [
                            {
                                "转义字段": "白天风向",
                                "转义字典": "风向字典"
                            },
                            {
                                "转义字段": "夜晚风向",
                                "转义字典": "风向字典"
                            }
                        ]
                    },
                    "样式配置": {
                        "主题样式": "自定义主题",
                        "自定义主题色彩": ["#40E0D0", "#9370DB"],
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "区域填充颜色": "不填充",
                        "是否显示度量": "显示",
                        "度量字体大小": "15",
                        "是否显示标题": "显示",
                        "标题对齐方式": "居中",
                        "标题字体大小": "26",
                        "坐标轴名称字体大小": "20",
                        "坐标轴刻度标签字体大小": "17"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_dashboard_image_display(self):
        u"""仪表盘添加图像"""
        action = {
            "操作": "DashboardAddImage",
            "参数": {
                "图像列表": [
                    "auto_天气预报"
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_add(self):
        u"""画流程图，添加一个报表节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_business_conf(self):
        u"""配置报表节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "报表节点",
                "节点名称": "报表节点",
                "业务配置": {
                    "节点名称": "新冠统计展示",
                    "操作方式": "添加",
                    "变量选择": "新冠统计",
                    "变量索引配置": [
                        ["1", "省市 地区", "字符", "", "X轴(维度)"],
                        ["2", "新增 确诊", "数字", "", "Y轴(度量)"],
                        ["3", "新增 无症状", "数字", "", "Y轴(度量)"],
                        ["4", "累计 确诊", "数字", "", "Y轴(度量)"],
                        ["5", "风险 地区", "数字", "", "Y轴(度量)"]
                    ],
                    "数据接口名称": "新冠统计",
                    "备注": "新冠统计",
                    "样例数据": "COVID-19_sample.txt"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_access_dashboard(self):
        u"""从报表节点进入仪表盘"""
        action = {
            "操作": "AccessReportDashboard",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点名称": "新冠统计展示"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_dashboard_conf(self):
        u"""添加仪表盘"""
        pres = """
        ${Database}.dashboard|delete from dashboard_dictionary where interface_id=(select interface_id from dashboard_data_interface where interface_name='新冠统计')
        ${Database}.dashboard|delete from dashboard_visual_image where interface_id=(select interface_id from dashboard_data_interface where interface_name='新冠统计')
        ${Database}.dashboard|delete from dashboard_main where dashboard_name='新冠统计展示仪表盘'
        """
        action = {
            "操作": "DashboardConf",
            "参数": {
                "仪表盘配置": {
                    "仪表盘名称": "新冠统计展示仪表盘",
                    "仪表盘副标题": "新冠统计展示仪表盘${yyyyMMdd}",
                    "备注": "新冠统计展示仪表盘",
                    "主题样式": "默认主题",
                    "显示标题": "显示",
                    "启用轮播": "启用",
                    "轮播间隔": "10"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_dashboard_dictionary_add(self):
        u"""添加字典"""
        action = {
            "操作": "DashboardDictAdd",
            "参数": {
                "字典配置": [
                    {
                        "字典名称": "新冠统计字典1",
                        "主题分类": "auto_报表节点流程_新冠统计展示",
                        "数据接口": "新冠统计",
                        "字典项": "map1.txt"
                    },
                    {
                        "字典名称": "新冠统计字典2",
                        "主题分类": "auto_报表节点流程_新冠统计展示",
                        "数据接口": "新冠统计",
                        "字典项": "map2.txt"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_dashboard_image_conf(self):
        u"""添加图像，地图，新冠累计确诊"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_地图_累计确诊",
                    "图像类型": "地图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "累计 确诊",
                                "自定义名称": "累计 确诊"
                            }
                        ],
                        "区域": {
                            "地区": "全国",
                            "钻取": "启用",
                            "省份字段": "省市 地区",
                            "城市字段": "省市 地区"
                        }
                    },
                    "样式配置": {
                        "主题样式": "默认主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "显示地区名称": "是",
                        "显示颜色条": "是",
                        "最小值": "1",
                        "最大值": "10000"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_dashboard_image_conf(self):
        u"""添加图像，地图，新冠新增确诊"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_地图_新增确诊",
                    "图像类型": "地图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "新增 确诊",
                                "自定义名称": "新增 确诊"
                            }
                        ],
                        "区域": {
                            "地区": "全国",
                            "钻取": "启用",
                            "省份字段": "省市 地区",
                            "城市字段": "省市 地区"
                        }
                    },
                    "样式配置": {
                        "主题样式": "默认主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "显示地区名称": "是",
                        "显示颜色条": "是",
                        "最小值": "1",
                        "最大值": "1000"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_dashboard_image_conf(self):
        u"""添加图像，地图，新冠新增无症状"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_地图_新增无症状",
                    "图像类型": "地图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "新增 无症状",
                                "自定义名称": "新增 无症状"
                            }
                        ],
                        "区域": {
                            "地区": "全国",
                            "钻取": "启用",
                            "省份字段": "省市 地区",
                            "城市字段": "省市 地区"
                        }
                    },
                    "样式配置": {
                        "主题样式": "默认主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "显示地区名称": "是",
                        "显示颜色条": "是",
                        "最小值": "1",
                        "最大值": "500"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_dashboard_image_conf(self):
        u"""添加图像，地图，新冠风险 地区"""
        action = {
            "操作": "DashboardImageConf",
            "参数": {
                "图像配置": {
                    "图像名称": "auto_地图_风险地区",
                    "图像类型": "地图",
                    "数据源配置": {
                        "y轴": [
                            {
                                "度量": "风险 地区",
                                "自定义名称": "风险 地区"
                            }
                        ],
                        "区域": {
                            "地区": "全国",
                            "钻取": "启用",
                            "省份字段": "省市 地区",
                            "城市字段": "省市 地区"
                        }
                    },
                    "样式配置": {
                        "主题样式": "默认主题",
                        "自定义背景颜色": "是",
                        "背景颜色": "#FFDEAD",
                        "是否显示标题": "显示",
                        "标题对齐方式": "右对齐",
                        "标题字体大小": "26",
                        "显示地区名称": "是",
                        "显示颜色条": "是",
                        "最小值": "1",
                        "最大值": "50"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_46_dashboard_image_display(self):
        u"""仪表盘添加图像"""
        action = {
            "操作": "DashboardAddImage",
            "参数": {
                "图像列表": [
                    "auto_地图_新增确诊",
                    "auto_地图_新增无症状",
                    "auto_地图_累计确诊",
                    "auto_地图_风险地区"
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_47_process_node_line(self):
        u"""开始节点连线到节点：报表数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "开始",
                "终止节点名称": "报表数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点报表数据连线到节点：通用报表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "报表数据",
                "终止节点名称": "通用报表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_49_process_node_line(self):
        u"""节点通用报表连线到节点：加载定制报表数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "通用报表",
                "终止节点名称": "加载定制报表数据",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_process_node_line(self):
        u"""节点加载定制报表数据连线到节点：天气预报展示"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "加载定制报表数据",
                "终止节点名称": "天气预报展示",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点天气预报展示连线到节点：新冠统计展示"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "天气预报展示",
                "终止节点名称": "新冠统计展示",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_52_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_53_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_54_process_node_line(self):
        u"""节点新冠统计展示连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_报表节点流程",
                "起始节点名称": "新冠统计展示",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
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
