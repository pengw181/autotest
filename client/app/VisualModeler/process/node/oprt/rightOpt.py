# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:09

from .calculation import CalculationCenter
from client.app.VisualModeler.process.node.oprt.loop import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from client.page.func.alertBox import BeAlertBox
from client.page.func.dateUtil import set_calendar
from datetime import datetime
from client.page.func.pageMaskWait import page_wait
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


def opt_action(array):
    log.info("进入操作配置页面")
    opt_tree = OptTreeServer()
    """
    [
        {
            "对象": "操作",
            "右键操作": "添加条件",
            "条件配置": {
                "if": [
                    ["变量", "时间"],
                    ["不等于", ""],
                    ["空值", ""],
                    ["与", ""],
                    ["变量", "地点"],
                    ["包含", ""],
                    ["自定义值", "abc ddd"]
                ],
                "else": "是"
            }
        },
        {
            "对象": "操作",
            "右键操作": "添加循环",
            "循环配置": {
                "循环类型": "变量列表",
                "变量选择": "名字",
                "循环行变量名称": "loop_a",
                "赋值方式": "替换",
            }
        },
        {
            "对象": "操作",
            "右键操作": "添加子流程",
            "条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "操作类型": "绑定子流程",
            "子流程配置": {
                "子流程名称": "pw子流程带区块",
                "创建开始时间": "2020-09-01",
                "创建结束时间": "2020-09-02"
            }
        },
        {
            "对象": "操作",
            "右键操作": "添加子流程",
            "操作类型": "添加子流程",
            "条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "子流程配置": {
                "流程名称":  "pw自动化测试子流程",
                "专业领域":  "AiSee,CS域",
                "流程类型":  "子流程",
                "流程说明":  "pw自动化测试子流程说明",
                "节点异常终止流程": "是"
            }
        },
        {
            "对象": "普通运算结果",
            "右键操作": "复制"
        },
        {
            "对象": "if",
            "右键操作": "删除"
        },
        {
            "对象": "操作",
            "右键操作": "添加操作",
            "运算配置": {
                "运算类型": "基础运算",
                "条件": [
                    ["变量", "时间"],
                    ["不等于", ""],
                    ["空值", ""],
                    ["与", ""],
                    ["变量", "地点"],
                    ["包含", ""],
                    ["自定义值", "abc ddd"]
                ],
                "配置": {
                    "表达式": [
                        ["变量", "时间"],
                        ["不等于", ""],
                        ["空值", ""],
                        ["与", ""],
                        ["变量", "地点"],
                        ["包含", ""],
                        ["自定义值", "abc ddd"]
                    ],
                    "输出名称": "普通运算结果",
                    "输出列": "*",
                    "赋值方式": "替换",
                    "是否转置": "否",
                    "批量修改所有相同的变量名": "否"
                }
            }
        }
    ]
    """
    for tree_step in array:
        # 右键操作节点
        r_click_obj = tree_step.get("对象")
        r_opt = tree_step.get("右键操作")
        opt_tree.r_click_opt(obj=r_click_obj, opt=r_opt)

        # 选择右键操作
        r_opt = tree_step.get("右键操作")
        if r_opt == "添加条件":
            condition_set = tree_step.get("条件配置")
            if condition_set.get("else") == "是":
                flag = True
            else:
                flag = False
            opt_tree.add_if(if_array=condition_set.get("if"), enable_else=flag)

        elif r_opt == "添加循环":
            loop_set = tree_step.get("循环配置")
            opt_tree.add_loop(where=3, loop_type=loop_set.get("循环类型"), loop_info=loop_set)

        elif r_opt == "添加操作":
            opt_config = tree_step.get("运算配置")
            cal = CalculationCenter(oprt_type=opt_config.get("运算类型"))
            # 设置条件
            if opt_config.__contains__("条件"):
                cal.cal_condition(array=opt_config.get("条件"))
            # 启动运算配置
            cal.cal_set(params=opt_config.get("配置"))

        elif r_opt == "添加子流程":
            # 条件
            if tree_step.__contains__("条件"):
                cond = tree_step.get("条件")
            else:
                cond = None

            if tree_step.get("操作类型") == "绑定子流程":
                # 绑定子流程
                subprocess_info = tree_step.get("子流程配置")
                opt_tree.bind_subprocess(subprocess_name=subprocess_info.get("子流程名称"),
                                         create_begin_time=subprocess_info.get("创建开始时间"),
                                         create_end_time=subprocess_info.get("创建结束时间"), cond=cond)
            else:
                # 添加子流程
                subprocess_info = tree_step.get("子流程配置")
                if subprocess_info.get("节点异常终止流程") == "是":
                    flag = True
                else:
                    flag = False
                opt_tree.add_subprocess(process_name=subprocess_info.get("流程名称"), field=subprocess_info.get("专业领域"),
                                        process_type=subprocess_info.get("流程类型"), process_desc=subprocess_info.get("流程说明"),
                                        except_abort=flag, cond=cond)

        elif r_opt == "复制":
            opt_tree.copy()

        elif r_opt == "删除":
            opt_tree.delete()

        else:
            raise KeyError("不支持的右键操作: {0}".format(r_opt))


class OptTreeServer:

    def __init__(self, location=1):
        """

        :param location: 操作位置，0：爬虫节点配置，1：操作配置，默认为1
        """
        self.browser = get_global_var("browser")
        # locator 用来定位一个id为tree的xpath
        if location == 1:
            # 节点操作配置的操作树，通用
            self.locator = "//*[@id='op_tree']"
        else:
            # 爬虫节点的操作树
            self.locator = "//*[@id='fetchop_tree']"
        self.common_tree = (location == 1)

    def r_click_opt(self, obj, opt):
        """
        # 点击某个节点，右键，选择对应动作：添加条件/添加循环/添加操作/删除/添加子流程/复制
        # 适用于操作配置/爬虫节点业务配置

        :param obj: 右键点击的节点元素title属性，如果无法唯一识别，取第一个
        :param opt: 右键操作，包含：添加条件/添加循环/添加操作/删除/添加子流程/复制
        :return: 点击
        """
        log.info("操作树开始进行操作")
        sleep(1)
        action = ActionChains(self.browser)
        page_wait()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.visibility_of_element_located((
            By.XPATH, self.locator + "//*[contains(text(),'{0}')]".format(obj))))
        try:
            right_objs = self.browser.find_elements(By.XPATH, self.locator + "//*[contains(text(),'{0}')]".format(obj))
        except NoSuchElementException:
            raise
        # 取第一个匹配到的元素，右键
        action.context_click(list(right_objs)[0]).perform()
        log.info("选择树节点: {0}".format(obj))
        page_wait(3)
        sleep(1)
        right_menu = self.browser.find_elements(By.XPATH, "//*[text()='{0}']".format(opt))
        # 根据文本匹配到多个元素，找到当前可见的元素，然后点击
        for menu in right_menu:
            if menu.is_displayed():
                menu.click()
                log.info("右键点击: {0}".format(opt))
                break
        sleep(2)

    def add_if(self, if_array, enable_else):
        """
        :param if_array: if，数组
        :param enable_else: else
        {
            "if": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "else": "是"
        }
        """
        # 切换到if配置iframe
        if self.common_tree:
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateNodeCondition.html')]"))
        else:
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerOperateCondition.html')]"))

        # 点击修改按钮
        if self.common_tree:
            self.browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('oprtfitcnd');\"]").click()
        else:
            self.browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('oprtfitcnd','1');\"]").click()

        # 配置条件
        condition(array=if_array)

        # 是否需要勾选else
        js = 'return $("#is_cnd_else")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【ELSE】勾选状态: {0}".format(status))

        if self.common_tree:
            enable_click = self.browser.find_element(By.XPATH, "//*[@id='is_cnd_else']")
        else:
            enable_click = self.browser.find_element(By.XPATH, "//*[@for='is_cnd_else']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if enable_else:
            if not status:
                enable_click.click()
                log.info("勾选【ELSE】")
        else:
            if status:
                enable_click.click()
            log.info("取消勾选【ELSE】")

        # 保存
        if self.common_tree:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveCondtion()']//*[text()='保存']").click()
        else:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveFetchCondtions()']//*[text()='保存']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存条件成功")
        else:
            log.warning("保存条件失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

        if self.common_tree:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))
        else:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到业务配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("CrawlerIframe")))

        return True

    def add_loop(self, where, loop_type, loop_info):
        """
        :param where: 1: 业务配置 2: 控制配置 3: 操作配置
        :param loop_type: 循环类型
        :param loop_info: 循环配置，字典

        # 变量列表循环，自定义模式
        {
            "循环类型": "变量列表",
            "变量选择": "名字",
            "模式": "自定义模式",
            "循环行变量名称": "loop_a",
            "赋值方式": "替换",
        }

        # 变量列表循环，便捷模式
        {
            "循环类型": "变量列表",
            "模式": "便捷模式",
            "变量类型": "指令输出变量",
            "变量选择": "名字"
        }

        # 次数循环
        {
            "循环类型": "次数",
            "循环次数": "3",
            "循环变量名称": "ki",
            "赋值方式": "追加",
            "跳至下一轮条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "结束循环条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ]
        }

        # 条件循环
        {
            "循环类型": "条件",
            "循环条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "跳至下一轮条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "结束循环条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ]
        }

        # 步骤循环
        {
            "循环类型": "步骤",
            "步骤选择": "表格取数",
            "循环变量名称": "ki",
            "赋值方式": "替换"
        }
        """

        if self.common_tree:
            option_iframe_xpath = "//iframe[contains(@src,'operateNodeCircle.html')]"
        else:
            option_iframe_xpath = "//iframe[contains(@src,'crawlerOperateCircle.html')]"
        # 切换到循环配置iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, option_iframe_xpath))

        if where == 1:
            iframe_xpath_list = [get_global_var("NodeIframe"), get_global_var("CrawlerIframe"), option_iframe_xpath]
        elif where == 2:
            iframe_xpath_list = [get_global_var("NodeIframe"), get_global_var("ControlIframe")]
        else:
            iframe_xpath_list = [get_global_var("NodeIframe"), get_global_var("OptIframe"), option_iframe_xpath]

        # 循环类型
        if loop_type:
            elements = self.browser.find_elements(By.XPATH, "//*[@name='looptype']/..//*[text()='{0}']".format(loop_type))
            for e in elements:
                if e.is_displayed():
                    e.click()
                    sleep(1)
                    break
            log.info("选择循环类型: {0}".format(loop_type))
            sleep(1)

        if loop_type == "变量列表":
            # 按变量列表循环
            var_loop(mode=loop_info.get("模式"), var_name=loop_info.get("变量选择"),
                     loop_var_name=loop_info.get("循环行变量名称"), value_type=loop_info.get("赋值方式"))

        elif loop_type == "次数":
            # 按次数循环
            times_loop(loop_times=loop_info.get("循环次数"), loop_var_name=loop_info.get("循环变量名称"),
                       value_type=loop_info.get("赋值方式"), next_condition=loop_info.get("跳至下一轮条件"),
                       end_condition=loop_info.get("结束循环条件"), common_tree=self.common_tree,
                       iframe_xpath_list=iframe_xpath_list)

        elif loop_type == "条件":
            # 按条件循环
            condition_loop(cir_condition=loop_info.get("循环条件"), next_condition=loop_info.get("跳至下一轮条件"),
                           end_condition=loop_info.get("结束循环条件"), common_tree=self.common_tree,
                           iframe_xpath_list=iframe_xpath_list)

        elif loop_type == "步骤":
            # 按步骤循环
            step_loop(step_name=loop_info.get("步骤选择"), cir_var_name=loop_info.get("循环变量名称"),
                      value_type=loop_info.get("赋值方式"))

        # 非法循环类型
        else:
            raise KeyError("循环类型: {0} 输入非法".format(loop_type))

        # 保存循环
        if self.common_tree:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveCircleInfo()']//*[text()='保存']").click()
        else:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveFetchCircleInfos()']//*[text()='保存']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("保存循环成功")
        else:
            log.warning("保存循环失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

        if where == 1:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到业务配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("CrawlerIframe")))
        elif where == 2:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到控制配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("ControlIframe")))
        else:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))

        return True

    def add_step(self, steps):
        """
        :param steps: 步骤名称, 数组
        :return: 连续勾选多个步骤，点击保存

        {
            "对象": "操作",
            "右键操作": "添加步骤",
            "元素名称": ["休眠", "点击按钮", "表格取数"]
        }
        """
        # 切换到选择步骤iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerOperateSteps.html')]"))
        sleep(1)

        for s in steps:
            self.browser.find_element(By.XPATH, "//*[@name='stepName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='stepName']/preceding-sibling::input").send_keys(s)
            self.browser.find_element(By.XPATH, "//*[@data-dg-query='#query_steps_tab']//*[text()='查询']").click()
            sleep(2)
            page_wait()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'query_steps')]//*[@field='elementName']//*[text()='{0}']".format(s)).click()
            self.browser.find_element(By.XPATH, "//*[@onclick='saveChooseStep();']//*[text()='保存']").click()

            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("添加步骤 {0} 成功".format(s))
            else:
                log.warning("添加步骤失败，失败提示: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)

            # 切换到节点iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/crawlerNode.html?')]"))
            # 切换到业务配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='busi_crawler_node']"))
            # 切换到选择步骤iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'crawlerOperateSteps.html')]"))
        # 添加步骤完成后，返回上层iframe
        self.browser.switch_to.parent_frame()

        return True

    def bind_subprocess(self, subprocess_name, create_begin_time, create_end_time, cond):
        """
        :param subprocess_name: 子流程名称
        :param create_begin_time: 创建开始时间
        :param create_end_time: 创建结束时间
        :param cond: 条件，数组

        # 绑定子流程
        "条件": [
                    ["变量", "时间"],
                    ["不等于", ""],
                    ["空值", ""],
                    ["与", ""],
                    ["变量", "地点"],
                    ["包含", ""],
                    ["自定义值", "abc ddd"]
                ]

        {
            "子流程名称": "pw子流程带区块",
            "创建开始时间": "2020-09-01",
            "创建结束时间": "2020-09-02"
            "条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ]
        }
        """
        # 切换到子流程iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateNodeChild.html')]"))

        # 点击绑定子流程
        self.browser.find_element(
            By.XPATH, "//*[@id='addQuickdiv']/*[@onclick='addSubProcess();']/*[text()='绑定子流程']").click()
        page_wait()
        sleep(1)

        # 进入操作子流程iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateSubprocess.html')]"))

        # 等待页面加载
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
        page_wait()

        # 子流程名称
        if subprocess_name:
            self.browser.find_element(
                By.XPATH, "//*[@name='keyword']/preceding-sibling::input").send_keys(subprocess_name)
            log.info("设置子流程名称: {0}".format(subprocess_name))
            sleep(1)

        # 创建开始时间
        if create_begin_time:
            self.browser.find_element(By.XPATH, "//*[@name='createTime']/preceding-sibling::span[1]/a").click()
            log.info("设置创建开始时间: {0}".format(create_begin_time))
            set_calendar(date_s=create_begin_time)
            sleep(1)

        # 创建结束时间
        if create_end_time:
            self.browser.find_element(By.XPATH, "//*[@name='endTime']/preceding-sibling::span[1]/a").click()
            log.info("设置创建结束时间: {0}".format(create_end_time))
            set_calendar(date_s=create_end_time)
            sleep(1)

        # 查询
        self.browser.find_element(By.XPATH, "//*[@data-dg-query='#process_info_tab']//*[text()='查询']").click()
        page_wait()

        # 选择子流程
        self.browser.find_element(
            By.XPATH, "//*[contains(@id,'process_info_tab')]/*[@field='processName']//*[text()='{0}']".format(
                subprocess_name)).click()
        log.info("选择子流程: {0}".format(subprocess_name))

        # 点击保存
        self.browser.find_element(By.XPATH, "//*[@id='save_process_button']//*[text()='保存']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("子流程 {0} 绑定成功".format(subprocess_name))
            result = True
        else:
            log.warning("子流程 {0} 绑定失败，失败提示: {1}".format(subprocess_name, msg))
            result = False
        set_global_var("ResultMsg", msg, False)

        if result:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))
            # 切换到子流程iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateNodeChild.html')]"))

            # 条件
            if cond:
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@onclick=\"showAdd('subProCnd');\"]//*[text()='修改']")))
                self.browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('subProCnd');\"]//*[text()='修改']").click()
                log.info("绑定子流程设置条件")
                sub_process_iframe = "//iframe[contains(@src,'operateNodeChild.html')]"
                iframe_xpath_list = [get_global_var("NodeIframe"), get_global_var("OptIframe"), sub_process_iframe]
                condition(array=cond, iframe_xpath_list=iframe_xpath_list)

        return result

    def add_subprocess(self, process_name, field, process_type, process_desc, except_abort, cond):
        """
        :param process_name: 流程名称
        :param field: 专业领域，字典
        :param process_type: 流程类型
        :param process_desc: 流程说明
        :param except_abort: 节点异常终止流程，bool
        :param cond: 条件，数组

        # 添加子流程
        "条件": [
                    ["变量", "时间"],
                    ["不等于", ""],
                    ["空值", ""],
                    ["与", ""],
                    ["变量", "地点"],
                    ["包含", ""],
                    ["自定义值", "abc ddd"]
                ]
        {
            "流程名称":  "pw自动化测试子流程",
            "专业领域":  "AiSee,CS域",
            "流程类型":  "子流程",
            "流程说明":  "pw自动化测试子流程说明",
            "节点异常终止流程": "是",
            "条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "地点"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ]
        }
        """
        # 切换到子流程iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateNodeChild.html')]"))

        # 点击添加子流程
        self.browser.find_element(
            By.XPATH, "//*[@id='addQuickdiv']/*[@onclick='createChildProcess();']/*[text()='添加子流程']").click()
        sleep(1)

        # 进入添加子流程iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'../processInfoEdit.html')]"))

        # 等待页面加载
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='process_name']/preceding-sibling::input")))

        # 流程名称
        if process_name:
            process_name = process_name + '_' + datetime.now().strftime('%Y%m%d%H%M%S')
            self.browser.find_element(
                By.XPATH, "//*[@name='process_name']/preceding-sibling::input").send_keys(process_name)
            log.info("设置子流程名称: {0}".format(process_name))

        # 专业领域
        if field:
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            page_wait()
            sleep(1)
            for f in field:
                self.browser.find_element(
                    By.XPATH, "//*[contains(@id,'temp_type_id') and text()='{0}']".format(f)).click()
            self.browser.find_element(
                By.XPATH, "//*[contains(text(),'专业领域')]/../following-sibling::div[1]/div/span").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 流程类型
        if process_type:
            combobox = self.browser.find_element(By.XPATH, "//*[@name='processTypeId']/preceding-sibling::input")
            self.browser.execute_script("arguments[0].click();", combobox)
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'processTypeId') and text()='{0}']".format(process_type)).click()
            log.info("设置流程类型: {0}".format(process_type))

        # 流程说明
        if process_desc:
            self.browser.find_element(
                By.XPATH, "//*[@name='re_mark']/preceding-sibling::textarea").send_keys(process_desc)
            log.info("设置流程说明: {0}".format(process_desc))

        # 节点异常终止流程
        if except_abort:
            log.info("开启【节点异常终止流程】")
        else:
            self.browser.find_element(By.XPATH, "//*[@id='isNodeExpEnd']").click()
            log.info("关闭【节点异常终止流程】")

        # 点击提交
        self.browser.find_element(By.XPATH, "//*[contains(@href,'submitForm()')]//*[text()='提交']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("子流程 {0} 添加成功".format(process_name))
            result = True
        else:
            log.warning("子流程 {0} 添加失败，失败提示: {1}".format(process_name, msg))
            result = False
        set_global_var("ResultMsg", msg, False)

        if result:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))
            # 切换到子流程iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateNodeChild.html')]"))

            # 条件
            if cond:
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[@onclick=\"showAdd('subProCnd');\"]//*[text()='修改']")))
                self.browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('subProCnd');\"]//*[text()='修改']").click()
                log.info("添加子流程设置条件")
                sub_process_iframe = "//iframe[contains(@src,'operateNodeChild.html')]"
                iframe_xpath_list = [get_global_var("NodeIframe"), get_global_var("OptIframe"), sub_process_iframe]
                condition(array=cond, iframe_xpath_list=iframe_xpath_list)

        return result

    def copy(self):
        """
        # 点击复制后，操作成功，复制一条操作
        :return: 点击
        """
        # 弹出删除二次确认框
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("操作复制成功")
        else:
            log.warning("操作复制失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

        # 切到节点iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
        # 切到操作配置iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))

        return True

    def delete(self):
        """
        # 点击删除后，先弹出删除二次确认，点击确认后，删除成功
        :return: 点击
        """
        # 弹出删除二次确认框
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除", auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("步骤从操作树删除成功")
                result = True
            else:
                log.warning("步骤从操作树删除失败，失败提示: {0}".format(msg))
                result = False
            set_global_var("ResultMsg", msg, False)
        else:
            log.warning("步骤从操作树删除失败，失败提示: {0}".format(msg))
            result = False
        set_global_var("ResultMsg", msg, False)

        if result:
            if self.common_tree:
                # 切换到节点iframe
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                # 切换到操作配置iframe
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))
            else:
                # 切换到节点iframe
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                # 切换到业务配置iframe
                self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("CrawlerIframe")))

        return result
