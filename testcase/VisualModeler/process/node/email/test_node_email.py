# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/6 下午6:16

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class EmailNode(unittest.TestCase):

    log.info("装载流程邮件节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_邮件节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试邮件节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_邮件节点流程说明",
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
                "流程名称": "auto_邮件节点流程",
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
                "流程名称": "auto_邮件节点流程",
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
        u"""通用节点，操作配置，添加操作，基础运算，添加一个自定义变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
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
                                    ["变量", "时间"]
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

    def test_6_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，收件人从列表选择"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送,收件人从列表选择",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com", "auto_test@henghaodata.com"]
                        },
                        "标题": "测试邮件",
                        "正文": [
                            {
                                "类型": "自定义值",
                                "自定义值": "地点:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "流程定义变量",
                                "变量名": "地点"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "流程实例id:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "系统内置变量",
                                "变量名": "流程实例ID"
                            }
                        ]
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，收件人为变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送,收件人为变量",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "变量",
                            "值": "地点"
                        },
                        "标题": "测试邮件",
                        "正文": [
                            {
                                "类型": "自定义值",
                                "自定义值": "地点:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "流程定义变量",
                                "变量名": "地点"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "流程实例id:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "系统内置变量",
                                "变量名": "流程实例ID"
                            }
                        ]
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
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，抄送人从列表选择"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送,抄送人从列表选择",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com", "auto_test@henghaodata.com"]
                        },
                        "抄送人": {
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com", "auto_test@henghaodata.com"]
                        },
                        "标题": "测试邮件",
                        "正文": [
                            {
                                "类型": "自定义值",
                                "自定义值": "地点:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "流程定义变量",
                                "变量名": "地点"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "流程实例id:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "系统内置变量",
                                "变量名": "流程实例ID"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，抄送人为变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送,抄送人为变量",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com", "auto_test@henghaodata.com"]
                        },
                        "抄送人": {
                            "方式": "变量",
                            "值": "时间"
                        },
                        "标题": "测试邮件",
                        "正文": [
                            {
                                "类型": "自定义值",
                                "自定义值": "地点:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "流程定义变量",
                                "变量名": "地点"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "流程实例id:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "系统内置变量",
                                "变量名": "流程实例ID"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，标题引用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件发送,标题引用变量",
                    "邮件模式": "发送",
                    "参数配置": {
                        "发件人": "pw@henghaodata.com",
                        "收件人": {
                            "类型": "自定义",
                            "方式": "请选择",
                            "值": ["pw@henghaodata.com", "auto_test@henghaodata.com"]
                        },
                        "抄送人": {
                            "方式": "变量",
                            "值": "时间"
                        },
                        "标题": "测试邮件_${参数1}_${时间}",
                        "正文": [
                            {
                                "类型": "变量",
                                "变量分类": "自定义变量",
                                "变量名": "参数1"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "流程定义变量",
                                "变量名": "地点"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "自定义值",
                                "自定义值": "流程实例id:"
                            },
                            {
                                "类型": "快捷键",
                                "快捷键": "换行"
                            },
                            {
                                "类型": "变量",
                                "变量分类": "系统内置变量",
                                "变量名": "流程实例ID"
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，携带附件，动态生成"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送,收件人从列表选择",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "动态生成",
                                    "附件标题": "动态生成标题",
                                    "附件内容": "动态生成内容",
                                    "附件类型": "csv"
                                }
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，携带附件，本地上传"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送,收件人从列表选择",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "本地上传",
                                    "文件名": "factor.xlsx"
                                }
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，携带附件，远程加载，本地文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送,收件人从列表选择",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "远程加载",
                                    "存储类型": "本地",
                                    "变量引用": "否",
                                    "目录": "auto_一级目录",
                                    "过滤类型": "关键字",
                                    "文件名": "加载文件",
                                    "附件类型": "docx"
                                }
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，携带附件，远程加载，ftp"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送,收件人从列表选择",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "远程加载",
                                    "存储类型": "远程",
                                    "远程服务器": "auto_ftp",
                                    "目录": "根目录-pw-1",
                                    "变量引用": "否",
                                    "过滤类型": "正则",
                                    "文件名": {
                                        "设置方式": "选择",
                                        "正则模版名称": "auto_正则模版_匹配日期"
                                    },
                                    "附件类型": "jpeg"
                                }
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_business_conf(self):
        u"""配置邮件节点，邮件发送，携带附件，远程加载，本地文件，正则匹配文件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件发送,收件人从列表选择",
                "业务配置": {
                    "参数配置": {
                        "附件": [
                            {
                                "操作类型": "添加",
                                "附件配置": {
                                    "附件来源": "远程加载",
                                    "存储类型": "本地",
                                    "变量引用": "否",
                                    "目录": "auto_一级目录",
                                    "过滤类型": "正则",
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
                                    "附件类型": "xlsx"
                                }
                            }
                        ]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，选择开始时间和结束时间"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,选择开始时间和结束时间",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "否",
                            "值": "2020-11-20 10:15"
                        },
                        "发件结束时间": {
                            "变量引用": "否",
                            "值": "2020-11-23 23:59"
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

    def test_23_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，开始时间和结束时间使用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,开始时间和结束时间使用变量",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${地点}"
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

    def test_25_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，收件人/发件人/标题/正文/附件使用关键字"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,收件人/发件人/标题/正文/附件使用关键字",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${地点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "发件人": {
                            "正则匹配": "否",
                            "值": "pw@henghaodata.com"
                        },
                        "标题": {
                            "正则匹配": "否",
                            "值": "测试邮件标题"
                        },
                        "正文": {
                            "正则匹配": "否",
                            "值": "测试邮件正文"
                        },
                        "附件": {
                            "正则匹配": "否",
                            "值": "测试邮件附件"
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

    def test_27_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，收件人/发件人/标题/正文/附件引用变量"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,收件人/发件人/标题/正文/附件引用变量",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${地点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "${名字}@henghaodata.com"
                        },
                        "发件人": {
                            "正则匹配": "否",
                            "值": "${名字}@henghaodata.com"
                        },
                        "标题": {
                            "正则匹配": "否",
                            "值": "测试邮件${名字}"
                        },
                        "正文": {
                            "正则匹配": "否",
                            "值": "测试邮件${地点}"
                        },
                        "附件": {
                            "正则匹配": "否",
                            "值": "测试邮件${时间}"
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

    def test_29_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，收件人/发件人/标题/正文/附件正则匹配"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,收件人/发件人/标题/正文/附件正则匹配",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "发件结束时间": {
                            "变量引用": "是",
                            "值": "${地点}"
                        },
                        "收件人": {
                            "正则匹配": "否",
                            "值": "${名字}@henghaodata.com"
                        },
                        "发件人": {
                            "正则匹配": "是",
                            "值": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配日期"
                            }
                        },
                        "标题": {
                            "正则匹配": "是",
                            "值": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配日期"
                            }
                        },
                        "正文": {
                            "正则匹配": "是",
                            "值": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_匹配日期"
                            }
                        },
                        "附件": {
                            "正则匹配": "是",
                            "值": {
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
                            }
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

    def test_31_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，选择附件类型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,选择附件类型",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "附件类型": ["txt", "xlsx"]
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_process_node_add(self):
        u"""画流程图，添加一个邮件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_process_node_business_conf(self):
        u"""配置邮件节点，邮件接收，存储附件"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件节点",
                "业务配置": {
                    "节点名称": "邮件接收,存储附件",
                    "邮件模式": "接收",
                    "参数配置": {
                        "接收邮箱": "pw@henghaodata.com",
                        "发件开始时间": {
                            "变量引用": "是",
                            "值": "${时间}"
                        },
                        "存储附件": "开启",
                        "存储附件目录": "auto_一级目录"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_fetch_conf(self):
        u"""节点添加取数配置，标题"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件标题",
                    "变量类型": "标题",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_fetch_conf(self):
        u"""节点添加取数配置，正文"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件正文",
                    "变量类型": "正文",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_fetch_conf(self):
        u"""节点添加取数配置，附件内容"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件附件内容",
                    "变量类型": "附件",
                    "附件类型": "xlsx",
                    "文件名": "factor",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_fetch_conf(self):
        u"""节点添加取数配置，附件文件名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件附件文件名",
                    "变量类型": "附件文件名",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_fetch_conf(self):
        u"""节点添加取数配置，发件人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件发件人",
                    "变量类型": "发件人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_process_node_fetch_conf(self):
        u"""节点添加取数配置，收件人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件收件人",
                    "变量类型": "收件人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_fetch_conf(self):
        u"""节点添加取数配置，抄送人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件抄送人",
                    "变量类型": "抄送人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_process_node_fetch_conf(self):
        u"""节点添加取数配置，变量名已存在"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件抄送人",
                    "变量类型": "抄送人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "该变量已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "获取邮件抄送人",
                    "变量名称": "获取邮件抄送人2",
                    "变量类型": "附件",
                    "附件类型": "xls",
                    "文件名": "abcd",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "获取邮件抄送人2"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_process_node_fetch_conf(self):
        u"""节点添加取数配置，抄送人"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "邮件节点",
                "节点名称": "邮件接收,开始时间和结束时间使用变量",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "获取邮件抄送人",
                    "变量类型": "抄送人",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_46_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
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

    def test_47_process_node_line(self):
        u"""节点参数设置连线到：邮件发送,收件人从列表选择"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "邮件发送,收件人从列表选择",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点邮件发送,收件人从列表选择连线到：邮件发送,收件人为变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件发送,收件人从列表选择",
                "终止节点名称": "邮件发送,收件人为变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_49_process_node_line(self):
        u"""节点邮件发送,收件人为变量连线到：邮件发送,抄送人从列表选择"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件发送,收件人为变量",
                "终止节点名称": "邮件发送,抄送人从列表选择",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_process_node_line(self):
        u"""节点邮件发送,抄送人从列表选择连线到：邮件发送,抄送人为变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件发送,抄送人从列表选择",
                "终止节点名称": "邮件发送,抄送人为变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点邮件发送,抄送人为变量连线到：邮件发送,标题引用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件发送,抄送人为变量",
                "终止节点名称": "邮件发送,标题引用变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_52_process_node_line(self):
        u"""节点邮件发送,标题引用变量连线到：邮件接收,选择开始时间和结束时间"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件发送,标题引用变量",
                "终止节点名称": "邮件接收,选择开始时间和结束时间",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_53_process_node_line(self):
        u"""节点邮件接收,选择开始时间和结束时间连线到：邮件接收,开始时间和结束时间使用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,选择开始时间和结束时间",
                "终止节点名称": "邮件接收,开始时间和结束时间使用变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_54_process_node_line(self):
        u"""节点邮件接收,开始时间和结束时间使用变量连线到：邮件接收,收件人/发件人/标题/正文/附件使用关键字"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,开始时间和结束时间使用变量",
                "终止节点名称": "邮件接收,收件人/发件人/标题/正文/附件使用关键字",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_55_process_node_line(self):
        u"""节点邮件接收,收件人/发件人/标题/正文/附件使用关键字连线到：邮件接收,收件人/发件人/标题/正文/附件引用变量"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,收件人/发件人/标题/正文/附件使用关键字",
                "终止节点名称": "邮件接收,收件人/发件人/标题/正文/附件引用变量",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_56_process_node_line(self):
        u"""节点邮件接收,收件人/发件人/标题/正文/附件引用变量连线到：邮件接收,收件人/发件人/标题/正文/附件正则匹配"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,收件人/发件人/标题/正文/附件引用变量",
                "终止节点名称": "邮件接收,收件人/发件人/标题/正文/附件正则匹配",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_57_process_node_line(self):
        u"""节点邮件接收,收件人/发件人/标题/正文/附件正则匹配连线到：邮件接收,选择附件类型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,收件人/发件人/标题/正文/附件正则匹配",
                "终止节点名称": "邮件接收,选择附件类型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_58_process_node_line(self):
        u"""节点邮件接收,选择附件类型连线到：邮件接收,存储附件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,选择附件类型",
                "终止节点名称": "邮件接收,存储附件",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_59_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_60_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_61_process_node_line(self):
        u"""节点邮件接收,存储附件连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_邮件节点流程",
                "起始节点名称": "邮件接收,存储附件",
                "终止节点名称": "正常",
                "关联关系": "满足"
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
