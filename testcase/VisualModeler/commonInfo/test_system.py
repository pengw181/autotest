# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/31 下午5:35

import unittest
from src.screenShot import screenShot
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class System(unittest.TestCase):

    log.info("装载第三方系统配置测试用例")
    worker = CaseWorker()
    crawler_ver = get_global_var("CrawlerVersion")

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_system_clear(self):
        u"""第三方系统管理，数据清理"""
        pre = """
        ${Database}.main|delete from tn_node_vos_login_cfg where platform like 'auto_%'
        """
        action = {
            "操作": "ThirdSystemDataClear",
            "参数": {
                "平台名称": "auto_第三方系统",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_system_add(self):
        u"""添加第三方系统，简易版，不验证登录"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_system_add(self):
        u"""添加第三方系统，平台名称在本领域存在"""
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
        msg = "第三方系统名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_system_test(self):
        u"""测试第三方系统连通性，不验证登录"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_system_add(self):
        u"""添加第三方系统，使用代理"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_system_add(self):
        u"""添加第三方系统，验证登录"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_system_test(self):
        u"""测试第三方系统连通性，验证登录"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_system_add(self):
        u"""添加第三方系统，使用验证码"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_system_add(self):
        u"""添加第三方系统，完整版"""
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
                        ["aa", "id"],
                        ["bb", "xpath"],
                        ["ok", "alert"]
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
                            ["cc", "id"],
                            ["dd", "xpath"],
                            ["dd1", "id"]
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_system_update(self):
        u"""修改第三方系统，取消验证码配置"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_system_update(self):
        u"""修改第三方系统，取消优先点击页面元素和是否在输入账号密码后运行配置"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_system_update(self):
        u"""修改第三方系统，取消代理配置"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != 'ctcc', "非深圳电信版本不测试")
    def test_17_system_update(self):
        u"""修改第三方系统，修改为外部网"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != 'ctcc', "非深圳电信版本不测试")
    def test_18_system_test(self):
        u"""测试第三方系统连通性，外部网，验证登录"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_system_update(self):
        u"""修改第三方系统，密码错误"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_system_test(self):
        u"""测试第三方系统连通性，密码错误，验证登录"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "账号或密码错误"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_system_update(self):
        u"""修改第三方系统，浏览器类型配置成谷歌"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_system_test(self):
        u"""测试第三方系统连通性，谷歌浏览器"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_system_add(self):
        u"""添加第三方系统，火狐浏览器"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_system_test(self):
        u"""测试第三方系统连通性，火狐浏览器"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_火狐"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_system_add(self):
        u"""添加第三方系统，ie浏览器"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_system_test(self):
        u"""测试第三方系统连通性，ie浏览器"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_ie"
            }
        }
        msg = "爬虫服务端未配置，请检查"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_system_update(self):
        u"""修改第三方系统，修改成https"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_system_test(self):
        u"""测试第三方系统连通性，https测试"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_system_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_system_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_system_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_system_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_system_update(self):
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "测试成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统https"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_system_add(self):
        u"""添加第三方系统，真实版"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_system_add(self):
        u"""添加第三方系统，简易版"""
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_system_add(self):
        u"""添加第三方系统，打开首页失败"""
        action = {
            "操作": "AddThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_打开首页失败",
                "平台地址": "http://10.222.13.4/test",
                "平台网络标识": "${PlatformNwName}",
                "浏览器类型": "chrome",
                "数据类型": "私有"
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_system_test(self):
        u"""测试第三方系统连通性"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_打开首页失败"
            }
        }
        msg = "测试失败"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_system_delete(self):
        u"""删除第三方系统"""
        action = {
            "操作": "DeleteThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_打开首页失败"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_45_system_add(self):
        u"""添加第三方系统，开启手机验证码"""
        action = {
            "操作": "AddThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码",
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
                    "登录异常输出": "账号或密码错误",
                    "是否开启手机验证码": {
                        "状态": "开启",
                        "验证码输入标识": "userId",
                        "验证码输入标识类型": "id",
                        "手机验证码发送按钮标识": "password",
                        "手机验证码发送按钮标识类型": "id"
                    }
                }
            }
        }
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_46_system_test(self):
        u"""测试第三方系统连通性，开启手机验证码，不输入验证码"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码"
            }
        }
        msg = "手机验证码为空"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_47_system_test(self):
        u"""测试第三方系统连通性，开启手机验证码，验证码输入错误"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码",
                "手机验证码": "112233"
            }
        }
        msg = "第三方系统登录失败"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_48_system_test(self):
        u"""测试第三方系统连通性，开启手机验证码，验证码格式错误，包含非数字和字母"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码",
                "手机验证码": "你好11"
            }
        }
        msg = "验证码由数字和字母组成！长度必须小于等于10个字符"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_49_system_test(self):
        u"""测试第三方系统连通性，开启手机验证码，验证码格式错误，长度超过10哥字符"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码",
                "手机验证码": "12345678901"
            }
        }
        # 长度超过10字符，在页面无法提交
        msg = "手机验证码为空"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    @unittest.skipIf(crawler_ver != "ctcc", "深圳电信版本才支持手机验证码")
    def test_50_system_test(self):
        u"""测试第三方系统连通性，输入正确手机验证码"""
        action = {
            "操作": "TestThirdSystem",
            "参数": {
                "平台名称": "auto_第三方系统_手机验证码",
                "手机验证码": "${LoginUser}"
            }
        }
        msg = "测试成功"
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
