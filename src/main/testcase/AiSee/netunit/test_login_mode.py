# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class LoginMode(unittest.TestCase):

    log.info("装载网元登录模式测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_login_mode_add(self):
        u"""添加网元登录模式，SSH模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "AUTO",
                "登录模式名称": "SSH模式",
                "登录模式描述": "SSH登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_login_mode_add(self):
        u"""添加网元登录模式，TELNET模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "AUTO",
                "登录模式名称": "TELNET模式",
                "登录模式描述": "TELNET登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_login_mode_add(self):
        u"""添加网元登录模式，空模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "AUTO",
                "登录模式名称": "空模式",
                "登录模式描述": "空登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_login_mode_add(self):
        u"""添加网元登录模式，异常模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "AUTO",
                "登录模式名称": "异常模式",
                "登录模式描述": "异常登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_login_mode_add(self):
        u"""添加网元登录模式，普通模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "POP",
                "登录模式名称": "普通模式",
                "登录模式描述": "普通登录模式"
            }
        }
        msg = "登录模式名称重复"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_login_mode_add(self):
        u"""添加网元登录模式，网元类型不同，登录模式名称相同"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "POP",
                "登录模式名称": "TELNET模式",
                "登录模式描述": "TELNET登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_login_mode_add(self):
        u"""添加网元登录模式，重复添加"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "AUTO",
                "登录模式名称": "TELNET模式",
                "登录模式描述": "TELNET登录模式"
            }
        }
        msg = "登录模式名称重复"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_login_mode_update(self):
        u"""修改网元登录模式"""
        action = {
            "操作": "UpdateLoginMode",
            "参数": {
                "查询条件": {
                    "网元类型": "AUTO",
                    "登录模式名称": "空模式",
                },
                "修改内容": {
                    "登录模式名称": "空模式1",
                    "登录模式描述": "空登录模式1"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_login_mode_update(self):
        u"""修改网元登录模式，改回原值"""
        action = {
            "操作": "UpdateLoginMode",
            "参数": {
                "查询条件": {
                    "网元类型": "AUTO",
                    "登录模式名称": "空模式1",
                },
                "修改内容": {
                    "登录模式名称": "空模式",
                    "登录模式描述": "空登录模式"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_login_mode_add(self):
        u"""添加网元登录模式，网元类型：MME，TELNET模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "MME",
                "登录模式名称": "TELNET模式",
                "登录模式描述": "TELNET登录模式",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_login_mode_add(self):
        u"""添加网元登录模式，网元类型：CSCE，TELNET模式"""
        action = {
            "操作": "AddLoginMode",
            "参数": {
                "网元类型": "CSCE",
                "登录模式名称": "TELNET模式",
                "登录模式描述": "TELNET登录模式",
                "搜索是否存在": "是"
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
