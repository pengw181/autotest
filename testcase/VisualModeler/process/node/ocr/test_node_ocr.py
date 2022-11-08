# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/7 下午6:35

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class OcrNode(unittest.TestCase):

    log.info("装载流程OCR节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_OCR节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试OCR节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_OCR节点流程说明",
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
                "流程名称": "auto_OCR节点流程",
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
                "流程名称": "auto_OCR节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，本地目录"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
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
                                    ["自定义值", "/auto_一级目录"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "本地目录"
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
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置OCR节点，普通发票"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "普通发票",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_普通发票",
                        "变量引用": "否"
                    },
                    "启用过滤配置": {
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

    def test_8_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置OCR节点，专用发票"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "专用发票",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_专用发票",
                        "变量引用": "否"
                    },
                    "启用过滤配置": {
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

    def test_10_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置OCR节点，关键字识别图片名"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "关键字识别图片名",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_ocr目录",
                        "变量引用": "否"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "关键字",
                            "文件名": "03",
                            "文件类型": "全部"
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

    def test_12_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置OCR节点，识别jpg"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "识别jpg",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_ocr目录",
                        "变量引用": "否"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "添加",
                                "正则模版名称": "auto_正则模版",
                                "标签配置": [
                                    {
                                        "标签": "数字",
                                        "长度": "1到多个",
                                        "是否取值": "无"
                                    }
                                ]
                            },
                            "文件类型": "jpg"
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

    def test_14_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置OCR节点，识别jpeg"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "识别jpeg",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_ocr目录",
                        "变量引用": "否"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配数字"
                            },
                            "文件类型": "jpeg"
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
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置OCR节点，识别png"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "识别png",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_ocr目录",
                        "变量引用": "否"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "正则匹配",
                            "文件名": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配数字"
                            },
                            "文件类型": "png"
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

    def test_18_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置OCR节点，从远程服务器加载"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "远程加载文件",
                    "存储参数配置": {
                        "存储类型": "远程",
                        "远程服务器": "auto_ftp",
                        "目录": "根目录-pw-ocr",
                        "变量引用": "否"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "关键字",
                            "文件名": "03",
                            "文件类型": "全部"
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

    def test_20_process_node_add(self):
        u"""画流程图，添加一个OCR节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置OCR节点，目录使用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "OCR节点",
                "业务配置": {
                    "节点名称": "目录使用变量",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "${本地目录}",
                        "变量引用": "是"
                    },
                    "启用过滤配置": "开启",
                    "过滤配置": [
                        {
                            "类型": "关键字",
                            "文件名": "03",
                            "文件类型": "全部"
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
        u"""配置OCR节点，关闭过滤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "远程加载文件",
                "业务配置": {
                    "启用过滤配置": "关闭"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_business_conf(self):
        u"""配置OCR节点，开启高级设置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "远程加载文件",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置OCR节点，关闭过滤"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "远程加载文件",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_fetch_conf(self):
        u"""节点添加取数配置，基本信息"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "普通发票_基本信息",
                    "取值类型": "基本信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_fetch_conf(self):
        u"""节点添加取数配置，明细信息"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "普通发票_明细信息",
                    "取值类型": "明细信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "普通发票_基本信息",
                    "变量名": "普通发票_基本信息1",
                    "取值类型": "基本信息",
                    "赋值方式": "追加",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "普通发票_基本信息1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_fetch_conf(self):
        u"""节点普通发票添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "普通发票_基本信息",
                    "取值类型": "基本信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_fetch_conf(self):
        u"""节点普通发票添加取数配置，变量名已存在"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "普通发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "普通发票_基本信息",
                    "取值类型": "基本信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "该变量已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_fetch_conf(self):
        u"""节点专用发票添加取数配置，基本信息"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "专用发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "专用发票_基本信息",
                    "取值类型": "基本信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_fetch_conf(self):
        u"""节点专用发票添加取数配置，明细信息"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "OCR节点",
                "节点名称": "专用发票",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "专用发票_明细信息",
                    "取值类型": "明细信息",
                    "赋值方式": "替换",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
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

    def test_34_process_node_line(self):
        u"""节点参数设置连线到节点：普通发票"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "普通发票",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_line(self):
        u"""节点普通发票连线到节点：专用发票"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "普通发票",
                "终止节点名称": "专用发票",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_line(self):
        u"""节点专用发票连线到节点：关键字识别图片名"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "专用发票",
                "终止节点名称": "关键字识别图片名",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_line(self):
        u"""节点关键字识别图片名连线到节点：识别jpg"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "关键字识别图片名",
                "终止节点名称": "识别jpg",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_line(self):
        u"""节点识别jpg连线到节点：识别jpeg"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "识别jpg",
                "终止节点名称": "识别jpeg",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_line(self):
        u"""节点识别jpeg连线到节点：识别png"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "识别jpeg",
                "终止节点名称": "识别png",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_process_node_line(self):
        u"""节点识别png连线到节点：远程加载文件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "识别png",
                "终止节点名称": "远程加载文件",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_line(self):
        u"""节点远程加载文件连线到节点：目录使用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "远程加载文件",
                "终止节点名称": "目录使用变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_process_node_line(self):
        u"""节点目录使用变量连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_OCR节点流程",
                "起始节点名称": "目录使用变量",
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
