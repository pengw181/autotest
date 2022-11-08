# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/30 下午10:36

import unittest
from service.src.screenShot import screenShot
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from service.gooflow.case import CaseWorker


class File(unittest.TestCase):

    log.info("装载文件目录管理测试用例")
    worker = CaseWorker()

    def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理
        self.browser = get_global_var("browser")
        self.worker.init()

    def test_1_file_dir_clear(self):
        u"""个人目录清理"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_2_file_dir_clear(self):
        u"""系统目录清理"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_3_file_dir_make(self):
        u"""个人目录创建一级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_一级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_4_file_dir_make(self):
        u"""同级下创建同名目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_一级目录"
            }
        }
        msg = "目录已经存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_5_file_dir_make(self):
        u"""个人目录创建二级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "目录名": "auto_二级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_6_file_dir_make(self):
        u"""个人目录创建三级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_二级目录",
                "目录名": "auto_三级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_7_file_dir_make(self):
        u"""个人目录一次创建三级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "目录名": "auto_a级目录/auto_b级目录/auto_c级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_8_file_dir_make(self):
        u"""不同层级下创建同名目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_二级目录",
                "目录名": "auto_b级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_9_file_dir_update(self):
        u"""修改一级目录名"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "目录名": "auto_一级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_10_file_dir_update(self):
        u"""修改二级目录名，同级下目录名已存在"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_二级目录",
                "目录名": "auto_a级目录"
            }
        }
        msg = "目录已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_11_file_dir_update(self):
        u"""修改二级目录名，同级下目录名不存在"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_二级目录",
                "目录名": "auto_二级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_12_file_dir_update(self):
        u"""修改三级目录名"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_三级目录",
                "目录名": "auto_三级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_13_file_upload(self):
        u"""在一级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_14_file_upload(self):
        u"""在一级目录下上传文件，该目录下文件已存在"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_15_file_upload(self):
        u"""在二级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_二级目录新",
                "文件名": "disturb_file_test.csv"
            }
        }
        checks = """
        CheckFile|disturb_file_test.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_16_file_upload(self):
        u"""在三级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_三级目录新",
                "文件名": "factor.xlsx"
            }
        }
        checks = """
        CheckFile|factor.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_17_file_download(self):
        u"""下载文件"""
        action = {
            "操作": "DownloadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckDownloadFile|request|txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_18_file_delete(self):
        u"""删除文件"""
        action = {
            "操作": "DeleteFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        msg = "删除文件成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_19_file_upload(self):
        u"""在一级目录下上传xlsx文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "factor.xlsx"
            }
        }
        checks = """
        CheckFile|factor.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_20_file_upload(self):
        u"""在一级目录下上传csv文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": "disturb_file_test.csv"
            }
        }
        checks = """
        CheckFile|disturb_file_test.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_21_file_download_batch(self):
        u"""批量下载文件"""
        action = {
            "操作": "DownloadFileBatch",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": ["factor.xlsx", "disturb_file_test.csv"]
            }
        }
        checks = """
        CheckDownloadFile|批量下载文件|zip
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_22_file_delete_batch(self):
        u"""批量删除文件"""
        action = {
            "操作": "DeleteFileBatch",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新",
                "文件名": ["factor.xlsx", "disturb_file_test.csv"]
            }
        }
        msg = "批量删除文件成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_23_file_dir_delete(self):
        u"""删除目录，目录下无子目录"""
        action = {
            "操作": "DeleteDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_c级目录"
            }
        }
        msg = "删除目录成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_24_file_dir_delete(self):
        u"""删除目录，目录下有子目录"""
        action = {
            "操作": "DeleteDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录新"
            }
        }
        msg = "删除目录成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_25_file_dir_make(self):
        u"""系统目录创建一级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "system",
                "目录名": "auto_一级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_26_file_dir_make(self):
        u"""同级下创建同名目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "system",
                "目录名": "auto_一级目录"
            }
        }
        msg = "目录已经存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_27_file_dir_make(self):
        u"""系统目录创建二级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录",
                "目录名": "auto_二级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_28_file_dir_make(self):
        u"""系统目录创建三级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_二级目录",
                "目录名": "auto_三级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_29_file_dir_make(self):
        u"""系统目录一次创建三级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录",
                "目录名": "auto_a级目录/auto_b级目录/auto_c级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_30_file_dir_make(self):
        u"""不同层级下创建同名目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_二级目录",
                "目录名": "auto_b级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_31_file_dir_update(self):
        u"""修改一级目录名"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录",
                "目录名": "auto_一级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_32_file_dir_update(self):
        u"""修改二级目录名，同级下目录名已存在"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_二级目录",
                "目录名": "auto_a级目录"
            }
        }
        msg = "目录已存在"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_33_file_dir_update(self):
        u"""修改二级目录名，同级下目录名不存在"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_二级目录",
                "目录名": "auto_二级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_34_file_dir_update(self):
        u"""修改三级目录名"""
        action = {
            "操作": "UpdateDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_三级目录",
                "目录名": "auto_三级目录新"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_35_file_upload(self):
        u"""在一级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_36_file_upload(self):
        u"""在一级目录下上传文件，该目录下文件已存在"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_37_file_upload(self):
        u"""在二级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_二级目录新",
                "文件名": "disturb_file_test.csv"
            }
        }
        checks = """
        CheckFile|disturb_file_test.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_38_file_upload(self):
        u"""在三级目录下上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_三级目录新",
                "文件名": "factor.xlsx"
            }
        }
        checks = """
        CheckFile|factor.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_39_file_download(self):
        u"""下载文件"""
        action = {
            "操作": "DownloadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckDownloadFile|request|txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_40_file_delete(self):
        u"""删除文件"""
        action = {
            "操作": "DeleteFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "request.txt"
            }
        }
        msg = "删除文件成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_41_file_upload(self):
        u"""在一级目录下上传xlsx文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "factor.xlsx"
            }
        }
        checks = """
        CheckFile|factor.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_42_file_upload(self):
        u"""在一级目录下上传csv文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": "disturb_file_test.csv"
            }
        }
        checks = """
        CheckFile|disturb_file_test.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_43_file_download_batch(self):
        u"""批量下载文件"""
        action = {
            "操作": "DownloadFileBatch",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": ["factor.xlsx", "disturb_file_test.csv"]
            }
        }
        checks = """
        CheckDownloadFile|批量下载文件|zip
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_44_file_delete_batch(self):
        u"""批量删除文件"""
        action = {
            "操作": "DeleteFileBatch",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新",
                "文件名": ["factor.xlsx", "disturb_file_test.csv"]
            }
        }
        msg = "批量删除文件成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_45_file_dir_delete(self):
        u"""删除目录，目录下无子目录"""
        action = {
            "操作": "DeleteDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_c级目录"
            }
        }
        msg = "删除目录成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_46_file_dir_delete(self):
        u"""删除目录，目录下有子目录"""
        action = {
            "操作": "DeleteDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_一级目录新"
            }
        }
        msg = "删除目录成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_47_file_dir_clear(self):
        u"""个人目录清理"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_48_file_dir_clear(self):
        u"""系统目录清理"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_系统一级目录"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_49_file_dir_make(self):
        u"""个人目录创建一级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_一级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_50_file_dir_make(self):
        u"""个人目录创建二级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "目录名": "auto_二级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_51_file_dir_make(self):
        u"""系统目录创建一级目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "system",
                "目标目录": "system",
                "目录名": "auto_系统一级目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_52_file_upload(self):
        u"""个人目录上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_53_file_upload(self):
        u"""个人目录上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_一级目录",
                "文件名": "data.xlsx"
            }
        }
        checks = """
        CheckFile|data.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_54_file_upload(self):
        u"""系统目录上传文件"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "system",
                "目标目录": "auto_系统一级目录",
                "文件名": "request.txt"
            }
        }
        checks = """
        CheckFile|request.txt
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_55_file_dir_clear(self):
        u"""删除个人目录，auto_ocr目录"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_56_file_dir_make(self):
        u"""个人目录创建：auto_ocr目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_ocr目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_57_file_upload(self):
        u"""auto_ocr目录上传文件012.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "012.jpg"
            }
        }
        checks = """
        CheckFile|012.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_58_file_upload(self):
        u"""auto_ocr目录上传文件021.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "021.jpg"
            }
        }
        checks = """
        CheckFile|021.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_59_file_upload(self):
        u"""auto_ocr目录上传文件032.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "032.jpg"
            }
        }
        checks = """
        CheckFile|032.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_60_file_upload(self):
        u"""auto_ocr目录上传文件034.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "034.jpg"
            }
        }
        checks = """
        CheckFile|034.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_61_file_upload(self):
        u"""auto_ocr目录上传文件034_compress.jPG"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "034_compress.jPG"
            }
        }
        checks = """
        CheckFile|034_compress.jPG
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_62_file_upload(self):
        u"""auto_ocr目录上传文件4301.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "4301.jpg"
            }
        }
        checks = """
        CheckFile|4301.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_63_file_upload(self):
        u"""auto_ocr目录上传文件4302.png"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "4302.png"
            }
        }
        checks = """
        CheckFile|4302.png
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_64_file_upload(self):
        u"""auto_ocr目录上传文件4303.jpeg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "4303.jpeg"
            }
        }
        checks = """
        CheckFile|4303.jpeg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_65_file_upload(self):
        u"""auto_ocr目录上传文件034-3.4M.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "034-3.4M.jpg"
            }
        }
        checks = """
        CheckFile|034-3.4M.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_66_file_upload(self):
        u"""auto_ocr目录上传文件034-70dpi.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "034-70dpi.jpg"
            }
        }
        checks = """
        CheckFile|034-70dpi.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_67_file_upload(self):
        u"""auto_ocr目录上传文件034-500px.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "034-500px.jpg"
            }
        }
        checks = """
        CheckFile|034-500px.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_68_file_upload(self):
        u"""auto_ocr目录上传文件047_7000.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "文件类别": "ocr",
                "文件名": "047_7000.jpg"
            }
        }
        checks = """
        CheckFile|047_7000.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_69_file_dir_make(self):
        u"""auto_ocr目录创建二级目录：auto_普通发票"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "目录名": "auto_普通发票"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_70_file_dir_make(self):
        u"""auto_ocr目录创建二级目录：auto_专用发票"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_ocr目录",
                "目录名": "auto_专用发票"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_71_file_upload(self):
        u"""auto_普通发票上传文件201.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_普通发票",
                "文件类别": "ocr",
                "文件名": "201.jpg"
            }
        }
        checks = """
        CheckFile|201.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_72_file_upload(self):
        u"""auto_普通发票上传文件222.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_普通发票",
                "文件类别": "ocr",
                "文件名": "222.jpg"
            }
        }
        checks = """
        CheckFile|222.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_73_file_upload(self):
        u"""auto_普通发票上传文件225.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_普通发票",
                "文件类别": "ocr",
                "文件名": "225.jpg"
            }
        }
        checks = """
        CheckFile|225.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_74_file_upload(self):
        u"""auto_普通发票上传文件226.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_普通发票",
                "文件类别": "ocr",
                "文件名": "226.jpg"
            }
        }
        checks = """
        CheckFile|226.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_75_file_upload(self):
        u"""auto_普通发票上传文件235.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_普通发票",
                "文件类别": "ocr",
                "文件名": "235.jpg"
            }
        }
        checks = """
        CheckFile|235.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_76_file_upload(self):
        u"""auto_专用发票上传文件105.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_专用发票",
                "文件类别": "ocr",
                "文件名": "105.jpg"
            }
        }
        checks = """
        CheckFile|105.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_77_file_upload(self):
        u"""auto_专用发票上传文件109.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_专用发票",
                "文件类别": "ocr",
                "文件名": "109.jpg"
            }
        }
        checks = """
        CheckFile|109.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_78_file_upload(self):
        u"""auto_专用发票上传文件110.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_专用发票",
                "文件类别": "ocr",
                "文件名": "110.jpg"
            }
        }
        checks = """
        CheckFile|110.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_79_file_upload(self):
        u"""auto_专用发票上传文件116.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_专用发票",
                "文件类别": "ocr",
                "文件名": "116.jpg"
            }
        }
        checks = """
        CheckFile|116.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_80_file_upload(self):
        u"""auto_专用发票上传文件122.jpg"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_专用发票",
                "文件类别": "ocr",
                "文件名": "122.jpg"
            }
        }
        checks = """
        CheckFile|122.jpg
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_81_file_dir_clear(self):
        u"""删除个人目录，auto_AI"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_82_file_dir_make(self):
        u"""个人目录创建：auto_AI"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_AI"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_83_file_upload(self):
        u"""auto_AI上传文件factorLGBM_predict.csv"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "factorLGBM_predict.csv"
            }
        }
        checks = """
        CheckFile|factorLGBM_predict.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_84_file_upload(self):
        u"""auto_AI上传文件factorXGB_predict.csv"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "factorXGB_predict.csv"
            }
        }
        checks = """
        CheckFile|factorXGB_predict.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_85_file_upload(self):
        u"""auto_AI上传文件factorLGBM_predict.csv"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "factorLGBM_predict.csv"
            }
        }
        checks = """
        CheckFile|factorLGBM_predict.csv
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_86_file_upload(self):
        u"""auto_AI上传文件single_predict.xlsx"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "single_predict.xlsx"
            }
        }
        checks = """
        CheckFile|single_predict.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_87_file_upload(self):
        u"""auto_AI上传文件factor_predict.xlsx"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "factor_predict.xlsx"
            }
        }
        checks = """
        CheckFile|factor_predict.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_88_file_upload(self):
        u"""auto_AI上传文件classical_predict.xlsx"""
        action = {
            "操作": "UploadFile",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_AI",
                "文件类别": "predict",
                "文件名": "classical_predict.xlsx"
            }
        }
        checks = """
        CheckFile|classical_predict.xlsx
        """
        result = self.worker.action(action)
        assert result
        result = self.worker.check(checks)
        assert result

    def test_89_file_dir_clear(self):
        u"""删除个人目录，auto_全流程"""
        action = {
            "操作": "DirDataClear",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_全流程"
            }
        }
        result = self.worker.action(action)
        assert result

    def test_90_file_dir_make(self):
        u"""个人目录创建：auto_全流程"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "personal",
                "目录名": "auto_全流程"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_91_file_dir_make(self):
        u"""个人目录创建：auto_临时目录"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_全流程",
                "目录名": "auto_临时目录"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_92_file_dir_make(self):
        u"""添加目录，目录名包含./"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_临时目录",
                "目录名": "./back"
            }
        }
        msg = "操作成功"
        result = self.worker.action(action)
        assert result
        log.info(get_global_var("ResultMsg"))
        assert get_global_var("ResultMsg").startswith(msg)

    def test_93_file_dir_make(self):
        u"""添加目录，目录名包含../"""
        action = {
            "操作": "MkDir",
            "参数": {
                "目录分类": "personal",
                "目标目录": "auto_临时目录",
                "目录名": "../back"
            }
        }
        msg = "请输入正确的目录名称"
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
