# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class SqlNode(unittest.TestCase):

    log.info("装载流程数据库节点配置模式测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试sql节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_数据库配置模式",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_数据库配置模式说明",
                "高级配置": {
                    "节点异常终止流程": "否"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_node_opt_conf(self):
        u"""通用节点，添加一个自定义变量，内置变量，时间变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
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
                                    ["变量", {
                                        "变量名称": "时间变量",
                                        "时间格式": "yyyy-MM-dd HH:mm:ss",
                                        "间隔": "0",
                                        "单位": "日",
                                        "语言": "中文"
                                    }]
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置sql节点，删除历史数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "删除历史数据",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${OtherInfoTableName}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载测试数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载入库数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_一级目录",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "data",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "2",
                            "变量": "加载数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置sql节点，普通模式，数据插入内部库，网元其它资料"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "数据插入网元其它资料",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "加载数据",
                        "数据库": "AiSee",
                        "存储模式": "",
                        "表选择": "auto_网元其它资料",
                        "字段映射": {
                            "列1": {
                                "值类型": "索引",
                                "字段值": "1"
                            },
                            "列2": {
                                "值类型": "索引",
                                "字段值": "2"
                            },
                            "列3": {
                                "值类型": "索引",
                                "字段值": "3"
                            },
                            "列4": {
                                "值类型": "自定义值",
                                "字段值": "美好的一天"
                            },
                            "列5": {
                                "值类型": "变量名",
                                "字段值": "当前时间"
                            }
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置sql节点，查询语句"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "查询内部库",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${OtherInfoTableName}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置sql节点，普通模式，数据插入内部库，数据拼盘数据模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "数据插入数据拼盘",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "加载数据",
                        "数据库": "AiSee",
                        "存储模式": "",
                        "表选择": "auto_数据模式",
                        "字段映射": {
                            "列1": {
                                "值类型": "索引",
                                "字段值": "1"
                            },
                            "列2": {
                                "值类型": "索引",
                                "字段值": "2"
                            },
                            "列3": {
                                "值类型": "索引",
                                "字段值": "3"
                            },
                            "列4": {
                                "值类型": "索引",
                                "字段值": "4"
                            },
                            "列5": {
                                "值类型": "索引",
                                "字段值": "5"
                            }
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_node_fetch_conf(self):
        u"""节点添加取数配置，不含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_不含列名",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_fetch_conf(self):
        u"""节点添加取数配置，含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_含列名",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_fetch_conf(self):
        u"""节点添加取数配置，取部分列"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_取部分列",
                    "赋值方式": "替换",
                    "输出列": "1,2,3",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载测试数据：大数据1w_正常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载大数据入库数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_一级目录",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "大数据1w_正常",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "1",
                            "分隔符": ",",
                            "变量": "大数据1w_正常",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载测试数据：大数据1w_异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "文件节点",
                "节点名称": "加载大数据入库数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "大数据1w_异常",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "1",
                            "分隔符": ",",
                            "变量": "大数据1w_异常",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置sql节点，删除历史数据，pg数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "postgres外部表数据清理",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_postgres数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${BigImportTable}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置sql节点，删除历史数据，oracle数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "oracle外部表数据清理",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oracle数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${BigImportTable}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""配置sql节点，删除历史数据，mysql数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "mysql外部表数据清理",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_mysql数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${BigImportTable}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_business_conf(self):
        u"""配置sql节点，配置模式，导入外部pg数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部pg数据库",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_正常",
                        "数据库": "auto_postgres数据库",
                        "存储模式": "",
                        "表选择": "auto_大数据表_postgres",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_business_conf(self):
        u"""配置sql节点，配置模式，导入外部oracle数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部oracle数据库",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_正常",
                        "数据库": "auto_oracle数据库",
                        "存储模式": "",
                        "表选择": "auto_大数据表_oracle",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_process_node_business_conf(self):
        u"""配置sql节点，配置模式，导入外部mysql数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_正常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "表选择": "auto_大数据表_mysql",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_node_business_conf(self):
        u"""配置sql节点，配置模式，批量提交行数为空，数据存在异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "批量提交行数为空存在异常",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_异常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_大数据表_mysql",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_node_business_conf(self):
        u"""配置sql节点，配置模式，批量提交行数不为空，数据都正常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "批量提交行数不为空且全部成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_正常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_大数据表_mysql",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_process_node_business_conf(self):
        u"""配置sql节点，配置模式，pg数据库，批量提交行数不为空，数据有异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部pg数据库部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_异常",
                        "数据库": "auto_postgres数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_大数据表_postgres",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_process_node_business_conf(self):
        u"""配置sql节点，配置模式，oracle数据库，批量提交行数不为空，数据有异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部oracle数据库部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_异常",
                        "数据库": "auto_oracle数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_大数据表_oracle",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_business_conf(self):
        u"""配置sql节点，配置模式，mysql数据库，批量提交行数不为空，数据有异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_异常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_大数据表_mysql",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_business_conf(self):
        u"""配置sql节点，配置模式，跳过行数不为空"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库跳过部分行",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据1w_正常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "跳过行数": "3",
                            "批量提交行数": "",
                        },
                        "表选择": "auto_大数据表_mysql",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = gbl.service.get("browser")
        saveScreenShot()
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
