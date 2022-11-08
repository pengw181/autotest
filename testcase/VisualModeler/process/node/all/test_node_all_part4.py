# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/4 上午10:26

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class AllNodePart4(unittest.TestCase):

    log.info("装载全流程配置测试用例（4）")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_150_process_node_add(self):
        u"""画流程图，添加一个接口节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "接口节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_151_process_node_business_conf(self):
        u"""配置接口节点：soap接口"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "接口节点",
                "节点名称": "接口节点",
                "业务配置": {
                    "节点名称": "webservice接口",
                    "接口": "auto_用户密码期限检测"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_152_process_node_line(self):
        u"""开始节点连线到：参数设置"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "开始",
                "终止节点名称": "参数设置",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_153_process_node_line(self):
        u"""节点参数设置连线到：指令节点多指令"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "参数设置",
                "终止节点名称": "指令节点多指令",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_154_process_node_line(self):
        u"""节点指令节点多指令连线到：指令结果数组格式化"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "指令节点多指令",
                "终止节点名称": "指令结果数组格式化",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_155_process_node_line(self):
        u"""节点指令结果数组格式化连线到将指令结果存入文件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "指令结果数组格式化",
                "终止节点名称": "将指令结果存入文件",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_156_process_node_line(self):
        u"""节点将指令结果存入文件连线到：将文件移入临时目录"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "将指令结果存入文件",
                "终止节点名称": "将文件移入临时目录",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_157_process_node_line(self):
        u"""节点将文件移入临时目录连线到：从临时目录加载文件"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "将文件移入临时目录",
                "终止节点名称": "从临时目录加载文件",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_158_process_node_line(self):
        u"""节点从临时目录加载文件连线到：清除历史数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "从临时目录加载文件",
                "终止节点名称": "清除历史数据",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_159_process_node_line(self):
        u"""节点清除历史数据连线到：将指令结果格式化存入数据库"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "清除历史数据",
                "终止节点名称": "将指令结果格式化存入数据库",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_160_process_node_line(self):
        u"""节点将指令结果格式化存入数据库连线到：python脚本"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "将指令结果格式化存入数据库",
                "终止节点名称": "python脚本",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_161_process_node_line(self):
        u"""节点python脚本连线到：java脚本"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "python脚本",
                "终止节点名称": "java脚本",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_162_process_node_line(self):
        u"""节点java脚本连线到：jar脚本"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "java脚本",
                "终止节点名称": "jar脚本",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_163_process_node_line(self):
        u"""节点jar脚本连线到：表格取数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "jar脚本",
                "终止节点名称": "表格取数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_164_process_node_line(self):
        u"""节点表格取数连线到：文件下载"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "表格取数",
                "终止节点名称": "文件下载",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_165_process_node_line(self):
        u"""节点文件下载连线到：附件上传"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "文件下载",
                "终止节点名称": "附件上传",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_166_process_node_line(self):
        u"""节点附件上传连线到：restful接口"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "附件上传",
                "终止节点名称": "restful接口",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_167_process_node_line(self):
        u"""节点restful接口连线到：soap接口"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "restful接口",
                "终止节点名称": "soap接口",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_168_process_node_line(self):
        u"""节点soap接口连线到：多网元类型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "soap接口",
                "终止节点名称": "多网元类型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_169_process_node_line(self):
        u"""节点多网元类型连线到：指令模版带参数"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "多网元类型",
                "终止节点名称": "指令模版带参数",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_170_process_node_line(self):
        u"""节点指令模版带参数连线到：指令模版按网元类型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "指令模版带参数",
                "终止节点名称": "指令模版按网元类型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_171_process_node_line(self):
        u"""节点指令模版按网元类型连线到：数据拼盘二维表模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "指令模版按网元类型",
                "终止节点名称": "数据拼盘二维表模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_172_process_node_line(self):
        u"""节点数据拼盘二维表模式连线到：数据拼盘列更新模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "数据拼盘二维表模式",
                "终止节点名称": "数据拼盘列更新模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_173_process_node_line(self):
        u"""节点数据拼盘列更新模式连线到：数据拼盘分段模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "数据拼盘列更新模式",
                "终止节点名称": "数据拼盘分段模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_174_process_node_line(self):
        u"""节点数据拼盘分段模式连线到：数据拼盘合并模式"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "数据拼盘分段模式",
                "终止节点名称": "数据拼盘合并模式",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_175_process_node_line(self):
        u"""节点数据拼盘合并模式连线到：邮件发送"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "数据拼盘合并模式",
                "终止节点名称": "邮件发送",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_176_process_node_line(self):
        u"""节点邮件发送连线到：指令运行情况汇总"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "邮件发送",
                "终止节点名称": "指令运行情况汇总",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_177_process_node_line(self):
        u"""节点指令运行情况汇总连线到：流程相关信息展示"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "指令运行情况汇总",
                "终止节点名称": "流程相关信息展示",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_178_process_node_line(self):
        u"""节点流程相关信息展示连线到：邮件接收"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "流程相关信息展示",
                "终止节点名称": "邮件接收",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_179_process_node_line(self):
        u"""节点邮件接收连线到：加载AI预测数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "邮件接收",
                "终止节点名称": "加载AI预测数据",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_180_process_node_line(self):
        u"""节点加载AI预测数据连线到：LSTM预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "加载AI预测数据",
                "终止节点名称": "LSTM预测模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_181_process_node_line(self):
        u"""节点LSTM预测模型连线到：SARIMA预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "LSTM预测模型",
                "终止节点名称": "SARIMA预测模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_182_process_node_line(self):
        u"""节点SARIMA预测模型连线到：GRU预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "SARIMA预测模型",
                "终止节点名称": "GRU预测模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_183_process_node_line(self):
        u"""节点GRU预测模型连线到：xgboost预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "GRU预测模型",
                "终止节点名称": "xgboost预测模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_184_process_node_line(self):
        u"""节点xgboost预测模型连线到：factorLGBM模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "xgboost预测模型",
                "终止节点名称": "factorLGBM模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_185_process_node_line(self):
        u"""节点factorLGBM模型连线到：lightgbm模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "factorLGBM模型",
                "终止节点名称": "lightgbm模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_186_process_node_line(self):
        u"""节点lightgbm模型连线到：梯度提升树（GBDT）模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "lightgbm模型",
                "终止节点名称": "梯度提升树（GBDT）模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_187_process_node_line(self):
        u"""节点梯度提升树（GBDT）模型连线到：随机森林模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "梯度提升树（GBDT）模型",
                "终止节点名称": "随机森林模型",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_188_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_全流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_189_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_全流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_190_process_node_line(self):
        u"""节点随机森林模型连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_全流程",
                "起始节点名称": "随机森林模型",
                "终止节点名称": "正常",
                "关联关系": "无条件"
            }
        }
        msg = "操作成功"
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
