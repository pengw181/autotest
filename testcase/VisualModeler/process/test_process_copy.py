# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/10/13 上午11:47

import unittest
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class CopyProcess(unittest.TestCase):

    log.info("装载复制流程测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_copy_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_copy(self):
        u"""复制流程，不含子流程，使用自动生成的流程名称"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "主流程名称": "auto_copy_AI节点流程",
                "子流程名称列表": [
                    ["auto_子流程_正常", "auto_copy_子流程_正常"],
                    ["auto_子流程_异常", "auto_copy_子流程_异常"]
                ]
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_2_process_copy(self):
        u"""复制流程，含子流程，修改流程名称"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "主流程名称": "auto_copy_AI节点流程",
                "子流程名称列表": [
                    ["auto_子流程_正常", "auto_copy_子流程_正常"],
                    ["auto_子流程_异常", "auto_copy_子流程_异常"]
                ]
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        # screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
