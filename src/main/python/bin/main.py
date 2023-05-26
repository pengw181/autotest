# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-06 14:57

import os
# import time
from src.main.python.lib.globals import gbl
from src.main.python.core.gooflow.suite import createSuite
from src.main.python.core.gooflow.initiation import initiation_work
from src.main.python.conf.config import global_config


def main():
    global_config()
    initiation_work()
    suites = createSuite()
    report_path = gbl.service.get("ProjectPath") + '/src/main/python/reports/output/'
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # # 设置报告名称格式
    # # report_file = report_path + "/HTMLReport_" + now + ".html"
    report_file = report_path + "/HTMLReport" + ".html"
    fp = open(report_file, 'wb')
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    from src.main.python.lib import HTMLTestRunner
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试报告", description="用例执行结果")
    runner.run(suites)
    fp.close()


if __name__ == "__main__":
    main()
