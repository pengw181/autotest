# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/8 上午10:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CrawlerNode(unittest.TestCase):

    log.info("装载流程爬虫节点文件上传配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试可视化操作模拟节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_流程_爬虫文件上传流程说明"
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
                "流程名称": "auto_流程_爬虫文件上传",
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
                "流程名称": "auto_流程_爬虫文件上传",
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
        u"""通用节点，添加一个自定义变量，个人目录"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_node_opt_conf(self):
        u"""通用节点，添加一个自定义变量，元素"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_node_opt_conf(self):
        u"""通用节点，添加一个自定义变量，元素名称"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_node_add(self):
        u"""画流程图，添加一个可视化操作模拟节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "节点类型": "可视化操作模拟节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击进入领域"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击常用信息管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击文件目录管理"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击个人目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，单击选择目录"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，点击上传文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "附件上传",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击上传文件",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='uploadBtn']",
                            "描述": "点击上传文件"
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
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，跳转iframe2"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，附件上传-远程加载-本地"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，附件上传场景，添加元素，休眠5秒"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""可视化操作模拟节点操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
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

    def test_21_process_node_line(self):
        u"""节点参数设置连线到节点：附件上传"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "起始节点名称": "参数设置",
                "终止节点名称": "附件上传",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_line(self):
        u"""节点附件上传连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "起始节点名称": "附件上传",
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
