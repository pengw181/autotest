# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/5 下午9:25

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class HandleNode(unittest.TestCase):

    log.info("装载流程数据处理节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_数据处理节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试数据处理节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_数据处理节点流程说明",
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
                "流程名称": "auto_数据处理节点流程",
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
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "参数设置",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，变量a"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
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
                                    ["自定义值", ["java,v1,100", "python,v1,200", "jar,v1,150"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "变量a"
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_opt_conf(self):
        u"""操作配置，添加操作，正则运算，得到二维数组"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "通用节点",
                "节点名称": "参数设置",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "变量a",
                                "输出变量": "变量a",
                                "赋值方式": "替换",
                                "数组索引": "",
                                "是否转置": "否",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "否",
                                    "列总数": "3",
                                    "拆分方式": "文本",
                                    "拆分符": ",",
                                    "样例数据": ["java,v1,100", "python,v1,200", "jar,v1,150"]
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

    def test_7_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，变量b"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
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
                                    ["自定义值", ["java,v1,100,a1", "python,v1,200,a2", "jar,v1,150,a3", "c,v1,150,a4"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "变量b"
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_opt_conf(self):
        u"""操作配置，添加操作，正则运算，得到二维数组"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "通用节点",
                "节点名称": "参数设置",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "变量b",
                                "输出变量": "变量b",
                                "赋值方式": "替换",
                                "数组索引": "",
                                "是否转置": "否",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "否",
                                    "列总数": "4",
                                    "拆分方式": "文本",
                                    "拆分符": ",",
                                    "样例数据": ["java,v1,100,a1", "python,v1,200,a2", "jar,v1,150,a3", "c,v1,150,a4"]
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

    def test_9_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个一维数组，变量c"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
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
                                    ["自定义值", "java"],
                                    ["并集", ""],
                                    ["自定义值", "python"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "变量c"
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_add(self):
        u"""画流程图，添加一个数据处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置数据处理节点，数据比对模式，取关联结果"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点",
                "节点名称": "数据处理节点",
                "业务配置": {
                    "节点名称": "数据比对,取关联结果",
                    "处理模式": "数据比对",
                    "变量1": "变量a",
                    "变量2": "变量b",
                    "关联列": [
                        ["1", "1"]
                    ],
                    "基准变量": "变量1",
                    "输出类型": "关联结果",
                    "输出变量名称": "数据比对-关联结果",
                    "输出列": "*",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个数据处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置数据处理节点，数据比对模式，取未关联结果"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点",
                "节点名称": "数据处理节点",
                "业务配置": {
                    "节点名称": "数据比对,取非关联结果",
                    "处理模式": "数据比对",
                    "变量1": "变量a",
                    "变量2": "变量b",
                    "关联列": [
                        ["1", "1"]
                    ],
                    "基准变量": "变量1",
                    "输出类型": "未关联结果",
                    "输出变量名称": "数据比对-未关联结果",
                    "输出列": "*",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_add(self):
        u"""画流程图，添加一个数据处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置数据处理节点，数据比对模式，二维表与一维表比对，取关联结果"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点",
                "节点名称": "数据处理节点",
                "业务配置": {
                    "节点名称": "二维表与一维表比对,取关联结果",
                    "处理模式": "数据比对",
                    "变量1": "变量a",
                    "变量2": "变量c",
                    "关联列": [
                        ["1", "1"]
                    ],
                    "基准变量": "变量1",
                    "输出类型": "关联结果",
                    "输出变量名称": "二维表与一维表比对-关联结果",
                    "输出列": "*",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_add(self):
        u"""画流程图，添加一个数据处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置数据处理节点，数据更新模式，更新已存在列"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点",
                "节点名称": "数据处理节点",
                "业务配置": {
                    "节点名称": "数据更新,更新已存在列",
                    "处理模式": "数据更新",
                    "变量1": "变量a",
                    "变量2": "变量b",
                    "关联列": [
                        ["1", "1"],
                        ["2", "2"]
                    ],
                    "更新列": [
                        ["3", "4"]
                    ],
                    "基准变量": "变量1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_add(self):
        u"""画流程图，添加一个数据处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置数据处理节点，数据更新模式，更新不存在列"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "数据处理节点",
                "节点名称": "数据处理节点",
                "业务配置": {
                    "节点名称": "数据更新,更新不存在列",
                    "处理模式": "数据更新",
                    "变量1": "变量a",
                    "变量2": "变量b",
                    "关联列": [
                        ["1", "1"],
                        ["2", "2"]
                    ],
                    "更新列": [
                        ["4", "4"],
                        ["6", "3"]
                    ],
                    "基准变量": "变量1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_line(self):
        u"""节点参数设置连线到节点：数据比对,取关联结果"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "数据比对,取关联结果",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_line(self):
        u"""节点数据比对,取关联结果连线到节点：数据比对,取非关联结果"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "数据比对,取关联结果",
                "终止节点名称": "数据比对,取非关联结果",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_line(self):
        u"""节点数据比对,取非关联结果连线到节点：二维表与一维表比对,取关联结果"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "数据比对,取非关联结果",
                "终止节点名称": "二维表与一维表比对,取关联结果",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_line(self):
        u"""节点二维表与一维表比对,取关联结果连线到节点：数据更新,更新已存在列"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "二维表与一维表比对,取关联结果",
                "终止节点名称": "数据更新,更新已存在列",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_line(self):
        u"""节点数据更新,更新已存在列连线到节点：数据更新,更新不存在列"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "数据更新,更新已存在列",
                "终止节点名称": "数据更新,更新不存在列",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_line(self):
        u"""节点数据更新,更新不存在列连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据处理节点流程",
                "起始节点名称": "数据更新,更新不存在列",
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
