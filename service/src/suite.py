import os
import unittest
from config.loads import properties
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def createSuite():
    # 设置测试用例目录
    test_case_path = properties.get("testCasePath")
    base = properties.get("projectBasePath") + properties.get("projectName")
    case_dir = base + test_case_path + get_global_var("Application")
    if not os.path.exists(case_dir):
        os.makedirs(case_dir)

    suite = unittest.TestSuite()
    # discover方法更正测试用例文件，将获取的测试用例组件组装到测试套件，discover过滤.py的用例文件
    # 想多级匹配，需要创建成package，将测试用例放在package下面，能递归查询用例文件
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
    log.debug(discover)

    # 通过循环遍历将过滤后的用例加入测试套件
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTests(test_case)
    log.info("装载测试用例集成功.")
    print(suite)
    return suite


if __name__ == "__main__":
    createSuite()
