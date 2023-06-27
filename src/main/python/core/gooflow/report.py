# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/12 下午5:41

import os
import xlrd
import xlwt
import shutil
from xlutils.copy import copy
from datetime import datetime


class ReportRunner:

    def __init__(self):

        timestamp = datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")
        self.path = os.path.dirname(
            os.path.dirname(os.path.dirname(__file__))) + "/reports/output/AutoTestReport_" + timestamp + ".xls"
        template_file_path = os.path.dirname(
            os.path.dirname(os.path.dirname(__file__))) + "/reports/template/AutoTestReport.xls"

        # 打开excel，formatting_info=True保留Excel当前格式
        shutil.copy(template_file_path, self.path)
        rbook = xlrd.open_workbook(self.path, formatting_info=True)
        self.wbook = copy(rbook)
        self.wsheets = self.wbook.get_sheet(0)

    def generateReportFile(self, report):
        """
        # 生成报表
        :param report: 二维数组
        """
        # 定义字体类型1. 字体：红色
        font0 = xlwt.Font()
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0

        # 定义字体类型2. 字体：蓝色
        font1 = xlwt.Font()
        font1.colour_index = 4
        font1.bold = True

        style1 = xlwt.XFStyle()
        style1.font = font1

        # 定义字体类型3. 字体：绿色
        font2 = xlwt.Font()
        font2.colour_index = 3
        font2.bold = True

        style2 = xlwt.XFStyle()
        style2.font = font2

        # 定义字体类型4. 字体：黄色
        font3 = xlwt.Font()
        font3.colour_index = 52
        font3.bold = True

        style3 = xlwt.XFStyle()
        style3.font = font3

        # 定义字体类型5. 字体：灰色
        font4 = xlwt.Font()
        font4.colour_index = 23
        font4.bold = True

        style4 = xlwt.XFStyle()
        style4.font = font4

        row_num = 1
        for info in report:
            # 分解报告内容
            if not isinstance(info, dict):
                raise ValueError("expect type dict, but get type {0}".format(type(info)))
            for file_name, one_file_result in info.items():
                if not isinstance(one_file_result, list):
                    raise ValueError("expect type list, but get type {0}".format(type(one_file_result)))
                for one_case in one_file_result:
                    test_file = file_name
                    test_name = one_case[0]
                    test_result = one_case[1]
                    exception_from = one_case[2]
                    exception_info = one_case[3]
                    picture = one_case[4]
                    self.wsheets.write(row_num, 0, test_file)
                    self.wsheets.write(row_num, 1, test_name)
                    if test_result == "PASS":
                        # 通过
                        style = style1
                    elif test_result == "FAIL":
                        # 不通过
                        style = style0
                    elif test_result == "ERROR":
                        # 异常
                        style = style3
                    else:
                        # 跳过
                        style = style4
                    self.wsheets.write(row_num, 2, test_result, style)
                    self.wsheets.write(row_num, 3, exception_from)
                    self.wsheets.write(row_num, 4, exception_info)
                    if picture:
                        self.wsheets.write(row_num, 5, xlwt.Formula('HYPERLINK("{0}")'.format(picture)), style2)
                    row_num += 1
                    self.wbook.save(self.path)
        return self.path


if __name__ == "__main__":
    show_info = [{
        '邮件节点.xls': [
            ['画流程图,添加一个邮件节点', 'PASS', '', '', ''],
            ['配置邮件节点,邮件发送,标题引用变量', 'ERROR', '', 'tn_node_email_send表数据不匹配，mail_content', '']
        ]
    }]
    report_run = ReportRunner()
    report_file = report_run.generateReportFile(show_info)
    print(report_file)
