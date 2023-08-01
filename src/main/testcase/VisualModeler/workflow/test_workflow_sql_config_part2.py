# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class WorkFlowSqlNodeConfigMode2(unittest.TestCase):

    log.info("装载流程数据库节点配置模式测试用例（2）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_46_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，全部成功，取总条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库_总条数",
                    "输出内容": "总条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_47_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，全部成功，取正常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库_正常条数",
                    "输出内容": "正常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_48_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，全部成功，取异常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库_异常条数",
                    "输出内容": "异常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，pg数据库，部分成功，取总条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库部分成功_总条数",
                    "输出内容": "总条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，pg数据库，部分成功，取正常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库部分成功_正常条数",
                    "输出内容": "正常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，pg数据库，部分成功，取异常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部pg数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部pg数据库部分成功_异常条数",
                    "输出内容": "异常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取总条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部oracle数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部oracle数据库部分成功_总条数",
                    "输出内容": "总条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取正常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部oracle数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部oracle数据库部分成功_正常条数",
                    "输出内容": "正常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，oracle数据库，部分成功，取异常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部oracle数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部oracle数据库部分成功_异常条数",
                    "输出内容": "异常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_55_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取总条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库部分成功_总条数",
                    "输出内容": "总条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取正常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库部分成功_正常条数",
                    "输出内容": "正常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_57_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，mysql数据库，部分成功，取异常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库部分成功",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库部分成功_异常条数",
                    "输出内容": "异常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，跳过行数不为空，取总条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库跳过部分行",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库跳过部分行_总条数",
                    "输出内容": "总条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，跳过行数不为空，取正常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库跳过部分行",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库跳过部分行_正常条数",
                    "输出内容": "正常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_process_node_fetch_conf(self):
        u"""节点添加取数配置，配置模式，跳过行数不为空，取异常条数"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "数据库节点",
                "节点名称": "导入外部mysql数据库跳过部分行",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "导入外部mysql数据库跳过部分行_异常条数",
                    "输出内容": "异常条数"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_line(self):
        u"""节点参数设置连线到节点：删除历史数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "参数设置",
                "终止节点名称": "删除历史数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_process_node_line(self):
        u"""节点删除历史数据连线到节点：加载入库数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "删除历史数据",
                "终止节点名称": "加载入库数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_line(self):
        u"""节点加载入库数据连线到节点：数据插入网元其它资料"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "加载入库数据",
                "终止节点名称": "数据插入网元其它资料",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_65_process_node_line(self):
        u"""节点数据插入网元其它资料连线到节点：查询内部库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "数据插入网元其它资料",
                "终止节点名称": "查询内部库",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_node_line(self):
        u"""节点查询内部库连线到节点：数据插入数据拼盘"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "查询内部库",
                "终止节点名称": "数据插入数据拼盘",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_67_process_node_line(self):
        u"""节点数据插入数据拼盘连线到节点：加载大数据入库数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "数据插入数据拼盘",
                "终止节点名称": "加载大数据入库数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_68_process_node_line(self):
        u"""节点加载大数据入库数据连线到节点：postgres外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "加载大数据入库数据",
                "终止节点名称": "postgres外部表数据清理",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_69_process_node_line(self):
        u"""节点postgres外部表数据清理连线到节点：oracle外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "postgres外部表数据清理",
                "终止节点名称": "oracle外部表数据清理",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_70_process_node_line(self):
        u"""节点oracle外部表数据清理连线到节点：mysql外部表数据清理"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "oracle外部表数据清理",
                "终止节点名称": "mysql外部表数据清理",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_71_process_node_line(self):
        u"""节点mysql外部表数据清理连线到节点：导入外部pg数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "mysql外部表数据清理",
                "终止节点名称": "导入外部pg数据库",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_72_process_node_line(self):
        u"""节点导入外部pg数据库连线到节点：导入外部oracle数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部pg数据库",
                "终止节点名称": "导入外部oracle数据库",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_73_process_node_line(self):
        u"""节点导入外部oracle数据库连线到节点：导入外部mysql数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部oracle数据库",
                "终止节点名称": "导入外部mysql数据库",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_74_process_node_line(self):
        u"""节点导入外部mysql数据库连线到节点：批量提交行数为空存在异常"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部mysql数据库",
                "终止节点名称": "批量提交行数为空存在异常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_75_process_node_line(self):
        u"""节点批量提交行数为空存在异常连线到节点：批量提交行数不为空且全部成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "批量提交行数为空存在异常",
                "终止节点名称": "批量提交行数不为空且全部成功",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_76_process_node_line(self):
        u"""节点批量提交行数不为空且全部成功连线到节点：导入外部pg数据库部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "批量提交行数不为空且全部成功",
                "终止节点名称": "导入外部pg数据库部分成功",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_77_process_node_line(self):
        u"""节点导入外部pg数据库部分成功连线到节点：导入外部oracle数据库部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部pg数据库部分成功",
                "终止节点名称": "导入外部oracle数据库部分成功",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_78_process_node_line(self):
        u"""节点导入外部oracle数据库部分成功连线到节点：导入外部mysql数据库部分成功"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部oracle数据库部分成功",
                "终止节点名称": "导入外部mysql数据库部分成功",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_79_process_node_line(self):
        u"""节点导入外部mysql数据库部分成功连线到节点：导入外部mysql数据库跳过部分行"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部mysql数据库部分成功",
                "终止节点名称": "导入外部mysql数据库跳过部分行",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_80_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_81_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_82_process_node_line(self):
        u"""节点导入外部mysql数据库跳过部分行连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "起始节点名称": "导入外部mysql数据库跳过部分行",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_83_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式"
            }
        }
        msg = "调用测试流程成功,请到流程运行日志中查看"
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
