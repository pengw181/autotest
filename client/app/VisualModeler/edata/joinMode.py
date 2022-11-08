# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/21 下午4:02

from time import sleep
from client.page.func.alertBox import BeAlertBox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from service.lib.log.logger import log
from service.lib.variable.globalVariable import *


class JoinModeEData:
    # 合并模式

    def __init__(self, eData_iframe_xpath, tab_xpath):
        """
        :param eData_iframe_xpath:
        :param tab_xpath:
        """
        self.browser = get_global_var("browser")
        self.eData_iframe_xpath = eData_iframe_xpath
        self.tab_xpath = tab_xpath

    def add_join_table(self, join_table_list, join_type, left_table_set, right_table_set, new_table_name, field,
                       new_table_set):
        """
        :param join_table_list: 合并表名称，数组
        :param join_type: 关联方式，左关联/右关联
        :param left_table_set: 左表配置，数组
        :param right_table_set: 右表配置，数组
        :param new_table_name: 数据表名称
        :param field: 专业领域，数组
        :param new_table_set: 新表配置，数组

        {
            "合并表名称": ["", ""],
            "关联方式": "左关联",
            "左表配置": [
                {
                    "列名": "网元名称",
                    "合并后显示": "是",
                    "关联列": "1"
                },
                {
                    "列名": "指令内容",
                    "合并后显示": "是"
                },
                {
                    "列名": "列1",
                    "合并后显示": "是"
                },
                {
                    "列名": "列2",
                    "合并后显示": "是"
                },
                {
                    "列名": "列3",
                    "合并后显示": "是"
                }
            ],
            "右表配置": [
                {
                    "列名": "网元名称",
                    "合并后显示": "否",
                    "关联列": "1"
                },
                {
                    "列名": "列1",
                    "合并后显示": "是"
                }
            ],
            "数据表名称": "pw合并模式join",
            "专业领域": ["", ""],
            "新表配置": [
                {
                    "表名": "pw二维表模式",
                    "原列名": "网元名称",
                    "新列名": "网元名称",
                    "搜索条件": "是"
                },
                {
                    "表名": "pw二维表模式",
                    "原列名": "指令内容",
                    "新列名": "指令内容",
                    "搜索条件": "是"
                },
                {
                    "表名": "pw二维表模式",
                    "原列名": "列2",
                    "新列名": "列2",
                    "搜索条件": "是"
                },
                {
                    "表名": "pw二维表模式",
                    "原列名": "列3",
                    "新列名": "列3",
                    "搜索条件": "是"
                },
                {
                    "表名": "pw列更新模式",
                    "原列名": "列1",
                    "新列名": "列1",
                    "搜索条件": "是"
                }
            ]
        }

        """
        log.info("开始添加join模式")
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-addJoin']").click()
        # 进入表配置页面iframe
        join_mode_iframe_xpath = "//iframe[contains(@src,'/VisualModeler/html/edata/joinmode/joinModeTmplEditWin.html')]"
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, join_mode_iframe_xpath)))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]")))

        # 合并表名称
        if join_table_list:
            for table_name in join_table_list:
                self.browser.find_element(By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]").send_keys(table_name)
                self.browser.find_element(
                    By.XPATH, "//*[@id='table_info']//span[text()='{0}']".format(table_name)).click()
                log.info("选择合并表: {0}".format(table_name))
                sleep(1)

        # 划到第二步
        step_element = self.browser.find_element(By.XPATH, "//*[@id='leftJoin']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", step_element)
        sleep(1)

        # 关联方式
        if join_type:
            if join_type == "左关联":
                self.browser.find_element(By.XPATH, "//*[@id='leftJoin']").click()
            else:
                self.browser.find_element(By.XPATH, "//*[@id='rightJoin']").click()
            log.info("设置关联方式: {0}".format(join_type))

        # 左表配置
        if left_table_set:
            for col_set in left_table_set:
                if not isinstance(col_set, dict):
                    raise AttributeError("格式错误，必须是字典")

                # 列名
                if col_set.__contains__("列名"):
                    col_name = col_set.get("列名")
                else:
                    raise AttributeError("未指定列名")

                # 合并后展示
                if col_set.__contains__("合并后显示"):
                    show_col = col_set.get("合并后显示")
                    if show_col == "是":
                        self.browser.find_element(
                            By.XPATH, "//*[@id='leftTable']//*[text()='{0}']/../following-sibling::td[2]".format(
                                col_name)).click()

                # 关联列
                if col_set.__contains__("关联列"):
                    add_on = col_set.get("关联列")
                    self.browser.find_element(
                        By.XPATH, "//*[@id='leftTable']//*[text()='{0}']/../following-sibling::td[3]//a".format(
                            col_name)).click()
                    on_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(add_on))
                    if len(on_elements) > 0:
                        for element in on_elements:
                            if element.is_displayed():
                                element.click()
                                break
                    else:
                        raise KeyError("【{0}】列无法配置关联列【{1}】".format(col_name, add_on))

                    log.info("【{0}】列配置完成".format(col_name))
                    sleep(1)

            log.info("左配置完成")

        # 右表配置
        if right_table_set:
            for col_set in right_table_set:
                if not isinstance(col_set, dict):
                    raise AttributeError("格式错误，必须是字典")

                # 列名
                if col_set.__contains__("列名"):
                    col_name = col_set.get("列名")
                else:
                    raise AttributeError("未指定列名")

                # 合并后展示
                if col_set.__contains__("合并后显示"):
                    show_col = col_set.get("合并后显示")
                    if show_col == "是":
                        self.browser.find_element(
                            By.XPATH, "//*[@id='rightTable']//*[text()='{0}']/../following-sibling::td[2]".format(
                                col_name)).click()

                # 关联列
                if col_set.__contains__("关联列"):
                    add_on = col_set.get("关联列")
                    self.browser.find_element(
                        By.XPATH, "//*[@id='rightTable']//*[text()='{0}']/../following-sibling::td[3]//a".format(
                            col_name)).click()
                    on_elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'combobox') and text()='{0}']".format(add_on))
                    if len(on_elements) > 0:
                        for element in on_elements:
                            if element.is_displayed():
                                element.click()
                                break
                    else:
                        raise KeyError("【{0}】列无法配置关联列【{1}】".format(col_name, add_on))

                log.info("【{0}】列配置完成".format(col_name))
                sleep(1)
            log.info("右表配置完成")

        # 点击确定已选关系
        self.browser.find_element(By.XPATH, "//*[@id='join-confirmRel']").click()
        sleep(1)
        # 划到第三步
        step_element = self.browser.find_element(By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", step_element)
        sleep(1)

        # 数据表名称
        if new_table_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(new_table_name)
            log.info("设置数据表名称: {0}".format(new_table_name))

        # 专业领域
        if field:
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeId']/following-sibling::span//a").click()
            sleep(1)
            # 判断当前是否已经选择了专业领域，如果是，则先取消
            choose_field_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'tempTypeId') and contains(@class,'selected')]")
            if len(choose_field_list) > 0:
                for cf in choose_field_list:
                    cf.click()
            # 依次选择专业领域
            for f in field:
                field_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'tempTypeId') and text()='{0}']".format(f))
                for element in field_elements:
                    if element.is_displayed():
                        element.click()
                        break
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeId']/following-sibling::span//a").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 新表配置
        if new_table_set:
            for col_set in new_table_set:
                if not isinstance(col_set, dict):
                    raise AttributeError("格式错误，必须是字典")

                # 表名
                if col_set.__contains__("表名"):
                    table_name = col_set.get("表名")
                else:
                    raise AttributeError("未指定表名")

                # 原列名
                if col_set.__contains__("原列名"):
                    old_col_name = col_set.get("原列名")
                else:
                    raise AttributeError("未指定原列名")

                # 定义辅助xpath
                row_obj_xpath = "//*[text()='{0}']/../following-sibling::td[1]/*[text()='{1}']/..".format(
                    table_name, old_col_name)

                # 新列名
                if col_set.__contains__("新列名"):
                    new_col_name = col_set.get("新列名")
                    if new_col_name != old_col_name:
                        # 修改新列名
                        new_col_ele = self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[1]")
                        new_col_ele.click()
                        self.browser.find_element(By.XPATH, "//*[@id='popup_box']/div/div/span/input[1]").clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@id='popup_box']/div/div/span/input[1]").send_keys(new_col_name)
                        self.browser.find_element(By.XPATH, "//*[@onclick='confirmBox($(this))']").click()
                        log.info("设置新列名: {0}".format(new_col_name))

                        # 移动鼠标，消除"新列名"tips遮挡
                        action = ActionChains(self.browser)
                        action.move_to_element(new_col_ele).perform()

                        # 修改新列名，会自动勾选"搜索条件"，先勾掉
                        self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[2]").click()

                # 搜索条件
                if col_set.__contains__("搜索条件"):
                    search_col = col_set.get("搜索条件")
                    if search_col == "是":
                        self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[2]").click()
                        log.info("【{0} {1}】列设置为搜索条件".format(table_name, old_col_name))
                sleep(1)
            log.info("新表配置完成")

        # 保存新表
        self.browser.find_element(By.XPATH, "//*[@id='join-save']").click()
        self.browser.switch_to.default_content()
        # 进入模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
        alert = BeAlertBox(back_iframe=False, timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(new_table_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(new_table_name, msg))
        set_global_var("ResultMsg", msg, False)

    def add_union_table(self, join_table_list, join_type, join_table_set, new_table_name, field, new_table_set):
        """
        :param join_table_list: 合并表名称，数组
        :param join_type: 关联方式，UNION/UNION ALL
        :param join_table_set: 合并表配置，数组
        :param new_table_name: 数据表名称
        :param field: 专业领域，数组
        :param new_table_set: 新表配置，数组

        {
            "合并表名称": ["pw二维表模式", "pw数据拼盘-二维表模式"],
            "关联方式": "UNION",
            "合并表配置": [
                {
                    "表名": "pw二维表模式",
                    "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                },
                {
                     "表名": "pw数据拼盘-二维表模式",
                    "合并列": ["网元名称", "指令内容", "列1", "列2", "列3"]
                }
            ],
            "数据表名称": "pw合并模式union",
            "专业领域": ["AiSee", "auto域"],
            "新表配置": [
                {
                    "原列名": "网元名称",
                    "新列名": "网元名称",
                    "搜索条件": "是"
                },
                {
                    "原列名": "指令内容",
                    "新列名": "指令内容",
                    "搜索条件": "是"
                },
                {
                    "原列名": "列1",
                    "新列名": "列1",
                    "搜索条件": "是"
                },
                {
                    "原列名": "列2",
                    "新列名": "列2",
                    "搜索条件": "是"
                },
                {
                    "原列名": "列3",
                    "新列名": "列3",
                    "搜索条件": "是"
                }
            ]
        }

        """
        log.info("开始添加union模式")
        self.browser.find_element(By.XPATH, self.tab_xpath + "//*[@id='edata-addUnion']").click()
        # 进入表配置页面iframe
        join_mode_iframe_xpath = "//iframe[contains(@src,'/VisualModeler/html/edata/joinmode/unionModeTmplEditWin.html')]"
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, join_mode_iframe_xpath)))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]")))

        # 合并表名称
        if join_table_list:
            for table_name in join_table_list:
                self.browser.find_element(By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]").clear()
                self.browser.find_element(
                    By.XPATH, "//*[@id='tableSearch']/following-sibling::span/input[1]").send_keys(table_name)
                self.browser.find_element(
                    By.XPATH, "//*[@id='table_info']//span[text()='{0}']".format(table_name)).click()
                log.info("选择合并表: {0}".format(table_name))
                sleep(1)

        # 划到第二步
        step_element = self.browser.find_element(By.XPATH, "//*[@name='joinType' and @value ='UNION']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", step_element)
        sleep(1)

        # 关联方式
        if join_type:
            self.browser.find_element(By.XPATH, "//*[@name='joinType' and @value='{0}']".format(join_type)).click()
            log.info("设置关联方式: {0}".format(join_type))

        # 合并表配置
        if join_table_set:
            for col_set in join_table_set:
                if not isinstance(col_set, dict):
                    raise AttributeError("格式错误，必须是字典")

                # 表名
                if col_set.__contains__("表名"):
                    table_name = col_set.get("表名")
                else:
                    raise AttributeError("未指定表名")

                # 合并列
                if col_set.__contains__("合并列"):
                    union_col_list = col_set.get("合并列")
                    for col in union_col_list:
                        self.browser.find_element(
                            By.XPATH, "//*[text()='{0}']/../following-sibling::div[1]//td[text()='{1}']".format(
                                table_name, col)).click()

                    log.info("【{0}】配置完成".format(table_name))
                    sleep(1)
            log.info("合并表配置完成")

        # 点击确定已选关系
        self.browser.find_element(By.XPATH, "//*[@id='join-confirmRel']").click()
        # 划到第三步
        step_element = self.browser.find_element(By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", step_element)
        sleep(1)

        # 数据表名称
        if new_table_name:
            self.browser.find_element(By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='tableNameCh']/following-sibling::span/input[1]").send_keys(new_table_name)
            log.info("设置数据表名称: {0}".format(new_table_name))

        # 专业领域
        if field:
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeId']/following-sibling::span//a").click()
            sleep(1)
            # 判断当前是否已经选择了专业领域，如果是，则先取消
            choose_field_list = self.browser.find_elements(
                By.XPATH, "//*[contains(@id,'tempTypeId') and contains(@class,'selected')]")
            if len(choose_field_list) > 0:
                for cf in choose_field_list:
                    cf.click()
            # 依次选择专业领域
            for f in field:
                field_elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'tempTypeId') and text()='{0}']".format(f))
                for element in field_elements:
                    if element.is_displayed():
                        element.click()
                        break
            self.browser.find_element(By.XPATH, "//*[@id='tempTypeId']/following-sibling::span//a").click()
            log.info("设置专业领域: {0}".format(",".join(field)))

        # 新表配置
        if new_table_set:
            for col_set in new_table_set:
                if not isinstance(col_set, dict):
                    raise AttributeError("格式错误，必须是字典")

                # 原列名
                if col_set.__contains__("原列名"):
                    old_col_name = col_set.get("原列名")
                else:
                    raise AttributeError("未指定原列名")

                # 定义辅助xpath
                row_obj_xpath = "//*[text()='{0}']/..".format(old_col_name)

                # 新列名
                if col_set.__contains__("新列名"):
                    new_col_name = col_set.get("新列名")
                    if new_col_name != old_col_name:
                        new_col_ele = self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[1]")
                        new_col_ele.click()
                        self.browser.find_element(By.XPATH, "//*[@id='popup_box']/div/div/span/input[1]").clear()
                        self.browser.find_element(
                            By.XPATH, "//*[@id='popup_box']/div/div/span/input[1]").send_keys(new_col_name)
                        self.browser.find_element(By.XPATH, "//*[@onclick='confirmBox($(this))']").click()
                        log.info("设置新列名: {0}".format(new_col_name))

                        # 移动鼠标，消除"新列名"tips遮挡
                        action = ActionChains(self.browser)
                        action.move_to_element(new_col_ele).perform()

                        # 修改新列名，会自动勾选"搜索条件"，先勾掉
                        self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[4]").click()

                # 搜索条件
                if col_set.__contains__("搜索条件"):
                    search_col = col_set.get("搜索条件")
                    if search_col == "是":
                        self.browser.find_element(By.XPATH, row_obj_xpath + "/following-sibling::td[4]").click()
                        log.info("【{0}】列设置为搜索条件".format(old_col_name))
                sleep(1)

            log.info("新表配置完成")

        # 保存新表
        self.browser.find_element(By.XPATH, "//*[@id='join-save']").click()
        self.browser.switch_to.default_content()
        # 进入模版配置列表页面
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, self.eData_iframe_xpath))
        alert = BeAlertBox(back_iframe=False, timeout=30)
        msg = alert.get_msg()
        if alert.title_contains("保存成功"):
            log.info("{0} 添加成功".format(new_table_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(new_table_name, msg))
        set_global_var("ResultMsg", msg, False)
