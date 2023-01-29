# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/17 下午4:56

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from client.page.func.alertBox import BeAlertBox
from client.page.func.input import set_textarea
from client.app.VisualModeler.doctorwho.doctorWho import DoctorWho
from client.page.func.pageMaskWait import page_wait
from client.page.func.tableData import get_table_data2
from client.page.func.loadData import load_sample
from client.page.func.regular import RegularCube
from client.page.func.pagination import Pagination
from client.page.func.level import choose_level
from client.app.VisualModeler.cmd.tplVar import VarEditor
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class RulerX:

    def __init__(self):
        self.browser = get_global_var("browser")
        DoctorWho().choose_menu("指令配置-通用指令解析配置")
        page_wait()
        self.ruler_main_iframe_xpath = "//iframe[contains(@src, '/VisualModeler/html/rulerx/rulerxTmpl.html')]"
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, self.ruler_main_iframe_xpath)))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]")))
        page_wait()
        self.analysis_name = None
        self.judge_type = None
        sleep(1)

    def choose(self, analyzer_name):
        """
        :param analyzer_name: 解析模版名称
        """
        try:
            self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='keyword']/following-sibling::span[1]/input[1]").send_keys(analyzer_name)
            page_wait()
            self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-query']").click()
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[@field='analyzerName']/*[contains(@class,'analyzerName')]/*[text()='{}']".format(
                    analyzer_name)).click()
            log.info("选择解析模版：{0}".format(analyzer_name))
        except NoSuchElementException:
            log.error("所选解析模版不存在, 解析模版名称: {0}".format(analyzer_name))

    def add(self, basic_cfg, result_format_cfg, segment_cfg, format_table_cfg, judge_type, judge_cfg):
        """
        :param basic_cfg: 基本信息配置
        :param result_format_cfg: 结果格式化配置
        :param segment_cfg: 分段规则配置
        :param format_table_cfg: 格式化二维表配置
        :param judge_type: 选择判断规则
        :param judge_cfg: 判断规则配置

        {
            "操作": "",
            "参数": {
                "基本信息配置": {
                    "模版名称": "",
                    "模版说明": ""
                },
                "结果格式化配置": {
                    "分段": "是",
                    "格式化成二维表": "是",
                },
                "分段规则配置": {
                    "段开始特征行": "",
                    "段结束特征行": "",
                    "样例数据": "",
                    "抽取每一段的头部字段": "否"

                },
                "格式化二维表配置": {
                    "解析开始行": "1",
                    "通过正则匹配数据列": "是",
                    "列总数": "",
                    "拆分方式": "",
                    "列分隔符": "",
                    "正则魔方": {
                        "设置方式": "添加",
                        "正则模版名称": "pw自动化正则模版",
                        "高级模式": "否",
                        "标签配置": [
                            {
                                "标签": "自定义文本",
                                "值": "pw",
                                "是否取值": "黄色"
                            },
                            {
                                "标签": "任意字符",
                                "值": "1到多个",
                                "是否取值": "绿色"
                            }
                        ]
                    },
                    "样例数据": ""
                },
                "选择判断规则": "二维表结果判断",
                "判断规则配置": {
                    "目标行": "",
                    "行结果关系": "",
                    "规则管理": [
                        {
                            "列名": "列1",
                            "关系": "不等于",
                            "匹配值": "0",
                            "条件满足时": "异常",
                            "匹配不到值时": "无数据进行规则判断",
                            "异常提示信息": ""
                        }
                    ]
                }
            }
        }
        """
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[text()='添加']")))
        self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-add']").click()
        # 进入解析模版配置详情页面
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='analyzerName']/following-sibling::span/input[1]")))
        sleep(1)

        # 基本信息配置
        if basic_cfg:
            self.step_basic_info(analyzer_name=basic_cfg.get("模版名称"), remark=basic_cfg.get("模版说明"))
        # 点击下一步
        self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
        page_wait(timeout=3)

        # 结果格式化配置
        if result_format_cfg:
            self.step_result_format(enable_segment=result_format_cfg.get("分段"),
                                    enable_format_table=result_format_cfg.get("格式化成二维表"))
        # 点击下一步
        self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
        page_wait(timeout=3)

        # 分段规则配置
        if segment_cfg:
            self.step_segment(regexp_start=segment_cfg.get("段开始特征行"), regexp_end=segment_cfg.get("段结束特征行"),
                              sample=segment_cfg.get("样例数据"), extract_header=segment_cfg.get("抽取头部字段"))
            # 点击下一步
            self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
            page_wait(timeout=3)

        # 格式化二维表配置
        if format_table_cfg:
            self.step_format_table(begin_row=format_table_cfg.get("解析开始行"), enable_magic=format_table_cfg.get("通过正则匹配数据列"),
                                   total_columns=format_table_cfg.get("列总数"), row_split_type=format_table_cfg.get("拆分方式"),
                                   split_tag=format_table_cfg.get("列分隔符"), magic=format_table_cfg.get("正则魔方"),
                                   sample=format_table_cfg.get("样例数据"))
            # 点击下一步
            self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
            page_wait(timeout=3)

        # 选择判断规则
        if judge_type:
            # 本身有4种规则，当前面选择格式化二维表配置时，出现特定判断规则
            self.step_choose_judge_type(judge_type=judge_type)
            self.judge_type = judge_type
        # 点击下一步
        self.browser.find_element(By.XPATH, "//*[text()='下一步']").click()
        page_wait(timeout=3)

        # 判断规则配置
        if judge_cfg:
            self.step_judge_cfg(keyword=judge_cfg.get("关键字"), ignore_case=judge_cfg.get("忽略大小写"),
                                section_relation=judge_cfg.get("段结果关系"), when_matched=judge_cfg.get("条件满足时"),
                                unmeet_desc=judge_cfg.get("异常提示信息"), keyword_edit=judge_cfg.get("关键字配置"),
                                var_list=judge_cfg.get("变量配置"), kw_relation=judge_cfg.get("关键字值比较结果关系"),
                                compare=judge_cfg.get("条件"), rows=judge_cfg.get("行数"),
                                target_row=judge_cfg.get("目标行"), row_relation=judge_cfg.get("行结果关系"),
                                ruler_conf=judge_cfg.get("规则管理"), issuing_cmd=judge_cfg.get("下发指令"),
                                sample=judge_cfg.get("样例数据"))
        # 点击完成
        self.browser.find_element(By.XPATH, "//*[text()='完成']").click()
        alert = BeAlertBox(timeout=5)
        msg = alert.get_msg()
        if alert.title_contains("向导配置完成"):
            log.info("解析模版【{0}】配置完成".format(self.analysis_name))
        else:
            log.warning("解析模版【{0}】配置失败，失败提示: {1}".format(self.analysis_name, msg))
        set_global_var("ResultMsg", msg, False)

    def step_basic_info(self, analyzer_name, remark):
        """
        # 基本信息配置
        :param analyzer_name: 模版名称
        :param remark: 模版说明
        """
        # 模版名称
        if analyzer_name:
            self.browser.find_element(By.XPATH, "//*[@id='analyzerName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='analyzerName']/following-sibling::span/input[1]").send_keys(analyzer_name)
            log.info("设置模版名称: {}".format(analyzer_name))

        # 模版说明
        if remark:
            remark_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='analyzerDesc']/following-sibling::span/textarea")
            set_textarea(textarea=remark_textarea, msg=remark)
            if isinstance(remark, list):
                log.info("设置模版说明: {}".format('\n'.join(remark)))
            else:
                log.info("设置模版说明: {}".format(remark))

        # 获取当前解析模版名称
        self.analysis_name = self.browser.find_element(
            By.XPATH, "//*[@id='analyzerName']/following-sibling::span/input[2]").get_attribute("defaultValue")
        sleep(1)

    def step_result_format(self, enable_segment, enable_format_table):
        """
        :param enable_segment: 分段， 是/否
        :param enable_format_table: 格式化成二维表， 是/否
        """
        # 分段
        js = 'return $("#askSubsection")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【分段】勾选状态: {0}".format(status))

        enable_segment_element = self.browser.find_element(By.XPATH, "//*[@id='askSubsection']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_segment_element)

        tmp = True if enable_segment == "是" else False
        if tmp ^ status:
            enable_segment_element.click()
            log.info("【分段】设置成: {0}".format(enable_segment))
        else:
            log.info("【分段】状态已经是: {0}".format(enable_segment))

        # 格式化成二维表
        js = 'return $("#askTable")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【格式化成二维表】勾选状态: {0}".format(status))

        enable_format_table_element = self.browser.find_element(By.XPATH, "//*[@id='askTable']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_format_table_element)

        tmp = True if enable_format_table == "是" else False
        if tmp ^ status:
            enable_format_table_element.click()
            log.info("【格式化成二维表】设置成: {0}".format(enable_format_table))
        else:
            log.info("【格式化成二维表】状态已经是: {0}".format(enable_format_table))
        sleep(1)

    def step_segment(self, regexp_start, regexp_end, sample, extract_header):
        """
        # 分段规则配置
        :param regexp_start: 段开始特征行，正则
        :param regexp_end: 段结束特征行，正则
        :param sample: 样例数据，文件名
        :param extract_header: 抽取头部字段，是/否
        """
        # 段开始特征行
        if regexp_start:
            self.browser.find_element(By.XPATH, "//*[@id='regexpStart']/following-sibling::span//a").click()

            # 切换到正则配置iframe页面
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]")))
            confirm_selector = "//*[@id='regexpPopUp']"
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regexp_start.get("设置方式"), regular_name=regexp_start.get("正则模版名称"),
                                    advance_mode=regexp_start.get("高级模式"), regular=regexp_start.get("标签配置"),
                                    expression=regexp_start.get("表达式"), confirm_selector=confirm_selector)
            if regular_cube.needJumpIframe:
                self.browser.switch_to.default_content()
                # 进入解析模版配置列表页面
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.ruler_main_iframe_xpath))
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到解析模版配置页面
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]")))
                    # 切换到正则配置iframe页面
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]")))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)

            # 点击确定关闭正则魔方配置
            self.browser.find_element(By.XPATH, "//*[@id='regexp-ok']").click()
            self.browser.switch_to.parent_frame()
            sleep(1)

        # 段结束特征行
        if regexp_end:
            self.browser.find_element(By.XPATH, "//*[@id='regexpEnd']/following-sibling::span//a").click()

            # 切换到正则配置iframe页面
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]")))
            confirm_selector = "//*[@id='regexpPopUp']"
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regexp_end.get("设置方式"), regular_name=regexp_end.get("正则模版名称"),
                                    advance_mode=regexp_end.get("高级模式"), regular=regexp_end.get("标签配置"),
                                    expression=regexp_end.get("表达式"), confirm_selector=confirm_selector)
            if regular_cube.needJumpIframe:
                self.browser.switch_to.default_content()
                # 进入解析模版配置列表页面
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.ruler_main_iframe_xpath))
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到解析模版配置页面
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]")))
                    # 切换到正则配置iframe页面
                    wait = WebDriverWait(self.browser, 30)
                    wait.until(ec.frame_to_be_available_and_switch_to_it((
                        By.XPATH,
                        "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]")))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)

            # 点击确定关闭正则魔方配置
            self.browser.find_element(By.XPATH, "//*[@id='regexp-ok']").click()
            self.browser.switch_to.parent_frame()
            sleep(1)

        # 样例数据
        if sample:
            sample_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='subsectionSampleData']/following-sibling::span/textarea")
            sample = load_sample(sample_file_name=sample)
            set_textarea(textarea=sample_textarea, msg=sample)
            log.info("样例数据填充完成")
            sleep(1)

        # 抽取头部字段
        if extract_header:
            if extract_header == "是":
                self.browser.find_element(By.XPATH, "//*[@id='isExtractHeaderEach']").click()
                log.info("勾选【抽取每一段的头部字段】")

        sleep(1)

    def step_format_table(self, begin_row, enable_magic, total_columns, row_split_type, split_tag, magic, sample):
        """
        # 格式化二维表配置
        :param begin_row: 解析开始行
        :param enable_magic: 通过正则匹配数据列，是/否
        :param total_columns: 列总数
        :param row_split_type: 拆分方式，文本/正则
        :param split_tag: 列分隔符
        :param magic: 正则魔方，开启通过正则匹配数据列或拆分方式为正则时使用
        :param sample: 样例数据，指定resources下的文件名，自动从文件加载并填充
        """
        # 正则配置
        regular_cube = RegularCube()
        regular_cube.setAnalyze(begin_row=begin_row, enable_magic=enable_magic, total_columns=total_columns,
                                row_split_type=row_split_type, split_tag=split_tag, magic=magic)
        if regular_cube.needJumpIframe:
            # 向上返回2级，切换到解析模版配置iframe
            self.browser.switch_to.parent_frame()
            self.browser.switch_to.parent_frame()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存正则模版成功")
                # 切换到正则魔方配置iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)

        # 样例数据
        if sample:
            sample_data = load_sample(sample_file_name=sample)
            sample_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='tableExampleDatatableFormatCfgDiv']/following-sibling::span/textarea")
            set_textarea(textarea=sample_textarea, msg=sample_data)
            log.info("样例数据填充完成")
            sleep(1)

        # 点击效果预览
        self.browser.find_element(By.XPATH, "//*[@id='tableFormatCfgDiv']//*[@class='formatBtn']").click()
        page_wait(timeout=5)
        sleep(1)
        # 如果出现弹出框，则表示预览异常
        alert = BeAlertBox(timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            raise Exception(msg)
        else:
            log.info("解析规则预览正常")
            # 切换到通用指令解析配置页面
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]"))
            table_xpath = "//*[@id='issuingCmdIframeTabletableFormatCfgDiv']/following-sibling::div[1]//*[@class='format_tab']"
            data = get_table_data2(table_xpath=table_xpath, return_column=True)
            log.info("预览结果: {}".format(data))
        sleep(1)

    def step_choose_judge_type(self, judge_type):
        """
        # 选择判断规则
        :param judge_type: 判断规则，只能选一个
        """
        # 选择判断规则
        self.browser.find_element(
            By.XPATH, "//*[@name='judgeType']/following-sibling::span[text()='{}']".format(judge_type)).click()
        sleep(1)

    def step_judge_cfg(self, keyword, ignore_case, section_relation, when_matched, unmeet_desc, keyword_edit, var_list,
                       kw_relation, compare, rows, target_row, row_relation, ruler_conf, issuing_cmd, sample):
        """
        # 判断规则配置
        :param keyword: 关键字
        :param ignore_case: 忽略大小写
        :param section_relation: 段结果关系
        :param when_matched: 条件满足时
        :param unmeet_desc: 异常提示信息
        :param keyword_edit: 关键字配置
        :param var_list: 变量配置
        :param kw_relation: 关键字值比较结果关系
        :param compare: 条件
        :param rows: 行数
        :param target_row: 目标行
        :param row_relation: 行结果关系
        :param ruler_conf: 规则管理，数组
        :param issuing_cmd: 下发指令
        :param sample: 样例数据
        """
        page_wait(timeout=3)
        sleep(1)

        if self.judge_type == "匹配关键字判断":
            # 匹配关键字判断
            self.judge_cfg_kw(keyword, ignore_case, section_relation, when_matched, unmeet_desc, issuing_cmd, sample)

        elif self.judge_type == "匹配关键字的值比较判断":
            # 匹配关键字的值比较判断
            self.judge_cfg_kwValue(keyword_edit, var_list, kw_relation, ruler_conf, issuing_cmd, sample)

        elif self.judge_type == "结果行数判断":
            # 结果行数判断
            self.judge_cfg_rows(compare, rows, section_relation, when_matched, unmeet_desc, issuing_cmd, sample)

        elif self.judge_type == "二维表结果判断":
            # 二维表结果判断
            self.judge_cfg_table(target_row, row_relation, var_list, ruler_conf)
        else:
            # 无需判断
            return

        # 预览结果
        page_wait()
        alert = BeAlertBox(timeout=1)
        if alert.exist_alert:
            msg = alert.get_msg()
            log.info("解析结果预览失败，预览提示: {}".format(msg))
            raise Exception(msg)
        else:
            # 切换到通用指令解析配置页面
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src, 'rulerxTmplEditWin.html')]"))
            analysis_result_element = self.browser.find_element(
                By.XPATH, "//*[contains(@class,'analysisResult')]/following-sibling::span/input")
            analysis_result = analysis_result_element.get_attribute("defaultValue")
            log.info("解析结果预览成功，解析结果: {}".format(analysis_result))
        sleep(1)

    def judge_cfg_table(self, target_row, row_relation, var_list, ruler_conf):
        """
        # 判断规则配置-二维表结果判断
        :param target_row: 目标行
        :param row_relation: 行结果关系
        :param var_list: 变量配置，数组
        :param ruler_conf: 规则管理，数组
        """
        log.info("判断规则配置，选择【二维表结果判断】")

        # 目标行
        if target_row:
            self.browser.find_element(
                By.XPATH, "//*[@name='tableTargetRowSel']/../../*[contains(text(),'{}')]".format(target_row)).click()
            log.info("设置目标行: {}".format(target_row))

        # 行结果关系
        if row_relation:
            self.browser.find_element(
                By.XPATH, "//*[@name='tableRowRelation']/../../*[contains(text(),'{}')]".format(row_relation)).click()
            log.info("设置行结果关系: {}".format(row_relation))

        # 变量配置
        if var_list:
            if not isinstance(var_list, list):
                raise TypeError("变量配置需要是数组格式")
            for var in var_list:
                self.browser.find_element(By.XPATH, "//*[@id='tableVarEditor']//a[contains(@class,'add')]").click()
                self.variable_manage(var_mode=var.get("变量模式"), var_name=var.get("变量名称"),
                                     var_type=var.get("变量类型"), var_desc=var.get("变量描述"),
                                     algorithm_list=var.get("运算规则配置"), time_set=var.get("时间配置"),
                                     list_content=var.get("列表内容"), agg_func_set=var.get("聚合函数配置"),
                                     func_set=var.get("功能函数配置"))

        # 规则管理
        if ruler_conf:
            i = 1
            for rule in ruler_conf:
                add_element = self.browser.find_element(By.XPATH, "//*[@id='tableRuleMgr']//*[@data-mtips='添加一套规则']")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", add_element)
                add_element.click()
                log.info("设置规则{}".format(i))
                self.ruler(left_value=rule.get("列名"), relation=rule.get("关系"), right_value=rule.get("匹配值"),
                           when_matched=rule.get("条件满足时"), when_not_matched=rule.get("匹配不到值时"),
                           error_tips=rule.get("异常提示信息"), row_num=i)
                i += 1

        # 解析结果预览
        self.browser.find_element(By.XPATH, "//*[text()='解析结果预览']/following-sibling::div/a").click()
        sleep(1)
        # page_wait()
        # alert = BeAlertBox(timeout=5)
        # if alert.exist_alert:
        #     msg = alert.get_msg()
        #     log.info("解析结果预览失败，预览提示: {}".format(msg))
        #     raise Exception(msg)
        # else:
        #     # 切换到通用指令解析配置页面
        #     self.browser.switch_to.frame(
        #         self.browser.find_element(By.XPATH, "//iframe[contains(@src, 'rulerxTmplEditWin.html')]"))
        #     analysis_result_element = self.browser.find_element(By.XPATH, 
        #         "//*[contains(@class,'analysisResult')]/following-sibling::span/input")
        #     analysis_result = analysis_result_element.get_attribute("defaultValue")
        #     log.info("解析结果预览成功，解析结果: {}".format(analysis_result))

    def judge_cfg_kw(self, keyword, ignore_case, section_relation, when_matched, unmeet_desc, issuing_cmd, sample):
        """
        # 判断规则配置-匹配关键字判断
        :param keyword: 关键字
        :param ignore_case: 忽略大小写
        :param section_relation: 段结果关系，或/且
        :param when_matched: 条件满足时
        :param unmeet_desc: 异常提示信息
        :param issuing_cmd: 下发指令
        :param sample: 样例数据

        {
            "关键字": "abc",
            "忽略大小写": "是",
            "段结果关系": "或",
            "条件满足时": "异常",
            "异常提示信息": "未匹配到关键字",
            "下发指令": "",
            "样例数据": "xxx_sample.txt"
        }

        """
        log.info("判断规则配置，选择【匹配关键字判断】")

        # 关键字
        if keyword:
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'keyWord')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'keyWord')]/following-sibling::span/input[1]").send_keys(keyword)
            log.info("设置关键字: {0}".format(keyword))

        # 忽略大小写
        js = 'return $(".ignoreCase")[0].checked;'
        ignore_status = self.browser.execute_script(js)
        log.info("【忽略大小写】勾选状态: {0}".format(ignore_status))
        ignore_element = self.browser.find_element(By.XPATH, "//*[@class='ignoreCase']")
        if ignore_case:
            if ignore_case == "是":
                if ignore_status:
                    log.info("【忽略大小写】已勾选")
                else:
                    ignore_element.click()
                    log.info("勾选【忽略大小写】")
            else:
                if ignore_status:
                    ignore_element.click()
                    log.info("取消勾选【忽略大小写】")
                else:
                    log.info("【忽略大小写】未勾选")

        # 段结果关系
        if section_relation:
            if section_relation == "或":
                self.browser.find_element(By.XPATH, "//*[@name='sectionRelation' and @value='0']").click()
            else:
                self.browser.find_element(By.XPATH, "//*[@name='sectionRelation' and @value='1']").click()
            log.info("设置段结果关系: {0}".format(section_relation))

        # 条件满足时
        if when_matched:
            self.browser.find_element(By.XPATH, "//*[contains(@class,'meetResult')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(when_matched))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("条件满足时选择: {0}".format(when_matched))
                    break

        # 异常提示信息
        if unmeet_desc:
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'unmeetDesc')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'unmeetDesc')]/following-sibling::span/input[1]").send_keys(unmeet_desc)
            log.info("设置异常提示信息: {0}".format(unmeet_desc))

        # 下发指令
        if issuing_cmd:
            self.issuing_cmd(level=issuing_cmd.get("网元分类"), vendor=issuing_cmd.get("厂家"),
                             model=issuing_cmd.get("设备型号"), netunit=issuing_cmd.get("网元名称"),
                             cmd=issuing_cmd.get("指令名称"))
            log.info("执行下发指令操作")

        # 样例数据
        if sample:
            sample_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='kwExampleData']/following-sibling::span/textarea")
            sample = load_sample(sample_file_name=sample)
            set_textarea(textarea=sample_textarea, msg=sample)
            log.info("样例数据填充完成")

        # 点击格式化按钮
        self.browser.find_element(
            By.XPATH, "//*[@id='issuingCmdIframeKw']/following-sibling::div//*[@class='formatBtn']").click()
        sleep(1)

    def judge_cfg_kwValue(self, keyword_edit, var_list, kw_relation, ruler_conf, issuing_cmd, sample):
        """
        # 判断规则配置-匹配关键字的值比较判断
        :param keyword_edit: 关键字配置，数组
        :param var_list: 变量配置，数组
        :param kw_relation: 关键字值比较结果关系，或/且
        :param ruler_conf: 规则管理，数组
        :param issuing_cmd: 下发指令
        :param sample: 样例数据

        {
            "关键字配置": [
                {
                    "关键字": "行数",
                    "抓取行": ["1", ""],
                    "正则魔方": {
                        "设置方式": "选择",
                        "正则模版名称": "正则魔方cat /etc/passwd"
                    },
                    "取值": "取所有匹配值",
                    "将结果转成16进制": "否",
                    "统计个数": "是"
                }
            ],
            "变量配置": [
                {
                    "变量模式": "常用变量",
                    "变量名称": "前1天(YYYY-MM-DD)"
                },
                {
                    "变量模式": "高级模式",
                    "变量名称": "行数加1",
                    "变量类型": "关键字运算",
                    "变量描述": "取行数加1结果",
                    "变量内容": [
                        ["", "行数", "+", "1", ""]
                    ]
                }
            ],
            "关键字值比较结果关系": "或",
            "规则管理": {
                "列名": "列5",
                "关系": "等于",
                "匹配值": "Normal",
                "条件满足时": "正常",
                "匹配不到值时": "无数据进行规则判断",
                "异常提示信息": "板卡状态出现异常"
            },
            "下发指令": "",
            "样例数据": "xxx_sample.txt"
        }

        """

        log.info("判断规则配置，选择【匹配关键字的值比较判断】")

        # 关键字配置
        if keyword_edit:

            for key_set in keyword_edit:
                if not isinstance(key_set, dict):
                    raise KeyError("【关键字配置】格式错误")
                self.browser.find_element(By.XPATH, "//*[@id='kwValueKwEditor']//a[contains(@class,'add')]").click()
                sleep(1)

                keyword = key_set.get("关键字")
                filter_lines = key_set.get("抓取行")
                keyword_regex = key_set.get("正则魔方")
                value_type = key_set.get("取值")
                is_hex = key_set.get("将结果转成16进制")
                is_count = key_set.get("统计个数")
                num = 1

                # 获取关键字id属性
                keyword_edit_box = self.browser.find_element(
                    By.XPATH, "//*[contains(@onblur,'kwEditor.checkKeywordName') and text()='关键字{0}']/../..".format(num))
                keyword_id = keyword_edit_box.get_attribute("id")
                if keyword_id is None:
                    raise NoSuchElementException
                key_xpath = "//*[@id='{0}']".format(keyword_id)

                # 关键字
                if keyword:
                    key_input = self.browser.find_element(
                        By.XPATH, key_xpath + "//*[contains(@onblur,'kwEditor.checkKeywordName')]")
                    key_input.click()
                    key_input.send_keys(Keys.COMMAND, "a")      # mac使用COMMAND，windows使用CONTROL
                    key_input.send_keys(Keys.DELETE)
                    key_input.send_keys(keyword)
                    log.info("设置关键字: {0}".format(keyword))
                    sleep(1)

                # 抓取行
                if filter_lines:
                    begin_line = filter_lines[0]
                    end_line = filter_lines[1]

                    # 开始行
                    if begin_line:
                        self.browser.find_element(
                            By.XPATH, key_xpath + "//*[contains(@class,'startRow')]/following-sibling::span[1]/input[1]").send_keys(
                            begin_line)

                    # 结束行
                    if end_line:
                        self.browser.find_element(
                            By.XPATH, key_xpath + "//*[contains(@class,'endRow')]/following-sibling::span[1]/input[1]").send_keys(
                            begin_line)

                    log.info("设置从哪些行抓取: {0} - {1}".format(begin_line, end_line))

                # 正则魔方
                if keyword_regex:
                    confirm_selector = "//*[@id='regexp{0}']".format(keyword_id)
                    regular_cube = RegularCube()
                    regular_cube.setRegular(set_type=keyword_regex.get("设置方式"), regular_name=keyword_regex.get("正则模版名称"),
                                            advance_mode=keyword_regex.get("高级模式"), regular=keyword_regex.get("标签配置"),
                                            expression=keyword_regex.get("表达式"), confirm_selector=confirm_selector)
                    if regular_cube.needJumpIframe:
                        alert = BeAlertBox()
                        msg = alert.get_msg()
                        if alert.title_contains("成功"):
                            log.info("保存正则模版成功")
                            # 进入解析模版配置详情页面
                            wait = WebDriverWait(self.browser, 30)
                            wait.until(ec.frame_to_be_available_and_switch_to_it((
                                By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]")))
                        else:
                            log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                        set_global_var("resultMsg", msg, False)

                # 划动页面
                move_element = self.browser.find_element(
                    By.XPATH, key_xpath + "//*[contains(@class,'valueType')]/following-sibling::span//a")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", move_element)

                # 取值
                if value_type:
                    self.browser.find_element(
                        By.XPATH, key_xpath + "//*[contains(@class,'valueType')]/following-sibling::span//a").click()
                    value_type_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'_combobox_') and text()='{0}']".format(value_type))
                    if len(value_type_elements) == 0:
                        raise NoSuchElementException
                    for element in value_type_elements:
                        if element.is_displayed():
                            element.click()
                            log.info("取值选择: {0}".format(value_type))
                            break

                # 将结果转成16进制
                if is_hex:
                    if is_hex == "是":
                        self.browser.find_element(By.XPATH, key_xpath + "//*[@class='isHex']").click()
                        log.info("勾选【将结果转成16进制】")

                # 统计个数
                if is_count:
                    if is_count == "是":
                        self.browser.find_element(By.XPATH, key_xpath + "//*[@class='isCount']").click()
                        log.info("勾选【统计个数】")

                # 休眠
                num += 1
                sleep(1)

        # 变量配置
        if var_list:
            if not isinstance(var_list, list):
                raise TypeError("变量配置需要是数组格式")
            for var in var_list:
                self.browser.find_element(By.XPATH, "//*[@id='kwValueVarEditor']//a[contains(@class,'add')]").click()
                self.variable_manage(var_mode=var.get("变量模式"), var_name=var.get("变量名称"),
                                     var_type=var.get("变量类型"), var_desc=var.get("变量描述"),
                                     algorithm_list=var.get("运算规则配置"), time_set=var.get("时间配置"),
                                     list_content=var.get("列表内容"), agg_func_set=var.get("聚合函数配置"),
                                     func_set=var.get("功能函数配置"))

        # 关键字值比较结果关系
        if kw_relation:
            if kw_relation == "或":
                self.browser.find_element(By.XPATH, "//*[@name='kwRelation' and @value='0']")
            elif kw_relation == "且":
                self.browser.find_element(By.XPATH, "//*[@name='kwRelation' and @value='1']")
            else:
                raise KeyError("【关键字值比较结果关系】值错误，{0}".format(kw_relation))

        # 规则管理
        if ruler_conf:
            i = 1
            for rule in ruler_conf:
                add_element = self.browser.find_element(By.XPATH, "//*[@id='kwValueRuleMgr']//*[@data-mtips='添加一套规则']")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", add_element)
                add_element.click()
                log.info("设置规则{}".format(i))
                self.ruler(left_value=rule.get("列名"), relation=rule.get("关系"), right_value=rule.get("匹配值"),
                           when_matched=rule.get("条件满足时"), when_not_matched=rule.get("匹配不到值时"),
                           error_tips=rule.get("异常提示信息"), row_num=i)
                i += 1

        # 下发指令
        if issuing_cmd:
            self.issuing_cmd(level=issuing_cmd.get("网元分类"), vendor=issuing_cmd.get("厂家"),
                             model=issuing_cmd.get("设备型号"), netunit=issuing_cmd.get("网元名称"),
                             cmd=issuing_cmd.get("指令名称"))
            log.info("执行下发指令操作")

            # 样例数据
        if sample:
            sample_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='kwValueExampleData']/following-sibling::span/textarea")
            sample = load_sample(sample_file_name=sample)
            set_textarea(textarea=sample_textarea, msg=sample)
            log.info("样例数据填充完成")

            # 点击格式化按钮
        self.browser.find_element(
            By.XPATH, "//*[@id='issuingCmdIframeKwValue']/following-sibling::div//*[@class='formatBtn']").click()
        sleep(1)

    def judge_cfg_rows(self, compare, rows, section_relation, when_matched, unmeet_desc, issuing_cmd, sample):
        """
        # 判断规则配置-结果行数判断
        :param compare: 条件
        :param rows: 行数
        :param section_relation: 段结果关系
        :param when_matched: 条件满足时
        :param unmeet_desc: 异常提示信息
        :param issuing_cmd: 下发指令
        :param sample: 样例数据

        {
            "条件": "不等于",
            "行数": "10",
            "段结果关系": "且",
            "条件满足时": "异常",
            "异常提示信息": "日志结果行数不匹配",
            "下发指令": "",
            "样例数据": "xxx_sample.txt"
        }

        """
        log.info("判断规则配置，选择【结果行数判断】")

        # 条件
        if compare:
            self.browser.find_element(By.XPATH, "//*[contains(@class,'compare')]/following-sibling::span//a").click()
            compare_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{0}']".format(compare))
            if len(compare_elements) == 0:
                raise NoSuchElementException
            for element in compare_elements:
                if element.is_displayed():
                    element.click()
                    log.info("选择: {0}".format(compare))
                    break

        # 行数
        if rows:
            self.browser.find_element(By.XPATH, "//*[contains(@class,'rowNum')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'rowNum')]/following-sibling::span/input[1]").send_keys(rows)
            log.info("设置行数: {0}".format(rows))

        # 段结果关系
        if section_relation:
            if section_relation == "或":
                self.browser.find_element(By.XPATH, "//*[@name='sectionRelation' and @value='0']").click()
            else:
                self.browser.find_element(By.XPATH, "//*[@name='sectionRelation' and @value='1']").click()
            log.info("设置段结果关系: {0}".format(section_relation))

        # 条件满足时
        if when_matched:
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'meetResult')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(when_matched))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("条件满足时选择: {0}".format(when_matched))
                    break

        # 异常提示信息
        if unmeet_desc:
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'unmeetDesc')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'unmeetDesc')]/following-sibling::span/input[1]").send_keys(unmeet_desc)
            log.info("设置异常提示信息: {0}".format(unmeet_desc))

        # 下发指令
        if issuing_cmd:
            self.issuing_cmd(level=issuing_cmd.get("网元分类"), vendor=issuing_cmd.get("厂家"),
                             model=issuing_cmd.get("设备型号"), netunit=issuing_cmd.get("网元名称"),
                             cmd=issuing_cmd.get("指令名称"))
            log.info("执行下发指令操作")

        # 样例数据
        if sample:
            sample_textarea = self.browser.find_element(
                By.XPATH, "//*[@id='rowExampleData']/following-sibling::span/textarea")
            sample = load_sample(sample_file_name=sample)
            set_textarea(textarea=sample_textarea, msg=sample)
            log.info("样例数据填充完成")

        # 点击格式化按钮
        self.browser.find_element(
            By.XPATH, "//*[@id='issuingCmdIframeRow']/following-sibling::div//*[@class='formatBtn']").click()
        sleep(1)

    def variable_manage(self, var_mode, var_name, var_type, var_desc, algorithm_list, time_set, list_content,
                        agg_func_set, func_set):
        """
        :param var_mode: 变量模式
        :param var_name: 变量名称，高级模式使用
        :param var_type: 变量类型，高级模式使用
        :param var_desc: 变量描述，高级模式使用
        :param algorithm_list: 运算规则配置，数组，高级模式使用
        :param time_set: 时间配置，字典，高级模式使用
        :param list_content: 列表内容，字符串，高级模式使用
        :param agg_func_set: 聚合函数配置，字典，高级模式使用
        :param func_set: 功能函数配置，字典，高级模式使用
        """
        # 切换到变量配置页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/vareditor/varEditorWin.html')]")))
        var_editor = VarEditor(var_mode=var_mode)
        var_editor.add(var_name, var_type, var_desc, algorithm_list, time_set, list_content, agg_func_set, func_set)
        # 返回上层iframe
        self.browser.switch_to.parent_frame()
        sleep(1)

    def issuing_cmd(self, level, vendor, model, netunit, cmd):
        """
        # 下发指令填充样例数据
        :param level: 网元分类
        :param vendor: 厂家
        :param model: 设备型号
        :param netunit: 网元名称
        :param cmd: 指令名称
        """

        # 切换到下发指令页面iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'./issuingCmdIframe.html')]")))
        if self.judge_type == "匹配关键字判断":
            value = "kwExampleData"
        elif self.judge_type == "匹配关键字的值比较判断":
            value = ""
        elif self.judge_type == "结果行数判断":
            value = ""
        else:
            raise KeyError("不支持的判断规则: {0}".format(self.judge_type))

        # 划到下发指令填充样例数据
        step_element = self.browser.find_element(By.XPATH, "//*[text()='下发指令填充样例数据']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", step_element)
        sleep(1)
        # 点开下发指令页面
        self.browser.find_element(By.XPATH, "//*[@value='{0}']/following-sibling::div/div/div[2]/a".format(value))

        # 网元分类
        if level:
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            choose_level(level_list=level)
            # 再次点击收起下拉框
            self.browser.find_element(By.XPATH, "//*[@id='level']/following-sibling::span//a").click()
            log.info("设置网元分类: {0}".format(level))

        # 厂家
        if vendor:
            self.browser.find_element(By.XPATH, "//*[@id='vendor']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vendor') and text()='{0}']".format(vendor)).click()
            log.info("设置厂家: {0}".format(vendor))

        # 设备型号
        if model:
            self.browser.find_element(By.XPATH, "//*[@id='netunitModel']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'netunitModel') and text()='{0}']".format(model)).click()
            log.info("设置设备型号: {0}".format(model))

        # 点击查询按钮
        self.browser.find_element(By.XPATH, "//*[@id='queryIssuingTab']").click()
        page_wait()
        sleep(1)

        # 网元名称
        if netunit:
            table_xpath = "//*[@id='tabToolbar']/following-sibling::div[1]"
            page = Pagination(table_xpath=table_xpath)
            page.set_page_size(50)
            self.browser.find_element(By.XPATH, "//*[@field='netunitName']/*[text()='{0}']".format(netunit)).click()
            log.info("选择网元名称: {0}".format(netunit))

        # 划到指令名称区域
        cmd_area = self.browser.find_element(By.XPATH, "//*[@id='tabToolbar']/following-sibling::div[1]/div/div[2]")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", cmd_area)
        sleep(1)

        # 指令名称
        if cmd:
            table_xpath = "//*[@id='tabToolbar']/following-sibling::div[3]"
            page = Pagination(table_xpath=table_xpath)
            page.set_page_size(50)
            self.browser.find_element(By.XPATH, "//*[@field='cmdName']/*[text()='{0}']".format(cmd)).click()
            log.info("选择指令名称: {0}".format(cmd))

        # 点击指令下发按钮
        self.browser.find_element(By.XPATH, "//*[@id='issuingCmd']").click()
        self.browser.switch_to.default_content()
        # 进入解析模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.ruler_main_iframe_xpath))
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("确定在网元【{0}】上下发指令吗".format(cmd), auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("下发成功，正在尝试查询下发日志"):
                log.info("指令【{0}】下发成功".format(cmd))

                # 切换到解析模版配置页面
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'rulerxTmplEditWin.html')]")))
            else:
                log.warning("指令下发失败，失败提示: {0}".format(msg))
        else:
            log.warning("指令下发失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def ruler(self, left_value, relation, right_value, row_num, when_matched, when_not_matched, error_tips):
        """
        :param left_value: 列名
        :param relation: 关系
        :param right_value: 匹配值
        :param when_matched: 条件满足时
        :param when_not_matched: 匹配不到值时
        :param error_tips: 异常提示信息
        :param row_num: 规则N
        """
        parent_ruler_xpath = "//*[@class='cfg_box_row singleRule'][{0}]".format(row_num)
        rule_element = self.browser.find_element(By.XPATH, "//*[@class='rowRuleDiv']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", rule_element)

        # 列名
        if left_value:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[contains(@class,'leftValue')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(left_value))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("规则{0}选择列名: {1}".format(row_num, left_value))
                    break

        # 关系
        if relation:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[contains(@class,'operator')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(relation))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("规则{0}选择关系: {1}".format(row_num, relation))
                    break

        # 匹配值
        if right_value:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[contains(@class,'rightValue')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(right_value))
            if len(elements) == 0:
                # 如果下拉框没有预期的值，则在输入框手动输入
                self.browser.find_element(
                    By.XPATH, parent_ruler_xpath + "//*[contains(@class,'rightValue')]/following-sibling::span//a").click()
                self.browser.find_element(
                    By.XPATH, parent_ruler_xpath + "//*[contains(@class,'rightValue')]/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, parent_ruler_xpath + "//*[contains(@class,'rightValue')]/following-sibling::span/input[1]").send_keys(
                    right_value)
                log.info("规则{0}输入匹配值: {1}".format(row_num, right_value))
            else:
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        log.info("规则{0}选择匹配值: {1}".format(row_num, right_value))
                        break

        # 条件满足时
        if when_matched:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[contains(@class,'meetResult')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(when_matched))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("规则{0}选择条件满足时: {1}".format(row_num, when_matched))
                    break

        # 匹配不到值时
        if when_not_matched:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[contains(@class,'unFoundResult')]/following-sibling::span//a").click()
            elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'_combobox_') and text()='{}']".format(when_not_matched))
            for element in elements:
                if element.is_displayed():
                    element.click()
                    log.info("规则{0}选择匹配不到值时: {1}".format(row_num, when_not_matched))
                    break

        # 异常提示信息
        if error_tips:
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[text()='异常提示信息']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, parent_ruler_xpath + "//*[text()='异常提示信息']/following-sibling::span/input[1]").send_keys(
                error_tips)
            log.info("规则{0}设置异常提示信息: {1}".format(row_num, error_tips))

        # 规则N配置完成
        log.info("规则{}配置完成".format(row_num))
        sleep(1)

    def data_clear(self, analyzer_name, fuzzy_match=False):
        """
        :param analyzer_name: 解析模版名称
        :param fuzzy_match: 模糊匹配
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]")))
        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").clear()
        self.browser.find_element(By.XPATH, "//*[@id='keyword']/following-sibling::span/input[1]").send_keys(analyzer_name)
        self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-query']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        sleep(1)
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='analyzerName']//*[starts-with(@data-mtips,'{0}')]".format(analyzer_name))
        else:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='analyzerName']//*[@data-mtips='{0}']".format(analyzer_name))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                js = 'return $(".rulerxTmplTab_datagrid-cell-c1-analyzerName")[1].innerText;'
                search_result = self.browser.execute_script(js)
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element(By.XPATH, "//*[@id='rulerxTmpl-del']").click()
                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains("您确定需要删除{0}吗".format(search_result), auto_click_ok=False):
                    alert.click_ok()
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("成功"):
                        log.info("{0} 删除成功".format(search_result))
                        page_wait()
                        if fuzzy_match:
                            # 重新获取页面查询结果
                            record_element = self.browser.find_elements(
                                By.XPATH, "//*[@field='analyzerName']//*[starts-with(@data-mtips,'{0}')]".format(
                                    analyzer_name))
                            if len(record_element) > 0:
                                exist_data = True
                            else:
                                # 查询结果为空,修改exist_data为False，退出循环
                                log.info("数据清理完成")
                                exist_data = False
                        else:
                            break
                    else:
                        raise Exception("删除数据时出现未知异常: {0}".format(msg))
                else:
                    # 无权操作
                    log.warning("{0} 删除失败，失败提示: {1}".format(analyzer_name, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
