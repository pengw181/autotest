# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:52

from app.VisualModeler.doctorwho.doctorWho import DoctorWho
from time import sleep
from common.page.func.alertBox import BeAlertBox
from common.page.func.input import set_textarea
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.page.func.upload import upload
from common.log.logger import log
from common.variable.globalVariable import *


class AiModel:

    def __init__(self):
        self.browser = get_global_var("browser")
        self.algorithm = None
        DoctorWho().choose_menu("常用信息管理-AI模型管理")
        self.browser.switch_to.frame(
            self.browser.find_element(
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/algorithm.html')]"))
        page_wait()
        sleep(1)

    def choose(self, model_name):
        """
        :param model_name: 模型名称
        :return:
        """
        self.browser.find_element(By.XPATH, "//*[@name='modelName']/preceding-sibling::input").send_keys(model_name)
        self.browser.find_element(By.XPATH, "//*[@id='queryButton']//*[text()='查询']").click()
        page_wait()
        self.browser.find_element(
            By.XPATH, "//*[contains(@id,'templetManage')]/*[@field='modelName']/*[text()='{0}']".format(
                model_name)).click()
        log.info("已选择模型: {0}".format(model_name))

    def add(self, application_mode, algorithm, model_name, model_desc, train_scale, test_scale, timeout, file_name,
            params, columns):
        """
        :param application_mode: 应用模式
        :param algorithm: 算法名称
        :param model_name: 模型名称
        :param model_desc: 模型描述
        :param train_scale: 训练比例
        :param test_scale: 测试比例
        :param timeout: 超时时间
        :param file_name: 模型数据
        :param params: 参数设置
        :param columns: 列设置
        """
        log.info("开始添加数据")
        self.browser.find_element(By.XPATH, "//*[text()='添加']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='applicationMode']/preceding-sibling::input")))

        self.algorithm_page(application_mode, algorithm, model_name, model_desc, train_scale, test_scale, timeout,
                            file_name, params, columns)

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 添加成功".format(model_name))
        else:
            log.warning("{0} 添加失败，失败提示: {1}".format(model_name, msg))
        set_global_var("ResultMsg", msg, False)

    def update(self, obj, model_name, model_desc, train_scale, test_scale, timeout, file_name, params, columns):
        """
        :param obj: 模型名称
        :param model_name: 模型名称
        :param model_desc: 模型描述
        :param train_scale: 训练比例
        :param test_scale: 测试比例
        :param timeout: 超时时间
        :param file_name: 模型数据
        :param params: 参数设置
        :param columns: 列设置
        """
        log.info("开始修改数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='modelName']/preceding-sibling::input")))

            self.algorithm_page(None, None, model_name, model_desc, train_scale, test_scale, timeout, file_name, params,
                                columns)
            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("修改成功"):
                log.info("{0} 修改成功".format(obj))
            else:
                log.warning("{0} 修改失败，失败提示: {1}".format(obj, msg))
            set_global_var("ResultMsg", msg, False)

    def algorithm_page(self, application_mode, algorithm, model_name, model_desc, train_scale, test_scale, timeout,
                       file_name, params, columns):
        """
        :param application_mode: 应用模式
        :param algorithm: 算法名称
        :param model_name: 模型名称
        :param model_desc: 模型描述
        :param train_scale: 训练比例
        :param test_scale: 测试比例
        :param timeout: 超时时间
        :param file_name: 模型数据
        :param params: 参数设置，数组
        :param columns: 列设置，字典
        """
        # 应用模式
        if application_mode:
            self.browser.find_element(By.XPATH, "//*[@id='applicationMode']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'applicationMode') and text()='{0}']".format(application_mode)).click()
            log.info("设置应用模式: {0}".format(application_mode))
            sleep(1)

        # 算法名称
        if algorithm:
            self.browser.find_element(By.XPATH, "//*[@id='algorithm']/following-sibling::span//a").click()
            self.browser.find_element(
                By.XPATH, "//*[contains(@id,'algorithm') and text()='{0}']".format(algorithm)).click()
            log.info("设置算法名称: {0}".format(algorithm))

        # 模型名称
        if model_name:
            self.browser.find_element(By.XPATH, "//*[@name='modelName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='modelName']/preceding-sibling::input").send_keys(model_name)
            log.info("设置模型名称: {0}".format(model_name))

        # 模型描述
        if model_desc:
            model_desc_textarea = self.browser.find_element(By.XPATH, "//*[@name='modelDesc']/preceding-sibling::textarea")
            set_textarea(textarea=model_desc_textarea, msg=model_desc)
            log.info("设置模型描述: {0}".format(model_desc))

        # 训练比例
        if train_scale:
            self.browser.find_element(By.XPATH, "//*[@id='trainDataScale']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='trainDataScale']/following-sibling::span//input[1]").send_keys(train_scale)
            log.info("设置训练比例: {0}".format(train_scale))

        # 测试比例
        if test_scale:
            self.browser.find_element(By.XPATH, "//*[@id='testDataScale']/following-sibling::span//input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='testDataScale']/following-sibling::span//input[1]").send_keys(test_scale)
            log.info("设置测试比例: {0}".format(test_scale))

        # 超时时间
        if timeout:
            self.browser.find_element(By.XPATH, "//*[@id='train_test_timeout']/following-sibling::span/input[1]").clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='train_test_timeout']/following-sibling::span/input[1]").send_keys(timeout)
            log.info("设置超时时间: {0}".format(timeout))

        # 模型数据
        if file_name:
            # 点击选择文件
            # self.browser.find_element(By.XPATH, "//*[@id='fileName']/following-sibling::span//label").click()
            # sleep(1)
            log.info("开始上传模型数据文件: {0}".format(file_name))
            upload(file_name=file_name, catalog="model", input_id="filebox_file_id_3")
            sleep(1)
            # 点击上传按钮
            self.browser.find_element(By.XPATH, "//*[@onclick='importAITestFile()']//*[text()='上传']").click()
            alert = BeAlertBox(timeout=10)
            msg = alert.get_msg()
            if alert.title_contains("文件上传成功"):
                log.info("{0} 上传成功".format(file_name))
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
                sleep(1)
            else:
                log.warning("{0} 上传失败，失败提示: {1}".format(file_name, msg))
            set_global_var("ResultMsg", msg, False)

        # 参数设置
        if params:
            algorithm_obj = self.browser.find_element(By.XPATH, "//*[@name='algorithm']")
            algorithm = algorithm_obj.get_attribute("value")
            self.ai_param_set(algorithm=self.get_algorithm(algorithm), params=params)

        # 列设置
        if columns:
            algorithm_obj = self.browser.find_element(By.XPATH, "//*[@name='algorithm']")
            algorithm = algorithm_obj.get_attribute("value")
            self.ai_col_set(algorithm=self.get_algorithm(algorithm), col_sets=columns)

        # 提交
        self.browser.find_element(By.XPATH, "//*[@id='saveButton']//*[text()='提交']").click()

    @staticmethod
    def get_algorithm(algorithm):
        algorithm_map = {
            "LSTM": "lstm",
            "SARIMA": "sarima",
            "GRU_disturb1": "disturb1",
            "factorLGBM": "factorLGBM",
            "factorXGB": "factorXGB",
            "lightgbm": "lightgbm",
            "GBDT": "GBDT",
            "random_forest": "random_forest",
        }
        return algorithm_map.get(algorithm)

    def ai_param_set(self, algorithm, params):
        """
        :param algorithm: 算法名称
        :param params: 参数列表
        """
        num = 1
        for param in params:
            param_tag = algorithm + "_param_" + str(num)
            self.browser.find_element(By.XPATH, "//*[@id='{0}']/following-sibling::span/input[1]".format(param_tag)).clear()
            self.browser.find_element(
                By.XPATH, "//*[@id='{0}']/following-sibling::span/input[1]".format(param_tag)).send_keys(param)
            log.info("设置参数: {0}".format(param))
            num += 1

    def ai_col_set(self, algorithm, col_sets):
        """
        :param algorithm: 算法名称
        :param col_sets: 列设置，字典

        # LSTM预测模型: lstm
        {
            "时间列": "time",
            "预测列": "online_number"
        }

        # SARIMA预测模型: sarima
        {
            "时间列": "Time",
            "预测列": "Data (TB)"
        }

        # GRU预测模型: disturb1
        {
            "时间列": "Time",
            "预测列": "Data (TB)",
            "干扰因素列": ["标签", "小时数"]
        }

        # xgboost预测模型: factorXGB
        {
            "时间列": "ds",
            "预测列": "y",
            "干扰因素列": ["add_1", "add_2", "add_3"]
        }

        # factorLGBM: factorLGBM
        {
            "时间列": "时间列",
            "预测列": "预测列",
            "特征列": ["特征列1", "特征列2"],
            "干扰因素列": ["干扰因素1", "干扰因素2"]
        }

        # 通用算法
        {
            "时间列": "",
            "预测列": "IS_REAL_ALARM",
            "干扰因素列": [
                "country_id",
                "IMPORTANCE",
                "REQ_SUCCESS_RATE",
                "DIVINE_REQ_SUCCESS_RATE",
                "REQ_SUCCESS",
                "SCALER_REQ_SUCCESS_DRIFT",
                "REQ_SUM",
                "SCALER_REQ_SUM_DRIFT",
                "DIVINE_REQ_SUCCESS",
                "DIVINE_REQ_SUM",
                "REQ_SUCCESS_RATE_DRIFT",
                "REQ_SUCCESS_RATE_DRIFT_FLAG",
                "COUNT",
                "WARN_TIME"
            ]
        }
        """
        num = 1
        for col_name, col_value in col_sets.items():
            col_tag = algorithm + "_col_" + str(num)
            if col_value:
                # 点开下拉框
                self.browser.find_element(By.XPATH, "//*[@id='{0}']/following-sibling::span//a".format(col_tag)).click()
                sleep(1)

                # 时间列、预测列单选
                if col_name in ["时间列", "预测列"]:
                    col_ele = self.browser.find_elements(
                        By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(col_value))
                    if len(col_ele) > 0:
                        for element in col_ele:
                            if element.is_displayed():
                                element.click()
                                log.info("{0}选择: {1}".format(col_name, col_value))
                                break
                    else:
                        raise KeyError("{0}下找不到: {1}".format(col_name, col_value))
                else:
                    # 特征列、干扰因素列多选
                    for key in col_value:
                        col_ele = self.browser.find_elements(
                            By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(key))
                        if len(col_ele) > 0:
                            for element in col_ele:
                                if element.is_displayed():
                                    element.click()
                                    log.info("{0}选择: {1}".format(col_name, key))
                                    break

                        else:
                            raise KeyError("{0}下找不到: {1}".format(col_name, key))
                    # 多选选择完成后，再次点击下拉框箭头，收起下拉框
                    self.browser.find_element(
                        By.XPATH, "//*[@id='{0}']/following-sibling::span//a".format(col_tag)).click()
                num += 1
            else:
                num += 1

    def train_model(self, model_name):
        """
        :param model_name: 模型名称
        """
        log.info("开始训练模型")
        self.choose(model_name=model_name)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='modelName']/preceding-sibling::input")))

            # 点击训练按钮
            self.browser.find_element(By.XPATH, "//*[@onclick='getTrainResult()']").click()
            alert = BeAlertBox(timeout=30)
            msg = alert.get_msg()
            if alert.title_contains("提交训练成功"):
                log.info("{0} 提交训练成功".format(model_name))
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
                sleep(1)
            else:
                log.warning("{0} 提交训练失败，失败提示: {1}".format(model_name, msg))
            set_global_var("ResultMsg", msg, False)

    def test_model(self, model_name):
        """
        :param model_name: 模型名称
        """
        log.info("开始测试模型")
        self.choose(model_name=model_name)
        self.browser.find_element(By.XPATH, "//*[text()='修改']").click()

        # 鉴于数据权限问题，在修改/删除数据时，需要判断是否有弹出框提示无权操作
        alert = BeAlertBox(back_iframe=False, timeout=2)
        if alert.exist_alert:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='modelName']/preceding-sibling::input")))

            # 点击测试按钮
            self.browser.find_element(By.XPATH, "//*[@onclick='getTestResult()']").click()
            alert = BeAlertBox(timeout=30)
            msg = alert.get_msg()
            if alert.title_contains("提交测试成功"):
                log.info("{0} 提交测试成功".format(model_name))
                wait = WebDriverWait(self.browser, 10)
                wait.until(ec.frame_to_be_available_and_switch_to_it((
                    By.XPATH, "//iframe[contains(@src,'algorithmEdit.html')]")))
                sleep(1)
            else:
                log.warning("{0} 提交测试失败，失败提示: {1}".format(model_name, msg))
            set_global_var("ResultMsg", msg, False)

    def delete(self, obj):
        """
        :param obj: 模型名称
        """
        log.info("开始删除数据")
        self.choose(obj)
        self.browser.find_element(By.XPATH, "//*[text()='删除']").click()

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            # 无权操作
            log.warning("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def import_disturb(self, model_name, file_name):
        """
        # 导入干扰因素
        :param model_name: 模型名称
        :param file_name: 文件名
        """
        self.choose(model_name)
        self.browser.find_element(By.XPATH, "//*[text()='{0}']/../following-sibling::td[3]//a".format(model_name)).click()
        page_wait(10)
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'algorithmDisturbCfg.html')]")))
        # 点击导入
        self.browser.find_element(By.XPATH, "//*[@onclick='toBatchAddOperate()']").click()
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'disturbcfgImportWin.html')]")))
        upload(file_name=file_name, catalog="model", input_id="filebox_file_id_2")
        # 点击上传
        self.browser.find_element(By.XPATH, "//*[@onclick='uploadDisturbFile()']").click()
        self.browser.switch_to.parent_frame()
        alert = BeAlertBox(timeout=20)
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("{0} 导入成功".format(file_name))
        else:
            log.warning("{0} 导入失败，失败提示: {1}".format(file_name, msg))
        set_global_var("ResultMsg", msg, False)

    def data_clear(self, obj, fuzzy_match=False):
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element(By.XPATH, "//*[@name='modelName']/preceding-sibling::input").clear()
        self.browser.find_element(By.XPATH, "//*[@name='modelName']/preceding-sibling::input").send_keys(obj)
        self.browser.find_element(By.XPATH, "//*[@id='queryButton']//*[text()='查询']").click()
        page_wait()
        fuzzy_match = True if fuzzy_match == "是" else False
        if fuzzy_match:
            record_element = self.browser.find_elements(
                By.XPATH, "//*[@field='modelName']/*[starts-with(text(),'{0}')]".format(obj))
        else:
            record_element = self.browser.find_elements(By.XPATH, "//*[@field='modelName']/*[text()='{0}']".format(obj))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element(By.XPATH, "//*[text()='删除']").click()
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
                                By.XPATH, "//*[@field='modelName']/*[starts-with(text(),'{0}')]".format(obj))
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
                    log.warning("{0} 清理失败，失败提示: {1}".format(obj, msg))
                    set_global_var("ResultMsg", msg, False)
                    break
        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            pass
