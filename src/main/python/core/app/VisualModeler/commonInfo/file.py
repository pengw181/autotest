# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午11:43

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from src.main.python.lib.upload import upload
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.pageMaskWait import page_wait
from src.main.python.core.app.VisualModeler.doctorWho import DoctorWho
from src.main.python.db.SQLHelper import SQLUtil
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class File:

    def __init__(self, catalog):
        self.browser = gbl.service.get("browser")
        self.catalog = catalog
        self.root_flag = False
        dw = DoctorWho()
        if catalog == "personal":
            dw.choose_menu("常用信息管理-文件目录管理-个人目录")
            self.browser.switch_to.frame(self.browser.find_element(
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/catalogPersonalDef.html')]"))
            log.info("进入个人目录")
        elif catalog == "system":
            dw.choose_menu("常用信息管理-文件目录管理-系统目录")
            self.browser.switch_to.frame(self.browser.find_element(
                By.XPATH, "//iframe[contains(@src, '/VisualModeler/html/commonInfo/catalogSystemDef.html')]"))
            log.info("进入系统目录")
        else:
            raise KeyError("catalog仅支持personal/system")
        page_wait()
        sleep(1)

        # 获取系统目录
        if gbl.service.get('SystemCatalogPath') is None:
            sql_util = SQLUtil(db=gbl.service.get("environment"), schema="main")
            sql = """ SELECT A.CATALOG_PATH AS catalogPath FROM TN_CATALOG_DEF A
                        WHERE A.CATALOG_TYPE = '1'
                        AND A.BELONG_ID = '{0}' AND A.DOMAIN_ID = '{1}'""".format(
                gbl.service.get("BelongID"), gbl.service.get("DomainID"))
            system_path = sql_util.select(sql)
            gbl.service.set('SystemCatalogPath', system_path)
        system_catalog_path = gbl.service.get('SystemCatalogPath').split("/")
        self.system_catalog_path = system_catalog_path[-1]
        log.info(self.system_catalog_path)

    def choose_dir(self, dir_name):
        """
        :param dir_name: 目标目录
        :return: 返回element对象,并更新root_flag
        """
        if self.catalog == "personal" and dir_name == "personal":
            # 父目录是根目录
            dir_name = gbl.service.get("LoginUser")
        if dir_name == "system":
            dir_name = self.system_catalog_path
        dir_elements = self.browser.find_elements(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(dir_name))
        dir_element = None
        for element in dir_elements:
            if element.is_displayed():
                self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                log.info("已选择目录: {0}".format(dir_name))
                page_wait()
                sleep(1)
                dir_element = element
                break
        return dir_element

    def dir_r_click(self, dir_name):
        """
        :param dir_name: 目标目录
        """
        # 需要先点击版本后开始操作
        dir_element = self.choose_dir(dir_name)

        # 焦点定位到文件名元素上
        self.browser.execute_script("arguments[0].scrollIntoView(true);", dir_element)
        # 指定脚本文件右键
        action = ActionChains(self.browser)
        action.context_click(dir_element).perform()
        sleep(1)

    def mkdir(self, parent_dir, dir_name):
        """
        :param parent_dir: 目标目录
        :param dir_name: 目录名
        """
        self.dir_r_click(dir_name=parent_dir)
        page_wait()
        sleep(1)

        add_elements = self.browser.find_elements(By.XPATH, "//*[text()='添加目录']")
        for element in add_elements:
            if element.is_displayed():
                element.click()
                break

        # 切换到添加目录的iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'catalogDefOperate.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='pathName']/preceding-sibling::input")))

        if parent_dir == "personal":
            # 父目录是根目录
            parent_dir = gbl.service.get("LoginUser")
        cur_parent = self.browser.find_element(By.XPATH, "//*[@name='parentPath']").get_attribute("value")
        if parent_dir == "system":
            parent_dir = self.system_catalog_path
        if parent_dir != cur_parent:
            raise Exception("当前选择目录【{0}】，预期选择【{1}】".format(cur_parent, parent_dir))
        else:
            # 输入目录名称
            self.browser.find_element(By.XPATH, "//*[@name='pathName']/preceding-sibling::input").send_keys(dir_name)
            self.browser.find_element(By.XPATH, "//*[@onclick='addPathSave()']//*[text()='提交']").click()

            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("操作成功"):
                log.info("目录 {0} 添加成功".format(dir_name))
            else:
                log.warning("目录 {0} 添加失败，失败提示: {1}".format(dir_name, msg))
            gbl.temp.set("ResultMsg", msg)

    def update_dir(self, target_dir, new_dir):
        """
        :param target_dir: 目标目录
        :param new_dir: 目录名
        """
        self.dir_r_click(dir_name=target_dir)
        page_wait()

        update_elements = self.browser.find_elements(By.XPATH, "//*[text()='修改目录']")
        for element in update_elements:
            if element.is_displayed():
                element.click()

        # 切换到修改目录的iframe
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'updCatalogDefOperate.html')]")))
        page_wait()
        sleep(1)

        try:
            wait = WebDriverWait(self.browser, 30)
            wait.until(ec.text_to_be_present_in_element_value((By.XPATH, "//*[@name='pathName']"), target_dir))

            # 输入目录名称
            self.browser.find_element(By.XPATH, "//*[@name='pathName']/preceding-sibling::input").clear()
            self.browser.find_element(By.XPATH, "//*[@name='pathName']/preceding-sibling::input").send_keys(new_dir)
            self.browser.find_element(By.XPATH, "//*[@onclick='updPathSave()']//*[text()='提交']").click()

            alert = BeAlertBox()
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("目录 {0} 修改成功".format(target_dir))
            else:
                log.warning("目录 {0} 修改失败，失败提示: {1}".format(target_dir, msg))
            gbl.temp.set("ResultMsg", msg)
        except TimeoutError:
            raise Exception("选择目录错误")

    def delete_dir(self, dir_name):
        """
        :param dir_name: 目标目录
        """
        self.dir_r_click(dir_name=dir_name)
        page_wait()

        delete_elements = self.browser.find_elements(By.XPATH, "//*[text()='删除目录']")
        dir_exist = False
        for element in delete_elements:
            if element.is_displayed():
                element.click()
                dir_exist = True

                alert = BeAlertBox(back_iframe=False)
                msg = alert.get_msg()
                if alert.title_contains(dir_name, auto_click_ok=False):
                    alert.click_ok()
                    sleep(1)
                    alert = BeAlertBox(back_iframe=False)
                    msg = alert.get_msg()
                    if alert.title_contains("成功"):
                        log.info("目录{0} 删除成功".format(dir_name))
                    else:
                        log.warning("目录{0} 删除失败，失败提示: {1}".format(dir_name, msg))
                else:
                    log.warning("目录{0} 删除失败，失败提示: {1}".format(dir_name, msg))
                gbl.temp.set("ResultMsg", msg)
        return dir_exist

    def upload_file(self, dir_name, catalog, file_name):
        """
        :param dir_name: 目标目录
        :param catalog: 文件类别
        :param file_name: 文件名
        """
        # 选择目录
        self.choose_dir(dir_name)
        self.browser.find_element(By.XPATH, "//*[@id='uploadBtn']//*[text()='上传文件']").click()
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'catalogDefUpload.html')]")))
        sleep(1)
        wait = WebDriverWait(self.browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(@for,'filebox_file_id_')]")))

        log.info("开始上传文件: {0}".format(file_name))
        upload(file_name=file_name, catalog=catalog)
        sleep(1)
        self.browser.find_element(By.XPATH, "//*[@onclick='uploadFiles()']//*[text()='上传']").click()

        alert = BeAlertBox()
        msg = alert.get_msg()
        if alert.title_contains("上传成功"):
            # 获取文件列表第一个文件的文件名，与上传文件名比较，判断是否上传正确
            sleep(1)
            files = self.browser.find_elements(
                By.XPATH, "//*[@value='{0}']/..//*[contains(@id,'catalogDef_info_tab_')][1]/*[@field='fileName']/div".format(
                    self.catalog))
            for f in files:
                if f.is_displayed():
                    gbl.temp.set("CheckFileName", f.text)
                    log.info("当前目录【{0}】下，第一个文件名: {1}".format(dir_name, gbl.temp.get("CheckFileName")))
                    break
        else:
            log.warning("目录【{0}】上传文件 {1} 失败，失败提示: {2}".format(dir_name, file_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def choose_file(self, dir_name, file_name):
        """
        :param dir_name: 目标目录
        :param file_name: 文件名
        """
        self.choose_dir(dir_name)
        self.browser.find_element(
            By.XPATH, "//*[@value='{0}']/..//*[@name='fileName']/preceding-sibling::input".format(
                self.catalog)).send_keys(file_name)
        self.browser.find_element(
            By.XPATH, "//*[@value='{0}']/..//*[@id='queryBtn']//*[text()='查询']".format(self.catalog)).click()
        sleep(1)

        self.browser.find_element(
            By.XPATH, "//*[@value='{0}']/..//*[contains(@id,'catalogDef_info_tab_')][1]/*[@field='fileName']/div".format(
                self.catalog)).click()
        log.info("选择文件: {0}".format(file_name))

    def download_file(self, dir_name, file_name):
        """
        :param dir_name: 目标目录
        :param file_name: 文件名
        """
        # 选择文件
        self.choose_file(dir_name, file_name)

        self.browser.find_element(
            By.XPATH, "//*[@value='{0}']/..//*[@funcid='systemFile_down' and contains(@href,'{1}')]".format(
                self.catalog, file_name)).click()
        sleep(3)
        log.info("下载文件: {0}".format(file_name))

    def download_file_batch(self, dir_name, file_names):
        """
        :param dir_name: 目标目录
        :param file_names: 文件名，file_names 为list，所有文件都在第一页，不支持跨页选择数据
        """
        # 选择目录
        dir_element = self.choose_dir(dir_name)
        dir_element.click()
        sleep(1)
        log.info("开始批量下载文件，待下载文件列表: {0}".format(", ".join(file_names)))
        for file in file_names:
            try:
                self.browser.find_element(
                    By.XPATH, "//*[@value='{0}']/..//*[contains(@id,'catalogDef')]/*[@field='fileName']//*[text()='{1}']".format(
                        self.catalog, file)).click()
                log.info("选择文件: {0}".format(file))
                sleep(1)
            except NoSuchElementException:
                log.warning("文件: {0}不在第一页列表中".format(file))
                raise
        self.browser.find_element(By.XPATH, "//*[@id='downloadBtn']//*[text()='批量下载']").click()
        log.info("点击批量下载")

    def delete_file(self, dir_name, file_name):
        """
        :param dir_name: 目标目录
        :param file_name: 文件名
        """
        # 选择文件
        self.choose_file(dir_name, file_name)
        # 点击删除文件
        self.browser.find_element(
            By.XPATH, "//*[@value='{0}']/..//*[@funcid='systemFile_del' and contains(@href,'{1}')]".format(
                self.catalog, file_name)).click()
        log.info("点击删除文件")

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要删除{0}吗".format(file_name), auto_click_ok=False):
            alert.click_ok()

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("目录【{0}】删除文件: {1} 成功".format(dir_name, file_name))
            else:
                log.warning("目录【{0}】删除文件: {1} 失败，返回结果: {2}".format(dir_name, file_name, msg))
        else:
            log.warning("目录【{0}】删除文件: {1} 失败，返回结果: {2}".format(dir_name, file_name, msg))
        gbl.temp.set("ResultMsg", msg)

    def delete_file_batch(self, dir_name, file_names):
        """
        :param dir_name: 目标目录
        :param file_names: 文件名，file_names 为list，所有文件都在第一页，不支持跨页选择数据
        :return:
        """
        # 选择目录
        dir_name = self.choose_dir(dir_name)
        dir_name.click()
        sleep(1)
        for file in file_names:
            try:
                self.browser.find_element(
                    By.XPATH, "//*[@value='{0}']/..//*[contains(@id,'catalogDef')]/*[@field='fileName']//*[text()='{1}']".format(
                        self.catalog, file)).click()
                log.info("选择文件: {0}".format(file))
                sleep(1)
            except NoSuchElementException:
                log.warning("文件: {0}不在第一页列表中".format(file))
                raise
        self.browser.find_element(By.XPATH, "//*[@id='deleteBtn']//*[text()='批量删除']").click()
        log.info("点击批量删除")

        alert = BeAlertBox(back_iframe=False)
        msg = alert.get_msg()
        if alert.title_contains("您确定需要批量删除吗", auto_click_ok=False):
            alert.click_ok()

            alert = BeAlertBox(back_iframe=False)
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("目录【{0}】删除文件: {1} 成功".format(dir_name, ",".join(file_names)))
            else:
                log.warning("目录【{0}】删除文件: {1} 失败，返回结果: {2}".format(dir_name, ",".join(file_names), msg))
        else:
            log.warning("目录【{0}】删除文件: {1} 失败，返回结果: {2}".format(dir_name, ",".join(file_names), msg))
        gbl.temp.set("ResultMsg", msg)

    def data_clear(self, obj):
        """
        :param obj: 目标目录
        """
        # 用于清除数据，在测试之前执行, 使用关键字开头模糊查询
        dir_elements = self.browser.find_elements(By.XPATH, "//*[@class='tree-title' and text()='{0}']".format(obj))
        if len(dir_elements) == 0:
            log.info("指定目录 {0} 不存在，无需清理".format(obj))
            return

        for element in dir_elements:
            if element.is_displayed():
                self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                log.info("已选择目录: {0}".format(obj))
                self.delete_dir(obj)
                break
