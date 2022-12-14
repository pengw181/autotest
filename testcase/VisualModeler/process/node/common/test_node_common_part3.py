# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/11 下午12:58

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CommonNodePart3(unittest.TestCase):

    log.info("装载流程通用节点配置测试用例（3）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_37_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "子流程",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_opt_conf(self):
        u"""操作配置，添加子流程"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "子流程",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "条件": [
                            ["变量", "时间"],
                            ["不等于", ""],
                            ["空值", ""],
                            ["与", ""],
                            ["变量", "地点"],
                            ["包含", ""],
                            ["自定义值", ["abc ddd"]]
                        ],
                        "操作类型": "添加子流程",
                        "子流程配置": {
                            "流程名称":  "auto_子流程",
                            "专业领域":  ["AiSee", "auto域"],
                            "流程类型":  "子流程",
                            "流程说明":  "auto_子流程说明",
                            "节点异常终止流程": "是"
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

    def test_40_process_node_opt_conf(self):
        u"""操作配置，绑定子流程"""
        pres = """
        ${Database}.main|update tn_process_conf_info set create_time=to_timestamp('2021-10-01 10:00:00', 'yyyy-MM-dd hh24:mi:ss') where process_name='auto_子流程'||continue
        ${Database}.main|update tn_process_conf_info set create_time=date_format('2021-10-01 10:00:00', '%Y-%m-%d %H:%i:%s') where process_name='auto_子流程'||continue
        """
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "子流程",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "条件": [
                            ["变量", "时间"],
                            ["不等于", ""],
                            ["空值", ""],
                            ["与", ""],
                            ["变量", "地点"],
                            ["包含", ""],
                            ["自定义值", ["abc ddd"]]
                        ],
                        "操作类型": "绑定子流程",
                        "子流程配置": {
                            "子流程名称": "auto_子流程",
                            "创建开始时间": "2021-10-01",
                            "创建结束时间": "2021-10-02"
                        }
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_opt_conf(self):
        u"""操作配置，复制"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "普通运算结果",
                        "右键操作": "复制"
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_process_node_opt_conf(self):
        u"""操作配置，删除变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "普通运算结果",
                        "右键操作": "删除"
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_process_node_opt_conf(self):
        u"""操作配置，删除循环"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "条件循环",
                        "右键操作": "删除"
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_process_node_opt_conf(self):
        u"""操作配置，删除条件else"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "else",
                        "右键操作": "删除"
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_process_node_opt_conf(self):
        u"""操作配置，删除条件if"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "if",
                        "右键操作": "删除"
                    }
                ]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_46_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_47_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "函数",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_48_process_node_opt_conf(self):
        u"""操作配置，添加函数，取绝对值"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "取绝对值"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-取绝对值"
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

    def test_49_process_node_opt_conf(self):
        u"""操作配置，添加函数，数组转字符串"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "数组转字符串",
                                                "分隔符": ","
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-数组转字符串"
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

    def test_50_process_node_opt_conf(self):
        u"""操作配置，添加函数，时间处理"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "时间处理",
                                                "时间格式": "yyyyMMddHHmmss",
                                                "间隔": "-1",
                                                "单位": "日",
                                                "语言": "中文"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-时间处理"
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

    def test_51_process_node_opt_conf(self):
        u"""操作配置，添加函数，10进制转16进制"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "10进制转16进制"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-10进制转16进制"
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

    def test_52_process_node_opt_conf(self):
        u"""操作配置，添加函数，去重"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "去重"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-去重"
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

    def test_53_process_node_opt_conf(self):
        u"""操作配置，添加函数，科学计数法转普通数字"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "科学计数法转普通数字"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-科学计数法转普通数字"
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

    def test_54_process_node_opt_conf(self):
        u"""操作配置，添加函数，获取网元属性"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "获取网元属性",
                                                "网元列": "1"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-获取网元属性"
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

    def test_55_process_node_opt_conf(self):
        u"""操作配置，添加函数，16进制转10进制"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "16进制转10进制"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-16进制转10进制"
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

    def test_56_process_node_opt_conf(self):
        u"""操作配置，添加函数，数组格式化"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "数组格式化"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-数组格式化"
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

    def test_57_process_node_opt_conf(self):
        u"""操作配置，添加函数，长度"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "长度"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-长度"
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

    def test_58_process_node_opt_conf(self):
        u"""操作配置，添加函数，科学计算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "科学计算"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-科学计算"
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

    def test_59_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符替换"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符替换",
                                                "正则匹配": "否",
                                                "查找内容": "aaabbc",
                                                "替换": "nice",
                                                "方式": "替换所有"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符替换"
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

    def test_60_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符替换，使用正则匹配"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符替换",
                                                "正则匹配": "是",
                                                "查找内容": {
                                                    "设置方式": "添加",
                                                    "正则模版名称": "auto_正则模版",
                                                    "标签配置": [
                                                        {
                                                            "标签": "自定义文本",
                                                            "自定义值": "pw",
                                                            "是否取值": "黄色"
                                                        },
                                                        {
                                                            "标签": "任意字符",
                                                            "长度": "1到多个",
                                                            "是否取值": "绿色"
                                                        }
                                                    ]
                                                },
                                                "替换": "nice",
                                                "方式": "替换所有"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符替换-使用正则"
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

    def test_61_process_node_opt_conf(self):
        u"""操作配置，添加函数，取小数位数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "取小数位数",
                                                "小数位数": "2",
                                                "使用千分位分隔符": "是"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-取小数位数"
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

    def test_62_process_node_opt_conf(self):
        u"""操作配置，添加函数，文本拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "拆分",
                                                "拆分方式": "文本",
                                                "分隔符": ","
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-文本拆分"
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

    def test_63_process_node_opt_conf(self):
        u"""操作配置，添加函数，正则拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "拆分",
                                                "拆分方式": "正则",
                                                "分隔符": {
                                                    "设置方式": "添加",
                                                    "正则模版名称": "auto_正则模版",
                                                    "标签配置": [
                                                        {
                                                            "标签": "自定义文本",
                                                            "自定义值": "pw",
                                                            "是否取值": "黄色"
                                                        },
                                                        {
                                                            "标签": "任意字符",
                                                            "长度": "1到多个",
                                                            "是否取值": "绿色"
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-正则拆分"
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

    def test_64_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符串转数字"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符串转数字"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符串转数字"
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

    def test_65_process_node_opt_conf(self):
        u"""操作配置，添加函数，科学计算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "科学计算"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-科学计算"
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

    def test_66_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符串截取"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符串截取",
                                                "开始": "1",
                                                "结束": "5"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符串截取"
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

    def test_67_process_node_opt_conf(self):
        u"""操作配置，添加函数，转置"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "转置"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-转置"
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

    def test_68_process_node_opt_conf(self):
        u"""操作配置，添加函数，去空格"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "函数",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "去空格"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-去空格"
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

    def test_69_process_node_line(self):
        u"""开始节点连线到：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
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

    def test_70_process_node_line(self):
        u"""参数设置连线到：条件依赖"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "条件依赖",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_71_process_node_line(self):
        u"""节点条件依赖连线到：条件和循环"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "条件依赖",
                "终止节点名称": "条件和循环",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_72_process_node_line(self):
        u"""节点条件和循环连线到：运算"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "条件和循环",
                "终止节点名称": "运算",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_73_process_node_line(self):
        u"""节点运算连线到：聚合运算"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "运算",
                "终止节点名称": "聚合运算",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_74_process_node_line(self):
        u"""节点聚合运算连线到：子流程"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "聚合运算",
                "终止节点名称": "子流程",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_75_process_node_line(self):
        u"""节点子流程连线到：函数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "子流程",
                "终止节点名称": "函数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_76_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_77_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_77_process_node_line(self):
        u"""节点函数连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "起始节点名称": "函数",
                "终止节点名称": "正常",
                "关联关系": "满足"
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
