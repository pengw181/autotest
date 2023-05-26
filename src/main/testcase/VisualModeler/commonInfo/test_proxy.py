# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 上午10:15

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Proxy(unittest.TestCase):

    log.info("装载代理配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_proxy_clear(self):
        u"""代理管理，数据清理"""
        action = {
            "操作": "ProxyDataClear",
            "参数": {
                "代理名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_proxy_add(self):
        u"""添加代理配置"""
        action = {
            "操作": "AddProxy",
            "参数": {
                "代理名称": "auto_代理",
                "代理服务器": "192.168.88.1",
                "代理端口": "8080",
                "代理用户名": "proxy",
                "代理密码": "proxy_pass",
                "代理协议": "socks",
                "是否有效": "有效",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_proxy_update(self):
        u"""修改代理配置"""
        action = {
            "操作": "UpdateProxy",
            "参数": {
                "代理名称": "auto_代理",
                "修改内容": {
                    "代理名称": "auto_代理1",
                    "代理服务器": "192.168.88.2",
                    "代理端口": "8081",
                    "代理用户名": "proxy1",
                    "代理密码": "proxy_pass1",
                    "代理协议": "http",
                    "是否有效": "无效",
                    "数据类型": "私有"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_proxy_delete(self):
        u"""删除代理配置"""
        action = {
            "操作": "DeleteProxy",
            "参数": {
                "代理名称": "auto_代理1"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_field_add(self):
        u"""添加代理配置"""
        action = {
            "操作": "AddProxy",
            "参数": {
                "代理名称": "auto_代理",
                "代理服务器": "192.168.88.1",
                "代理端口": "8080",
                "代理用户名": "proxy",
                "代理密码": "proxy_pass",
                "代理协议": "socks",
                "是否有效": "有效",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
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
