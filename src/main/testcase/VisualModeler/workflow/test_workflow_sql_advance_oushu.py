# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class SqlNodeOuShu(unittest.TestCase):

    log.info("装载流程数据库节点OuShu数据库测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试sql节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_OuShu数据库",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_oushu数据库说明",
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
                "流程名称": "auto_流程_OuShu数据库",
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
                "流程名称": "auto_流程_OuShu数据库",
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
                "流程名称": "auto_流程_OuShu数据库",
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
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置sql节点，oushu数据库drop表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "oushu数据库drop表",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "drop table auto_test_sql_data"
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
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置sql节点，oushu数据库create表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "oushu数据库create表",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "create table auto_test_sql_data("
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   stats_date varchar(100),"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   netunit varchar(100),"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   hv numeric,"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   cv numeric,"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   category varchar(64),"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "   insert_date timestamp"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": ")"
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

    def test_10_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置sql节点，oushu数据库insert数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "oushu数据库insert数据",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "insert into auto_test_sql_data values('2019', 'GZ001', 122, 1222, '101', now())"
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

    def test_12_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置sql节点，oushu数据库select数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "oushu数据库select数据",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "select * from auto_test_sql_data"
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
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置sql节点，oushu数据库drop表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "删除备用表",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "drop table auto_test_sql_data2"
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

    def test_16_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置sql节点，使用create as select创建表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "使用create as select创建表",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "create table auto_test_sql_data2 as select * from auto_test_sql_data"
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

    def test_18_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置sql节点，使用insert into select插入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "使用insert into select插入数据",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "auto_oushu数据库",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "insert into auto_test_sql_data2 select * from auto_test_sql_data"
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

    def test_20_process_node_fetch_conf(self):
        u"""节点添加取数配置，oushu数据库select数据"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "数据库节点",
                "节点名称": "oushu数据库select数据",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "oushu数据库select查询结果",
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

    def test_21_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_line(self):
        u"""节点参数设置连线到节点：oushu数据库drop表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "参数设置",
                "终止节点名称": "oushu数据库drop表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_line(self):
        u"""节点oushu数据库drop表连线到节点：oushu数据库create表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "oushu数据库drop表",
                "终止节点名称": "oushu数据库create表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_line(self):
        u"""节点oushu数据库create表连线到节点：oushu数据库insert数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "oushu数据库create表",
                "终止节点名称": "oushu数据库insert数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_line(self):
        u"""节点oushu数据库insert数据连线到节点：oushu数据库select数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "oushu数据库insert数据",
                "终止节点名称": "oushu数据库select数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_node_line(self):
        u"""节点oushu数据库select数据连线到节点：删除备用表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "oushu数据库select数据",
                "终止节点名称": "删除备用表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_line(self):
        u"""节点删除备用表连线到节点：使用create as select创建表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "删除备用表",
                "终止节点名称": "使用create as select创建表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_node_line(self):
        u"""节点使用create as select创建表连线到节点：使用insert into select插入数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "使用create as select创建表",
                "终止节点名称": "使用insert into select插入数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_line(self):
        u"""节点使用insert into select插入数据连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "起始节点名称": "使用insert into select插入数据",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库"
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
