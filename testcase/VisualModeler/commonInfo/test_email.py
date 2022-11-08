# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/30 下午9:36

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class Email(unittest.TestCase):

    log.info("装载邮箱配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_email_clear(self):
        u"""邮箱配置管理，数据清理"""
        pre = """
        ${Database}.main|delete from tn_email_cfg where mail_account = 'pw@henghaodata.com'
        ${Database}.main|delete from tn_email_cfg where mail_addr like 'auto_'
        """
        action = {
            "操作": "MailDataClear",
            "参数": {
                "邮箱地址": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_email_add(self):
        u"""添加邮箱"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "auto_test@henghaodata.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_email_add(self):
        u"""添加邮箱，邮箱地址在本领域存在"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "auto_test@henghaodata.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "邮箱地址已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_email_test(self):
        u"""测试邮箱地址smtp/pop连通性"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "auto_test@henghaodata.com"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_email_add(self):
        u"""添加邮箱，联系人"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "auto_cc@henghaodata.com",
                "邮箱类型": ["联系人"],
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_email_update(self):
        u"""修改邮箱"""
        action = {
            "操作": "UpdateMail",
            "参数": {
                "邮箱地址": "auto_test@henghaodata.com",
                "修改内容": {
                    "邮箱地址": "auto_new@henghaodata.com",
                    "邮箱类型": ["接收邮箱", "发送邮箱", "联系人"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_email_test(self):
        u"""测试邮箱地址smtp/imap连通性"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_email_update(self):
        u"""修改邮箱密码，输入错误密码"""
        action = {
            "操作": "UpdateMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com",
                "修改内容": {
                    "邮箱类型": ["发送邮箱"],
                    "密码或授权码": "12345678"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_email_test(self):
        u"""发送邮箱，测试邮箱，邮箱密码错误"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com"
            }
        }
        msg = "测试失败：账号或密码错误"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_email_update(self):
        u"""修改邮箱，将邮箱设置为接收邮箱"""
        action = {
            "操作": "UpdateMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com",
                "修改内容": {
                    "邮箱类型": ["接收邮箱"],
                    "密码或授权码": "12345678"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_email_test(self):
        u"""接收邮箱，测试邮箱，密码错误"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com"
            }
        }
        msg = "测试失败：账号或密码错误"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_email_update(self):
        u"""修改邮箱，重新设置正确密码"""
        action = {
            "操作": "UpdateMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com",
                "修改内容": {
                    "邮箱类型": ["接收邮箱", "发送邮箱", "联系人"],
                    "密码或授权码": "${EmailPwd}"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_email_test(self):
        u"""测试smtp/imap连通性"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_email_clear(self):
        u"""邮箱配置管理，数据清理"""
        action = {
            "操作": "MailDataClear",
            "参数": {
                "邮箱地址": "aireade.p@outlook.com"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_15_email_add(self):
        u"""添加邮箱，使用EXCHANGE协议"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "aireade.p@outlook.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_email_test(self):
        u"""测试EXCHANGE连通性"""
        action = {
            "操作": "TestMail",
            "参数": {
                "邮箱地址": "aireade.p@outlook.com"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_email_delete(self):
        u"""删除邮箱"""
        action = {
            "操作": "DeleteMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_email_add(self):
        u"""添加邮箱imap"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "auto_new@henghaodata.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_email_add(self):
        u"""添加邮箱pop"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "auto_test@henghaodata.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_email_clear(self):
        u"""邮箱配置管理，数据清理"""
        action = {
            "操作": "MailDataClear",
            "参数": {
                "邮箱地址": "pw@henghaodata.com"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_21_email_add(self):
        u"""添加邮箱pop"""
        action = {
            "操作": "AddMail",
            "参数": {
                "邮箱地址": "pw@henghaodata.com",
                "邮箱类型": ["接收邮箱", "发送邮箱"],
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
        msg = "保存成功"
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
