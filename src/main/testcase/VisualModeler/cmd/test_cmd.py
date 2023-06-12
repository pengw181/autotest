# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 15:47

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Command(unittest.TestCase):

    log.info("装载指令集配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_cmd_status_update(self):
        u"""启用指令集"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_cmd_status_update(self):
        u"""禁用指令集"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

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
                "指令解析模版": [
                    "auto_解析模板_解析ping",
                    "auto_解析模板_列更新",
                    "auto_解析模板_分段",
                    "auto_二维表结果判断，添加变量配置"
                ],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_cmd_status_update(self):
        u"""启用指令集：auto_指令_ping，网元类型MME"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_cmd_status_update(self):
        u"""启用指令集：auto_指令_ping，网元类型CSCE"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_cmd_status_update(self):
        u"""启用指令集：auto_指令_date"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_cmd_status_update(self):
        u"""启用指令集：auto_指令_单参数"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_cmd_status_update(self):
        u"""启用指令集：auto_指令_多参数"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_cmd_status_update(self):
        u"""启用指令集：auto_指令_组合指令"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_cmd_add(self):
        u"""添加指令集，echo指令"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_echo",
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
                "指令": ["echo 'hello, <?>'"],
                "说明": "echo信息",
                "指令解析模版": [],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_cmd_status_update(self):
        u"""启用指令集：auto_指令_echo"""
        action = {
            "操作": "UpdateCmdSetStatus",
            "参数": {
                "查询条件": {
                    "指令名称": "auto_指令_echo",
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
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_cmd_set_output_param(self):
        u"""指令集设置输出参数：auto_指令_单参数"""
        action = {
            "操作": "CmdSetOutput",
            "参数": {
                "查询条件": {
                    "指令名称": "auto_指令_单参数",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "正则参数": [{
                    "参数名称": "result_ping",
                    "参数说明": "ping解析",
                    "私有参数": "否",
                    "正则魔方": {
                        "设置方式": "选择",
                        "正则模版名称": "auto_正则模版_获取丢包率"
                    },
                    "取值": "取匹配到第一个值"
                }]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_cmd_set_input_param(self):
        u"""指令集设置输入参数：auto_指令_echo"""
        action = {
            "操作": "CmdSetInput",
            "参数": {
                "查询条件": {
                    "指令名称": "auto_指令_echo",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "参数信息": [{
                    "输出参数": "result_ping"
                }]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_cmd_set_input_param(self):
        u"""指令集设置输入参数：auto_指令_单参数"""
        action = {
            "操作": "CmdSetInput",
            "参数": {
                "查询条件": {
                    "指令名称": "auto_指令_单参数",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "参数信息": [{
                    "变量配置": [{
                        "变量模式": "业务变量",
                        "变量名称": "ssip"
                    }],
                    "变量参数": "ssip"
                }]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_cmd_add(self):
        u"""添加指令集，auto_指令_磁盘利用率检查"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_磁盘利用率检查",
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
                "指令": ["df -hl"],
                "说明": "磁盘利用率检查",
                "指令解析模版": ["auto_解析模板_服务器磁盘利用率检查"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_cmd_add(self):
        u"""添加指令集，auto_指令_查看Slab"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_查看Slab",
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
                "指令": ["cat /proc/meminfo | grep ^Slab"],
                "说明": "查看Slab",
                "指令解析模版": ["auto_解析模板_查看Slab解析"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_cmd_add(self):
        u"""添加指令集，auto_指令_内存利用率检查"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_内存利用率检查",
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
                "指令": ["free -m | grep Mem"],
                "说明": "内存利用率检查",
                "指令解析模版": ["auto_解析模板_内存利用率解析"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_cmd_add(self):
        u"""添加指令集，auto_指令_服务器性能检测Top"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_服务器性能检测Top",
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
                "指令": ["top -bn 1"],
                "说明": "top指令监测设备性能负荷",
                "指令解析模版": ["auto_解析模板_cpu利用率检查"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_cmd_add(self):
        u"""添加指令集，auto_指令_服务器负载检查"""
        action = {
            "操作": "AddCmdSet",
            "参数": {
                "指令名称": "auto_指令_服务器负载检查",
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
                "指令": ["cat /proc/loadavg"],
                "说明": [
                    "前三个值分别代表系统5分钟、10分钟、15分钟前的平均负载",
                    "第四个值的分子是正在运行的进程数，分母为总进程数",
                    "第五个值是最近运行的进程id"]
                ,
                "指令解析模版": ["auto_解析模板_服务器负载检查"],
                "指令翻页符": "",
                "期待返回的结束符": "",
                "隐藏指令返回": ""
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def tearDown(self):     # 最后执行的函数
        self.browser = gbl.service.get("browser")
        saveScreenShot()
        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()
