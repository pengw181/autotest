# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/31 下午3:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class Ai(unittest.TestCase):

    log.info("装载AI模型配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_ai_add(self):
        u"""添加AI模型，lstm"""
        pre = """
        global|ModelName|auto_AI模型lstm
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "单指标预测",
                "算法名称": "LSTM预测模型",
                "模型名称": "auto_AI模型lstm",
                "模型描述": "auto_AI模型lstm描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "lstm.csv",
                "参数设置": ["20", "24", "50", "10", "5", "5"],
                "列设置": {
                    "时间列": "time",
                    "预测列": "online_number"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_2_ai_add(self):
        u"""添加AI模型，sarima"""
        pre = """
        global|ModelName|auto_AI模型sarima
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "单指标预测",
                "算法名称": "SARIMA预测模型",
                "模型名称": "auto_AI模型sarima",
                "模型描述": "auto_AI模型sarima描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "sarima.csv",
                "参数设置": ["2", "1", "1", "1", "2", "2"],
                "列设置": {
                    "时间列": "Time",
                    "预测列": "Data (TB)"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_ai_add(self):
        u"""添加AI模型，gru"""
        pre = """
        global|ModelName|auto_AI模型gru
        ${Database}.main|delete from tn_model_dist_detail_cfg where dist_time_id in (select dist_time_id from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}'))
        ${Database}.main|delete from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_name_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_cate_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "存在干扰因素的多指标预测",
                "算法名称": "GRU预测模型",
                "模型名称": "auto_AI模型gru",
                "模型描述": "auto_AI模型gru描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "gru.csv",
                "参数设置": ["64", "4", "1", "50", "10", "50", "2"],
                "列设置": {
                    "时间列": "Time",
                    "预测列": "Data (TB)",
                    "干扰因素列": ["标签", "小时数"]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_ai_add(self):
        u"""添加AI模型，factorLGBM"""
        pre = """
        global|ModelName|auto_AI模型factorLGBM
        ${Database}.main|delete from tn_model_dist_detail_cfg where dist_time_id in (select dist_time_id from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}'))
        ${Database}.main|delete from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_name_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_cate_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "存在干扰因素的多指标预测",
                "算法名称": "factorLGBM",
                "模型名称": "auto_AI模型factorLGBM",
                "模型描述": "auto_AI模型factorLGBM描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "factorLGBM.csv",
                "参数设置": ["5", "7", "63", "0.02", "0.01", "0.01", "1000"],
                "列设置": {
                    "时间列": "时间列",
                    "预测列": "预测列",
                    "特征列": ["特征列1", "特征列2"],
                    "干扰因素列": ["干扰因素1", "干扰因素2"]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_ai_add(self):
        u"""添加AI模型，xgboost"""
        pre = """
        global|ModelName|auto_AI模型xgboost
        ${Database}.main|delete from tn_model_dist_detail_cfg where dist_time_id in (select dist_time_id from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}'))
        ${Database}.main|delete from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_name_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_cate_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "存在干扰因素的多指标预测",
                "算法名称": "xgboost预测模型",
                "模型名称": "auto_AI模型xgboost",
                "模型描述": "auto_AI模型xgboost描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "xgboost.csv",
                "参数设置": ["20", "8", "10", "0.05", "500"],
                "列设置": {
                    "时间列": "ds",
                    "预测列": "y",
                    "干扰因素列": ["add_1", "add_2", "add_3"]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_ai_add(self):
        u"""添加AI模型，lightgbm"""
        pre = """
        global|ModelName|auto_AI模型lightgbm
        ${Database}.main|delete from tn_model_dist_detail_cfg where dist_time_id in (select dist_time_id from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}'))
        ${Database}.main|delete from tn_model_dist_time_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_name_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_dist_cate_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "通用分类算法",
                "算法名称": "lightgbm模型",
                "模型名称": "auto_AI模型lightgbm",
                "模型描述": "auto_AI模型lightgbm描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "classification.csv",
                "参数设置": ["10", "31", "1", "-1", "0.1", "255"],
                "列设置": {
                    "时间列": "",
                    "预测列": "IS_REAL_ALARM",
                    "干扰因素列": [
                        "country_id",
                        "IMPORTANCE",
                        "REQ_SUCCESS_RATE",
                        "DIVINE_REQ_SUCCESS_RATE",
                        "REQ_SUCCESS",
                        "SCALER_REQ_SUCCESS_DRIFT",
                        "REQ_SUM",
                        "SCALER_REQ_SUM_DRIFT",
                        "DIVINE_REQ_SUCCESS",
                        "DIVINE_REQ_SUM",
                        "REQ_SUCCESS_RATE_DRIFT",
                        "REQ_SUCCESS_RATE_DRIFT_FLAG",
                        "COUNT",
                        "WARN_TIME"
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_ai_add(self):
        u"""添加AI模型，梯度提升树（GBDT）"""
        pre = """
        global|ModelName|auto_AI模型梯度提升树（GBDT）
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "通用分类算法",
                "算法名称": "梯度提升树（GBDT）模型",
                "模型名称": "auto_AI模型梯度提升树（GBDT）",
                "模型描述": "auto_AI模型梯度提升树（GBDT）描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "classification.csv",
                "参数设置": ["100", "2", "1", "None", "3", "0.1", "1"],
                "列设置": {
                    "时间列": "",
                    "预测列": "IS_REAL_ALARM",
                    "干扰因素列": [
                        "country_id",
                        "IMPORTANCE",
                        "REQ_SUCCESS_RATE",
                        "DIVINE_REQ_SUCCESS_RATE",
                        "REQ_SUCCESS",
                        "SCALER_REQ_SUCCESS_DRIFT",
                        "REQ_SUM",
                        "SCALER_REQ_SUM_DRIFT",
                        "DIVINE_REQ_SUCCESS",
                        "DIVINE_REQ_SUM",
                        "REQ_SUCCESS_RATE_DRIFT",
                        "REQ_SUCCESS_RATE_DRIFT_FLAG",
                        "COUNT",
                        "WARN_TIME"
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_ai_add(self):
        u"""添加AI模型，随机森林模型"""
        pre = """
        global|ModelName|auto_AI模型随机森林
        ${Database}.main|delete from tn_model_data_cfg where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_effect where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model_param where algorithm_model_id=(select algorithm_model_id from tn_algorithm_model where model_name='${ModelName}')
        ${Database}.main|delete from tn_algorithm_model where model_name='${ModelName}'
        """
        action = {
            "操作": "AddAiModel",
            "参数": {
                "应用模式": "通用分类算法",
                "算法名称": "随机森林模型",
                "模型名称": "auto_AI模型随机森林",
                "模型描述": "auto_AI模型随机森林描述",
                "训练比例": "80",
                "测试比例": "20",
                "超时时间": "3600",
                "模型数据": "classification.csv",
                "参数设置": ["100", "2", "1", "auto"],
                "列设置": {
                    "时间列": "",
                    "预测列": "IS_REAL_ALARM",
                    "干扰因素列": [
                        "country_id",
                        "IMPORTANCE",
                        "REQ_SUCCESS_RATE",
                        "DIVINE_REQ_SUCCESS_RATE",
                        "REQ_SUCCESS",
                        "SCALER_REQ_SUCCESS_DRIFT",
                        "REQ_SUM",
                        "SCALER_REQ_SUM_DRIFT",
                        "DIVINE_REQ_SUCCESS",
                        "DIVINE_REQ_SUM",
                        "REQ_SUCCESS_RATE_DRIFT",
                        "REQ_SUCCESS_RATE_DRIFT_FLAG",
                        "COUNT",
                        "WARN_TIME"
                    ]
                }
            }
        }
        msg = "操作成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_ai_import_disturb(self):
        u"""gru模型导入干扰因素"""
        action = {
            "操作": "ImportDisturb",
            "参数": {
                "模型名称": "auto_AI模型gru",
                "文件名": "disturbModel.xlsx"
            }
        }
        msg = "导入干扰因素配置项成功"
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
