# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 下午2:36

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class SqlNode(unittest.TestCase):

    log.info("装载流程数据库节点SQL模式测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_48_process_node_fetch_conf(self):
        u"""节点添加取数配置，不含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_不含列名",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_49_process_node_fetch_conf(self):
        u"""节点添加取数配置，含列名"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_含列名",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "是"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_50_process_node_fetch_conf(self):
        u"""节点添加取数配置，取部分列"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "查询内部库",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "查询结果_取部分列",
                    "赋值方式": "替换",
                    "输出列": "1,2,3",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_51_process_node_fetch_conf(self):
        u"""节点添加取数配置，mysql数据库，mysql外部库select数据"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "mysql外部库select数据",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "mysql外部库select查询结果",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_52_process_node_fetch_conf(self):
        u"""节点添加取数配置，mysql数据库，oracle外部库select数据"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "oracle外部库select数据",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "oracle外部库select查询结果",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_53_process_node_fetch_conf(self):
        u"""节点添加取数配置，mysql数据库，postgres外部库select数据"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "数据库节点",
                "节点名称": "postgres外部库select数据",
                "取数配置": {
                    "操作": "添加",
                    "变量名": "postgres外部库select查询结果",
                    "赋值方式": "替换",
                    "输出列": "*",
                    "获取列名": "否"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_54_process_node_line(self):
        u"""开始节点连线到节点：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
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

    def test_55_process_node_line(self):
        u"""节点参数设置连线到节点：加载入库数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "参数设置",
                "终止节点名称": "加载入库数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_56_process_node_line(self):
        u"""节点加载入库数据连线到节点：删除历史数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "加载入库数据",
                "终止节点名称": "删除历史数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_57_process_node_line(self):
        u"""节点删除历史数据连线到节点：查询内部库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "删除历史数据",
                "终止节点名称": "查询内部库",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_58_process_node_line(self):
        u"""节点查询内部库连线到节点：insert网元其它资料表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "查询内部库",
                "终止节点名称": "对表数据进行insert",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_59_process_node_line(self):
        u"""节点对表数据进行insert连线到节点：对表数据进行update"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "对表数据进行insert",
                "终止节点名称": "对表数据进行update",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_60_process_node_line(self):
        u"""节点对表数据进行update连线到节点：对表数据进行delete"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "对表数据进行update",
                "终止节点名称": "对表数据进行delete",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_61_process_node_line(self):
        u"""节点对表数据进行delete连线到节点：mysql外部库drop表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "对表数据进行delete",
                "终止节点名称": "mysql外部库drop表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_62_process_node_line(self):
        u"""节点mysql外部库drop表连线到节点：mysql外部库create表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "mysql外部库drop表",
                "终止节点名称": "mysql外部库create表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_63_process_node_line(self):
        u"""节点mysql外部库create表连线到节点：mysql外部库insert数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "mysql外部库create表",
                "终止节点名称": "mysql外部库insert数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_64_process_node_line(self):
        u"""节点mysql外部库insert数据连线到节点：mysql外部库select数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "mysql外部库insert数据",
                "终止节点名称": "mysql外部库select数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_65_process_node_line(self):
        u"""节点mysql外部库select数据连线到节点：oracle外部库drop表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "mysql外部库select数据",
                "终止节点名称": "oracle外部库drop表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_66_process_node_line(self):
        u"""节点oracle外部库drop表连线到节点：oracle外部库create表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "oracle外部库drop表",
                "终止节点名称": "oracle外部库create表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_67_process_node_line(self):
        u"""节点oracle外部库create表连线到节点：oracle外部库insert数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "oracle外部库create表",
                "终止节点名称": "oracle外部库insert数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_68_process_node_line(self):
        u"""节点oracle外部库insert数据连线到节点：oracle外部库select数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "oracle外部库insert数据",
                "终止节点名称": "oracle外部库select数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_69_process_node_line(self):
        u"""节点oracle外部库select数据连线到节点：postgres外部库drop表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "oracle外部库select数据",
                "终止节点名称": "postgres外部库drop表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_70_process_node_line(self):
        u"""节点postgres外部库drop表连线到节点：postgres外部库create表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "postgres外部库drop表",
                "终止节点名称": "postgres外部库create表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_71_process_node_line(self):
        u"""节点postgres外部库create表连线到节点：postgres外部库insert数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "postgres外部库create表",
                "终止节点名称": "postgres外部库insert数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_72_process_node_line(self):
        u"""节点postgres外部库insert数据连线到节点：postgres外部库select数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "postgres外部库insert数据",
                "终止节点名称": "postgres外部库select数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_73_process_node_line(self):
        u"""节点postgres外部库select数据连线到节点：删除备用表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "postgres外部库select数据",
                "终止节点名称": "删除备用表",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_74_process_node_line(self):
        u"""节点删除备用表连线到节点：使用create as select创建表"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "删除备用表",
                "终止节点名称": "使用create as select创建表",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_75_process_node_line(self):
        u"""节点使用create as select创建表连线到节点：使用insert into select插入数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "使用create as select创建表",
                "终止节点名称": "使用insert into select插入数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_76_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_77_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_78_process_node_line(self):
        u"""节点使用insert into select插入数据连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "起始节点名称": "使用insert into select插入数据",
                "终止节点名称": "正常",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_79_process_test(self):
        u"""流程列表，测试流程"""
        action = {
            "操作": "TestProcess",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式"
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
