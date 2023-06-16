# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Terminal(unittest.TestCase):

    log.info("装载统一终端配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_terminal_add(self):
        u"""添加统一终端"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "test_auto_manual",
                "网元类型": "MME",
                "网元IP": "192.168.88.123",
                "生产厂家": "华为",
                "设备型号": "ME60",
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
                "网元名称": "test_auto_manual",
                "网元类型": "MME",
                "网元IP": "192.168.88.122",
                "生产厂家": "华为",
                "设备型号": "ME60",
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
                "网元名称": "test_auto_manual",
                "修改内容": {
                    "网元名称": "test_auto_manual_bak",
                    "登录模式": "MME",
                    "网元IP": "192.168.88.122",
                    "生产厂家": "爱立信",
                    "设备型号": "SE600",
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
                "网元名称": "test_auto_manual_bak",
                "修改内容": {
                    "网元名称": "test_auto_manual",
                    "登录模式": "MME",
                    "网元IP": "192.168.88.123",
                    "生产厂家": "华为",
                    "设备型号": "ME60",
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
                "网元名称": "test_auto_manual"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_netunit_clear(self):
        u"""网元管理，数据清理"""
        action = {
            "操作": "NetUnitDataClear",
            "参数": {
                "网元名称": "test_auto_manual_",
                "模糊查询": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_8_netunit_add(self):
        u"""添加网元，test_auto_manual_s_ssh"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "test_auto_manual_s_ssh",
                "网元类型": "MME",
                "网元IP": "192.168.88.123",
                "生产厂家": "华为",
                "设备型号": "ME60",
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
        u"""网元设置登录信息，普通模式，本身，SSH"""
        action = {
            "网元名称": "test_auto_manual_s_ssh",
            "登录模式": "普通模式",
            "终端配置": {
                "终端名称": "本身",
                "登录方式": "SSH",
                "用户名": "u_normal",
                "密码": "u_normal_pass",
                "IP": "192.168.88.123",
                "端口": "22",
                "期待返回符": "",
                "失败返回符": "",
                "字符集": "GBK"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_netunit_add(self):
        u"""添加网元，test_auto_manual_s_telnet"""
        action = {
            "操作": "AddNetUnit",
            "参数": {
                "网元名称": "test_auto_manual_s_telnet",
                "网元类型": "MME",
                "网元IP": "192.168.88.123",
                "生产厂家": "华为",
                "设备型号": "ME60",
                "业务状态": "带业务",
                "最大并发数": "1"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_netunit_set_login_info(self):
        u"""网元设置登录信息，普通模式，本身，TELNET"""
        action = {
            "网元名称": "test_auto_manual_s_telnet",
            "登录模式": "普通模式",
            "终端配置": {
                "终端名称": "本身",
                "登录方式": "TELNET",
                "用户名": "u_normal",
                "密码": "u_normal_pass",
                "IP": "192.168.88.123",
                "端口": "23",
                "期待返回符": "",
                "失败返回符": "",
                "字符集": "GBK"
            },
            "指令配置": {
                "终端指令": [
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    },
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    }
                ],
                "登录指令": [
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    },
                    {
                        "指令内容": "",
                        "账号名称": "",
                        "期待返回符": "",
                        "失败返回符": "",
                        "隐藏输入指令": "",
                        "隐藏指令返回": "",
                        "退出命令": "",
                        "执行后等待时间": "",
                        "是否适配网元": "",
                        "字符集": "",
                        "换行符": "",
                        "指令类型": ""
                    }
                ]
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
