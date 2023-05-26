# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/8 上午10:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CrawlerNodePart5(unittest.TestCase):

    log.info("装载流程可视化操作模拟节点配置测试用例（5）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_144_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加条件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "操作",
                            "右键操作": "添加条件",
                            "条件配置": {
                                "if": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ],
                                "else": "是"
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_145_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "if",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "休眠-不刷新页面",
                                "点击按钮",
                                "表格取数"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_146_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加循环，按变量列表"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "if",
                            "右键操作": "添加循环",
                            "循环配置": {
                                "循环类型": "变量列表",
                                "变量选择": "名字",
                                "循环行变量名称": "loop_a",
                                "赋值方式": "替换"
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_147_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加循环，按次数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "else",
                            "右键操作": "添加循环",
                            "循环配置": {
                                "循环类型": "次数",
                                "循环次数": "3",
                                "循环变量名称": "ki",
                                "赋值方式": "追加",
                                "跳至下一轮条件": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ],
                                "结束循环条件": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ]
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_148_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加循环，按条件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "列表循环",
                            "右键操作": "添加循环",
                            "循环配置": {
                                "循环类型": "条件",
                                "循环条件": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ],
                                "跳至下一轮条件": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ],
                                "结束循环条件": [
                                    ["变量", "时间"],
                                    ["不等于", ""],
                                    ["空值", ""],
                                    ["与", ""],
                                    ["变量", "地点"],
                                    ["包含", ""],
                                    ["自定义值", ["abc ddd"]]
                                ]
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_149_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "条件循环",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "休眠-不刷新页面",
                                "点击按钮",
                                "表格取数"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_150_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加循环，按步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "条件循环",
                            "右键操作": "添加循环",
                            "循环配置": {
                                "循环类型": "步骤",
                                "步骤选择": "表格取数",
                                "循环变量名称": "mi",
                                "赋值方式": "替换"
                            }
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_151_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树删除步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "休眠-不刷新页面",
                            "右键操作": "删除"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_152_process_node_business_conf(self):
        u"""可视化操作模拟节点，元素列表删除被操作数引用的元素"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "元素配置": [
                        {
                            "操作类型": "删除",
                            "目标元素": "点击按钮"
                        }
                    ]
                }
            }
        }
        msg = "业务配置中操作树步骤引用"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_153_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树删除循环"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "条件循环",
                            "右键操作": "删除"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_154_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树删除条件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "if",
                            "右键操作": "删除"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_155_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "操作",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "休眠-不刷新页面",
                                "点击按钮",
                                "表格取数"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_156_process_node_business_conf(self):
        u"""可视化操作模拟节点，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_157_process_node_business_conf(self):
        u"""可视化操作模拟节点，关闭高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "高级配置": {
                        "状态": "关闭"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_158_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "流程-表格取数",
                    "元素名称": "表格取数",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_159_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "流程-表格取数",
                    "变量名": "流程-表格取数1",
                    "元素名称": "表格取数",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_160_process_node_business_conf(self):
        u"""操作树删除步骤，该步骤已被取数配置引用"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "表格取数",
                            "右键操作": "删除"
                        }
                    ]
                }
            }
        }
        msg = "操作步骤被取数配置引用，请及时修改取数配置项"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_161_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "流程-表格取数1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_162_process_node_business_conf(self):
        u"""可视化操作模拟节点，操作树添加步骤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "添加多种动作",
                "业务配置": {
                    "操作树": [
                        {
                            "对象": "操作",
                            "右键操作": "添加步骤",
                            "元素名称": [
                                "表格取数"
                            ]
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_163_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "流程列表",
                    "元素名称": "流程取数",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_164_process_node_fetch_conf(self):
        u"""节点添加取数配置，变量名已存在"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "可视化操作模拟节点",
                "节点名称": "表格取数",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "流程列表",
                    "元素名称": "流程取数",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "该变量已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_165_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_166_process_node_line(self):
        u"""节点参数设置连线到节点：表格取数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "表格取数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_167_process_node_line(self):
        u"""节点表格取数连线到节点：文件下载"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "表格取数",
                "终止节点名称": "文件下载",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_168_process_node_line(self):
        u"""节点文件下载连线到节点：附件上传"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "文件下载",
                "终止节点名称": "附件上传",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_169_process_node_line(self):
        u"""节点附件上传连线到节点：添加多种动作"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "附件上传",
                "终止节点名称": "添加多种动作",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_170_process_node_line(self):
        u"""节点添加多种动作连线到节点：修改元素"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "添加多种动作",
                "终止节点名称": "修改元素",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    @unittest.skip
    def test_171_process_node_line(self):
        u"""节点复制元素连线到节点：修改元素"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "复制元素",
                "终止节点名称": "修改元素",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_172_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_173_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def test_174_process_node_line(self):
        u"""节点修改元素连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_可视化操作模拟节点流程",
                "起始节点名称": "修改元素",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.service.get("ResultMsg"))
        assert gbl.service.get("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = gbl.service.get("browser")
        saveScreenShot()
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
