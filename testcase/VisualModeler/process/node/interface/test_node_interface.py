# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/6 下午5:07

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class InterfaceNode(unittest.TestCase):

    log.info("装载流程接口节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_接口节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试接口节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_接口节点流程说明",
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
                "流程名称": "auto_接口节点流程",
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
                "流程名称": "auto_接口节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，自定义文本"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
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
                                    ["自定义值", ["hello"]]
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

    def test_6_process_node_opt_conf(self):
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量，内置变量，时间变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
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
                                    ["变量", {
                                        "变量名称": "时间变量",
                                        "时间格式": "yyyyMMddHHmmss",
                                        "间隔": "0",
                                        "单位": "日",
                                        "语言": "中文"
                                    }]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "当前时间"
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

    def test_7_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置接口节点，webservice接口"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "webservice接口",
                    "接口": "auto_用户密码期限检测"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置接口节点，restful接口，请求方式post"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "post请求",
                    "接口": "auto_万能mock_post",
                    "请求体内容": [
                        {
                            "类型": "自定义值",
                            "自定义值": "请求体："
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "当前时间"
                        }
                    ],
                    "请求头列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "时间"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "2020-10-20 10:00:00"
                        },
                        "param3": {
                            "设置方式": "固定值",
                            "参数值": "hello world"
                        }
                    },
                    "参数列表": {
                        "name": {
                            "设置方式": "变量",
                            "参数值": "名字"
                        },
                        "age": {
                            "设置方式": "固定值",
                            "参数值": "18"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置接口节点，restful接口，请求方式get"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "get请求",
                    "接口": "auto_万能mock_get",
                    "请求体内容": [
                        {
                            "类型": "自定义值",
                            "自定义值": "请求体："
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "当前时间"
                        }
                    ],
                    "请求头列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "时间"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "2020-10-20 10:00:00"
                        }
                    },
                    "参数列表": {
                        "name": {
                            "设置方式": "变量",
                            "参数值": "名字"
                        },
                        "age": {
                            "设置方式": "固定值",
                            "参数值": "18"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置接口节点，restful接口，请求方式put"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "put请求",
                    "接口": "auto_万能mock_put",
                    "请求体内容": [
                        {
                            "类型": "自定义值",
                            "自定义值": "请求体："
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "当前时间"
                        }
                    ],
                    "请求头列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "时间"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "2020-10-20 10:00:00"
                        }
                    },
                    "参数列表": {
                        "age": {
                            "设置方式": "固定值",
                            "参数值": "18"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_business_conf(self):
        u"""配置接口节点，restful接口，请求方式delete"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "delete请求",
                    "接口": "auto_万能mock_delete",
                    "请求体内容": [
                        {
                            "类型": "自定义值",
                            "自定义值": "请求体："
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "当前时间"
                        }
                    ],
                    "请求头列表": {
                        "param1": {
                            "设置方式": "变量",
                            "参数值": "时间"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "2020-10-20 10:00:00"
                        }
                    },
                    "参数列表": {
                        "name": {
                            "设置方式": "变量",
                            "参数值": "名字"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置接口节点，soap接口"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "soap接口",
                    "接口": "auto_第三方soap接口"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置接口节点，修改请求体"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "post请求",
                "业务配置": {
                    "请求体内容": [
                        {
                            "类型": "自定义值",
                            "自定义值": "请求体："
                        },
                        {
                            "类型": "快捷键",
                            "快捷键": "换行"
                        },
                        {
                            "类型": "变量",
                            "变量分类": "自定义变量",
                            "变量名": "当前时间"
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
        u"""配置接口节点，修改请求头参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "post请求",
                "业务配置": {
                    "请求头列表": {
                        "param1": {
                            "设置方式": "固定值",
                            "参数值": "2020"
                        },
                        "param2": {
                            "设置方式": "固定值",
                            "参数值": "你好"
                        },
                        "param3": {
                            "设置方式": "变量",
                            "参数值": "地点"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_business_conf(self):
        u"""配置接口节点，修改接口参数"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "post请求",
                "业务配置": {
                    "参数列表": {
                        "name": {
                            "设置方式": "固定值",
                            "参数值": "kk"
                        },
                        "age": {
                            "设置方式": "固定值",
                            "参数值": "20"
                        }
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置接口节点，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "post请求",
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

    def test_23_process_node_business_conf(self):
        u"""配置接口节点，关闭高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "post请求",
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

    def test_24_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置接口节点，restful接口_notify"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "restful接口_notify",
                    "接口": "auto_第三方restful接口_notify"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_fetch_conf(self):
        u"""节点添加取数配置，返回内容为json，取完整内容"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "webservice接口",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "webservice接口返回",
                    "表达式": "$",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_fetch_conf(self):
        u"""节点添加取数配置，返回内容为json，解析json"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "webservice接口",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "webservice接口返回msg",
                    "表达式": "$.msg",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_fetch_conf(self):
        u"""节点添加取数配置，返回内容为xml，取完整内容"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "soap接口",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "soap接口返回",
                    "表达式": "$",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "webservice接口",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "webservice接口返回msg",
                    "变量名称": "webservice接口返回msg2",
                    "表达式": "$.msg",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "webservice接口",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "webservice接口返回msg2"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "webservice接口",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "webservice接口返回time",
                    "表达式": "$.time",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_fetch_conf(self):
        u"""节点添加取数配置，返回内容为字符串"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "接口节点",
                "节点名称": "restful接口_notify",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "restful接口_notify返回",
                    "赋值方式": "替换"
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
                "流程名称": "auto_接口节点流程",
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
        u"""节点参数设置连线到节点：webservice接口"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "webservice接口",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_line(self):
        u"""节点webservice接口连线到节点：post请求"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "webservice接口",
                "终止节点名称": "post请求",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_line(self):
        u"""节点post请求连线到节点：get请求"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "post请求",
                "终止节点名称": "get请求",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_line(self):
        u"""节点get请求连线到节点：put请求"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "get请求",
                "终止节点名称": "put请求",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_line(self):
        u"""节点put请求连线到节点：delete请求"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "put请求",
                "终止节点名称": "delete请求",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_line(self):
        u"""节点delete请求连线到节点：soap接口"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "delete请求",
                "终止节点名称": "soap接口",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_process_node_line(self):
        u"""节点soap接口连线到节点：restful接口_notify"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "soap接口",
                "终止节点名称": "restful接口_notify",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_process_node_line(self):
        u"""节点restful接口_notify连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_接口节点流程",
                "起始节点名称": "restful接口_notify",
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
