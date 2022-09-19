# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/30 下午5:13

import unittest
from src.screenShot import screenShot
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class Template(unittest.TestCase):

    log.info("装载网元模版配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_field_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "TableDataClear",
            "参数": {
                "模版类型": "网元基础信息",
                "表名": "auto_网元基础信息表"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_table_add(self):
        u"""网元基础信息，添加模版：auto_网元基础信息表"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元基础信息",
                "表名": "auto_网元基础信息表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_field_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "TableDataClear",
            "参数": {
                "模版类型": "网元辅助资料",
                "表名": "auto_网元辅助资料"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_4_table_add(self):
        u"""网元辅助资料，添加模版：auto_网元辅助资料"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元辅助资料",
                "表名": "auto_网元辅助资料"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_table_set_col(self):
        u"""网元辅助资料：auto_网元辅助资料，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元辅助资料",
                "表名": "auto_网元辅助资料",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_field_clear(self):
        u"""网元模版配置管理，数据清理"""
        action = {
            "操作": "TableDataClear",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_7_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_table_set_col(self):
        u"""网元辅助资料：auto_网元辅助资料，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料，删除网元名称列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_table_add(self):
        u"""网元其它资料，添加模版：auto_测试告警表"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试告警表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_table_set_col(self):
        u"""网元其它资料：auto_测试告警表，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试告警表",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_table_set_col(self):
        u"""网元其它资料：auto_测试告警表，删除网元名称列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试告警表",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_table_add(self):
        u"""网元其它资料，添加模版：auto_测试输出表"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试输出表"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_table_set_col(self):
        u"""网元其它资料：auto_测试输出表，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试输出表",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_table_set_col(self):
        u"""网元其它资料：auto_测试输出表，删除网元名称列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_测试输出表",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料_多类型"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_多类型"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_多类型，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_多类型",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_多类型，删除网元名称列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_多类型",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_table_add(self):
        u"""网元其它资料，添加模版：auto_网元其它资料_vm仪表盘"""
        action = {
            "操作": "AddTable",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_vm仪表盘"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，添加列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_vm仪表盘",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_table_set_col(self):
        u"""网元其它资料：auto_网元其它资料_vm仪表盘，删除网元名称列"""
        action = {
            "操作": "TableColSet",
            "参数": {
                "模版类型": "网元其它资料",
                "表名": "auto_网元其它资料_vm仪表盘",
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
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
