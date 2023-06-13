# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/25 下午9:46

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CmdTpl(unittest.TestCase):

    log.info("装载指令模版配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_task_clear(self):
        u"""任务数据清理，删除历史数据"""
        action = {
            "操作": "TaskDataClear",
            "参数": {
                "任务名称": "auto_指令任务_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_指令模版节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_3_cmdTpl_clear(self):
        u"""指令模版数据清理，删除历史数据"""
        action = {
            "操作": "CmdTplDataClear",
            "参数": {
                "模版名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_4_cmdTpl_add(self):
        u"""添加指令模版，指令不带参数"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "不带参数指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_date",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_date", "auto_解析模板_解析date"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_cmdTpl_add(self):
        u"""添加指令模版，指令带参数"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_指令带参数",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "带参数指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_指令带参数",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_指令带参数",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_单参数",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_单参数", "auto_解析模板_解析ping"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_cmdTpl_add(self):
        u"""添加指令模版，组合指令"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_组合指令",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "组合指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_组合指令",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_组合指令",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_组合指令",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_组合指令", "auto_解析模板_解析date"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_cmdTpl_add(self):
        u"""添加指令模版，多指令"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_多指令",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "多条指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_多指令",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_多指令",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_date", "auto_解析模板_解析date"],
                            ["auto_指令_ping", "auto_解析模板_解析ping"]
                         ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_cmdTpl_add(self):
        u"""添加指令模版，按网元类型"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元类型",
                "备注": "按网元类型"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_cmdTpl_update_status(self):
        u"""指令模版未绑定网元，启动指令模版"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "修改内容": {
                    "模版网元类型绑定": {
                        "待分配网元类型": [
                            "MME"
                        ]
                    }
                }
            }
        }
        msg = "修改模版前，请先禁用该模版"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_cmdTpl_update_status(self):
        u"""禁用指令模版"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "状态": "禁用"
            }
        }
        msg = "禁用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "修改内容": {
                    "模版网元类型绑定": {
                        "待分配网元类型": [
                            "MME"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_cmdTpl_update_status(self):
        u"""指令模版未绑定指令，启动指令模版"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_cmdTpl_update_status(self):
        u"""禁用指令模版"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "状态": "禁用"
            }
        }
        msg = "禁用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_date",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_date", "auto_解析模板_解析date"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_cmdTpl_update(self):
        u"""修改指令模版，启用自动跟进策略"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "自动跟进策略配置": {
                        "状态": "启用",
                        "跟进范围": [
                            "网元无法连接",
                            "网元登录失败",
                            "网元执行失败",
                            "网管无法连接",
                            "网管登录失败",
                            "执行跳转指令失败"
                        ],
                        "跟进周期": "3",
                        "跟进次数": "2"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_cmdTpl_update(self):
        u"""修改指令模版，修改自动跟进策略"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "自动跟进策略配置": {
                        "状态": "启用",
                        "跟进范围": [
                            "网管无法连接",
                            "网管登录失败",
                            "执行跳转指令失败"
                        ],
                        "跟进周期": "12",
                        "跟进次数": "1"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_cmdTpl_update(self):
        u"""修改指令模版，禁用自动跟进策略"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "自动跟进策略配置": {
                        "状态": "禁用"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_cmdTpl_update(self):
        u"""修改指令模版，启用自动跟进策略"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "修改内容": {
                    "自动跟进策略配置": {
                        "状态": "启用",
                        "跟进范围": [
                            "网元登录失败",
                            "网管无法连接",
                            "网管登录失败",
                            "执行跳转指令失败"
                        ],
                        "跟进周期": "6",
                        "跟进次数": "1"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_cmdTpl_add(self):
        u"""添加指令模版，磁盘利用率检查"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_磁盘利用率检查",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "磁盘利用率检查"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_磁盘利用率检查",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_磁盘利用率检查",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_磁盘利用率检查",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_磁盘利用率检查", "auto_解析模板_服务器磁盘利用率检查"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_cmdTpl_add(self):
        u"""添加指令模版，查看Slab"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_查看Slab",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "查看Slab"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_查看Slab",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_查看Slab",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_查看Slab",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_查看Slab", "auto_解析模板_查看Slab解析"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_cmdTpl_add(self):
        u"""添加指令模版，内存利用率检查"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_内存利用率检查",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "内存利用率检查"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_内存利用率检查",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_内存利用率检查",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_查看Slab",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_内存利用率检查", "auto_解析模板_内存利用率解析"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_cmdTpl_add(self):
        u"""添加指令模版，服务器性能检测Top"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器性能检测Top",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "服务器性能检测Top"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器性能检测Top",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器性能检测Top",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_查看Slab",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_服务器性能检测Top", "auto_解析模板_cpu利用率检查"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_cmdTpl_add(self):
        u"""添加指令模版，服务器负载检查"""
        action = {
            "操作": "AddCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器负载检查",
                "专业领域": ["AiSee"],
                "网络层级": ["4G"],
                "选择方式": "网元",
                "备注": "服务器负载检查"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_cmdTpl_update(self):
        u"""修改指令模版，绑定网元"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器负载检查",
                "修改内容": {
                    "模版网元绑定": {
                        "网元名称": "MME",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配网元": [
                            "${NetunitMME1}",
                            "${NetunitMME2}",
                            "${NetunitMME3}"
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_cmdTpl_update(self):
        u"""修改指令模版，绑定指令"""
        action = {
            "操作": "UpdateCmdTpl",
            "参数": {
                "模版名称": "auto_指令模板_服务器负载检查",
                "修改内容": {
                    "模版指令绑定": {
                        "指令名称": "auto_指令_查看Slab",
                        "网元分类": ["4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60",
                        "待分配指令": [
                            ["auto_指令_服务器负载检查", "auto_解析模板_服务器负载检查"]
                        ]
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_date"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_date",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_指令带参数"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_指令带参数",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_组合指令"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_组合指令",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_多指令"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_多指令",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_按网元类型"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_按网元类型",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_磁盘利用率检查"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_磁盘利用率检查",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_查看Slab"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_查看Slab",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_内存利用率检查"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_内存利用率检查",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_服务器性能检测Top"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_服务器性能检测Top",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_cmdTpl_update_status(self):
        u"""启动指令模版：auto_指令模板_服务器负载检查"""
        action = {
            "操作": "UpdateCmpTplStatus",
            "参数": {
                "模版名称": "auto_指令模板_服务器负载检查",
                "状态": "启用"
            }
        }
        msg = "启用指令模版成功"
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
