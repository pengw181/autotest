# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/4 上午10:26

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class AllNodePart1(unittest.TestCase):

    log.info("装载全流程配置测试用例（1）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_全流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，全流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_全流程",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_全流程",
                "高级配置": {
                    "节点异常终止流程": "否",
                    "输出异常": {
                        "状态": "开启",
                        "告警方式": "邮件",
                        "发件人": "pw@henghaodata.com",
                        "收件人": ["pw@henghaodata.com"],
                        "抄送人": ["pw@henghaodata.com"],
                        "主题": "auto_全流程标题",
                        "正文": "auto_全流程运行异常"
                    }
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
                "流程名称": "auto_全流程",
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
                "流程名称": "auto_全流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：ip列表"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "www.baidu.com"],
                                    ["并集", ""],
                                    ["自定义值", "www.huya.com"],
                                    ["并集", ""],
                                    ["自定义值", "www.sina.com"],
                                    ["并集", ""],
                                    ["自定义值", "192.168.88.116"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "ip列表"
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：次数列表"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "1"],
                                    ["并集", ""],
                                    ["自定义值", "2"],
                                    ["并集", ""],
                                    ["自定义值", "3"],
                                    ["并集", ""],
                                    ["自定义值", "4"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "次数列表"
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：指令参数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", [
                                        "${NetunitMME1},192.168.88.116,2",
                                        "${NetunitMME1},192.168.88.116,3",
                                        "${NetunitMME2},192.168.88.107,4",
                                        "${NetunitMME3},www.baidu.com,5",
                                        "${NetunitMME3},www.sina.com,2"
                                    ]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "指令参数"
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

    def test_8_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，正则运算，对变量指令参数进行正则运算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "参数设置",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "正则运算",
                            "配置": {
                                "输入变量": "指令参数",
                                "输出变量": "指令参数",
                                "解析配置": {
                                    "解析开始行": "1",
                                    "通过正则匹配数据列": "否",
                                    "列总数": "3",
                                    "拆分方式": "文本",
                                    "拆分符": ",",
                                    "样例数据": [
                                        "${NetunitMME1},192.168.88.116,2",
                                        "${NetunitMME1},192.168.88.116,3",
                                        "${NetunitMME2},192.168.88.107,4",
                                        "${NetunitMME3},www.baidu.com,5",
                                        "${NetunitMME3},www.sina.com,2"
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：绝对路径"""
        pres = """
        ${Database}.main|select catalog_path from tn_catalog_def t where belong_id='${BelongID}' and domain_id='${DomainID}' and catalog_type=1|CatalogPath
        """
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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

    def test_10_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：相对路径"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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

    def test_11_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：文件名"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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

    def test_12_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：脚本参数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "hello world"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "脚本参数"
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

    def test_13_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：个人目录"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "/auto_一级目录"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "个人目录"
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

    def test_14_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：元素"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "//span[text()='个人目录']"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "元素"
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

    def test_15_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：元素名称"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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
                                    ["自定义值", "常用信息管理"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "元素名称"
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

    def test_16_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：当天0点"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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

    def test_17_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量：当天24点"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
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

    def test_18_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置指令节点，指令节点多指令"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "指令节点多指令",
                    "选择方式": "网元",
                    "配置": {
                        "层级": "4G,4G_MME",
                        "层级成员": ["${NetunitMME1}", "${NetunitMME2}"],
                        "网元类型": "MME",
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "网元": ["${NetunitMME1}", "${NetunitMME2}"],
                        "指令": {
                            "auto_指令_date": {
                                "解析模版": "auto_解析模板_解析date"
                            },
                            "auto_指令_单参数": {
                                "解析模版": "auto_解析模板_解析ping",
                                "参数设置": {
                                    "模式": "独立模式",
                                    "参数": "ip列表"
                                }
                            },
                            "auto_指令_多参数": {
                                "解析模版": "auto_解析模板_解析ping",
                                "参数设置": {
                                    "模式": "二维表模式",
                                    "参数": {
                                        "选择变量": "指令参数",
                                        "对象设置": "[1]",
                                        "参数1": "[2],ip",
                                        "参数2": "[3],times"
                                    }
                                }
                            }
                        }
                    },
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "1"
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
        u"""节点指令节点多指令添加取数配置，成员-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点",
                "节点名称": "指令节点多指令",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "成员-解析结果",
                    "对象类型": "成员",
                    "结果类型": "解析结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_fetch_conf(self):
        u"""节点指令节点多指令添加取数配置，网元-格式化二维表结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点",
                "节点名称": "指令节点多指令",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元-格式化二维表结果",
                    "对象类型": "网元",
                    "结果类型": "格式化二维表结果",
                    "指令": "auto_指令_多参数",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_fetch_conf(self):
        u"""节点指令节点多指令添加取数配置，网元-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点",
                "节点名称": "指令节点多指令",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元-解析结果",
                    "对象类型": "网元",
                    "结果类型": "解析结果",
                    "指令": "全部指令",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_fetch_conf(self):
        u"""节点指令节点多指令添加取数配置，网元-异常结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "指令节点",
                "节点名称": "指令节点多指令",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元-异常结果",
                    "对象类型": "网元",
                    "结果类型": "异常结果",
                    "指令": "全部指令",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置通用节点：指令结果数组格式化"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "指令结果数组格式化",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_node_opt_conf(self):
        u"""节点指令结果数组格式化，操作配置，添加循环"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令结果数组格式化",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加循环",
                        "循环配置": {
                            "循环类型": "变量列表",
                            "模式": "便捷模式",
                            "变量选择": "网元-格式化二维表结果"
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

    def test_27_process_node_opt_conf(self):
        u"""节点指令结果数组格式化，操作配置，循环中添加操作，添加变量：table_format"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令结果数组格式化",
                "操作配置": [
                    {
                        "对象": "列表循环",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "tableFormat_网元-格式化二维表结果",
                                        "数组索引": "",
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
                                    "变量名": "table_format"
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

    def test_28_process_node_opt_conf(self):
        u"""节点指令结果数组格式化，操作配置，循环中添加操作，添加变量：指令结果格式化"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令结果数组格式化",
                "操作配置": [
                    {
                        "对象": "列表循环",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["变量", "netunitName_网元-格式化二维表结果"],
                                    ["并集", ""],
                                    ["变量", "cmdname_网元-格式化二维表结果"],
                                    ["并集", ""],
                                    ["变量", "table_format"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "指令结果格式化"
                                },
                                "输出列": "*",
                                "赋值方式": "追加",
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

    def test_29_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_business_conf(self):
        u"""配置文件节点：将指令结果存入文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "将指令结果存入文件",
                    "操作模式": "文件存储",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_全流程"
                    },
                    "文件配置": [
                        {
                            "变量": "指令结果格式化",
                            "文件名": "指令结果格式化",
                            "文件类型": "xlsx"
                        },
                        {
                            "变量": "网元-格式化二维表结果",
                            "文件名": "网元-格式化二维表结果",
                            "文件类型": "xls"
                        },
                        {
                            "变量": "网元-异常结果",
                            "文件名": "网元-异常结果",
                            "文件类型": "txt",
                            "分隔符": ","
                        },
                        {
                            "变量": "成员-解析结果",
                            "文件名": "成员-解析结果",
                            "文件类型": "csv",
                            "分隔符": ","
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

    def test_31_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_node_business_conf(self):
        u"""配置文件节点：将文件移入临时目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "将文件移入临时目录",
                    "操作模式": "文件拷贝或移动",
                    "源": {
                         "存储类型": "本地",
                         "目录": "auto_全流程"
                    },
                    "目标": {
                         "存储类型": "本地",
                         "目录": "auto_临时目录"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "指令结果格式化",
                            "目标文件": "",
                            "模式": "移动"
                        },
                        {
                            "类型": "关键字",
                            "文件名": "网元-格式化二维表结果",
                            "目标文件": "",
                            "模式": "移动"
                        },
                        {
                            "类型": "关键字",
                            "文件名": "网元-异常结果",
                            "目标文件": "",
                            "模式": "移动"
                        },
                        {
                            "类型": "关键字",
                            "文件名": "成员-解析结果",
                            "目标文件": "",
                            "模式": "移动"
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

    def test_33_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_node_business_conf(self):
        u"""配置文件节点：从临时目录加载文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "从临时目录加载文件",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_临时目录"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "指令结果格式化",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "",
                            "变量": "加载网元_table_format",
                            "变量类型": "替换"
                        },
                        {
                            "类型": "关键字",
                            "文件名": "网元-格式化二维表结果",
                            "文件类型": "xls",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "",
                            "变量": "加载网元-格式化二维表结果",
                            "变量类型": "替换"
                        },
                        {
                            "类型": "关键字",
                            "文件名": "网元-异常结果",
                            "文件类型": "txt",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "分隔符": ",",
                            "变量": "加载网元-异常结果",
                            "变量类型": "替换"
                        },
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配成员文件名"
                            },
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "分隔符": ",",
                            "变量": "加载成员-解析结果",
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

    def test_35_process_node_add(self):
        u"""画流程图，添加一个sql节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "Sql节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_node_business_conf(self):
        u"""配置sql节点：清除历史数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "清除历史数据",
                    "操作模式": "SQL模式",
                    "sql配置": {
                        "数据库": "AiSee",
                        "编写sql": [
                            {
                                "类型": "自定义值",
                                "自定义值": "delete from ${OtherInfoTableName} where 1=1"
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
                "流程名称": "auto_全流程",
                "节点类型": "数据库节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_node_business_conf(self):
        u"""配置sql节点：将指令结果格式化存入数据库"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据库节点",
                "节点名称": "数据库节点",
                "业务配置": {
                    "节点名称": "将指令结果格式化存入数据库",
                    "操作模式": "配置模式",
                    "sql配置": {
                        "变量": "指令结果格式化",
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
                                "字段值": ""
                            },
                            "列5": {
                                "值类型": "自定义值",
                                "字段值": ""
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

    def test_39_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_business_conf(self):
        u"""配置脚本节点：python脚本"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "python脚本",
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

    def test_41_process_node_fetch_conf(self):
        u"""节点python脚本添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "python脚本",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "python脚本返回",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_business_conf(self):
        u"""配置脚本节点：java脚本"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "java脚本",
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

    def test_44_process_node_fetch_conf(self):
        u"""节点java脚本添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "java脚本",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "java脚本返回",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_add(self):
        u"""画流程图，添加一个脚本节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_business_conf(self):
        u"""配置脚本节点：jar脚本"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "脚本节点",
                "业务配置": {
                    "节点名称": "jar脚本",
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

    def test_47_process_node_fetch_conf(self):
        u"""节点jar脚本添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "脚本节点",
                "节点名称": "jar脚本",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "jar脚本返回",
                    "赋值方式": "替换"
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
