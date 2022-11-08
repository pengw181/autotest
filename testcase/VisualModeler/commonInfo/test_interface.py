# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/31 下午4:23

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class Interface(unittest.TestCase):

    log.info("装载第三方接口配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_interface_clear(self):
        u"""第三方接口管理，数据清理"""
        pre = """
        ${Database}.main|delete from tn_interface_cfg where interface_name like 'auto_%'
        """
        action = {
            "操作": "InterfaceDataClear",
            "参数": {
                "接口名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_interface_add(self):
        u"""添加第三方接口管理，webservice接口"""
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_用户密码期限检测",
                "接口类型": "webservice",
                "接口url": ["${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_interface_add(self):
        u"""添加第三方接口管理，restful接口"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_第三方restful接口_notify')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_第三方restful接口_notify'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify",
                "接口类型": "restful",
                "接口url": ["http://${MockIp}:5009/mock/http/notify"],
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
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_interface_add(self):
        u"""添加第三方接口管理，soap接口"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_第三方soap接口')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_第三方soap接口'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_第三方soap接口",
                "接口类型": "soap",
                "接口url": ["http://${MockIp}:8088/mockServiceSoapBinding/login"],
                "数据类型": "私有",
                "请求方式": "post",
                "超时时间": "30",
                "返回结果样例": {
                    "结果类型": "xml",
                    "结果样例": ["<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sam=\"http://www.soapui.org/sample/\">", "<soapenv:Header/>", "<soapenv:Body>", "<sam:loginResponse>", "<sessionid>${sessionid}</sessionid>", "</sam:loginResponse>", "</soapenv:Body>", "</soapenv:Envelope>"]
                },
                "请求体内容": {
                    "请求体内容类型": "xml",
                    "请求体内容": ["<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:sam=\"http://www.soapui.org/sample/\">", "<soapenv:Header/>", "<soapenv:Body>", "<sam:login>", "<username>Login</username>", "<password>Login123</password>", "</sam:login>", "</soapenv:Body>", "</soapenv:Envelope>"]
                }
            }
        }
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_interface_clear(self):
        u"""第三方接口管理，数据清理"""
        action = {
            "操作": "InterfaceDataClear",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_6_interface_add(self):
        u"""添加第三方接口管理，restful接口，配置请求头"""
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify",
                "接口类型": "restful",
                "接口url": ["http://${MockIp}:5009/mock/http/notify"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_interface_delete(self):
        u"""删除第三方接口：auto_第三方restful接口_notify"""
        action = {
            "操作": "DeleteInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_interface_add(self):
        u"""添加第三方接口管理，restful接口，配置请求参数"""
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify",
                "接口类型": "restful",
                "接口url": ["http://${MockIp}:5009/mock/http/notify"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_interface_delete(self):
        u"""删除第三方接口：auto_第三方restful接口_notify"""
        action = {
            "操作": "DeleteInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_interface_add(self):
        u"""添加第三方接口管理，restful接口，配置请求体"""
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify",
                "接口类型": "restful",
                "接口url": ["http://${MockIp}:5009/mock/http/notify"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_interface_add(self):
        u"""添加第三方接口管理，restful接口，mock_post"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_post')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_post'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_万能mock_post",
                "接口类型": "restful",
                "接口url": ["http://192.168.88.116:8090/mocker/mock"],
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
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_interface_add(self):
        u"""添加第三方接口管理，restful接口，mock_get"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_get')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_get'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_万能mock_get",
                "接口类型": "restful",
                "接口url": ["http://192.168.88.116:8090/mocker/mock"],
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
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_interface_add(self):
        u"""添加第三方接口管理，restful接口，mock_put"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_put')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_put'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_万能mock_put",
                "接口类型": "restful",
                "接口url": ["http://192.168.88.116:8090/mocker/mock"],
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
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_interface_add(self):
        u"""添加第三方接口管理，restful接口，mock_delete"""
        pre = """
        ${Database}.main|delete from tn_interface_param_cfg where interface_id = (select interface_id from tn_interface_cfg where interface_name = 'auto_万能mock_delete')
        ${Database}.main|delete from tn_interface_cfg where interface_name = 'auto_万能mock_delete'
        """
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_万能mock_delete",
                "接口类型": "restful",
                "接口url": ["http://192.168.88.116:8090/mocker/mock"],
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
        msg = "保存成功"
        result = self.worker.pre(pre)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_interface_clear(self):
        u"""第三方接口管理，数据清理"""
        action = {
            "操作": "InterfaceDataClear",
            "参数": {
                "接口名称": "auto_用户密码期限检测"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_16_interface_add(self):
        u"""添加第三方接口管理，webservice接口"""
        action = {
            "操作": "AddInterface",
            "参数": {
                "接口名称": "auto_用户密码期限检测",
                "接口类型": "webservice",
                "接口url": ["${ThirdSystem}/AiSee/services/CheckUserPwdOverdue?wsdl"],
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
        msg = "保存成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_interface_test(self):
        u"""测试第三方接口，webservice接口"""
        action = {
            "操作": "TestInterface",
            "参数": {
                "接口名称": "auto_用户密码期限检测"
            }
        }
        msg = "{'status':'1','msg':'运行成功'}"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_18_interface_test(self):
        u"""测试第三方接口，restful接口"""
        action = {
            "操作": "TestInterface",
            "参数": {
                "接口名称": "auto_第三方restful接口_notify"
            }
        }
        msg = "Interface request date save to database successfully"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_interface_test(self):
        u"""测试第三方接口，soap接口"""
        action = {
            "操作": "TestInterface",
            "参数": {
                "接口名称": "auto_第三方soap接口"
            }
        }
        msg = "soapenv:Envelope"
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
