# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/6 下午6:16

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class EmailNode(unittest.TestCase):

    log.info("装载流程邮件接收配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_邮件接收"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试邮件节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_流程_邮件接收说明"
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
                "流程名称": "auto_流程_邮件接收",
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
                "流程名称": "auto_流程_邮件接收",
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
        u"""通用节点，添加一个自定义变量，当天0点"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
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
                                        "时间格式": "yyyy-MM-dd 00:00",
                                        "间隔": "0",
                                        "单位": "日",
                                        "语言": "中文"
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "当天0点"
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
        u"""通用节点，添加一个自定义变量，当天24点"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
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
                                        "时间格式": "yyyy-MM-dd 23:59",
                                        "间隔": "0",
                                        "单位": "日",
                                        "语言": "中文"
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "当天24点"
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
        u"""通用节点，添加一个自定义变量，标题"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
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
                                    ["自定义值", ["自动化测试"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "标题"
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

    def test_8_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，选择开始时间和结束时间"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "选择开始时间和结束时间过滤",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "否",
                            "值": "2020-11-20 10:15"
                        },
                        "发件结束时间": {
                            "变量引用": "否",
                            "值": "2020-11-23 23:59"
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

    def test_10_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，开始时间和结束时间使用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "开始时间和结束时间使用变量",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，收件人使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "收件人使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，发件人使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "发件人使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "发件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
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

    def test_16_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，标题使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "标题使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "标题": {
                            "正则匹配": "否",
                            "值": "测试邮件(2)"
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

    def test_18_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，正文使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "正文使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "正文": {
                            "正则匹配": "否",
                            "值": "收件人为变量"
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，附件使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "附件使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "附件": {
                            "正则匹配": "否",
                            "值": "factor"
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，标题引用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "标题引用变量",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "标题": {
                            "正则匹配": "否",
                            "值": "{标题}"
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，附件使用正则匹配"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "附件使用正则匹配",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "发件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "附件": {
                            "正则匹配": "是",
                            "值": {
                                "设置方式": "添加",
                                "正则模版名称": "auto_正则模版",
                                "标签配置": [
                                    {
                                        "标签": "任意中文字符",
                                        "长度": "1到多个",
                                        "是否取值": "无"
                                    },
                                    {
                                        "标签": "字母",
                                        "长度": "1到多个",
                                        "是否取值": "无"
                                    },
                                    {
                                        "标签": "自定义文本",
                                        "自定义值": ".pdf",
                                        "是否取值": "无"
                                    }
                                ]
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

    def test_26_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，接收并存储附件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "接收并存储附件",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${当天0点}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${当天24点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "发件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "附件类型": ["txt", "xlsx"],
                        "存储附件": "开启",
                        "存储附件目录": "auto_一级目录"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_node_fetch_conf(self):
        u"""节点添加取数配置，标题"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件标题",
                    "变量类型": "标题",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_fetch_conf(self):
        u"""节点添加取数配置，正文"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件正文",
                    "变量类型": "正文",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_fetch_conf(self):
        u"""节点添加取数配置，附件内容"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件附件内容",
                    "变量类型": "附件",
                    "附件类型": "xlsx",
                    "文件名": "factor",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_fetch_conf(self):
        u"""节点添加取数配置，附件文件名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件附件文件名",
                    "变量类型": "附件文件名",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_node_fetch_conf(self):
        u"""节点添加取数配置，发件人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件发件人",
                    "变量类型": "发件人",
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
        u"""节点添加取数配置，收件人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件收件人",
                    "变量类型": "收件人",
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
        u"""节点添加取数配置，抄送人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "邮件节点",
                "节点名称": "接收并存储附件",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件抄送人",
                    "变量类型": "抄送人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
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

    def test_36_process_node_line(self):
        u"""节点参数设置连线到：选择开始时间和结束时间过滤"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "参数设置",
                "终止节点名称": "选择开始时间和结束时间过滤",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_node_line(self):
        u"""节点选择开始时间和结束时间过滤选择连线到：开始时间和结束时间使用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "选择开始时间和结束时间过滤",
                "终止节点名称": "开始时间和结束时间使用变量",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_node_line(self):
        u"""节点开始时间和结束时间使用变量连线到：收件人使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "开始时间和结束时间使用变量",
                "终止节点名称": "收件人使用关键字",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_process_node_line(self):
        u"""节点收件人使用关键字连线到：发件人使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "收件人使用关键字",
                "终止节点名称": "发件人使用关键字",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_line(self):
        u"""节点发件人使用关键字连线到：标题使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "发件人使用关键字",
                "终止节点名称": "标题使用关键字",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_process_node_line(self):
        u"""节点标题使用关键字连线到：正文使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "标题使用关键字",
                "终止节点名称": "正文使用关键字",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_process_node_line(self):
        u"""节点正文使用关键字连线到：附件使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "正文使用关键字",
                "终止节点名称": "附件使用关键字",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_line(self):
        u"""节点附件使用关键字连线到：标题引用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "附件使用关键字",
                "终止节点名称": "标题引用变量",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_line(self):
        u"""节点标题引用变量连线到：附件使用正则匹配"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "标题引用变量",
                "终止节点名称": "附件使用正则匹配",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_line(self):
        u"""节点附件使用正则匹配连线到：接收并存储附件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "附件使用正则匹配",
                "终止节点名称": "接收并存储附件",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点接收并存储附件连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "起始节点名称": "接收并存储附件",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_邮件接收"
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