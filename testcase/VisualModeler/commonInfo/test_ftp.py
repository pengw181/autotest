# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/31 下午2:48

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class Ftp(unittest.TestCase):

    log.info("装载远程FTP服务器配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_ftp_clear(self):
        u"""远程FTP服务器管理，数据清理"""
        pre = """
        ${Database}.main|delete from tn_ftp_server_cfg where server_name like 'auto_%'
        """
        action = {
            "操作": "FTPDataClear",
            "参数": {
                "服务器名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_ftp_add(self):
        u"""添加远程FTP服务器"""
        action = {
            "操作": "AddFTP",
            "参数": {
                "服务器名称": "auto_ftp",
                "服务器IP": "192.168.88.132",
                "服务器端口": "21",
                "用户名": "viper.catalog",
                "密码": "viper.catalog_pass",
                "服务器类型": "ftp",
                "服务器编码": "UTF-8",
                "数据类型": "公有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_ftp_add(self):
        u"""添加远程FTP服务器，服务器名称在本领域存在"""
        action = {
            "操作": "AddFTP",
            "参数": {
                "服务器名称": "auto_ftp",
                "服务器IP": "192.168.88.132",
                "服务器端口": "21",
                "用户名": "viper.catalog",
                "密码": "viper.catalog_pass",
                "服务器类型": "ftp",
                "服务器编码": "UTF-8",
                "数据类型": "公有"
            }
        }
        msg = "服务器名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_ftp_test(self):
        u"""测试ftp连通性"""
        action = {
            "操作": "TestFTP",
            "参数": {
                "服务器名称": "auto_ftp"
            }
        }
        msg = "ftp连接测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_ftp_add(self):
        u"""添加远程FTP服务器，密码错误"""
        pre = """
        ${Database}.main|delete from tn_ftp_server_cfg where server_name='auto_sftp'
        """
        action = {
            "操作": "AddFTP",
            "参数": {
                "服务器名称": "auto_sftp",
                "服务器IP": "192.168.88.132",
                "服务器端口": "22",
                "用户名": "viper.catalog",
                "密码": "viper.catalog",
                "服务器类型": "sftp",
                "服务器编码": "UTF-8",
                "数据类型": "公有"
            }
        }
        msg = "ftp连接测试失败！用户名或密码错误！"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_ftp_update(self):
        u"""修改ftp"""
        action = {
            "操作": "UpdateFTP",
            "参数": {
                "服务器名称": "auto_ftp",
                "修改内容": {
                    "服务器名称": "auto_sftp",
                    "服务器IP": "192.168.88.132",
                    "服务器端口": "22",
                    "用户名": "viper.catalog",
                    "密码": "viper.catalog_pass",
                    "服务器类型": "sftp",
                    "服务器编码": "GBK",
                    "数据类型": "私有"
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_ftp_test(self):
        u"""测试sftp连通性"""
        action = {
            "操作": "TestFTP",
            "参数": {
                "服务器名称": "auto_sftp"
            }
        }
        msg = "ftp连接测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_ftp_delete(self):
        u"""删除远程FTP服务器"""
        action = {
            "操作": "DeleteFTP",
            "参数": {
                "服务器名称": "auto_sftp"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_ftp_add(self):
        u"""添加远程FTP服务器"""
        action = {
            "操作": "AddFTP",
            "参数": {
                "服务器名称": "auto_ftp",
                "服务器IP": "192.168.88.132",
                "服务器端口": "21",
                "用户名": "viper.catalog",
                "密码": "viper.catalog_pass",
                "服务器类型": "ftp",
                "服务器编码": "UTF-8",
                "数据类型": "私有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_ftp_add(self):
        u"""添加远程SFTP服务器"""
        action = {
            "操作": "AddFTP",
            "参数": {
                "服务器名称": "auto_sftp",
                "服务器IP": "192.168.88.132",
                "服务器端口": "22",
                "用户名": "viper.catalog",
                "密码": "viper.catalog_pass",
                "服务器类型": "sftp",
                "服务器编码": "UTF-8",
                "数据类型": "私有"
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
