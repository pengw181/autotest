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


class Interface(unittest.TestCase):

	log.info("装载第三方接口管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_InterfaceDataClear(self):
		u"""第三方接口管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_interface_cfg where interface_name like 'auto_%'
		"""
		action = {
			"操作": "InterfaceDataClear",
			"参数": {
				"接口名称": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 第三方接口管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddInterface(self):
		u"""添加第三方接口管理，webservice接口"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_用户密码期限检测",
				"接口类型": "webservice",
				"接口url": [
					"${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl"
				],
				"数据类型": "私有",
				"接口空间名": "http://webservice.portal.aisee.hh.com/",
				"接口方法名": "checkUserPwdOverdue",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"status\":\"1\",\"msg\":\"运行成功\"}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_用户密码期限检测| interface_url|${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl|interface_type|1|data_type_id|0|interface_ns|http://webservice.portal.aisee.hh.com/|interface_method|checkUserPwdOverdue|result_sample|{"status":"1","msg":"运行成功"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30
		"""
		log.info('>>>>> 添加第三方接口管理，webservice接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddInterface(self):
		u"""添加第三方接口管理，restful接口"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify",
				"接口类型": "restful",
				"接口url": [
					"http://${MockIp}:5009/mock/http/notify"
				],
				"数据类型": "私有",
				"请求方式": "post",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "字符串",
					"结果样例": "Interface request date save to database successfully!"
				},
				"接口请求头": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数默认值": "20"
					},
					{
						"参数名称": "address",
						"参数类型": "字符",
						"参数默认值": "广州"
					}
				],
				"请求体内容": {
					"请求体内容类型": "json",
					"请求体内容": "{\"type\": 1,\"name\": \"abc\"}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方restful接口_notify| interface_url|http://${MockIp}:5009/mock/http/notify|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|Interface request date save to database successfully!|result_type|1|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|1|request_body|{"type": 1,"name": "abc"}|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|age|param_type|2|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header3|param_name|address|param_type|1|param_order|3|param_sample|广州|param_category|header
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddInterface(self):
		u"""添加第三方接口管理，soap接口"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方soap接口",
				"接口类型": "soap",
				"接口url": [
					"http://${MockIp}:8088/mockServiceSoapBinding/login"
				],
				"数据类型": "私有",
				"请求方式": "post",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "xml",
					"结果样例": [
						"<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sam=\"http://www.soapui.org/sample/\">",
						"<soapenv:Header/>",
						"<soapenv:Body>",
						"<sam:loginResponse>",
						"<sessionid>${sessionid}</sessionid>",
						"</sam:loginResponse>",
						"</soapenv:Body>",
						"</soapenv:Envelope>"
					]
				},
				"请求体内容": {
					"请求体内容类型": "xml",
					"请求体内容": [
						"<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sam=\"http://www.soapui.org/sample/\">",
						"<soapenv:Header/>",
						"<soapenv:Body>",
						"<sam:login>",
						"<username>Login</username>",
						"<password>Login123</password>",
						"</sam:login>",
						"</soapenv:Body>",
						"</soapenv:Envelope>"
					]
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方soap接口| interface_url|http://${MockIp}:8088/mockServiceSoapBinding/login|interface_type|4|data_type_id|0|interface_ns||interface_method||result_sample|<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sam="http://www.soapui.org/sample/">~<soapenv:Header/>~<soapenv:Body>~<sam:loginResponse>~<sessionid>${sessionid}</sessionid>~</sam:loginResponse>~</soapenv:Body>~</soapenv:Envelope>|result_type|3|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|1|request_body|<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sam="http://www.soapui.org/sample/">~<soapenv:Header/>~<soapenv:Body>~<sam:login>~<username>Login</username>~<password>Login123</password>~</sam:login>~</soapenv:Body>~</soapenv:Envelope>|request_body_type|2
		"""
		log.info('>>>>> 添加第三方接口管理，soap接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_InterfaceDataClear(self):
		u"""第三方接口管理,数据清理"""
		action = {
			"操作": "InterfaceDataClear",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify"
			}
		}
		log.info('>>>>> 第三方接口管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_6_AddInterface(self):
		u"""添加第三方接口管理，restful接口，配置请求头"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify",
				"接口类型": "restful",
				"接口url": [
					"http://${MockIp}:5009/mock/http/notify"
				],
				"数据类型": "公有",
				"请求方式": "get",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "字符串",
					"结果样例": "Interface request date save to database successfully!"
				},
				"接口请求头": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数默认值": "20"
					},
					{
						"参数名称": "address",
						"参数类型": "字符",
						"参数默认值": "广州"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方restful接口_notify| interface_url|http://${MockIp}:5009/mock/http/notify|interface_type|3|data_type_id|1|interface_ns||interface_method||result_sample|Interface request date save to database successfully!|result_type|1|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|2|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|age|param_type|2|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header3|param_name|address|param_type|1|param_order|3|param_sample|广州|param_category|header
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，配置请求头 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_DeleteInterface(self):
		u"""删除第三方接口：auto_第三方restful接口_notify"""
		pres = """
		${Database}.main|select interface_id from tn_interface_cfg where interface_name= 'auto_第三方restful接口_notify'|InterfaceID|
		"""
		action = {
			"操作": "DeleteInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_interface_cfg|0|interface_name|auto_第三方restful接口_notify
		CheckData|${Database}.main.tn_interface_param_cfg|0|interface_id|${InterfaceID}
		"""
		log.info('>>>>> 删除第三方接口：auto_第三方restful接口_notify <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_AddInterface(self):
		u"""添加第三方接口管理，restful接口，配置请求参数"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify",
				"接口类型": "restful",
				"接口url": [
					"http://${MockIp}:5009/mock/http/notify"
				],
				"数据类型": "公有",
				"请求方式": "get",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "字符串",
					"结果样例": "Interface request date save to database successfully!"
				},
				"接口参数": [
					{
						"参数名称": "action",
						"参数类型": "字符",
						"参数值样例": "购买"
					},
					{
						"参数名称": "accout",
						"参数类型": "数值",
						"参数值样例": "100"
					},
					{
						"参数名称": "quantity",
						"参数类型": "数值",
						"参数值样例": "2"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方restful接口_notify| interface_url|http://${MockIp}:5009/mock/http/notify|interface_type|3|data_type_id|1|interface_ns||interface_method||result_sample|Interface request date save to database successfully!|result_type|1|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|2|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param1|param_name|action|param_type|1|param_order|1|param_sample|购买|param_category|param
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param2|param_name|accout|param_type|2|param_order|2|param_sample|100|param_category|param
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param3|param_name|quantity|param_type|2|param_order|3|param_sample|2|param_category|param
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，配置请求参数 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_DeleteInterface(self):
		u"""删除第三方接口：auto_第三方restful接口_notify"""
		pres = """
		${Database}.main|select interface_id from tn_interface_cfg where interface_name= 'auto_第三方restful接口_notify'|InterfaceID|
		"""
		action = {
			"操作": "DeleteInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_interface_cfg|0|interface_name|auto_第三方restful接口_notify
		CheckData|${Database}.main.tn_interface_param_cfg|0|interface_id|${InterfaceID}
		"""
		log.info('>>>>> 删除第三方接口：auto_第三方restful接口_notify <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_AddInterface(self):
		u"""添加第三方接口管理，restful接口，配置请求体"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify",
				"接口类型": "restful",
				"接口url": [
					"http://${MockIp}:5009/mock/http/notify"
				],
				"数据类型": "私有",
				"请求方式": "post",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "字符串",
					"结果样例": "Interface request date save to database successfully!"
				},
				"接口请求头": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数默认值": "20"
					},
					{
						"参数名称": "address",
						"参数类型": "字符",
						"参数默认值": "广州"
					}
				],
				"请求体内容": {
					"请求体内容类型": "json",
					"请求体内容": "{\"type\": 1,\"name\": \"abc\"}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方restful接口_notify| interface_url|http://${MockIp}:5009/mock/http/notify|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|Interface request date save to database successfully!|result_type|1|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|1|request_body|{"type": 1,"name": "abc"}|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|age|param_type|2|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header3|param_name|address|param_type|1|param_order|3|param_sample|广州|param_category|header
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，配置请求体 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_11_DeleteInterface(self):
		u"""UNTEST,删除第三方接口：auto_第三方restful接口_notify"""
		pres = """
		${Database}.main|select interface_id from tn_interface_cfg where interface_name= 'auto_第三方restful接口_notify'|InterfaceID|
		"""
		action = {
			"操作": "DeleteInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_interface_cfg|0|interface_name|auto_第三方restful接口_notify
		CheckData|${Database}.main.tn_interface_param_cfg|0|interface_id|${InterfaceID}
		"""
		log.info('>>>>> UNTEST,删除第三方接口：auto_第三方restful接口_notify <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_12_AddInterface(self):
		u"""UNTEST,添加第三方接口，设置代理"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify",
				"接口类型": "restful",
				"接口url": [
					"http://${MockIp}:5009/mock/http/notify"
				],
				"数据类型": "公有",
				"请求方式": "get",
				"超时时间": "30",
				"代理名称": "自动化测试代理",
				"返回结果样例": {
					"结果类型": "字符串",
					"结果样例": "Interface request date save to database successfully!"
				},
				"接口请求头": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数默认值": "20"
					},
					{
						"参数名称": "address",
						"参数类型": "字符",
						"参数默认值": "广州"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select proxy_id from tn_proxy_cfg where proxy_name='自动化测试代理'|ProxyID
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_第三方restful接口_notify| interface_url|http://${MockIp}:5009/mock/http/notify|interface_type|3|data_type_id|1|interface_ns||interface_method||result_sample|Interface request date save to database successfully!|result_type|1|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|2|proxy_id|${ProxyID}|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|age|param_type|2|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header3|param_name|address|param_type|1|param_order|3|param_sample|广州|param_category|header
		"""
		log.info('>>>>> UNTEST,添加第三方接口，设置代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_AddInterface(self):
		u"""添加第三方接口管理，restful接口，mock_post"""
		pres = """
		${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_post')
		${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_post'
		"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_万能mock_post",
				"接口类型": "restful",
				"接口url": [
					"http://192.168.88.116:8090/mocker/mock"
				],
				"数据类型": "私有",
				"请求方式": "post",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"contextPath\":\"/VisualModeler\", \"msg\":\"server running\", \"time\":\"2019-07-09 11:08:21\"}"
				},
				"接口请求头": [
					{
						"参数名称": "param1",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "param2",
						"参数类型": "字符",
						"参数默认值": "20"
					},
					{
						"参数名称": "param3",
						"参数类型": "字符",
						"参数默认值": "广州"
					}
				],
				"接口参数": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数值样例": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数值样例": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_万能mock_post| interface_url|http://192.168.88.116:8090/mocker/mock|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|{"contextPath":"/VisualModeler", "msg":"server running", "time":"2019-07-09 11:08:21"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|1|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|param1|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|param2|param_type|1|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header3|param_name|param3|param_type|1|param_order|3|param_sample|广州|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|param
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param2|param_name|age|param_type|2|param_order|2|param_sample|100|param_category|param
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，mock_post <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddInterface(self):
		u"""添加第三方接口管理，restful接口，mock_get"""
		pres = """
		${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_get')
		${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_get'
		"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_万能mock_get",
				"接口类型": "restful",
				"接口url": [
					"http://192.168.88.116:8090/mocker/mock"
				],
				"数据类型": "私有",
				"请求方式": "get",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"contextPath\":\"/VisualModeler\", \"msg\":\"server running\", \"time\":\"2019-07-09 11:08:21\"}"
				},
				"接口请求头": [
					{
						"参数名称": "param1",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "param2",
						"参数类型": "字符",
						"参数默认值": "20"
					}
				],
				"接口参数": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数值样例": "张三"
					},
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数值样例": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_万能mock_get| interface_url|http://192.168.88.116:8090/mocker/mock|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|{"contextPath":"/VisualModeler", "msg":"server running", "time":"2019-07-09 11:08:21"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|2|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|param1|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|param2|param_type|1|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|param
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param2|param_name|age|param_type|2|param_order|2|param_sample|100|param_category|param
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，mock_get <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_AddInterface(self):
		u"""添加第三方接口管理，restful接口，mock_put"""
		pres = """
		${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_put')
		${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_put'
		"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_万能mock_put",
				"接口类型": "restful",
				"接口url": [
					"http://192.168.88.116:8090/mocker/mock"
				],
				"数据类型": "私有",
				"请求方式": "put",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"contextPath\":\"/VisualModeler\", \"msg\":\"server running\", \"time\":\"2019-07-09 11:08:21\"}"
				},
				"接口请求头": [
					{
						"参数名称": "param1",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "param2",
						"参数类型": "字符",
						"参数默认值": "20"
					}
				],
				"接口参数": [
					{
						"参数名称": "age",
						"参数类型": "数值",
						"参数值样例": "100"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_万能mock_put| interface_url|http://192.168.88.116:8090/mocker/mock|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|{"contextPath":"/VisualModeler", "msg":"server running", "time":"2019-07-09 11:08:21"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|3|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|param1|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|param2|param_type|1|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param1|param_name|age|param_type|2|param_order|1|param_sample|100|param_category|param
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，mock_put <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_AddInterface(self):
		u"""添加第三方接口管理，restful接口，mock_delete"""
		pres = """
		${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_delete')
		${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_delete'
		"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_万能mock_delete",
				"接口类型": "restful",
				"接口url": [
					"http://192.168.88.116:8090/mocker/mock"
				],
				"数据类型": "私有",
				"请求方式": "delete",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"contextPath\":\"/VisualModeler\", \"msg\":\"server running\", \"time\":\"2019-07-09 11:08:21\"}"
				},
				"接口请求头": [
					{
						"参数名称": "param1",
						"参数类型": "字符",
						"参数默认值": "张三"
					},
					{
						"参数名称": "param2",
						"参数类型": "字符",
						"参数默认值": "20"
					}
				],
				"接口参数": [
					{
						"参数名称": "name",
						"参数类型": "字符",
						"参数值样例": "张三"
					}
				]
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_万能mock_delete| interface_url|http://192.168.88.116:8090/mocker/mock|interface_type|3|data_type_id|0|interface_ns||interface_method||result_sample|{"contextPath":"/VisualModeler", "msg":"server running", "time":"2019-07-09 11:08:21"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30|request_type|4|FetchID|interface_id
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header1|param_name|param1|param_type|1|param_order|1|param_sample|张三|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|header2|param_name|param2|param_type|1|param_order|2|param_sample|20|param_category|header
		CheckData|${Database}.main.tn_interface_param_cfg|1|interface_id|${InterfaceID}|param_id|param1|param_name|name|param_type|1|param_order|1|param_sample|张三|param_category|param
		"""
		log.info('>>>>> 添加第三方接口管理，restful接口，mock_delete <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_InterfaceDataClear(self):
		u"""第三方接口管理,数据清理"""
		action = {
			"操作": "InterfaceDataClear",
			"参数": {
				"接口名称": "auto_用户密码期限检测"
			}
		}
		log.info('>>>>> 第三方接口管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_18_AddInterface(self):
		u"""添加第三方接口管理，webservice接口"""
		action = {
			"操作": "AddInterface",
			"参数": {
				"接口名称": "auto_用户密码期限检测",
				"接口类型": "webservice",
				"接口url": [
					"${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl"
				],
				"数据类型": "私有",
				"接口空间名": "http://webservice.portal.aisee.hh.com/",
				"接口方法名": "checkUserPwdOverdue",
				"超时时间": "30",
				"返回结果样例": {
					"结果类型": "json",
					"结果样例": "{\"status\":\"1\",\"msg\":\"运行成功\"}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_interface_cfg|1|interface_name|auto_用户密码期限检测| interface_url|${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl|interface_type|1|data_type_id|0|interface_ns|http://webservice.portal.aisee.hh.com/|interface_method|checkUserPwdOverdue|result_sample|{"status":"1","msg":"运行成功"}|result_type|2|user_id|${LoginUser}|create_time|now|update_time|now|updater|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|connect_timeout|30
		"""
		log.info('>>>>> 添加第三方接口管理，webservice接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_TestInterface(self):
		u"""测试第三方接口，webservice接口"""
		action = {
			"操作": "TestInterface",
			"参数": {
				"接口名称": "auto_用户密码期限检测"
			}
		}
		checks = """
		CheckMsg|{'status':'1','msg':'运行成功'}
		"""
		log.info('>>>>> 测试第三方接口，webservice接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_TestInterface(self):
		u"""测试第三方接口，restful接口"""
		action = {
			"操作": "TestInterface",
			"参数": {
				"接口名称": "auto_第三方restful接口_notify"
			}
		}
		checks = """
		CheckMsg|Interface request date save to database successfully
		"""
		log.info('>>>>> 测试第三方接口，restful接口 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_TestInterface(self):
		u"""测试第三方接口，soap接口"""
		action = {
			"操作": "TestInterface",
			"参数": {
				"接口名称": "auto_第三方soap接口"
			}
		}
		checks = """
		CheckMsg|soapenv:Envelope
		"""
		log.info('>>>>> 测试第三方接口，soap接口 <<<<<')
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
