# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class TaskManager(unittest.TestCase):

    log.info("装载任务配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_task_clear(self):
        u"""任务数据清理，删除历史数据"""
        action = {
            "操作": "TaskDataClear",
            "参数": {
                "任务名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_task_add(self):
        u"""添加任务，手动任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_date",
                "配置定时任务": "关闭",
                "任务说明": "auto_指令任务_date"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_task_update(self):
        u"""修改任务，定时任务，按月"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "1",
                        "间隔周期单位": "月"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_task_update(self):
        u"""修改任务，定时任务，按周"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "1",
                        "间隔周期单位": "周"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_task_update(self):
        u"""修改任务，定时任务，按天"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "1",
                        "间隔周期单位": "天"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_task_update(self):
        u"""修改任务，定时任务，按小时"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "12",
                        "间隔周期单位": "小时"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_task_update(self):
        u"""修改任务，定时任务，按分钟"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "30",
                        "间隔周期单位": "分钟"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_task_update(self):
        u"""修改任务，定时任务，启用高级模式"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "开启",
                        "Cron表达式": "0 0/30 9,18 * * ?"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_task_update(self):
        u"""修改任务，定时任务，关闭高级模式"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "3",
                        "间隔周期单位": "小时"

                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_task_update(self):
        u"""修改任务，定时任务改成手动任务"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "关闭",
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_task_delete(self):
        u"""删除任务，任务未启用"""
        action = {
            "操作": "DeleteTask",
            "参数": {
                "任务名称": "auto_指令任务_date"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_task_add(self):
        u"""添加任务，指令任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_date",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_指令任务_date"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_task_add(self):
        u"""添加任务，指令任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_指令带参数",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_指令带参数",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_指令任务_指令带参数"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_task_add(self):
        u"""添加任务，指令任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_组合指令",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_组合指令",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_指令任务_组合指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_task_add(self):
        u"""添加任务，指令任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_多指令",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_多指令",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_指令任务_多指令"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_task_add(self):
        u"""添加任务，指令任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_指令任务_按网元类型",
                "模版类型": "指令任务",
                "绑定任务名称": "auto_指令模板_按网元类型",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_指令任务_按网元类型"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_二维表模式",
                "模版类型": "数据拼盘任务",
                "绑定任务名称": "auto_数据拼盘_二维表模式",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_数据拼盘任务_二维表模式"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_分段模式",
                "模版类型": "数据拼盘任务",
                "绑定任务名称": "auto_数据拼盘_分段模式",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_数据拼盘任务_分段模式"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_列更新模式",
                "模版类型": "数据拼盘任务",
                "绑定任务名称": "auto_数据拼盘_列更新模式",
                "配置定时任务": "开启",
                "定时配置": {
                    "首次执行时间": "now",
                    "高级模式": "关闭",
                    "间隔周期": "1",
                    "间隔周期单位": "天"
                },
                "任务说明": "auto_数据拼盘任务_列更新模式"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_合并模式join",
                "模版类型": "数据拼盘(合并表)任务",
                "绑定任务名称": "auto_数据拼盘_合并模式join",
                "配置定时任务": "关闭",
                "任务说明": "auto_数据拼盘任务_合并模式join"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_合并模式union",
                "模版类型": "数据拼盘(合并表)任务",
                "绑定任务名称": "auto_数据拼盘_合并模式union",
                "配置定时任务": "关闭",
                "任务说明": "auto_数据拼盘任务_合并模式union"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_task_add(self):
        u"""添加任务，数据拼盘任务"""
        action = {
            "操作": "AddTask",
            "参数": {
                "任务名称": "auto_数据拼盘任务_合并模式unionall",
                "模版类型": "数据拼盘(合并表)任务",
                "绑定任务名称": "auto_数据拼盘_合并模式unionall",
                "配置定时任务": "关闭",
                "任务说明": "auto_数据拼盘任务_合并模式unionall"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_task_update_status(self):
        u"""更新任务状态"""
        action = {
            "操作": "UpdateTaskStatus",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "状态": "启用"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_task_update(self):
        u"""修改任务，任务已启用"""
        action = {
            "操作": "UpdateTask",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "修改内容": {
                    "任务名称": "auto_指令任务_date",
                    "配置定时任务": "开启",
                    "定时配置": {
                        "首次执行时间": "now",
                        "高级模式": "关闭",
                        "间隔周期": "1",
                        "间隔周期单位": "月"
                    },
                    "任务说明": "auto_指令任务_date"
                }
            }
        }
        msg = "任务已经启用"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_task_delete(self):
        u"""删除任务，任务已启用"""
        action = {
            "操作": "DeleteTask",
            "参数": {
                "任务名称": "auto_指令任务_date"
            }
        }
        msg = "任务已经启用"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_task_update_status(self):
        u"""更新任务状态"""
        action = {
            "操作": "UpdateTaskStatus",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "状态": "禁用"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_task_trigger(self):
        u"""触发任务，任务未启用"""
        action = {
            "操作": "TriggerTask",
            "参数": {
                "任务名称": "auto_指令任务_date"
            }
        }
        msg = "任务未启用"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_task_update_status(self):
        u"""更新任务状态"""
        action = {
            "操作": "UpdateTaskStatus",
            "参数": {
                "任务名称": "auto_指令任务_date",
                "状态": "启用"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_task_trigger(self):
        u"""触发任务，任务已启用"""
        action = {
            "操作": "TriggerTask",
            "参数": {
                "任务名称": "auto_指令任务_date"
            }
        }
        msg = "运行成功"
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
