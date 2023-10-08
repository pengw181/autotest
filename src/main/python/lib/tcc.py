# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/7/30 下午8:47

import os
import time
import json
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseEngine


set_name = {
    # AlarmPlatform
    "/测试准备/数据清理.xls": {
        "cls_name": "DataClearWorker",
        "dir_name": "/dataPrepare",
        "file_name": "data_clear"
    },
    "/连接配置/关系型数据库配置.xls": {
        "cls_name": "DatabaseConfig",
        "dir_name": "/connection",
        "file_name": "database"
    },
    "/连接配置/表归属配置.xls": {
        "cls_name": "TableBelongConfig",
        "dir_name": "/connection",
        "file_name": "table_belong"
    },
    "/连接配置/FTP配置.xls": {
        "cls_name": "FTPConfig",
        "dir_name": "/connection",
        "file_name": "ftp"
    },
    "/告警配置/告警元数据.xls": {
        "cls_name": "MetaDataConfig",
        "dir_name": "/config",
        "file_name": "metadata"
    },
    "/告警配置/字典配置.xls": {
        "cls_name": "DictionaryConfig",
        "dir_name": "/config",
        "file_name": "dictionary"
    },
    "/告警配置/告警计划.xls": {
        "cls_name": "AlarmPlanConfig",
        "dir_name": "/config",
        "file_name": "alarm_plan"
    },
    "/告警配置/告警规则.xls": {
        "cls_name": "AlarmRuleConfig",
        "dir_name": "/config",
        "file_name": "alarm_rule"
    },
    "/告警配置/消息模版.xls": {
        "cls_name": "MessageTemplConfig",
        "dir_name": "/config",
        "file_name": "message_templ"
    },
    "/推送计划/推送计划.xls": {
        "cls_name": "SendPlanConfig",
        "dir_name": "/send",
        "file_name": "send_plan"
    },
    "/告警服务/执行告警.xls": {
        "cls_name": "AlarmServerConfig",
        "dir_name": "/alarmServer",
        "file_name": "alarm_server"
    },
    # VisualModeler
    "/流程配置/全流程功能.xls": {
        "cls_name": "WorkFlowAllNode",
        "dir_name": "/workflow",
        "file_name": "workflow_all"
    },
    "/流程引擎/流程数据库节点大数据效率.xls": {
        "cls_name": "WorkFlowSqlNodeEfficiency",
        "dir_name": "/workflow",
        "file_name": "workflow_sql_efficiency"
    }
}


class AutoCreateCaseCls:

    def __init__(self, case_path, point_case=None):
        """
        :param case_path: base_path/application/
        :param point_case: 指定某个用例文件(相对路径)，为空则将所有用例文件转成测试用例class
        """
        if not os.path.exists(case_path):
            raise IsADirectoryError("测试用例路径错误, {}".format(case_path))
        if not case_path.endswith("/"):
            case_path += "/"
        self.relative_case_filepath = []
        if not point_case:
            dirs = os.listdir(case_path)
            for _dir in dirs:
                case_file_path = case_path + _dir
                if os.path.isdir(case_file_path):
                    files = os.listdir(case_file_path)
                    if len(files) == 0:
                        continue
                    for _file_name in files:
                        if not _file_name.endswith(".xls"):
                            continue
                        _relative_case_file = "/" + _dir + "/" + _file_name
                        self.relative_case_filepath.append(_relative_case_file)
        else:
            self.relative_case_filepath = [point_case]

        # 用例最终输出
        self.case_order = 1
        self.whole_case_content = ""
        log.info("启动自动生成测试用例程序...")

    def _add(self, line, add_tab=False, tab_times=0):
        if add_tab:
            for i in range(tab_times):
                self.whole_case_content += "\t"
        self.whole_case_content += line
        if line != "\n":
            self.whole_case_content += "\n"

    def _create_import(self):
        now = time.strftime('%y/%m/%d %p%I:%M')
        self._add("# -*- encoding: utf-8 -*-")
        self._add("# @Author: peng wei")
        self._add("# @Time: {}".format(now))
        self._add("\n")
        self._add("import unittest")
        self._add("from datetime import datetime")
        self._add("from src.main.python.lib.globals import gbl")
        self._add("from src.main.python.lib.logger import log")
        self._add("from src.main.python.core.gooflow.case import CaseWorker")
        self._add("from src.main.python.core.gooflow.case import CaseEngine")
        self._add("from src.main.python.lib.screenShot import saveScreenShot")
        self._add("\n")
        self._add("\n")

    def _create_case_cls_name(self, relative_path):
        """
        自动生成测试类名称
        :return:
        """
        global set_name
        cls_name = set_name.get(relative_path).get("cls_name")
        self._add("class {}(unittest.TestCase):".format(cls_name))
        self._add("\n")

    def _create_init(self, relative_path):
        temp = relative_path[:relative_path.find(".")]
        temp = temp.split("/")[-1]
        self._add("log.info(\"装载{}测试用例\")".format(temp), True, 1)
        self._add("worker = CaseWorker()", True, 1)
        self._add("case = CaseEngine(worker=worker)", True, 1)
        self._add("case.load(case_file=\"{}\")".format(relative_path), True, 1)
        self._add("\n")

    def _create_setup(self):
        self._add("def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理", True, 1)
        self._add("self.browser = gbl.service.get(\"browser\")", True, 2)
        self._add("self.worker.init()", True, 2)
        self._add("\n")

    def _create_each_case(self, relative_path, case_order, case_prefix="test"):
        # noinspection PyBroadException
        try:
            case = CaseEngine()
            case.load(case_file=relative_path)

            case.construct(case_order=case_order)
            case_name = gbl.service.get("CaseConstruct")[0]
            pres = gbl.service.get("CaseConstruct")[1]
            action = gbl.service.get("CaseConstruct")[2]
            checks = gbl.service.get("CaseConstruct")[3]

            if len(case_name.strip()) == 0:
                return False
            if case_name.startswith("UNTEST"):
                self._add("@unittest.skip", True, 1)

            short_case_name = action.get("操作")
            if not short_case_name:
                raise KeyError("生成测试用例函数失败，action数据错误")
            action = json.dumps(action, indent=4, ensure_ascii=False)

            func_name = "{}_{}_{}".format(case_prefix, self.case_order, short_case_name)
            self._add("def {}(self):".format(func_name), True, 1)

            self._add("u\"\"\"{}\"\"\"".format(case_name.replace("\"", "")), True, 2)

            if len(pres.strip()) > 0:
                self._add("pres = \"\"\"", True, 2)
                pres_lines = pres.split("\n")
                for pres_line in pres_lines:
                    self._add("{}".format(pres_line), True, 2)
                self._add("\"\"\"", True, 2)

            action_lines = action.split("\n")
            for action_line in action_lines:
                action_line = action_line.replace("    ", "\t")
                if action_line == action_lines[0]:
                    self._add("action = {}".format(action_line), True, 2)
                else:
                    self._add("{}".format(action_line), True, 2)

            if len(checks.strip()) > 0:
                self._add("checks = \"\"\"", True, 2)
                checks_lines = checks.split("\n")
                for checks_line in checks_lines:
                    self._add("{}".format(checks_line), True, 2)
                self._add("\"\"\"", True, 2)
            self._add("log.info('>>>>> {} <<<<<')".format(case_name), True, 2)
            self._add("gbl.temp.set(\"StartTime\", datetime.now().strftime('%Y%m%d%H%M%S'))", True, 2)

            if len(pres.strip()) > 0:
                self._add("result = self.worker.pre(pres)", True, 2)
                self._add("assert result", True, 2)
            self._add("result = self.worker.action(action)", True, 2)
            self._add("assert result", True, 2)
            if len(checks.strip()) > 0:
                self._add("log.info(gbl.temp.get(\"ResultMsg\"))", True, 2)
                self._add("result = self.worker.check(checks)", True, 2)
                self._add("assert result", True, 2)
            self._add("\n")
            self.case_order += 1
            return True
        except Exception:
            return False

    def _create_teardown(self):
        self._add("def tearDown(self):  # 最后执行的函数", True, 1)
        self._add("self.browser = gbl.service.get(\"browser\")", True, 2)
        self._add("saveScreenShot()", True, 2)
        self._add("self.browser.refresh()", True, 2)
        self._add("\n")
        self._add("\n")

    def _creat_footer(self):
        self._add("if __name__ == '__main__':")
        self._add("unittest.main()", True, 1)

    def auto_create(self, output_path, file_prefix="test"):
        if len(self.relative_case_filepath) == 0:
            log.info("没有测试文件需要生成测试用例")
            return

        for case_path in self.relative_case_filepath:
            self.case_order = 1
            self.whole_case_content = ""

            self._create_import()
            self._create_case_cls_name(relative_path=case_path)
            self._create_init(relative_path=case_path)
            self._create_setup()
            while True:
                result = self._create_each_case(relative_path=case_path, case_order=self.case_order)
                if not result:
                    break
            self._create_teardown()
            self._creat_footer()

            if self.whole_case_content == "":
                log.error("无法生成测试用例, 测试文件路径: {}".format(case_path))
                return

            if output_path.endswith("/"):
                output_path = output_path[:-1]
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            global set_name
            file_name = set_name.get(case_path).get("file_name")
            dir_name = set_name.get(case_path).get("dir_name")
            _output_path = output_path + dir_name + "/"
            if not os.path.exists(_output_path):
                os.mkdir(_output_path)
            output_file = _output_path + file_prefix + "_" + file_name + ".py"
            # print(self.whole_case_content)
            with open(output_file, mode='w') as f:
                f.write(self.whole_case_content)
                log.info("生成测试用例文件: {}".format(output_file))


if __name__ == "__main__":
    auto = AutoCreateCaseCls(case_path="/Users/pengwei/Desktop/测试用例集/3.3/VisualModeler", point_case="/流程引擎/流程数据库节点大数据效率.xls")
    # auto = AutoCreateCaseCls(case_path="/Users/pengwei/Desktop/测试用例集/3.3/VisualModeler")
    auto.auto_create(output_path="/Users/pengwei/Downloads/Download/cases/VisualModeler")
