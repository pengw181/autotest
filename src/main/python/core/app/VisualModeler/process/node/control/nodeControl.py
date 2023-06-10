# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/3/29 下午2:37


from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.input import set_text_enable_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.core.app.VisualModeler.process.node.oprt.condition import set_condition
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


class NodeControl:

    def __init__(self):
        self.browser = gbl.service.get("browser")
        log.info("开始节点控制配置")

    def condition_dependence(self, enable):
        """
        # 条件依赖
        :param enable: 状态，开启/关闭
        """
        # 获取条件依赖勾选状态
        js = 'return $("#is_cnd_rely")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【条件依赖】勾选状态: {0}".format(status))
        # 状态
        if enable:
            if enable not in ["开启", "关闭"]:
                raise KeyError("状态 值错误")
            temp = True if enable == "开启" else False
            if temp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='is_cnd_rely']").click()
            log.info("【条件依赖】{0}".format(enable))

        # 点击保存
        self.save()

    def set_loop(self, enable, loopTagList, loopType, loopContent):
        """
        # 开启循环
        :param enable: 状态，开启/关闭
        :param loopTagList: 循环条件，数组
        :param loopType: 循环类型
        :param loopContent: 循环内容，字典

        # 自定义模式
        {
            "状态": "开启",
            "循环条件": ["操作配置"],
            "循环类型": "变量列表",
            "循环内容": {
                "模式": "自定义模式",
                "变量名称": "数据",
                "循环行变量名称": "xxx",
                "赋值方式": "替换"
            }
        }

        # 便捷模式
        {
            "状态": "开启",
            "循环条件": ["操作配置"],
            "循环类型": "变量列表",
            "循环内容": {
                "模式": "便捷模式",
                "变量名称": "数据"
            }
        }
        """
        # 获取开启循环勾选状态
        js = 'return $("#_node_circle_tag")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【开启循环】勾选状态: {0}".format(status))
        if enable:
            if enable not in ["开启", "关闭"]:
                raise KeyError("状态 值错误")
            temp = True if enable == "开启" else False
            if temp ^ status:
                self.browser.find_element(By.XPATH, "//*[@id='_node_circle_tag']").click()
                sleep(1)
            log.info("【开启循环】{0}".format(enable))
            page_wait(5)

        # 循环条件
        if loopTagList:
            # 先将已选择的标签取消勾选
            try:
                self.browser.find_element(By.XPATH, "//*[@id='loopchecktr']//*[text()='业务配置']")
                # 获取业务配置勾选状态
                js = 'return $("#is_busi_loop")[0].checked;'
                status = self.browser.execute_script(js)
                log.info("循环条件【业务配置】勾选状态: {0}".format(status))
                if status:
                    self.browser.find_element(By.XPATH, "//*[@id='is_busi_loop']").click()
            except NoSuchElementException:
                pass

            try:
                self.browser.find_element(By.XPATH, "//*[@id='loopchecktr']//*[text()='取数配置']")
                # 获取取数配置勾选状态
                js = 'return $("#is_getdata_loop")[0].checked;'
                status = self.browser.execute_script(js)
                log.info("循环条件【取数配置】勾选状态: {0}".format(status))
                if status:
                    self.browser.find_element(By.XPATH, "//*[@id='is_getdata_loop']").click()
            except NoSuchElementException:
                pass

            try:
                self.browser.find_element(By.XPATH, "//*[@id='loopchecktr']//*[text()='操作配置']")
                # 获取操作配置勾选状态
                js = 'return $("#is_operate_loop")[0].checked;'
                status = self.browser.execute_script(js)
                log.info("循环条件【操作配置】勾选状态: {0}".format(status))
                if status:
                    self.browser.find_element(By.XPATH, "//*[@id='is_operate_loop']").click()
            except NoSuchElementException:
                pass

            # 依次勾选循环条件
            for tag in loopTagList:
                self.browser.find_element(By.XPATH, "//*[@id='loopchecktr']//*[text()='{0}']".format(tag)).click()
                log.info("循环条件勾选【{0}】".format(tag))

        # 循环类型
        if loopType:
            self.browser.find_element(
                By.XPATH, "//*[@name='looptype']/following-sibling::span[text()='{0}']".format(loopType)).click()
            log.info("循环类型勾选: {0}".format(loopType))

        # 循环内容
        if loopContent:
            if not isinstance(loopContent, dict):
                raise TypeError("循环内容格式错误")
            if loopType == "变量列表":
                self._var_list_loop(mode=loopContent.get("模式"), varName=loopContent.get("变量名称"),
                                    outVarName=loopContent.get("循环行变量名称"), valueType=loopContent.get("赋值方式"),
                                    varType=loopContent.get("变量类型"))

            elif loopType == "次数":
                self._circle_loop(circleTimes=loopContent.get("循环次数"), outVarName=loopContent.get("循环变量名称"),
                                  valueType=loopContent.get("赋值方式"), toNextCondition=loopContent.get("跳至下一轮条件"),
                                  endCondition=loopContent.get("结束循环条件"))

            elif loopType == "条件":
                self._condition_loop(circleCondition=loopContent.get("循环条件"), toNextCondition=loopContent.get("跳至下一轮条件"),
                                     endCondition=loopContent.get("结束循环条件"))

            else:
                raise KeyError("不支持的循环类型: {0}".format(loopType))

        # 点击保存
        self.save()

    def _var_list_loop(self, mode, varName, outVarName, valueType, varType):
        """
        # 变量列表循环
        :param mode: 模式
        :param varName: 变量名称
        :param outVarName: 循环行变量名称
        :param valueType: 赋值方式
        :param varType: 变量类型
        """
        # 模式
        if mode:
            self.browser.find_element(
                By.XPATH, "//*[@name='mode']/following-sibling::label[text()='{0}']/preceding-sibling::input".format(
                    mode)).click()
            log.info("选择模式: {0}".format(mode))
            sleep(1)

        # 变量类型
        if varType:
            self.browser.find_element(By.XPATH, "//*[@id='vartype']/following-sibling::span//a").click()
            self.browser.find_element(By.XPATH, "//*[contains(@id,'vartype') and text()='{0}']".format(varType)).click()
            log.info("选择变量类型: {0}".format(varType))

        # 变量名称
        if varName:
            try:
                self.browser.find_element(
                    By.XPATH, "//*[@id='dataH_inputVarControl2Name']/following-sibling::span//a").click()
            except ElementNotInteractableException:
                self.browser.find_element(
                    By.XPATH, "//*[@id='dataH_cmdVarName']/following-sibling::span//a").click()
            choose_var(var_name=varName)

        # 循环行变量名称，选择变量后会自动填充
        if outVarName:
            self.browser.find_element(By.XPATH, "//*[@id='outVarName']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='outVarName']/following-sibling::span//input[1]").send_keys(outVarName)
            log.info("设置循环行变量名称: {0}".format(outVarName))

        # 赋值方式
        if valueType:
            self.browser.find_element(By.XPATH, "//*[@id='valuetype_1']/following-sibling::span[1]//a").click()
            panel_xpath = getPanelXpath(1)
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(valueType)).click()
            sleep(1)

    def _circle_loop(self, circleTimes, outVarName, valueType, toNextCondition, endCondition):
        """
        # 次数循环
        :param circleTimes: 循环次数
        :param outVarName: 循环变量名称
        :param valueType: 赋值方式
        :param toNextCondition: 跳至下一轮条件
        :param endCondition: 结束循环条件
        """
        # 循环次数
        if circleTimes:
            input_xpath = "//*[@id='ctrl_times']/following-sibling::span/input[1]"
            set_text_enable_var(input_xpath=input_xpath, msg=circleTimes)
            log.info("设置循环次数: {0}".format(circleTimes))

        # 循环变量名称
        if outVarName:
            self.browser.find_element(By.XPATH, "//*[@id='outVarName_2']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='outVarName_2']/following-sibling::span/input[1]").send_keys(outVarName)
            log.info("设置循环变量名称: {0}".format(outVarName))

        # 赋值方式
        if valueType:
            elements = self.browser.find_elements(By.XPATH, "//*[@id='valuetype_2']/following-sibling::span[1]//a")
            for e1 in elements:
                if e1.is_displayed():
                    e1.click()
                    elements = self.browser.find_elements(
                        By.XPATH, "//*[contains(@id,'valuetype_2') and text()='{0}']".format(valueType))
                    for e2 in elements:
                        if e2.is_displayed():
                            e2.click()
                            log.info("设置赋值方式: {0}".format(valueType))
                            sleep(1)
                            break

        # 跳至下一轮条件
        if toNextCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'times_nextCondition')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'times_nextCondition')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=toNextCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【跳至下一轮条件】配置完成")
            sleep(1)

        # 结束循环条件
        if endCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'times_endCondition')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'times_endCondition')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=endCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【结束循环条件】配置完成")
            sleep(1)

    def _condition_loop(self, circleCondition, toNextCondition, endCondition):
        """
        # 条件循环
        :param circleCondition: 循环条件
        :param toNextCondition: 跳至下一轮条件
        :param endCondition: 结束循环条件
        """
        # 循环条件
        if circleCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'circleCondition')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'circleCondition')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=circleCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【循环条件】配置完成")
            sleep(1)

        # 跳至下一轮条件
        if toNextCondition:
            # 先清空
            del_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'nextCondition')]")
            if len(del_elements) == 0:
                raise NoSuchElementException
            for element in del_elements:
                if element.is_displayed():
                    element.click()
                    break
            # 点击修改
            show_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'nextCondition')]")
            if len(show_elements) == 0:
                raise NoSuchElementException
            for element in show_elements:
                if element.is_displayed():
                    element.click()
                    break
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=toNextCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【跳至下一轮条件】配置完成")
            sleep(1)

        # 结束循环条件
        if endCondition:
            # 先清空
            del_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'endCondition')]")
            if len(del_elements) == 0:
                raise NoSuchElementException
            for element in del_elements:
                if element.is_displayed():
                    element.click()
                    break
            # 点击修改
            show_elements = self.browser.find_elements(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'endCondition')]")
            if len(show_elements) == 0:
                raise NoSuchElementException
            for element in show_elements:
                if element.is_displayed():
                    element.click()
                    break
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=endCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【结束循环条件】配置完成")
            sleep(1)

    # def get_value_by_col(self, enable, varSetList):
    #     """
    #     # 按列取数
    #     :param enable: 状态，开启/关闭
    #     :param varSetList: 变量列表
    #     """
    #     page_wait()
    #     # 切换到节点iframe
    #     wait = WebDriverWait(self.browser, 30)
    #     wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("NodeIframe"))))
    #     # 切换到控制配置页面iframe
    #     wait = WebDriverWait(self.browser, 30)
    #     wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("ControlIframe"))))
    #
    #     # 获取是否按列取数勾选状态
    #     js = 'return $("#is_getValueByCol")[0].checked;'
    #     status = self.browser.execute_script(js)
    #     log.info("【是否按列取数】勾选状态: {0}".format(status))
    #     if enable:
    #         if enable not in ["开启", "关闭"]:
    #             raise KeyError("状态 值错误")
    #         temp = True if enable == "开启" else False
    #         if not (temp and status):
    #             self.browser.find_element(By.XPATH, "//*[@id='is_getValueByCol']").click()
    #             sleep(1)
    #         log.info("【是否按列取数】{0}".format(enable))
    #         page_wait(3)
    #
    #     # 变量列表
    #     if varSetList:
    #         if not isinstance(varSetList, list):
    #             raise TypeError("变量列表格式错误")
    #         for var_info in varSetList:
    #             # 循环得到变量配置
    #             if not isinstance(var_info, dict):
    #                 raise TypeError("变量配置格式错误")
    #             opt_type = var_info.get("操作")
    #             obj_var = var_info.get("目标变量")
    #             var_name = var_info.get("变量名称")
    #             value_type = var_info.get("赋值方式")
    #             array_index = var_info.get("数据索引")
    #
    #             opt_type = "添加" if opt_type is None else opt_type
    #             if opt_type == "添加":
    #                 # 点击添加
    #                 self.browser.find_element(By.XPATH, "//*[@onclick='addCtrlGetInfo();']").click()
    #                 sleep(1)
    #                 self._col_var_page(varName=var_name, valueType=value_type, arrayIndex=array_index)
    #             else:
    #                 # 目标变量
    #                 if not obj_var:
    #                     raise AttributeError("操作类型为{0}时，需要指定目标变量".format(opt_type))
    #                 self.browser.find_element(By.XPATH, "//*[@field='varName']/*[text()='{0}']".format(obj_var)).click()
    #
    #                 if opt_type == "修改":
    #                     # 点击修改
    #                     self.browser.find_element(By.XPATH, "//*[@onclick='edit_ctrcfg_var();']").click()
    #                     self._col_var_page(varName=var_name, valueType=value_type, arrayIndex=array_index)
    #                 else:
    #                     # 点击删除
    #                     self.browser.find_element(By.XPATH, "//*[@onclick='delete_ctrcfg_var();']").click()
    #                     alert = BeAlertBox(back_iframe="default")
    #                     msg = alert.get_msg()
    #                     if alert.title_contains("您确定需要删除{0}吗".format(obj_var), auto_click_ok=False):
    #                         alert.click_ok()
    #                         alert = BeAlertBox(back_iframe=False)
    #                         msg = alert.get_msg()
    #                         if alert.title_contains("操作成功"):
    #                             log.info("【按列取数】设置变量成功")
    #                             # 切换到节点iframe
    #                             wait = WebDriverWait(self.browser, 30)
    #                             wait.until(
    #                                 ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("NodeIframe"))))
    #                             # 切换到控制配置页面iframe
    #                             wait = WebDriverWait(self.browser, 30)
    #                             wait.until(
    #                                 ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("ControlIframe"))))
    #                         else:
    #                             log.warn("【按列取数】删除变量失败，失败提示: {0}".format(msg))
    #                     else:
    #                         log.warn("【按列取数】删除变量失败，失败提示: {0}".format(msg))
    #                     gbl.temp.set("ResultMsg", msg)
    #
    #         # 保存控制配置
    #         self.save()
    #
    # def _col_var_page(self, varName, valueType, arrayIndex):
    #     """
    #     # 按列取数页面
    #     :param varName: 变量名称
    #     :param valueType: 赋值方式
    #     :param arrayIndex: 数据索引
    #     """
    #     # 变量名称
    #     if varName:
    #         self.browser.find_element(By.XPATH, "//*[@id='ctrlvarName']/following-sibling::span/input[1]").clear()
    #         self.browser.find_element(
    #             By.XPATH, "//*[@id='ctrlvarName']/following-sibling::span/input[1]").send_keys(varName)
    #         log.info("【按列取数】设置变量名称: {0}".format(varName))
    #
    #     # 赋值方式
    #     if valueType:
    #         elements = self.browser.find_elements(By.XPATH, "//*[@id='valuetype']/following-sibling::span[1]//a")
    #         for e1 in elements:
    #             if e1.is_displayed():
    #                 e1.click()
    #                 elements = self.browser.find_elements(
    #                     By.XPATH, "//*[contains(@id,'valuetype') and text()='{0}']".format(valueType))
    #                 for e2 in elements:
    #                     if e2.is_displayed():
    #                         e2.click()
    #                         log.info("【按列取数】设置赋值方式: {0}".format(valueType))
    #                         sleep(1)
    #                         break
    #     # 数据索引
    #     if arrayIndex:
    #         self.browser.find_element(
    #             By.XPATH, "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").clear()
    #         self.browser.find_element(
    #             By.XPATH, "//*[@id='ctrlarrayIndex']/following-sibling::span/input[1]").send_keys(arrayIndex)
    #         log.info("【按列取数】设置数据索引: {0}".format(arrayIndex))
    #
    #     # 保存
    #     self.browser.find_element(By.XPATH, "//*[@onclick='addColumnVar()']").click()
    #     alert = BeAlertBox(back_iframe="default")
    #     msg = alert.get_msg()
    #     if alert.title_contains("操作成功"):
    #         log.info("【按列取数】设置变量成功")
    #         # 切换到节点iframe
    #         wait = WebDriverWait(self.browser, 30)
    #         wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("NodeIframe"))))
    #         # 切换到控制配置页面iframe
    #         wait = WebDriverWait(self.browser, 30)
    #         wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, gbl.service.get("ControlIframe"))))
    #     else:
    #         log.warn("【按列取数】设置变量失败，失败提示: {0}".format(msg))
    #     gbl.temp.set("ResultMsg", msg)
    #
    # def advance_cfg(self, saveLog, recordCycleNum, outputLogPrintRuler):
    #     """
    #     # 高级配置
    #     :param saveLog: 是否记录循环日志，是/否
    #     :param recordCycleNum: 循环日志记录条数
    #     :param outputLogPrintRuler: 输出日志打印规则
    #     """
    #     # 展开高级配置
    #     advance_element = self.browser.find_element(By.XPATH, "//*[@id='adv_btn']")
    #     expander_flag = advance_element.get_attribute("class")
    #     if expander_flag.find("expander") == -1:
    #         # 点击箭头展开
    #         advance_element.click()
    #         sleep(1)
    #
    #     # 获取是否记录循环日志勾选状态
    #     js = 'return $("#is_addLog")[0].checked;'
    #     status = self.browser.execute_script(js)
    #     log.info("【是否按列取数】勾选状态: {0}".format(status))
    #     if saveLog:
    #         if saveLog not in ["是", "否"]:
    #             raise KeyError("状态 值错误")
    #         temp = True if saveLog == "开启" else False
    #         if temp ^ status:
    #             self.browser.find_element(By.XPATH, "//*[@id='is_addLog']").click()
    #             sleep(1)
    #         log.info("【是否记录循环日志】{0}".format(saveLog))
    #         page_wait(3)
    #
    #     # 循环日志记录条数
    #     if recordCycleNum:
    #         self.browser.find_element(By.XPATH, "//*[@id='recordCycleNum']/following-sibling::span").clear()
    #         self.browser.find_element(
    #             By.XPATH, "//*[@id='recordCycleNum']/following-sibling::span").send_keys(recordCycleNum)
    #         log.info("设置循环日志记录条数: {0}".format(recordCycleNum))
    #
    #     # 循环日志记录条数
    #     if outputLogPrintRuler:
    #         self.browser.find_element(By.XPATH, "//*[@id='outputLogPrintRuler']/following-sibling::span").clear()
    #         self.browser.find_element(
    #             By.XPATH, "//*[@id='outputLogPrintRuler']/following-sibling::span").send_keys(outputLogPrintRuler)
    #         log.info("设置循环日志记录条数: {0}".format(outputLogPrintRuler))
    #
    #     # 点击保存
    #     self.save()

    def set_logic_branch(self, enable, branchType, meetCondition, unMeetCondition, unCertainCondition, dynamicCondition):
        """
        # 逻辑分支控制
        :param enable: 状态，开启/关闭
        :param branchType: 逻辑分支类型
        :param meetCondition: 满足条件
        :param unMeetCondition: 不满足条件
        :param unCertainCondition: 不确定条件
        :param dynamicCondition: 动态值

        # 固定值分支
        {
            "状态": "开启",
            "逻辑分支类型": "固定值分支",
            "满足条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "名字"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "不满足条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "名字"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ],
            "不确定条件": [
                ["变量", "时间"],
                ["不等于", ""],
                ["空值", ""],
                ["与", ""],
                ["变量", "名字"],
                ["包含", ""],
                ["自定义值", "abc ddd"]
            ]
        }

        # 动态值分支
        {
            "状态": "开启",
            "逻辑分支类型": "动态值分支",
            "动态值": [
                ["变量", "时间"],
                ["+", ""],
                ["自定义值", "1"]
            ]
        }
        """
        # 滑动页面
        logic_element = self.browser.find_element(By.XPATH, "//*[@id='westExap']//h2")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", logic_element)

        # 获取逻辑分支控制勾选状态
        js = 'return $("#_node_logic_tag")[0].checked;'
        status = self.browser.execute_script(js)
        log.info("【逻辑分支控制】勾选状态: {0}".format(status))
        if enable:
            if enable not in ["开启", "关闭"]:
                raise KeyError("状态 值错误")
            temp = True if enable == "开启" else False
            if not (temp and status):
                self.browser.find_element(By.XPATH, "//*[@id='_node_logic_tag']").click()
                sleep(1)
            log.info("【逻辑分支控制】{0}".format(enable))
            page_wait(3)

        # 逻辑分支类型
        if branchType:
            self.browser.find_element(
                By.XPATH, "//*[@name='branchType']/following-sibling::span[text()='{0}']".format(branchType)).click()
            log.info("逻辑分支类型选择: {0}".format(branchType))
            sleep(1)

        # 满足条件
        if meetCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'fitcnd')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'fitcnd')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=meetCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【满足条件】配置完成")
            sleep(1)

        # 不满足条件
        if unMeetCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'nofitcnd')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'nofitcnd')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=unMeetCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【不满足条件】配置完成")
            sleep(1)

        # 不确定条件
        if unCertainCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'unsurecnd')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'unsurecnd')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=unCertainCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【不确定条件】配置完成")
            sleep(1)

        # 动态值
        if dynamicCondition:
            # 先清空
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'deleteAdd') and contains(@onclick,'dynamicCnd')]").click()
            # 点击修改
            self.browser.find_element(
                By.XPATH, "//*[contains(@onclick,'showAdd') and contains(@onclick,'dynamicCnd')]").click()
            page_wait()
            iframe_xpath_list = [gbl.service.get("NodeIframe"), gbl.service.get("ControlIframe")]
            set_condition(array=dynamicCondition, iframe_xpath_list=iframe_xpath_list)
            log.info("【动态值】配置完成")
            sleep(1)

        # 点击保存
        self.save()

    def save(self):
        self.browser.find_element(By.XPATH, "//*[@onclick='saveCtrlCfgCondition()']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("设置成功")
        else:
            log.warn("【设置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)
