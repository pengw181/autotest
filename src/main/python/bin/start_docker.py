# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:22

import sys
from src.main.python.core.gooflow.case import loadCase
from src.main.python.lib.globals import gbl


def main(begin_file_line, begin_case_line):

    # runAllTest为true时，runTestLevel不生效；runAllTest为false时，只执行runTestLevel指定级别的用例
    gbl.service.set("RunAllTest", True)
    # 用例执行失败，是否继续执行下一条
    gbl.service.set("ContinueRunWhenError", False)
    # 设置测试用例覆盖级别
    gbl.service.set("RunTestLevel", ["高", "中", "低"])
    # 是否输出报告
    gbl.service.set("BuiltReport", False)

    # 开始运行，第一个数字为读取第几个测试用例文件（从1开始），第二个数字为读取测试用例的第几行（从1开始）
    loadCase(begin_file_line, begin_case_line)


if __name__ == "__main__":
    begin_file = sys.argv[1]
    begin_case = sys.argv[2]
    print("接收参数: {}, {}，开始启动测试".format(begin_file, begin_case))
    main(begin_file, begin_case)

