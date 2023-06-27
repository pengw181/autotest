# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/13 上午11:00

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CmdTplNode(unittest.TestCase):

    log.info("装载流程指令模版通用功能测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试指令模版节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_指令模版通用功能",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_指令模版通用功能说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个指令模版节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置指令模版节点，指令不带参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令模版节点",
                "业务配置": {
                    "节点名称": "指令不带参数",
                    "指令任务模版": "auto_指令模板_date",
                    "应用指令模版名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_node_add(self):
        u"""画流程图，添加一个指令模版节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_node_business_conf(self):
        u"""配置指令模版节点，指令带参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令模版节点",
                "业务配置": {
                    "节点名称": "指令带参数",
                    "指令任务模版": "auto_指令模板_指令带参数",
                    "应用指令模版名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_add(self):
        u"""画流程图，添加一个指令模版节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置指令模版节点，组合指令"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令模版节点",
                "业务配置": {
                    "节点名称": "组合指令",
                    "指令任务模版": "auto_指令模板_组合指令",
                    "应用指令模版名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置指令模版节点，应用指令模版名称"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令不带参数",
                "业务配置": {
                    "节点名称": "指令不带参数",
                    "指令任务模版": "auto_指令模板_date",
                    "应用指令模版名称": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置指令模版节点，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "auto_指令模板_date",
                "业务配置": {
                    "节点名称": "指令不带参数",
                    "指令任务模版": "auto_指令模板_date",
                    "应用指令模版名称": "否",
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600"
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
        u"""画流程图，添加一个指令模版节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置指令模版节点，按网元类型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令模版节点",
                "业务配置": {
                    "节点名称": "按网元类型",
                    "指令任务模版": "auto_指令模板_按网元类型",
                    "应用指令模版名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-原始结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令不带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令模版节点-网元-原始结果",
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

    def test_14_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令不带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令模版节点-网元-解析结果",
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

    def test_15_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-清洗结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令不带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令模版节点-网元-清洗结果",
                    "对象类型": "网元",
                    "结果类型": "清洗结果",
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

    def test_16_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-格式化二维表结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "指令模版节点",
                "节点名称": "指令不带参数",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "指令模版节点-网元-格式化二维表结果",
                    "对象类型": "网元",
                    "结果类型": "格式化二维表结果",
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

    def test_17_process_node_line(self):
        u"""开始节点连线到节点：指令不带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "起始节点名称": "开始",
                "终止节点名称": "指令不带参数",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_line(self):
        u"""节点指令不带参数连线到节点：指令带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "起始节点名称": "指令不带参数",
                "终止节点名称": "指令带参数",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_line(self):
        u"""节点指令带参数连线到节点：组合指令"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "起始节点名称": "指令带参数",
                "终止节点名称": "组合指令",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_line(self):
        u"""节点组合指令连线到节点：按网元类型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "起始节点名称": "组合指令",
                "终止节点名称": "按网元类型",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_line(self):
        u"""节点按网元类型连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "起始节点名称": "按网元类型",
                "终止节点名称": "正常",
                "关联关系": "满足"
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
