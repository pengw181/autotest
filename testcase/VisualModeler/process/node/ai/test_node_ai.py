# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/9/5 下午8:28

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class AiNode(unittest.TestCase):

    log.info("装载流程AI节点配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_process_clear(self):
        u"""流程数据清理，删除历史数据"""
        action = {
            "操作": "ProcessDataClear",
            "参数": {
                "流程名称": "auto_AI节点流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_process_add(self):
        u"""添加流程，测试AI节点"""
        action = {
            "操作": "AddProcess",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "专业领域": ["AiSee", "auto域"],
                "流程类型": "主流程",
                "流程说明": "auto_AI节点流程说明",
                "高级配置": {
                    "自定义流程变量": {
                        "状态": "开启",
                        "参数列表": {
                            "时间": "2020-10-20###必填",
                            "地点": "广州###",
                            "名字": "pw###必填"
                        }
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_process_node_add(self):
        u"""画流程图，添加一个文件节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：单指标接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点",
                "节点名称": "文件节点",
                "业务配置": {
                    "节点名称": "加载AI预测数据",
                    "操作模式": "文件加载",
                    "存储参数配置": {
                        "存储类型": "本地",
                        "目录": "auto_AI"
                    },
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "single_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "1",
                            "开始读取行": "2",
                            "变量": "单指标接入数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：通用算法接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "classical_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "3",
                            "变量": "通用算法接入数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：干扰因素接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factor_predict",
                            "文件类型": "xlsx",
                            "编码格式": "UTF-8",
                            "sheet页索引": "",
                            "开始读取行": "",
                            "变量": "干扰因素接入数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：factorXGB接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factorXGB_predict",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "2",
                            "分隔符": ",",
                            "变量": "factorXGB接入数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_process_node_business_conf(self):
        u"""配置文件节点：加载AI预测数据，输出变量：factorLGBM接入数据"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "文件节点",
                "节点名称": "加载AI预测数据",
                "业务配置": {
                    "文件配置": [
                        {
                            "类型": "关键字",
                            "文件名": "factorLGBM_predict",
                            "文件类型": "csv",
                            "编码格式": "UTF-8",
                            "开始读取行": "",
                            "分隔符": ",",
                            "变量": "factorLGBM接入数据",
                            "变量类型": "替换"
                        }
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_process_node_business_conf(self):
        u"""配置AI节点，单指标预测，lstm模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "LSTM预测模型",
                    "节点模式": "单指标预测",
                    "算法选择": "LSTM预测模型",
                    "模型": "auto_AI模型lstm",
                    "输入变量": "单指标接入数据",
                    "预测步长": "10",
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_process_node_business_conf(self):
        u"""配置AI节点，单指标预测，sarima模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "SARIMA预测模型",
                    "节点模式": "单指标预测",
                    "算法选择": "SARIMA预测模型",
                    "模型": "auto_AI模型sarima",
                    "输入变量": "单指标接入数据",
                    "预测步长": "10"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_process_node_business_conf(self):
        u"""配置AI节点，存在干扰因素的多指标预测，gru模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "GRU预测模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "GRU预测模型",
                    "模型": "auto_AI模型gru",
                    "输入变量": "干扰因素接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_process_node_business_conf(self):
        u"""配置AI节点，存在干扰因素的多指标预测，xgboost模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "xgboost预测模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "xgboost预测模型",
                    "模型": "auto_AI模型xgboost",
                    "输入变量": "factorXGB接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_process_node_business_conf(self):
        u"""配置AI节点，存在干扰因素的多指标预测，factorLGBM模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "factorLGBM模型",
                    "节点模式": "存在干扰因素的多指标预测",
                    "算法选择": "factorLGBM",
                    "模型": "auto_AI模型factorLGBM",
                    "输入变量": "factorLGBM接入数据",
                    "预测步长": "5"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_process_node_business_conf(self):
        u"""配置AI节点，通用分类算法，lightgbm模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "lightgbm模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "lightgbm模型",
                    "模型": "auto_AI模型lightgbm",
                    "输入变量": "通用算法接入数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_process_node_business_conf(self):
        u"""配置AI节点，通用分类算法，梯度提升树（GBDT）模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "梯度提升树（GBDT）模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "梯度提升树（GBDT）模型",
                    "模型": "auto_AI模型梯度提升树（GBDT）",
                    "输入变量": "通用算法接入数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_process_node_add(self):
        u"""画流程图，添加一个AI节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_process_node_business_conf(self):
        u"""配置AI节点，通用分类算法，随机森林模型"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "AI节点",
                "业务配置": {
                    "节点名称": "随机森林模型",
                    "节点模式": "通用分类算法",
                    "算法选择": "随机森林模型",
                    "模型": "auto_AI模型随机森林",
                    "输入变量": "通用算法接入数据"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_process_node_business_conf(self):
        u"""配置AI节点：LSTM预测模型，设置对应关系"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "业务配置": {
                    "对应关系配置": {
                        "状态": "开启",
                        "1": "time(时间列)",
                        "2": "online_number(预测列)"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_process_node_business_conf(self):
        u"""配置AI节点：LSTM预测模型，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "业务配置": {
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_process_node_business_conf(self):
        u"""配置AI节点：LSTM预测模型，关闭高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "业务配置": {
                    "高级配置": {
                        "状态": "关闭"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_process_node_business_conf(self):
        u"""配置AI节点：LSTM预测模型，开启高级配置"""
        action = {
            "操作": "NodeBusinessConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "业务配置": {
                    "高级配置": {
                        "状态": "开启",
                        "超时时间": "600",
                        "超时重试次数": "2"
                    }
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_process_node_fetch_conf(self):
        u"""节点添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "ai预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_process_node_fetch_conf(self):
        u"""节点修改取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "取数配置": {
                    "操作": "修改",
                    "目标变量": "ai预测结果",
                    "变量名称": "ai预测结果1",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_process_node_fetch_conf(self):
        u"""节点删除取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "取数配置": {
                    "操作": "删除",
                    "目标变量": "ai预测结果1"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_process_node_fetch_conf(self):
        u"""节点LSTM预测模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "LSTM预测模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "LSTM预测模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_process_node_fetch_conf(self):
        u"""节点SARIMA预测模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "SARIMA预测模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "SARIMA预测模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_process_node_fetch_conf(self):
        u"""节点GRU预测模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "GRU预测模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "GRU预测模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_process_node_fetch_conf(self):
        u"""节点xgboost预测模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "xgboost预测模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "xgboost预测模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_process_node_fetch_conf(self):
        u"""节点factorLGBM模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "factorLGBM模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "factorLGBM模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_process_node_fetch_conf(self):
        u"""节点lightgbm模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "lightgbm模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "lightgbm模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_process_node_fetch_conf(self):
        u"""节点梯度提升树（GBDT）模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "梯度提升树（GBDT）模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "梯度提升树（GBDT）模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_process_node_fetch_conf(self):
        u"""节点随机森林模型添加取数配置"""
        action = {
            "操作": "NodeFetchConf",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "AI节点",
                "节点名称": "随机森林模型",
                "取数配置": {
                    "操作": "添加",
                    "变量名称": "随机森林模型预测结果",
                    "赋值方式": "替换"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_process_node_line(self):
        u"""开始节点连线到节点：加载AI预测数据"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "起始节点名称": "开始",
                "终止节点名称": "加载AI预测数据",
                "关联关系": "满足"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_process_node_line(self):
        u"""节点加载AI预测数据连线到节点：LSTM预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_42_process_node_line(self):
        u"""节点LSTM预测模型连线到节点：SARIMA预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_43_process_node_line(self):
        u"""节点SARIMA预测模型连线到节点：GRU预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_44_process_node_line(self):
        u"""节点GRU预测模型连线到节点：xgboost预测模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_45_process_node_line(self):
        u"""节点xgboost预测模型连线到节点：factorLGBM模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_46_process_node_line(self):
        u"""节点factorLGBM模型连线到节点：lightgbm模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_47_process_node_line(self):
        u"""节点lightgbm模型连线到节点：梯度提升树（GBDT）模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_48_process_node_line(self):
        u"""节点梯度提升树（GBDT）模型连线到节点：随机森林模型"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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

    def test_49_process_node_add(self):
        u"""画流程图，添加一个结束节点"""
        action = {
            "操作": "AddNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "节点类型": "结束节点"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_process_node_end_conf(self):
        u"""设置结束节点状态为正常"""
        action = {
            "操作": "SetEndNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
                "状态": "正常"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_51_process_node_line(self):
        u"""节点随机森林模型连线到结束节点"""
        action = {
            "操作": "LineNode",
            "参数": {
                "流程名称": "auto_AI节点流程",
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
