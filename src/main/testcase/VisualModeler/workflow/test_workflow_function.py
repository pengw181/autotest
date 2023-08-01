# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/5 上午11:39

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class WorkFlowNodeFunction(unittest.TestCase):

    log.info("装载流程函数功能测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_函数计算"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_流程_函数计算说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：绝对值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载函数测试数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_一级目录",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "1",
                            "变量": "绝对值",
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

    def test_5_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：时间转换"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "2",
                            "变量": "时间转换",
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

    def test_6_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：十转十六"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "3",
                            "变量": "十转十六",
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

    def test_7_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：十六转十"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "4",
                            "变量": "十六转十",
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

    def test_8_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：科学计数法"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "5",
                            "变量": "科学计数法",
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

    def test_9_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：科学计数转普通数字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "6",
                            "变量": "科学计数转普通数字",
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

    def test_10_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：字符串替换"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "7",
                            "变量": "字符串替换",
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

    def test_11_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：取小数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "8",
                            "变量": "取小数",
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

    def test_12_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：字符串转数字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "9",
                            "变量": "字符串转数字",
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

    def test_13_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：字符串截取"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "10",
                            "变量": "字符串截取",
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

    def test_14_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：数组转字符串"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "11",
                            "变量": "数组转字符串",
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

    def test_15_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：去重"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "12",
                            "变量": "去重",
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

    def test_16_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：转置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "13",
                            "变量": "转置",
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

    def test_17_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：拆分"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "14",
                            "变量": "拆分",
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

    def test_18_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载函数测试数据：去空格"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "函数",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "sheet页索引": "15",
                            "变量": "去空格",
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

    def test_19_process_node_business_conf(self):
        u"""配置文件节点，文件加载，从本地加载文本文件：清洗日志"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "文件节点",
                "节点名称": "加载函数测试数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "清洗日志",
                            "文件类型": "txt",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "分隔符": "",
                            "变量": "清洗日志",
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

    def test_20_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置指令节点，date指令"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "指令节点",
                "节点名称": "指令节点",
                "业务配置": {
                    "节点名称": "执行指令获取变量内容",
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
                            "auto_指令_date": {
                                "解析模版": "auto_解析模板_解析date"
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

    def test_22_process_node_fetch_conf(self):
        u"""节点添加取数配置，格式化二维表结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "指令节点",
                "节点名称": "执行指令获取变量内容",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元格式化二维表结果",
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

    def test_23_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_测试流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "函数计算",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_node_opt_conf(self):
        u"""操作配置，添加函数，取绝对值"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "绝对值",
                                        "数组索引": "1,3",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "取绝对值"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-取绝对值"
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

    def test_26_process_node_opt_conf(self):
        u"""操作配置，添加函数，时间处理"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "时间转换",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "时间处理",
                                                "时间格式": "yyyyMMddHHmmss",
                                                "间隔": "-1",
                                                "单位": "日",
                                                "语言": "中文"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-时间处理"
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

    def test_27_process_node_opt_conf(self):
        u"""操作配置，添加函数，10进制转16进制"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "十转十六",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "10进制转16进制"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-10进制转16进制"
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
        u"""操作配置，添加函数，16进制转10进制"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "十六转十",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "16进制转10进制"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-16进制转10进制"
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

    def test_29_process_node_opt_conf(self):
        u"""操作配置，添加函数，科学计算"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "科学计数法",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "科学计算"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-科学计算"
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

    def test_30_process_node_opt_conf(self):
        u"""操作配置，添加函数，科学计数法转普通数字"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "科学计数转普通数字",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "科学计数法转普通数字"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-科学计数法转普通数字"
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

    def test_31_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符替换，替换所有"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串替换",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符替换",
                                                "正则匹配": "否",
                                                "查找内容": "qaq",
                                                "替换": "nice",
                                                "方式": "替换所有"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符替换"
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

    def test_32_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符替换，替换一次"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串替换",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符替换",
                                                "正则匹配": "否",
                                                "查找内容": "qaq",
                                                "替换": "nice",
                                                "方式": "替换一次"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符替换-替换一次"
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

    def test_33_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符替换，使用正则匹配"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串替换",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符替换",
                                                "正则匹配": "是",
                                                "查找内容": {
                                                    "设置方式": "添加",
                                                    "正则模版名称": "auto_正则模版",
                                                    "标签配置": [
                                                        {
                                                            "标签": "字母",
                                                            "长度": "1到多个",
                                                            "是否取值": "无"
                                                        }
                                                    ]
                                                },
                                                "替换": "regex",
                                                "方式": "替换所有"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符替换-使用正则"
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

    def test_34_process_node_opt_conf(self):
        u"""操作配置，添加函数，取小数位数"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "取小数",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "取小数位数",
                                                "小数位数": "2",
                                                "使用千分位分隔符": "是"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-取小数位数"
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

    def test_35_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符串转数字"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串转数字",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符串转数字"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符串转数字"
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

    def test_36_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符串截取，截取中间范围"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串截取",
                                        "数组索引": "1",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符串截取",
                                                "开始": "1",
                                                "结束": "5"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符串截取"
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

    def test_37_process_node_opt_conf(self):
        u"""操作配置，添加函数，字符串截取，剔除首字符"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "字符串截取",
                                        "数组索引": "1",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "字符串截取",
                                                "开始": "1",
                                                "结束": "*"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-字符串截取-剔除首字符"
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

    def test_38_process_node_opt_conf(self):
        u"""操作配置，添加函数，数组转字符串"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "数组转字符串",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "数组转字符串",
                                                "分隔符": ","
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-数组转字符串"
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

    def test_39_process_node_opt_conf(self):
        u"""操作配置，添加函数，去重"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "去重",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "去重"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-去重"
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

    def test_40_process_node_opt_conf(self):
        u"""操作配置，添加函数，转置"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "转置",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "转置"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-转置"
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

    def test_41_process_node_opt_conf(self):
        u"""操作配置，添加函数，去空格"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "去空格",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "去空格"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-去空格"
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

    def test_42_process_node_opt_conf(self):
        u"""操作配置，添加函数，长度"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "清洗日志",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "长度"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-长度"
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

    def test_43_process_node_opt_conf(self):
        u"""操作配置，添加函数，拆分，按文本拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "拆分",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "拆分",
                                                "拆分方式": "文本",
                                                "分隔符": ","
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-文本拆分"
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

    def test_44_process_node_opt_conf(self):
        u"""操作配置，添加函数，拆分，按正则拆分"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "函数计算",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "清洗日志",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "拆分",
                                                "拆分方式": "正则",
                                                "分隔符": {
                                                    "设置方式": "选择",
                                                    "正则模版名称": "auto_正则模版_横杠拆分符"
                                                }
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-正则拆分"
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

    def test_45_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "指令结果处理",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_opt_conf(self):
        u"""通用节点，控制配置，添加循环"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "指令结果处理",
                "控制配置": {
                    "开启循环": {
                        "状态": "开启",
                        "循环条件": ["操作配置"],
                        "循环类型": "变量列表",
                        "循环内容": {
                            "模式": "便捷模式",
                            "变量类型": "指令输出变量",
                            "变量名称": "网元格式化二维表结果"
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

    def test_48_process_node_opt_conf(self):
        u"""通用节点，操作配置，取table_format"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "指令结果处理",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["变量", "tableFormat_网元格式化二维表结果"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "table_format"
                                },
                                "输出列": "3",
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

    def test_49_process_node_opt_conf(self):
        u"""操作配置，添加函数，数组格式化"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "指令结果处理",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "table_format",
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

    def test_50_process_node_opt_conf(self):
        u"""通用节点，操作配置，结果整合"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "指令结果处理",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["变量", "netunitName_网元格式化二维表结果"],
                                    ["拼列", ""],
                                    ["变量", "table_format"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "网元数组格式化结果"
                                },
                                "输出列": "*",
                                "赋值方式": "追加",
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

    def test_51_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "获取网元属性",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_opt_conf(self):
        u"""配置通用节点，添加一个变量，单网元名称"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "获取网元属性",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["自定义值", ["${NetunitMME1}"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "单网元名称"
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

    def test_54_process_node_opt_conf(self):
        u"""配置通用节点，添加一个变量，网元名称列表"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "获取网元属性",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["自定义值", ["${NetunitMME1}"]],
                                    ["并集", ""],
                                    ["自定义值", ["${NetunitMME2}"]],
                                    ["并集", ""],
                                    ["自定义值", ["${NetunitMME3}"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "网元名称列表"
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

    def test_55_process_node_opt_conf(self):
        u"""操作配置，添加函数，获取网元属性，单网元名称"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "获取网元属性",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "单网元名称",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "获取网元属性",
                                                "网元列": "1"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-获取网元属性-单网元"
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

    def test_56_process_node_opt_conf(self):
        u"""操作配置，添加函数，获取网元属性，网元名称列表"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "获取网元属性",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "网元名称列表",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "获取网元属性",
                                                "网元列": "1"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-获取网元属性-网元列表"
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

    def test_57_process_node_opt_conf(self):
        u"""操作配置，添加函数，获取网元属性，网元格式化二维表结果"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "通用节点",
                "节点名称": "获取网元属性",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "基础运算",
                            "配置": {
                                "表达式": [
                                    ["函数", {
                                        "输入变量": "网元格式化二维表结果",
                                        "数组索引": "",
                                        "函数处理列表": [
                                            {
                                                "动作": "添加",
                                                "函数": "获取网元属性",
                                                "网元列": "2"
                                            }
                                        ]
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "普通运算函数结果-获取网元属性-网元格式化二维表结果"
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

    def test_58_process_node_line(self):
        u"""开始节点连线到节点：加载函数测试数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "开始",
                "终止节点名称": "加载函数测试数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_process_node_line(self):
        u"""节点加载函数测试数据连线到节点：执行指令获取变量内容"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "加载函数测试数据",
                "终止节点名称": "执行指令获取变量内容",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_process_node_line(self):
        u"""节点执行指令获取变量内容连线到节点：函数计算"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "执行指令获取变量内容",
                "终止节点名称": "函数计算",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_process_node_line(self):
        u"""节点函数计算连线到节点：指令结果处理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "函数计算",
                "终止节点名称": "指令结果处理",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_line(self):
        u"""节点指令结果处理连线到节点：获取网元属性"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "指令结果处理",
                "终止节点名称": "获取网元属性",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_65_process_node_line(self):
        u"""节点获取网元属性连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "起始节点名称": "获取网元属性",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_函数计算"
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
