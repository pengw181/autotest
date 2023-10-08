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


class Email(unittest.TestCase):

	log.info("装载邮箱管理测试用例")
	worker = CaseWorker()

	def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
		self.browser = gbl.service.get("browser")
		self.worker.init()

	def test_1_MailDataClear(self):
		u"""邮箱管理,数据清理"""
		pres = """
		${Database}.main|delete from tn_email_cfg where mail_account = 'pw@henghaodata.com'
		"""
		action = {
			"操作": "MailDataClear",
			"参数": {
				"邮箱地址": "auto_",
				"模糊匹配": "是"
			}
		}
		log.info('>>>>> 邮箱管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result

	def test_2_AddMail(self):
		u"""添加邮箱"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "公有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "pop3",
				"接收服务器地址": "pop-ent.21cn.com",
				"接收端口": "110",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_test@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|pop3|receive_server_name|pop-ent.21cn.com|receive_port|110|mail_account|pw@henghaodata.com|pwd|notnull|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|1|data_type_id|1|del_flag|null
		"""
		log.info('>>>>> 添加邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_3_AddMail(self):
		u"""添加邮箱,邮箱地址在本领域存在"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "公有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "pop3",
				"接收服务器地址": "pop-ent.21cn.com",
				"接收端口": "110",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "是"
			}
		}
		checks = """
		CheckMsg|已存在
		"""
		log.info('>>>>> 添加邮箱,邮箱地址在本领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_4_AddMail(self):
		u"""添加邮箱,邮箱地址在本领域不存在,在其他领域存在"""
		pres = """
		${Database}.main|delete from tn_email_cfg where mail_addr='auto_test@henghaodata.com' 
		${Database}.main|insert into tn_email_cfg(mail_id, proxy_id, data_type_id, mail_addr, cfg_type, protocol_type, server_name, send_port, receive_protocol_type, receive_server_name, receive_port, mail_account, pwd, create_time, update_time, create_by, update_by, del_flag, belong_id, domain_id, is_platf_account) values(uuid(),'',1,'auto_test@henghaodata.com','0,1','smtp','smtp-ent.21cn.com','25','pop3','pop-ent.21cn.com','110','pw@henghaodata.com','notnull',now(),now(),'pw','pw',NULL,'440100','AiSeeCN',0)
		"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "公有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "pop3",
				"接收服务器地址": "pop-ent.21cn.com",
				"接收端口": "110",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_test@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|pop3|receive_server_name|pop-ent.21cn.com|receive_port|110|mail_account|pw@henghaodata.com|pwd|notnull|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|1|data_type_id|1|del_flag|null
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_test@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|pop3|receive_server_name|pop-ent.21cn.com|receive_port|110|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|notnull|create_by|pw|update_by|pw|belong_id|440100|domain_id|AiSeeCN|is_platf_account|0|data_type_id|1|del_flag|null
		"""
		log.info('>>>>> 添加邮箱,邮箱地址在本领域不存在,在其他领域存在 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_5_TestMail(self):
		u"""测试邮箱地址smtp/pop连通性"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试邮箱地址smtp/pop连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_6_MailDataClear(self):
		u"""邮箱管理,数据清理"""
		action = {
			"操作": "MailDataClear",
			"参数": {
				"邮箱地址": "auto_cc@henghaodata.com"
			}
		}
		log.info('>>>>> 邮箱管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_7_AddMail(self):
		u"""添加邮箱,联系人"""
		pres = """
		${Database}.main|delete from tn_email_cfg where mail_addr='auto_cc@henghaodata.com' and belong_id='${BelongID}' and domain_id='${DomainID}'
		"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_cc@henghaodata.com",
				"邮箱类型": [
					"联系人"
				],
				"数据类型": "公有"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_cc@henghaodata.com|cfg_type|2|protocol_type||server_name||send_port|null|receive_protocol_type||receive_server_name||receive_port|null|mail_account||pwd|null|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account||data_type_id|1|del_flag|null
		"""
		log.info('>>>>> 添加邮箱,联系人 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_8_UpdateMail(self):
		u"""修改邮箱"""
		pres = """
		${Database}.main|delete from tn_email_cfg where mail_addr='auto_test@henghaodata.com' and belong_id='440100' and domain_id='AiSeeCN'
		"""
		action = {
			"操作": "UpdateMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com",
				"修改内容": {
					"邮箱地址": "auto_new@henghaodata.com",
					"邮箱类型": [
						"接收邮箱",
						"发送邮箱",
						"联系人"
					],
					"数据类型": "私有",
					"发送协议类型": "smtp",
					"发送服务器地址": "smtp-ent.21cn.com",
					"发送端口": "25",
					"接收协议类型": "imap",
					"接收服务器地址": "imap-ent.21cn.com",
					"接收端口": "143",
					"账号": "pw@henghaodata.com",
					"密码或授权码": "${EmailPwd}",
					"代理名称": "",
					"平台账号": "否"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_new@henghaodata.com|cfg_type|0,1,2|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|imap|receive_server_name|imap-ent.21cn.com|receive_port|143|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|0|data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 修改邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.pre(pres)
		assert result
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_9_TestMail(self):
		u"""测试邮箱地址smtp/imap连通性"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试邮箱地址smtp/imap连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_10_UpdateMail(self):
		u"""修改邮箱密码,输入错误密码"""
		action = {
			"操作": "UpdateMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com",
				"修改内容": {
					"邮箱类型": [
						"发送邮箱"
					],
					"密码或授权码": "12345678"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_new@henghaodata.com|cfg_type|1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|imap|receive_server_name|imap-ent.21cn.com|receive_port|143|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account||data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 修改邮箱密码,输入错误密码 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_11_TestMail(self):
		u"""发送邮箱,密码错误,测试邮箱"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|账号或密码错误
		"""
		log.info('>>>>> 发送邮箱,密码错误,测试邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_12_UpdateMail(self):
		u"""将邮箱设置为接收邮箱"""
		action = {
			"操作": "UpdateMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com",
				"修改内容": {
					"邮箱类型": [
						"接收邮箱"
					],
					"密码或授权码": "12345678"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_new@henghaodata.com|cfg_type|0|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|imap|receive_server_name|imap-ent.21cn.com|receive_port|143|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account||data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 将邮箱设置为接收邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_13_TestMail(self):
		u"""接收邮箱,密码错误,测试邮箱"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|账号或密码错误
		"""
		log.info('>>>>> 接收邮箱,密码错误,测试邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_14_UpdateMail(self):
		u"""重新设置正确密码"""
		action = {
			"操作": "UpdateMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com",
				"修改内容": {
					"邮箱类型": [
						"接收邮箱",
						"发送邮箱",
						"联系人"
					],
					"密码或授权码": "${EmailPwd}"
				}
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_new@henghaodata.com|cfg_type|0,1,2|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|imap|receive_server_name|imap-ent.21cn.com|receive_port|143|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account||data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 重新设置正确密码 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_15_TestMail(self):
		u"""测试smtp/imap连通性"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试smtp/imap连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_16_MailDataClear(self):
		u"""邮箱管理,数据清理"""
		action = {
			"操作": "MailDataClear",
			"参数": {
				"邮箱地址": "aireade.p@outlook.com"
			}
		}
		log.info('>>>>> 邮箱管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_17_AddMail(self):
		u"""添加邮箱，使用EXCHANGE协议"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "aireade.p@outlook.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "私有",
				"发送协议类型": "EXCHANGE",
				"发送服务器地址": "outlook.live.com",
				"发送端口": "25",
				"接收协议类型": "EXCHANGE",
				"接收服务器地址": "outlook.live.com",
				"接收端口": "443",
				"账号": "aireade.p@outlook.com",
				"密码或授权码": "${EmailPwd2}",
				"代理名称": "",
				"平台账号": "否"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|aireade.p@outlook.com|cfg_type|0,1|protocol_type|EXCHANGE|server_name|outlook.live.com|send_port|25|receive_protocol_type|EXCHANGE|receive_server_name|outlook.live.com|receive_port|443|mail_account|aireade.p@outlook.com|pwd|notnull|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|0|data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 添加邮箱，使用EXCHANGE协议 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_18_TestMail(self):
		u"""测试EXCHANGE连通性"""
		action = {
			"操作": "TestMail",
			"参数": {
				"邮箱地址": "aireade.p@outlook.com"
			}
		}
		checks = """
		CheckMsg|测试成功
		"""
		log.info('>>>>> 测试EXCHANGE连通性 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_19_DeleteMail(self):
		u"""删除邮箱"""
		action = {
			"操作": "DeleteMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com"
			}
		}
		checks = """
		CheckMsg|删除成功
		CheckData|${Database}.main.tn_email_cfg|0|mail_addr|auto_new@henghaodata.com
		"""
		log.info('>>>>> 删除邮箱 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_20_AddMail(self):
		u"""添加邮箱imap"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_new@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "私有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "imap",
				"接收服务器地址": "imap-ent.21cn.com",
				"接收端口": "143",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "否"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_new@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|imap|receive_server_name|imap-ent.21cn.com|receive_port|143|mail_account|pw@henghaodata.com|pwd|notnull|create_time|notnull|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|0|data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 添加邮箱imap <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_21_AddMail(self):
		u"""添加邮箱pop"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "auto_test@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "私有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "pop3",
				"接收服务器地址": "pop-ent.21cn.com",
				"接收端口": "110",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "否"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|auto_test@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|pop3|receive_server_name|pop-ent.21cn.com|receive_port|110|mail_account|pw@henghaodata.com|pwd|notnull|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|0|data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 添加邮箱pop <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result
		log.info(gbl.temp.get("ResultMsg"))
		result = self.worker.check(checks)
		assert result

	def test_22_MailDataClear(self):
		u"""邮箱管理,数据清理"""
		action = {
			"操作": "MailDataClear",
			"参数": {
				"邮箱地址": "pw@henghaodata.com"
			}
		}
		log.info('>>>>> 邮箱管理,数据清理 <<<<<')
		gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
		result = self.worker.action(action)
		assert result

	def test_23_AddMail(self):
		u"""添加邮箱，平台邮箱"""
		action = {
			"操作": "AddMail",
			"参数": {
				"邮箱地址": "pw@henghaodata.com",
				"邮箱类型": [
					"接收邮箱",
					"发送邮箱"
				],
				"数据类型": "私有",
				"发送协议类型": "smtp",
				"发送服务器地址": "smtp-ent.21cn.com",
				"发送端口": "25",
				"接收协议类型": "pop3",
				"接收服务器地址": "pop-ent.21cn.com",
				"接收端口": "110",
				"账号": "pw@henghaodata.com",
				"密码或授权码": "${EmailPwd}",
				"代理名称": "",
				"平台账号": "是"
			}
		}
		checks = """
		CheckMsg|保存成功
		CheckData|${Database}.main.tn_email_cfg|1|mail_addr|pw@henghaodata.com|cfg_type|0,1|protocol_type|smtp|server_name|smtp-ent.21cn.com|send_port|25|receive_protocol_type|pop3|receive_server_name|pop-ent.21cn.com|receive_port|110|mail_account|pw@henghaodata.com|pwd|notnull|create_time|now|update_time|now|create_by|${LoginUser}|update_by|${LoginUser}|belong_id|${BelongID}|domain_id|${DomainID}|is_platf_account|1|data_type_id|0|del_flag|null
		"""
		log.info('>>>>> 添加邮箱，平台邮箱 <<<<<')
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
