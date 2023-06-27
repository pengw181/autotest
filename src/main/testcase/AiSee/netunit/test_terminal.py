# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Terminal(unittest.TestCase):

    log.info("装载统一直连终端配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_terminal_add(self):
        u"""添加统一直连终端，auto_终端_SSH"""
        action = {
            "操作": "AddTerminal",
            "参数": {
                "终端名称": "auto_终端_SSH",
                "终端类型": "SSH",
                "账号名称": "auto_账号_常用账号",
                "字符集": "GBK",
                "期待返回符": "",
                "失败返回符": "",
                "终端IP": "%IP",
                "终端端口": "22",
                "用途": "直连网元",
                "登录指令": [],
                "搜索是否存在": "是",
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_terminal_add(self):
        u"""添加统一直连终端，auto_终端_TELNET"""
        action = {
            "操作": "AddTerminal",
            "参数": {
                "终端名称": "auto_终端_TELNET",
                "终端类型": "TELNET",
                "账号名称": "",
                "字符集": "GBK",
                "期待返回符": "ogin:",
                "失败返回符": "",
                "终端IP": "%IP",
                "终端端口": "23",
                "用途": "直连网元",
                "登录指令": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": "auto_登录指令_telnet直连网元"
                    }
                ],
                "搜索是否存在": "是",
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_terminal_add(self):
        u"""添加统一直连终端，auto_终端_终端加跳转"""
        action = {
            "操作": "AddTerminal",
            "参数": {
                "终端名称": "auto_终端_终端加跳转",
                "终端类型": "TELNET",
                "账号名称": "",
                "字符集": "GBK",
                "期待返回符": "ogin:",
                "失败返回符": "",
                "终端IP": "192.168.88.123",
                "终端端口": "23",
                "用途": "终端加跳转",
                "登录指令": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": "auto_登录指令_telnet直连网元"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": "auto_登录指令_跳转指令"
                    }
                ],
                "搜索是否存在": "是",
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_terminal_add(self):
        u"""添加统一直连终端，auto_终端_异常终端"""
        action = {
            "操作": "AddTerminal",
            "参数": {
                "终端名称": "auto_终端_异常终端",
                "终端类型": "TELNET",
                "账号名称": "",
                "字符集": "GBK",
                "期待返回符": "ogin:",
                "失败返回符": "",
                "终端IP": "192.168.88.123",
                "终端端口": "23",
                "用途": "终端加跳转",
                "登录指令": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": "auto_登录指令_telnet直连网元"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": "auto_登录指令_异常跳转指令"
                    }
                ],
                "搜索是否存在": "是",
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
