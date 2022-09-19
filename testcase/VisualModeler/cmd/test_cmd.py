# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from src.screenShot import screenShot
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class Command(unittest.TestCase):

    log.info("装载指令集配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_cmd_clear(self):
        u"""指令集数据清理，删除历史数据"""
        pres = """
        ${Database}.main|update tn_cmd_info set is_alive=0 where cmd_name like 'auto_%'
        """
        action = {
            "操作": "CmdSetDataClear",
            "参数": {
                "指令名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_cmd_add(self):
        u"""添加指令集，指令不带参数，ping指令，网元类型MME"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_ping",
                "指令类别": "不带参数指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping www.baidu.com -c 5"],
                "说明": "ping百度",
                "指令解析模版": ["auto_解析模板_解析ping"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_cmd_add(self):
        u"""添加指令集，指令不带参数，ping指令，网元类型CSCE"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_ping",
                "指令类别": "不带参数指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_CSCE"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping www.baidu.com -c 5"],
                "说明": "ping百度",
                "指令解析模版": ["auto_解析模板_解析ping"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_cmd_add(self):
        u"""添加指令集，指令不带参数，date指令"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_date",
                "指令类别": "不带参数指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["date"],
                "说明": "date获取时间",
                "指令解析模版": ["auto_解析模板_解析date"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_cmd_add(self):
        u"""添加指令集，指令单参数"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_单参数",
                "指令类别": "带参指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping <?> -c 5"],
                "说明": "ping指令带单参数",
                "指令解析模版": ["auto_解析模板_解析ping"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_cmd_add(self):
        u"""添加指令集，指令多参数"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_多参数",
                "指令类别": "带参指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping <?> -c <?>"],
                "说明": "ping指令带多参数",
                "指令解析模版": ["auto_解析模板_解析ping"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_cmd_add(self):
        u"""添加指令集，组合指令"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_组合指令",
                "指令类别": "组合指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping www.baidu.com -c 5", "date"],
                "说明": "ping百度",
                "指令解析模版": ["auto_解析模板_解析date"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_cmd_status_update(self):
        u"""启用指令集"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_cmd_delete(self):
        u"""指令已启用，无法删除"""
        action = {
            "操作": "DeleteCmdSet",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                }
            }
        }
        msg = "所选指令集信息已启用，不能够进行删除操作"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_cmd_status_update(self):
        u"""禁用指令集"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "禁用"
            }
        }
        msg = "禁用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_cmd_delete(self):
        u"""指令已禁用，允许删除"""
        action = {
            "操作": "DeleteCmdSet",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                }
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_cmd_add(self):
        u"""添加指令集，指令不带参数，ping指令，网元类型MME"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_ping",
                "指令类别": "不带参数指令",
                "指令用途": "巡检类",
                "网元分类": ["4G,4G_MME"],
                "厂家": "华为",
                "设备型号": ["ME60"],
                "登录模式": "普通模式",
                "公有指令": "是",
                "隐藏输入指令": "否",
                "个性指令": "否",
                "指令等待超时": "20",
                "指令": ["ping www.baidu.com -c 5"],
                "说明": "ping百度",
                "指令解析模版": ["auto_解析模板_解析ping", "auto_解析模板_列更新", "auto_解析模板_分段"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_cmd_status_update(self):
        u"""启用指令集：auto_指令_ping，网元类型MME"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_cmd_status_update(self):
        u"""启用指令集：auto_指令_ping，网元类型CSCE"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_ping",
                    "网元分类": ["4G,4G_CSCE"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_cmd_status_update(self):
        u"""启用指令集：auto_指令_date"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_date",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_cmd_status_update(self):
        u"""启用指令集：auto_指令_单参数"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_单参数",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_cmd_status_update(self):
        u"""启用指令集：auto_指令_多参数"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_多参数",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_cmd_status_update(self):
        u"""启用指令集：auto_指令_组合指令"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "指令信息": {
                    "指令名称": "auto_指令_组合指令",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "状态": "启用"
            }
        }
        msg = "启用成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def tearDown(self):     # 最后执行的函数
        self.browser = get_global_var("browser")
        screenShot(self.browser)
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
