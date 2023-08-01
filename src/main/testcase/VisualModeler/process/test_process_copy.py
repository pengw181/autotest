# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/10/13 上午11:47

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.lib.screenShot import saveScreenShot
from src.main.python.core.gooflow.case import CaseWorker


class CopyProcess(unittest.TestCase):

    log.info("装载复制流程测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_copy_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    # def test_2_process_copy(self):
        u"""复制流程，复制主流程，主流程含子流程"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_多级流程",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_多级流程",
                "子流程名称列表": [
                    ["auto_一级子流程", "auto_copy_一级子流程"],
                    ["auto_二级子流程", "auto_copy_二级子流程"],
                    ["auto_二级子流程2", "auto_copy_二级子流程2"],
                    ["auto_三级子流程", "auto_copy_三级子流程"]
                ]
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_copy_多级流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_process_copy(self):
        u"""复制流程，复制子流程，子流程含子流程"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_一级子流程",
                "流程类型": "子流程",
                "主流程名称": "auto_copy_一级子流程",
                "子流程名称列表": [
                    ["auto_二级子流程", "auto_copy_二级子流程"],
                    ["auto_二级子流程2", "auto_copy_二级子流程2"],
                    ["auto_三级子流程", "auto_copy_三级子流程"]
                ]
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_process_delete(self):
        u"""删除流程"""
        action = {
            "操作": "DeleteProcess",
            "参数": {
                "流程名称": "auto_copy_一级子流程",
                "流程类型": "子流程"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_copy_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_6_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_指令通用功能"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_指令通用功能",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_指令通用功能"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_测试指令输入输出参数"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_测试指令输入输出参数",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_测试指令输入输出参数"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_指令按网元类型"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_指令按网元类型",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_指令按网元类型"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_指令系统检查"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_指令系统检查",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_指令系统检查"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_指令模版系统检查"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_指令模版系统检查",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_指令模版系统检查"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_指令模版通用功能"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_指令模版通用功能",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_指令模版通用功能"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_爬虫表格取数"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_爬虫表格取数",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_爬虫表格取数"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_爬虫文件下载"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_爬虫文件下载",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_爬虫文件下载"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_爬虫文件上传"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_爬虫文件上传",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_爬虫文件上传"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_数据处理"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_数据处理",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_数据处理"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_邮件接收"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_邮件接收",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_邮件接收"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_邮件发送"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_邮件发送",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_邮件发送"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_文件存储"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_文件存储",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_文件存储"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_文件拷贝移动"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_文件拷贝移动",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_文件拷贝移动"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_文件加载"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_文件加载",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_文件加载"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_21_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_信息展示"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_信息展示",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_信息展示"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_22_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_信息推送告警"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_信息推送告警",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_信息推送告警"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_23_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_webservice接口"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_webservice接口",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_webservice接口"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_24_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_soap接口"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_soap接口",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_soap接口"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_25_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_restful接口"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_restful接口",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_restful接口"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_26_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_报表链接模式"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_报表链接模式",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_报表链接模式"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_27_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_报表仪表盘模式"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_报表仪表盘模式",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_报表仪表盘模式"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_28_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_AI预测"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_AI预测",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_AI预测"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_29_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_OCR识别"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_OCR识别",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_OCR识别"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_30_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_逻辑分支"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_逻辑分支",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_逻辑分支"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_31_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_运算操作"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_运算操作",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_运算操作"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_32_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_函数计算"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_函数计算",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_函数计算"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_33_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_数据库节点SQL模式"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_数据库节点SQL模式",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_数据库节点SQL模式"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_34_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_数据库配置模式"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_数据库配置模式",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_数据库配置模式"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_35_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_数据库节点权限"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_数据库节点权限",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_数据库节点权限"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_36_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_OuShu数据库"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_OuShu数据库",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_OuShu数据库"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_37_process_copy(self):
        u"""复制流程，复制主流程：auto_流程_脚本调用"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_流程_脚本调用",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_流程_脚本调用"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_38_process_copy(self):
        u"""复制流程，复制主流程：auto_配置流程"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_配置流程",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_配置流程"
            }
        }
        msg = "复制流程成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_39_process_copy(self):
        u"""复制流程，复制主流程：auto_全流程"""
        action = {
            "操作": "CopyProcess",
            "参数": {
                "流程名称": "auto_全流程",
                "流程类型": "主流程",
                "主流程名称": "auto_copy_全流程"
            }
        }
        msg = "复制流程成功"
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
