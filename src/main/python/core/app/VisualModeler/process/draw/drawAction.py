# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:30

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from src.main.python.core.app.VisualModeler.process.draw.processInfo import Process
from src.main.python.core.app.VisualModeler.process.draw.node import Node
from src.main.python.core.app.VisualModeler.process.draw.processJson import ProcessNodeJson
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.windows import WindowHandles
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.lib.positionPanel import getPanelXpath
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class DrawProcess:

    def __init__(self, process_name):
        self.browser = gbl.service.get("browser")
        self.process_name = process_name
        self.current_node_count = 0
        self.last_node_name = "开始"
        try:
            current_win_handle = WindowHandles()
            current_win_handle.switch("流程图编辑器")
        except NoSuchWindowException:
            log.info("当前不在流程图编辑页面，自动进入画流程图页面")
            Process().search(query={"关键字": process_name}, need_choose=True)
            self.browser.find_element(By.XPATH, "//*[text()='画流程图']").click()

            # 保存新窗口，并切换到新窗口
            current_win_handle = WindowHandles()
            current_win_handle.save("流程图编辑器")
            current_win_handle.switch("流程图编辑器")
        finally:
            page_wait()
            # # 如果操作过程中，顶部保存按钮不可见，先刷新当前页面
            # try:
            #     save_button = self.browser.find_element(By.XPATH, "//*[contains(@class,'ico_save')]")
            #     if save_button.is_displayed() is False:
            #         log.info("保存按钮不可见，刷新页面")
            #         self.browser.refresh()
            # except NoSuchElementException:
            #     log.info("保存按钮不存在，刷新页面")
            #     self.browser.refresh()
            sleep(1)

    def get_new_location(self, is_end_node=False):
        # 获取开始节点
        start_node_element = self.browser.find_element(
            By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[@class='ico_start']")
        location = start_node_element.location
        x = location['x']
        y = location['y']
        size_x = start_node_element.size["width"]
        size_y = start_node_element.size["height"]
        x -= size_x
        y -= size_y
        log.info("开始节点坐标：[%s, %s]" % (x, y))

        pnj = ProcessNodeJson(process_name=self.process_name)
        self.current_node_count = pnj.count_node()
        self.last_node_name = pnj.get_last_node_name()
        maxNodePerLine = int(gbl.service.get("maxNodePerLine"))
        # 去掉开始节点
        self.current_node_count -= 1
        # 计算下一个节点放在第几行，每一行最多4-6个节点
        which_line = self.current_node_count // maxNodePerLine   # 8 // 5 = 1
        which_row = self.current_node_count % maxNodePerLine     # 8 % 5 = 3
        # x = 150 * (which_row + 1) + 100 * which_row
        x = 120 * (which_row + 1) + 80 * which_row
        y = -30 + 120 * which_line
        if is_end_node:
            # 开始、结束节点高度只有24，普通节点高度64，折中结束节点y轴加20
            y += 18
        log.info("下一个节点距离开始节点坐标：[%s, %s]" % (x, y))
        self.current_node_count += 1
        return start_node_element, x, y

    def check_node_located(self, node_name=None):
        # 验证节点是否已加入画布中
        try:
            if node_name == '结束节点':
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[@class='ico_end']")
            else:
                self.browser.find_element(
                    By.XPATH, "//*[contains(@class, 'GooFlow_item') and contains(@title,'节点未保存')]//*[text()='{}']".format
                    (node_name))
            # self.browser.execute_script("arguments[0].scrollIntoView(true);", new_node_element)
            log.info("节点已放置在画布中")
        except NoSuchElementException as e:
            log.error("节点加入画布异常，请查看流程图")
            raise e

    # 选择节点并将节点放到画布坐标上
    def locate_node(self, node_type, x_loc=None, y_loc=None):
        # 定义鼠标对象
        action = ActionChains(self.browser)
        log.info("开始画流程图")
        self.browser.switch_to.parent_frame()
        page_wait()
        sleep(1)

        # 获取下一个节点摆放坐标
        if node_type != "结束节点":
            start_node_element, xset, yset = self.get_new_location()
        else:
            start_node_element, xset, yset = self.get_new_location(is_end_node=True)

        # 如果指定具体位置，则以该位置为准
        location = start_node_element.location
        if x_loc is not None:
            xset = x_loc - location['x']
        if y_loc is not None:
            yset = y_loc - location['y'] + 30   # 加上节点高度/2
        log.info("由于指定了新节点坐标，使用指定坐标偏值（相较于开始节点）：[{}, {}]".format(xset, yset))

        # 如果当前流程图中节点较多，在添加新节点前，先滚动屏幕
        if self.current_node_count > 20:
            start_node_element = self.browser.find_element(
                By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[@class='ico_start']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", start_node_element)
            sleep(1)

        # 如果当前屏幕已布满，则每次移到最后一个节点
        # if self.current_node_count > 30:
        #     last_node = self.browser.find_element(By.XPATH, 
        #         "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(self.last_node_name))
        #     self.browser.execute_script("arguments[0].scrollIntoView(true);", last_node)
        #     sleep(1)

        if node_type == "指令节点":
            # 添加指令节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_instruction']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("指令节点")

        elif node_type == "通用节点":
            # 添加通用节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_usual']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("通用节点")

        elif node_type == "文件节点":
            # 添加文件节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_file']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("文件节点")

        elif node_type == "脚本节点":
            # 添加脚本节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_script']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("脚本节点")

        elif node_type == "接口节点":
            # 添加接口节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_port']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("接口节点")

        elif node_type == "Sql节点" or node_type == "数据库节点":
            # 添加数据库节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_sql']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("数据库节点")

        elif node_type == "指令模版节点":
            # 添加指令模版节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_instructionsTemplate']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("指令模版节点")

        elif node_type == "数据拼盘节点":
            # 添加数据拼盘节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_instructionsEdataCustom']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("数据拼盘节点")

        elif node_type == "可视化操作模拟节点":
            # 添加可视化操作模拟节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_datafetch']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("可视化操作模拟节点")

        elif node_type == "信息处理节点":
            # 添加信息处理节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_infohandle']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("信息处理节点")

        elif node_type == "数据处理节点":
            # 添加数据处理节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_datahandle']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("数据处理节点")

        elif node_type == "AI节点":
            # 添加AI节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_ir']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("AI节点")

        elif node_type == "OCR节点":
            # 添加OCR节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_ocr']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("OCR节点")

        elif node_type == "邮件节点":
            # 添加邮件节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_email']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("邮件节点")

        elif node_type == "数据接入节点":
            # 添加数据接入节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_dataAccess']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("数据接入节点")

        elif node_type == "告警节点":
            # 添加告警节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_alarm']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("告警节点")

        elif node_type == "报表节点":
            # 添加报表节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_report']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("报表节点")

        elif node_type == "结束节点":
            # 添加结束节点
            self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_end']").click()
            action.move_to_element_with_offset(start_node_element, xset, yset).click().perform()
            sleep(1)

            # 验证节点是否成功放入画布
            self.check_node_located("结束节点")

            # new_node_element = self.browser.find_element(
            #     By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[@class='ico_end']")
            # try:
            #     self.browser.execute_script("arguments[0].scrollIntoView(true);", new_node_element)
            #     log.info("节点已放置在画布中")
            # except NoSuchElementException:
            #     log.error("节点加入画布异常，请查看流程图")

        else:
            raise KeyError("未知节点类型")

        # 保存流程图
        self.save()

    def combine(self, source_node_name, target_node_name, logic):

        action = ActionChains(self.browser)
        page_wait()
        log.info("开始给节点连线")

        # source节点
        source_element = self.browser.find_element(
            By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(source_node_name))

        # target节点
        target_element = self.browser.find_element(
            By.XPATH, "//*[contains(@class, 'GooFlow_item')]//*[text()='{0}']".format(target_node_name))

        # 连线
        self.browser.find_element(By.XPATH, "//*[@id='aisee_btn_direct']").click()
        sleep(1)
        # self.browser.execute_script("arguments[0].scrollIntoView(true);", source_element)
        action.drag_and_drop(source_element, target_element).perform()
        sleep(1)

        # 设置关联关系
        pnj = ProcessNodeJson(process_name=self.process_name)
        from_location, to_location, line_type = pnj.get_line_location(
            source_node_name=source_node_name,
            target_node_name=target_node_name)
        try:
            line = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cn_line_') and @from='{0}' and @to='{1}']".format(from_location, to_location))
        except NoSuchElementException:
            line = self.browser.find_element(
                By.XPATH, "//*[contains(@id,'cn_line_')]//*[@text-anchor='middle' and not(text())]/..")

        action = ActionChains(self.browser)
        action.double_click(line).perform()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src,'./node/lineNode.html')]")))

        # 加个等待
        wait = WebDriverWait(self.browser, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='line_relex']/preceding-sibling::span[1]/a")))
        self.browser.find_element(By.XPATH, "//*[@name='line_relex']/preceding-sibling::span[1]/a").click()
        panel_xpath = getPanelXpath(10)
        try:
            self.browser.find_element(By.XPATH, panel_xpath + "//*[text()='{0}']".format(logic)).click()
        except NoSuchElementException:
            # 自定义值
            self.browser.find_element(By.XPATH, "//*[@name='line_relex']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='line_relex']/preceding-sibling::input").send_keys(logic)
            self.browser.find_element(By.XPATH, "//*[@name='line_relex']/preceding-sibling::span[1]/a").click()
        self.browser.find_element(By.XPATH, "//*[@onclick='add_line_config_info();']").click()
        log.info("设置连线关系: {}".format(logic))
        self.browser.switch_to.default_content()

        if line_type == 2:
            # 改变连线方式
            line.click()
            self.browser.find_element(By.XPATH, "//*[@class='b_l2']").click()
            sleep(1)

        # 保存流程图
        self.save()

    def save(self):
        # 保存流程图
        # wait = WebDriverWait(self.browser, 10)
        # wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(@class,'ico_save')]")))
        self.browser.find_element(By.XPATH, "//*[contains(@class,'ico_save')]").click()
        log.info("保存流程图")

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("流程保存成功")
        else:
            log.warning("流程保存失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    def set_end_node(self, status):
        end_nodes = self.browser.find_elements(By.XPATH, "//*[@class='span openwin']/..")
        cur_end_attr_id = None
        deal_end_node_ids = gbl.service.get("EndNodeID")
        if deal_end_node_ids is None:
            deal_end_node_ids = []
        for _end_node in end_nodes:
            cur_end_attr_id = _end_node.get_attribute("id")
            if cur_end_attr_id in deal_end_node_ids:
                continue
            else:
                deal_end_node_ids.append(cur_end_attr_id)
                break
        gbl.service.set("EndNodeID", deal_end_node_ids)
        end_node = self.browser.find_element(By.XPATH, "//*[@id='{}']//*[@class='span openwin']".format(cur_end_attr_id))
        # end_node = self.browser.find_element(By.XPATH, "//*[@class='span openwin' and text()='正常']")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", end_node)
        # 双击进入节点
        action = ActionChains(self.browser)
        action.double_click(end_node).perform()
        sleep(1)
        # 切换到结束节点配置iframe
        self.browser.switch_to.frame(
            self.browser.find_element(By.XPATH, "//iframe[contains(@src,'./node/endNode.html')]"))
        self.browser.find_element(By.XPATH, "//*[@id='status']/following-sibling::span//a").click()
        if status in ["正常", "异常", "未知"]:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.element_to_be_clickable((
                By.XPATH, "//*[contains(@id,'status') and text()='{0}']".format(status))))
            self.browser.find_element(By.XPATH, "//*[contains(@id,'status') and text()='{0}']".format(status)).click()
        else:
            wait = WebDriverWait(self.browser, 10)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='status']/preceding-sibling::input")))
            self.browser.find_element(By.XPATH, "//*[@name='status']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='status']/preceding-sibling::input").send_keys(status)
        sleep(1)
        self.browser.find_element(By.XPATH, "//*[@id='saveEndNodeBtn']//*[text()='提交']").click()
        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("成功"):
            log.info("结束节点设置成功")
        else:
            log.warning("结束节点设置失败，失败提示: {0}".format(msg))
        gbl.temp.set("ResultMsg", msg)

    @staticmethod
    def node_business_conf(node_type, node_name, **kwargs):
        node = Node(node_type=node_type, node_name=node_name)
        node.business_conf(**kwargs)

    @staticmethod
    def node_fetch_conf(node_type, node_name, **kwargs):
        node = Node(node_type=node_type, node_name=node_name)
        node.fetch_conf(**kwargs)

    @staticmethod
    def node_control_conf(node_type, node_name, **kwargs):
        node = Node(node_type=node_type, node_name=node_name)
        node.control_conf(**kwargs)

    @staticmethod
    def node_operate_conf(node_type, node_name, **kwargs):
        node = Node(node_type=node_type, node_name=node_name)
        node.operate_conf(**kwargs)
