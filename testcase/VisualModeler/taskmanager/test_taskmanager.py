# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class TaskManager(unittest.TestCase):

    log.info("装载任务配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")

    def test_1_task_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_测试流程"
            }
        }
        # noinspection PyBroadException
        try:
            self.worker.action(action)
        except Exception:
            raise AssertionError("清理流程失败")

    def tearDown(self):     # 最后执行的函数
        self.browser = get_global_var("browser")
        # screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
