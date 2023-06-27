# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/5 下午9:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class InfoNode(unittest.TestCase):

    log.info("装载流程信息处理节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_信息处理节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试信息处理节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_信息处理节点流程",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_信息处理节点流程说明",
                "高级配置": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
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
                "流程名称": "auto_信息处理节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
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
                                    ["自定义值", ["hello world"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "测试数据"
                                },
                                "输出列": "*",
                                "赋值方式": "替换",
                                "是否转置": "否",
                                "批量修改所有相同的变量名": "否"
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
        u"""画流程图，添加一个信息处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置信息处理节点，结果呈现/下载模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "信息处理节点",
                "业务配置": {
                    "节点名称": "数据呈现",
                    "操作模式": "结果呈现/下载",
                    "信息描述": "运行结果",
                    "显示在运行信息的标题": "是",
                    "信息明细": [
                        {
                            "类型": "自定义值",
                            "自定义值": "地点:"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "流程定义变量",
                            "变量名": "地点"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "自定义值",
                            "自定义值": "流程实例id:"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "系统内置变量",
                            "变量名": "流程实例ID"
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

    def test_8_process_node_add(self):
        u"""画流程图，添加一个信息处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置信息处理节点，结果呈现/下载模式，启用下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "信息处理节点",
                "业务配置": {
                    "节点名称": "启用下载功能",
                    "操作模式": "结果呈现/下载",
                    "信息描述": "运行结果",
                    "显示在运行信息的标题": "是",
                    "信息明细": [
                        {
                            "类型": "自定义值",
                            "自定义值": "地点:"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "流程定义变量",
                            "变量名": "地点"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "自定义值",
                            "自定义值": "流程实例id:"
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "系统内置变量",
                            "变量名": "流程实例ID"
                        }
                    ],
                    "启用下载": {
                        "状态": "开启",
                        "文件配置": [
                            {
                                "目录": "auto_一级目录",
                                "文件名": "aaa.xlsx"
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

    def test_10_process_node_business_conf(self):
        u"""配置信息处理节点，结果呈现/下载模式，启用下载，增加一条配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "启用下载功能",
                "业务配置": {
                    "启用下载": {
                        "状态": "开启",
                        "文件配置": [
                            {
                                "目录": "auto_二级目录",
                                "文件名": "bbb.csv"
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

    def test_11_process_node_business_conf(self):
        u"""配置信息处理节点，结果呈现/下载模式，禁用下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "启用下载功能",
                "业务配置": {
                    "启用下载": {
                        "状态": "关闭"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置信息处理节点，结果呈现/下载模式，启用下载，增加一条配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "启用下载功能",
                "业务配置": {
                    "启用下载": {
                        "状态": "开启",
                        "文件配置": [
                            {
                                "目录": "auto_一级目录",
                                "文件名": "aaa.txt"
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
        u"""画流程图，添加一个信息处理节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置信息处理节点，告警推送模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "信息处理节点",
                "节点名称": "信息处理节点",
                "业务配置": {
                    "节点名称": "告警推送",
                    "操作模式": "告警推送",
                    "变量选择": "测试数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
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

    def test_16_process_node_line(self):
        u"""节点参数设置连线到节点：数据呈现"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "数据呈现",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_line(self):
        u"""节点数据呈现连线到节点：启用下载功能"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "起始节点名称": "数据呈现",
                "终止节点名称": "启用下载功能",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_line(self):
        u"""节点启用下载功能连线到节点：告警推送"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "起始节点名称": "启用下载功能",
                "终止节点名称": "告警推送",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_line(self):
        u"""节点告警推送连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_信息处理节点流程",
                "起始节点名称": "告警推送",
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
