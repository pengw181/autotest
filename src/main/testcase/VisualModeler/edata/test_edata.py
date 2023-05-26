# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/3 上午11:10

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Edata(unittest.TestCase):

    log.info("装载数据拼盘配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_edata_clear(self):
        u"""数据拼盘，数据清理"""
        action = {
            "操作": "EDataDataClear",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_edata_add(self):
        u"""数据拼盘，添加二维表模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_二维表模式，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_edata_add(self):
        u"""数据拼盘，添加二维表模式，名称已存在"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_二维表模式，勿删"
            }
        }
        msg = "表名已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_edata_delete(self):
        u"""数据拼盘，删除二维表模式"""
        action = {
            "操作": "DeleteEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_edata_add(self):
        u"""数据拼盘，添加二维表模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_二维表模式，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_edata_col_set(self):
        u"""数据拼盘，二维表模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列2",
                        "列类型": "字符",
                        "字符长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列3",
                        "列类型": "字符",
                        "字符长度": "200"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_edata_update_rule_config(self):
        u"""数据拼盘，二维表模式配置更新规则"""
        action = {
            "操作": "EDataConfigUpdateRule",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "取参指令": {
                    "关键字": "auto_指令_date",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "指令解析模版": "auto_解析模板_解析date",
                "二维表结果绑定": ["列1", "列2", "列3"]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_edata_add(self):
        u"""数据拼盘，添加二维表模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式2",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_二维表模式2，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_edata_col_set(self):
        u"""数据拼盘，二维表模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式2",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列2",
                        "列类型": "字符",
                        "字符长度": "200"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列3",
                        "列类型": "字符",
                        "字符长度": "200"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_edata_update_rule_config(self):
        u"""数据拼盘，二维表模式配置更新规则"""
        action = {
            "操作": "EDataConfigUpdateRule",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式2",
                "取参指令": {
                    "关键字": "auto_指令_date",
                    "网元分类": ["4G,4G_MME"],
                    "厂家": "华为",
                    "设备型号": "ME60"
                },
                "指令解析模版": "auto_解析模板_解析date",
                "二维表结果绑定": ["列1", "列2", "列3"]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_edata_clear(self):
        u"""数据拼盘，数据清理"""
        action = {
            "操作": "EDataDataClear",
            "参数": {
                "模版类型": "列更新模式",
                "数据表名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_12_edata_add(self):
        u"""数据拼盘，添加列更新模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "列更新模式",
                "数据表名称": "auto_数据拼盘_列更新模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_列更新模式，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_edata_col_set(self):
        u"""数据拼盘，列更新模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "列更新模式",
                "数据表名称": "auto_数据拼盘_列更新模式",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "200",
                        "取参指令": {
                            "关键字": "auto_指令_ping"
                        },
                        "指令解析模版": "auto_解析模板_列更新"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_edata_clear(self):
        u"""数据拼盘，数据清理"""
        action = {
            "操作": "EDataDataClear",
            "参数": {
                "模版类型": "分段模式",
                "数据表名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_15_edata_add(self):
        u"""数据拼盘，添加分段模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "分段模式",
                "数据表名称": "auto_数据拼盘_分段模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_分段模式，勿删",
                "取参指令": {
                    "关键字": "auto_指令_ping"
                },
                "段开始特征行": {
                    "设置方式": "选择",
                    "正则模版名称": "auto_正则模版_time特征行"
                },
                "样例数据": "ping_sample.txt"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_edata_col_set(self):
        u"""数据拼盘，分段模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "分段模式",
                "数据表名称": "auto_数据拼盘_分段模式",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "200",
                        "指令解析模版": "auto_解析模板_分段"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_edata_clear(self):
        u"""数据拼盘，数据清理"""
        action = {
            "操作": "EDataDataClear",
            "参数": {
                "模版类型": "数据模式",
                "数据表名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_18_edata_add(self):
        u"""数据拼盘，添加数据模式"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "数据模式",
                "数据表名称": "auto_数据拼盘_数据模式",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据拼盘_数据模式，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_edata_col_set(self):
        u"""数据拼盘，数据模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "数据模式",
                "数据表名称": "auto_数据拼盘_数据模式",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列2",
                        "列类型": "字符",
                        "字符长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列3",
                        "列类型": "字符",
                        "字符长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列4",
                        "列类型": "字符",
                        "字符长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列5",
                        "列类型": "字符",
                        "字符长度": "100"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_edata_add(self):
        u"""数据拼盘，添加数据模式，多数据类型列"""
        action = {
            "操作": "AddEDataTpl",
            "参数": {
                "模版类型": "数据模式",
                "数据表名称": "auto_数据模式_多数据类型",
                "专业领域": ["AiSee", "auto域"],
                "备注": "auto_数据模式_多数据类型，勿删"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_edata_col_set(self):
        u"""数据拼盘，数据模式添加列配置"""
        action = {
            "操作": "EDataSetCol",
            "参数": {
                "模版类型": "数据模式",
                "数据表名称": "auto_数据模式_多数据类型",
                "列配置": [
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列1",
                        "列类型": "字符",
                        "字符长度": "100"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列2",
                        "列类型": "数值",
                        "小位数": "0"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列3",
                        "列类型": "数值",
                        "小位数": "2"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列4",
                        "列类型": "文本"
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列5",
                        "列类型": "日期",
                        "输入格式": ["yyyy-MM-dd HH:mm:ss", ""],
                        "输出格式": ["yyyyMMddHHmmss", ""]
                    },
                    {
                        "操作类型": "添加",
                        "列名(自定义)": "列6",
                        "列类型": "日期",
                        "输入格式": ["自定义", "yyyy-MM-dd"],
                        "输出格式": ["yyyyMMddHHmmss", ""]
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_edata_clear(self):
        u"""数据拼盘，数据清理"""
        action = {
            "操作": "EDataDataClear",
            "参数": {
                "模版类型": "合并模式",
                "数据表名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_23_edata_add(self):
        u"""数据拼盘，添加合并模式，join"""
        action = {
            "操作": "AddJoinEDataTpl",
            "参数": {
                "模版类型": "合并模式",
                "合并表名称": ["auto_数据拼盘_二维表模式", "auto_数据拼盘_二维表模式2"],
                "关联方式": "左关联",
                "左表配置": [
                    {
                        "列名": "网元名称",
                        "合并后显示": "是",
                        "关联列": "1"
                    },
                    {
                        "列名": "指令内容",
                        "合并后显示": "是"
                    },
                    {
                        "列名": "列1",
                        "合并后显示": "否"
                    },
                    {
                        "列名": "列2",
                        "合并后显示": "是"
                    },
                    {
                        "列名": "列3",
                        "合并后显示": "是"
                    }
                ],
                "右表配置": [
                    {
                        "列名": "网元名称",
                        "合并后显示": "否",
                        "关联列": "1"
                    },
                    {
                        "列名": "列1",
                        "合并后显示": "是"
                    }
                ],
                "数据表名称": "auto_数据拼盘_合并模式join",
                "专业领域": ["AiSee", "auto域"],
                "新表配置": [
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "原列名": "网元名称",
                        "新列名": "netunit",
                        "搜索条件": "是"
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "原列名": "指令内容",
                        "新列名": "command",
                        "搜索条件": "是"
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "原列名": "列2",
                        "新列名": "col_2",
                        "搜索条件": "是"
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "原列名": "列3",
                        "新列名": "col_3",
                        "搜索条件": "是"
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式2",
                        "原列名": "列1",
                        "新列名": "col_1",
                        "搜索条件": "是"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_edata_add(self):
        u"""数据拼盘，添加合并模式，union"""
        action = {
            "操作": "AddUnionEDataTpl",
            "参数": {
                "模版类型": "合并模式",
                "合并表名称": ["auto_数据拼盘_二维表模式", "auto_数据拼盘_二维表模式2"],
                "关联方式": "UNION",
                "合并表配置": [
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式2",
                        "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                    }
                ],
                "数据表名称": "auto_数据拼盘_合并模式union",
                "专业领域": ["AiSee", "auto域"],
                "新表配置": [
                    {
                        "原列名": "网元名称",
                        "新列名": "netunit",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "指令内容",
                        "新列名": "command",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列1",
                        "新列名": "col_1",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列2",
                        "新列名": "col_2",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列3",
                        "新列名": "col_3",
                        "搜索条件": "是"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_edata_add(self):
        u"""数据拼盘，添加合并模式，union all"""
        action = {
            "操作": "AddUnionEDataTpl",
            "参数": {
                "模版类型": "合并模式",
                "合并表名称": ["auto_数据拼盘_二维表模式", "auto_数据拼盘_二维表模式2"],
                "关联方式": "UNION ALL",
                "合并表配置": [
                    {
                        "表名": "auto_数据拼盘_二维表模式",
                        "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                    },
                    {
                        "表名": "auto_数据拼盘_二维表模式2",
                        "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                    }
                ],
                "数据表名称": "auto_数据拼盘_合并模式unionall",
                "专业领域": ["AiSee", "auto域"],
                "新表配置": [
                    {
                        "原列名": "网元名称",
                        "新列名": "netunit",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "指令内容",
                        "新列名": "command",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列1",
                        "新列名": "col_1",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列2",
                        "新列名": "col_2",
                        "搜索条件": "是"
                    },
                    {
                        "原列名": "列3",
                        "新列名": "col_3",
                        "搜索条件": "是"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_edata_status_update(self):
        u"""数据拼盘，启用二维表模式，未绑定网元"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "状态": "启用"
            }
        }
        msg = "该模版未绑定网元，不能启动"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_edata_netunit_bind(self):
        u"""数据拼盘，二维表模式绑定网元"""
        action = {
            "操作": "EDataBindNE",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "网元列表": [
                    {
                        "网元名称": "${NetunitMME1}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME2}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME3}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_edata_netunit_bind(self):
        u"""数据拼盘，列更新模式绑定网元"""
        action = {
            "操作": "EDataBindNE",
            "参数": {
                "模版类型": "列更新模式",
                "数据表名称": "auto_数据拼盘_列更新模式",
                "网元列表": [
                    {
                        "网元名称": "${NetunitMME1}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME2}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME3}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_edata_netunit_bind(self):
        u"""数据拼盘，分段模式绑定网元"""
        action = {
            "操作": "EDataBindNE",
            "参数": {
                "模版类型": "分段模式",
                "数据表名称": "auto_数据拼盘_分段模式",
                "网元列表": [
                    {
                        "网元名称": "${NetunitMME1}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME2}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME3}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_edata_netunit_bind(self):
        u"""数据拼盘，二维表模式绑定网元"""
        action = {
            "操作": "EDataBindNE",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式2",
                "网元列表": [
                    {
                        "网元名称": "${NetunitMME1}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME2}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME3}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    }
                ]
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_edata_status_update(self):
        u"""数据拼盘，启用二维表模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_edata_update(self):
        u"""数据拼盘，二维表模式已启用，修改数据拼盘"""
        action = {
            "操作": "UpdateEDataTpl",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "修改内容": {
                    "数据表名称": "auto_数据拼盘_二维表模式",
                    "专业领域": ["AiSee", "auto域"],
                    "备注": "auto_数据拼盘_二维表模式，勿删"
                }
            }
        }
        msg = "请先禁用该模版后再修改"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_edata_netunit_bind(self):
        u"""数据拼盘，二维表模式已启用，绑定网元"""
        action = {
            "操作": "EDataBindNE",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "网元列表": [
                    {
                        "网元名称": "${NetunitMME1}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME2}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    },
                    {
                        "网元名称": "${NetunitMME3}",
                        "网元分类": ["4G,4G_MME"],
                        "厂家": "华为",
                        "设备型号": "ME60"
                    }
                ]
            }
        }
        msg = "请先禁用该模版后再修改"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_edata_status_update(self):
        u"""数据拼盘，禁用二维表模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "状态": "禁用"
            }
        }
        msg = "禁用成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_edata_status_update(self):
        u"""数据拼盘，启用二维表模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_edata_status_update(self):
        u"""数据拼盘，启用二维表模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "二维表模式",
                "数据表名称": "auto_数据拼盘_二维表模式2",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_edata_status_update(self):
        u"""数据拼盘，启用列更新模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "列更新模式",
                "数据表名称": "auto_数据拼盘_列更新模式",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_edata_status_update(self):
        u"""数据拼盘，启用分段模式"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "分段模式",
                "数据表名称": "auto_数据拼盘_分段模式",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_edata_status_update(self):
        u"""数据拼盘，启用合并模式，join"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "合并模式",
                "数据表名称": "auto_数据拼盘_合并模式join",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_40_edata_status_update(self):
        u"""数据拼盘，启用合并模式，union"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "合并模式",
                "数据表名称": "auto_数据拼盘_合并模式union",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_41_edata_status_update(self):
        u"""数据拼盘，启用合并模式，union all"""
        action = {
            "操作": "EDataUpdateStatus",
            "参数": {
                "模版类型": "合并模式",
                "数据表名称": "auto_数据拼盘_合并模式unionall",
                "状态": "启用"
            }
        }
        msg = "启用模版成功"
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
