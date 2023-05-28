# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/1 下午9:53

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class FileNode(unittest.TestCase):

    log.info("装载流程文件存储配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_文件存储"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试文件节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称":  "auto_流程_文件存储",
                "专业领域":  ["AiSee", "auto域"],
                "流程类型":  "主流程",
                "流程说明":  "auto_流程_文件存储说明"
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
                "流程名称": "auto_流程_文件存储",
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
                "流程名称": "auto_流程_文件存储",
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
                "流程名称": "auto_流程_文件存储",
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

    def test_6_process_node_opt_conf(self):
        u"""配置通用节点，添加一个变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
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
                                    ["自定义值", ["auto_一级目录/auto_二级目录"]]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "目录变量"
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

    def test_7_process_node_add(self):
        u"""画流程图，添加一个指令节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "指令节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置指令节点，多指令"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
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
                            },
                            "auto_指令_ping": {
                                "解析模版": "auto_解析模板_解析ping"
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

    def test_9_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-解析结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "指令节点",
                "节点名称": "执行指令获取变量内容",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元解析结果",
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

    def test_10_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-格式化二维表结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
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

    def test_11_process_node_fetch_conf(self):
        u"""节点添加取数配置，网元-原始结果"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "指令节点",
                "节点名称": "执行指令获取变量内容",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "网元原始结果",
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

    def test_12_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置文件节点，文件存储，文件类型txt"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "存储指令结果",
                    "操作模式": "文件存储",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_二级目录",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "变量": "网元解析结果",
                            "文件名": "网元解析结果",
                            "文件类型": "txt",
                            "编码格式": "GBK",
                            "分隔符": ",",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""配置文件节点，文件存储，文件类型csv"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元二维表结果",
                            "文件名": "网元二维表结果",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "分隔符": ",",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""配置文件节点，文件存储，多个变量写入到同一个csv里"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元解析结果",
                            "文件名": "网元二维表结果",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "分隔符": ",",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""配置文件节点，文件存储，文件类型xls"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元原始结果",
                            "文件名": "网元原始结果",
                            "文件类型": "xls",
                            "编码格式": "UTF-8",
                            "sheet名称": "",
                            "时间前缀": "否",
                            "时间后缀": "是",
                            "时间格式": "yyyy-MM-dd"
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
        u"""配置文件节点，文件存储，文件类型xlsx"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元原始结果",
                            "文件名": "网元原始结果",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet名称": "网元原始结果",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""配置文件节点，文件存储，多个变量写到同一个xlsx"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元解析结果",
                            "文件名": "网元原始结果",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet名称": "网元原始结果",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""配置文件节点，文件存储，文件类型pdf"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "存储指令结果",
                "业务配置": {
                    "文件配置": [
                        {
                            "变量": "网元原始结果",
                            "文件名": "网元原始结果",
                            "文件类型": "pdf",
                            "编码格式": "UTF-8",
                            "时间前缀": "否",
                            "时间后缀": "否"
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
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置文件节点，文件存储，存储到远程ftp服务器"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "指令结果存储到ftp",
                    "操作模式": "文件存储",
                    "存储参数配置": {
                        "存储类型": "远程",
                        "远程服务器": "auto_ftp",
                        "目录": "根目录-pw-1",
                        "变量引用": "否"
                    },
                    "文件配置": [
                        {
                            "变量": "网元原始结果",
                            "文件名": "网元原始结果",
                            "文件类型": "txt",
                            "编码格式": "GBK",
                            "分隔符": ",",
                            "时间前缀": "否",
                            "时间后缀": "否"
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

    def test_22_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置文件节点，文件存储，存储到本地，目录使用变量引用"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "文件存储到个人目录",
                    "操作模式": "文件存储",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "${目录变量}",
                        "变量引用": "是"
                    },
                    "文件配置": [
                        {
                            "变量": "网元解析结果",
                            "文件名": "网元解析结果2",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet名称": "",
                            "时间前缀": "否",
                            "时间后缀": "否"
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

    def test_24_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
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

    def test_25_process_node_line(self):
        u"""节点参数设置连线到节点：执行指令获取变量内容"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "起始节点名称": "参数设置",
                "终止节点名称": "执行指令获取变量内容",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_node_line(self):
        u"""节点执行指令获取变量内容连线到节点：存储指令结果"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "起始节点名称": "执行指令获取变量内容",
                "终止节点名称": "存储指令结果",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_node_line(self):
        u"""节点存储指令结果连线到节点：指令结果存储到ftp"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "起始节点名称": "存储指令结果",
                "终止节点名称": "指令结果存储到ftp",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_node_line(self):
        u"""节点指令结果存储到ftp连线到节点：文件存储到个人目录"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "起始节点名称": "指令结果存储到ftp",
                "终止节点名称": "文件存储到个人目录",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_node_line(self):
        u"""节点文件存储到个人目录连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "起始节点名称": "文件存储到个人目录",
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
