# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/8 上午10:36

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CrawlerNodePart1(unittest.TestCase):

    log.info("装载流程可视化操作模拟节点配置测试用例（1）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试可视化操作模拟节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_可视化操作模拟节点流程说明",
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
                "流程名称": "auto_可视化操作模拟节点流程",
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
                "流程名称": "auto_可视化操作模拟节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，个人目录"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
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
                                    ["自定义值", ["/auto_一级目录"]]
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，元素"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
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
                                    ["自定义值", ["//span[text()='个人目录']"]]
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，元素名称"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
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
                                    ["自定义值", ["常用信息管理"]]
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_add(self):
        u"""画流程图，添加一个可视化操作模拟节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，点击进入领域"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "可视化操作模拟节点",
                "业务配置": {
                    "节点名称": "表格取数",
                    "目标系统": "auto_第三方系统",
                    "元素配置": [
                        {
                            "元素名称": "点击进入领域",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[text()='${Belong}>${Domain}']",
                            "描述": "点击进入领域"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，点击流程编辑器"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击流程编辑器",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//span[text()='流程编辑器']",
                            "描述": "点击流程编辑器"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，点击流程配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击流程配置",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@class='my-menu sub-menu']//span[text()='流程配置']",
                            "描述": "点击流程配置"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "跳转iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "xpath",
                            "元素标识": "//iframe[@src='/VisualModeler/html/gooflow/queryProcessInfo.html']",
                            "描述": "跳转iframe"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，休眠5秒"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "休眠5秒",
                            "动作": "休眠",
                            "描述": "休眠5秒",
                            "循环次数": "1",
                            "_休眠时间": "5",
                            "刷新页面": "否"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，表格取数场景，添加元素，流程取数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "流程取数",
                            "元素类型": "表格",
                            "动作": "取数",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]/table[@class='datagrid-btable']",
                            "描述": "表格取数动作",
                            "取数模式": "替换",
                            "下一页元素标识": "//*[@id='tb']/following-sibling::div[2]//span[@class='l-btn-icon pagination-next']",
                            "下一页标识类型": "xpath",
                            "休眠时间": "5",
                            "表格页数": "3",
                            "是否配置期待值": {
                                "状态": "关闭"
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""可视化操作模拟节点操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "业务配置": {
                    "操作树": [
                         {
                            "对象": "操作",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "点击进入领域",
                                "休眠5秒",
                                "点击流程编辑器",
                                "点击流程配置",
                                "跳转iframe",
                                "休眠5秒",
                                "流程取数"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_add(self):
        u"""画流程图，添加一个可视化操作模拟节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，点击进入领域"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "可视化操作模拟节点",
                "业务配置": {
                    "节点名称": "文件下载",
                    "目标系统": "auto_第三方系统",
                    "元素配置": [
                        {
                            "元素名称": "点击进入领域",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[text()='${Belong}>${Domain}']",
                            "描述": "点击进入领域"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，点击常用信息管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击常用信息管理",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//span[text()='${元素名称}']",
                            "描述": "点击常用信息管理"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，点击文件目录管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击文件目录管理",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//span[text()='文件目录管理']",
                            "描述": "点击文件目录管理"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，点击个人目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击个人目录",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "${元素}",
                            "描述": "点击个人目录"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，单击选择目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "单击选择目录",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']",
                            "描述": "单击选择目录"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "跳转iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "xpath",
                            "元素标识": "//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']",
                            "描述": "跳转iframe"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，输入文件名"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "输入文件名",
                            "元素类型": "输入框",
                            "动作": "输入",
                            "标识类型": "xpath",
                            "元素标识": "//*[@name='fileName']/preceding-sibling::input",
                            "描述": "输入文件名",
                            "值输入": "request.txt",
                            "敏感信息": "否"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，点击查询按钮"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击查询按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='queryBtn']//*[text()='查询']",
                            "描述": "点击查询按钮"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，文件下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "文件下载",
                            "元素类型": "按钮",
                            "动作": "下载",
                            "标识类型": "xpath",
                            "元素标识": "//*[@field='fileName']/*[text()='request.txt']/../following-sibling::td[2]//a[1]",
                            "描述": "文件下载",
                            "下载目录": "auto_一级目录"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，文件下载场景，添加元素，休眠5秒"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "休眠5秒",
                            "动作": "休眠",
                            "描述": "休眠5秒",
                            "循环次数": "1",
                            "_休眠时间": "5",
                            "刷新页面": "否"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""可视化操作模拟节点操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "文件下载",
                "业务配置": {
                    "操作树": [
                         {
                            "对象": "操作",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "点击进入领域",
                                "休眠5秒",
                                "点击常用信息管理",
                                "点击文件目录管理",
                                "点击个人目录",
                                "跳转iframe",
                                "单击选择目录",
                                "输入文件名",
                                "点击查询按钮",
                                "文件下载"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_add(self):
        u"""画流程图，添加一个可视化操作模拟节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击进入领域"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "可视化操作模拟节点",
                "业务配置": {
                    "节点名称": "附件上传",
                    "目标系统": "auto_第三方系统",
                    "元素配置": [
                        {
                            "元素名称": "点击进入领域",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[text()='${Belong}>${Domain}']",
                            "描述": "点击进入领域"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击常用信息管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击常用信息管理",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//span[text()='${元素名称}']",
                            "描述": "点击常用信息管理"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击文件目录管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击文件目录管理",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//span[text()='文件目录管理']",
                            "描述": "点击文件目录管理"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击个人目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击个人目录",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "${元素}",
                            "描述": "点击个人目录"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，单击选择目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "单击选择目录",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[contains(@id,'tree_personal')]/*[@class='tree-title' and text()='auto_一级目录']",
                            "描述": "单击选择目录"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "跳转iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "xpath",
                            "元素标识": "//iframe[@src='/VisualModeler/html/commonInfo/catalogPersonalDef.html']",
                            "描述": "跳转iframe"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击上传文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击上传文件",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='uploadBtn']//span[text()='上传文件']",
                            "描述": "点击上传文件"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，跳转iframe2"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "跳转iframe2",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "xpath",
                            "元素标识": "//iframe[@src='catalogDefUpload.html']",
                            "描述": "跳转iframe2"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，附件上传-远程加载-本地"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "附件上传-远程加载-本地",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "远程加载",
                                "存储类型": "本地",
                                "目录": "auto_一级目录",
                                "变量引用": "否",
                                "文件过滤方式": "关键字",
                                "文件名": "data",
                                "文件类型": "xlsx"
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，休眠5秒"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "休眠5秒",
                            "动作": "休眠",
                            "描述": "休眠5秒",
                            "循环次数": "1",
                            "_休眠时间": "5",
                            "刷新页面": "否"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_business_conf(self):
        u"""可视化操作模拟节点操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "操作树": [
                         {
                            "对象": "操作",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "点击进入领域",
                                "休眠5秒",
                                "点击常用信息管理",
                                "点击文件目录管理",
                                "点击个人目录",
                                "跳转iframe",
                                "单击选择目录",
                                "点击上传文件",
                                "跳转iframe2",
                                "附件上传-远程加载-本地"
                            ]
                        }
                    ]
                }
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
