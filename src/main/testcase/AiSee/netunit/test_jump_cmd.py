# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class MidJumpCmd(unittest.TestCase):

    log.info("装载统一登录指令配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_ssh直连网元"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_ssh直连网元",
                "登录指令用途": "ssh直连网元",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "assword",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_telnet直连网元"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_telnet直连网元",
                "登录指令用途": "telnet直连网元",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "assword:",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_错误账号"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_错误账号",
                "登录指令用途": "终端使用错误账号",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_测试异常账号",
                            "期待返回符": "assword",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_测试异常账号",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_空账号"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_空账号",
                "登录指令用途": "终端使用空账号",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_空账号模版",
                            "期待返回符": "assword:",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_空账号模版",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_跳转指令"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_跳转指令",
                "登录指令用途": "跳转指令",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "telnet %IP",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "ogin:",
                            "失败返回符": "",
                            "隐藏输入指令": "是",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "3",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "assword:",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_常用账号",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_jump_cmd_temp_add(self):
        u"""添加统一登录指令，auto_登录指令_异常跳转指令"""
        action = {
            "操作": "AddJumpCmdTemp",
            "参数": {
                "登录指令名称": "auto_登录指令_异常跳转指令",
                "登录指令用途": "异常跳转指令",
                "指令配置": [
                    {
                        "操作类型": "删除"
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "telnet %IP",
                            "账号名称": "",
                            "期待返回符": "ogin:",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "3",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%USERNAME",
                            "账号名称": "auto_账号_测试异常账号",
                            "期待返回符": "assword:",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    },
                    {
                        "操作类型": "添加",
                        "指令信息": {
                            "指令内容": "%PASSWORD",
                            "账号名称": "auto_账号_测试异常账号",
                            "期待返回符": "",
                            "失败返回符": "",
                            "隐藏输入指令": "否",
                            "隐藏指令返回": "",
                            "退出命令": "",
                            "执行后等待时间": "",
                            "是否适配网元": "是",
                            "字符集": "GBK",
                            "换行符": r"\n"
                        }
                    }
                ],
                "搜索是否存在": "是"
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
