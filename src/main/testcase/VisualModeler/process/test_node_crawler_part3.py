# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/8 上午10:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CrawlerNodePart3(unittest.TestCase):

    log.info("装载流程可视化操作模拟节点配置测试用例（3）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    @unittest.skip
    def test_74_process_node_add(self):
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    @unittest.skip
    def test_75_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "可视化操作模拟节点",
                "业务配置": {
                    "节点名称": "复制元素",
                    "目标系统": "auto_第三方系统"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    @unittest.skip
    def test_76_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，点击按钮"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "点击按钮",
                            "元素名称": "点击按钮_复制"
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

    @unittest.skip
    def test_77_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，点击按钮-ok"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "点击按钮-ok",
                            "元素名称": "点击按钮-ok_复制"
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

    @unittest.skip
    def test_78_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，点击按钮-cancel"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "点击按钮-cancel",
                            "元素名称": "点击按钮-cancel_复制"
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

    @unittest.skip
    def test_79_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，点击按钮-class"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "点击按钮-class",
                            "元素名称": "点击按钮-class_复制"
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

    @unittest.skip
    def test_80_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，点击按钮-name"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "点击按钮-name",
                            "元素名称": "点击按钮-name_复制"
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

    @unittest.skip
    def test_81_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，输入框输入"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "输入框输入",
                            "元素名称": "输入框输入_复制"
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

    @unittest.skip
    def test_82_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，输入框输入敏感信息"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "输入框输入敏感信息",
                            "元素名称": "输入框输入敏感信息_复制"
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

    @unittest.skip
    def test_83_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，文本取数-设置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "文本取数-设置期待值",
                            "元素名称": "文本取数-设置期待值_复制"
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

    @unittest.skip
    def test_84_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，文本取数-不设置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "文本取数-不设置期待值",
                            "元素名称": "文本取数-不设置期待值_复制"
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

    @unittest.skip
    def test_85_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，表格取数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "表格取数",
                            "元素名称": "表格取数_复制"
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

    @unittest.skip
    def test_86_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，form表单取数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "form表单取数",
                            "元素名称": "form表单取数_复制"
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

    @unittest.skip
    def test_87_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，form表单取数-不配置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "form表单取数-不配置期待值",
                            "元素名称": "form表单取数-不配置期待值_复制"
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

    @unittest.skip
    def test_88_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，等待元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "等待元素",
                            "元素名称": "等待元素_复制"
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

    @unittest.skip
    def test_89_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-动态生成"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-动态生成",
                            "元素名称": "附件上传-动态生成_复制"
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

    @unittest.skip
    def test_90_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-动态生成-变量引用"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-动态生成-变量引用",
                            "元素名称": "附件上传-动态生成-变量引用_复制"
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

    @unittest.skip
    def test_91_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-本地上传"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-本地上传",
                            "元素名称": "附件上传-本地上传_复制"
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

    @unittest.skip
    def test_92_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-远程加载-本地"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-远程加载-本地",
                            "元素名称": "附件上传-远程加载-本地_复制"
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

    @unittest.skip
    def test_93_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-远程加载-远程FTP"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-远程加载-远程FTP",
                            "元素名称": "附件上传-远程加载-远程FTP_复制"
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

    @unittest.skip
    def test_94_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，附件上传-远程加载-远程FTP-正则匹配文件名"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "附件上传-远程加载-远程FTP-正则匹配文件名",
                            "元素名称": "附件上传-远程加载-远程FTP-正则匹配文件名_复制"
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

    @unittest.skip
    def test_95_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，文件下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "文件下载",
                            "元素名称": "文件下载_复制"
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

    @unittest.skip
    def test_96_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，文件下载-url"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "文件下载-url",
                            "元素名称": "文件下载-url_复制"
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

    @unittest.skip
    def test_97_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，文件下载-do"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "文件下载-do",
                            "元素名称": "文件下载-do_复制"
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

    @unittest.skip
    def test_98_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，关闭当前窗口"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "关闭当前窗口",
                            "元素名称": "关闭当前窗口_复制"
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

    @unittest.skip
    def test_99_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "跳转iframe",
                            "元素名称": "跳转iframe_复制"
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

    @unittest.skip
    def test_100_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，跳转iframe，返回上层iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "跳转iframe_返回上层iframe",
                            "元素名称": "跳转iframe_返回上层iframe_复制"
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

    @unittest.skip
    def test_101_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，跳转iframe，返回最外层iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "跳转iframe_返回最外层iframe",
                            "元素名称": "跳转iframe_返回最外层iframe_复制"
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

    @unittest.skip
    def test_102_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，休眠-刷新页面"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "休眠-刷新页面",
                            "元素名称": "休眠-刷新页面_复制"
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

    @unittest.skip
    def test_103_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，休眠-不刷新页面"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "休眠-不刷新页面",
                            "元素名称": "休眠-不刷新页面_复制"
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

    @unittest.skip
    def test_104_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，悬停"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "悬停",
                            "元素名称": "悬停_复制"
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

    @unittest.skip
    def test_105_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，重复步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "重复步骤",
                            "元素名称": "重复步骤_复制"
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

    @unittest.skip
    def test_106_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：复制元素，元素名称已存在"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "复制元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "复制",
                            "节点名称": "添加多种动作",
                            "复制元素": "重复步骤",
                            "元素名称": "重复步骤_复制"
                        }
                    ]
                }
            }
        }
        msg = "元素已存在"
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
