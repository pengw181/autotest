# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/11 下午12:58

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CommonNodePart2(unittest.TestCase):

    log.info("装载流程通用节点配置测试用例（2）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_2_process_update(self):
        u"""修改流程，修改流程定义变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "开启",
                            "参数列表": {
                                "时间": "2020-10-21###",
                                "地点": "广州###",
                                "名字": "aisee###必填"
                            }
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
                "流程名称": "auto_通用节点流程",
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
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "条件和循环",
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
        u"""操作配置，添加条件"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加条件",
                        "条件配置": {
                            "if": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "else": "是"
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
        u"""操作配置，添加循环，按变量列表，自定义模式"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加循环",
                        "循环配置": {
                            "循环类型": "变量列表",
                            "变量选择": "名字",
                            "模式": "自定义模式",
                            "循环行变量名称": "loop_a",
                            "赋值方式": "替换"
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
        u"""操作配置，添加循环，按次数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "else",
                        "右键操作": "添加循环",
                        "循环配置": {
                            "循环类型": "次数",
                            "循环次数": "3",
                            "循环变量名称": "ki",
                            "赋值方式": "追加",
                            "跳至下一轮条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "结束循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ]
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
        u"""操作配置，添加循环，按条件"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "列表循环",
                        "右键操作": "添加循环",
                        "循环配置": {
                            "循环类型": "条件",
                            "循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "跳至下一轮条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "结束循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ]
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
        u"""操作配置，添加操作，基础运算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "表达式": [
                                    ["变量", "时间"],
                                    ["并集", ""],
                                    ["变量", "地点"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_10_process_node_opt_conf(self):
        u"""操作配置，基础运算，勾选转置"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件和循环",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "表达式": [
                                    ["变量", "时间"],
                                    ["并集", ""],
                                    ["变量", "地点"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算转置结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "是",
                                "批量修改所有相同的变量名": "否"
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

    def test_11_process_node_opt_conf(self):
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

    def test_12_process_node_opt_conf(self):
        u"""操作配置，删除"""
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

    def test_13_process_node_add(self):
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

    def test_14_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "运算",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_opt_conf(self):
        u"""操作配置，添加操作，正则运算，正则拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "时间",
                                "输出变量": "正则运算结果-正则拆分",
                                "赋值方式": "替换",
                                "数组索引": "2,3,5",
                                "是否转置": "否",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "否",
                                    "列总数": "4",
                                    "拆分方式": "正则",
                                    "正则配置": {
                                        "设置方式": "选择",
                                        "正则模版名称": "auto_正则模版_匹配逗号"
                                    },
                                    "样例数据": ["a1,1,2,3", "a2,1,2,3", "a3,1,2,3", "a4,1,2,3", "a5,1,2,3"]
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

    def test_16_process_node_opt_conf(self):
        u"""操作配置，添加操作，正则运算，正则匹配数据列"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "时间",
                                "输出变量": "正则运算结果-正则匹配数据列",
                                "赋值方式": "替换",
                                "数组索引": "2,3,5",
                                "是否转置": "否",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "是",
                                    "正则配置": {
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
                                            },
                                            {
                                                "标签": "自定义文本",
                                                "自定义值": "test",
                                                "是否取值": "无"
                                            }
                                        ]
                                    },
                                    "样例数据": ["pw 001 test", "pw 002 test", "pw 003 test", "pw 004 test", "pw 005 test"]
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

    def test_17_process_node_opt_conf(self):
        u"""操作配置，添加操作，过滤运算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "过滤运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "名字",
                                "过滤条件": [
                                    ["变量索引", "1"],
                                    ["包含", ""],
                                    ["变量", "时间"],
                                    ["或", ""],
                                    ["变量", "名字"],
                                    ["开头", ""],
                                    ["自定义值", ["张三"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "过滤运算结果"
                                },
                                "输出列": "1,2,4,3",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_18_process_node_add(self):
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

    def test_19_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "聚合运算",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，总计"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["总计(sum)", "1"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算总计结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_21_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，计数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["计数(count)", "1"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算计数结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_22_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，最大值"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["最大值(max)", "1"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算最大值结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_23_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，最小值"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["最小值(min)", "2"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算最小值结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_24_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，平均值"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["平均值(avg)", "3"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算平均值结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_25_process_node_opt_conf(self):
        u"""操作配置，添加操作，聚合运算，分组连接"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "聚合运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "时间",
                                "分组依据": "1",
                                "表达式": [
                                    ["分组连接", "2,&"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "聚合运算分组连接结果"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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

    def test_26_process_node_opt_conf(self):
        u"""操作配置，添加操作，网络地址运算，子网掩码方式"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "网络地址运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "输入方式": "子网掩码",
                                "输入地址": "255.255.0.0",
                                "TCP/IP地址": "192.168.88.123",
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "网络地址运算结果-子网掩码输入方式"
                                },
                                "赋值方式": "替换"
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

    def test_27_process_node_opt_conf(self):
        u"""操作配置，添加操作，网络地址运算，位元数方式"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "网络地址运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "输入方式": "位元数",
                                "输入地址": "11",
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "网络地址运算结果-位元数方式"
                                },
                                "赋值方式": "替换"
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

    def test_28_process_node_opt_conf(self):
        u"""操作配置，添加操作，分段拆分运算，只配置开始特征行"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "分段拆分运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "变量名称": "分段拆分运算结果-开始特征行",
                                "输入变量": "地点",
                                "赋值方式": "追加",
                                "开始特征行": {
                                    "状态": "开启",
                                    "设置方式": "选择",
                                    "正则模版名称": "auto_正则模版_匹配日期"
                                },
                                "样例数据": ["2020-11-15 12:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤", "2020-11-15 13:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤"]
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

    def test_29_process_node_opt_conf(self):
        u"""操作配置，添加操作，分段拆分运算，只配置结束特征行"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "分段拆分运算",
                            "配置": {
                                "变量名称": "分段拆分运算结果-结束特征行",
                                "输入变量": "地点",
                                "赋值方式": "追加",
                                "结束特征行": {
                                    "状态": "开启",
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
                                        },
                                        {
                                            "标签": "自定义文本",
                                            "自定义值": "test",
                                            "是否取值": "无"
                                        }
                                    ]
                                },
                                "样例数据": ["pw 001 test", "pw 002 test", "pw 003 test", "pw 004 test", "pw 005 test"]
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

    def test_30_process_node_opt_conf(self):
        u"""操作配置，添加操作，分段拆分运算，同时配置开始特征行和结束特征行"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "分段拆分运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "变量名称": "分段拆分运算结果-开始结束特征行",
                                "输入变量": "地点",
                                "赋值方式": "追加",
                                "开始特征行": {
                                    "状态": "开启",
                                    "设置方式": "选择",
                                    "正则模版名称": "auto_正则模版_匹配日期"
                                },
                                "结束特征行": {
                                    "状态": "开启",
                                    "设置方式": "添加",
                                    "正则模版名称": "auto_正则模版",
                                    "标签配置": [
                                        {
                                            "标签": "自定义文本",
                                            "自定义值": "END",
                                            "是否取值": "无"
                                        }
                                    ]
                                },
                                "样例数据": ["2020-11-15 12:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤 END", "2020-11-15 13:30:00 据央视新闻11月16日报道，当地时间14日，美国首都华盛顿爆发大规模抗议游行集会，持不同观点的抗议者之间多次出现对峙和冲突。截至15日凌晨，集会和冲突仍在持续。据华盛顿警方发布的消息，14日的集会和冲突已导致21人被逮捕，另有两名警察受伤 END"]
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

    def test_31_process_node_opt_conf(self):
        u"""操作配置，添加操作，排序运算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "排序运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "选择变量": "地点",
                                "排序配置": [
                                    {
                                        "操作": "添加",
                                        "列索引": "1",
                                        "排序方式": "升序"
                                    },
                                    {
                                        "操作": "添加",
                                        "列索引": "2",
                                        "排序方式": "降序"
                                    },
                                    {
                                        "操作": "添加",
                                        "列索引": "4",
                                        "排序方式": "升序"
                                    },
                                    {
                                        "操作": "修改",
                                        "已排序索引": "4",
                                        "列索引": "3",
                                        "排序方式": "降序"
                                    },
                                    {
                                        "操作": "删除",
                                        "已排序索引": "3"
                                    }
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "排序运算结果"
                                },
                                "输出列": "*",
                                "赋值方式": "追加"
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

    def test_32_process_node_opt_conf(self):
        u"""操作配置，添加操作，清洗筛选运算，按时间筛选"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "清洗筛选运算",
                            "条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "地点"],
                                ["包含", ""],
                                ["自定义值", ["abc ddd"]]
                            ],
                            "配置": {
                                "变量名称": "清洗筛选运算结果-按时间筛选",
                                "输入变量": "时间",
                                "赋值方式": "替换",
                                "筛选方向": "正向",
                                "按时间筛选": {
                                    "状态": "开启",
                                    "时间格式": "yyyy-MM-dd",
                                    "间隔": "-1",
                                    "单位": "日",
                                    "语言": "中文"
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

    def test_33_process_node_opt_conf(self):
        u"""操作配置，添加操作，清洗筛选运算，按关键字/变量筛选"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "清洗筛选运算",
                            "配置": {
                                "变量名称": "清洗筛选运算结果-按关键字/变量筛选",
                                "输入变量": "时间",
                                "赋值方式": "替换",
                                "筛选方向": "反向",
                                "按关键字/变量筛选": {
                                    "状态": "开启",
                                    "筛选配置": [
                                        {
                                            "类型": "变量",
                                            "值": "时间"
                                        },
                                        {
                                            "类型": "关键字",
                                            "值": {
                                                "设置方式": "选择",
                                                "正则模版名称": "auto_正则模版_匹配日期"
                                            }
                                        },
                                        {
                                            "类型": "关键字",
                                            "值": {
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
                                                    },
                                                    {
                                                        "标签": "自定义文本",
                                                        "自定义值": "test",
                                                        "是否取值": "无"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
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

    def test_34_process_node_opt_conf(self):
        u"""操作配置，添加操作，清洗筛选运算，同时按时间筛选和按关键字/变量筛选"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "清洗筛选运算",
                            "配置": {
                                "变量名称": "清洗筛选运算结果-同时筛选",
                                "输入变量": "时间",
                                "赋值方式": "替换",
                                "筛选方向": "正向",
                                "按时间筛选": {
                                    "状态": "开启",
                                    "时间格式": "yyyy-MM-dd",
                                    "间隔": "-1",
                                    "单位": "日",
                                    "语言": "中文"
                                },
                                "按关键字/变量筛选": {
                                    "状态": "开启",
                                    "筛选配置": [
                                        {
                                            "类型": "变量",
                                            "值": "时间"
                                        },
                                        {
                                            "类型": "关键字",
                                            "值": {
                                                "设置方式": "选择",
                                                "正则模版名称": "auto_正则模版_匹配日期"
                                            }
                                        },
                                        {
                                            "类型": "关键字",
                                            "值": {
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
                                                    },
                                                    {
                                                        "标签": "自定义文本",
                                                        "自定义值": "test",
                                                        "是否取值": "无"
                                                    }
                                                ]
                                            }
                                        }
                                    ]
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

    def test_35_process_node_opt_conf(self):
        u"""操作配置，添加操作，动作，休眠"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "动作",
                            "配置": {
                                "表达式": [
                                    ["休眠", "3"]
                                ]
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

    def test_36_process_node_opt_conf(self):
        u"""操作配置，添加操作，动作，置空"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "运算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "动作",
                            "配置": {
                                "表达式": [
                                    ["置空", "时间"]
                                ]
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

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
