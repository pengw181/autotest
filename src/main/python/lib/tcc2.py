# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/7/30 下午8:47

import os
import time
import json
import xlrd
import traceback
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log
from src.main.python.core.gooflow.case import CaseEngine


class CaseMap:

    def __init__(self):
        self.map = None

    def load(self, map_path, application=None):
        if not os.path.exists(map_path):
            raise FileNotFoundError("无法找到测试用例关系表文件, {}".format(map_path))
        workbook = xlrd.open_workbook(map_path, formatting_info=True)
        sheets = workbook.sheet_by_index(0)
        map_relation = {}
        for i in range(sheets.nrows):
            map_row = sheets.row_values(i)
            # 应用
            app_name = map_row[0]
            # 用例来源文件名
            case_file_from = map_row[1]
            # 用例类名标识
            case_cls_name = map_row[2]
            # 用例文件存放路径名
            case_save_path = map_row[3]
            # 用例文件名标识
            case_file_name = map_row[4]

            if len(case_file_from.strip()) == 0:
                break

            if application:
                if app_name != application:
                    continue

            if self.map and case_file_from in self.map.keys():
                log.info("数据重复，请检查：{}".format(case_file_from))
                continue

            map_relation[case_file_from] = {
                "用例类名标识": case_cls_name,
                "用例文件存放路径名": case_save_path,
                "用例文件名标识": case_file_name
            }
        self.map = map_relation
        log.info("加载用例文件映射关系表成功")


class AutoCreateCaseCls:

    def __init__(self, map_path, application, case_path, point_case=None):
        """
        :param case_path: base_path/application/
        :param point_case: 指定某个用例文件(相对路径)，为空则将所有用例文件转成测试用例class
        """
        if not os.path.exists(case_path):
            raise IsADirectoryError("测试用例路径错误, {}".format(case_path))
        if not case_path.endswith("/"):
            case_path += "/"
        case_path = case_path + application + "/"
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
        self.header = ""
        self.cls = ""
        self.init = ""
        self.setup = ""
        self.case = ""
        self.teardown = ""
        self.footer = ""

        self.header = Section(self.header)
        self.cls = Section(self.cls)
        self.init = Section(self.init)
        self.setup = Section(self.setup)
        self.case = Section(self.case)
        self.teardown = Section(self.teardown)
        self.footer = Section(self.footer)

        self.whole_case_content = ""
        self.cls_name = None
        self.file_suffix = ""
        self.case_order = 1
        self.last_part = self.new_part = 1
        log.info("启动自动生成测试用例程序...")

        case_map = CaseMap()
        case_map.load(map_path=map_path, application=application)
        self.case_relation = case_map.map

    def _create_import(self):
        now = time.strftime('%y/%m/%d %p%I:%M')
        self.header.add_line("# -*- encoding: utf-8 -*-")
        self.header.add_line("# @Author: peng wei")
        self.header.add_line("# @Time: {}".format(now))
        self.header.add_line("\n")
        self.header.add_line("import unittest")
        self.header.add_line("from datetime import datetime")
        self.header.add_line("from src.main.python.lib.globals import gbl")
        self.header.add_line("from src.main.python.lib.logger import log")
        self.header.add_line("from src.main.python.core.gooflow.case import CaseWorker")
        self.header.add_line("from src.main.python.core.gooflow.result import Result")
        self.header.add_line("from src.main.python.lib.screenShot import saveScreenShot")
        self.header.add_line("\n")
        self.header.add_line("\n")

    def _create_case_cls_name(self, relative_path):
        cls_name = self.case_relation.get(relative_path).get("用例类名标识")
        self.cls_name = "{}%PART%".format(cls_name)     # 若分文件则调整
        self.cls.add_line("class {}(unittest.TestCase):".format(self.cls_name))
        self.cls.add_line("\n")

    def _create_init(self, relative_path):
        temp = relative_path[:relative_path.find(".")]
        temp = temp.split("/")[-1]
        self.init.add_line("log.info(\"装载{}测试用例%PART%\")".format(temp), True, 1)  # 若分文件则调整
        self.init.add_line("worker = CaseWorker()", True, 1)
        self.init.add_line("\n")

    def _create_setup(self):
        self.setup.add_line("def setUp(self):    # 最先执行的函数，每执行一个方法调用一次，tearDown同理", True, 1)
        self.setup.add_line("self.browser = gbl.service.get(\"browser\")", True, 2)
        self.setup.add_line("self.worker.init()", True, 2)
        self.setup.add_line("\n")

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
                self.case.add_line("@unittest.skip", True, 1)

            if action:
                short_case_name = action.get("操作")
            else:
                short_case_name = None
            if not short_case_name:
                log.error("生成测试用例函数失败，action数据错误")
                log.error("第{}行用例发生异常".format(self.case_order))
                return False
            action = json.dumps(action, indent=4, ensure_ascii=False)

            func_name = "{}_{}_{}".format(case_prefix, self.case_order, short_case_name)
            self.case.add_line("def {}(self):".format(func_name), True, 1)

            self.case.add_line("u\"\"\"{}\"\"\"".format(case_name.replace("\"", "")), True, 2)

            if len(pres.strip()) > 0:
                self.case.add_line("pres = \"\"\"", True, 2)
                pres_lines = pres.split("\n")
                for pres_line in pres_lines:
                    pres_line = pres_line.replace("\\", "\\\\")
                    self.case.add_line(pres_line, True, 2)
                self.case.add_line("\"\"\"", True, 2)

            action_lines = action.split("\n")
            for action_line in action_lines:
                action_line = action_line.replace("    ", "\t")
                if action_line == action_lines[0]:
                    self.case.add_line("action = {}".format(action_line), True, 2)
                else:
                    self.case.add_line("{}".format(action_line), True, 2)

            if len(checks.strip()) > 0:
                self.case.add_line("checks = \"\"\"", True, 2)
                checks_lines = checks.split("\n")
                for checks_line in checks_lines:
                    checks_line = checks_line.replace("\\", "\\\\")
                    self.case.add_line(checks_line, True, 2)
                self.case.add_line("\"\"\"", True, 2)
            self.case.add_line("log.info('>>>>> {} <<<<<')".format(case_name), True, 2)
            self.case.add_line("gbl.temp.set(\"StartTime\", datetime.now().strftime('%Y%m%d%H%M%S'))", True, 2)

            if len(pres.strip()) > 0:
                self.case.add_line("result = self.worker.pre(pres)", True, 2)
                self.case.add_line("assert result", True, 2)
            self.case.add_line("result = self.worker.action(action)", True, 2)
            self.case.add_line("assert result", True, 2)
            if len(checks.strip()) > 0:
                self.case.add_line("log.info(gbl.temp.get(\"ResultMsg\"))", True, 2)
                self.case.add_line("result = self.worker.check(checks)", True, 2)
                self.case.add_line("assert result", True, 2)
            self.case.add_line("\n")
            self.case_order += 1
            return True
        except IndexError:      # 查找完成
            return False
        except Exception:
            log.error("第{}行用例发生异常".format(self.case_order))
            traceback.print_exc()
            return False

    def _create_teardown(self):
        self.teardown.add_line("def tearDown(self):  # 最后执行的函数", True, 1)
        self.teardown.add_line("self.browser = gbl.service.get(\"browser\")", True, 2)
        self.teardown.add_line("success = Result(self).run_success()", True, 2)
        self.teardown.add_line("if not success:", True, 2)
        self.teardown.add_line("saveScreenShot()", True, 3)
        self.teardown.add_line("self.browser.refresh()", True, 2)
        self.teardown.add_line("\n")
        self.teardown.add_line("\n")

    def _creat_footer(self):
        self.footer.add_line("if __name__ == '__main__':")
        self.footer.add_line("unittest.main()", True, 1)

    def auto_create(self, output_path, batch=0):
        if len(self.relative_case_filepath) == 0:
            log.info("没有测试文件需要生成测试用例")
            return

        for case_path in self.relative_case_filepath:
            self.case_order = 1
            self.last_part = self.new_part = 1
            self.whole_case_content = ""

            log.info("读取文件: {}".format(case_path))
            self._create_import()
            self._create_case_cls_name(relative_path=case_path)
            self._create_init(relative_path=case_path)
            self._create_setup()
            while True:
                result = self._create_each_case(relative_path=case_path, case_order=self.case_order)
                if not result:
                    self._create_teardown()
                    self._creat_footer()
                    if batch > 20 and self.case_order > self.new_part * batch:
                        self.last_part, self.new_part = self.new_part, self.new_part + 1
                        self.cls.replace("Part{}".format(self.last_part), "Part{}".format(self.new_part))
                        self.init.replace("（{}）".format(self.last_part), "（{}）".format(self.new_part))
                        self.file_suffix = "_part{}".format(self.new_part)
                    else:
                        # 指明batch，但总共未超过，所有用例用一个文件保存
                        self.cls.replace("%PART%", "")
                        self.init.replace("%PART%", "")
                        self.file_suffix = None
                    self.save_file(output_path, case_path, self.file_suffix)
                    break
                if batch > 20:
                    if self.case_order > batch:
                        part = int(self.case_order / batch)      # 向下取整
                        if self.cls_name.find("%PART%") > -1:    # 首批用例，[1-batch]
                            self.cls_name = self.cls_name.replace("%PART%", "Part{}".format(self.new_part))
                            self.cls.replace("%PART%", "Part{}".format(part))
                            self.init.replace("%PART%", "（{}）".format(part))

                            # 将本批用例写入文件
                            self._create_teardown()
                            self._creat_footer()
                            self.last_part = self.new_part = part
                            self.file_suffix = "_part{}".format(self.new_part)
                            self.save_file(output_path, case_path, self.file_suffix)
                            # self.cls_name = self.cls_name.replace("%PART%", "Part{}".format(self.new_part))
                            self.whole_case_content = ""
                            self.case = Section("")
                            self.teardown = Section("")
                            self.footer = Section("")

                        if part > self.new_part:
                            # 将其它批次用例写入文件
                            self._create_teardown()
                            self._creat_footer()
                            self.last_part, self.new_part = self.new_part, part
                            self.file_suffix = "_part{}".format(self.new_part)
                            self.cls.replace("Part{}".format(self.last_part), "Part{}".format(self.new_part))
                            self.init.replace("（{}）".format(self.last_part), "（{}）".format(self.new_part))
                            self.cls_name = self.cls_name.replace("Part{}".format(self.last_part),
                                                                  "Part{}".format(self.new_part))
                            self.save_file(output_path, case_path, self.file_suffix)
                            self.whole_case_content = ""
                            self.case = Section("")
                            self.teardown = Section("")
                            self.footer = Section("")
                else:
                    # 所有用例用一个文件保存
                    self.cls.replace("%PART%", "")
                    self.init.replace("%PART%", "")
            if self.case_order == 1:
                log.error("无法生成测试用例, 测试文件路径: {}".format(case_path))
                continue

            self.header = Section("")
            self.cls = Section("")
            self.init = Section("")
            self.setup = Section("")
            self.case = Section("")
            self.teardown = Section("")
            self.footer = Section("")

    def save_file(self, output_path, case_path, file_suffix=None):

        temp = Section("")
        temp.add_section(self.header)
        temp.add_section(self.cls)
        temp.add_section(self.init)
        temp.add_section(self.setup)
        temp.add_section(self.case)
        temp.add_section(self.teardown)
        temp.add_section(self.footer)
        self.whole_case_content = temp

        if output_path.endswith("/"):
            output_path = output_path[:-1]
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        file_name = self.case_relation.get(case_path).get("用例文件名标识")
        dir_name = self.case_relation.get(case_path).get("用例文件存放路径名")
        _output_path = output_path + dir_name + "/"
        if not os.path.exists(_output_path):
            os.mkdir(_output_path)
        if file_suffix:
            file_name += file_suffix
        output_file = _output_path + file_name + ".py"
        if os.path.exists(output_file):
            os.remove(output_file)
        with open(output_file, mode='w') as f:
            f.write(self.whole_case_content.__str__())
            log.info("生成测试用例文件: {}".format(output_file))


class Section(str):

    def __init__(self, section):
        self.section = section
        super().__init__()

    def __str__(self):
        return self.section.__str__()

    def replace(self, old: str, new: str, count: int = ...):
        self.section = self.section.replace(old, new).__str__()

    def add_line(self, line, add_tab=False, tab_times=0):
        if add_tab:
            for i in range(tab_times):
                self.section += "\t"
        self.section += line
        if line != "\n":
            self.section += "\n"

    def add_section(self, section):
        self.section += section.__str__()


if __name__ == "__main__":
    case_load_path = "/Users/pengwei/Desktop/测试用例集/3.3"
    map_load_path = "/Users/pengwei/Documents/衡昊/测试/自动化测试/用例生成关系表.xls"
    app = "VisualModeler"
    # point = "/流程配置/邮件节点.xls"
    point = None
    auto = AutoCreateCaseCls(map_path=map_load_path, case_path=case_load_path, application=app, point_case=point)
    auto.auto_create(output_path="/Users/pengwei/Desktop/autotest/testcase/{}".format(app), batch=50)
