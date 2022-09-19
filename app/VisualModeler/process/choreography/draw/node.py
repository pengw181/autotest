# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:50

from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.VisualModeler.process.choreography.node.business.cmdBusi import cmd_business
from app.VisualModeler.process.choreography.node.business.commonBusi import common_business
from app.VisualModeler.process.choreography.node.business.fileBusi import file_business
from app.VisualModeler.process.choreography.node.business.scriptBusi import script_business
from app.VisualModeler.process.choreography.node.business.sqlBusi import sql_business
from app.VisualModeler.process.choreography.node.business.cmdTemplateBusi import cmd_template_business
from app.VisualModeler.process.choreography.node.business.edataBusi import edata_business
from app.VisualModeler.process.choreography.node.business.crawlerBusi import crawler_business
from app.VisualModeler.process.choreography.node.business.interfaceBusi import interface_business
from app.VisualModeler.process.choreography.node.business.dataHandleBusi import datahandle_business
from app.VisualModeler.process.choreography.node.business.infoBusi import info_business
from app.VisualModeler.process.choreography.node.business.aiBusi import ai_business
from app.VisualModeler.process.choreography.node.business.ocrBusi import ocr_business
from app.VisualModeler.process.choreography.node.business.emailBusi import email_business
from app.VisualModeler.process.choreography.node.business.dataAccessBusi import data_access_business
from app.VisualModeler.process.choreography.node.business.alarmBusi import alarm_business
from app.VisualModeler.process.choreography.node.business.reportBusi import report_business
from app.VisualModeler.process.choreography.node.fetch.cmdFetch import cmd_fetch
from app.VisualModeler.process.choreography.node.fetch.sqlFetch import sql_fetch
from app.VisualModeler.process.choreography.node.fetch.cmdTemplateFetch import cmd_temp_fetch
from app.VisualModeler.process.choreography.node.fetch.edataFetch import edata_fetch
from app.VisualModeler.process.choreography.node.fetch.judgeFetch import judge_fetch
from app.VisualModeler.process.choreography.node.fetch.scriptFetch import script_fetch
from app.VisualModeler.process.choreography.node.fetch.interfaceFetch import interface_fetch
from app.VisualModeler.process.choreography.node.fetch.crawlerFetch import crawler_fetch
from app.VisualModeler.process.choreography.node.fetch.emailFetch import email_fetch
from app.VisualModeler.process.choreography.node.fetch.aiFetch import ai_fetch
from app.VisualModeler.process.choreography.node.fetch.ocrFetch import ocr_fetch
from app.VisualModeler.process.choreography.node.oprt.rightOpt import opt_action
from app.VisualModeler.process.choreography.node.control.nodeControl import NodeControl
from common.page.func.pageMaskWait import page_wait
from common.page.func.alertBox import BeAlertBox
from common.variable.globalVariable import *
from common.log.logger import log


class Node:

    def __init__(self, node_type, node_name):

        self.browser = get_global_var("browser")
        self.node_type = node_type
        self.original_node_name = node_name
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(node_name))))
        page_wait()
        self.node_element = self.browser.find_element(
            By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(node_name))
        # self.browser.execute_script("arguments[0].scrollIntoView(true);", self.node_element)
        # 双击进入节点
        action = ActionChains(self.browser)
        action.double_click(self.node_element).perform()
        page_wait()

        if self.node_type == "指令节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/cmdNode.html')]")
        elif self.node_type == "通用节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/usualNode.html')]")
        elif self.node_type == "文件节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/fileNode.html')]")
        elif self.node_type == "Sql节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/sqlNode.html')]")
        elif self.node_type == "指令模版节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/cmdTemplateNode.html')]")
        elif self.node_type == "数据拼盘节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/edataCustomNode.html')]")
        elif self.node_type == "数据处理节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/dataHandleNode.html')]")
        elif self.node_type == "可视化操作模拟节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/crawlerNode.html')]")
        elif self.node_type == "脚本节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/scriptNode.html')]")
        elif self.node_type == "接口节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/portNode.html')]")
        elif self.node_type == "报表节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/reportNode.html')]")
        elif self.node_type == "邮件节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/emailNode.html')]")
        elif self.node_type == "AI节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/irNode.html')]")
        elif self.node_type == "OCR节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/ocrNode.html')]")
        elif self.node_type == "信息处理节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/nodeInfoCfg.html')]")
        elif self.node_type == "数据接入节点":
            set_global_var("NodeIframe", "//iframe[contains(@src,'./node/dataAccessNode.html')]")
        else:
            raise KeyError("不支持的节点类型: {0}".format(self.node_type))

        # 控制配置页面iframe
        set_global_var("ControlIframe", "//iframe[contains(@src,'controlCfg.html')]")
        # 操作配置页面iframe
        set_global_var("OptIframe", "//iframe[contains(@src,'operateNodeCfg.html')]")
        # 爬虫配置页面iframe
        set_global_var("CrawlerIframe", "//iframe[contains(@src,'busiCrawlerNode.html')]")

    def business_conf(self, **kwargs):

        # 切换到节点iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, get_global_var("NodeIframe"))))
        sleep(1)

        # node_name返回修改后的节点名，或者空，为空则使用原节点名称
        if self.node_type == "指令节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_cmd_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            # 业务配置
            node_name = cmd_business(node_name=kwargs.get("节点名称"), mem_filter=kwargs.get("成员选择"),
                                     ne_filter=kwargs.get("网元选择"), choose_type=kwargs.get("选择方式"),
                                     scene=kwargs.get("场景标识"), config=kwargs.get("配置"),
                                     advance_set=kwargs.get("高级配置"))

        elif self.node_type == "通用节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            # 业务配置
            node_name = common_business(node_name=kwargs.get("节点名称"), scene=kwargs.get("场景标识"))

        elif self.node_type == "文件节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = file_business(node_name=kwargs.get("节点名称"), operate_mode=kwargs.get("操作模式"),
                                      storage_set=kwargs.get("存储参数配置"), source_set=kwargs.get("源"),
                                      dest_set=kwargs.get("目标"), files_set=kwargs.get("文件配置"))

        elif self.node_type == "Sql节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_sql_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = sql_business(node_name=kwargs.get("节点名称"), opt_mode=kwargs.get("操作模式"),
                                     sql_config=kwargs.get("sql配置"), advance_set=kwargs.get("高级配置"))

        elif self.node_type == "指令模版节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_cmd_template_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = cmd_template_business(node_name=kwargs.get("节点名称"), cmd_temp_name=kwargs.get("指令任务模版"),
                                              use_temp_name=kwargs.get("应用指令模版名称"), advance_set=kwargs.get("高级配置"))

        elif self.node_type == "数据拼盘节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_edata_custom_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = edata_business(node_name=kwargs.get("节点名称"), edata=kwargs.get("数据拼盘名称"),
                                       use_edata_name=kwargs.get("应用数据拼盘名称"), advance_set=kwargs.get("高级配置"))

        elif self.node_type == "数据处理节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = datahandle_business(node_name=kwargs.get("节点名称"), mode=kwargs.get("处理模式"),
                                            var_name1=kwargs.get("变量1"), var_name2=kwargs.get("变量2"),
                                            rela_set=kwargs.get("关联列"), update_set=kwargs.get("更新列"),
                                            base_var=kwargs.get("基准变量"), output_type=kwargs.get("输出类型"),
                                            output_var=kwargs.get("输出变量名称"), output_cols=kwargs.get("输出列"),
                                            value_type=kwargs.get("赋值方式"))

        elif self.node_type == "可视化操作模拟节点":
            # 点击业务配置
            busi_iframe = "//iframe[@id='busi_crawler_node']"
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = crawler_business(node_name=kwargs.get("节点名称"), system_name=kwargs.get("目标系统"),
                                         element_config=kwargs.get("元素配置"), tree_set=kwargs.get("操作树"),
                                         advance_set=kwargs.get("高级配置"))

        elif self.node_type == "脚本节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = script_business(node_name=kwargs.get("节点名称"), script_name=kwargs.get("脚本"),
                                        ver_no=kwargs.get("版本号"), params=kwargs.get("参数列表"),
                                        advance_set=kwargs.get("高级配置"))

        elif self.node_type == "接口节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = interface_business(node_name=kwargs.get("节点名称"), interface=kwargs.get("接口"),
                                           request_body=kwargs.get("请求体内容"), request_header=kwargs.get("请求头列表"),
                                           params=kwargs.get("参数列表"), advance_set=kwargs.get("高级配置"))

        elif self.node_type == "报表节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = report_business(node_name=kwargs.get("节点名称"), opt_type=kwargs.get("操作方式"),
                                        obj_var=kwargs.get("变量名"), var_name=kwargs.get("变量选择"),
                                        var_map=kwargs.get("变量索引配置"), interface_name=kwargs.get("数据接口名称"),
                                        remark=kwargs.get("备注"), sample_data=kwargs.get("样例数据"))

        elif self.node_type == "邮件节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = email_business(node_name=kwargs.get("节点名称"), mode=kwargs.get("邮件模式"),
                                       params_set=kwargs.get("参数配置"))

        elif self.node_type == "AI节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = ai_business(node_name=kwargs.get("节点名称"), mode=kwargs.get("节点模式"),
                                    algorithm=kwargs.get("算法选择"), model=kwargs.get("模型"), var_name=kwargs.get("输入变量"),
                                    param_map=kwargs.get("对应关系配置"), interval=kwargs.get("预测步长"),
                                    advance_set=kwargs.get("高级配置"))

        elif self.node_type == "OCR节点":
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@class='tabs']//*[text()='业务配置']")))
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = ocr_business(node_name=kwargs.get("节点名称"), storage_set=kwargs.get("存储参数配置"),
                                     enable_filter_set=kwargs.get("启用过滤配置"), filter_set=kwargs.get("过滤配置"),
                                     advance_set=kwargs.get("高级配置"))

        elif self.node_type == "信息处理节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_tab']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = info_business(node_name=kwargs.get("节点名称"), mode=kwargs.get("操作模式"),
                                      info_desc=kwargs.get("信息描述"), show=kwargs.get("显示在运行信息的标题"),
                                      info=kwargs.get("信息明细"), download_set=kwargs.get("启用下载"),
                                      var_name=kwargs.get("变量选择"))

        elif self.node_type == "数据接入节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = data_access_business(node_name=kwargs.get("节点名称"), access_type=kwargs.get("接入类型"),
                                             access_task_name=kwargs.get("接入任务"), invoke_syn=kwargs.get("同步调用"),
                                             advance_set=kwargs.get("高级配置"))

        elif self.node_type == "告警节点":
            # 点击业务配置
            self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='业务配置']").click()
            # 切换到业务配置iframe
            busi_iframe = "//iframe[@id='busi_node']"
            self.browser.switch_to.frame(self.browser.find_element(By.XPATH, busi_iframe))
            # 等待页面加载
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
            node_name = alarm_business(node_name=kwargs.get("节点名称"), alarm_data_type=kwargs.get("告警类型"),
                                       alarm_plan=kwargs.get("告警计划"), alarm_rule=kwargs.get("告警规则"),
                                       invoke_syn=kwargs.get("同步调用"), advance_set=kwargs.get("高级配置"))

        else:
            raise KeyError("节点类型 {0} 错误".format(self.node_type))

        # iframe切到画流程图页面
        sleep(3)
        self.browser.switch_to.default_content()

        # 节点名称如果有修改，则重新保存节点描述
        if node_name:
            if node_name != self.original_node_name:
                log.info("节点名称有变动，重新保存节点描述")
                page_wait()
                sleep(1)
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(node_name)).click()
                sleep(1)
                # 点击描述下拉箭头
                self.browser.find_element(
                    By.XPATH, "//*[@id='node_desc_div']//*[contains(text(),'说明')]/following-sibling::div[1]/a").click()
                sleep(2)
                wait = WebDriverWait(self.browser, 30)
                wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='node_desc_text']")))
                sleep(1)
                self.browser.find_element(By.XPATH, "//*[@id='node_desc_text']").clear()
                self.browser.find_element(By.XPATH, "//*[@id='node_desc_text']").send_keys(node_name + "_节点说明")
                # 保存节点描述
                self.browser.find_element(By.XPATH, "//*[@onclick='node_desc_save();']//*[text()='保存']").click()
                alert = BeAlertBox()
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("设置节点描述信息")
                else:
                    log.warning("设置节点描述失败，失败提示: {0}".format(msg))
                set_global_var("ResultMsg", msg, False)
                self.browser.find_element(
                    By.XPATH, "//*[@id='node_desc_div']//*[contains(text(),'说明')]/following-sibling::div[1]/a").click()
        else:
            return

        # 保存流程图
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@title='保存流程图']").click()
        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存流程图成功")
        else:
            log.warning("保存流程图失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)

    def fetch_conf(self, **kwargs):
        # 切换到节点iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, get_global_var("NodeIframe"))))
        page_wait()
        self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='取数配置']").click()
        sleep(1)

        # 取数配置不是所有节点都有
        if self.node_type == "指令节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_cmd_node']"))
            cmd_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                      obj_type=kwargs.get("对象类型"), result_type=kwargs.get("结果类型"), cmd_name=kwargs.get("指令"),
                      temp_var=kwargs.get("变量名"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "指令模版节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_cmd_templ_node']"))
            cmd_temp_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                           obj_type=kwargs.get("对象类型"), result_type=kwargs.get("结果类型"),
                           cmd_name=kwargs.get("指令"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "数据拼盘节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_edata_custom_node']"))
            edata_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                        obj_type=kwargs.get("对象类型"), result_type=kwargs.get("结果类型"), cmd_name=kwargs.get("指令"),
                        value_type=kwargs.get("赋值方式"))

        elif self.node_type == "指标节点":
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_judge_node']"))
            judge_fetch(**kwargs)

        elif self.node_type == "脚本节点":
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'getDataScriptNode.html')]"))
            script_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                         value_type=kwargs.get("赋值方式"))

        elif self.node_type == "接口节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'getDataPortNode.html')]"))
            interface_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                            expression=kwargs.get("表达式"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "可视化操作模拟节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_crawler_node']"))
            crawler_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名"),
                          element_name=kwargs.get("元素名称"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "邮件节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataEmailNode.html')]"))
            email_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名称"),
                        var_type=kwargs.get("变量类型"), attach_type=kwargs.get("附件类型"),
                        file_name=kwargs.get("文件名"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "Sql节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[@id='getdata_sql_node']"))
            sql_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名"),
                      output_cols=kwargs.get("输出列"), get_col_name=kwargs.get("获取列名"),
                      value_type=kwargs.get("赋值方式"))

        elif self.node_type == "AI节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataIrNode.html')]"))
            ai_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"),
                     var_name=kwargs.get("变量名称"), value_type=kwargs.get("赋值方式"))

        elif self.node_type == "OCR节点":
            # 切换到取数配置iframe
            self.browser.switch_to.frame(
                self.browser.find_element(By.XPATH, "//iframe[contains(@src,'getdataOcrNode.html')]"))
            ocr_fetch(opt=kwargs.get("操作"), target_var=kwargs.get("目标变量"), var_name=kwargs.get("变量名"),
                      result_type=kwargs.get("取值类型"), get_col_name=kwargs.get("获取列名"),
                      value_type=kwargs.get("赋值方式"))

    def control_conf(self, **kwargs):

        # 切换到节点iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
        # 点击控制配置
        self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='控制配置']").click()
        # 切换到控制配置iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("ControlIframe")))
        sleep(1)
        node_control = NodeControl()

        # 条件依赖
        if kwargs.__contains__("条件依赖"):
            dependence = kwargs.get("条件依赖")
            node_control.condition_dependence(enable=dependence.get("状态"))

        # 开启循环
        if kwargs.__contains__("开启循环"):
            loop = kwargs.get("开启循环")
            node_control.set_loop(enable=loop.get("状态"), loopTagList=loop.get("循环条件"),
                                  loopType=loop.get("循环类型"), loopContent=loop.get("循环内容"))

        # 按列取数
        if kwargs.__contains__("按列取数"):
            col_var = kwargs.get("按列取数")
            node_control.get_value_by_col(enable=col_var.get("状态"), varSetList=col_var.get("变量列表"))

        # 高级配置
        if kwargs.__contains__("高级配置"):
            advance_set = kwargs.get("高级配置")
            node_control.advance_cfg(saveLog=advance_set.get("是否记录循环日志"), recordCycleNum=advance_set.get("循环日志记录条数"),
                                     outputLogPrintRuler=advance_set.get("输出日志打印规则"))

        # 逻辑分支控制
        if kwargs.__contains__("逻辑分支控制"):
            logic_branch = kwargs.get("逻辑分支控制")
            node_control.set_logic_branch(enable=logic_branch.get("状态"), branchType=logic_branch.get("逻辑分支类型"),
                                          meetCondition=logic_branch.get("满足条件"), unMeetCondition=logic_branch.get("不满足条件"),
                                          unCertainCondition=logic_branch.get("不确定条件"), dynamicCondition=logic_branch.get("动态值"))

    def operate_conf(self, array):
        # 切换到节点iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("NodeIframe")))
        # 点击操作配置
        self.browser.find_element(By.XPATH, "//*[@class='tabs']//*[text()='操作配置']").click()
        # 切换到操作配置iframe
        self.browser.switch_to.frame(self.browser.find_element(By.XPATH, get_global_var("OptIframe")))
        sleep(1)
        opt_action(array=array)
