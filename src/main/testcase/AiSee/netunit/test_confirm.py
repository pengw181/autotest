# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class LoginConfirm(unittest.TestCase):

    log.info("装载登录配置确认测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_confirm_selected(self):
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

    def test_2_confirm_all(self):
        u"""登录配置确认，确认全部"""
        action = {
            "操作": "ConfirmAll",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKea"
                }
            }
        }
        msg = "确认成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_cancel_selected(self):
        u"""登录配置确认，取消配置下发"""
        action = {
            "操作": "CancelSelected",
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
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_confirm_all(self):
        u"""登录配置确认，无登录配置信息需要确认，确认全部"""
        action = {
            "操作": "ConfirmAll",
            "参数": {
                "查询条件": {
                    "网元名称": "auto_TURK",
                    "网元类型": "AUTO",
                    "生产厂家": "图科",
                    "设备型号": "TKea"
                }
            }
        }
        msg = "无登录配置确认信息"
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
