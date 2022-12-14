# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 上午9:39

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class RulerX(unittest.TestCase):

    log.info("装载指令集配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_ruler_clear(self):
        u"""通用解析模版，数据清理"""
        pres = """
        ${Database}.main|delete from rulerx_analyzer_app_rela where analyzer_id in (select analyzer_id from rulerx_analyzer where analyzer_name like 'auto_%') and belong_id='${BelongID}' and domain_id='${DomainID}'
        """
        action = {
            "操作": "RulerXDataClear",
            "参数": {
                "解析模版名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_ruler_add(self):
        u"""添加指令解析模版，解析ping指令"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_解析模板_解析ping",
                    "模版说明": "auto_解析模板_解析ping说明"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "是"
                },
                "格式化二维表配置": {
                    "解析开始行": "1",
                    "通过正则匹配数据列": "是",
                    "正则魔方": {
                        "设置方式": "添加",
                        "正则模版名称": "auto_正则解析ping",
                        "标签配置": [
                            {
                                "标签": "任意字符",
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
                                "是否取值": "绿色"
                            },
                            {
                                "标签": "自定义文本",
                                "自定义值": "%",
                                "是否取值": "无"
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
                    },
                    "样例数据": "ping_sample.txt"
                },
                "选择判断规则": "二维表结果判断",
                "判断规则配置": {
                    "目标行": "所有行",
                    "行结果关系": "或",
                    "规则管理": [
                        {
                            "列名": "列1",
                            "关系": "不等于",
                            "匹配值": "0",
                            "条件满足时": "异常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "出现丢包情况"
                        }
                    ]
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_ruler_add(self):
        u"""添加指令解析模版，解析date指令"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_解析模板_解析date",
                    "模版说明": "auto_解析模板_解析date说明"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "是"
                },
                "格式化二维表配置": {
                    "解析开始行": "1",
                    "通过正则匹配数据列": "是",
                    "正则魔方": {
                        "设置方式": "添加",
                        "正则模版名称": "auto_正则解析date",
                        "标签配置": [
                            {
                                "标签": "任意字符",
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
                                "标签": "任意字符",
                                "长度": "1到多个",
                                "是否取值": "无"
                            }
                        ]
                    },
                    "样例数据": "date_sample.txt"
                },
                "选择判断规则": "无需判断"
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_ruler_add(self):
        u"""添加指令解析模版，解析板卡状态"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_解析模板_解析板卡状态",
                    "模版说明": "auto_解析模板_解析板卡状态说明"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "是"
                },
                "格式化二维表配置": {
                    "解析开始行": "1",
                    "通过正则匹配数据列": "是",
                    "正则魔方": {
                        "设置方式": "添加",
                        "正则模版名称": "auto_正则解析板卡状态",
                        "高级模式": "是",
                        "表达式": "(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(\\w+)\\s+(\\w+)\\s+(\\w+)"
                    },
                    "样例数据": "board_status_sample.txt"
                },
                "选择判断规则": "二维表结果判断",
                "判断规则配置": {
                    "目标行": "所有行",
                    "行结果关系": "且",
                    "规则管理": [
                        {
                            "列名": "列5",
                            "关系": "等于",
                            "匹配值": "Normal",
                            "条件满足时": "正常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "板卡状态出现异常"
                        }
                    ]
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_ruler_add(self):
        u"""添加指令解析模版，数据拼盘分段模式使用"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_解析模板_分段",
                    "模版说明": "auto_解析模板_分段，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "time",
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_ping延迟时间"
                            }
                        }
                    ],
                    "关键字值比较结果关系": "或",
                    "规则管理": [
                        {
                            "列名": "time",
                            "关系": "大于等于",
                            "匹配值": "0.8",
                            "条件满足时": "异常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "延时过高"
                        }
                    ],
                    "样例数据": "ping_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_ruler_add(self):
        u"""添加指令解析模版，数据拼盘列更新模式使用"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_解析模板_列更新",
                    "模版说明": "auto_解析模板_列更新，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "丢包率",
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_获取丢包率"
                            }
                        }
                    ],
                    "关键字值比较结果关系": "或",
                    "规则管理": [
                        {
                            "列名": "丢包率",
                            "关系": "等于",
                            "匹配值": "0%",
                            "条件满足时": "正常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "网络波动"
                        }
                    ],
                    "样例数据": "ping_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_ruler_add(self):
        u"""添加指令解析模版，分段+匹配关键字判断"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_分段+匹配关键字判断",
                    "模版说明": "auto_分段+匹配关键字判断，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "是",
                    "格式化成二维表": "否"
                },
                "分段规则配置": {
                    "段开始特征行": {
                        "设置方式": "选择",
                        "正则模版名称": "auto_正则模版_measInfoId段开始"
                    },
                    "段结束特征行": {
                        "设置方式": "选择",
                        "正则模版名称": "auto_正则模版_measInfoId段结束"
                    },
                    "样例数据": "measinfo_sample.txt",
                    "抽取头部字段": "否"
                },
                "选择判断规则": "匹配关键字判断",
                "判断规则配置": {
                    "关键字": "SC_SC_CD_UDM700FE02_B_HW",
                    "忽略大小写": "是",
                    "段结果关系": "或",
                    "条件满足时": "异常",
                    "异常提示信息": "未匹配到关键字",
                    "样例数据": "measinfo_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_ruler_add(self):
        u"""添加指令解析模版，分段+结果行数判断"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_分段+结果行数判断",
                    "模版说明": "auto_分段+结果行数判断，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "是",
                    "格式化成二维表": "否"
                },
                "分段规则配置": {
                    "段开始特征行": {
                        "设置方式": "选择",
                        "正则模版名称": "auto_正则模版_measInfoId段开始"
                    },
                    "段结束特征行": {
                        "设置方式": "选择",
                        "正则模版名称": "auto_正则模版_measInfoId段结束"
                    },
                    "样例数据": "measinfo_sample.txt",
                    "抽取头部字段": "否"
                },
                "选择判断规则": "结果行数判断",
                "判断规则配置": {
                    "条件": "不等于",
                    "行数": "10",
                    "段结果关系": "且",
                    "条件满足时": "异常",
                    "异常提示信息": "日志结果行数不匹配",
                    "下发指令": "",
                    "样例数据": "measinfo_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_ruler_add(self):
        u"""添加指令解析模版，匹配关键字的值比较判断"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_匹配关键字的值比较判断",
                    "模版说明": "auto_匹配关键字的值比较判断，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "行数",
                            "抓取行": ["1", ""],
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_password"
                            },
                            "取值": "取所有匹配值",
                            "将结果转成16进制": "否",
                            "统计个数": "是"
                        }
                    ],
                    "规则管理": [
                        {
                            "列名": "行数",
                            "关系": "等于",
                            "匹配值": "10",
                            "条件满足时": "正常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "行数不匹配"
                        }
                    ],
                    "样例数据": "password_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_ruler_add(self):
        u"""添加指令解析模版，数据拼盘分段模式使用"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_数据拼盘分段模式",
                    "模版说明": "auto_数据拼盘分段模式，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "time",
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_ping延迟时间"
                            }
                        }
                    ],
                    "关键字值比较结果关系": "或",
                    "规则管理": [
                        {
                            "列名": "time",
                            "关系": "大于等于",
                            "匹配值": "0.8",
                            "条件满足时": "异常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "延时过高"
                        }
                    ],
                    "样例数据": "ping_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_ruler_add(self):
        u"""添加指令解析模版，数据拼盘列更新模式使用"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_数据拼盘列更新模式",
                    "模版说明": "auto_数据拼盘列更新模式，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "丢包率",
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_获取丢包率"
                            }
                        }
                    ],
                    "关键字值比较结果关系": "或",
                    "规则管理": [
                        {
                            "列名": "丢包率",
                            "关系": "等于",
                            "匹配值": "0%",
                            "条件满足时": "正常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "网络波动"
                        }
                    ],
                    "样例数据": "ping_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_ruler_add(self):
        u"""添加指令解析模版，匹配关键字的值比较判断，添加变量配置"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_匹配关键字的值比较判断，添加变量配置",
                    "模版说明": "auto_匹配关键字的值比较判断，添加变量配置，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "否"
                },
                "选择判断规则": "匹配关键字的值比较判断",
                "判断规则配置": {
                    "关键字配置": [
                        {
                            "关键字": "行数",
                            "抓取行": ["1", ""],
                            "正则魔方": {
                                "设置方式": "选择",
                                "正则模版名称": "auto_正则模版_password"
                            },
                            "取值": "取所有匹配值",
                            "将结果转成16进制": "否",
                            "统计个数": "是"
                        }
                    ],
                    "关键字值比较结果关系": "或",
                    "变量配置": [
                        {
                            "变量模式": "常用变量",
                            "变量名称": "前1天(YYYY-MM-DD)"
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "行数加1",
                            "变量类型": "关键字运算",
                            "变量描述": "取行数加1结果",
                            "运算规则配置": [
                                ["", "行数", "+", "1", ""]
                            ]
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "前一天",
                            "变量类型": "时间类型",
                            "变量描述": "前一天时间",
                            "时间配置": {
                                "时间格式": "yyyyMMddHHmmss",
                                "间隔": "-1",
                                "单位": "天"
                            }
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "自定义值",
                            "变量类型": "自定义列表",
                            "变量描述": "自定义值",
                            "列表内容": "http://wwww.baidu.com,http://www.sina.com"
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "计数",
                            "变量类型": "聚合函数",
                            "变量描述": "计数",
                            "聚合函数配置": {
                                "操作内容": "行数",
                                "函数名称": "计数(count)"
                            }
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "行数替换",
                            "变量类型": "功能函数",
                            "变量描述": "行数替换",
                            "功能函数配置": {
                                "函数名称": "字符串替换",
                                "操作内容": "行数",
                                "匹配方式": "正则",
                                "匹配正则": {
                                    "标签配置": [
                                        {
                                            "标签": "数字",
                                            "正数负数": "正数",
                                            "长度": "1到多个",
                                            "是否取值": "无"
                                        }
                                    ]
                                },
                                "替换值": "行数"
                            }
                        }
                    ],
                    "规则管理": [
                        {
                            "列名": "行数",
                            "关系": "等于",
                            "匹配值": "10",
                            "条件满足时": "正常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "行数不匹配"
                        }
                    ],
                    "样例数据": "password_sample.txt"
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_ruler_add(self):
        u"""添加指令解析模版，二维表结果判断，添加变量配置"""
        action = {
            "操作": "AddRulerX",
            "参数": {
                "基本信息配置": {
                    "模版名称": "auto_二维表结果判断，添加变量配置",
                    "模版说明": "auto_二维表结果判断，添加变量配置，自动化测试，勿删"
                },
                "结果格式化配置": {
                    "分段": "否",
                    "格式化成二维表": "是"
                },
                "格式化二维表配置": {
                    "解析开始行": "1",
                    "通过正则匹配数据列": "是",
                    "正则魔方": {
                        "设置方式": "添加",
                        "正则模版名称": "auto_正则解析ping",
                        "标签配置": [
                            {
                                "标签": "任意字符",
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
                                "是否取值": "绿色"
                            },
                            {
                                "标签": "自定义文本",
                                "自定义值": "%",
                                "是否取值": "无"
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
                    },
                    "样例数据": "ping_sample.txt"
                },
                "选择判断规则": "二维表结果判断",
                "判断规则配置": {
                    "目标行": "所有行",
                    "行结果关系": "或",
                    "变量配置": [
                        {
                            "变量模式": "常用变量",
                            "变量名称": "前1天(YYYY-MM-DD)"
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "结果加1",
                            "变量类型": "列运算",
                            "变量描述": "取列1加1结果",
                            "运算规则配置": [
                                ["", "列1", "+", "1", ""]
                            ]
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "前一天",
                            "变量类型": "时间类型",
                            "变量描述": "前一天时间",
                            "时间配置": {
                                "时间格式": "自定义",
                                "自定义": "yyyyMMddHHmmss",
                                "间隔": "-1",
                                "单位": "天"
                            }
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "自定义值",
                            "变量类型": "自定义列表",
                            "变量描述": "自定义值",
                            "列表内容": "http://wwww.baidu.com,http://www.sina.com"
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "最大值",
                            "变量类型": "聚合函数",
                            "变量描述": "最大值",
                            "聚合函数配置": {
                                "操作内容": "列1",
                                "函数名称": "最大值(max)"
                            }
                        },
                        {
                            "变量模式": "高级模式",
                            "变量名称": "结果替换",
                            "变量类型": "功能函数",
                            "变量描述": "列1替换",
                            "功能函数配置": {
                                "函数名称": "字符串替换",
                                "操作内容": "列1",
                                "匹配方式": "文本",
                                "匹配值": "0",
                                "替换值": "正常"
                            }
                        }
                    ],
                    "规则管理": [
                        {
                            "列名": "列1",
                            "关系": "不等于",
                            "匹配值": "0",
                            "条件满足时": "异常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": "出现丢包情况"
                        }
                    ]
                }
            }
        }
        msg = "向导配置完成"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):  # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
