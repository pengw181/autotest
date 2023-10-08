# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 23/09/19 AM10:10

import unittest
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.core.gooflow.result import Result
from src.main.python.lib.screenShot import saveScreenShot


class AI(unittest.TestCase):

	log.info("装载AI模型管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	@unittest.skip
	def test_1_AiModelDataClear(self):
		u"""UNTEST,AI模型管理,数据清理"""
		pres = """
		${Database}.main|delete * from tn_algorithm_model where model_name like 'auto_%'
		"""
		action = {
			"操作": "AiModelDataClear",
			"参数": {
				"模型名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> UNTEST,AI模型管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddAiModel(self):
		u"""添加AI模型，lstm"""
		pres = """
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
				"参数设置": [
					"20",
					"24",
					"50",
					"10",
					"5",
					"5"
				],
				"列设置": {
					"时间列": "time",
					"预测列": "online_number"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型lstm|model_desc|auto_AI模型lstm描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|lstm.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_1|param_val|20
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_2|param_val|24
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_3|param_val|50
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_4|param_val|10
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_5|param_val|5
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|LSTM|algorithm_model_id|${AlgorithmModelID}|param_id|lstm_param_6|param_val|5
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|lstm_col_1|cfg_col_value|0|cfg_col_name|time
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|lstm_col_2|cfg_col_value|1|cfg_col_name|online_number
		"""
		log.info('>>>>> 添加AI模型，lstm <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddAiModel(self):
		u"""添加AI模型，sarima"""
		pres = """
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
				"参数设置": [
					"2",
					"1",
					"1",
					"1",
					"2",
					"2"
				],
				"列设置": {
					"时间列": "Time",
					"预测列": "Data (TB)"
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型sarima|model_desc|auto_AI模型sarima描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|sarima.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_1|param_val|2
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_2|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_3|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_4|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_5|param_val|2
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|SARIMA|algorithm_model_id|${AlgorithmModelID}|param_id|sarima_param_6|param_val|2
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|sarima_col_1|cfg_col_value|0|cfg_col_name|Time
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|sarima_col_2|cfg_col_value|1|cfg_col_name|Data (TB)
		"""
		log.info('>>>>> 添加AI模型，sarima <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddAiModel(self):
		u"""添加AI模型，gru"""
		pres = """
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
				"参数设置": [
					"64",
					"4",
					"1",
					"50",
					"10",
					"50",
					"2"
				],
				"列设置": {
					"时间列": "Time",
					"预测列": "Data (TB)",
					"干扰因素列": [
						"标签",
						"小时数"
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型gru|model_desc|auto_AI模型gru描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|gru.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_1|param_val|64
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_2|param_val|4
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_3|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_4|param_val|50
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_5|param_val|10
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_6|param_val|50
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GRU_disturb1|algorithm_model_id|${AlgorithmModelID}|param_id|disturb1_param_7|param_val|2
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|disturb1_col_1|cfg_col_value|0|cfg_col_name|Time
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|disturb1_col_2|cfg_col_value|1|cfg_col_name|Data (TB)
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|disturb1_col_3|cfg_col_value|2,3|cfg_col_name|标签,小时数
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|标签|create_time|now|user_id|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|小时数|create_time|now|user_id|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='标签'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|中秋节|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|台风|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|地铁故障|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|周末|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|标签|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|重阳节|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|国庆节|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='小时数'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|小时数|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|0|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|2|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|3|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|4|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|5|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|6|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|7|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|8|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|9|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|10|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|11|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|12|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|13|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|14|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|15|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|16|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|17|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|18|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|19|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|20|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|21|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|22|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|23|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加AI模型，gru <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_AddAiModel(self):
		u"""添加AI模型，factorLGBM"""
		pres = """
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
				"参数设置": [
					"5",
					"7",
					"63",
					"0.02",
					"0.01",
					"0.01",
					"1000"
				],
				"列设置": {
					"时间列": "时间列",
					"预测列": "预测列",
					"特征列": [
						"特征列1",
						"特征列2"
					],
					"干扰因素列": [
						"干扰因素1",
						"干扰因素2"
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型factorLGBM|model_desc|auto_AI模型factorLGBM描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|factorLGBM.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_1|param_val|5
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_2|param_val|7
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_3|param_val|63
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_4|param_val|0.02
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_5|param_val|0.01
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_6|param_val|0.01
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorLGBM|algorithm_model_id|${AlgorithmModelID}|param_id|factorLGBM_param_7|param_val|1000
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorLGBM_col_1|cfg_col_value|0|cfg_col_name|时间列
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorLGBM_col_2|cfg_col_value|1|cfg_col_name|预测列
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorLGBM_col_3|cfg_col_value|2,3|cfg_col_name|特征列1,特征列2
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorLGBM_col_4|cfg_col_value|4,5|cfg_col_name|干扰因素1,干扰因素2
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|干扰因素1|create_time|now|user_id|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|干扰因素2|create_time|now|user_id|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='干扰因素1'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|干扰因素1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|天晴|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|下雨|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='干扰因素2'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|干扰因素2|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|放假|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|没放假|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加AI模型，factorLGBM <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_AddAiModel(self):
		u"""添加AI模型，xgboost"""
		pres = """
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
				"参数设置": [
					"20",
					"8",
					"10",
					"0.05",
					"500"
				],
				"列设置": {
					"时间列": "ds",
					"预测列": "y",
					"干扰因素列": [
						"add_1",
						"add_2",
						"add_3"
					]
				}
			}
		}
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型xgboost|model_desc|auto_AI模型xgboost描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|xgboost.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorXGB|algorithm_model_id|${AlgorithmModelID}|param_id|factorXGB_param_1|param_val|20
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorXGB|algorithm_model_id|${AlgorithmModelID}|param_id|factorXGB_param_2|param_val|8
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorXGB|algorithm_model_id|${AlgorithmModelID}|param_id|factorXGB_param_3|param_val|10
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorXGB|algorithm_model_id|${AlgorithmModelID}|param_id|factorXGB_param_4|param_val|0.05
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|factorXGB|algorithm_model_id|${AlgorithmModelID}|param_id|factorXGB_param_5|param_val|500
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorXGB_col_1|cfg_col_value|0|cfg_col_name|ds
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorXGB_col_2|cfg_col_value|1|cfg_col_name|y
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|factorXGB_col_3|cfg_col_value|2,3,4|cfg_col_name|add_1,add_2,add_3
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|add_1|create_time|now|user_id|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|add_2|create_time|now|user_id|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_cate_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_name|add_3|create_time|now|user_id|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='add_1'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|add_1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|0|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|2|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|3|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|4|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|5|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|6|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='add_2'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|add_2|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|0|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		GetData|${Database}.main|select dist_cate_id from tn_model_dist_cate_cfg where algorithm_model_id='${AlgorithmModelID}' and dist_cate_name='add_3'|DistCateID
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|add_3|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|0|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		CheckData|${Database}.main.tn_model_dist_name_cfg|1|algorithm_model_id|${AlgorithmModelID}|dist_cate_id|${DistCateID}|dist_name|1|dist_source|0|create_time|now|update_time|now|user_id|${LoginUser}|updater|${LoginUser}
		"""
		log.info('>>>>> 添加AI模型，xgboost <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddAiModel(self):
		u"""添加AI模型，lightgbm"""
		pres = """
		global|ModelName|auto_AI模型lightgbm
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
				"参数设置": [
					"10",
					"31",
					"1",
					"-1",
					"0.1",
					"255"
				],
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
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型lightgbm|model_desc|auto_AI模型lightgbm描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|classification.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_1|param_val|10
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_2|param_val|31
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_3|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_4|param_val|-1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_5|param_val|0.1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|lightgbm|algorithm_model_id|${AlgorithmModelID}|param_id|lightgbm_param_6|param_val|255
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|lightgbm_col_1|cfg_col_value||cfg_col_name|
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|lightgbm_col_2|cfg_col_value|14|cfg_col_name|IS_REAL_ALARM
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|lightgbm_col_3|cfg_col_value|0,1,2,3,4,5,6,7,8,9,10,11,12,13|cfg_col_name|country_id,IMPORTANCE,REQ_SUCCESS_RATE,DIVINE_REQ_SUCCESS_RATE,REQ_SUCCESS,SCALER_REQ_SUCCESS_DRIFT,REQ_SUM,SCALER_REQ_SUM_DRIFT,DIVINE_REQ_SUCCESS,DIVINE_REQ_SUM,REQ_SUCCESS_RATE_DRIFT,REQ_SUCCESS_RATE_DRIFT_FLAG,COUNT,WARN_TIME
		"""
		log.info('>>>>> 添加AI模型，lightgbm <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddAiModel(self):
		u"""添加AI模型，梯度提升树（GBDT）"""
		pres = """
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
				"参数设置": [
					"100",
					"2",
					"1",
					"None",
					"3",
					"0.1",
					"1"
				],
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
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型梯度提升树（GBDT）|model_desc|auto_AI模型梯度提升树（GBDT）描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|classification.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_1|param_val|100
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_2|param_val|2
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_3|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_4|param_val|None
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_5|param_val|3
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_6|param_val|0.1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|GBDT|algorithm_model_id|${AlgorithmModelID}|param_id|GBDT_param_7|param_val|1
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|GBDT_col_1|cfg_col_value||cfg_col_name|
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|GBDT_col_2|cfg_col_value|14|cfg_col_name|IS_REAL_ALARM
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|GBDT_col_3|cfg_col_value|0,1,2,3,4,5,6,7,8,9,10,11,12,13|cfg_col_name|country_id,IMPORTANCE,REQ_SUCCESS_RATE,DIVINE_REQ_SUCCESS_RATE,REQ_SUCCESS,SCALER_REQ_SUCCESS_DRIFT,REQ_SUM,SCALER_REQ_SUM_DRIFT,DIVINE_REQ_SUCCESS,DIVINE_REQ_SUM,REQ_SUCCESS_RATE_DRIFT,REQ_SUCCESS_RATE_DRIFT_FLAG,COUNT,WARN_TIME
		"""
		log.info('>>>>> 添加AI模型，梯度提升树（GBDT） <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddAiModel(self):
		u"""添加AI模型，随机森林模型"""
		pres = """
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
				"参数设置": [
					"100",
					"2",
					"1",
					"auto"
				],
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
		checks = """
		CheckMsg|操作成功
		CheckData|${Database}.main.tn_algorithm_model|1|model_name|auto_AI模型随机森林|model_desc|auto_AI模型随机森林描述|train_data_scale|80|test_data_scale|20|train_test_timeout|3600|data_file_name|classification.csv|belong_id|${BelongID}|domain_id|${DomainID}|user_id|${LoginUser}|create_time|now|updater|${LoginUser}|update_time|now|FetchID|algorithm_model_id
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|random_forest|algorithm_model_id|${AlgorithmModelID}|param_id|random_forest_param_1|param_val|100
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|random_forest|algorithm_model_id|${AlgorithmModelID}|param_id|random_forest_param_2|param_val|2
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|random_forest|algorithm_model_id|${AlgorithmModelID}|param_id|random_forest_param_3|param_val|1
		CheckData|${Database}.main.tn_algorithm_model_param|1|algorithm_id|random_forest|algorithm_model_id|${AlgorithmModelID}|param_id|random_forest_param_4|param_val|auto
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|random_forest_col_1|cfg_col_value||cfg_col_name|
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|random_forest_col_2|cfg_col_value|14|cfg_col_name|IS_REAL_ALARM
		CheckData|${Database}.main.tn_model_data_cfg|1|algorithm_model_id|${AlgorithmModelID}|cfg_col_id|random_forest_col_3|cfg_col_value|0,1,2,3,4,5,6,7,8,9,10,11,12,13|cfg_col_name|country_id,IMPORTANCE,REQ_SUCCESS_RATE,DIVINE_REQ_SUCCESS_RATE,REQ_SUCCESS,SCALER_REQ_SUCCESS_DRIFT,REQ_SUM,SCALER_REQ_SUM_DRIFT,DIVINE_REQ_SUCCESS,DIVINE_REQ_SUM,REQ_SUCCESS_RATE_DRIFT,REQ_SUCCESS_RATE_DRIFT_FLAG,COUNT,WARN_TIME
		"""
		log.info('>>>>> 添加AI模型，随机森林模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_ImportDisturb(self):
		u"""gru模型导入干扰因素"""
		action = {
			"操作": "ImportDisturb",
			"参数": {
				"模型名称": "auto_AI模型gru",
				"文件名": "disturbModel.xlsx"
			}
		}
		checks = """
		CheckMsg|导入干扰因素配置项成功
		GetData|${Database}.main|select algorithm_model_id from tn_algorithm_model where model_name='auto_AI模型gru' and belong_id='${BelongID}' and domain_id='${DomainID}'|AlgorithmModelID
		CheckData|${Database}.main.tn_model_dist_time_cfg|96|algorithm_model_id|${AlgorithmModelID}
		"""
		log.info('>>>>> gru模型导入干扰因素 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_ListAiModel(self):
		u"""AI模型查询，按模型名称查询"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"模型名称": "auto"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按模型名称查询 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，LSTM预测模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "LSTM预测模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，LSTM预测模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，SARIMA预测模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "SARIMA预测模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，SARIMA预测模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，GRU预测模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "GRU预测模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，GRU预测模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_ListAiModel(self):
		u"""AI模型查询，按算法名称查询， factorLGBM"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "factorLGBM"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询， factorLGBM <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，xgboost预测模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "xgboost预测模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，xgboost预测模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，lightgbm模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "lightgbm模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，lightgbm模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，梯度提升树（GBDT）模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "梯度提升树（GBDT）模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，梯度提升树（GBDT）模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_ListAiModel(self):
		u"""AI模型查询，按算法名称查询，随机森林模型"""
		action = {
			"操作": "ListAiModel",
			"参数": {
				"查询条件": {
					"算法名称": "随机森林模型"
				}
			}
		}
		checks = """
		CheckMsg|
		"""
		log.info('>>>>> AI模型查询，按算法名称查询，随机森林模型 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def tearDown(self):  # 最后执行的函数
		self.browser = gbl.service.get("browser")
		success = Result(self).run_success()
		if not success:
			saveScreenShot()
		self.browser.refresh()


if __name__ == '__main__':
	unittest.main()
