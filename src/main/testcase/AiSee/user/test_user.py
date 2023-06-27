# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/6/15 下午5:07

import unittest
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseWorker
from src.main.python.lib.screenShot import saveScreenShot


class UserManager(unittest.TestCase):

    log.info("装载用户管理配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = gbl.service.get("browser")
        self.worker.init()

    def test_1_user_clear(self):
        u"""用户数据清理，删除历史数据"""
        action = {
            "操作": "UserDataClear",
            "参数": {
                "登录账号": "auto",
                "模糊匹配": "是"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_user_add(self):
        u"""用户管理，添加用户"""
        pres = """
        ${Database}.sso|delete from tn_user where user_id like 'auto%' and is_delete='1'
        """
        action = {
            "操作": "AddUser",
            "参数": {
                "登录账号": "autom",
                "用户名称": "自动化测试A",
                "性别": "男",
                "用户密码": "12345678",
                "所属组织": "海珠区事业办",
                "电话号码": "13000000000",
                "邮箱": "auto1@125.com",
                "portal号": "auto125",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "60",
                "密码过期预警天数": "1"
            }
        }
        result = self.worker.pre(pres)
        assert result
        msg = "用户信息保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_3_user_add(self):
        u"""用户管理，添加用户，登录账号已存在且未删除"""
        action = {
            "操作": "AddUser",
            "参数": {
                "登录账号": "autom",
                "用户名称": "自动化测试A",
                "性别": "男",
                "用户密码": "12345678",
                "所属组织": "海珠区事业办",
                "电话号码": "13000000000",
                "邮箱": "auto1@125.com",
                "portal号": "auto125",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "60",
                "密码过期预警天数": "1"
            }
        }
        msg = "登录账号已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_4_user_add(self):
        u"""用户管理，添加用户，用户名称已存在且未删除"""
        action = {
            "操作": "AddUser",
            "参数": {
                "登录账号": "autom",
                "用户名称": "自动化测试A",
                "性别": "男",
                "用户密码": "12345678",
                "所属组织": "海珠区事业办",
                "电话号码": "13000000000",
                "邮箱": "auto1@125.com",
                "portal号": "auto125",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "60",
                "密码过期预警天数": "1"
            }
        }
        msg = "用户名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_5_user_update(self):
        u"""用户管理，修改用户"""
        action = {
            "操作": "UpdateUser",
            "参数": {
                "用户": "autom",
                "修改内容": {
                    "用户名称": "自动化测试B",
                    "性别": "女",
                    "用户密码": "11111111",
                    "所属组织": "黄埔区事业办",
                    "电话号码": "13100000000",
                    "邮箱": "auto2@115.com",
                    "portal号": "auto115",
                    "启用状态": "启用",
                    "锁定状态": "未锁定",
                    "密码有效期(天)": "80",
                    "密码过期预警天数": "3"
                }
            }
        }
        msg = "用户信息修改成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_6_user_delete(self):
        u"""用户管理，删除用户，用户为启用状态"""
        action = {
            "操作": "DeleteUser",
            "参数": {
                "登录账号": "autom"
            }
        }
        msg = "用户启用时禁止删除"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_7_user_update(self):
        u"""用户管理，修改用户，修改为禁用状态"""
        action = {
            "操作": "UpdateUser",
            "参数": {
                "登录账号": "autom",
                "修改内容": {
                    "启用状态": "禁用"
                }
            }
        }
        msg = "用户信息修改成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_8_user_delete(self):
        u"""用户管理，删除用户，用户为禁用状态"""
        action = {
            "操作": "DeleteUser",
            "参数": {
                "登录账号": "autom"
            }
        }
        msg = "用户信息删除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_9_user_add(self):
        u"""用户管理，添加用户：自动化测试A"""
        action = {
            "操作": "AddUser",
            "参数": {
                "登录账号": "autom1",
                "用户名称": "自动化测试A",
                "性别": "男",
                "用户密码": "12345678",
                "所属组织": "海珠区事业办",
                "电话号码": "13000000000",
                "邮箱": "auto1@125.com",
                "portal号": "auto125",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "60",
                "密码过期预警天数": "1"
            }
        }
        msg = "用户信息保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_10_user_add(self):
        u"""用户管理，添加用户：自动化测试C"""
        action = {
            "操作": "AddUser",
            "参数": {
                "登录账号": "autom2",
                "用户名称": "自动化测试C",
                "性别": "男",
                "用户密码": "12345678",
                "所属组织": "海珠区事业办",
                "电话号码": "13000000000",
                "邮箱": "auto1@125.com",
                "portal号": "auto125",
                "启用状态": "启用",
                "锁定状态": "未锁定",
                "密码有效期(天)": "60",
                "密码过期预警天数": "1"
            }
        }
        msg = "用户信息保存成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_11_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元数据，移除全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "数据类型": "网元数据"
                },
                "分配类型": "移除全部"
            }
        }
        msg = "移除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_12_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，移除全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "数据类型": "网元类型数据"
                },
                "分配类型": "移除全部"
            }
        }
        msg = "移除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_13_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元数据，分配所选"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "auto_",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元数据"
                },
                "数据信息": [
                    "auto_TURK_TKea1",
                    "auto_TURK_TKea2",
                    "auto_TURK_TKea3"
                ],
                "分配类型": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_14_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元数据，分配全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "auto_",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元数据"
                },
                "分配类型": "分配全部"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_15_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，分配所选"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "数据信息": [
                    "AUTO",
                    "POP"
                ],
                "分配类型": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_16_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，分配全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "分配类型": "分配全部"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_17_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元数据，移除所选"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "auto_",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元数据"
                },
                "数据信息": [
                    "auto_TURK_TKea1",
                    "auto_TURK_TKea2",
                    "auto_TURK_TKea3"
                ],
                "分配类型": "移除所选"
            }
        }
        msg = "移除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_18_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，移除所选"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "数据信息": [
                    "AUTO",
                    "POP"
                ],
                "分配类型": "移除所选"
            }
        }
        msg = "移除成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_19_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，分配所选"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "autom1",
                "查询条件": {
                    "名称": "",
                    "厂家": "图科",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "数据信息": [
                    "AUTO",
                    "POP"
                ],
                "分配类型": "分配所选"
            }
        }
        msg = "分配成功"
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        assert gbl.temp.get("ResultMsg").startswith(msg)

    def test_20_data_permission_assign(self):
        u"""用户管理，数据权限分配，网元类型数据，分配全部"""
        action = {
            "操作": "AssignDataPermissions",
            "参数": {
                "登录账号": "${LoginUser}",
                "查询条件": {
                    "名称": "",
                    "厂家": "",
                    "归属": "${Belong}",
                    "领域": "${DomainID}",
                    "数据类型": "网元类型数据"
                },
                "分配类型": "分配全部"
            }
        }
        msg = "分配成功"
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
