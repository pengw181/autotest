# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class LevelInfo(unittest.TestCase):

    log.info("装载网元类型测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_level_add(self):
        u"""添加网元类型，层级类型：分类，2G"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["AiSee"],
                "层级名称": "2G",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_level_add(self):
        u"""添加网元类型，层级类型：分类，3G"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["AiSee"],
                "层级名称": "3G",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_level_add(self):
        u"""添加网元类型，层级类型：分类，4G"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["AiSee"],
                "层级名称": "4G",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_level_add(self):
        u"""添加网元类型，层级类型：分类，5G"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["AiSee"],
                "层级名称": "5G",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_level_add(self):
        u"""添加网元类型，层级类型：网元类型，POP"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["5G"],
                "层级名称": "POP",
                "层级类型": "网元类型",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_level_add(self):
        u"""添加网元类型，层级类型：网元类型，AUTO"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["3G"],
                "层级名称": "AUTO",
                "层级类型": "层级与网元类型",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_level_add(self):
        u"""添加网元类型，网元名称重复"""
        action = {
            "操作": "AddLevel",
            "参数": {
                "上级层级": ["4G"],
                "层级名称": "AUTO",
                "层级类型": "层级与网元类型"
            }
        }
        msg = "当前领域存在相同层级名称,请进行修改"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_level_update(self):
        u"""修改网元类型，增加上级层级"""
        action = {
            "操作": "UpdateLevel",
            "参数": {
                "网元类型": "AUTO",
                "修改内容": {
                    "上级层级": ["2G", "3G", "4G"],
                    "层级名称": "AUTO",
                    "层级类型": "层级与网元类型"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_level_update(self):
        u"""修改网元类型，修改层级名称"""
        action = {
            "操作": "UpdateLevel",
            "参数": {
                "网元类型": "AUTO",
                "修改内容": {
                    "上级层级": ["2G", "3G", "4G"],
                    "层级名称": "AUTO1",
                    "层级类型": "层级与网元类型"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_level_update(self):
        u"""修改网元类型，修改层级名称，改回正常名称"""
        action = {
            "操作": "UpdateLevel",
            "参数": {
                "网元类型": "AUTO1",
                "修改内容": {
                    "上级层级": ["2G", "3G", "4G"],
                    "层级名称": "AUTO",
                    "层级类型": "层级与网元类型"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_level_update(self):
        u"""修改网元类型，修改分类"""
        action = {
            "操作": "UpdateLevel",
            "参数": {
                "网元类型": "3G",
                "修改内容": {
                    "上级层级": ["AiSee"],
                    "层级名称": "3GS"
                }
            }
        }
        msg = "您选择的网元类型非子层级网元类型，不能修改"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，分配全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "${LoginUser}",
                "查询条件": {
                    "名称": "",
                    "厂家": "",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "分配类型": "分配全部"
            }
        }
        msg = "分配成功"
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
