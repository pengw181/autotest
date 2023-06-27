# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class ConnectTest(unittest.TestCase):

    log.info("装载网元连通性测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_connect_test_selected(self):
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

    def test_2_connect_test_all(self):
        u"""连通性测试，测试全部"""
        action = {
            "操作": "TestAllNetunit",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKea"
                }
            }
        }
        msg = "设备测试中,请等待"
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
