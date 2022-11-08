# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CommonNodePart1(unittest.TestCase):

    log.info("装载流程通用节点配置测试用例（1）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_通用节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，基础版"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_通用节点流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_process_add(self):
        u"""添加流程，流程名称已存在"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_通用节点流程说明"
            }
        }
        msg = "流程名称重复"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_process_update(self):
        u"""修改流程"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程新",
                    "专业领域": ["AiSee"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程新说明"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_通用节点流程新"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_add(self):
        u"""添加流程，配置自定义流程变量"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_通用节点流程说明",
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

    def test_7_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_通用节点流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_add(self):
        u"""添加流程，配置输出异常"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_通用节点流程说明",
                "高级配置": {
                    "输出异常": {
                        "状态": "开启",
                        "告警方式": "邮件",
                        "发件人": "pw@henghaodata.com",
                        "收件人": ["pw@henghaodata.com"],
                        "抄送人": ["pw@henghaodata.com"],
                        "主题": "auto_流程异常",
                        "正文": "auto_流程运行异常"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_通用节点流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_add(self):
        u"""添加流程，关闭节点异常终止流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_通用节点流程说明",
                "高级配置": {
                    "节点异常终止流程": "否"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_update(self):
        u"""修改流程，开启节点异常终止流程"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_update(self):
        u"""修改流程，设置流程变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "开启",
                            "参数列表": {
                                "时间": "2020-10-20###必填",
                                "地点": "广州###",
                                "名字": "pw###必填"
                            }
                        },
                        "输出异常": {
                            "状态": "开启",
                            "告警方式": "邮件",
                            "发件人": "pw@henghaodata.com",
                            "收件人": ["pw@henghaodata.com"],
                            "抄送人": ["pw@henghaodata.com"],
                            "主题": "auto_流程异常",
                            "正文": "auto_流程运行异常"
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

    def test_13_process_update(self):
        u"""修改流程，关闭流程变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "关闭"
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

    def test_14_process_update(self):
        u"""修改流程，设置输出异常"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "开启",
                            "参数列表": {
                                "时间": "2020-10-20###必填",
                                "地点": "广州###",
                                "名字": "pw###必填"
                            }
                        },
                        "输出异常": {
                            "状态": "开启",
                            "告警方式": "邮件",
                            "发件人": "pw@henghaodata.com",
                            "收件人": ["pw@henghaodata.com"],
                            "抄送人": ["pw@henghaodata.com"],
                            "主题": "auto_流程异常",
                            "正文": "auto_流程运行异常"
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

    def test_15_process_update(self):
        u"""修改流程，关闭输出异常"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "开启",
                            "参数列表": {
                                "时间": "2020-10-20###必填",
                                "地点": "广州###",
                                "名字": "pw###必填"
                            }
                        },
                        "输出异常": {
                            "状态": "关闭"
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

    def test_16_process_add(self):
        u"""添加流程，添加子流程"""
        pres = """
        ${Database}.main|delete from tn_templ_obj_rel where obj_id=(select process_id from tn_process_conf_info where process_name='auto_子流程')
        ${Database}.main|delete from tn_process_conf_info where process_name='auto_子流程'
        """
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_子流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "子流程",
                "流程说明": "auto_子流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_update(self):
        u"""修改流程，修改流程定义变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "修改内容": {
                    "流程名称": "auto_通用节点流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_通用节点流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是",
                        "自定义流程变量": {
                            "状态": "开启",
                            "参数列表": {
                                "时间": "2020-10-21###",
                                "年龄": "20###",
                                "名字": "aisee###必填"
                            }
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

    def test_18_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_测试流程",
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

    def test_20_process_node_opt_conf(self):
        u"""配置通用节点，添加一个变量"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
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
                                    ["变量", "时间"],
                                    ["并集", ""],
                                    ["变量", "名字"]
                                ],
                                "输出名称": {
                                    "类型": "输入",
                                    "变量名": "数据"
                                },
                                "输出列": "*",
                                "赋值方式": "替换"
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

    def test_21_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "条件依赖",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_control_conf(self):
        u"""配置通用节点，控制配置，关闭条件依赖"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "条件依赖": {
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

    def test_24_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启条件依赖"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "条件依赖": {
                        "状态": "开启"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启循环，变量列表循环，自定义模式"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "开启循环": {
                        "状态": "开启",
                        "循环条件": ["操作配置"],
                        "循环类型": "变量列表",
                        "循环内容": {
                            "模式": "自定义模式",
                            "变量名称": "数据",
                            "循环行变量名称": "i",
                            "赋值方式": "替换"
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

    def test_26_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启循环，次数循环"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "开启循环": {
                        "状态": "开启",
                        "循环条件": ["操作配置"],
                        "循环类型": "次数",
                        "循环内容": {
                            "循环次数": "5",
                            "循环变量名称": "num",
                            "赋值方式": "替换",
                            "跳至下一轮条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "名字"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ],
                            "结束循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "名字"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ]
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

    def test_27_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启循环，条件循环"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "开启循环": {
                        "状态": "开启",
                        "循环条件": ["操作配置"],
                        "循环类型": "条件",
                        "循环内容": {
                            "循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "名字"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ],
                            "跳至下一轮条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "名字"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ],
                            "结束循环条件": [
                                ["变量", "时间"],
                                ["不等于", ""],
                                ["空值", ""],
                                ["与", ""],
                                ["变量", "名字"],
                                ["包含", ""],
                                ["自定义值", "abc ddd"]
                            ]
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

    def test_28_process_node_control_conf(self):
        u"""配置通用节点，控制配置，关闭循环"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "开启循环": {
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

    def test_29_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启逻辑分支控制，固定值分支"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "逻辑分支控制": {
                        "状态": "开启",
                        "逻辑分支类型": "固定值分支",
                        "满足条件": [
                            ["变量", "时间"],
                            ["不等于", ""],
                            ["空值", ""],
                            ["与", ""],
                            ["变量", "名字"],
                            ["包含", ""],
                            ["自定义值", "abc ddd"]
                        ],
                        "不满足条件": [
                            ["变量", "时间"],
                            ["不等于", ""],
                            ["空值", ""],
                            ["与", ""],
                            ["变量", "名字"],
                            ["包含", ""],
                            ["自定义值", "abc ddd"]
                        ],
                        "不确定条件": [
                            ["变量", "时间"],
                            ["不等于", ""],
                            ["空值", ""],
                            ["与", ""],
                            ["变量", "名字"],
                            ["包含", ""],
                            ["自定义值", "abc ddd"]
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

    def test_30_process_node_control_conf(self):
        u"""配置通用节点，控制配置，开启逻辑分支控制，动态值分支"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "逻辑分支控制": {
                        "状态": "开启",
                        "逻辑分支类型": "动态值分支",
                        "动态值": [
                            ["变量", "时间"],
                            ["+", ""],
                            ["自定义值", "1"]
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

    def test_31_process_node_control_conf(self):
        u"""配置通用节点，控制配置，关闭逻辑分支控制"""
        action = {
            "操作": "NodeControlConf",
            "参数": {
                "流程名称": "auto_通用节点流程",
                "节点类型": "通用节点",
                "节点名称": "条件依赖",
                "控制配置": {
                    "逻辑分支控制": {
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

    def tearDown(self):     # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
