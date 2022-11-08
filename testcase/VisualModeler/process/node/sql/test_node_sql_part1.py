# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class SqlNodePart1(unittest.TestCase):

    log.info("装载流程sql节点配置测试用例（1）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_sql节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试sql节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_sql节点流程",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_sql节点流程说明",
                "高级配置": {
                    "节点异常终止流程": "否",
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
                "流程名称": "auto_sql节点流程",
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
                "流程名称": "auto_sql节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，内置变量，时间变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置sql节点，删除历史数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "删除历史数据",
                    "操作模式": "sql节点高级模式",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载测试数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置sql节点，普通模式，数据插入内部库，网元其它资料"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "普通模式数据插入网元其它资料",
                    "操作模式": "sql节点普通模式",
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
                                "字段值": "名字"
                            }
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置sql节点，查询语句"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "查询内部库",
                    "操作模式": "sql节点高级模式",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置sql节点，insert网元其它资料表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "insert网元其它资料表",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [{
                            "类型": "自定义值",
                            "自定义值": "insert into ${OtherInfoTableName} (pk, user_id, is_delete, update_date, belong_id, domain_id, col_2, col_3, col_4, col_5, col_6, aisee_batch_tag) values(uuid(), 'pw', 0, now(), '440100', 'AiSeeCore', '张三', '张三', '张三', '张三', '张三', '0')"
                        }]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置sql节点，insert外部库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "数据插入到外部数据库",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "auto_mysql数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "insert into pw_test_data values(1, 'zhangsan', 200, 5000, "
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "'"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "自定义变量",
                                "变量名": "当前时间"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "')"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置sql节点，select外部库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "查询外部数据库",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "auto_mysql数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from pw_test_data"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置sql节点，普通模式，数据插入内部库，数据拼盘数据模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "普通模式数据插入数据拼盘",
                    "操作模式": "sql节点普通模式",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置sql节点，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "查询内部库",
                "业务配置": {
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置sql节点，关闭高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "查询内部库",
                "业务配置": {
                    "高级配置": {
                        "状态": "关闭"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "查询结果",
                    "变量名": "查询结果1",
                    "赋值方式": "替换",
                    "输出列": "1,2,3",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "查询结果1"
                }
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_fetch_conf(self):
        u"""节点添加取数配置，不含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_fetch_conf(self):
        u"""节点添加取数配置，含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_fetch_conf(self):
        u"""节点添加取数配置，取部分列"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
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

    def test_31_process_node_line(self):
        u"""节点参数设置连线到节点：删除历史数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "删除历史数据",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_line(self):
        u"""节点删除历史数据连线到节点：加载入库数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "删除历史数据",
                "终止节点名称": "加载入库数据",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_process_node_line(self):
        u"""节点加载入库数据连线到节点：普通模式数据插入网元其它资料"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "加载入库数据",
                "终止节点名称": "普通模式数据插入网元其它资料",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_process_node_line(self):
        u"""节点普通模式数据插入网元其它资料连线到节点：查询内部库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "普通模式数据插入网元其它资料",
                "终止节点名称": "查询内部库",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_line(self):
        u"""节点查询内部库连线到节点：insert网元其它资料表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "查询内部库",
                "终止节点名称": "insert网元其它资料表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_line(self):
        u"""节点insert网元其它资料表连线到节点：数据插入到外部数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "insert网元其它资料表",
                "终止节点名称": "数据插入到外部数据库",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_line(self):
        u"""节点数据插入到外部数据库连线到节点：查询外部数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "数据插入到外部数据库",
                "终止节点名称": "查询外部数据库",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_line(self):
        u"""节点查询外部数据库连线到节点：普通模式数据插入数据拼盘"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "查询外部数据库",
                "终止节点名称": "普通模式数据插入数据拼盘",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${BasicInfoTableName}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行update",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "update ${BasicInfoTableName} set is_delete=0 where netunit_ip = '192.168.88.123'"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行delete",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${BasicInfoTableName} where netunit_name='MME_ME60_100'"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_46_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${SupplyInfoTableName}"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_47_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_48_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行update",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "update ${SupplyInfoTableName} set update_date=now() where col_2='www.baidu.com'"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_49_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行delete",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${SupplyInfoTableName}"
                            }
                        ]
                    }
                }
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
