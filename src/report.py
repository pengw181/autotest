# coding=utf-8

import os
import time
from config.loads import properties


def getReportName():

    # 设置报告文件保存路径
    path = properties.get("reportPath")
    report_path = properties.get("projectBasePath") + properties.get("projectName") + path
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    # 获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 设置报告名称格式
    # report_file = report_path + "/HTMLReport_" + now + ".html"
    report_file = report_path + "/HTMLReport" + ".html"
    return report_file


if __name__ == "__main__":
    getReportName()

