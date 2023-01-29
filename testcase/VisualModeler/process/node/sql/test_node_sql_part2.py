# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class SqlNodePart2(unittest.TestCase):

    log.info("装载流程sql节点配置测试用例（2）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_51_process_node_add(self):
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

    def test_52_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行update",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "update ${OtherInfoTableName} set is_delete=0 where col_2='时间'"
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

    def test_53_process_node_add(self):
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

    def test_54_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行truncate"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行truncate",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "truncate table ${OtherInfoTableName}"
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

    def test_55_process_node_add(self):
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

    def test_56_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行drop"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行drop",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "drop table ${OtherInfoTableName}"
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

    def test_57_process_node_add(self):
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

    def test_58_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${Edata1TableName}"
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

    def test_59_process_node_add(self):
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

    def test_60_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行update",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "update ${Edata1TableName} set version='0' where command='1'"
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

    def test_61_process_node_add(self):
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

    def test_62_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行delete",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${Edata1TableName} where 1=1"
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

    def test_63_process_node_add(self):
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

    def test_64_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘列更新模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘列更新模式表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${Edata2TableName}"
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

    def test_65_process_node_add(self):
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

    def test_66_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘分段模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘分段模式表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${Edata3TableName}"
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

    def test_67_process_node_add(self):
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

    def test_68_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${Edata4TableName}"
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

    def test_69_process_node_add(self):
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

    def test_70_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行update",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "update ${Edata4TableName} set version='0' where col_2='1'"
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

    def test_71_process_node_add(self):
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

    def test_72_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行delete",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${Edata4TableName} where col_2='1'"
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

    def test_73_process_node_add(self):
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

    def test_74_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行truncate"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行truncate",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "truncate table ${Edata4TableName}"
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

    def test_75_process_node_add(self):
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

    def test_76_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行drop"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行drop",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "drop table ${Edata4TableName}"
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

    def test_77_process_node_add(self):
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

    def test_78_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘合并模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对数据拼盘合并模式表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from ${Edata5TableName}"
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

    def test_79_process_node_add(self):
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

    def test_80_process_node_business_conf(self):
        u"""配置sql节点，对系统内部表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "Sql节点",
                "节点名称": "Sql节点",
                "业务配置": {
                    "节点名称": "对系统内部表执行select",
                    "操作模式": "sql节点高级模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from tn_process_conf_info"
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

    def test_81_process_node_line(self):
        u"""节点普通模式数据插入数据拼盘连线到:对网元基础信息表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "普通模式数据插入数据拼盘",
                "终止节点名称": "对网元基础信息表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_82_process_node_line(self):
        u"""节点对网元基础信息表执行select连线到：对网元基础信息表执行update节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元基础信息表执行select",
                "终止节点名称": "对网元基础信息表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_83_process_node_line(self):
        u"""节点对网元基础信息表执行update连线到：对网元基础信息表执行delete节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元基础信息表执行update",
                "终止节点名称": "对网元基础信息表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_84_process_node_line(self):
        u"""节点对网元基础信息表执行delete连线到：对网元辅助资料表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元基础信息表执行delete",
                "终止节点名称": "对网元辅助资料表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_85_process_node_line(self):
        u"""节点对网元辅助资料表执行select连线到：对网元辅助资料表执行update节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元辅助资料表执行select",
                "终止节点名称": "对网元辅助资料表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_86_process_node_line(self):
        u"""节点对网元辅助资料表执行update连线到：对网元辅助资料表执行delete节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元辅助资料表执行update",
                "终止节点名称": "对网元辅助资料表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_87_process_node_line(self):
        u"""节点对网元辅助资料表执行delete连线到：对网元其它资料表执行update节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元辅助资料表执行delete",
                "终止节点名称": "对网元其它资料表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_88_process_node_line(self):
        u"""节点对网元其它资料表执行update连线到：对网元其它资料表执行truncate节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元其它资料表执行update",
                "终止节点名称": "对网元其它资料表执行truncate",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_89_process_node_line(self):
        u"""节点对网元其它资料表执行truncate连线到：对网元其它资料表执行drop节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元其它资料表执行truncate",
                "终止节点名称": "对网元其它资料表执行drop",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_90_process_node_line(self):
        u"""节点对网元其它资料表执行drop连线到：对数据拼盘二维表模式表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对网元其它资料表执行drop",
                "终止节点名称": "对数据拼盘二维表模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_91_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行select连线到：对数据拼盘二维表模式表执行update节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘二维表模式表执行select",
                "终止节点名称": "对数据拼盘二维表模式表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_92_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行update连线到：对数据拼盘二维表模式表执行delete节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘二维表模式表执行update",
                "终止节点名称": "对数据拼盘二维表模式表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_93_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行delete连线到：对数据拼盘列更新模式表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘二维表模式表执行delete",
                "终止节点名称": "对数据拼盘列更新模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_94_process_node_line(self):
        u"""节点对数据拼盘列更新模式表执行select连线到：对数据拼盘分段模式表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘列更新模式表执行select",
                "终止节点名称": "对数据拼盘分段模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_95_process_node_line(self):
        u"""节点对数据拼盘分段模式表执行select连线到：对数据拼盘数据模式表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘分段模式表执行select",
                "终止节点名称": "对数据拼盘数据模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_96_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行select连线到：对数据拼盘数据模式表执行update节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘数据模式表执行select",
                "终止节点名称": "对数据拼盘数据模式表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_97_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行update连线到：对数据拼盘数据模式表执行delete节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘数据模式表执行update",
                "终止节点名称": "对数据拼盘数据模式表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_98_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行delete连线到：对数据拼盘数据模式表执行truncate节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘数据模式表执行delete",
                "终止节点名称": "对数据拼盘数据模式表执行truncate",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_99_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行truncate连线到：对数据拼盘数据模式表执行drop节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘数据模式表执行truncate",
                "终止节点名称": "对数据拼盘数据模式表执行drop",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_100_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行drop连线到：对数据拼盘合并模式表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘数据模式表执行drop",
                "终止节点名称": "对数据拼盘合并模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_101_process_node_line(self):
        u"""节点对数据拼盘合并模式表执行select连线到：对系统内部表执行select节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对数据拼盘合并模式表执行select",
                "终止节点名称": "对系统内部表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_102_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_103_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_104_process_node_line(self):
        u"""节点对系统内部表执行select连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_sql节点流程",
                "起始节点名称": "对系统内部表执行select",
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
