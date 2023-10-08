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


class System(unittest.TestCase):

	log.info("装载第三方系统管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_ThirdSystemDataClear(self):
		u"""第三方系统管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_node_vos_login_cfg where platform like 'auto_%'
		"""
		action = {
			"操作": "ThirdSystemDataClear",
			"参数": {
				"平台名称": "auto_第三方系统",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 第三方系统管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddThirdSystem(self):
		u"""添加第三方系统,简易版,不验证登录"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|0|label_username||username||label_pwd||pwd|null|label_submitbtn||is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type||label_pwd_type||label_submit_type||label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|1|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code||login_err_code_type||login_err_output||retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,简易版,不验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddThirdSystem(self):
		u"""添加第三方系统,平台名称在本领域存在"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加第三方系统,平台名称在本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddThirdSystem(self):
		u"""添加第三方系统,平台名称本领域不存在,在其他领域存在"""
		pres = """
		${Database}.main|delete from tn_node_vos_login_cfg where platform='auto_第三方系统' 
		${Database}.main|insert into tn_node_vos_login_cfg(platform_login_cfg_id, platform, visit_url, is_valid_login, label_username, username, label_pwd, pwd, label_submitbtn, is_valid_code, label_code, label_code_image, browser_type, label_username_type, label_pwd_type, label_submit_type, label_code_type, label_code_image_type, valid_code_model, update_time, data_origin, proxy_id, data_type_id, is_proxy, is_first_click_ele, is_inp_acc_last_click, click_elem_json, platform_nw_tag, belong_id, domain_id, create_time, create_by, update_by, login_err_code, login_err_code_type, login_err_output, retry_first_click_tag) VALUES (uuid(),'auto_第三方系统','${ThirdSystem}/AiSee/html/login/login.html','0','','','',null,'','0','','','chrome','','','','','','',now(),'2','','0','0','0','0',null,'0','440100','AiSeeCN',now(),'pw','pw','','','','1')
		"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|0|label_username||username||label_pwd||pwd|null|label_submitbtn||is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type||label_pwd_type||label_submit_type||label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|1|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code||login_err_code_type||login_err_output||retry_first_click_tag|1
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|0|label_username||username||label_pwd||pwd|null|label_submitbtn||is_valid_code|0|belong_id|440100|domain_id|AiSeeCN|create_by|pw|create_time|notnull|update_time|notnull|update_by|pw|label_code||label_code_image||browser_type|chrome|label_username_type||label_pwd_type||label_submit_type||label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code||login_err_code_type||login_err_output||retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,平台名称本领域不存在,在其他领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestThirdSystem(self):
		u"""测试第三方系统连通性,不验证登录"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性,不验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_DeleteThirdSystem(self):
		u"""删除第三方系统"""
		pres = """
		${Database}.main|delete from tn_node_vos_login_cfg where platform='auto_第三方系统' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "DeleteThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|0|platform|auto_第三方系统
		"""
		log.info('>>>>> 删除第三方系统 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_7_AddThirdSystem(self):
		u"""添加第三方系统,使用代理"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有",
				"是否启用代理": {
					"状态": "开启",
					"代理名称": "auto_代理"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select proxy_id from tn_proxy_cfg where proxy_name='auto_代理'|ProxyID
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|0|label_username||username||label_pwd||pwd|null|label_submitbtn||is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type||label_pwd_type||label_submit_type||label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id|${ProxyID}|data_type_id|1|is_proxy|1|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code||login_err_code_type||login_err_output||retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,使用代理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_DeleteThirdSystem(self):
		u"""删除第三方系统"""
		action = {
			"操作": "DeleteThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|0|platform|auto_第三方系统
		"""
		log.info('>>>>> 删除第三方系统 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_AddThirdSystem(self):
		u"""添加第三方系统,验证登录"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有",
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|1|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_TestThirdSystem(self):
		u"""测试第三方系统连通性,验证登录"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性,验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_DeleteThirdSystem(self):
		u"""删除第三方系统"""
		action = {
			"操作": "DeleteThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|0|platform|auto_第三方系统
		"""
		log.info('>>>>> 删除第三方系统 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_AddThirdSystem(self):
		u"""添加第三方系统,使用验证码"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有",
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误",
					"是否开启验证码": {
						"状态": "开启",
						"验证码输入标识": "ee",
						"验证码输入标识类型": "xpath",
						"验证码图片标识": "ff",
						"验证码图片标识类型": "id",
						"验证码识别模型": "网络资源验证码模型"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|1|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code|ee|label_code_image|ff|browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type|xpath|label_code_image_type|id|valid_code_model|captcha_reg_feature_gzrs|data_origin|2|proxy_id||data_type_id|1|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,使用验证码 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_DeleteThirdSystem(self):
		u"""删除第三方系统"""
		action = {
			"操作": "DeleteThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|0|platform|auto_第三方系统
		"""
		log.info('>>>>> 删除第三方系统 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_AddThirdSystem(self):
		u"""添加第三方系统,完整版"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "公有",
				"是否优先点击页面元素": {
					"状态": "开启",
					"登录失败是否重试优先点击页面元素": "是",
					"点击元素标识": [
						[
							"aa",
							"id"
						],
						[
							"bb",
							"xpath"
						],
						[
							"ok",
							"alert"
						]
					]
				},
				"是否启用代理": {
					"状态": "开启",
					"代理名称": "auto_代理"
				},
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误",
					"是否在输入账号密码后运行": {
						"状态": "开启",
						"点击元素标识": [
							[
								"cc",
								"id"
							],
							[
								"dd",
								"xpath"
							],
							[
								"dd1",
								"id"
							]
						]
					},
					"是否开启验证码": {
						"状态": "开启",
						"验证码输入标识": "ee",
						"验证码输入标识类型": "xpath",
						"验证码图片标识": "ff",
						"验证码图片标识类型": "id",
						"验证码识别模型": "网络资源验证码模型"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select proxy_id from tn_proxy_cfg where proxy_name='auto_代理'|ProxyID
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|1|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code|ee|label_code_image|ff|browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type|xpath|label_code_image_type|id|valid_code_model|captcha_reg_feature_gzrs|data_origin|2|proxy_id|${ProxyID}|data_type_id|1|is_proxy|1|is_first_click_ele|1|is_inp_acc_last_click|1|click_elem_json|[{"click_type":"is_first_click_ele","index":1,"elem_code":"aa","label_code_type":"id"},{"click_type":"is_first_click_ele","index":2,"elem_code":"bb","label_code_type":"xpath"},{"click_type":"is_first_click_ele","index":3,"elem_code":"ok","label_code_type":"alert"},{"click_type":"is_inp_acc_last_click","index":1,"elem_code":"cc","label_code_type":"id"},{"click_type":"is_inp_acc_last_click","index":2,"elem_code":"dd","label_code_type":"xpath"},{"click_type":"is_inp_acc_last_click","index":3,"elem_code":"dd1","label_code_type":"id"}]|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,完整版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_UpdateThirdSystem(self):
		u"""修改第三方系统,取消验证码配置"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"是否开启验证码": {
							"状态": "关闭"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select proxy_id from tn_proxy_cfg where proxy_name='auto_代理'|ProxyID
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id|${ProxyID}|data_type_id|0|is_proxy|1|is_first_click_ele|1|is_inp_acc_last_click|1|click_elem_json|[{"click_type":"is_first_click_ele","index":1,"elem_code":"aa","label_code_type":"id"},{"click_type":"is_first_click_ele","index":2,"elem_code":"bb","label_code_type":"xpath"},{"click_type":"is_first_click_ele","index":3,"elem_code":"ok","label_code_type":"alert"},{"click_type":"is_inp_acc_last_click","index":1,"elem_code":"cc","label_code_type":"id"},{"click_type":"is_inp_acc_last_click","index":2,"elem_code":"dd","label_code_type":"xpath"},{"click_type":"is_inp_acc_last_click","index":3,"elem_code":"dd1","label_code_type":"id"}]|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 修改第三方系统,取消验证码配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_UpdateThirdSystem(self):
		u"""修改第三方系统,取消优先点击页面元素和是否在输入账号密码后运行配置"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否优先点击页面元素": {
						"状态": "关闭"
					},
					"是否验证登录": {
						"状态": "开启",
						"是否在输入账号密码后运行": {
							"状态": "关闭"
						}
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		GetData|${Database}.main|select proxy_id from tn_proxy_cfg where proxy_name='auto_代理'|ProxyID
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id|${ProxyID}|data_type_id|0|is_proxy|1|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> 修改第三方系统,取消优先点击页面元素和是否在输入账号密码后运行配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_17_UpdateThirdSystem(self):
		u"""修改第三方系统,取消代理配置"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否启用代理": {
						"状态": "关闭"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> 修改第三方系统,取消代理配置 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_18_UpdateThirdSystem(self):
		u"""UNTEST,修改第三方系统,修改为外部网"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "外部网",
					"浏览器类型": "chrome",
					"数据类型": "私有"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|1|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> UNTEST,修改第三方系统,修改为外部网 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_19_TestThirdSystem(self):
		u"""UNTEST,测试第三方系统连通性,外部网,验证登录"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> UNTEST,测试第三方系统连通性,外部网,验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_UpdateThirdSystem(self):
		u"""修改第三方系统,密码错误"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "1qazXSW@1",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> 修改第三方系统,密码错误 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_TestThirdSystem(self):
		u"""测试第三方系统连通性,密码错误,验证登录"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|账号或密码错误
		"""
		log.info('>>>>> 测试第三方系统连通性,密码错误,验证登录 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_UpdateThirdSystem(self):
		u"""修改第三方系统,浏览器类型配置成谷歌"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> 修改第三方系统,浏览器类型配置成谷歌 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_23_TestThirdSystem(self):
		u"""测试第三方系统连通性,谷歌浏览器"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性,谷歌浏览器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_24_AddThirdSystem(self):
		u"""添加第三方系统,火狐"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统_火狐",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "firefox",
				"数据类型": "私有",
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统_火狐|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|firefox|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,火狐 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_25_TestThirdSystem(self):
		u"""UNTEST,测试第三方系统连通性,火狐浏览器"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统_火狐"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> UNTEST,测试第三方系统连通性,火狐浏览器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_26_AddThirdSystem(self):
		u"""添加第三方系统,ie"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统_ie",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "ie",
				"数据类型": "私有",
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统_ie|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|ie|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,ie <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	@unittest.skip
	def test_27_TestThirdSystem(self):
		u"""UNTEST,测试第三方系统连通性,ie浏览器"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统_ie"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> UNTEST,测试第三方系统连通性,ie浏览器 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_28_UpdateThirdSystem(self):
		u"""修改第三方系统,修改成https"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null
		"""
		log.info('>>>>> 修改第三方系统,修改成https <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_29_TestThirdSystem(self):
		u"""测试第三方系统连通性,https测试"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性,https测试 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_30_UpdateThirdSystem(self):
		u"""修改第三方系统，浏览器超时时间设为-1"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "-1",
					"空闲刷新时间": "0",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|-1|session_timeout|0
		"""
		log.info('>>>>> 修改第三方系统，浏览器超时时间设为-1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_31_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_32_UpdateThirdSystem(self):
		u"""修改第三方系统，浏览器超时时间设为0"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "0",
					"空闲刷新时间": "0",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|0|session_timeout|0
		"""
		log.info('>>>>> 修改第三方系统，浏览器超时时间设为0 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_33_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_34_UpdateThirdSystem(self):
		u"""修改第三方系统，浏览器超时时间设为30"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "30",
					"空闲刷新时间": "0",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|30|session_timeout|0
		"""
		log.info('>>>>> 修改第三方系统，浏览器超时时间设为30 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_35_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_36_UpdateThirdSystem(self):
		u"""修改第三方系统，空闲刷新时间设为-1"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "30",
					"空闲刷新时间": "-1",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|30|session_timeout|-1
		"""
		log.info('>>>>> 修改第三方系统，空闲刷新时间设为-1 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_37_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_38_UpdateThirdSystem(self):
		u"""修改第三方系统，空闲刷新时间设为0"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "30",
					"空闲刷新时间": "0",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|30|session_timeout|0
		"""
		log.info('>>>>> 修改第三方系统，空闲刷新时间设为0 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_39_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_40_UpdateThirdSystem(self):
		u"""修改第三方系统，空闲刷新时间设为180"""
		action = {
			"操作": "UpdateThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https",
				"修改内容": {
					"平台名称": "auto_第三方系统https",
					"平台地址": "${ThirdSystemHttps}/AiSee/html/login/login.html",
					"平台网络标识": "${PlatformNwName}",
					"浏览器类型": "chrome",
					"浏览器超时时间": "30",
					"空闲刷新时间": "180",
					"数据类型": "私有",
					"是否验证登录": {
						"状态": "开启",
						"用户名标识": "userId",
						"用户名标识类型": "id",
						"账号": "${LoginUser}",
						"密码标识": "password",
						"密码标识类型": "id",
						"密码": "${LoginPwd}",
						"登录按钮标识": "loginButton",
						"登录按钮标识类型": "id",
						"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
						"登录异常标识类型": "xpath",
						"登录异常输出": "账号或密码错误"
					}
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统https|visit_url|${ThirdSystemHttps}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|null|browse_timeout|30|session_timeout|180
		"""
		log.info('>>>>> 修改第三方系统，空闲刷新时间设为180 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_41_TestThirdSystem(self):
		u"""测试第三方系统连通性"""
		action = {
			"操作": "TestThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试第三方系统连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_42_DeleteThirdSystem(self):
		u"""删除第三方系统"""
		action = {
			"操作": "DeleteThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统https"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|0|platform|auto_第三方系统https
		"""
		log.info('>>>>> 删除第三方系统 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_43_ThirdSystemDataClear(self):
		u"""第三方系统管理,数据清理"""
		action = {
			"操作": "ThirdSystemDataClear",
			"参数": {
				"平台名称": "auto_第三方系统"
			}
		}
		log.info('>>>>> 第三方系统管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_44_AddThirdSystem(self):
		u"""添加第三方系统,真实版"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "私有",
				"是否验证登录": {
					"状态": "开启",
					"用户名标识": "userId",
					"用户名标识类型": "id",
					"账号": "${LoginUser}",
					"密码标识": "password",
					"密码标识类型": "id",
					"密码": "${LoginPwd}",
					"登录按钮标识": "loginButton",
					"登录按钮标识类型": "id",
					"登录异常标识": "//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]",
					"登录异常标识类型": "xpath",
					"登录异常输出": "账号或密码错误"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|1|label_username|userId|username|pw|label_pwd|password|pwd|notnull|label_submitbtn|loginButton|is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|notnull|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type|id|label_pwd_type|id|label_submit_type|id|label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code|//div[@id='errorTip']/span[contains(text(),'账号或密码错误')]|login_err_code_type|xpath|login_err_output|账号或密码错误|retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,真实版 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_45_AddThirdSystem(self):
		u"""添加第三方系统,简易版"""
		action = {
			"操作": "AddThirdSystem",
			"参数": {
				"平台名称": "auto_第三方系统_简易版",
				"平台地址": "${ThirdSystem}/AiSee/html/login/login.html",
				"平台网络标识": "${PlatformNwName}",
				"浏览器类型": "chrome",
				"数据类型": "私有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_node_vos_login_cfg|1|platform|auto_第三方系统_简易版|visit_url|${ThirdSystem}/AiSee/html/login/login.html|is_valid_login|0|label_username||username||label_pwd||pwd|null|label_submitbtn||is_valid_code|0|belong_id|${BelongID}|domain_id|${DomainID}|create_by|${LoginUser}|create_time|now|update_time|now|update_by|${LoginUser}|label_code||label_code_image||browser_type|chrome|label_username_type||label_pwd_type||label_submit_type||label_code_type||label_code_image_type||valid_code_model||data_origin|2|proxy_id||data_type_id|0|is_proxy|0|is_first_click_ele|0|is_inp_acc_last_click|0|click_elem_json|null|platform_nw_tag|0|login_err_code||login_err_code_type||login_err_output||retry_first_click_tag|1
		"""
		log.info('>>>>> 添加第三方系统,简易版 <<<<<')
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
