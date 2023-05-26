# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/1 下午3:13

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class RegexTpl(unittest.TestCase):

    log.info("装载正则模版配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_regex_clear(self):
        u"""正则模版管理，数据清理"""
        action = {
            "操作": "RegexpDataClear",
            "参数": {
                "正则模版名称": "auto_正则模版_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_regex_add(self):
        u"""添加正则模版，auto_正则模版_匹配日期"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_匹配日期",
                "模版描述": "auto_正则模版_匹配日期，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "日期",
                            "时间格式": "2014-05-28 12:30:00",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_regex_add(self):
        u"""添加正则模版，auto_正则模版_分段"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_分段",
                "模版描述": "auto_正则模版_分段，勿删",
                "正则魔方": {
                    "高级模式": "是",
                    "表达式": "time=(\\d+\\.?\\d*)\\s+ms"
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_regex_add(self):
        u"""添加正则模版，auto_正则模版_ping延迟时间"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_ping延迟时间",
                "模版描述": "auto_正则模版_ping延迟时间，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "自定义文本",
                            "自定义值": "time=",
                            "是否取值": "无"
                        },
                        {
                            "标签": "数字",
                            "匹配小数": "是",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "空格",
                            "长度": "1到多个",
                            "是否取值": "无"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": "ms",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_regex_add(self):
        u"""添加正则模版，auto_正则模版_匹配数字"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_匹配数字",
                "模版描述": "auto_正则模版_匹配数字，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "数字",
                            "长度": "1到多个",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_regex_add(self):
        u"""添加正则模版，auto_正则模版_匹配逗号"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_匹配逗号",
                "模版描述": "auto_正则模版_匹配逗号，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "自定义文本",
                            "自定义值": ",",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_regex_add(self):
        u"""添加正则模版，auto_正则模版_匹配成员文件名"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_匹配成员文件名",
                "模版描述": "auto_正则模版_匹配成员文件名，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "自定义文本",
                            "自定义值": "成员-",
                            "是否取值": "无"
                        },
                        {
                            "标签": "任意中文字符",
                            "长度": "1到多个",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_regex_add(self):
        u"""添加正则模版，auto_正则模版_获取丢包率"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_获取丢包率",
                "模版描述": "auto_正则模版_获取丢包率，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "任意非空格",
                            "长度": "1到多个",
                            "是否取值": "无"
                        },
                        {
                            "标签": "空格",
                            "长度": "1到多个",
                            "是否取值": "无"
                        },
                        {
                            "标签": "数字",
                            "长度": "1到多个",
                            "匹配%": "是",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "空格",
                            "长度": "1到多个",
                            "是否取值": "无"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": "packet loss",
                            "是否取值": "无"
                        },
                        {
                            "标签": "任意字符",
                            "长度": "1到多个",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_regex_add(self):
        u"""添加正则模版，auto_正则模版_time特征行"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_time特征行",
                "模版描述": "auto_正则模版_time特征行，勿删",
                "正则魔方": {
                    "高级模式": "是",
                    "表达式": "time=(\\d+\\.?\\d*)\\s+ms",
                    "开启验证": "是",
                    "样例数据": "ping_sample.txt"
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_regex_add(self):
        u"""添加正则模版，auto_正则模版_password"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_password",
                "模版描述": "auto_正则模版_password，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "字母",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "字母",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "数字",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "数字",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "任意字符",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "任意字符",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": ":",
                            "是否取值": "无"
                        },
                        {
                            "标签": "任意字符",
                            "长度": "1到多个",
                            "是否取值": "绿色"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_regex_add(self):
        u"""添加正则模版，auto_正则模版_measInfoId段开始"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_measInfoId段开始",
                "模版描述": "auto_正则模版_measInfoId段开始，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "自定义文本",
                            "自定义值": "measInfo measInfoId=\"",
                            "是否取值": "无"
                        },
                        {
                            "标签": "数字",
                            "长度": "1到多个",
                            "是否取值": "无"
                        },
                        {
                            "标签": "自定义文本",
                            "自定义值": "\"",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_regex_add(self):
        u"""添加正则模版，auto_正则模版_measInfoId段结束"""
        action = {
            "操作": "AddRegexpTemp",
            "参数": {
                "正则模版名称": "auto_正则模版_measInfoId段结束",
                "模版描述": "auto_正则模版_measInfoId段结束，勿删",
                "正则魔方": {
                    "标签配置": [
                        {
                            "标签": "自定义文本",
                            "自定义值": "</measInfo>",
                            "是否取值": "无"
                        }
                    ]
                }
            }
        }
        msg = "正则模版保存成功"
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
