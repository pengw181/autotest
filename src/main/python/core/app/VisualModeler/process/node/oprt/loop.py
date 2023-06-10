# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/11/9 下午4:54

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.main.python.core.app.VisualModeler.process.node.oprt.condition import set_condition
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.input import set_text_enable_var
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def var_loop(mode, var_name, loop_var_name, value_type, var_type="指令输出变量"):
    """
    :param mode: 模式
    :param var_type: 变量类型
    :param var_name: 变量选择
    :param loop_var_name: 循环行变量名称
    :param value_type: 赋值方式

    # 按变量列表循环
    """
    browser = gbl.service.get("browser")
    # 选择模式
    if mode:
        if mode == "自定义模式":
            browser.find_element(By.XPATH, "//*[@id='listBtn_mode1']").click()
        else:
            browser.find_element(By.XPATH, "//*[@id='listBtn_mode2']").click()
            # 选择变量类型,目前固定为指令输出变量
            if var_type:
                browser.find_element(By.XPATH, "//*[@name='vartype']/preceding-sibling::input").click()
                browser.find_element(By.XPATH, "//*[contains(@id,'vartype') and text()='{0}']".format(var_type)).click()
        log.info("设置模式: {0}".format(mode))
        sleep(1)

    # 选择变量
    if var_name:
        elements = browser.find_elements(By.XPATH, "//*[contains(text(),'变量选择')]/..//following-sibling::div//a")
        # 点击选择变量
        for e in elements:
            if e.is_displayed():
                e.click()
                break
        choose_var(var_name=var_name)
        log.info("设置变量: {0}".format(var_name))
        sleep(1)

    # 循环行变量名称
    if loop_var_name:
        elements = browser.find_elements(By.XPATH, "//*[@name='outVarName']/preceding-sibling::input")
        for e in elements:
            if e.is_displayed():
                e.clear()
                e.send_keys(loop_var_name)
                log.info("设置循环行变量名称: {0}".format(loop_var_name))
                sleep(1)
                break

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break


def times_loop(loop_times, loop_var_name, value_type, next_condition, end_condition, common_tree, iframe_xpath_list):
    """
    :param loop_times: 循环次数
    :param loop_var_name: 循环变量名称
    :param value_type: 赋值方式
    :param next_condition: 跳至下一轮条件，数组
    :param end_condition: 结束循环条件，数组
    :param common_tree: bool
    :param iframe_xpath_list: 数组

    # 按次数循环
    """
    browser = gbl.service.get("browser")
    # 循环次数
    if loop_times:
        input_xpath = "//*[@id='cir_times']/following-sibling::span/input[1]"
        set_text_enable_var(input_xpath=input_xpath, msg=loop_times)
        log.info("设置循环次数: {0}".format(loop_times))
        sleep(1)

    # 循环变量名称
    if loop_var_name:
        browser.find_element(By.XPATH, "//*[@name='outVarName_2']/preceding-sibling::input").send_keys(loop_var_name)
        log.info("设置循环变量名称: {0}".format(loop_var_name))
        sleep(1)

    # 跳至下一轮条件
    if next_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('times_nextCondition');\"]").click()
        else:
            browser.find_element(
                By.XPATH, "//*[@onclick=\"showAdd('times_nextCondition','1');\"]").click()
        set_condition(array=next_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 结束循环条件
    if end_condition:
        if common_tree:
            elements = browser.find_elements(
                By.XPATH, "//*[@onclick=\"showAdd('times_endCondition');\"]")
            for element in elements:
                if element.is_displayed():
                    element.click()
                    break
        else:
            elements = browser.find_elements(
                By.XPATH, "//*[@onclick=\"showAdd('times_endCondition','1');\"]")
            for element in elements:
                if element.is_displayed():
                    element.click()
                    break
        set_condition(array=end_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 赋值方式
    # 由于设置条件会自动保存，会将赋值方式重置为"替换"，所以将赋值方式放到最后配置
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break
                break


def condition_loop(cir_condition, next_condition, end_condition, common_tree, iframe_xpath_list):
    """
    :param cir_condition: 跳至下一轮条件，数组
    :param next_condition: 结束循环条件，数组
    :param end_condition: 结束循环条件
    :param common_tree: bool
    :param iframe_xpath_list: 数组

    # 按条件循环
    """
    browser = gbl.service.get("browser")
    # 循环条件
    if cir_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('circleCondition');\"]").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('circleCondition','1');\"]").click()
        set_condition(array=cir_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 跳至下一轮条件
    if next_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('nextCondition');\"]").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('nextCondition','1');\"]").click()
        set_condition(array=next_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)

    # 结束循环条件
    if end_condition:
        if common_tree:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('endCondition');\"]").click()
        else:
            browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('endCondition','1');\"]").click()
        set_condition(array=end_condition, iframe_xpath_list=iframe_xpath_list)
        sleep(1)


def step_loop(step_name, cir_var_name, value_type):
    """
    :param step_name: 步骤选择
    :param cir_var_name: 循环变量名称
    :param value_type: 赋值方式

    # 按步骤循环
    """
    browser = gbl.service.get("browser")
    # 步骤选择
    if step_name:
        browser.find_element(By.XPATH, "//*[@id='chooseStepName']/following-sibling::span//a").click()
        # 切换到选择步骤iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'stepList.html?')]"))
        # 等待页面加载
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='stepName']/preceding-sibling::input")))
        # 查询步骤名称
        browser.find_element(By.XPATH, "//*[@name='stepName']/preceding-sibling::input").send_keys(step_name)
        browser.find_element(By.XPATH, "//*[@data-dg-query='#query_steps_tab']").click()
        page_wait()
        browser.find_element(By.XPATH, "//*[contains(@id,'query_steps')]//*[text()='{0}']".format(step_name)).click()
        # 点击保存
        browser.find_element(By.XPATH, "//*[@onclick='saveChooseStepCondition();']").click()
        log.info("选择步骤: {0}".format(step_name))
        sleep(1)
        # 切换到步骤循环iframe
        browser.switch_to.parent_frame()

    # 循环变量名称
    if cir_var_name:
        browser.find_element(By.XPATH, "//*[@name='circleVarName_Step']/preceding-sibling::input").send_keys(cir_var_name)
        log.info("设置循环变量名称: {0}".format(cir_var_name))
        sleep(1)

    # 赋值方式
    if value_type:
        elements = browser.find_elements(By.XPATH, "//*[@name='valueType']/preceding-sibling::input")
        for e1 in elements:
            if e1.is_displayed():
                e1.click()
                elements = browser.find_elements(
                    By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(value_type))
                for e2 in elements:
                    if e2.is_displayed():
                        e2.click()
                        log.info("设置赋值方式: {0}".format(value_type))
                        sleep(1)
                        break


def fetch_by_col(where, loop_fetch, fetch_cols_list):
    """
    # 爬虫节点业务配置的变量循环没有按列取数，所以只考虑控制配置、操作配置
    :param where: 2: 控制配置 3: 操作配置
    :param loop_fetch: 是否按列取数，开启/关闭
    :param fetch_cols_list: 取数配置，数组

    {
        "状态": "开启",
        "取数配置": [
            {
                "变量名称": "",
                "赋值方式": "",
                "数据索引": ""
            },
            {
                "变量名称": "",
                "赋值方式": "",
                "数据索引": ""
            }
        ]
    }
    """
    browser = gbl.service.get("browser")
    js = 'return "$("#is_getValueByCol")[0].checked;"'
    status = browser.execute_script(js)
    temp = True if loop_fetch == "开启" else False

    if status ^ temp:
        browser.find_element(By.XPATH, "//*[@id='is_getValueByCol']").click()
        log.info("{}按列取数".format(loop_fetch))
    if temp:
        for col in fetch_cols_list:
            var_name = col.get("变量名称")
            value_type = col.get("赋值方式")
            arr_index = col.get("数据索引")
            page_wait()
            browser.find_element(By.XPATH, "//*[@id='addCircleGetInfo();']").click()
            panel_xpath = getPanelXpath()

            # 变量名称
            if var_name:
                browser.find_element(
                    By.XPATH, panel_xpath + "//*[@id='ctrlvarName']/following-sibling::span/input[1]").clear()
                browser.find_element(
                    By.XPATH, panel_xpath + "//*[@id='ctrlvarName']/following-sibling::span/input[1]").send_keys(var_name)
                log.info("按列取数设置变量名称: {}".format(var_name))

            # 赋值方式
            if value_type:
                browser.find_element(By.XPATH, panel_xpath + "//*[@id='valuetype']/following-sibling::span//a").click()
                panel_xpath = getPanelXpath()
                browser.find_element(By.XPATH, panel_xpath + "//*[text()='{}']".format(value_type)).click()
                log.info("按列取数设置赋值方式: {}".format(value_type))

            # 数据索引
            if arr_index:
                browser.find_element(
                    By.XPATH, panel_xpath + "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").clear()
                browser.find_element(
                    By.XPATH, panel_xpath + "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").send_keys(
                    arr_index)
                log.info("按列取数设置数据索引: {}".format(arr_index))

            # 保存
            browser.find_element(By.XPATH, panel_xpath + "//*[@onclick='addCircleColumnVar()']").click()
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("添加按列取数变量成功")

                if where == 2:
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                    # 切换到控制配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("ControlIframe")))
                else:
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                    # 切换到操作配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
            else:
                log.warning("添加按列取数变量失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)


class LoopAdvance:
    """
    1、循环里的按列取数
    2、高级配置，循环日志参数
    """
    def __init__(self, where):
        """
        :param where: 2: 控制配置 3: 操作配置
        """
        self.browser = gbl.service.get("browser")
        self.where = where

    def get_value_by_col(self, loop_fetch, fetch_cols_list):
        """
        # 爬虫节点业务配置的变量循环没有按列取数，所以只考虑控制配置、操作配置
        :param loop_fetch: 是否开启按列取数，开启/关闭
        :param fetch_cols_list: 变量列表

        {
            "状态": "开启",
            "取数配置": [
                {
                    "变量名称": "",
                    "赋值方式": "",
                    "数据索引": ""
                },
                {
                    "变量名称": "",
                    "赋值方式": "",
                    "数据索引": ""
                },
                {
                    "操作": "修改",
                    "目标变量": "",
                    "变量名称": "",
                    "赋值方式": "",
                    "数据索引": ""
                },
                {
                    "操作": "删除",
                    "目标变量": ""
                }
            ]
        }
        """
        page_wait()
        if self.where == 2:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
            # 切换到控制配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("ControlIframe")))
        else:
            # 切换到节点iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))

        # 获取是否按列取数勾选状态
        js = 'return $("#is_getValueByCol")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【是否按列取数】勾选状态: {0}".format(status))
        if loop_fetch not in ["开启", "关闭"]:
            raise KeyError("状态 值错误")
        temp = True if loop_fetch == "开启" else False
        if temp ^ status:
            self.browser.find_element(By.XPATH, "//*[@id='is_getValueByCol']").click()
            sleep(1)
        log.info("【是否按列取数】{0}".format(loop_fetch))
        page_wait(3)

        # 变量列表
        if fetch_cols_list:
            if not isinstance(fetch_cols_list, list):
                raise TypeError("变量列表格式错误")
            for var_info in fetch_cols_list:
                # 循环得到变量配置
                if not isinstance(var_info, dict):
                    raise TypeError("变量配置格式错误")
                opt_type = var_info.get("操作")
                obj_var = var_info.get("目标变量")
                var_name = var_info.get("变量名称")
                value_type = var_info.get("赋值方式")
                array_index = var_info.get("数据索引")

                opt_type = "添加" if opt_type is None else opt_type
                if opt_type == "添加":
                    # 点击添加
                    self.browser.find_element(By.XPATH, "//*[@onclick='addCtrlGetInfo();']").click()
                    sleep(1)
                    self._col_var_page(var_name=var_name, value_type=value_type, arr_index=array_index)
                else:
                    # 目标变量
                    if not obj_var:
                        raise AttributeError("操作类型为{0}时，需要指定目标变量".format(opt_type))
                    self.browser.find_element(By.XPATH, "//*[@field='varName']/*[text()='{0}']".format(obj_var)).click()

                    if opt_type == "修改":
                        # 点击修改
                        self.browser.find_element(By.XPATH, "//*[@onclick='edit_ctrcfg_var();']").click()
                        self._col_var_page(var_name=var_name, value_type=value_type, arr_index=array_index)
                    else:
                        # 点击删除
                        self.browser.find_element(By.XPATH, "//*[@onclick='delete_ctrcfg_var();']").click()
                        alert = BeAlertBox(back_iframe="default")
                        msg = alert.get_msg()
                        if alert.title_contains("您确定需要删除{0}吗".format(obj_var), auto_click_ok=False):
                            alert.click_ok()
                            alert = BeAlertBox(back_iframe=False)
                            msg = alert.get_msg()
                            if alert.title_contains("操作成功"):
                                log.info("【按列取数】设置变量成功")
                                if self.where == 2:
                                    # 切换到节点iframe
                                    self.browser.switch_to.frame(
                                        self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                                    # 切换到控制配置iframe
                                    self.browser.switch_to.frame(
                                        self.browser.find_element(By.XPATH, gbl.service.get("ControlIframe")))
                                else:
                                    # 切换到节点iframe
                                    self.browser.switch_to.frame(
                                        self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                                    # 切换到操作配置iframe
                                    self.browser.switch_to.frame(
                                        self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
                            else:
                                log.warn("【按列取数】删除变量失败，失败提示: {0}".format(msg))
                        else:
                            log.warn("【按列取数】删除变量失败，失败提示: {0}".format(msg))
                        gbl.temp.set("ResultMsg", msg)

        # 保存循环
        self.save()

    def _col_var_page(self, var_name, value_type, arr_index):
        """
        # 按列取数页面
        :param var_name: 变量名称
        :param value_type: 赋值方式
        :param arr_index: 数据索引
        """
        panel_xpath = getPanelXpath()

        # 变量名称
        if var_name:
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[@id='ctrlvarName']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[@id='ctrlvarName']/following-sibling::span/input[1]").send_keys(var_name)
            log.info("按列取数设置变量名称: {}".format(var_name))

        # 赋值方式
        if value_type:
            self.browser.find_element(By.XPATH, panel_xpath + "//*[@id='valuetype']/following-sibling::span//a").click()
            type_panel_xpath = getPanelXpath()
            self.browser.find_element(By.XPATH, type_panel_xpath + "//*[text()='{}']".format(value_type)).click()
            log.info("按列取数设置赋值方式: {}".format(value_type))

        # 数据索引
        if arr_index:
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, panel_xpath + "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").send_keys(
                arr_index)
            log.info("按列取数设置数据索引: {}".format(arr_index))

        # 保存
        if self.where == 2:
            self.browser.find_element(By.XPATH, "//*[@onclick='addColumnVar()']").click()
        else:
            self.browser.find_element(By.XPATH, "//*[@onclick='addCircleColumnVar()']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("【按列取数】设置变量成功")
            if self.where == 2:
                # 切换到节点iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                # 切换到控制配置iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(By.XPATH, gbl.service.get("ControlIframe")))
            else:
                # 切换到节点iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                # 切换到操作配置iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
        else:
            log.warn("【按列取数】设置变量失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def advance_cfg(self, save_log, record_cycle_num, log_print_ruler):
        """
        # 高级配置
        :param save_log: 是否记录循环日志，是/否
        :param record_cycle_num: 循环日志记录条数
        :param log_print_ruler: 输出日志打印规则
        """
        if self.where == 2:
            # 切换到节点iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
            # 切换到控制配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, gbl.service.get("ControlIframe")))
        else:
            # 切换到节点iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
            # 切换到操作配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, gbl.service.get("OptIframe")))
        # 展开高级配置
        advance_element = self.browser.find_element(By.XPATH, "//*[@id='adv_btn']")
        expander_flag = advance_element.get_attribute("class")
        if expander_flag.find("expander") == -1:
            # 点击箭头展开
            advance_element.click()
            sleep(1)

        # 获取是否记录循环日志勾选状态
        js = 'return $("#is_addLog")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【是否按列取数】勾选状态: {0}".format(status))
        if save_log:
            if save_log not in ["是", "否"]:
                raise KeyError("状态 值错误")
            temp = True if save_log == "是" else False
            if temp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='is_addLog']").click()
                sleep(1)
            log.info("【是否记录循环日志】{0}".format(save_log))
            page_wait(3)

        # 循环日志记录条数
        if record_cycle_num:
            self.browser.find_element(
                By.XPATH, "//*[@id='recordCycleNum']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='recordCycleNum']/following-sibling::span/input[1]").send_keys(record_cycle_num)
            log.info("设置循环日志记录条数: {0}".format(record_cycle_num))

        # 循环日志记录条数
        if log_print_ruler:
            self.browser.find_element(
                By.XPATH, "//*[@id='outputLogPrintRuler']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='outputLogPrintRuler']/following-sibling::span/input[1]").send_keys(log_print_ruler)
            log.info("设置循环日志记录条数: {0}".format(log_print_ruler))

        # 点击保存
        self.save()

    def save(self):
        if self.where == 2:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveCtrlCfgCondition()']").click()
        else:
            self.browser.find_element(By.XPATH, "//*[@onclick='saveCircleInfo()']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("设置成功")
        else:
            log.warn("【设置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)
