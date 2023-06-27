# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Account(unittest.TestCase):

    log.info("装载统一账号配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_account_temp_add(self):
        u"""添加账号模版，auto_账号_常用账号"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号模版类型": "本身",
                "账号模版用途": "登录系统",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_account_temp_add(self):
        u"""添加账号模版，auto_账号_测试异常账号"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_测试异常账号",
                "账号模版类型": "中转",
                "账号模版用途": "测试异常情况",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_account_temp_add(self):
        u"""添加账号模版，重复添加"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_测试异常账号",
                "账号模版类型": "中转",
                "账号模版用途": "登录系统"
            }
        }
        msg = "账号名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_account_clear(self):
        u"""账号清理，账号模版：auto_账号_常用账号"""
        action = {
            "操作": "AccountDataClear",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "创建人": "${CurrentUser}"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_5_account_add(self):
        u"""添加账号，公有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "公有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_account_add(self):
        u"""添加账号，私有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "私有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_account_add(self):
        u"""添加账号，当前账号模版存在公有账号，且本人已创建过私有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "私有",
                "用户名": "u_normal2",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加失败，您的公有、私有账号均已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_account_update(self):
        u"""修改账号，修改公有账号"""
        action = {
            "操作": "UpdateAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "公有",
                "修改内容": {
                    "用户名": "u_normal1",
                    "密码": "u_normal_pass1"
                }
            }
        }
        msg = "修改成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_account_update(self):
        u"""修改账号，修改私有账号"""
        action = {
            "操作": "UpdateAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "私有",
                "创建人": "${CurrentUser}",
                "修改内容": {
                    "用户名": "u_normal2",
                    "密码": "u_normal_pass2"
                }
            }
        }
        msg = "修改成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_account_delete(self):
        u"""删除账号，公有账号"""
        action = {
            "操作": "DeleteAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "公有",
                "创建人": "${CurrentUser}"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_account_delete(self):
        u"""删除账号，私有账号"""
        action = {
            "操作": "DeleteAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "私有",
                "创建人": "${CurrentUser}"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_account_add(self):
        u"""添加账号，公有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "公有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_account_add(self):
        u"""添加账号，私有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_常用账号",
                "账号作用域": "私有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_account_clear(self):
        u"""账号清理，账号模版：auto_账号_测试异常账号"""
        action = {
            "操作": "AccountDataClear",
            "参数": {
                "账号模版名称": "auto_账号_测试异常账号",
                "创建人": "${CurrentUser}"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_15_account_add(self):
        u"""添加账号，公有账号，错误用户名"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_测试异常账号",
                "账号作用域": "公有",
                "用户名": "u_normal1",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_account_add(self):
        u"""添加账号，私有账号，错误密码"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_测试异常账号",
                "账号作用域": "私有",
                "用户名": "u_normal",
                "密码": "u_normal_pass1"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_account_temp_add(self):
        u"""添加账号模版，auto_账号_空账号模版"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_空账号模版",
                "账号模版类型": "中转",
                "账号模版用途": "空账号模版",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_account_clear(self):
        u"""账号清理，账号模版：auto_账号_空账号模版"""
        action = {
            "操作": "AccountDataClear",
            "参数": {
                "账号模版名称": "auto_账号_空账号模版",
                "创建人": "${CurrentUser}"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_19_account_temp_add(self):
        u"""添加账号模版，auto_账号_公有账号"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_公有账号",
                "账号模版类型": "中转",
                "账号模版用途": "只含公有账号",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_account_clear(self):
        u"""账号清理，账号模版：auto_账号_公有账号"""
        action = {
            "操作": "AccountDataClear",
            "参数": {
                "账号模版名称": "auto_账号_公有账号",
                "创建人": "${CurrentUser}"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_21_account_add(self):
        u"""添加账号，公有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_公有账号",
                "账号作用域": "公有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_account_temp_add(self):
        u"""添加账号模版，auto_账号_私有账号"""
        action = {
            "操作": "AddAccountTemp",
            "参数": {
                "账号模版名称": "auto_账号_私有账号",
                "账号模版类型": "中转",
                "账号模版用途": "只含私有账号",
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_account_clear(self):
        u"""账号清理，账号模版：auto_账号_私有账号"""
        action = {
            "操作": "AccountDataClear",
            "参数": {
                "账号模版名称": "auto_账号_私有账号",
                "创建人": "${CurrentUser}"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_24_account_add(self):
        u"""添加账号，私有账号"""
        action = {
            "操作": "AddAccount",
            "参数": {
                "账号模版名称": "auto_账号_私有账号",
                "账号作用域": "私有",
                "用户名": "u_normal",
                "密码": "u_normal_pass"
            }
        }
        msg = "添加成功"
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
