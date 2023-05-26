# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午10:58

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.chooseDir import choose_ftp_dir, choose_file_dir
from src.main.python.lib.regular import RegularCube
from src.main.python.lib.input import set_text_enable_var
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def ocr_business(node_name, storage_set, enable_filter_set, filter_set, advance_set):
    """
    :param node_name: 节点名称
    :param storage_set: 存储参数配置，字典
    :param enable_filter_set: 启用过滤配置，开启/关闭
    :param filter_set: 过滤配置，数组
    :param advance_set: 高级配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "文件节点",
            "节点名称": "文件节点",
            "业务配置": {
                "节点名称": "文件节点1",
                "存储参数配置": {
                    "存储类型": "本地",
                    "目录": "OCR",
                    "变量引用": "否"
                },
                "启用过滤配置": "开启",
                "过滤配置": [
                    {
                        "类型": "关键字",
                        "文件名": "abc",
                        "文件类型": "jpeg"
                    },
                    {
                        "类型": "关键字",
                        "文件名": "4301",
                        "文件类型": "全部"
                    },
                    {
                        "类型": "正则匹配",
                        "文件名": {
                            "设置方式": "添加",
                            "正则模版名称": "pw自动化正则模版",
                            "标签配置": [
                                {
                                    "标签": "自定义文本",
                                    "值": "pw",
                                    "是否取值": "绿色"
                                },
                                {
                                    "标签": "任意字符",
                                    "值": "1到多个",
                                    "是否取值": "绿色"
                                }
                            ]
                        },
                        "文件类型": "全部"
                    }
                ],
                "高级配置": {
                    "状态": "开启",
                    "超时时间": "600",
                    "超时重试次数": "2"
                }
            }
        }
    }
    """
    browser = gbl.service.get("browser")
    log.info("开始配置OCR节点业务配置")
    # 等待页面加载，自动加载节点模式、算法选择
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='algorithmId']/preceding-sibling::input")))
    # 等待算法加载
    sleep(1)

    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 存储参数配置
    if storage_set:
        storage_param_set(storage_type=storage_set.get("存储类型"), dir_name=storage_set.get("目录"),
                          ftp=storage_set.get("远程服务器"), use_var=storage_set.get("变量引用"))

    # 启用过滤配置
    js = 'return $("#enableFilterCfg")[0].checked;'
    status = browser.execute_script(js)
    log.info("【启用过滤配置】勾选状态: {0}".format(status))

    # 聚焦元素
    enable_filter_element = browser.find_element(By.XPATH, "//*[@id='enableFilterCfg']")
    browser.execute_script("arguments[0].scrollIntoView(true);", enable_filter_element)
    if enable_filter_set == "开启":
        if not status:
            enable_filter_element.click()
            log.info("开启【启用过滤配置】")
        else:
            log.info("【启用过滤配置】已开启")
    else:
        if status:
            enable_filter_element.click()
            log.info("关闭【启用过滤配置】")
        else:
            log.info("【启用过滤配置】未开启")

    # 过滤配置
    if filter_set:
        rows = len(filter_set)
        log.info("需要添加{0}条配置".format(rows))
        num = 1
        flag = True
        while flag:

            # 先获取文件过滤类型
            js = "return $(\"input[name='file_choose_type{0}']\").val();".format(num)
            choose_type = browser.execute_script(js)
            log.info("类型: {0}".format(choose_type))
            if choose_type == "0":
                choose_type = "关键字"
            elif choose_type == "1":
                choose_type = "正则匹配"
            else:
                # 本行找不到类型下拉框的值，表示这一行不存在，那么上一行就是当前最后一行
                log.info("当前开始从第{0}行开始配置文件".format(num))

                if num > 1:
                    browser.find_element(
                        By.XPATH, "//*[@id='fileType{0}']/../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                            num - 1)).click()
                break
            log.info("类型转义: {0}".format(choose_type))

            # 根据类型获取文件名输入框的内容是否为空
            if choose_type == "关键字":
                file_name_element = browser.find_element(By.XPATH, "//*[@name='filepath{0}']".format(num))
            else:
                file_name_element = browser.find_element(By.XPATH, "//*[@name='keyExpr{0}']".format(num))
            var_name = file_name_element.get_attribute("value")
            log.info(var_name)
            if var_name:
                # 如果value不为空，表示本条已配置
                num += 1
            else:
                log.info("当前开始从第{0}行开始配置文件".format(num))

                if num > 1:
                    browser.find_element(
                        By.XPATH, "//*[@id='fileType{0}']/../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                            num - 1)).click()
                flag = False

        for file_msg in filter_set:
            file_filter(choose_type=file_msg.get("类型"), file_name=file_msg.get("文件名"),
                        file_type=file_msg.get("文件类型"), row_num=num)
            # 如果当前未添加完成，继续配置下一行
            if num < len(filter_set):
                browser.find_element(
                    By.XPATH, "//*[@id='fileType{0}']/../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                        num)).click()
            num += 1
            sleep(1)

    # 设置高级模式
    if advance_set:
        if advance_set.get("状态") == "开启":
            timeout = advance_set.get("超时时间")
            retry_times = advance_set.get("超时重试次数")
            try:
                enable_click = browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='开启高级模式']")
                enable_click.click()
                log.info("开启【高级配置】")
            except NoSuchElementException:
                pass

            browser.find_element(By.XPATH, "//*[@name='aiTimeout']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='aiTimeout']/preceding-sibling::input").send_keys(timeout)
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='tryTime']/preceding-sibling::input").send_keys(retry_times)
            log.info("设置高级模式")
            sleep(1)
        else:
            try:
                browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='开启高级模式']")
            except NoSuchElementException:
                disable_click = browser.find_element(By.XPATH, "//*[@onclick='toggleAdv($(this))']//*[text()='关闭高级模式']")
                disable_click.click()
                log.info("关闭【高级配置】")

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@onclick='saveOcrNodeInfo(false)']//*[text()='保存']").click()
    log.info("保存业务配置")

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("操作成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    gbl.temp.set("ResultMsg", msg)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name


def storage_param_set(storage_type, dir_name, ftp, use_var):
    """
    :param storage_type: 存储类型
    :param dir_name: 目录
    :param ftp: 远程服务器
    :param use_var: 变量引用，是/否
    """
    browser = gbl.service.get("browser")
    # 存储类型
    if storage_type == "本地":
        log.info("配置本地文件")
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@onclick=\"getStorageType(this,'0')\"]")))
        browser.find_element(By.XPATH, "//*[@onclick=\"getStorageType(this,'0')\"]").click()

        # 变量引用
        js = 'return $("#local_isKeyword")[0].checked;'
        status = browser.execute_script(js)
        log.info("【变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = browser.find_element(By.XPATH, "//*[@id='local_isKeyword']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if use_var == "是":
            # 点击目标变量引用
            if not status:
                enable_click.click()
            log.info("勾选【变量引用】")

            # 目标目录
            if dir_name:
                browser.find_element(By.XPATH, "//*[@name='local_keyword']/preceding-sibling::input").clear()
                browser.find_element(By.XPATH, "//*[@name='local_keyword']/preceding-sibling::input").send_keys(dir_name)
                log.info("设置目录: {0}".format(dir_name))
        else:
            if status:
                enable_click.click()
                log.info("取消勾选【变量引用】")

            # 目录
            browser.find_element(By.XPATH, "//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)
        sleep(1)

    elif storage_type == "远程":
        log.info("配置远程ftp文件")
        browser.find_element(By.XPATH, "//*[@name='storageType' and @onclick=\"getStorageType(this,'1')\"]").click()

        # 选择ftp
        if ftp:
            browser.find_element(By.XPATH, "//*[@name='srcServerId']/preceding-sibling::input[1]").click()
            server_element = browser.find_element(
                By.XPATH, "//*[contains(@id,'remote_srcServerId') and text()='{0}']".format(ftp))
            browser.execute_script("arguments[0].scrollIntoView(true);", server_element)
            server_element.click()
            sleep(1)
            log.info("选择ftp: {0}".format(ftp))

        # ftp目录
        if dir_name:
            browser.find_element(By.XPATH, "//*[@name='srcPath_2']/preceding-sibling::input[1]").click()
            choose_ftp_dir(path=dir_name)
            log.info("远程ftp目录选择完成")


def file_filter(choose_type, file_name, file_type, row_num):
    """
    :param choose_type: 类型
    :param file_name: 文件名
    :param file_type: 文件类型
    :param row_num: 行号
    """
    browser = gbl.service.get("browser")
    num = row_num
    focus_element = browser.find_element(
        By.XPATH, "//*[@id='loadfilepath{0}']//*[contains(text(),'文件') and @class='requireTag']".format(num))
    browser.execute_script("arguments[0].scrollIntoView(true);", focus_element)

    # 设置类型
    if choose_type:
        browser.find_element(By.XPATH, "//*[@name='file_choose_type{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'file_choose_type{0}') and text()='{1}']".format(num, choose_type)).click()
        sleep(1)

    # 当前设置类型
    js = "return $(\"input[name='file_choose_type{0}']\").val();".format(num)
    choose_type = browser.execute_script(js)
    if choose_type == "0":
        choose_type = "关键字"
    elif choose_type == "1":
        choose_type = "正则匹配"
    else:
        raise Exception("获取类型失败")
    log.info("选择类型: {0}".format(choose_type))

    if choose_type == "关键字":
        # 输入文件名
        if file_name:
            input_xpath = "//*[@name='filepath{0}']/preceding-sibling::input".format(num)
            set_text_enable_var(input_xpath=input_xpath, msg=file_name)
            log.info("设置文件名: {0}".format(file_name))
            sleep(1)
    else:
        # 输入文件名
        if file_name:
            browser.find_element(By.XPATH, "//*[@name='keyExpr{0}']/preceding-sibling::span/a".format(num)).click()
            sleep(1)
            # 切换到正则配置iframe页面
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=file_name.get("设置方式"), regular_name=file_name.get("正则模版名称"),
                                    advance_mode=file_name.get("高级模式"), regular=file_name.get("标签配置"),
                                    expression=file_name.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                gbl.temp.set("ResultMsg", msg)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()

            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
    sleep(1)

    # 选择文件类型，默认全部
    if file_type:
        browser.find_element(By.XPATH, "//*[@name='fileType{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileType{0}') and text()='{1}']".format(num, file_type)).click()
        log.info("选择文件类型: {0}".format(file_type))
        sleep(1)

    log.info("第{0}行文件配置完成, 文件名: {1}".format(num, file_name))
