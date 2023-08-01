# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class ProcessConfig(unittest.TestCase):

    log.info("装载流程配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_配置流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，基础版"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_配置流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_add(self):
        u"""添加流程，流程名称已存在"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_配置流程说明"
            }
        }
        msg = "流程名称重复"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_update(self):
        u"""修改流程"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程新",
                    "专业领域": ["AiSee"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程新说明"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_配置流程新"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_add(self):
        u"""添加流程，配置自定义流程变量"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_配置流程说明",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_配置流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_add(self):
        u"""添加流程，配置输出异常"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_配置流程说明",
                "高级配置": {
                    "输出异常": {
                        "状态": "开启",
                        "告警方式": "邮件",
                        "发件人": "pw@henghaodata.com",
                        "收件人": ["pw@henghaodata.com"],
                        "抄送人": ["pw@henghaodata.com"],
                        "主题": "auto_配置流程异常",
                        "正文": "auto_配置流程运行异常"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_配置流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_add(self):
        u"""添加流程，关闭节点异常终止流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_配置流程说明",
                "高级配置": {
                    "节点异常终止流程": "否"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_update(self):
        u"""修改流程，开启节点异常终止流程"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
                    "高级配置": {
                        "节点异常终止流程": "是"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_update(self):
        u"""修改流程，设置流程变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_update(self):
        u"""修改流程，关闭流程变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_update(self):
        u"""修改流程，设置输出异常"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
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
                            "主题": "auto_配置流程异常",
                            "正文": "auto_配置流程运行异常"
                        }
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_update(self):
        u"""修改流程，关闭输出异常"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_update(self):
        u"""修改流程，修改流程定义变量"""
        action = {
            "操作": "UpdateProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "修改内容": {
                    "流程名称": "auto_配置流程",
                    "专业领域": ["AiSee", "auto域"],
                    "流程类型": "主流程",
                    "流程说明": "auto_配置流程说明",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_配置流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_配置流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "休眠",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_node_opt_conf(self):
        u"""操作配置，添加操作，动作，休眠"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_配置流程",
                "节点类型": "通用节点",
                "节点名称": "休眠",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "动作",
                            "配置": {
                                "表达式": [
                                    ["休眠", "3"]
                                ]
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

    def test_21_process_node_line(self):
        u"""开始节点连线到节点：休眠"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_配置流程",
                "起始节点名称": "开始",
                "终止节点名称": "休眠",
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
                "流程名称": "auto_配置流程",
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
                "流程名称": "auto_配置流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_node_line(self):
        u"""节点休眠连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_配置流程",
                "起始节点名称": "休眠",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_多级流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_26_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_27_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_28_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_29_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_30_process_add(self):
        u"""添加流程，多级流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_多级流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_多级流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_add(self):
        u"""添加流程，添加一级子流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_一级子流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "子流程",
                "流程说明": "auto_一级子流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_add(self):
        u"""添加流程，添加二级子流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_二级子流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "子流程",
                "流程说明": "auto_二级子流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_process_add(self):
        u"""添加流程，添加二级子流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "子流程",
                "流程说明": "auto_二级子流程2说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_add(self):
        u"""添加流程，添加三级子流程"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_三级子流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "子流程",
                "流程说明": "auto_三级子流程说明"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_多级流程",
                "流程类型": "主流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_多级流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "主流程节点",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_node_opt_conf(self):
        u"""操作配置，绑定一级子流程"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_多级流程",
                "流程类型": "主流程",
                "节点类型": "通用节点",
                "节点名称": "主流程节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "操作类型": "绑定子流程",
                        "子流程配置": {
                            "子流程名称": "auto_一级子流程"
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

    def test_38_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "一级子流程节点",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_process_node_opt_conf(self):
        u"""操作配置，绑定二级子流程"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "一级子流程节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "操作类型": "绑定子流程",
                        "子流程配置": {
                            "子流程名称": "auto_二级子流程"
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

    def test_41_process_node_opt_conf(self):
        u"""操作配置，绑定二级子流程"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "一级子流程节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "操作类型": "绑定子流程",
                        "子流程配置": {
                            "子流程名称": "auto_二级子流程2"
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

    def test_42_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "二级子流程节点",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_process_node_opt_conf(self):
        u"""操作配置，绑定三级子流程"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "二级子流程节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加子流程",
                        "操作类型": "绑定子流程",
                        "子流程配置": {
                            "子流程名称": "auto_三级子流程"
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

    def test_45_process_node_line(self):
        u"""开始节点连线到节点：主流程节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_多级流程",
                "起始节点名称": "开始",
                "终止节点名称": "主流程节点",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_多级流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_多级流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_line(self):
        u"""节点主流程节点连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_多级流程",
                "起始节点名称": "主流程节点",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_line(self):
        u"""开始节点连线到节点：一级子流程节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "起始节点名称": "开始",
                "终止节点名称": "一级子流程节点",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_line(self):
        u"""节点一级子流程节点连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_一级子流程",
                "起始节点名称": "一级子流程节点",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_line(self):
        u"""开始节点连线到节点：一级子流程节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "起始节点名称": "开始",
                "终止节点名称": "二级子流程节点",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_55_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_line(self):
        u"""节点二级子流程节点连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_二级子流程",
                "流程类型": "子流程",
                "起始节点名称": "二级子流程节点",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_57_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "二级子流程2节点",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_process_node_opt_conf(self):
        u"""操作配置，添加操作，动作，休眠"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "二级子流程2节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "动作",
                            "配置": {
                                "表达式": [
                                    ["休眠", "2"]
                                ]
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

    def test_60_process_node_line(self):
        u"""开始节点连线到节点：二级子流程2节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "起始节点名称": "开始",
                "终止节点名称": "二级子流程2节点",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_process_node_line(self):
        u"""节点二级子流程2节点连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_二级子流程2",
                "流程类型": "子流程",
                "起始节点名称": "二级子流程2节点",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_add(self):
        u"""画流程图，添加一个通用节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_65_process_node_business_conf(self):
        u"""配置通用节点"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "通用节点",
                "业务配置": {
                    "节点名称": "三级子流程节点",
                    "场景标识": "无"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_node_opt_conf(self):
        u"""操作配置，添加操作，动作，休眠"""
        action = {
            "操作": "NodeOptConf",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "节点类型": "通用节点",
                "节点名称": "三级子流程节点",
                "操作配置": [
                    {
                        "对象": "操作",
                        "右键操作": "添加操作",
                        "运算配置": {
                            "运算类型": "动作",
                            "配置": {
                                "表达式": [
                                    ["休眠", "3"]
                                ]
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

    def test_67_process_node_line(self):
        u"""开始节点连线到节点：三级子流程节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "起始节点名称": "开始",
                "终止节点名称": "三级子流程节点",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_68_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_69_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_70_process_node_line(self):
        u"""节点三级子流程节点连线到：结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_三级子流程",
                "流程类型": "子流程",
                "起始节点名称": "三级子流程节点",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def tearDown(self):     # 最后执行的函数
        self.browser = gbl.service.get("browser")
        saveScreenShot()
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
