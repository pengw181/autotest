# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/10 下午5:14


from common.variable.globalVariable import *
from app.Crawler.main.menu.chooseMenu import choose_menu
from common.page.func.pageMaskWait import page_wait
from common.page.func.alertBox import BeAlertBox
from time import sleep
from common.log.logger import log
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from app.VisualModeler.process.choreography.node.business.crawlerBusi import config_element
from app.VisualModeler.process.choreography.node.oprt.rightOpt import OptTreeServer
from app.VisualModeler.process.choreography.node.oprt.calculation import CalculationCenter


class CrawlerTemplate:

    def __init__(self):
        self.browser = get_global_var("browser")
        # 进入菜单
        choose_menu("配置-爬虫模版")
        page_wait()
        # 切换到爬虫模版配置iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='ifr-CrawlerApp2001']")))
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((
            By.XPATH, "//*[@id='crawlerCfg_form']//*[@id='templateName']/following-sibling::span[1]/input[1]")))
        page_wait()
        sleep(1)

    def choose(self, template_name):
        """
        :param template_name: 模版名称
        """
        input_ele = self.browser.find_element_by_xpath(
            "//*[@id='crawlerCfg_form']//*[@id='templateName']/following-sibling::span[1]/input[1]")
        input_ele.clear()
        input_ele.send_keys(template_name)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='查询']").click()
        page_wait()
        self.browser.find_element_by_xpath("//*[@field='templateName']//a[text()='{}']".format(template_name)).click()
        log.info("已选择爬虫模版: {}".format(template_name))

    def add(self, template_name, system_name, advance_set):
        """
        :param template_name: 模版名称
        :param system_name: 目标系统
        :param advance_set: 高级配置
        """
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='添加']").click()
        page_wait()
        # 切换到添加爬虫模版页面iframe
        self.browser.switch_to.frame(
            self.browser.find_element_by_xpath("//iframe[contains(@src,'crawlerTemplateEdit.html?type=add')]"))
        sleep(1)

        # 模版名称
        if template_name:
            self.browser.find_element_by_xpath("//*[@name='node_name']/preceding-sibling::input").clear()
            self.browser.find_element_by_xpath("//*[@name='node_name']/preceding-sibling::input").send_keys(template_name)
            log.info("设置模版名称: {}".format(template_name))

        # 目标系统
        if system_name:
            self.browser.find_element_by_xpath("//*[@id='platformId']/following-sibling::span//a").click()
            sleep(1)
            system_list = self.browser.find_element_by_xpath(
                "//*[contains(@id,'platformId') and text()='{}']".format(system_name))
            action = ActionChains(self.browser)
            action.move_to_element(system_list).click().perform()
            log.info("设置目标系统: {}".format(system_name))

        # 高级配置
        if advance_set:
            if advance_set.get("flag") == "是":
                timeout = advance_set.get("超时时间")
                retry_times = advance_set.get("超时重试次数")
                try:
                    enable_click = self.browser.find_element_by_xpath(
                        "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                    enable_click.click()
                    log.info("开启【高级配置】")
                except NoSuchElementException:
                    pass

                self.browser.find_element_by_xpath("//*[@name='timeOut']/preceding-sibling::input").clear()
                self.browser.find_element_by_xpath("//*[@name='timeOut']/preceding-sibling::input").send_keys(timeout)
                self.browser.find_element_by_xpath("//*[@name='tryTime']/preceding-sibling::input").clear()
                self.browser.find_element_by_xpath("//*[@name='tryTime']/preceding-sibling::input").send_keys(retry_times)
                log.info("设置高级模式")
                sleep(1)
            else:
                try:
                    self.browser.find_element_by_xpath("//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                except NoSuchElementException:
                    disable_click = self.browser.find_element_by_xpath(
                        "//*[@onclick='show_advanced_mode($(this))']//*[text()='关闭高级模式']")
                    disable_click.click()
                    log.info("关闭【高级配置】")

        # 点击保存
        self.browser.find_element_by_xpath("//*[@id='save_fetchContent']//*[text()='保存']").click()

        alert = BeAlertBox(back_iframe="default")
        msg = alert.get_msg()
        if alert.title_contains("操作成功"):
            log.info("保存模版配置成功")
        else:
            log.warn("保存模版配置失败，失败提示: {0}".format(msg))
        set_global_var("ResultMsg", msg, False)
        return True

    def update(self, obj, template_name, system_name, advance_set):
        """
        :param obj: 目标模版
        :param template_name: 模版名称
        :param system_name: 目标系统
        :param advance_set: 高级配置
        """
        self.choose(template_name=obj)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='修改']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 切换到修改爬虫模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'crawlerTemplateEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input")))

            # 模版名称
            if template_name:
                self.browser.find_element_by_xpath("//*[@name='node_name']/preceding-sibling::input").clear()
                self.browser.find_element_by_xpath("//*[@name='node_name']/preceding-sibling::input").send_keys(
                    template_name)
                log.info("设置模版名称: {}".format(template_name))

            # 目标系统
            if system_name:
                self.browser.find_element_by_xpath("//*[@id='platformId']/following-sibling::span//a").click()
                system_list = self.browser.find_element_by_xpath(
                    "//*[contains(@id,'platformId') and text()='{}']".format(system_name))
                action = ActionChains(self.browser)
                action.move_to_element(system_list).perform()
                log.info("设置目标系统: {}".format(system_name))

            # 高级配置
            if advance_set:
                if advance_set.get("flag") == "是":
                    timeout = advance_set.get("超时时间")
                    retry_times = advance_set.get("超时重试次数")
                    try:
                        enable_click = self.browser.find_element_by_xpath(
                            "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                        enable_click.click()
                        log.info("开启【高级配置】")
                    except NoSuchElementException:
                        pass

                    self.browser.find_element_by_xpath("//*[@name='timeOut']/preceding-sibling::input").clear()
                    self.browser.find_element_by_xpath("//*[@name='timeOut']/preceding-sibling::input").send_keys(timeout)
                    self.browser.find_element_by_xpath("//*[@name='tryTime']/preceding-sibling::input").clear()
                    self.browser.find_element_by_xpath("//*[@name='tryTime']/preceding-sibling::input").send_keys(
                        retry_times)
                    log.info("设置高级模式")
                    sleep(1)
                else:
                    try:
                        self.browser.find_element_by_xpath(
                            "//*[@onclick='show_advanced_mode($(this))']//*[text()='开启高级模式']")
                    except NoSuchElementException:
                        disable_click = self.browser.find_element_by_xpath(
                            "//*[@onclick='show_advanced_mode($(this))']//*[text()='关闭高级模式']")
                        disable_click.click()
                        log.info("关闭【高级配置】")

            # 点击保存
            self.browser.find_element_by_xpath("//*[@id='save_fetchContent']//*[text()='保存']").click()

            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("保存模版配置成功")
            else:
                log.warn("保存模版配置失败，失败提示: {0}".format(msg))
            set_global_var("ResultMsg", msg, False)

    def delete(self, obj):
        """
        :param obj: 目标模版
        """
        self.choose(template_name=obj)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='删除']").click()
        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains(obj, auto_click_ok=False):
            alert.click_ok()
            sleep(1)
            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("{0} 删除成功".format(obj))
            else:
                log.warn("{0} 删除失败，失败提示: {1}".format(obj, msg))
        else:
            log.warn("{0} 删除失败，失败提示: {1}".format(obj, msg))
        set_global_var("ResultMsg", msg, False)

    def element_config(self, template_name, element_config):
        """
        :param template_name: 模版名称
        :param element_config: 元素配置，数组
        """
        self.choose(template_name=template_name)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='修改']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 切换到修改爬虫模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'crawlerTemplateEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input")))

            # 调用vm爬虫节点的元素配置方法
            config_element(elements=element_config)

    def element_tree_set(self, template_name, tree_set):
        """
        :param template_name: 模版名称
        :param tree_set: 操作树，数组
        :return:
        """
        self.choose(template_name=template_name)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='修改']").click()
        alert = BeAlertBox(back_iframe=False, timeout=1)
        exist = alert.exist_alert
        if exist:
            set_global_var("ResultMsg", alert.get_msg(), False)
        else:
            # 切换到修改爬虫模版页面iframe
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.frame_to_be_available_and_switch_to_it((
                By.XPATH, "//iframe[contains(@src,'crawlerTemplateEdit.html?type=edit')]")))
            sleep(1)
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input")))

            tree = OptTreeServer(location=2)
            for tree_step in tree_set:
                # 右键操作节点
                r_click_obj = tree_step.get("对象")
                r_opt = tree_step.get("右键操作")
                tree.r_click_opt(obj=r_click_obj, opt=r_opt)

                # 选择右键操作
                r_opt = tree_step.get("右键操作")
                if r_opt == "添加条件":
                    if_set = tree_step.get("条件配置")
                    if if_set.get("else") == "是":
                        enable_else_flag = True
                    else:
                        enable_else_flag = False
                    tree.add_if(if_array=if_set.get("if"), enable_else=enable_else_flag)

                elif r_opt == "添加循环":
                    loop_set = tree_step.get("循环配置")
                    tree.add_loop(where=1, loop_type=loop_set.get("循环类型"), loop_info=tree_step.get("循环配置"))

                elif r_opt == "添加步骤":
                    tree.add_step(steps=tree_step.get("元素名称"))

                elif r_opt == "添加操作":
                    opt_config = tree_step.get("运算配置")
                    cal = CalculationCenter(oprt_type=opt_config.get("运算类型"))
                    # 设置条件
                    if opt_config.__contains__("条件"):
                        cal.cal_condition(array=opt_config.get("条件"))
                    # 启动运算配置
                    cal.cal_set(params=opt_config.get("配置"))

                elif r_opt == "添加异常处理":
                    # catch
                    js = 'return $("#is_cnd_catch")[0].checked;'
                    status = self.browser.execute_script(js)
                    log.info("【CATCH】勾选状态: {0}".format(status))

                    enable_catch_element = self.browser.find_element_by_xpath("//*[@for='is_cnd_catch']")
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_catch_element)
                    if tree_step.get("启用CATCH") == "是":
                        if not status:
                            enable_catch_element.click()
                            log.info("开启【CATCH】")
                    else:
                        if status:
                            enable_catch_element.click()
                            log.info("关闭【CATCH】")
                        else:
                            log.info("【CATCH】标识为否，不开启")

                    # finally
                    js = 'return $("#is_cnd_finally")[0].checked;'
                    status = self.browser.execute_script(js)
                    log.info("【FINALLY】勾选状态: {0}".format(status))

                    enable_finally_element = self.browser.find_element_by_xpath("//*[@for='is_cnd_finally']")
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", enable_finally_element)
                    if tree_step.get("启用FINALLY") == "是":
                        if not status:
                            enable_finally_element.click()
                            log.info("开启【FINALLY】")
                    else:
                        if status:
                            enable_finally_element.click()
                            log.info("关闭【FINALLY】")
                        else:
                            log.info("【CATCH】标识为否，不开启")

                elif r_opt == "删除":
                    tree.delete()

                else:
                    raise KeyError("不支持的右键操作: {0}".format(r_opt))

    def data_clear(self, obj, fuzzy_match=False):
        """
        :param obj: 模版名称
        :param fuzzy_match: 是否模糊查询，使用关键字开头模糊查询
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        self.browser.find_element_by_xpath(
            "//*[@id='crawlerCfg_form']//*[@id='templateName']/following-sibling::span[1]/input[1]").clear()
        self.browser.find_element_by_xpath(
            "//*[@id='crawlerCfg_form']//*[@id='templateName']/following-sibling::span[1]/input[1]").send_keys(obj)
        self.browser.find_element_by_xpath("//*[@id='crawlerCfg_form']//span[text()='查询']").click()
        page_wait()
        if fuzzy_match:
            record_element = self.browser.find_elements_by_xpath(
                "//*[@field='templateName']/*[contains(@class,'templateName')]/*[starts-with(text(),'{0}')]".format(obj))
        else:
            record_element = self.browser.find_elements_by_xpath(
                "//*[@field='templateName']/*[contains(@class,'templateName')]/*[text()='{0}']".format(obj))
        if len(record_element) > 0:
            exist_data = True

            while exist_data:
                pe = record_element[0]
                search_result = pe.text
                pe.click()
                log.info("选择: {0}".format(search_result))
                # 删除
                self.browser.find_element_by_xpath("//*[text()='删除']").click()
                alert = BeAlertBox(back_iframe="default")
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
                            record_element = self.browser.find_elements_by_xpath(
                                "//*[@field='templateName']/*[contains(@class,'templateName')]/*[starts-with(text(),'{0}')]".format(
                                    obj))
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
                    log.warn("{0} 清理失败，失败提示: {1}".format(obj, msg))
                    set_global_var("ResultMsg", msg, False)

        else:
            # 查询结果为空,结束处理
            log.info("查询不到满足条件的数据，无需清理")
            pass
