# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class ConnectTestReport(unittest.TestCase):

    log.info("装载连通测试报告测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_connect_test_report(self):
        u"""连通测试报告，获取测试结果汇总"""
        action = {
            "操作": "GetConnectReport",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        msg = "正常：3条，异常：0条，测试中：0条"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_connect_test_report_detail(self):
        u"""连通测试报告，查看登录日志详情"""
        action = {
            "操作": "GetConnectDetailLog",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                },
                "网元名称": "auto_TURK_TKea1"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_3_connect_retest(self):
        u"""连通测试报告，重新测试"""
        action = {
            "操作": "ConnectRetest",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                }
            }
        }
        msg = "设备测试中,请等待"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_connect_detail_retest(self):
        u"""连通测试报告，登录详情页重新测试"""
        action = {
            "操作": "ConnectDetailRetest",
            "参数": {
                "查询条件": {
                    "触发用户": "${CurrentUser}",
                    "测试类型": "网元设备"
                },
                "网元名称": "auto_TURK_TKea1"
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
