# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Template(unittest.TestCase):

    log.info("装载统一网元配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_template_clear(self):
        u"""统一网元配置，数据清理"""
        action = {
            "操作": "TemplateDataClear",
            "参数": {
                "模版名称": "auto_网元模版",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_template_add(self):
        u"""添加统一网元配置，auto_网元模版_SSH终端"""
        action = {
            "操作": "AddTemplate",
            "参数": {
                "模版名称": "auto_网元模版_SSH终端",
                "网元类型": "AUTO",
                "登录模式": "SSH模式",
                "用途说明": "ssh连接终端",
                "登录配置": [
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_终端_SSH"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_template_add(self):
        u"""添加统一网元配置，auto_网元模版_TELNET终端"""
        action = {
            "操作": "AddTemplate",
            "参数": {
                "模版名称": "auto_网元模版_TELNET终端",
                "网元类型": "AUTO",
                "登录模式": "TELNET模式",
                "用途说明": "telnet连接终端",
                "登录配置": [
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_终端_TELNET"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_template_bind_ne(self):
        u"""统一网元配置网元绑定，模版名称：auto_网元模版_SSH终端"""
        action = {
            "操作": "TemplateBindNE",
            "参数": {
                "模版名称": "auto_网元模版_SSH终端",
                "网元名称": "auto_TURK",
                "厂家": "图科",
                "设备型号": "TKea",
                "待分配网元": [
                    "auto_TURK_TKea1",
                    "auto_TURK_TKea2",
                    "auto_TURK_TKea3"
                ],
                "分配方式": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_template_delivery(self):
        u"""统一网元配置下发配置"""
        action = {
            "操作": "TemplateDelivery",
            "参数": {
                "模版名称": "auto_网元模版_SSH终端"
            }
        }
        msg = '请到“登录配置确认”页面确认更改内容'
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_confirm_selected(self):
        u"""登录配置确认，确认所选"""
        action = {
            "操作": "ConfirmSelected",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKea"
                },
                "网元列表": [
                    "auto_TURK_TKea1",
                    "auto_TURK_TKea2",
                    "auto_TURK_TKea3"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_connect_test_selected(self):
        u"""连通性测试，测试所选"""
        action = {
            "操作": "TestSelectedNetunit",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKea"
                },
                "网元列表": [
                    {
                        "网元名称": "auto_TURK_TKea1",
                        "登录模式": "SSH模式"
                    },
                    {
                        "网元名称": "auto_TURK_TKea2",
                        "登录模式": "SSH模式"
                    },
                    {
                        "网元名称": "auto_TURK_TKea3",
                        "登录模式": "SSH模式"
                    }
                ]
            }
        }
        msg = "设备测试中,请等待"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_connect_test_report(self):
        u"""休眠后，获取测试结果汇总"""
        pres = """
        wait|30
        """
        action = {
            "操作": "GetConnectReport",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        result = self.worker.pre(pres)
        assert result
        msg = "正常：3条，异常：0条，测试中：0条"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_template_bind_ne(self):
        u"""统一网元配置网元绑定，模版名称：auto_网元模版_TELNET终端"""
        action = {
            "操作": "TemplateBindNE",
            "参数": {
                "模版名称": "auto_网元模版_TELNET终端",
                "网元名称": "auto_TURK",
                "厂家": "图科",
                "设备型号": "TKing",
                "待分配网元": [
                    "auto_TURK_TKing1",
                    "auto_TURK_TKing2"
                ],
                "分配方式": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_template_delivery(self):
        u"""统一网元配置下发配置"""
        action = {
            "操作": "TemplateDelivery",
            "参数": {
                "模版名称": "auto_网元模版_TELNET终端"
            }
        }
        msg = '请到“登录配置确认”页面确认更改内容'
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_confirm_selected(self):
        u"""登录配置确认，确认所选"""
        action = {
            "操作": "ConfirmSelected",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKing"
                },
                "网元列表": [
                    "auto_TURK_TKing1",
                    "auto_TURK_TKing2"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_connect_test_selected(self):
        u"""连通性测试，测试所选"""
        action = {
            "操作": "TestSelectedNetunit",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKing"
                },
                "网元列表": [
                    {
                        "网元名称": "auto_TURK_TKing1",
                        "登录模式": "TELNET模式"
                    },
                    {
                        "网元名称": "auto_TURK_TKing2",
                        "登录模式": "TELNET模式"
                    }
                ]
            }
        }
        msg = "设备测试中,请等待"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_connect_test_report(self):
        u"""休眠30秒后，获取测试结果汇总"""
        pres = """
        wait|30
        """
        action = {
            "操作": "GetConnectReport",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        result = self.worker.pre(pres)
        assert result
        msg = "正常：2条，异常：0条，测试中：0条"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_template_add(self):
        u"""添加统一网元配置，auto_网元模版_异常跳转指令"""
        action = {
            "操作": "AddTemplate",
            "参数": {
                "模版名称": "auto_网元模版_异常跳转指令",
                "网元类型": "POP",
                "登录模式": "普通模式",
                "用途说明": "登录异常",
                "登录配置": [
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_终端_TELNET"
                    },
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_登录指令_异常跳转指令"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_template_bind_ne(self):
        u"""统一网元配置网元绑定，模版名称：auto_网元模版_异常跳转指令"""
        action = {
            "操作": "TemplateBindNE",
            "参数": {
                "模版名称": "auto_网元模版_异常跳转指令",
                "网元名称": "auto_SEARCH",
                "厂家": "思旗",
                "设备型号": "Sight",
                "待分配网元": [
                    "auto_SEARCH_Sight1"
                ],
                "分配方式": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_template_delivery(self):
        u"""统一网元配置下发配置"""
        action = {
            "操作": "TemplateDelivery",
            "参数": {
                "模版名称": "auto_网元模版_异常跳转指令"
            }
        }
        msg = '请到“登录配置确认”页面确认更改内容'
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_confirm_selected(self):
        u"""登录配置确认，确认所选"""
        action = {
            "操作": "ConfirmSelected",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_SEARCH",
                    "网元类型": "POP",
                    "生产厂家": "思旗",
                    "设备型号": "Sight"
                },
                "网元列表": [
                    "auto_SEARCH_Sight1"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_connect_test_selected(self):
        u"""连通性测试，测试所选"""
        action = {
            "操作": "TestSelectedNetunit",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_SEARCH",
                    "网元类型": "POP",
                    "生产厂家": "思旗",
                    "设备型号": "Sight"
                },
                "网元列表": [
                    {
                        "网元名称": "auto_SEARCH_Sight1",
                        "登录模式": "普通模式"
                    }
                ]
            }
        }
        msg = "设备测试中,请等待"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_connect_test_report(self):
        u"""休眠后，获取测试结果汇总"""
        pres = """
        wait|90
        """
        action = {
            "操作": "GetConnectReport",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        result = self.worker.pre(pres)
        assert result
        msg = "正常：0条，异常：1条，测试中：0条"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_template_add(self):
        u"""添加统一网元配置，auto_网元模版_异常终端"""
        action = {
            "操作": "AddTemplate",
            "参数": {
                "模版名称": "auto_网元模版_异常终端",
                "网元类型": "POP",
                "登录模式": "普通模式",
                "用途说明": "登录异常",
                "登录配置": [
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_终端_异常终端"
                    },
                    {
                        "操作类型": "添加",
                        "步骤信息": "auto_登录指令_跳转指令"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_template_bind_ne(self):
        u"""统一网元配置网元绑定，模版名称：auto_网元模版_异常终端"""
        action = {
            "操作": "TemplateBindNE",
            "参数": {
                "模版名称": "auto_网元模版_异常终端",
                "网元名称": "auto_SEARCH",
                "厂家": "思旗",
                "设备型号": "Sight",
                "待分配网元": [
                    "auto_SEARCH_Sight2"
                ],
                "分配方式": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_template_delivery(self):
        u"""统一网元配置下发配置"""
        action = {
            "操作": "TemplateDelivery",
            "参数": {
                "模版名称": "auto_网元模版_异常终端"
            }
        }
        msg = '请到“登录配置确认”页面确认更改内容'
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_confirm_selected(self):
        u"""登录配置确认，确认所选"""
        action = {
            "操作": "ConfirmSelected",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_SEARCH",
                    "网元类型": "POP",
                    "生产厂家": "思旗",
                    "设备型号": "Sight"
                },
                "网元列表": [
                    "auto_SEARCH_Sight2"
                ]
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_connect_test_selected(self):
        u"""连通性测试，测试所选"""
        action = {
            "操作": "TestSelectedNetunit",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_SEARCH",
                    "网元类型": "POP",
                    "生产厂家": "思旗",
                    "设备型号": "Sight"
                },
                "网元列表": [
                    {
                        "网元名称": "auto_SEARCH_Sight2",
                        "登录模式": "普通模式"
                    }
                ]
            }
        }
        msg = "设备测试中,请等待"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_connect_test_report(self):
        u"""休眠后，获取测试结果汇总"""
        pres = """
        wait|90
        """
        action = {
            "操作": "GetConnectReport",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        result = self.worker.pre(pres)
        assert result
        msg = "正常：0条，异常：1条，测试中：0条"
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
