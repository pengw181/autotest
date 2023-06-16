# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class OrgManager(unittest.TestCase):

    log.info("装载组织结构管理配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_org_clear(self):
        u"""用户管理，组织机构配置，数据清理"""
        action = {
            "操作": "ClearOrganization",
            "参数": {
                "节点名称": "广州事业部"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_org_add(self):
        u"""用户管理，添加组织机构：广州事业部"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "${Belong}",
                "组织名称": "广州事业部"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_org_add(self):
        u"""用户管理，添加组织机构：海珠区事业办"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "广州事业部",
                "组织名称": "海珠区事业办"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_org_add(self):
        u"""用户管理，添加组织机构，同级下名称已存在"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "广州事业部",
                "组织名称": "海珠区事业办"
            }
        }
        msg = "该组织名称已存在，请重新命名"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_org_add(self):
        u"""用户管理，添加组织机构：黄埔区事业办"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "广州事业部",
                "组织名称": "黄埔区事业办"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_org_add(self):
        u"""用户管理，添加组织机构：广州塔办公室"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "海珠区事业办",
                "组织名称": "广州塔办公室"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_org_add(self):
        u"""用户管理，添加组织机构：鱼珠办公室，指定上层组织"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "海珠区事业办",
                "上级组织": "黄埔区事业办",
                "组织名称": "鱼珠办公室"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_org_update(self):
        u"""用户管理，修改组织机构，指定上层组织"""
        action = {
            "操作": "UpdateOrganization",
            "参数": {
                "节点名称": "广州塔办公室",
                "上级组织": "黄埔区事业办",
                "组织名称": "广州塔办公室2"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_org_delete(self):
        u"""用户管理，删除组织机构"""
        action = {
            "操作": "DeleteOrganization",
            "参数": {
                "节点名称": "广州塔办公室2"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_org_add(self):
        u"""用户管理，添加组织机构：广州塔办公室"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "海珠区事业办",
                "组织名称": "广州塔办公室"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_org_add(self):
        u"""用户管理，添加组织机构：中山大学办公室"""
        action = {
            "操作": "AddOrganization",
            "参数": {
                "节点名称": "海珠区事业办",
                "组织名称": "中山大学办公室"
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
