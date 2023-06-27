# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 14:57

import os
import unittest
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def createSuite():
    # 设置测试用例目录
    case_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/testcase/" + gbl.service.get("application")
    if not os.path.exists(case_dir):
        os.makedirs(case_dir)

    suite = unittest.TestSuite()
    # discover方法更正测试用例文件，将获取的测试用例组件组装到测试套件，discover过滤.py的用例文件
    # 想多级匹配，需要创建成package，将测试用例放在package下面，能递归查询用例文件
    for dir1 in gbl.case.get("path"):
        cur_case_path = case_dir + dir1
        top_level_dir = cur_case_path
        discover = unittest.defaultTestLoader.discover(cur_case_path, pattern='test*.py', top_level_dir=top_level_dir)
        log.debug(discover)

        # 通过循环遍历将过滤后的用例加入测试套件
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTests(test_case)
    log.info("装载测试用例集成功.")
    return suite


if __name__ == "__main__":
    createSuite()
