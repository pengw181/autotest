# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/8 上午10:36

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CrawlerNodePart4(unittest.TestCase):

    log.info("装载流程可视化操作模拟节点配置测试用例（4）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_107_process_node_add(self):
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

    def test_108_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，节点名称：修改元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "可视化操作模拟节点",
                "业务配置": {
                    "节点名称": "修改元素",
                    "目标系统": "auto_第三方系统"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_109_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-修改",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
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

    def test_110_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, ok"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-ok",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "alert",
                            "元素标识": "ok",
                            "描述": "点击按钮动作"
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

    def test_111_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, cancel"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-cancel",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "alert",
                            "元素标识": "cancel",
                            "描述": "点击按钮动作"
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

    def test_112_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, OK"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-点击OK",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "alert",
                            "元素标识": "OK",
                            "描述": "点击按钮动作"
                        }
                    ]
                }
            }
        }
        msg = "元素标识类型为alert时，元素标识只能输入ok或cancel"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_113_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, Cancel"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                       {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-点击Cancel",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "alert",
                            "元素标识": "Cancel",
                            "描述": "点击按钮动作"
                        }
                    ]
                }
            }
        }
        msg = "元素标识类型为alert时，元素标识只能输入ok或cancel"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_114_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, 非ok、cancel"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-点击success",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "alert",
                            "元素标识": "success",
                            "描述": "点击按钮动作"
                        }
                    ]
                }
            }
        }
        msg = "元素标识类型为alert时，元素标识只能输入ok或cancel"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_115_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, 标识类型:class"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-class",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "class",
                            "元素标识": "username",
                            "描述": "点击按钮动作"
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

    def test_116_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，点击按钮, 标识类型:name"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "点击按钮-name",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "name",
                            "元素标识": "btn",
                            "描述": "点击按钮动作"
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

    def test_117_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，输入框输入"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "输入框输入",
                            "元素类型": "输入框",
                            "动作": "输入",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='input']/*[text()='${元素名称}']",
                            "描述": "输入框输入动作",
                            "值输入": "abc",
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

    def test_118_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，输入框输入敏感信息"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "输入框输入敏感信息",
                            "元素类型": "输入框",
                            "动作": "输入",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='input']",
                            "描述": "输入框输入动作",
                            "值输入": "${元素}",
                            "敏感信息": "是"
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

    def test_119_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，文本取数-设置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "文本取数-设置期待值",
                            "元素类型": "文本",
                            "动作": "取数",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='text']",
                            "描述": "文本取数动作",
                            "是否配置期待值": {
                                "状态": "开启",
                                "期待值": "成功_${元素名称}",
                                "尝试次数": "3",
                                "等待时间": "5"
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

    def test_120_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，文本取数-不设置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "文本取数-不设置期待值",
                            "元素类型": "文本",
                            "动作": "取数",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='text']/@name",
                            "描述": "文本取数动作",
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

    def test_121_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，表格取数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "表格取数",
                            "元素类型": "表格",
                            "动作": "取数",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='text']",
                            "描述": "表格取数动作",
                            "取数模式": "追加",
                            "下一页元素标识": "//*[@name='next']",
                            "下一页标识类型": "xpath",
                            "休眠时间": "5",
                            "表格页数": "3",
                            "是否配置期待值": {
                                "状态": "开启",
                                "期待值": "成功",
                                "尝试次数": "3",
                                "等待时间": "5"
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

    @unittest.skip
    def test_122_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，form表单取数，配置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "form表单取数",
                            "元素类型": "表单",
                            "动作": "取数",
                            "标识类型": "id",
                            "元素标识": "login_form",
                            "描述": "form表单取数",
                            "取数模式": "替换",
                            "是否配置期待值": {
                                "状态": "开启",
                                "期待值": "成功",
                                "尝试次数": "3",
                                "等待时间": "5"
                            },
                            "变量名": "form表单取数变量名"
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

    @unittest.skip
    def test_123_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，form表单取数，不配置期待值"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "form表单取数-不配置期待值",
                            "元素类型": "表单",
                            "动作": "取数",
                            "标识类型": "id",
                            "元素标识": "login_form",
                            "描述": "form表单取数-不配置期待值",
                            "取数模式": "替换",
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

    @unittest.skip
    def test_124_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，等待元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "等待元素",
                            "元素类型": "文本",
                            "动作": "等待元素",
                            "等待元素标识类型": "id",
                            "等待元素标识": "userName",
                            "描述": "等待元素",
                            "最大等待时间": "10",
                            "期待值": "成功",
                            "变量名": "等待元素变量名"
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

    def test_125_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-动态生成"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "附件上传-动态生成",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "动态生成",
                                "附件标题": "动态csv",
                                "附件内容": "我们都是中国人",
                                "附件类型": "csv"
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

    def test_126_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-动态生成-变量引用"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "附件上传-动态生成-变量引用",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "动态生成",
                                "附件标题": "${名字}",
                                "附件内容": "${元素}",
                                "附件类型": "csv"
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

    def test_127_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-本地上传"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "附件上传-本地上传",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "本地上传",
                                "附件名称": "factor.xlsx"
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

    def test_128_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-远程加载-本地"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
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
                                "文件名": "test_",
                                "文件类型": "xls"
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

    def test_129_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-远程加载-远程，文件名使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "附件上传-远程加载-远程FTP",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "远程加载",
                                "存储类型": "远程",
                                "远程服务器": "auto_ftp",
                                "目录": "根目录-pw-1",
                                "变量引用": "否",
                                "文件过滤方式": "关键字",
                                "文件名": "test_",
                                "文件类型": "csv"
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

    def test_130_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，附件上传-远程加载-远程，文件名使用正则匹配"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "附件上传-远程加载-远程FTP-正则匹配文件名",
                            "元素类型": "输入框",
                            "动作": "附件上传",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='filebox_file_id_2']",
                            "描述": "附件上传动作",
                            "附件": {
                                "附件来源": "远程加载",
                                "存储类型": "远程",
                                "远程服务器": "auto_ftp",
                                "目录": "根目录-pw-1",
                                "变量引用": "否",
                                "文件过滤方式": "正则匹配",
                                "文件名": {
                                    "设置方式": "添加",
                                    "正则模版名称": "auto_正则模版",
                                    "标签配置": [
                                        {
                                            "标签": "自定义文本",
                                            "自定义值": "pw",
                                            "是否取值": "绿色"
                                        },
                                        {
                                            "标签": "任意字符",
                                            "长度": "1到多个",
                                            "是否取值": "绿色"
                                        }
                                    ]
                                },
                                "文件类型": "csv"
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

    def test_131_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，文件下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "文件下载",
                            "元素类型": "按钮",
                            "动作": "下载",
                            "标识类型": "xpath",
                            "元素标识": "//*[text()='data.xlsx']/../following-sibling::td[2]//a[@funcid='systemFile_down']",
                            "描述": "文件下载动作",
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

    def test_132_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，文件下载，使用url下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "文件下载-url",
                            "元素类型": "按钮",
                            "动作": "下载",
                            "标识类型": "url",
                            "元素标识": "http://192.168.88.116:9200/VisualModeler/VisualModelerHelps/VariableInstruction.pdf",
                            "描述": "文件下载动作",
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

    def test_133_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，文件下载，使用.do下载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "文件下载-do",
                            "元素类型": "按钮",
                            "动作": "下载",
                            "标识类型": "url",
                            "元素标识": "http://192.168.88.116:9200/approval/restful/downloadFile.do?fileId=a641b1d5-7583-4fa9-8086-9c4d1792891d",
                            "描述": "文件下载动作",
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

    def test_134_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，跳转iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "跳转iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "xpath",
                            "元素标识": "//iframe[@src='catalogDefUpload.html']",
                            "描述": "跳转iframe动作"
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

    def test_135_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，跳转iframe，返回上层iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "跳转iframe_返回上层iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "id",
                            "元素标识": "parent",
                            "描述": "跳转iframe动作"
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

    def test_136_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，跳转iframe，返回最外层iframe"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "跳转iframe_返回最外层iframe",
                            "元素类型": "Iframe",
                            "动作": "跳转iframe",
                            "标识类型": "id",
                            "元素标识": "default",
                            "描述": "跳转iframe动作"
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

    def test_137_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，关闭当前窗口"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "关闭当前窗口",
                            "动作": "关闭当前窗口",
                            "描述": "关闭当前窗口动作"
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

    def test_138_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，休眠-刷新页面"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "休眠-刷新页面",
                            "动作": "休眠",
                            "描述": "休眠动作",
                            "循环次数": "3",
                            "_休眠时间": "5",
                            "刷新页面": "是"
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

    def test_139_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，休眠-不刷新页面"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "休眠-不刷新页面",
                            "动作": "休眠",
                            "描述": "休眠动作",
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

    def test_140_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，悬停"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "悬停",
                            "元素类型": "文本",
                            "动作": "悬停",
                            "标识类型": "xpath",
                            "元素标识": "//*[@class='title']",
                            "描述": "悬停动作"
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

    def test_141_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，重复步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "重复步骤",
                            "动作": "重复步骤",
                            "描述": "重复步骤动作",
                            "重复步骤": [
                                "表格取数",
                                "悬停",
                                "文件下载",
                                "输入框输入"
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

    def test_142_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，修改元素，重复步骤，名称已存在"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "修改",
                            "目标元素": "点击按钮",
                            "元素名称": "重复步骤",
                            "动作": "重复步骤",
                            "描述": "重复步骤动作",
                            "重复步骤": [
                                "表格取数",
                                "悬停",
                                "文件下载",
                                "输入框输入"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "元素已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_143_process_node_business_conf(self):
        u"""配置可视化操作模拟节点，删除元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "修改元素",
                "业务配置": {
                    "元素配置": [
                        {
                            "元素名称": "点击按钮",
                            "元素类型": "按钮",
                            "动作": "单击",
                            "标识类型": "xpath",
                            "元素标识": "//*[@id='btn']",
                            "描述": "点击按钮动作"
                        },
                        {
                            "操作类型": "删除",
                            "目标元素": "点击按钮"
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
