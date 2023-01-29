# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from service.gooflow.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class Field(unittest.TestCase):

    log.info("装载专业领域配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_field_clear(self):
        u"""专业领域管理，数据清理"""
        action = {
            "操作": "FieldDataClear",
            "参数": {
                "专业领域名称": "pw领域"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_field_add(self):
        u"""添加专业领域"""
        action = {
            "操作": "AddField",
            "参数": {
                "专业领域名称": "pw领域"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_field_add(self):
        u"""添加专业领域，专业名称本领域存在"""
        action = {
            "操作": "AddField",
            "参数": {
                "专业领域名称": "pw领域"
            }
        }
        msg = "该专业领域名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_field_update(self):
        u"""修改专业领域名称"""
        action = {
            "操作": "UpdateField",
            "参数": {
                "专业领域名称": "pw领域",
                "修改内容": {
                    "专业领域名称": "pw领域新"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_field_delete(self):
        u"""删除专业领域"""
        action = {
            "操作": "DeleteField",
            "参数": {
                "专业领域名称": "pw领域新"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_field_clear(self):
        u"""专业领域管理，数据清理"""
        action = {
            "操作": "FieldDataClear",
            "参数": {
                "专业领域名称": "auto域"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_7_field_add(self):
        u"""添加专业领域，auto域"""
        action = {
            "操作": "AddField",
            "参数": {
                "专业领域名称": "auto域"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):     # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
