# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/4 上午10:26

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class WorkFlowAllNodePart3(unittest.TestCase):

    log.info("装载全流程配置测试用例（3）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_101_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_102_process_node_business_conf(self):
        u"""配置数据拼盘节点：数据拼盘二维表模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_103_process_node_fetch_conf(self):
        u"""配置数据拼盘节点：数据拼盘二维表模式，取数配置，添加变量：数据拼盘节点-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘二维表模式",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "数据拼盘节点-解析结果",
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

    def test_104_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_105_process_node_business_conf(self):
        u"""配置数据拼盘节点：数据拼盘列更新模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘列更新模式",
                    "数据拼盘名称": "auto_数据拼盘_列更新模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_106_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_107_process_node_business_conf(self):
        u"""配置数据拼盘节点：数据拼盘分段模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘分段模式",
                    "数据拼盘名称": "auto_数据拼盘_分段模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_108_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_109_process_node_business_conf(self):
        u"""配置数据拼盘节点：数据拼盘合并模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘合并模式",
                    "数据拼盘名称": "auto_数据拼盘_合并模式join",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_110_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_111_process_node_business_conf(self):
        u"""配置邮件节点：邮件发送"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com"]
                        },
                        "抄送人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com"]
                        },
                        "标题": "auto_全流程邮件标题",
                        "正文": [
                            {
                                "类型": "自定义值",
                                "自定义值": "全流程邮件正文"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "自定义变量",
                                "变量名": "指令结果格式化"
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

    def test_112_process_node_business_conf(self):
        u"""配置邮件节点：邮件发送，添加附件，动态生成"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "动态生成",
                                    "附件标题": "全流程附件标题",
                                    "附件内容": "${指令结果格式化}",
                                    "附件类型": "xlsx"
                                }
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

    def test_113_process_node_business_conf(self):
        u"""配置邮件节点：邮件发送，添加附件，从个人目录加载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "远程加载",
                                    "存储类型": "本地",
                                    "变量引用": "否",
                                    "目录": "auto_一级目录",
                                    "过滤类型": "关键字",
                                    "文件名": "VariableInstruction",
                                    "附件类型": "pdf"
                                }
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

    def test_114_process_node_business_conf(self):
        u"""配置邮件节点：邮件发送，添加附件，从远程ftp加载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "远程加载",
                                    "存储类型": "远程",
                                    "远程服务器": "auto_ftp",
                                    "目录": "根目录-pw-2",
                                    "过滤类型": "关键字",
                                    "文件名": "A000",
                                    "附件类型": "xlsx"
                                }
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

    def test_115_process_node_add(self):
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

    def test_116_process_node_business_conf(self):
        u"""配置通用节点：指令运行情况汇总"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "指令运行情况汇总",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_117_process_node_opt_conf(self):
        u"""配置通用节点：指令运行情况汇总，操作配置，添加运算，过滤运算，输出：正常指令"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令运行情况汇总",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "过滤运算",
                            "配置": {
                                "选择变量": "网元-解析结果",
                                "过滤条件": [
                                    ["变量索引", "3"],
                                    ["等于", ""],
                                    ["自定义值", "正常"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "正常指令"
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

    def test_118_process_node_opt_conf(self):
        u"""配置通用节点：指令运行情况汇总，操作配置，添加运算，过滤运算，输出：异常指令"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令运行情况汇总",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "过滤运算",
                            "配置": {
                                "选择变量": "网元-解析结果",
                                "过滤条件": [
                                    ["变量索引", "3"],
                                    ["等于", ""],
                                    ["自定义值", "异常"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "异常指令"
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

    def test_119_process_node_opt_conf(self):
        u"""配置通用节点：指令运行情况汇总，操作配置，添加运算，聚合运算，输出：正常指令个数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令运行情况汇总",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "配置": {
                                "选择变量": "正常指令",
                                "分组依据": "0",
                                "表达式": [
                                    ["计数(count)", "1"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "正常指令个数"
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

    def test_120_process_node_opt_conf(self):
        u"""配置通用节点：指令运行情况汇总，操作配置，添加运算，聚合运算，输出：异常指令个数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "通用节点",
                "节点名称": "指令运行情况汇总",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "聚合运算",
                            "配置": {
                                "选择变量": "异常指令",
                                "分组依据": "0",
                                "表达式": [
                                    ["计数(count)", "1"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "异常指令个数"
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

    def test_121_process_node_add(self):
        u"""画流程图，添加一个信息处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "信息处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_122_process_node_business_conf(self):
        u"""配置信息处理节点：流程相关信息展示"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "信息处理节点",
                "节点名称": "信息处理节点",
                "业务配置": {
                    "节点名称": "流程相关信息展示",
                    "操作模式": "结果呈现/下载",
                    "信息描述": "正常：${正常指令个数}，异常：${异常指令个数}",
                    "显示在运行信息的标题": "是",
                    "信息明细": [
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "加载网元-格式化二维表结果"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "restful接口返回"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "soap接口返回sessionid"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "流程列表"
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

    def test_123_process_node_business_conf(self):
        u"""配置信息处理节点：流程相关信息展示，启用下载，增加下载文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "信息处理节点",
                "节点名称": "流程相关信息展示",
                "业务配置": {
                    "启用下载": {
                        "状态": "开启",
                        "文件配置": [
                            {
                                "目录": "auto_一级目录",
                                "文件名": "request.txt"
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

    def test_124_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_125_process_node_business_conf(self):
        u"""配置邮件节点：邮件接收"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收",
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
                        "标题": {
                            "正则匹配": "否",
                            "值": "auto_全流程"
                        },
                        "正文": {
                            "正则匹配": "否",
                            "值": "全流程邮件正文"
                        },
                        "附件类型": ["xlsx"],
                        "存储附件": "开启",
                        "存储附件目录": "auto_全流程"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_126_process_node_fetch_conf(self):
        u"""配置邮件节点：邮件接收，取数配置，添加变量：邮件接收附件文件名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "邮件接收附件文件名",
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

    def test_127_process_node_fetch_conf(self):
        u"""配置邮件节点：邮件接收，取数配置，添加变量：邮件接收正文"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "邮件接收正文",
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

    def test_128_process_node_add(self):
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

    def test_129_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：单指标接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载AI预测数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_AI"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "single_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "1",
                            "开始读取行": "2",
                            "变量": "单指标接入数据",
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

    def test_130_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：通用算法接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "classical_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "3",
                            "变量": "通用算法接入数据",
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

    def test_131_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：干扰因素接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factor_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "",
                            "变量": "干扰因素接入数据",
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

    def test_132_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：factorXGB接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factorXGB_predict",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "2",
                            "分隔符": ",",
                            "变量": "factorXGB接入数据",
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

    def test_133_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：factorLGBM接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factorLGBM_predict",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "分隔符": ",",
                            "变量": "factorLGBM接入数据",
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

    def test_134_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_135_process_node_business_conf(self):
        u"""配置AI节点：LSTM预测模型，单指标预测，lstm模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "LSTM预测模型",
                    "节点模式": "单指标预测",
                    "算法选择": "LSTM预测模型",
                    "模型": "auto_AI模型lstm",
                    "输入变量": "单指标接入数据",
                    "对应关系配置": {
                        "状态": "开启",
                        "1": "time(时间列)",
                        "2": "online_number(预测列)"
                    },
                    "预测步长": "10",
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

    def test_136_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_137_process_node_business_conf(self):
        u"""配置AI节点：SARIMA预测模型，单指标预测，sarima模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "SARIMA预测模型",
                    "节点模式": "单指标预测",
                    "算法选择": "SARIMA预测模型",
                    "模型": "auto_AI模型sarima",
                    "输入变量": "单指标接入数据",
                    "预测步长": "10"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_138_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_139_process_node_business_conf(self):
        u"""配置AI节点：GRU预测模型，存在干扰因素的多指标预测，gru模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "GRU预测模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "GRU预测模型",
                    "模型": "auto_AI模型gru",
                    "输入变量": "干扰因素接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_140_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_141_process_node_business_conf(self):
        u"""配置AI节点：xgboost预测模型，存在干扰因素的多指标预测，xgboost模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "xgboost预测模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "xgboost预测模型",
                    "模型": "auto_AI模型xgboost",
                    "输入变量": "factorXGB接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_142_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_143_process_node_business_conf(self):
        u"""配置AI节点：factorLGBM模型，存在干扰因素的多指标预测，factorLGBM模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "factorLGBM模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "factorLGBM",
                    "模型": "auto_AI模型factorLGBM",
                    "输入变量": "factorLGBM接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_144_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_145_process_node_business_conf(self):
        u"""配置AI节点：lightgbm模型，通用分类算法，lightgbm模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "lightgbm模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "lightgbm模型",
                    "模型": "auto_AI模型lightgbm",
                    "输入变量": "通用算法接入数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_146_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_147_process_node_business_conf(self):
        u"""配置AI节点：梯度提升树（GBDT）模型，通用分类算法，梯度提升树（GBDT）模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "梯度提升树（GBDT）模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "梯度提升树（GBDT）模型",
                    "模型": "auto_AI模型梯度提升树（GBDT）",
                    "输入变量": "通用算法接入数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_148_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_149_process_node_business_conf(self):
        u"""配置AI节点：随机森林模型，通用分类算法，随机森林模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "随机森林模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "随机森林模型",
                    "模型": "auto_AI模型随机森林",
                    "输入变量": "通用算法接入数据"
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
