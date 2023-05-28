# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/1 下午9:53

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class FileNode(unittest.TestCase):

    log.info("装载流程文件拷贝移动配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试文件节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_文件拷贝移动",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_文件拷贝移动说明"
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
                "流程名称": "auto_流程_文件拷贝移动",
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
                "流程名称": "auto_流程_文件拷贝移动",
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
        u"""配置通用节点，添加一个变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
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
                                    ["自定义值", ["网元"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "文件名关键字"
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
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置文件节点，文件拷贝，使用关键字过滤文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "使用关键字拷贝文件",
                    "操作模式": "文件拷贝或移动",
                    "源": {
                         "存储类型": "本地",
                         "目录": "auto_二级目录",
                         "变量引用": "否"
                    },
                    "目标": {
                         "存储类型": "本地",
                         "目录": "auto_一级目录",
                         "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "解析结果",
                            "目标文件": "目标文件1.xlsx",
                            "模式": "拷贝"
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

    def test_20_process_node_business_conf(self):
        u"""配置文件节点，文件拷贝，文件引用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件拷贝，使用关键字过滤文件",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "${文件名关键字}",
                            "目标文件": "",
                            "模式": "拷贝"
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

    def test_21_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置文件节点，文件拷贝，使用正则匹配过滤文件，添加正则"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "文件拷贝，使用正则匹配文件名",
                    "操作模式": "文件拷贝或移动",
                    "源": {
                         "存储类型": "本地",
                         "目录": "auto_一级目录",
                         "变量引用": "否"
                    },
                    "目标": {
                         "存储类型": "本地",
                         "目录": "auto_二级目录",
                         "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "添加",
                                "正则模版名称": "auto_正则模版",
                                "标签配置": [
                                    {
                                        "标签": "自定义文本",
                                        "自定义值": "网元",
                                        "是否取值": "无"
                                    },
                                    {
                                        "标签": "任意中文字符",
                                        "长度": "1到多个",
                                        "是否取值": "无"
                                    },
                                    {
                                        "标签": "自定义文本",
                                        "自定义值": ".xlsx",
                                        "是否取值": "无"
                                    }
                                ]
                            },
                            "目标文件": "",
                            "模式": "拷贝"
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

    def test_23_process_node_business_conf(self):
        u"""配置文件节点，文件拷贝，使用正则匹配过滤文件，选择已有正则"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件拷贝，使用正则匹配文件名",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配日期"
                            },
                            "目标文件": "",
                            "模式": "拷贝"
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

    def test_24_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置文件节点，文件移动，从本地移动到ftp"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "从本地移动到ftp",
                    "操作模式": "文件拷贝或移动",
                    "源": {
                         "存储类型": "本地",
                         "目录": "auto_二级目录",
                         "变量引用": "否"
                    },
                    "目标": {
                         "存储类型": "远程",
                         "远程服务器": "auto_ftp",
                         "目录": "根目录-pw-1",
                         "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "文件名关键字",
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

    def test_26_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""配置文件节点，文件移动，从ftp移动到本地"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "从ftp移动到本地",
                    "操作模式": "文件拷贝或移动",
                    "源": {
                        "存储类型": "远程",
                        "远程服务器": "auto_ftp",
                        "目录": "根目录-pw-1",
                        "变量引用": "否"
                    },
                    "目标": {
                        "存储类型": "本地",
                        "目录": "auto_一级目录",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "文件名关键字",
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

    def test_42_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
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

    def test_43_process_node_line(self):
        u"""节点参数设置连线到节点：文件存储-本地"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "参数设置",
                "终止节点名称": "文件存储-本地",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_line(self):
        u"""节点文件存储-本地连线到节点：文件存储-ftp"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件存储-本地",
                "终止节点名称": "文件存储-ftp",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_process_node_line(self):
        u"""节点文件存储-ftp连线到节点：文件存储-目录变量引用"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件存储-ftp",
                "终止节点名称": "文件存储-目录变量引用",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_line(self):
        u"""节点文件存储-目录变量引用连线到节点：文件拷贝，使用关键字过滤文件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件存储-目录变量引用",
                "终止节点名称": "文件拷贝，使用关键字过滤文件",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_line(self):
        u"""节点文件拷贝，使用关键字过滤文件连线到节点：文件拷贝，使用正则匹配文件名"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件拷贝，使用关键字过滤文件",
                "终止节点名称": "文件拷贝，使用正则匹配文件名",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点文件拷贝，使用正则匹配文件名连线到节点：从本地移动到ftp"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件拷贝，使用正则匹配文件名",
                "终止节点名称": "从本地移动到ftp",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_line(self):
        u"""节点从本地移动到ftp连线到节点：从ftp移动到本地"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "从本地移动到ftp",
                "终止节点名称": "从ftp移动到本地",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_line(self):
        u"""节点从ftp移动到本地连线到节点：文件加载，从本地加载"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "从ftp移动到本地",
                "终止节点名称": "文件加载，从本地加载",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点文件加载，从本地加载连线到节点：文件加载，从ftp加载"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件加载，从本地加载",
                "终止节点名称": "文件加载，从ftp加载",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_line(self):
        u"""节点文件加载，从ftp加载连线到节点：文件加载，使用正则匹配文件名"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件加载，从ftp加载",
                "终止节点名称": "文件加载，使用正则匹配文件名",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_line(self):
        u"""节点文件加载，使用正则匹配文件名连线到节点：文件加载,开启过滤"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件加载，使用正则匹配文件名",
                "终止节点名称": "文件加载,开启过滤",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_55_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_line(self):
        u"""节点文件加载,开启过滤连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "起始节点名称": "文件加载,开启过滤",
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
