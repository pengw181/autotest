# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class VendorModel(unittest.TestCase):

    log.info("装载设备厂家测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_vendor_add(self):
        u"""添加厂家，测试"""
        action = {
            "操作": "AddVendor",
            "参数": {
                "厂家中文名": "测试",
                "厂家英文名": "TEST",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_vendor_add(self):
        u"""添加厂家，图科"""
        action = {
            "操作": "AddVendor",
            "参数": {
                "厂家中文名": "图科",
                "厂家英文名": "TURK",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_vendor_add(self):
        u"""添加厂家，思旗"""
        action = {
            "操作": "AddVendor",
            "参数": {
                "厂家中文名": "思旗",
                "厂家英文名": "SEARCH",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_vendor_add(self):
        u"""添加厂家，重复添加"""
        action = {
            "操作": "AddVendor",
            "参数": {
                "厂家中文名": "思旗",
                "厂家英文名": "SEARCH1"
            }
        }
        msg = "厂家已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_vendor_update(self):
        u"""修改厂家，思旗"""
        action = {
            "操作": "UpdateVendor",
            "参数": {
                "查询条件": {
                    "厂家": "思旗"
                },
                "修改内容": {
                    "厂家中文名": "思旗二代",
                    "厂家英文名": "SEARCH2"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_vendor_update(self):
        u"""修改厂家，中文名已存在"""
        action = {
            "操作": "UpdateVendor",
            "参数": {
                "查询条件": {
                    "厂家": "思旗二代"
                },
                "修改内容": {
                    "厂家中文名": "图科",
                    "厂家英文名": "SEARCH2"
                }
            }
        }
        msg = "厂家已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_vendor_update(self):
        u"""修改厂家，英文名已存在"""
        action = {
            "操作": "UpdateVendor",
            "参数": {
                "查询条件": {
                    "厂家": "思旗二代"
                },
                "修改内容": {
                    "厂家中文名": "思旗",
                    "厂家英文名": "TURK"
                }
            }
        }
        msg = "厂家已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_vendor_update(self):
        u"""修改厂家，改回正常值"""
        action = {
            "操作": "UpdateVendor",
            "参数": {
                "查询条件": {
                    "厂家": "思旗二代"
                },
                "修改内容": {
                    "厂家中文名": "思旗",
                    "厂家英文名": "SEARCH"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_model_add(self):
        u"""添加设备型号，厂家：图科，设备型号：TKing"""
        action = {
            "操作": "AddModel",
            "参数": {
                "所属厂家": "图科",
                "设备型号": "TKing",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_model_add(self):
        u"""添加设备型号，厂家：图科，设备型号：TKea"""
        action = {
            "操作": "AddModel",
            "参数": {
                "所属厂家": "图科",
                "设备型号": "TKea",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_model_add(self):
        u"""添加设备型号，厂家：思旗，设备型号：Sight"""
        action = {
            "操作": "AddModel",
            "参数": {
                "所属厂家": "思旗",
                "设备型号": "Sight",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_model_add(self):
        u"""添加设备型号，厂家：测试，设备型号：AutoTest"""
        action = {
            "操作": "AddModel",
            "参数": {
                "所属厂家": "测试",
                "设备型号": "AutoTest",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_model_add(self):
        u"""添加设备型号，重复添加"""
        action = {
            "操作": "AddModel",
            "参数": {
                "所属厂家": "图科",
                "设备型号": "TKea"
            }
        }
        msg = "设备型号已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_vendor_update(self):
        u"""修改设备型号，同厂家下设备型号已存在"""
        action = {
            "操作": "UpdateModel",
            "参数": {
                "查询条件": {
                    "厂家": "图科",
                    "设备型号": "TKea"
                },
                "修改内容": {
                    "设备型号": "TKing"
                }
            }
        }
        msg = "设备型号已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_vendor_update(self):
        u"""修改设备型号，不同厂家下设备型号已存在"""
        action = {
            "操作": "UpdateModel",
            "参数": {
                "查询条件": {
                    "厂家": "图科",
                    "设备型号": "TKea"
                },
                "修改内容": {
                    "设备型号": "Sight"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_vendor_update(self):
        u"""修改设备型号，改回原值"""
        action = {
            "操作": "UpdateModel",
            "参数": {
                "查询条件": {
                    "厂家": "图科",
                    "设备型号": "Sight"
                },
                "修改内容": {
                    "设备型号": "TKea"
                }
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
