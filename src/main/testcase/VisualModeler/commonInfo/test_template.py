# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/30 下午5:13

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Template(unittest.TestCase):

    log.info("装载网元模版配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_template_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "ZgTempDataClear",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_table_add(self):
        u"""网元基础信息，添加模版：auto_网元基础信息表"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_template_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "ZgTempDataClear",
            "参数": {
                "模版类型": "网元辅助资料",
                "模版名称": "auto_网元辅助资料"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_4_table_add(self):
        u"""网元辅助资料，添加模版：auto_网元辅助资料"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元辅助资料",
                "模版名称": "auto_网元辅助资料"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_table_set_col(self):
        u"""网元辅助资料：auto_网元辅助资料，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元辅助资料",
                "模版名称": "auto_网元辅助资料",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "列1",
                        "业务变量": "ssip",
                        "数据类型": "字符",
                        "长度": "100"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_template_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "ZgTempDataClear",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_7_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_table_set_col(self):
        u"""网元辅助资料：auto_网元辅助资料，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "列1",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列2",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列3",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列4",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列5",
                        "数据类型": "字符",
                        "长度": "200"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料，删除网元名称列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料",
                "列配置": [
                    {
                        "操作类型": "删除",
                        "配置项": "网元名称"
                    }
                ]
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_table_add(self):
        u"""网元其它资料，添加模版：auto_测试告警表"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试告警表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_table_set_col(self):
        u"""网元其它资料：auto_测试告警表，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试告警表",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "列1",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列2",
                        "数据类型": "字符",
                        "长度": "200"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_table_set_col(self):
        u"""网元其它资料：auto_测试告警表，删除网元名称列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试告警表",
                "列配置": [
                    {
                        "操作类型": "删除",
                        "配置项": "网元名称"
                    }
                ]
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_table_add(self):
        u"""网元其它资料，添加模版：auto_测试输出表"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试输出表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_table_set_col(self):
        u"""网元其它资料：auto_测试输出表，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试输出表",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "列1",
                        "数据类型": "字符",
                        "长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列2",
                        "数据类型": "字符",
                        "长度": "200"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_table_set_col(self):
        u"""网元其它资料：auto_测试输出表，删除网元名称列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_测试输出表",
                "列配置": [
                    {
                        "操作类型": "删除",
                        "配置项": "网元名称"
                    }
                ]
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料_多类型"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_多类型"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_多类型，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_多类型",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "列1",
                        "数据类型": "字符",
                        "长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列2",
                        "数据类型": "数值",
                        "小位数": "2"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列3",
                        "数据类型": "日期",
                        "输入格式": ["yyyyMMddHHmmss", ""],
                        "输出格式": ["yyyyMMddHHmmss", ""]
                    },
                    {
                        "操作类型": "添加",
                        "列名": "列4",
                        "数据类型": "文本"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_多类型，删除网元名称列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_多类型",
                "列配置": [
                    {
                        "操作类型": "删除",
                        "配置项": "网元名称"
                    }
                ]
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料_vm仪表盘"""
        action = {
            "操作": "AddZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，添加列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名": "姓名",
                        "数据类型": "字符",
                        "长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "等级",
                        "数据类型": "字符",
                        "长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名": "分数",
                        "数据类型": "数值",
                        "小位数": "0"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，删除网元名称列"""
        action = {
            "操作": "SaveZgTempCol",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "列配置": [
                    {
                        "操作类型": "删除",
                        "配置项": "网元名称"
                    }
                ]
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_table_set_col_search(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置搜索条件"""
        action = {
            "操作": "UpdateColSearch",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "列名列表": ["姓名", "等级", "分数"]
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_table_set_col_frozen(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置是否冻结"""
        action = {
            "操作": "UpdateColFrozen",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "列名列表": ["姓名", "等级", "分数"]
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_table_set_col_null(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，设置允许为空"""
        action = {
            "操作": "UpdateColNull",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "列名列表": ["姓名", "等级", "分数"]
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_table_copy(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，复制模版"""
        action = {
            "操作": "CopyZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘",
                "新模版名称": "auto_网元其它资料_vm仪表盘2"
            }
        }
        msg = "复制成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_table_copy(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘2，删除模版"""
        action = {
            "操作": "DeleteZgTemp",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘2"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_table_push_alarm(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台"""
        action = {
            "操作": "ZgTempPushAlarm",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "推送成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_table_sync_alarm(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，同步告警平台"""
        action = {
            "操作": "ZgTempSyncAlarm",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "同步成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_table_revoke_alarm(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送告警平台"""
        action = {
            "操作": "ZgTempRevokeAlarm",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "撤销成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_table_push_alarm(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送告警平台"""
        action = {
            "操作": "ZgTempPushAlarm",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "推送成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_table_push_dashboard(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘"""
        action = {
            "操作": "ZgTempPushDashboard",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "推送成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_table_sync_dashboard(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，同步仪表盘"""
        action = {
            "操作": "ZgTempSyncDashboard",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "同步成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_table_revoke_dashboard(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，撤销推送仪表盘"""
        action = {
            "操作": "ZgTempRevokeDashboard",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "撤销成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_table_push_dashboard(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，推送仪表盘"""
        action = {
            "操作": "ZgTempPushDashboard",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "推送成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_table_set_col_search(self):
        u"""网元其它资料：auto_网元其它资料，设置搜索条件"""
        action = {
            "操作": "UpdateColSearch",
            "参数": {
                "模版类型": "网元其它资料",
                "模版名称": "auto_网元其它资料",
                "列名列表": ["列1", "列2", "列3", "列4", "列5"]
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME1}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据，网元已添加，未二次确认"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME1}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_table_data_confirm(self):
        u"""网元基础信息，数据管理，二次确认，确认通过"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": ["${NetunitMME1}"]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME2}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_table_data_confirm(self):
        u"""网元基础信息，数据管理，二次确认，确认通过"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": ["${NetunitMME2}"]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据，网元已存在"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME1}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_42_table_data_update(self):
        u"""网元基础信息，数据管理，修改数据，网元已存在"""
        action = {
            "操作": "ZgUpdateData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元名称": "${NetunitMME1}",
                "数据信息": [
                    ["网元名称", "${NetunitMME2}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.116"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "无业务"]
                ]
            }
        }
        msg = "网元名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_43_table_data_update(self):
        u"""网元基础信息，数据管理，修改数据"""
        action = {
            "操作": "ZgUpdateData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元名称": "${NetunitMME1}",
                "数据信息": [
                    ["网元名称", "${NetunitMME2}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.116"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "无业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_44_table_data_confirm(self):
        u"""网元基础信息，数据管理，修改数据，二次确认"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": ["${NetunitMME1}"]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_45_table_data_delete(self):
        u"""网元基础信息，数据管理，删除数据"""
        action = {
            "操作": "ZgDeleteData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元名称": "${NetunitMME1}"
                }
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_46_table_data_confirm(self):
        u"""网元基础信息，数据管理，删除数据，取消确认"""
        action = {
            "操作": "ZgDataRevokeSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元名称": "${NetunitMME1}"
                },
                "网元列表": ["${NetunitMME1}"]
            }
        }
        msg = "撤销成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_table_data_delete(self):
        u"""网元基础信息，数据管理，删除数据"""
        action = {
            "操作": "ZgDeleteData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元名称": "${NetunitMME1}"
                }
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_table_data_confirm(self):
        u"""网元基础信息，数据管理，删除数据，二次确认，确认所选"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": ["${NetunitMME1}"]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_table_data_delete(self):
        u"""网元基础信息，数据管理，删除数据"""
        action = {
            "操作": "ZgDeleteData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元名称": "${NetunitMME2}"
                }
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_table_data_confirm(self):
        u"""网元基础信息，数据管理，删除数据，二次确认，确认全部"""
        action = {
            "操作": "ZgDataConfirmAll",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME1}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME2}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_table_data_add(self):
        u"""网元基础信息，数据管理，添加数据"""
        action = {
            "操作": "ZgAddData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "数据信息": [
                    ["网元名称", "${NetunitMME3}"],
                    ["网元类型", "MME"],
                    ["网元IP", "192.168.88.123"],
                    ["生产厂家", "华为"],
                    ["设备型号", "ME60"],
                    ["业务状态", "带业务"]
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_table_data_confirm(self):
        u"""网元基础信息，数据管理，二次确认，确认所选"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": [
                    "${NetunitMME1}",
                    "${NetunitMME2}",
                    "${NetunitMME3}"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_55_table_data_templ_download(self):
        u"""网元基础信息，数据管理，导入数据，下载模版"""
        action = {
            "操作": "ZgDownloadTempl",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        checks = """
        CheckDownloadFile|网元基础信息auto_网元基础信息表模板文件|xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_56_table_data_upload(self):
        u"""网元基础信息，数据管理，导入数据"""
        action = {
            "操作": "ZgUploadData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "文件路径": "网元基础信息auto_网元基础信息表.xlsx"
            }
        }
        msg = "文件导入成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_57_table_data_confirm(self):
        u"""网元基础信息，数据管理，导入数据，二次确认，撤销所有"""
        action = {
            "操作": "ZgDataRevokeAll",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        msg = "撤销成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_table_data_upload(self):
        u"""网元基础信息，数据管理，导入数据，数据正常"""
        action = {
            "操作": "ZgUploadData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "文件路径": "网元基础信息auto_网元基础信息表.xlsx"
            }
        }
        msg = "文件导入成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_table_data_confirm(self):
        u"""网元基础信息，数据管理，导入数据，二次确认，确认部分"""
        action = {
            "操作": "ZgDataConfirmSelected",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "网元列表": [
                    "auto_test_004",
                    "auto_test_005",
                    "auto_test_006",
                    "auto_test_007"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_table_data_confirm(self):
        u"""网元基础信息，数据管理，导入数据，二次确认，确认所有"""
        action = {
            "操作": "ZgDataConfirmAll",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_table_data_export(self):
        u"""网元基础信息，导出数据"""
        action = {
            "操作": "ZgExportData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表"
            }
        }
        checks = """
        CheckDownloadFile|auto_网元基础信息表网元基础信息|csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_62_table_data_list(self):
        u"""网元基础信息，数据管理，按网元名称查询"""
        action = {
            "操作": "ZgListData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元名称": "auto_test_002"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_table_data_list(self):
        u"""网元基础信息，数据管理，按网元IP查询"""
        action = {
            "操作": "ZgListData",
            "参数": {
                "模版类型": "网元基础信息",
                "模版名称": "auto_网元基础信息表",
                "查询条件": {
                    "网元IP": "192.168.88.123"
                }
            }
        }
        msg = ""
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
