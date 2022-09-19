# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 上午10:36

import unittest
from src.screenShot import screenShot
from common.variable.globalVariable import *
from common.log.logger import log
from gooflow.caseWorker import CaseWorker


class Script(unittest.TestCase):

    log.info("装载脚本配置测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_script_clear(self):
        u"""脚本管理，数据清理"""
        pres = """
        ${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
        ${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python')
        ${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本python'
        ${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java')
        ${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java')
        ${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本java'
        ${Database}.main|delete from tn_script_param_cfg where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar')
        ${Database}.main|delete from tn_script_version where script_id in (select script_id from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar')
        ${Database}.main|delete from tn_script_cfg where SCRIPT_NAME = 'auto_脚本jar'
        """
        action = {
            "操作": "ScriptDataClear",
            "参数": {
                "脚本名称": "auto_",
                "模糊匹配": "是"
            }
        }
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result

    def test_2_script_add(self):
        u"""添加脚本，类型python"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本python",
                "脚本类型": "python",
                "数据类型": "公有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_3_script_add(self):
        u"""添加脚本，类型java"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本java",
                "脚本类型": "java",
                "数据类型": "公有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_script_add(self):
        u"""添加脚本，类型jar"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "脚本类型": "jar",
                "数据类型": "公有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_script_add(self):
        u"""添加脚本，脚本名称在本领域存在"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本python",
                "脚本类型": "python",
                "数据类型": "公有"
            }
        }
        msg = "脚本名称已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_script_update(self):
        u"""修改脚本"""
        action = {
            "操作": "UpdateScript",
            "参数": {
                "脚本名称": "auto_脚本python",
                "修改内容": {
                    "脚本名称": "auto_脚本python新",
                    "数据类型": "私有"
                }
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_script_add_param(self):
        u"""修改脚本，添加参数"""
        action = {
            "操作": "AddScriptParams",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本参数": ["param1", "param2"]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_script_update_param(self):
        u"""修改脚本，修改参数"""
        action = {
            "操作": "UpdateScriptParams",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本参数": [[1, "parama"], [2, "paramb"]]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_script_upload_file(self):
        u"""上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "test_time.py"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_script_upload_file(self):
        u"""python类型脚本，上传java脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "readfile1.java"
            }
        }
        msg = "文件格式不正确，请选择py格式的文件"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_script_upload_file(self):
        u"""python类型脚本，上传jar脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "CompareDataUtil.jar"
            }
        }
        msg = "文件格式不正确，请选择py格式的文件"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_script_upload_file(self):
        u"""java类型脚本，上传python脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1",
                "脚本文件名": "fa.py"
            }
        }
        msg = "文件格式不正确，请选择java或jar格式的文件"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_script_upload_file(self):
        u"""java类型脚本，上传jar脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1",
                "脚本文件名": "CompareDataUtil.jar"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_14_script_upload_file(self):
        u"""jar类型脚本，上传python脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "版本号": "1",
                "脚本文件名": "test_time.py"
            }
        }
        msg = "文件格式不正确，请选择jar格式的文件"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_15_script_upload_file(self):
        u"""jar类型脚本，上传java脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "版本号": "1",
                "脚本文件名": "readfile1.java"
            }
        }
        msg = "文件格式不正确，请选择jar格式的文件"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_16_script_set_main(self):
        u"""设置主脚本"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "test_time.py",
                "右键": "设置为主脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_17_script_download_version(self):
        u"""下载版本"""
        action = {
            "操作": "DownloadScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1"
            }
        }
        checks = """
        CheckDownloadFile|auto_脚本python新_1|zip
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_18_script_download_file(self):
        u"""下载脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "test_time.py",
                "右键": "下载脚本"
            }
        }
        checks = """
        CheckDownloadFile|test_time|py
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_19_script_save_new(self):
        u"""保存新版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_20_script_update_content(self):
        u"""修改脚本内容"""
        action = {
            "操作": "UpdateScriptFileContent",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "test_time.py",
                "脚本内容": "print('hello world')"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_21_script_delete_file(self):
        u"""删除脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "1",
                "脚本文件名": "test_time.py",
                "右键": "删除脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_22_script_delete_version(self):
        u"""删除版本"""
        action = {
            "操作": "DeleteScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python新",
                "版本号": "2"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_script_delete_version(self):
        u"""删除版本,当前只有1个版本"""
        action = {
            "操作": "DeleteScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1"
            }
        }
        msg = "脚本至少保留一条版本信息，该条信息不可删除"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_script_delete(self):
        u"""删除脚本python"""
        action = {
            "操作": "DeleteScript",
            "参数": {
                "脚本名称": "auto_脚本python新"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_script_delete(self):
        u"""删除脚本java"""
        action = {
            "操作": "DeleteScript",
            "参数": {
                "脚本名称": "auto_脚本java"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_script_delete(self):
        u"""删除脚本jar"""
        action = {
            "操作": "DeleteScript",
            "参数": {
                "脚本名称": "auto_脚本jar"
            }
        }
        msg = "删除成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_script_clear(self):
        u"""脚本管理，数据清理，清除python脚本"""
        action = {
            "操作": "ScriptDataClear",
            "参数": {
                "脚本名称": "auto_脚本python"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_28_script_add(self):
        u"""添加脚本，类型python"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本python",
                "脚本类型": "python",
                "数据类型": "私有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_script_upload_file(self):
        u"""不带参python脚本上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "1",
                "脚本文件名": "test_no_param.py"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_script_submit_approval(self):
        u"""python脚本版本1提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "1"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_script_save_new(self):
        u"""python脚本保存新版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "1"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_script_delete_file(self):
        u"""带参python脚本删除版本2的脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2",
                "脚本文件名": "test_no_param.py",
                "右键": "删除脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_script_upload_file(self):
        u"""带参python脚本上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2",
                "脚本文件名": "fa.py"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_script_upload_file(self):
        u"""带参python脚本上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2",
                "脚本文件名": "fb.py"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_script_set_main(self):
        u"""带参python脚本设置主脚本"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2",
                "脚本文件名": "fb.py",
                "右键": "设置为主脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_36_script_add_param(self):
        u"""带参python脚本添加参数"""
        action = {
            "操作": "AddScriptParams",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2",
                "脚本参数": ["param1", "param2"]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_37_script_submit_approval(self):
        u"""python脚本版本2提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "2"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_38_script_save_new(self):
        u"""python脚本保存新版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "1"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_39_script_delete_file(self):
        u"""带参python脚本删除版本3的脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3",
                "脚本文件名": "test_no_param.py",
                "右键": "删除脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_40_script_upload_file(self):
        u"""带参python脚本上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3",
                "脚本文件名": "readfile.py"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_script_set_main(self):
        u"""带参python脚本设置主脚本"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3",
                "脚本文件名": "readfile.py",
                "右键": "设置为主脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_42_script_add_param(self):
        u"""带参python脚本添加参数"""
        action = {
            "操作": "AddScriptParams",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3",
                "脚本参数": ["param1", "param2", "param3"]
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_43_script_save(self):
        u"""python脚本保存当前版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_44_script_submit_approval(self):
        u"""python脚本版本3提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本python",
                "版本号": "3"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_script_clear(self):
        u"""脚本管理，数据清理，清除java脚本"""
        action = {
            "操作": "ScriptDataClear",
            "参数": {
                "脚本名称": "auto_脚本java"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_46_script_add(self):
        u"""添加脚本，类型java"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本java",
                "脚本类型": "java",
                "数据类型": "私有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_47_script_upload_file(self):
        u"""java脚本上传脚本文件，读取personal目录下的文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1",
                "脚本文件名": "readfile1.java"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_48_script_submit_approval(self):
        u"""java脚本版本1提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_49_script_save_new(self):
        u"""java脚本保存新版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_script_delete_file(self):
        u"""java脚本删除版本2的脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "2",
                "脚本文件名": "readfile1.java",
                "右键": "删除脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_51_script_upload_file(self):
        u"""java脚本上传脚本文件，读取system目录下的文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "2",
                "脚本文件名": "readfile2.java"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_52_script_submit_approval(self):
        u"""java脚本版本2提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "2"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_53_script_save_new(self):
        u"""java脚本保存新版本"""
        action = {
            "操作": "SaveNewScriptVersion",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "1"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_54_script_delete_file(self):
        u"""java脚本删除版本3的脚本文件"""
        action = {
            "操作": "ScriptFileRClick",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "3",
                "脚本文件名": "readfile1.java",
                "右键": "删除脚本"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_55_script_upload_file(self):
        u"""java脚本上传脚本文件，读取绝对路径下的文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "3",
                "脚本文件名": "readfilejd.java"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_56_script_submit_approval(self):
        u"""java脚本版本3提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本java",
                "版本号": "3"
            }
        }
        msg = "提交成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_57_script_clear(self):
        u"""脚本管理，数据清理，清除jar脚本"""
        action = {
            "操作": "ScriptDataClear",
            "参数": {
                "脚本名称": "auto_脚本jar"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_58_script_add(self):
        u"""添加脚本，类型jar"""
        action = {
            "操作": "AddScript",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "脚本类型": "jar",
                "数据类型": "私有"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_59_script_upload_file(self):
        u"""jar脚本上传脚本文件"""
        action = {
            "操作": "UploadScriptFile",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "版本号": "1",
                "脚本文件名": "CompareDataUtil.jar"
            }
        }
        msg = "文件上传成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_60_script_submit_approval(self):
        u"""jar脚本版本1提交审批"""
        action = {
            "操作": "SubmitScriptApproval",
            "参数": {
                "脚本名称": "auto_脚本jar",
                "版本号": "1"
            }
        }
        msg = "提交成功"
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
