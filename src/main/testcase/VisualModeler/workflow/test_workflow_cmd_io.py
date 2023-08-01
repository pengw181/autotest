# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 上午11:55

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class WorkFlowCmdNodeIO(unittest.TestCase):

    log.info("装载流程输入输出指令配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试指令节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_测试指令输入输出参数",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_测试指令输入输出参数说明"
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
                "流程名称": "auto_流程_测试指令输入输出参数",
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
                "流程名称": "auto_流程_测试指令输入输出参数",
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
        u"""通用节点，添加域名变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
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
                                    ["自定义值", "www.sina.com"],
                                    ["并集", ""],
                                    ["自定义值", "www.huya.com"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "域名"
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
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置指令节点，输出参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "输入输出指令-输出参数",
                    "成员选择": "",
                    "网元选择": "",
                    "选择方式": "网元",
                    "场景标识": "无",
                    "配置": {
                        "层级": "4G,4G_MME",
                        "层级成员": ["${NetunitMME1}", "${NetunitMME2}"],
                        "网元类型": "MME",
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "网元": ["${NetunitMME1}", "${NetunitMME2}"],
                        "指令": {
                            "auto_指令_单参数": {
                                "解析模版": "auto_解析模板_解析ping",
                                "参数设置": ""
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

    def test_8_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置指令节点，输入参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "输入输出指令-输入参数",
                    "成员选择": "",
                    "网元选择": "",
                    "选择方式": "网元",
                    "场景标识": "无",
                    "配置": {
                        "层级": "4G,4G_MME",
                        "层级成员": ["${NetunitMME1}", "${NetunitMME2}"],
                        "网元类型": "MME",
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "网元": ["${NetunitMME1}", "${NetunitMME2}"],
                        "指令": {
                            "auto_指令_echo": {
                                "解析模版": "",
                                "参数设置": ""
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

    def test_10_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-原始结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点",
                "节点名称": "输入输出指令-输出参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令输出参数-原始结果",
                    "对象类型": "网元",
                    "结果类型": "原始结果",
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

    def test_11_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-原始结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "指令节点",
                "节点名称": "输入输出指令-输入参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令输入参数-原始结果",
                    "对象类型": "网元",
                    "结果类型": "原始结果",
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

    def test_12_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
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

    def test_13_process_node_line(self):
        u"""节点参数设置连线到节点：输入输出指令-输出参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "起始节点名称": "参数设置",
                "终止节点名称": "输入输出指令-输出参数",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_node_line(self):
        u"""节点输入输出指令-输出参数连线到节点：输入输出指令-输入参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "起始节点名称": "输入输出指令-输出参数",
                "终止节点名称": "输入输出指令-输入参数",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_line(self):
        u"""节点输入输出指令-输入参数连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "起始节点名称": "输入输出指令-输入参数",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数"
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
