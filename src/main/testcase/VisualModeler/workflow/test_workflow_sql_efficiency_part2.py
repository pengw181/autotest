# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class WorkFlowSqlNodeEfficiencyPart2(unittest.TestCase):

    log.info("装载流程数据库节点大数据效率测试用例（2）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_51_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_business_conf(self):
        u"""配置sql节点，配置模式，pg数据库，批量提交行数不为空，2w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部pg数据库2w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据2w_异常",
                        "数据库": "auto_postgres数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_53_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_business_conf(self):
        u"""配置sql节点，配置模式，oracle数据库，批量提交行数不为空，2w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部oracle数据库2w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据2w_异常",
                        "数据库": "auto_oracle数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_55_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_business_conf(self):
        u"""配置sql节点，配置模式，mysql数据库，批量提交行数不为空，2w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库2w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据2w_异常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_57_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_process_node_business_conf(self):
        u"""配置sql节点，配置模式，pg数据库，批量提交行数不为空，5w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部pg数据库5w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据5w_异常",
                        "数据库": "auto_postgres数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_59_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_process_node_business_conf(self):
        u"""配置sql节点，配置模式，oracle数据库，批量提交行数不为空，5w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部oracle数据库5w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据5w_异常",
                        "数据库": "auto_oracle数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_61_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_business_conf(self):
        u"""配置sql节点，配置模式，mysql数据库，批量提交行数不为空，5w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库5w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据5w_异常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_63_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_business_conf(self):
        u"""配置sql节点，配置模式，pg数据库，批量提交行数不为空，10w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部pg数据库10w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据10w_异常",
                        "数据库": "auto_postgres数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_65_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_node_business_conf(self):
        u"""配置sql节点，配置模式，oracle数据库，批量提交行数不为空，10w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部oracle数据库10w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据10w_异常",
                        "数据库": "auto_oracle数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_67_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_68_process_node_business_conf(self):
        u"""配置sql节点，配置模式，mysql数据库，批量提交行数不为空，10w部分异常"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "导入外部mysql数据库10w部分成功",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "大数据10w_异常",
                        "数据库": "auto_mysql数据库",
                        "存储模式": "",
                        "高级配置": {
                            "状态": "开启",
                            "跳过行数": "",
                            "批量提交行数": "1000",
                        },
                        "表选择": "auto_测试表",
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

    def test_69_process_node_line(self):
        u"""开始节点连线到节点：加载大数据入库数据1w"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "开始",
                "终止节点名称": "加载大数据入库数据1w",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_70_process_node_line(self):
        u"""节点加载大数据入库数据1w连线到节点：加载大数据入库数据2w"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "加载大数据入库数据1w",
                "终止节点名称": "加载大数据入库数据2w",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_71_process_node_line(self):
        u"""节点加载大数据入库数据2w连线到节点：加载大数据入库数据5w"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "加载大数据入库数据2w",
                "终止节点名称": "加载大数据入库数据5w",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_72_process_node_line(self):
        u"""节点加载大数据入库数据5w连线到节点：加载大数据入库数据10w"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "加载大数据入库数据5w",
                "终止节点名称": "加载大数据入库数据10w",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_73_process_node_line(self):
        u"""节点加载大数据入库数据10w连线到节点：postgres外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "加载大数据入库数据10w",
                "终止节点名称": "postgres外部表数据清理",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_74_process_node_line(self):
        u"""节点postgres外部表数据清理连线到节点：oracle外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "postgres外部表数据清理",
                "终止节点名称": "oracle外部表数据清理",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_75_process_node_line(self):
        u"""节点oracle外部表数据清理连线到节点：mysql外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "oracle外部表数据清理",
                "终止节点名称": "mysql外部表数据清理",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_76_process_node_line(self):
        u"""节点mysql外部表数据清理连线到节点：导入外部pg数据库1w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "mysql外部表数据清理",
                "终止节点名称": "导入外部pg数据库1w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_77_process_node_line(self):
        u"""节点导入外部pg数据库1w正常连线到节点：导入外部oracle数据库1w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库1w正常",
                "终止节点名称": "导入外部oracle数据库1w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_78_process_node_line(self):
        u"""节点导入外部oracle数据库1w正常连线到节点：导入外部mysql数据库1w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库1w正常",
                "终止节点名称": "导入外部mysql数据库1w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_79_process_node_line(self):
        u"""节点导入外部mysql数据库1w正常连线到节点：导入外部pg数据库2w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库1w正常",
                "终止节点名称": "导入外部pg数据库2w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_80_process_node_line(self):
        u"""节点导入外部pg数据库2w正常连线到节点：导入外部oracle数据库2w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库2w正常",
                "终止节点名称": "导入外部oracle数据库2w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_81_process_node_line(self):
        u"""节点导入外部oracle数据库2w正常连线到节点：导入外部mysql数据库2w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库2w正常",
                "终止节点名称": "导入外部mysql数据库2w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_82_process_node_line(self):
        u"""节点导入外部mysql数据库2w正常连线到节点：导入外部mysql数据库2w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库2w正常",
                "终止节点名称": "导入外部pg数据库5w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_83_process_node_line(self):
        u"""节点导入外部mysql数据库2w正常连线到节点：导入外部oracle数据库5w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库2w正常",
                "终止节点名称": "导入外部oracle数据库5w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_84_process_node_line(self):
        u"""节点导入外部oracle数据库5w正常连线到节点：导入外部mysql数据库5w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库5w正常",
                "终止节点名称": "导入外部mysql数据库5w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_85_process_node_line(self):
        u"""节点导入外部mysql数据库5w正常连线到节点：导入外部pg数据库10w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库5w正常",
                "终止节点名称": "导入外部pg数据库10w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_86_process_node_line(self):
        u"""节点导入外部pg数据库10w正常连线到节点：导入外部oracle数据库10w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库10w正常",
                "终止节点名称": "导入外部oracle数据库10w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_87_process_node_line(self):
        u"""节点导入外部oracle数据库10w正常连线到节点：导入外部mysql数据库10w正常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库10w正常",
                "终止节点名称": "导入外部mysql数据库10w正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_88_process_node_line(self):
        u"""节点导入外部mysql数据库10w正常连线到节点：导入外部pg数据库1w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库10w正常",
                "终止节点名称": "导入外部pg数据库1w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_89_process_node_line(self):
        u"""节点导入外部pg数据库1w部分成功连线到节点：导入外部oracle数据库1w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库1w部分成功",
                "终止节点名称": "导入外部oracle数据库1w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_90_process_node_line(self):
        u"""节点导入外部oracle数据库1w部分成功连线到节点：导入外部mysql数据库1w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库1w部分成功",
                "终止节点名称": "导入外部mysql数据库1w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_91_process_node_line(self):
        u"""节点导入外部mysql数据库1w部分成功连线到节点：导入外部pg数据库2w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库1w部分成功",
                "终止节点名称": "导入外部pg数据库2w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_92_process_node_line(self):
        u"""节点导入外部pg数据库2w部分成功连线到节点：导入外部oracle数据库2w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库2w部分成功",
                "终止节点名称": "导入外部oracle数据库2w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_93_process_node_line(self):
        u"""节点导入外部oracle数据库2w部分成功连线到节点：导入外部mysql数据库2w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库2w部分成功",
                "终止节点名称": "导入外部mysql数据库2w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_94_process_node_line(self):
        u"""节点导入外部mysql数据库2w部分成功连线到节点：导入外部pg数据库5w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库2w部分成功",
                "终止节点名称": "导入外部pg数据库5w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_95_process_node_line(self):
        u"""节点导入外部pg数据库5w部分成功连线到节点：导入外部oracle数据库5w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库5w部分成功",
                "终止节点名称": "导入外部oracle数据库5w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_96_process_node_line(self):
        u"""节点导入外部oracle数据库5w部分成功连线到节点：导入外部mysql数据库5w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库5w部分成功",
                "终止节点名称": "导入外部mysql数据库5w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_97_process_node_line(self):
        u"""节点导入外部mysql数据库5w部分成功连线到节点：导入外部pg数据库10w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库5w部分成功",
                "终止节点名称": "导入外部pg数据库10w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_98_process_node_line(self):
        u"""节点导入外部pg数据库10w部分成功连线到节点：导入外部oracle数据库10w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部pg数据库10w部分成功",
                "终止节点名称": "导入外部oracle数据库10w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_99_process_node_line(self):
        u"""节点导入外部oracle数据库10w部分成功连线到节点：导入外部mysql数据库10w部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部oracle数据库10w部分成功",
                "终止节点名称": "导入外部mysql数据库10w部分成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_100_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_101_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_102_process_node_line(self):
        u"""节点导入外部mysql数据库10w部分成功连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率",
                "起始节点名称": "导入外部mysql数据库10w部分成功",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_103_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_外部库导入效率"
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
