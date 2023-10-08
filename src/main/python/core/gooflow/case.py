# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午4:12

import os
import xlrd
import json
import traceback
from datetime import datetime
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.precondition import preconditions
from src.main.python.core.gooflow.operation import basic_run
from src.main.python.core.gooflow.compares import compare_data
from src.main.python.conf.config import global_config
from src.main.python.core.gooflow.initiation import Initiation, initiation_work


class CaseWorker:

    @staticmethod
    def init():
        """
        业务参数初始化
        """
        Initiation.clear_var()

    @staticmethod
    def pre(pres):
        """
        预置条件
        @param: pres: 文本，支持多行，以换行分割
        """
        if pres is None or pres == "":
            return True
        # noinspection PyBroadException
        try:
            result = preconditions(action=pres)
        except Exception:
            result = False
            traceback.print_exc()
        return result

    @staticmethod
    def action(step):
        """
        用户操作，一次一个步骤
        """
        # noinspection PyBroadException
        try:
            result = basic_run(step=step)
        except Exception:
            result = False
            traceback.print_exc()
        return result

    @staticmethod
    def check(items):
        """
        结果匹配
        """
        if items is None or items == "":
            return True
        # noinspection PyBroadException
        try:
            result = compare_data(items)
        except Exception:
            result = False
            traceback.print_exc()
        return result


class CaseEngine:
    """构造测试用例py文件时用到"""
    def __init__(self, worker=None):
        global_config()
        if worker:
            initiation_work()
        self.worker = worker

    @staticmethod
    def load(case_file):
        application = gbl.service.get("application")
        case_file_path = gbl.service.get("TestCasePath") + application + case_file
        if not os.path.exists(case_file_path):
            raise FileNotFoundError("无法找到测试用例文件, {}".format(case_file_path))
        workbook = xlrd.open_workbook(case_file_path, formatting_info=True)
        sheets = workbook.sheet_by_index(0)
        sheets_content = []
        for row_num in range(sheets.nrows):
            case_name = sheets.row_values(row_num)[0]
            case_action = sheets.row_values(row_num)[3]
            if case_name is None or len(case_name) == 0:
                break
            if case_name.startswith("UNTEST") and len(case_action) == 0:
                continue
            sheets_content.append(sheets.row_values(row_num))
        gbl.service.set("CaseSheets", sheets_content)

    @staticmethod
    def construct(case_order):
        sheet_case = gbl.service.get("CaseSheets")
        case_rows = sheet_case[case_order]
        # 用例名称
        case_name = case_rows[0]
        # 预置条件
        case_pres = case_rows[2]
        # 操作步骤
        case_action = case_rows[3]
        try:
            case_action = json.loads(str(case_action))
        except json.decoder.JSONDecodeError:
            log.info(case_action)
            traceback.print_exc()
            case_action = None
        # 预期结果
        case_checks = case_rows[4]
        gbl.service.set("CaseConstruct", [case_name, case_pres, case_action, case_checks])

    def execute(self):
        if not self.worker:
            raise KeyError("参数不全，实例缺少【worker】参数")

        case_name = gbl.service.get("CaseConstruct")[0]
        pres = gbl.service.get("CaseConstruct")[1]
        action = gbl.service.get("CaseConstruct")[2]
        checks = gbl.service.get("CaseConstruct")[3]
        log.info(">>>>> {} <<<<<".format(case_name))

        if case_name.startswith("UNTEST"):
            log.info("本用例不执行，跳过")
            gbl.temp.set("SkipCase", True)
            assert True
            return

        gbl.temp.set("StartTime", datetime.now().strftime('%Y%m%d%H%M%S'))
        result = self.worker.pre(pres)
        assert result
        result = self.worker.action(action)
        assert result
        log.info(gbl.temp.get("ResultMsg"))
        result = self.worker.check(checks)
        assert result
