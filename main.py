# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 14:57

from service.gooflow.report import getReportName
from service.gooflow.suite import createSuite
from service.gooflow import HTMLTestRunner


def main():
    suites = createSuite()

    report_file = getReportName()
    fp = open(report_file, 'wb')
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试报告", description="用例执行结果")
    runner.run(suites)
    fp.close()


if __name__ == "__main__":
    main()
