# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/2 下午3:11

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class ScriptNode(unittest.TestCase):

    log.info("装载流程脚本调用配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_脚本调用"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试脚本节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_脚本调用",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_脚本调用说明"
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
                "流程名称": "auto_流程_脚本调用",
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
                "流程名称": "auto_流程_脚本调用",
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
        u"""通用节点，操作配置,添加操作，基础运算，添加一个自定义变量，参数1"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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
                                    ["自定义值", "10"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "参数1"
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

    def test_6_process_node_opt_conf(self):
        u"""通用节点，操作配置,添加操作，基础运算，添加一个自定义变量，相对路径"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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
                                    ["自定义值", "/personal/auto_一级目录/"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "相对路径"
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

    def test_7_process_node_opt_conf(self):
        u"""通用节点，操作配置,添加操作，基础运算，添加一个自定义变量，绝对路径"""
        pres = """
        ${Database}.main|select catalog_path from tn_catalog_def t where belong_id='440100' and domain_id='AiSeeCore' and catalog_type=1|CatalogPath
        """
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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
                                    ["自定义值", "${CatalogPath}/auto_系统一级目录/"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "绝对路径"
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
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_opt_conf(self):
        u"""通用节点，操作配置,添加操作，基础运算，添加一个自定义变量，文件名"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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
                                    ["自定义值", "request.txt"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "文件名"
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

    def test_9_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，内置变量，时间变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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
                                        "时间格式": "yyyyMMddHHmmss",
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

    def test_10_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置脚本节点，不带参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本不带参数",
                    "脚本": "auto_脚本python",
                    "版本号": "V 1",
                    "参数列表": {}
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置脚本节点，带参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本带参数",
                    "脚本": "auto_脚本python",
                    "版本号": "V 2",
                    "参数列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "参数1"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "2022"
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

    def test_14_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置脚本节点，java"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点java脚本",
                    "脚本": "auto_脚本java",
                    "版本号": "V 1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置脚本节点，jar"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点jar脚本",
                    "脚本": "auto_脚本jar",
                    "版本号": "V 1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置脚本节点，相对路径"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点相对路径",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "相对路径"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "0"
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

    def test_20_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置脚本节点，绝对路径"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点绝对路径",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "绝对路径"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "0"
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

    def test_22_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置脚本节点，操作个人目录文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点操作个人目录",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "固定值",
                            "参数值": "/personal/auto_一级目录/request.txt"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "0"
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

    def test_24_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置脚本节点，操作系统目录文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本节点操作系统目录",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "固定值",
                            "参数值": "/system/auto_系统一级目录/request.txt"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "0"
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

    def test_26_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""配置脚本节点，脚本执行超时"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本执行超时",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "固定值",
                            "参数值": "/system/auto_系统一级目录/request.txt"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "700"
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

    def test_28_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_business_conf(self):
        u"""配置脚本节点，脚本重试"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "脚本执行超时重试",
                    "脚本": "auto_脚本python",
                    "版本号": "V 3",
                    "参数列表": {
                        "param1": {
                            "设置方式": "固定值",
                            "参数值": "/system/auto_系统一级目录/request.txt"
                        },
                        "param2": {
                            "设置方式": "变量",
                            "参数值": "文件名"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "60"
                        }
                    },
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "20",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_business_conf(self):
        u"""配置脚本节点，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本带参数",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_business_conf(self):
        u"""配置脚本节点，节点脚本带参数开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本带参数",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本带参数_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_process_node_fetch_conf(self):
        u"""节点脚本不带参数添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本不带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本不带参数_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_node_fetch_conf(self):
        u"""节点脚本节点java脚本添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点java脚本",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本节点java脚本_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_node_fetch_conf(self):
        u"""节点脚本节点jar脚本添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点jar脚本",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本节点jar脚本_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_node_fetch_conf(self):
        u"""节点脚本节点相对路径添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点相对路径",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本节点相对路径_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_node_fetch_conf(self):
        u"""节点脚本节点绝对路径添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点绝对路径",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "脚本节点绝对路径_脚本返回结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
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

    def test_39_process_node_line(self):
        u"""节点参数设置连线到节点：脚本不带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "参数设置",
                "终止节点名称": "脚本不带参数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_line(self):
        u"""节点脚本不带参数连线到节点：脚本带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本不带参数",
                "终止节点名称": "脚本带参数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_process_node_line(self):
        u"""节点脚本带参数连线到节点：脚本节点java脚本"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本带参数",
                "终止节点名称": "脚本节点java脚本",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_process_node_line(self):
        u"""节点脚本节点java脚本连线到节点：脚本节点jar脚本"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点java脚本",
                "终止节点名称": "脚本节点jar脚本",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_line(self):
        u"""节点脚本节点jar脚本连线到节点：脚本节点相对路径"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点jar脚本",
                "终止节点名称": "脚本节点相对路径",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_line(self):
        u"""节点脚本节点相对路径连线到节点：脚本节点绝对路径"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点相对路径",
                "终止节点名称": "脚本节点绝对路径",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_line(self):
        u"""节点脚本节点绝对路径连线到节点：脚本节点操作个人目录"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点绝对路径",
                "终止节点名称": "脚本节点操作个人目录",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_line(self):
        u"""节点脚本节点操作个人目录连线到节点：脚本节点操作系统目录"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点操作个人目录",
                "终止节点名称": "脚本节点操作系统目录",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_line(self):
        u"""节点脚本节点操作系统目录连线到节点：脚本执行超时"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本节点操作系统目录",
                "终止节点名称": "脚本执行超时",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点脚本执行超时连线到节点：脚本执行超时重试"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本执行超时",
                "终止节点名称": "脚本执行超时重试",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点脚本执行超时重试连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "起始节点名称": "脚本执行超时重试",
                "终止节点名称": "正常",
                "关联关系": "无条件"
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
