# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class NetUnit(unittest.TestCase):

    log.info("装载网元管理配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_netunit_clear(self):
        u"""网元管理，数据清理"""
        action = {
            "操作": "NetUnitDataClear",
            "参数": {
                "网元名称": "auto_manual"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_netunit_add(self):
        u"""添加网元"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_manual",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_netunit_add(self):
        u"""添加网元，网元名称已存在"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_manual",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.122",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "网元名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_netunit_update(self):
        u"""修改网元"""
        action = {
            "操作": "UpdateNetUnit",
            "参数": {
                "网元名称": "auto_manual",
                "修改内容": {
                    "网元名称": "auto_manual_bak",
                    "登录模式": "POP",
                    "网元IP": "192.168.88.122",
                    "生产厂家": "思旗",
                    "设备型号": "Sight",
                    "业务状态": "无业务",
                    "最大并发数": "10"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_netunit_update(self):
        u"""修改网元，恢复正确数据"""
        action = {
            "操作": "UpdateNetUnit",
            "参数": {
                "网元名称": "auto_manual_bak",
                "修改内容": {
                    "网元名称": "auto_manual",
                    "网元类型": "AUTO",
                    "网元IP": "192.168.88.123",
                    "生产厂家": "图科",
                    "设备型号": "TKea",
                    "业务状态": "带业务",
                    "最大并发数": "1"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_netunit_delete(self):
        u"""删除网元"""
        action = {
            "操作": "DeleteNetUnit",
            "参数": {
                "网元名称": "auto_manual"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_netunit_clear(self):
        u"""网元管理，数据清理"""
        action = {
            "操作": "NetUnitDataClear",
            "参数": {
                "网元名称": "auto_manual_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_8_netunit_add(self):
        u"""添加网元，auto_manual_s_ssh"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_manual_s_ssh",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_netunit_set_login_info(self):
        u"""网元设置登录信息，普通模式，自身，SSH"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual_s_ssh",
                "登录模式": "普通模式",
                "终端配置": {
                    "终端名称": "自身",
                    "登录方式": "SSH",
                    "用户名": "u_normal",
                    "密码": "u_normal_pass",
                    "IP": "192.168.88.123",
                    "端口": "22",
                    "期待返回符": "",
                    "失败返回符": "",
                    "字符集": "GBK"
                },
                "是否覆盖终端指令": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_netunit_add(self):
        u"""添加网元，auto_manual_s_telnet"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_manual_s_telnet",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_netunit_add(self):
        u"""添加网元，auto_manual"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_manual",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_netunit_set_login_info(self):
        u"""网元设置登录信息，普通模式，自身，TELNET"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual_s_telnet",
                "登录模式": "普通模式",
                "终端配置": {
                    "终端名称": "自身",
                    "登录方式": "TELNET",
                    "用户名": "",
                    "密码": "",
                    "IP": "192.168.88.123",
                    "端口": "23",
                    "期待返回符": "",
                    "失败返回符": "",
                    "字符集": "GBK"
                },
                "是否覆盖终端指令": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_netunit_set_login_cmd(self):
        u"""网元设置登录信息，普通模式，指令设置"""
        action = {
            "操作": "NELoginConfigSetCmd",
            "参数": {
                "网元名称": "auto_manual_s_telnet",
                "登录模式": "普通模式",
                "指令配置": {
                    "登录指令": [
                        {
                            "操作类型": "删除"
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "%USERNAME",
                                "账号名称": "auto_账号_常用账号",
                                "期待返回符": "assword:",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n",
                                "指令类型": "私有指令"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "%PASSWORD",
                                "账号名称": "auto_账号_常用账号",
                                "期待返回符": "",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n",
                                "指令类型": "私有指令"
                            }
                        }
                    ]
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_netunit_set_login_info(self):
        u"""网元设置登录信息，SSH模式，使用终端"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual",
                "登录模式": "SSH模式",
                "终端配置": {
                    "终端名称": "auto_终端_SSH"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_netunit_set_login_info(self):
        u"""网元设置登录信息，TELNET模式，使用终端"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual",
                "登录模式": "TELNET模式",
                "终端配置": {
                    "终端名称": "auto_终端_TELNET"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_netunit_set_login_info(self):
        u"""网元设置登录信息，异常模式，使用终端"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual",
                "登录模式": "异常模式",
                "终端配置": {
                    "终端名称": "auto_终端_异常终端"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_netunit_set_login_info(self):
        u"""网元设置登录信息，普通模式，自定义登录信息"""
        action = {
            "操作": "NELoginConfigSetTerminal",
            "参数": {
                "网元名称": "auto_manual",
                "登录模式": "普通模式",
                "终端配置": {
                    "终端名称": "auto_终端_SSH"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_netunit_set_login_cmd(self):
        u"""网元设置登录信息，普通模式，指令设置"""
        action = {
            "操作": "NELoginConfigSetCmd",
            "参数": {
                "网元名称": "auto_manual",
                "登录模式": "普通模式",
                "指令配置": {
                    "终端指令": [
                        {
                            "操作类型": "删除"
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "date",
                                "账号名称": "",
                                "期待返回符": "",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "ping %IP -c 5",
                                "账号名称": "",
                                "期待返回符": "",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n"
                            }
                        }
                    ],
                    "终端指令设为私有指令": "否",
                    "登录指令": [
                        {
                            "操作类型": "删除"
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "telnet %IP",
                                "账号名称": "",
                                "期待返回符": "ogin:",
                                "失败返回符": "",
                                "隐藏输入指令": "是",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "3",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "%USERNAME",
                                "账号名称": "auto_账号_常用账号",
                                "期待返回符": "assword:",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "指令信息": {
                                "指令内容": "%PASSWORD",
                                "账号名称": "auto_账号_常用账号",
                                "期待返回符": "",
                                "失败返回符": "",
                                "隐藏输入指令": "否",
                                "隐藏指令返回": "",
                                "退出命令": "",
                                "执行后等待时间": "",
                                "是否适配网元": "是",
                                "字符集": "GBK",
                                "换行符": r"\n"
                            }
                        }
                    ],
                    "登录指令设为私有指令": "否"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_netunit_clear(self):
        u"""网元管理，数据清理"""
        action = {
            "操作": "NetUnitDataClear",
            "参数": {
                "网元名称": "auto_TURK",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_20_netunit_add(self):
        u"""添加网元，auto_TURK_TKea1"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_TURK_TKea1",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_netunit_add(self):
        u"""添加网元，auto_TURK_TKea2"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_TURK_TKea2",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_netunit_add(self):
        u"""添加网元，auto_TURK_TKea3"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_TURK_TKea3",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKea",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_netunit_add(self):
        u"""添加网元，auto_TURK_TKing1"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_TURK_TKing1",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKing",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_netunit_add(self):
        u"""添加网元，auto_TURK_TKing2"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_TURK_TKing2",
                "网元类型": "AUTO",
                "网元IP": "192.168.88.123",
                "生产厂家": "图科",
                "设备型号": "TKing",
                "业务状态": "无业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_netunit_clear(self):
        u"""网元管理，数据清理"""
        action = {
            "操作": "NetUnitDataClear",
            "参数": {
                "网元名称": "auto_SEARCH",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_26_netunit_add(self):
        u"""添加网元，auto_SEARCH_Sight1"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_SEARCH_Sight1",
                "网元类型": "POP",
                "网元IP": "192.168.88.123",
                "生产厂家": "思旗",
                "设备型号": "Sight",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_netunit_add(self):
        u"""添加网元，auto_SEARCH_Sight2"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "auto_SEARCH_Sight2",
                "网元类型": "POP",
                "网元IP": "192.168.88.123",
                "生产厂家": "思旗",
                "设备型号": "Sight",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
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
