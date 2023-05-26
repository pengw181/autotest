# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/11 下午12:58

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class CommonNodePart3(unittest.TestCase):

    log.info("装载流程通用节点配置测试用例（4）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_list(self):
        u"""流程列表，按流程名称查询"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "关键字": "auto_"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_process_list(self):
        u"""流程列表，按用户名称查询"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "关键字": "厂家运维"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_list(self):
        u"""流程列表，按节点名称查询"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "关键字": "参数设置"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_list(self):
        u"""流程列表，按流程类型查询，主流程"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "流程类型": "主流程"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_list(self):
        u"""流程列表，按流程类型查询，子流程"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "流程类型": "子流程"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_list(self):
        u"""流程列表，按流程创建时间查询，同时输入开始时间和结束时间"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "创建开始时间": {
                        "间隔": "-1",
                        "单位": "月",
                        "时间格式": "%Y-%m-%d"
                    },
                    "创建结束时间": {
                        "间隔": "0",
                        "单位": "天",
                        "时间格式": "%Y-%m-%d"
                    }
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_list(self):
        u"""流程列表，按流程创建时间查询，只输入开始时间"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "创建开始时间": {
                        "间隔": "-1",
                        "单位": "月",
                        "时间格式": "%Y-%m-%d"
                    }
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_list(self):
        u"""流程列表，按流程创建时间查询，只输入结束时间"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "创建结束时间": {
                        "间隔": "-1",
                        "单位": "天",
                        "时间格式": "%Y-%m-%d"
                    }
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_list(self):
        u"""流程列表，按流程创建时间查询，同时输入开始时间和结束时间，开始时间大于结束时间"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "创建开始时间": {
                        "间隔": "1",
                        "单位": "天",
                        "时间格式": "%Y-%m-%d"
                    },
                    "创建结束时间": {
                        "间隔": "0",
                        "单位": "天",
                        "时间格式": "%Y-%m-%d"
                    }
                }
            }
        }
        msg = "开始时间不可大于结束时间"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_list(self):
        u"""流程列表，按专业领域查询"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "专业领域": ["AiSee", "auto域"]
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_list(self):
        u"""流程列表，按启用状态查询，启用"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "启用状态": "是"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_list(self):
        u"""流程列表，按启用状态查询，未启用"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "启用状态": "否"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_list(self):
        u"""流程列表，按审批状态查询，待提交"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "待提交"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_list(self):
        u"""流程列表，按审批状态查询，审批中"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "审批中"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_list(self):
        u"""流程列表，按审批状态查询，审批通过"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "审批通过"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_list(self):
        u"""流程列表，按审批状态查询，审批不通过"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "审批不通过"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_list(self):
        u"""流程列表，按审批状态查询，已撤销"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "已撤销"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_list(self):
        u"""流程列表，按审批状态查询，超时关闭"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "审批状态": "超时关闭"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_list(self):
        u"""流程列表，按经验来源查询，云端下载"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "经验来源": "云端下载"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_list(self):
        u"""流程列表，按经验来源查询，本地创建"""
        action = {
            "操作": "ListProcess",
            "参数": {
                "查询条件": {
                    "经验来源": "本地创建"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试"
            }
        }
        msg = "调用测试流程成功,请到流程运行日志中查看"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_fast_run(self):
        u"""流程列表，一键启动流程，使用默认参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试"
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "1"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "2"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "3"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "4"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "5"
                }
            }
        }
        msg = ""
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_fast_run(self):
        u"""流程列表，一键启动流程，传参数启动"""
        action = {
            "操作": "FastRunProcess",
            "参数": {
                "流程名称": "pw流程逻辑分支测试",
                "参数列表": {
                    "a": "6"
                }
            }
        }
        msg = ""
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
