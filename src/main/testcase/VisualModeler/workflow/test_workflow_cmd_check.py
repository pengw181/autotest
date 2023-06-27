# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 上午11:55

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CmdNode(unittest.TestCase):

    log.info("装载流程指令系统检查测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_指令系统检查"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试指令节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_指令系统检查",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_指令系统检查说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置指令节点，服务器磁盘利用率检查"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "服务器磁盘利用率检查",
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
                            "auto_指令_磁盘利用率检查": {
                                "解析模版": "auto_解析模板_服务器磁盘利用率检查"
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

    def test_5_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_node_business_conf(self):
        u"""配置指令节点，查看Slab"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "查看Slab",
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
                            "auto_指令_查看Slab": {
                                "解析模版": "auto_解析模板_查看Slab解析"
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

    def test_7_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置指令节点，内存利用率检查"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "内存利用率检查",
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
                            "auto_指令_内存利用率检查": {
                                "解析模版": "auto_解析模板_内存利用率解析"
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

    def test_9_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置指令节点，服务器性能检测Top"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "服务器性能检测Top",
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
                            "auto_指令_服务器性能检测Top": {
                                "解析模版": "auto_解析模板_cpu利用率检查"
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

    def test_11_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置指令节点，服务器负载检查"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "服务器负载检查",
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
                            "auto_指令_服务器负载检查": {
                                "解析模版": "auto_解析模板_服务器负载检查"
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

    def test_13_process_node_fetch_conf(self):
        u"""节点添加取数配置，服务器磁盘利用率检查结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "服务器磁盘利用率检查",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "服务器磁盘利用率检查结果",
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

    def test_14_process_node_fetch_conf(self):
        u"""节点添加取数配置，查看Slab结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "查看Slab",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "查看Slab结果",
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
        u"""节点添加取数配置，内存利用率检查结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "内存利用率检查",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "内存利用率检查结果",
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

    def test_16_process_node_fetch_conf(self):
        u"""节点添加取数配置，服务器性能检测Top结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "服务器性能检测Top",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "服务器性能检测Top结果",
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

    def test_17_process_node_fetch_conf(self):
        u"""节点添加取数配置，服务器负载检查结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "指令节点",
                "节点名称": "服务器负载检查",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "服务器负载检查结果",
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

    def test_18_process_node_line(self):
        u"""开始节点连线到节点：服务器磁盘利用率检查"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "开始",
                "终止节点名称": "服务器磁盘利用率检查",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_line(self):
        u"""节点服务器磁盘利用率检查连线到节点：指令不带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "服务器磁盘利用率检查",
                "终止节点名称": "查看Slab",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_line(self):
        u"""节点查看Slab连线到节点：内存利用率检查"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "查看Slab",
                "终止节点名称": "内存利用率检查",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_line(self):
        u"""节点内存利用率检查连线到节点：服务器性能检测Top"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "内存利用率检查",
                "终止节点名称": "服务器性能检测Top",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_line(self):
        u"""节点服务器性能检测Top连线到节点：服务器负载检查"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "服务器性能检测Top",
                "终止节点名称": "服务器负载检查",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_line(self):
        u"""节点服务器负载检查连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "起始节点名称": "服务器负载检查",
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
