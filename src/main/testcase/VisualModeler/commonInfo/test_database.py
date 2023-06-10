# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/30 下午6:58

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Database(unittest.TestCase):

    log.info("装载数据库配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_database_clear(self):
        u"""数据库配置管理，数据清理"""
        pre = """
        ${Database}.main|delete from tn_db_cfg where db_name like 'auto_%'
        """
        action = {
            "操作": "DBDataClear",
            "参数": {
                "数据库名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_database_add(self):
        u"""添加mysql数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库",
                "数据库驱动": "mysql",
                "数据库URL": "jdbc:mysql://192.168.88.116:3306/aisee1",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "私有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_database_add(self):
        u"""添加数据库,名称本领域存在"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库",
                "数据库驱动": "mysql",
                "数据库URL": "jdbc:mysql://192.168.88.116:3306/aisee1",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "私有"
            }
        }
        msg = "数据库名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_database_test(self):
        u"""测试mysql数据库连通性"""
        action = {
            "操作": "TestDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_database_add(self):
        u"""添加oracle数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_oracle数据库",
                "数据库驱动": "oracle",
                "数据库URL": "jdbc:oracle:thin:@192.168.88.116:2310/AiSee",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_database_test(self):
        u"""测试oracle数据库连通性"""
        action = {
            "操作": "TestDatabase",
            "参数": {
                "数据库名称": "auto_oracle数据库"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_database_add(self):
        u"""添加postgres数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_postgres数据库",
                "数据库驱动": "postgresql",
                "数据库URL": "jdbc:postgresql://192.168.88.116:4310/postgres",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_database_test(self):
        u"""测试postgres数据库连通性"""
        action = {
            "操作": "TestDatabase",
            "参数": {
                "数据库名称": "auto_postgres数据库"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_database_update(self):
        u"""修改数据库"""
        action = {
            "操作": "UpdateDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库",
                "修改内容": {
                    "数据库名称": "auto_mysql数据库",
                    "数据库驱动": "mysql",
                    "数据库URL": "jdbc:mysql://192.168.88.116:3306/aisee1",
                    "用户名": "aisee1",
                    "密码": "aisee2_pass",
                    "归属类型": "外部库",
                    "数据类型": "公有"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_database_test(self):
        u"""测试mysql数据库连通性，密码错误"""
        action = {
            "操作": "TestDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库"
            }
        }
        msg = "测试失败：数据库URL、用户名或密码错误"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_database_delete(self):
        u"""删除oracle数据库"""
        action = {
            "操作": "DeleteDatabase",
            "参数": {
                "数据库名称": "auto_oracle数据库"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_database_delete(self):
        u"""删除mysql数据库"""
        action = {
            "操作": "DeleteDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_database_delete(self):
        u"""删除postgres数据库"""
        action = {
            "操作": "DeleteDatabase",
            "参数": {
                "数据库名称": "auto_postgres数据库"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_database_add(self):
        u"""添加数据库，oracle数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_oracle数据库",
                "数据库驱动": "oracle",
                "数据库URL": "jdbc:oracle:thin:@192.168.88.116:2310/AiSee",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_database_add(self):
        u"""添加数据库，mysql数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_mysql数据库",
                "数据库驱动": "mysql",
                "数据库URL": "jdbc:mysql://192.168.88.116:3306/aisee1",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "私有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_database_add(self):
        u"""添加数据库，postgres数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_postgres数据库",
                "数据库驱动": "postgresql",
                "数据库URL": "jdbc:postgresql://192.168.88.116:4310/postgres",
                "用户名": "aisee1",
                "密码": "aisee1_pass",
                "归属类型": "外部库",
                "数据类型": "私有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_database_add(self):
        u"""添加数据库，oushu数据库"""
        action = {
            "操作": "AddDatabase",
            "参数": {
                "数据库名称": "auto_oushu数据库",
                "数据库驱动": "postgresql",
                "数据库URL": "jdbc:postgresql://192.168.91.171:5432/postgres",
                "用户名": "oushu",
                "密码": "lavaadmin",
                "归属类型": "外部库",
                "数据类型": "私有"
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
