# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class SqlNode(unittest.TestCase):

    log.info("装载流程数据库SQL模式权限测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试sql节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_数据库节点权限",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_数据库节点权限说明",
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
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行update",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置sql节点，对网元基础信息表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元基础信息表执行delete",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行update",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置sql节点，对网元辅助资料表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元辅助资料表执行delete",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行update",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行truncate"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行truncate",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_business_conf(self):
        u"""配置sql节点，对网元其它资料表执行drop"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对网元其它资料表执行drop",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行update",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘二维表模式表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘二维表模式表执行delete",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘列更新模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘列更新模式表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘分段模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘分段模式表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行update"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行update",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行delete",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行truncate"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行truncate",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘数据模式表执行drop"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘数据模式表执行drop",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_process_node_business_conf(self):
        u"""配置sql节点，对数据拼盘合并模式表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对数据拼盘合并模式表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_business_conf(self):
        u"""配置sql节点，对系统内部表执行select"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "对系统内部表执行select",
                    "操作模式": "SQL模式",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_line(self):
        u"""开始节点连线到：对网元基础信息表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "开始",
                "终止节点名称": "对网元基础信息表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_line(self):
        u"""节点对网元基础信息表执行select连线到：对网元基础信息表执行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元基础信息表执行select",
                "终止节点名称": "对网元基础信息表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_line(self):
        u"""节点对网元基础信息表执行update连线到：对网元基础信息表执行delete"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元基础信息表执行update",
                "终止节点名称": "对网元基础信息表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点对网元基础信息表执行delete连线到：对网元辅助资料表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元基础信息表执行delete",
                "终止节点名称": "对网元辅助资料表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_line(self):
        u"""节点对网元辅助资料表执行select连线到：对网元辅助资料表执行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元辅助资料表执行select",
                "终止节点名称": "对网元辅助资料表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_line(self):
        u"""节点对网元辅助资料表执行update连线到：对网元辅助资料表执行delete"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元辅助资料表执行update",
                "终止节点名称": "对网元辅助资料表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点对网元辅助资料表执行delete连线到：对网元其它资料表执行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元辅助资料表执行delete",
                "终止节点名称": "对网元其它资料表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_line(self):
        u"""节点对网元其它资料表执行update连线到：对网元其它资料表执行truncate"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元其它资料表执行update",
                "终止节点名称": "对网元其它资料表执行truncate",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_line(self):
        u"""节点对网元其它资料表执行truncate连线到：对网元其它资料表执行drop"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元其它资料表执行truncate",
                "终止节点名称": "对网元其它资料表执行drop",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_line(self):
        u"""节点对网元其它资料表执行drop连线到：对数据拼盘二维表模式表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对网元其它资料表执行drop",
                "终止节点名称": "对数据拼盘二维表模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_55_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行select连线到：对数据拼盘二维表模式表执行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘二维表模式表执行select",
                "终止节点名称": "对数据拼盘二维表模式表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行update连线到：对数据拼盘二维表模式表执行delete"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘二维表模式表执行update",
                "终止节点名称": "对数据拼盘二维表模式表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_57_process_node_line(self):
        u"""节点对数据拼盘二维表模式表执行delete连线到：对数据拼盘列更新模式表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘二维表模式表执行delete",
                "终止节点名称": "对数据拼盘列更新模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_process_node_line(self):
        u"""节点对数据拼盘列更新模式表执行select连线到：对数据拼盘分段模式表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘列更新模式表执行select",
                "终止节点名称": "对数据拼盘分段模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_process_node_line(self):
        u"""节点对数据拼盘分段模式表执行select连线到：对数据拼盘数据模式表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘分段模式表执行select",
                "终止节点名称": "对数据拼盘数据模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行select连线到：对数据拼盘数据模式表执行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘数据模式表执行select",
                "终止节点名称": "对数据拼盘数据模式表执行update",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行update连线到：对数据拼盘数据模式表执行delete"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘数据模式表执行update",
                "终止节点名称": "对数据拼盘数据模式表执行delete",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行delete连线到：对数据拼盘数据模式表执行truncate"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘数据模式表执行delete",
                "终止节点名称": "对数据拼盘数据模式表执行truncate",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行truncate连线到：对数据拼盘数据模式表执行drop"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘数据模式表执行truncate",
                "终止节点名称": "对数据拼盘数据模式表执行drop",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_line(self):
        u"""节点对数据拼盘数据模式表执行drop连线到：对数据拼盘合并模式表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘数据模式表执行drop",
                "终止节点名称": "对数据拼盘合并模式表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_65_process_node_line(self):
        u"""节点对数据拼盘合并模式表执行select连线到：对系统内部表执行select"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对数据拼盘合并模式表执行select",
                "终止节点名称": "对系统内部表执行select",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_67_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_68_process_node_line(self):
        u"""节点对系统内部表执行select连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "起始节点名称": "对系统内部表执行select",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_69_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限"
            }
        }
        msg = "调用测试流程成功,请到流程运行日志中查看"
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
