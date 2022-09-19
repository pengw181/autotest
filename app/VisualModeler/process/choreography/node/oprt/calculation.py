# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:12

from time import sleep
from .condition import condition
from common.page.func.alertBox import BeAlertBox
from app.VisualModeler.process.choreography.node.oprt.cal.regular import regular
from app.VisualModeler.process.choreography.node.oprt.cal.basic import basic
from app.VisualModeler.process.choreography.node.oprt.cal.filter import filter
from app.VisualModeler.process.choreography.node.oprt.cal.aggregate import aggregate
from app.VisualModeler.process.choreography.node.oprt.cal.networkAddr import network_addr
from app.VisualModeler.process.choreography.node.oprt.cal.section import section
from app.VisualModeler.process.choreography.node.oprt.cal.sort import sort
from app.VisualModeler.process.choreography.node.oprt.cal.wash import wash
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.pageMaskWait import page_wait
from common.log.logger import log
from common.variable.globalVariable import *


class CalculationCenter:
    # 运算

    def __init__(self, oprt_type):
        self.browser = get_global_var("browser")
        self.oprt_type = oprt_type

        # 切换到运算配置iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'operateVar.html')]")))
        # 选择运算类型
        self.browser.find_element(By.XPATH, "//*[@name='operate_type']/preceding-sibling::input").click()
        self.browser.find_element(
            By.XPATH, "//*[contains(@id,'oprt_type') and text()='{0}']".format(self.oprt_type)).click()
        log.info("开始配置: {0}".format(oprt_type))
        page_wait()
        sleep(2)

    def cal_condition(self, array):
        # 运算满足条件执行
        """
        [
            ["变量", "时间"],
            ["不等于", ""],
            ["空值", ""],
            ["与", ""],
            ["变量", "地点"],
            ["包含", ""],
            ["自定义值", "abc ddd"]
        ]
        """
        self.browser.find_element(By.XPATH, "//*[@onclick=\"showAdd('oprtfitcnd','1');\"]//*[text()='修改']").click()
        condition(array=array)

    def cal_save(self):

        # 点击保存
        save_elements = self.browser.find_elements(By.XPATH, "//*[@onclick='saveOprtResult();']//*[text()='保存']")
        for element in save_elements:
            if element.is_displayed():
                element.click()
                log.info("点击保存运算配置")

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存运算成功")
        else:
            log.warning("保存运算失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def cal_set(self, params):

        # 根据运算类型，自动选择相应的方法
        if self.oprt_type == "正则运算":
            # 正则运算
            if params.get("是否转置") == "是":
                transpose = True
            else:
                transpose = False
            regular(input_var=params.get("输入变量"), output_var=params.get("输出变量"), value_type=params.get("赋值方式"),
                    var_index=params.get("数组索引"), transpose=transpose, ruler=params.get("解析配置"), fetch=params.get("取值配置"))

        elif self.oprt_type == "过滤运算":
            # 过滤运算
            if params.get("是否转置") == "是":
                transpose = True
            else:
                transpose = False
            filter(input_var=params.get("选择变量"), expression=params.get("过滤条件"), output_var=params.get("输出名称"),
                   output_col=params.get("输出列"), value_type=params.get("赋值方式"), transpose=transpose)

        elif self.oprt_type == "聚合运算":
            # 聚合运算
            if params.get("是否转置") == "是":
                transpose = True
            else:
                transpose = False
            aggregate(input_var=params.get("选择变量"), group_by=params.get("分组依据"), expression=params.get("表达式"),
                      output_var=params.get("输出名称"), output_col=params.get("输出列"), value_type=params.get("赋值方式"),
                      transpose=transpose)

        elif self.oprt_type == "基础运算":
            # 基础运算
            if params.get("是否转置") == "是":
                transpose = True
            else:
                transpose = False
            basic(expression=params.get("表达式"), output_var=params.get("输出名称"), output_col=params.get("输出列"),
                  value_type=params.get("赋值方式"), transpose=transpose)

        elif self.oprt_type == "网络地址运算":
            # 网络地址运算
            network_addr(input_type=params.get("输入方式"), input_addr=params.get("输入地址"), ip=params.get("TCP/IP地址"),
                         output_var=params.get("输出名称"), value_type=params.get("赋值方式"))

        elif self.oprt_type == "分段拆分运算":
            # 分段拆分运算
            section(output_var=params.get("变量名称"), input_var=params.get("输入变量"), value_type=params.get("赋值方式"),
                    begin_config=params.get("开始特征行"), end_config=params.get("结束特征行"), sample_data=params.get("样例数据"))

        elif self.oprt_type == "排序运算":
            # 排序运算
            sort(input_var=params.get("选择变量"), sort_config=params.get("排序配置"), output_var=params.get("输出名称"),
                 output_col=params.get("输出列"), value_type=params.get("赋值方式"))

        elif self.oprt_type == "清洗筛选运算":
            # 清洗筛选运算
            wash(output_var=params.get("变量名称"), input_var=params.get("输入变量"), value_type=params.get("赋值方式"),
                 wash_direction=params.get("筛选方向"), time_wash=params.get("按时间筛选"), key_wash=params.get("按关键字/变量筛选"))

        elif self.oprt_type == "动作":
            self.movement(params.get("表达式"))
        else:
            raise KeyError("不支持的运算类型: {0}".format(self.oprt_type))

        # 保存运算
        self.cal_save()

    def movement(self, expression):
        # 动作
        """
        :param expression: 表达式，必填

        # 休眠
        {
            "表达式": [
                ["休眠", "3"]
            ]
        }

        # 置空
        {
            "表达式": [
                ["置空", "时间"]
            ]
        }
        """
        # 切换到动作iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'operateCfgAction.html')]"))

        # 配置动作
        if expression:
            condition(array=expression, basic_cal=True)

        # 返回到上层iframe
        self.browser.switch_to.parent_frame()
