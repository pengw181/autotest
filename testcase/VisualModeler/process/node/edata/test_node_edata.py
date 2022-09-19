# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/13 上午11:01

import unittest
from src.screenShot import screenShot
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class EdataNode(unittest.TestCase):

    log.info("装载流程数据拼盘节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试数据拼盘节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_数据拼盘节点流程说明",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_process_node_opt_conf(self):
        u"""配置通用节点，操作配置，添加操作，基础运算，添加一个自定义变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
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
                                    ["变量", "时间"]
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置数据拼盘节点，二维表模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘-二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置数据拼盘节点，列更新模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘-列更新模式",
                    "数据拼盘名称": "auto_数据拼盘_列更新模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置数据拼盘节点，分段模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘-分段模式",
                    "数据拼盘名称": "auto_数据拼盘_分段模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个数据拼盘节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置数据拼盘节点，合并模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘节点",
                "业务配置": {
                    "节点名称": "数据拼盘-合并模式",
                    "数据拼盘名称": "auto_数据拼盘_合并模式join",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置数据拼盘节点，应用数据拼盘名称"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "业务配置": {
                    "节点名称": "数据拼盘-二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置数据拼盘节点，取消应用数据拼盘名称"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "auto_数据拼盘_二维表模式",
                "业务配置": {
                    "节点名称": "数据拼盘-二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_business_conf(self):
        u"""配置数据拼盘节点，开启高级模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "业务配置": {
                    "节点名称": "数据拼盘-二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "否",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置数据拼盘节点，关闭高级模式"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "业务配置": {
                    "节点名称": "数据拼盘-二维表模式",
                    "数据拼盘名称": "auto_数据拼盘_二维表模式",
                    "应用数据拼盘名称": "否",
                    "高级配置": {
                        "状态": "关闭"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-原始结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "数据拼盘节点-网元-原始结果",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "数据拼盘节点-网元-解析结果",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "数据拼盘节点-网元-解析结果",
                    "变量名称": "数据拼盘节点-网元-解析结果1",
                    "对象类型": "网元",
                    "结果类型": "解析结果",
                    "指令": "auto_指令_date",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "数据拼盘节点-网元-解析结果1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "数据拼盘节点-网元-解析结果",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_fetch_conf(self):
        u"""节点添加取数配置，变量名已存在"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "数据拼盘节点",
                "节点名称": "数据拼盘-二维表模式",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "数据拼盘节点-网元-解析结果",
                    "对象类型": "网元",
                    "结果类型": "解析结果",
                    "指令": "全部指令",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "该变量已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_line(self):
        u"""节点参数设置连线到节点：数据拼盘-二维表模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "数据拼盘-二维表模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_line(self):
        u"""节点数据拼盘-二维表模"连线到节点：数据拼盘-列更新模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "数据拼盘-二维表模式",
                "终止节点名称": "数据拼盘-列更新模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_line(self):
        u"""节点数据拼盘-列更新模式连线到节点：数据拼盘-分段模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "数据拼盘-列更新模式",
                "终止节点名称": "数据拼盘-分段模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_line(self):
        u"""节点数据拼盘-分段模式连线到节点：数据拼盘-合并模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "数据拼盘-分段模式",
                "终止节点名称": "数据拼盘-合并模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_line(self):
        u"""节点数据拼盘-合并模式连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_数据拼盘节点流程",
                "起始节点名称": "数据拼盘-合并模式",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
