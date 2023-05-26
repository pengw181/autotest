# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:29

from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.input import set_textarea
from src.main.python.lib.loadData import load_sample
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class RegularCube:
    
    def __init__(self):
        self.browser = gbl.service.get("browser")
        self.needJumpIframe = False

    def setRegular(self, set_type=None, regular_name=None, advance_mode=None, regular=None, expression=None,
                   enable_check=None, check_msg=None, confirm_selector="//*[@id='regexDiv']"):
        """
        # 用来操作正则魔方
        :param set_type: 设置方式，选择/添加, 必填
        :param regular_name: 正则模版名称，如果是在正则模版管理菜单添加，则不填
        :param advance_mode: 高级模式，是/否
        :param regular: 标签配置，设置方式为选择时，为空
        :param expression: 表达式，advance_mode为True时，必填
        :param enable_check: 开启验证，是/否
        :param check_msg: 样例数据，传文件名
        :param confirm_selector: 用来定位，推荐用id定位到父节点tr或div标签

        方式一，选择正则模版：
        {
            "设置方式": "选择",
            "正则模版名称": "pw按时间拆分",
            "开启验证": "是",
            "样例数据": "ping_sample.txt"
        }

        方式二，配置正则魔方：
        {
            "设置方式": "添加",
            "正则模版名称": "pw自动化正则模版",
            "高级模式": "否",
            "标签配置": [
                {
                    "标签": "自定义文本",
                    "自定义值": "pw",
                    "是否取值": "黄色"
                },
                {
                    "标签": "任意字符",
                    "长度": "1到多个",
                    "是否取值": "绿色"
                },
                {
                    "标签": "数字",
                    "正数负数": "正数",
                    "匹配小数": "否",
                    "匹配%": "否",
                    "匹配千分位": "否",
                    "匹配并去掉逗号": "否",
                    "长度": "1到多个",
                    "是否取值": "绿色"
                },
                {
                    "标签": "特殊字符",
                    "特殊字符": "$",
                    "长度": "1到多个",
                    "是否取值": "绿色"
                },
                {
                    "标签": "IP",
                    "IPV4": "是",
                    "IPV6": "是",
                    "是否取值": "绿色"
                }
            ],
            "开启验证": "是",
            "样例数据": "ping_sample.txt"
        }

        方式三，高级模式：
        {
            "设置方式": "添加",
            "正则模版名称": "pw自动化正则模版",
            "高级模式": "是",
            "表达式": "(pw)(.+)",
            "开启验证": "是",
            "样例数据": "ping_sample.txt"
        }
        """
        page_wait()
        sleep(1)
        # 聚焦元素
        if regular_name:
            reg_temp_name_input = self.browser.find_element(
                By.XPATH, confirm_selector + "//*[contains(@class,'regxTemplName')]/following-sibling::span/input[1]")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", reg_temp_name_input)

        log.info("开始配置正则")
        # 保存正则模版时正则模版名称是否加时间戳后缀
        attach_timestamp = True
        if set_type is None:
            set_type = "添加"

        if set_type == "选择":

            # 点击查询正则模版
            self.browser.find_element(
                By.XPATH, confirm_selector + "//*[contains(@class,'regexSearch')]/span/span[2]").click()
            page_wait()
            # 进入正则模版页面，切换iframe
            self.browser.switch_to.frame(
                self.browser.find_element(
                    By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplSelectWin.html?')]"))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='keyword']/preceding-sibling::input")))
            page_wait()
            # 输入正则模版名称
            self.browser.find_element(By.XPATH, "//*[@name='keyword']/preceding-sibling::input").send_keys(regular_name)
            # 点击查询
            self.browser.find_element(By.XPATH, "//*[@id='regexp-query']//*[text()='查询']").click()
            page_wait()
            # 勾选正则模版
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'regexpTab_datagrid-row-')]//*[text()='{0}']".format(regular_name)).click()
            # 点击确认
            self.browser.find_element(By.XPATH, "//*[@id='regexp-ok']//*[text()='确定']").click()
            # 切到上级iframe
            self.browser.switch_to.parent_frame()
            log.info("选择正则: {0}".format(regular_name))

            obj_lis = self.browser.find_elements(By.XPATH, confirm_selector + "//*[@class='tag_pool']/div/ul/li")
            obj_id_list = []
            if len(obj_lis) > 0:
                for obj in obj_lis:
                    obj_id_list.append(obj.get_attribute("obj_id"))
                log.info("从正则魔方获取标签obj_id: {0}".format(obj_id_list))
                gbl.temp.set("ObjIDs", obj_id_list)

        elif set_type == "添加":
            # 如果是选择正则魔方，needJumpIframe为false,上面会自动返回到上层iframe，调用方只需要手动关闭窗口或不做处理。
            # 如果needJumpIframe为true，通知调用方手动跳转iframe。
            self.needJumpIframe = True

            # 判断是否高级模式
            if advance_mode == "是":
                # 点击启用高级功能
                self.browser.find_element(By.XPATH, confirm_selector + "//*[contains(text(),'启用高级功能')]").click()
                # 输入表达式，\需要换成\\
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[contains(text(),'表达式')]/../../following-sibling::div[1]//*[contains(@id,'_textbox_')]").send_keys(
                    expression)
            else:
                rows = len(regular)
                log.info("需要添加{0}个标签元素".format(rows))
                action = ActionChains(self.browser)
                for tag_msg in regular:
                    tag_name = tag_msg.get("标签")
                    tag_color = tag_msg.get("是否取值")

                    # 标签类型
                    label_type = self._getLabelType(tag_name)

                    # 标签
                    tag_element_xpath = confirm_selector + "//*[@class ='label-btn' and text()='{0}']".format(tag_name)
                    tag_element = self.browser.find_element(By.XPATH, tag_element_xpath)

                    # 表达式池
                    text_element_xpath = confirm_selector + "//*[text()='标签池']/../following-sibling::div"
                    text_element = self.browser.find_element(By.XPATH, text_element_xpath)

                    # 将标签拖入表达式池
                    action.drag_and_drop(tag_element, text_element).perform()
                    sleep(1)

                    # 单击加入到标签池的新标签
                    self.browser.find_element(
                        By.XPATH, confirm_selector + "//*[@label_id='{}' and contains(@class,'current')]".format(
                            label_type)).click()

                    # 按不同类型配置标签值
                    self._setLabelAttribute(confirm_selector=confirm_selector, label_name=tag_msg.get("标签"), tag_info=tag_msg)

                    # 设置取数颜色
                    if tag_color == "黄色":
                        color_button = "yellowButton"
                    elif tag_color == "绿色":
                        color_button = "greenButton"
                    else:
                        color_button = "whiteButton"

                    # 选择标签并着色
                    if tag_name in ["任意字符", "任意中文字符", "字母", "空格", "任意非空格", "字母/数字", "特殊字符", "换行"]:
                        tag_value = tag_msg.get("长度")
                    elif tag_name == "数字":
                        if tag_msg.__contains__("匹配千分位"):
                            check1 = True if tag_msg.get("匹配千分位") == "是" else False
                        else:
                            check1 = False
                        if tag_msg.__contains__("匹配并去掉逗号"):
                            check2 = True if tag_msg.get("匹配并去掉逗号") == "是" else False
                        else:
                            check2 = False
                        if check1 or check2:
                            tag_value = "千分位数字"
                        else:
                            tag_value = tag_msg.get("长度")
                    elif tag_name == "日期":
                        tag_value = tag_msg.get("时间格式")
                    elif tag_name == "自定义文本":
                        tag_value = tag_msg.get("自定义值")
                    elif tag_name == "IP":
                        tag_value = "IPv4/IPv6"
                    elif tag_name == "开始":
                        tag_value = "开始"
                    elif tag_name == "结束":
                        tag_value = "结束"
                    else:
                        raise KeyError("正则魔方不支持的标签: {}".format(tag_name))

                    if tag_value is None:
                        raise KeyError("定位标签的属性值为空，如长度字段缺失")
                    self.browser.find_element(
                        By.XPATH, confirm_selector + "//*[@label_id='{0}' and contains(@class,'current')]//*[text()='{1}']/../following-sibling::div[1]/*[contains(@class,'{2}')]".format(
                            label_type, tag_value, color_button)).click()
                    log.info("正则标签池加入标签: {0}".format(tag_name))
                    sleep(1)

            # 是否验证
            if enable_check:
                if enable_check == "是":
                    if check_msg:
                        sample_data = load_sample(sample_file_name=check_msg)
                    else:
                        raise AttributeError("开启验证时，需要指定样例数据文件名")

                    # 输入样例数据
                    try:
                        check_textarea = self.browser.find_element(By.XPATH, "//*[@class='testDiv']/*[@class='srcText']/textarea")
                        set_textarea(check_textarea, sample_data)
                    except NoSuchElementException:
                        self.browser.find_element(By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'验证')]").click()
                        check_textarea = self.browser.find_element(By.XPATH, "//*[@class='testDiv']/*[@class='srcText']/textarea")
                        set_textarea(check_textarea, sample_data)
                    log.info("输入样例数据")

                    # 进行结果验证
                    validateBtn = self.browser.find_element(By.XPATH, "//*[@class='testDiv']/*[@class='validateBtn']")
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", validateBtn)
                    validateBtn.click()
                    page_wait()
                    # result_textarea = self.browser.find_element(By.XPATH, "//*[@class='testDiv']/*[@class='destText']/textarea")
                    # test_result = result_textarea.get_attribute("")
                else:
                    try:
                        self.browser.find_element(By.XPATH, "//*[@class='testDiv']/*[@class='srcText']/textarea")
                        self.browser.find_element(By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'验证')]").click()
                    except NoSuchElementException:
                        log.info("关闭【验证】")

            # 正则模版名称
            if regular_name:
                # 点击保存模版
                self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存模版']").click()
                # 切换到保存正则模版的iframe
                self.browser.switch_to.frame(
                    self.browser.find_element(
                        By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplSaveWin.html?')]"))
                # 输入正则模版名称，加上_时间戳
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((
                    By.XPATH, "//*[contains(text(),'模版名称')]/../following-sibling::div[1]//*[contains(@id,'_textbox_input')]")))
                if attach_timestamp:
                    regular_name = regular_name + '_' + datetime.now().strftime('%Y%m%d%H%M%S')
                gbl.service.set("RegularName", regular_name)
                self.browser.find_element(
                    By.XPATH, "//*[contains(text(),'模版名称')]/../following-sibling::div[1]//*[contains(@id,'_textbox_input')]").send_keys(
                    regular_name)
                # 点击提交
                self.browser.find_element(By.XPATH, "//*[@id='regex-save']//*[text()='提交']").click()
            else:
                # 正则模版管理不需要保存模版名称，会有其他字段来保存
                pass
        else:
            raise KeyError("正则魔方只支持 选择 和 添加")

    @staticmethod
    def _getLabelType(label_name):
        tag = {
            "任意字符": "label_char",
            "数字": "label_number",
            "自定义文本": "custom_text",
            "空格": "label_space",
            "日期": "label_date",
            "任意中文字符": "label_Ch_char",
            "字母": "label_word",
            "任意非空格": "label_not_space",
            "特殊字符": "label_special",
            "字母/数字": "label_wAndn",
            "换行": "label_wrap",
            "IP": "label_ip",
            "开始": "label_start",
            "结束": "label_end"
        }
        return tag.get(label_name)

    def _setLabelAttribute(self, confirm_selector, label_name, tag_info):
        """
        # 设置标签属性
        :param confirm_selector: 用来定位，推荐用id定位到父节点tr或div标签
        :param label_name: 标签
        :param tag_info: 标签信息

        {
            "标签": "自定义文本",
            "自定义值": "pw",
            "是否取值": "黄色"
        },
        {
            "标签": "任意字符",
            "长度": "1到多个",
            "是否取值": "绿色"
        },
        {
            "标签": "数字",
            "正数负数": "正数",
            "匹配小数": "否",
            "匹配%": "否",
            "匹配千分位": "否",
            "匹配并去掉逗号": "1到多个",
            "是否取值": "绿色"
        },
        {
            "标签": "特殊字符",
            "特殊字符": "$",
            "长度": "1到多个",
            "是否取值": "绿色"
        },
        {
            "标签": "IP",
            "IPV4": "是",
            "IPV6": "是",
            "是否取值": "绿色"
        },
        {
            "标签": "日期",
            "时间格式": "2014-05-28 12:30:00"
        }
        """

        if label_name == "自定义文本":
            if tag_info.__contains__("自定义值"):
                custom_value = tag_info.get("自定义值")
                # 输入标签值
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[contains(@id,'_textbox_')]").send_keys(
                    custom_value)

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

        elif label_name in ["任意字符", "任意中文字符", "字母", "空格", "任意非空格", "字母/数字", "换行"]:
            if tag_info.__contains__("长度"):
                length = tag_info.get("长度")
                # 点击下拉框
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[contains(@class,'combo-arrow')]").click()
                sleep(1)
                # 选择属性
                elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'easyui_combobox_') and text()='{0}']".format(length))
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        break
                sleep(1)

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

        elif label_name == "日期":
            if tag_info.__contains__("时间格式"):
                time_format = tag_info.get("时间格式")
                # 点击下拉框
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[contains(@class,'combo-arrow')]").click()
                sleep(1)
                # 选择属性
                elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'easyui_combobox_') and text()='{0}']".format(time_format))
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        break
                sleep(1)

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

        elif label_name == "数字":
            # 正数负数
            if tag_info.__contains__("正数负数"):
                positive_negative = tag_info.get("正数负数")
                if positive_negative == "正数":
                    pn_value = "p"
                elif positive_negative == "负数":
                    pn_value = "n"
                elif positive_negative == "正负数":
                    pn_value = "pn"
                else:
                    raise KeyError("标签为数字时，数字仅支持：正数、负数、正数负数，当前值为：{} ".format(positive_negative))
                self.browser.find_element(By.XPATH, "//*[@name='isPn' and @value='{}']".format(pn_value)).click()

            # 匹配小数
            if tag_info.__contains__("匹配小数"):
                if tag_info.get("匹配小数") == "是":
                    self.browser.find_element(
                        By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'匹配小数(选中将匹配小数点)')]").click()

            # 匹配小数
            if tag_info.__contains__("匹配%"):
                if tag_info.get("匹配%") == "是":
                    self.browser.find_element(
                        By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'匹配%(选中将匹配带%的数字)')]").click()

            # 匹配千分位
            if tag_info.__contains__("匹配千分位"):
                if tag_info.get("匹配千分位") == "是":
                    self.browser.find_element(
                        By.XPATH, "//*[@name='regex_comma']/../../*[contains(text(),'匹配“,”(匹配带千位分隔符“,”的数字)')]").click()

            # 匹配并去掉逗号
            if tag_info.__contains__("匹配并去掉逗号"):
                if tag_info.get("匹配并去掉逗号") == "是":
                    self.browser.find_element(
                        By.XPATH, "//*[@name='regex_comma']/../../*[contains(text(),'匹配“,”号，并去掉“,”号')]").click()

            if tag_info.__contains__("长度"):
                length = tag_info.get("长度")
                # 点击长度下拉框
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[contains(@class,'combo-arrow')]").click()
                sleep(1)

                # 选择长度属性
                elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'easyui_combobox_') and text()='{0}']".format(length))
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        break
                sleep(1)

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

        elif label_name == "特殊字符":
            if tag_info.__contains__("特殊字符"):
                # 点击特殊字符下拉框
                special_char = tag_info.get("特殊字符")
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[text()='特殊字符']/following-sibling::span//*[contains(@class,'combo-arrow')]").click()
                sleep(1)
                # 选择特殊字符
                elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'easyui_combobox_') and text()='{0}']".format(special_char))
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        break
                sleep(1)

            if tag_info.__contains__("长度"):
                # 点击长度下拉框
                length = tag_info.get("长度")
                self.browser.find_element(
                    By.XPATH, confirm_selector + "//*[text()='标签属性']/following-sibling::div//*[text()='长度']/following-sibling::span//*[contains(@class,'combo-arrow')]").click()
                sleep(1)
                # 选择特殊字符
                elements = self.browser.find_elements(
                    By.XPATH, "//*[contains(@id,'easyui_combobox_') and text()='{0}']".format(length))
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        break
                sleep(1)

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

        elif label_name == "IP":
            # IPV4
            if tag_info.__contains__("IPV4"):
                if tag_info.get("IPV4") == "否":
                    self.browser.find_element(By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'IPv4')]").click()

            # IPV6
            if tag_info.__contains__("IPV6"):
                if tag_info.get("IPV6") == "否":
                    self.browser.find_element(By.XPATH, "//*[@class='my_checkbox2' and contains(text(),'IPV6')]").click()

            # 点击保存属性
            self.browser.find_element(By.XPATH, confirm_selector + "//*[text()='保存属性']").click()

    def setAnalyze(self, begin_row=None, enable_magic=None, total_columns=None, row_split_type=None, split_tag=None,
                   magic=None, advance_conf=None, confirm_selector="//*[@id='regexptableFormatCfgDiv']"):
        """
        # 解析配置，包括配置正则魔方，高级配置，不包括样例数据
        :param begin_row: 解析开始行
        :param enable_magic: 通过正则匹配数据列，是/否
        :param total_columns: 列总数
        :param row_split_type: 拆分方式，文本/正则
        :param split_tag: 列分隔符
        :param magic: 正则魔方，开启通过正则匹配数据列或拆分方式为正则时使用
        :param advance_conf: 高级配置
        :param confirm_selector: 确定解析配置
        :return: 如果是选择正则魔方，返回false,会自动返回到上层iframe，调用方只需要手动关闭窗口或不做处理。
                如果返回true，调用方要手动跳转iframe。
        """
        # 解析开始行
        if begin_row:
            self.browser.find_element(By.XPATH, "//*[contains(@class,'startRow')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'startRow')]/following-sibling::span/input[1]").send_keys(begin_row)
            log.info("设置解析开始行: {}".format(begin_row))

        # 通过正则匹配数据列
        js = 'return $(".isMagic")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【通过正则匹配数据列】勾选状态: {0}".format(status))

        enable_magic_element = self.browser.find_element(By.XPATH, "//*[@class='isMagic']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_magic_element)

        if enable_magic == "是":
            if not status:
                enable_magic_element.click()
                log.info("勾选【通过正则匹配数据列】")
        elif enable_magic == "否":
            if status:
                enable_magic_element.click()
                log.info("取消勾选【通过正则匹配数据列】")
            else:
                log.info("【通过正则匹配数据列】 设置为否，不勾选")
        else:
            pass

        # 列总数
        if total_columns:
            self.browser.find_element(By.XPATH, "//*[contains(@class,'colFields')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'colFields')]/following-sibling::span/input[1]").send_keys(total_columns)
            log.info("设置列总数: {}".format(total_columns))

        # 拆分方式
        if row_split_type == "文本":
            self.browser.find_element(By.XPATH, "//*[@name='rowSplitType' and @value='text']").click()
        elif row_split_type == "正则":
            self.browser.find_element(By.XPATH, "//*[@name='rowSplitType' and @value='regexp']").click()
        else:
            pass

        # 列分隔符
        if split_tag:
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'splitChar')]/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[contains(@class,'splitChar')]/following-sibling::span/input[1]").send_keys(split_tag)
            log.info("设置列分隔符: {}".format(split_tag))

        # 高级配置
        if advance_conf:
            pass

        # 正则魔方
        if magic:
            self.setRegular(set_type=magic.get("设置方式"), regular_name=magic.get("正则模版名称"),
                            advance_mode=magic.get("高级模式"), regular=magic.get("标签配置"),
                            expression=magic.get("表达式"), confirm_selector=confirm_selector)

        # 如果是选择正则魔方，needJumpIframe为false,上面会自动返回到上层iframe，调用方只需要手动关闭窗口或不做处理。
        # 如果needJumpIframe为true，通知调用方手动跳转iframe。
        if not magic:
            # 如果不需要配置正则魔方，则返回false
            self.needJumpIframe = False
        else:
            if magic.get("设置方式") == "添加":
                # 如果需要配置正则魔方，且设置方式为添加，则返回true
                self.needJumpIframe = True
            else:
                # 如果需要配置正则魔方，且设置方式为选择，则返回false
                self.needJumpIframe = False
