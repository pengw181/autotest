# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午10:22

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.alertBox import BeAlertBox
from src.main.python.lib.processVar import choose_var
from src.main.python.lib.chooseDir import choose_ftp_dir, choose_file_dir
from src.main.python.lib.regular import RegularCube
from src.main.python.lib.input import set_text_enable_var
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def file_business(node_name, operate_mode, storage_set, source_set, dest_set, files_set):
    """
    :param node_name: 节点名称
    :param operate_mode: 操作模式
    :param storage_set: 存储参数配置，字典
    :param source_set: 源，字典
    :param dest_set: 目标，字典
    :param files_set: 文件配置，字典

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "文件节点",
            "节点名称": "文件节点",
            "业务配置": {
                "节点名称": "文件节点1",
                "操作模式": "文件存储",
                "存储参数配置": {
                    "存储类型": "本地",
                    "目录": "AI",
                    "变量引用": "否"
                },
                "文件配置": [
                    {
                        "变量": "地点",
                        "文件名": "pw自动化测试文件名1",
                        "文件类型": "xlsx",
                        "编码格式": "UTF-8",
                        "时间前后缀": "时间前缀",
                        "时间格式": "yyyyMMdd"
                    },
                    {
                        "变量": "地点",
                        "文件名": "pw自动化测试文件名2",
                        "文件类型": "txt",
                        "编码格式": "GBK",
                        "时间前后缀": "无",
                        "时间格式": "yyyyMMdd"
                    }
                ]
            }
        }
    }
    """
    browser = gbl.service.get("browser")
    sleep(2)
    log.info("开始配置文件节点业务配置")
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称")
        sleep(1)

    # 设置操作模式
    if operate_mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input[1]").click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(operate_mode)).click()
        log.info("选择操作模式: {0}".format(operate_mode))
        sleep(1)

    # 获取操作模式当前选择值
    js = "return $(\"input[name='node_model_id']\").val();"
    operate_mode = browser.execute_script(js)
    log.info("操作模式: {0}".format(operate_mode))
    if operate_mode == "1501":
        operate_mode = "文件存储"
    elif operate_mode == "1502":
        operate_mode = "文件拷贝或移动"
    elif operate_mode == "1503":
        operate_mode = "文件加载"
    else:
        raise Exception("获取操作模式失败")
    log.info("操作模式转义: {0}".format(operate_mode))
    # 切换到文件配iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='file_model_content']"))
    # 等待页面加载
    wait = WebDriverWait(browser, 30)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'存储类型')]")))

    # 文件配置
    if operate_mode == "文件存储":
        # 文件存储
        file_storage_mode(storage_set=storage_set, files_set=files_set)

    elif operate_mode == "文件拷贝或移动":
        # 文件拷贝或移动
        file_cp_mode(src_set=source_set, dest_set=dest_set, files_set=files_set)

    else:
        # 文件加载
        file_load_mode(storage_set=storage_set, files_set=files_set)

    # 切换到业务配置iframe
    browser.switch_to.parent_frame()

    # 获取节点名称
    node_name = browser.find_element(
        By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='save_irContent']/span/span[1]").click()
    log.info("保存业务配置")

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    gbl.temp.set("ResultMsg", msg)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name


def file_storage_mode(storage_set, files_set):
    """
    :param storage_set: 存储参数配置，字典，必填
    :param files_set: 文件配置，数组，必填

    # 存储参数配置
    {
        "存储类型": "本地",
        "目录": "AI",
        "变量引用": "否"
    }

    # 文件配置
    [
        {
            "变量": "地点",
            "文件名": "pw自动化测试文件名1",
            "文件类型": "xlsx",
            "编码格式": "UTF-8",
            "sheet名称": "sheeta",
            "时间前后缀": "时间前缀",
            "时间格式": "yyyyMMdd"
        },
        {
            "变量": "地点",
            "文件名": "pw自动化测试文件名2",
            "文件类型": "txt",
            "编码格式": "GBK",
            "分隔符": ",",
            "时间前后缀": "无",
            "时间格式": "yyyyMMdd"
        }
    ]
    """
    browser = gbl.service.get("browser")
    # 存储类型
    if storage_set:
        file_storage_mode_dir_set(storage_type=storage_set.get("存储类型"), use_var=storage_set.get("变量引用"),
                                  ftp=storage_set.get("远程服务器"), dir_name=storage_set.get("目录"))

    # 文件配置
    rows = len(files_set)
    log.info("需要添加{0}条配置".format(rows))
    # 通过试探变量是否选择完成，来判断新配置从第几行开始添加
    num = 1
    flag = True
    while flag:
        try:
            var = browser.find_element(
                By.XPATH, "//*[@id='dataH_inputVar{0}Name']/following-sibling::span/*[@class='textbox-value']".format(num))
            var_name = var.get_attribute("value")
            if var_name:
                # 如果value不为空，表示有选择变量
                num += 1
            else:
                log.info("当前开始从第{0}行开始配置文件".format(num))

                if num > 1:
                    browser.find_element(
                        By.XPATH, "//*[@name='timeFormat{0}']/../../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                            num - 1)).click()
                flag = False
        except NoSuchElementException:
            log.info("当前开始从第{0}行开始配置文件".format(num))

            if num > 1:
                browser.find_element(
                    By.XPATH, "//*[@name='timeFormat{0}']/../../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                        num - 1)).click()
            flag = False

    for file_msg in files_set:
        if file_msg.get("时间前缀") == "是":
            add_prefix = True
        else:
            add_prefix = False

        if file_msg.get("时间后缀") == "是":
            add_suffix = True
        else:
            add_suffix = False

        file_storage_mode_file_set(input_var=file_msg.get("变量"), file_name=file_msg.get("文件名"),
                                   file_type=file_msg.get("文件类型"), encoding=file_msg.get("编码格式"),
                                   seperator=file_msg.get("分隔符"), sheet_name=file_msg.get("sheet名称"),
                                   add_prefix=add_prefix, add_suffix=add_suffix, time_format=file_msg.get("时间格式"),
                                   row_num=num)
        log.info("第{0}行文件配置完成".format(num))
        # 如果当前未添加完成，继续配置下一行
        if num < len(files_set):
            browser.find_element(
                By.XPATH, "//*[@name='timeFormat{0}']/../../following-sibling::div/a[@onclick='addFilePath(this)']".format(
                    num)).click()
        # 行计数器累加
        num += 1
        sleep(1)


def file_storage_mode_dir_set(storage_type, use_var, ftp, dir_name):
    """
    :param storage_type:  存储类型
    :param use_var: 变量引用
    :param ftp: 远程服务器
    :param dir_name: 目录
    """
    browser = gbl.service.get("browser")
    log.info("文件存储模式配置文件目录")
    if storage_type == "本地":
        log.info("配置本地文件")
        browser.find_element(By.XPATH, "//*[@onclick=\"getStorageType(this,'0')\"]").click()

        # 变量引用
        js = 'return $("#local_isKeyword")[0].checked;'
        status = browser.execute_script(js)
        log.info("【变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = browser.find_element(By.XPATH, "//*[@id='local_isKeyword']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)
        if use_var == "是":
            # 点击源变量引用
            if not status:
                enable_click.click()
            log.info("勾选【变量引用】")

            # 目录
            if dir_name:
                browser.find_element(By.XPATH, "//*[@name='local_keyword']/preceding-sibling::input").clear()
                input_xpath = "//*[@name='local_keyword']/preceding-sibling::input"
                set_text_enable_var(input_xpath=input_xpath, msg=dir_name)
                log.info("输入目录: {0}".format(dir_name))
                sleep(1)
        else:
            if status:
                enable_click.click()
                log.info("取消勾选【变量引用】")

            # 目录
            browser.find_element(By.XPATH, "//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)
        sleep(1)

    elif storage_type == "远程":
        log.info("配置远程ftp目录文件")
        browser.find_element(By.XPATH, "//*[@onclick=\"getStorageType(this,'1')\"]").click()
        # 选择ftp
        browser.find_element(By.XPATH, "//*[@name='srcServerId']/preceding-sibling::input[1]").click()
        server_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'remote_srcServerId') and text()='{0}']".format(ftp))
        browser.execute_script("arguments[0].scrollIntoView(true);", server_element)
        server_element.click()
        log.info("选择ftp: {0}".format(ftp))
        # 点击目录
        browser.find_element(By.XPATH, "//*[@name='srcPath_2']/preceding-sibling::input[1]").click()
        choose_ftp_dir(path=dir_name)
        log.info("ftp目录选择完成")


def file_storage_mode_file_set(input_var, file_name, file_type, encoding, seperator, sheet_name, add_prefix,
                               add_suffix, time_format, row_num):
    """
    # 可循环调用该函数
    :param input_var: 变量，必填
    :param file_name: 文件名，必填
    :param file_type: 文件类型，非必填
    :param encoding: 编码格式，非必填
    :param seperator: 分隔符，file_type选txt或csv时出现，非必填
    :param sheet_name: sheet名称，file_type选xls或xlsx时出现，非必填
    :param add_prefix: 时间前缀，bool，非必填
    :param add_suffix: 时间后缀，bool，非必填
    :param time_format: 时间格式，非必填
    :param row_num: 行号

    {
        "变量": "地点",
        "文件名": "pw自动化测试文件名1",
        "文件类型": "xlsx",
        "编码格式": "UTF-8",
        "sheet名称": "sheeta",
        "时间前缀": "是",
        "时间后缀": "是",
        "时间格式": "yyyyMMdd"
    },
    {
        "变量": "地点",
        "文件名": "pw自动化测试文件名2",
        "文件类型": "txt",
        "编码格式": "GBK",
        "分隔符": ",",
        "时间前缀": "无",
        "时间后缀": "是",
        "时间格式": "yyyyMMdd"
    }
    """
    browser = gbl.service.get("browser")
    num = row_num
    # 聚焦元素
    row_element = browser.find_element(
        By.XPATH, "//*[@id='filePathTab']/div[{0}]//*[contains(@data-options,'chooseFileVar(e)')]/following-sibling::span/span/a".format(
                num))
    browser.execute_script("arguments[0].scrollIntoView(true);", row_element)

    # 点击选择变量
    if input_var:
        browser.find_element(
            By.XPATH, "//*[@id='filePathTab']/div[{0}]//*[contains(@data-options,'chooseFileVar(e)')]/following-sibling::span/span/a".format(
                num)).click()
        # 进入变量检索页面选择变量
        choose_var(var_name=input_var)
        log.info("选择变量: {0}".format(input_var))
        sleep(1)

    # 输入文件名
    if file_name:
        input_xpath = "//*[@name='filepath{0}']/preceding-sibling::input".format(num)
        set_text_enable_var(input_xpath=input_xpath, msg=file_name)
        log.info("输入文件名: {0}".format(file_name))
        sleep(1)

    # 选择文件类型。txt/csv可以设置分隔符，xls/xlsx可以设置sheet
    if file_type:
        browser.find_element(By.XPATH, "//*[@name='fileType{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileType{0}') and text()='{1}']".format(num, file_type)).click()
        log.info("选择文件类型: {0}".format(file_type))
        sleep(1)

    # 设置编码格式
    if encoding:
        browser.find_element(By.XPATH, "//*[@name='fileCode{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileCode{0}') and text()='{1}']".format(num, encoding)).click()
        log.info("选择编码格式: {0}".format(encoding))
        sleep(1)

    # 设置分隔符
    if seperator:
        browser.find_element(By.XPATH, "//*[@name='seperator{0}']/preceding-sibling::input".format(num)).send_keys(seperator)
        log.info("设置分隔符: {0}".format(seperator))
        sleep(1)

    # 设置sheet名
    if sheet_name:
        browser.find_element(By.XPATH, "//*[@name='sheetName{0}']/preceding-sibling::input".format(num)).send_keys(sheet_name)
        log.info("设置sheet名: {0}".format(sheet_name))
        sleep(1)

    # 设置时间前缀
    js = 'return $("#prefixTime{0}")[0].checked;'.format(num)
    status = browser.execute_script(js)
    log.info("第{0}行【时间前缀】勾选状态: {0}".format(status))
    # 聚焦元素
    add_prefix_click = browser.find_element(By.XPATH, "//*[@id='prefixTime{0}']".format(num))
    browser.execute_script("arguments[0].scrollIntoView(true);", add_prefix_click)
    if add_prefix:
        if not status:
            add_prefix_click.click()
            sleep(1)
        log.info("第{0}行勾选【时间前缀】".format(num))
    else:
        if status:
            add_prefix_click.click()
        log.info("第{0}行取消勾选【时间前缀】".format(num))

    # 设置时间后缀
    js = 'return $("#suffixTime{0}")[0].checked;'.format(num)
    status = browser.execute_script(js)
    log.info("第{0}行【时间后缀】勾选状态: {0}".format(status))
    # 聚焦元素
    add_suffix_click = browser.find_element(By.XPATH, "//*[@id='suffixTime{0}']".format(num))
    browser.execute_script("arguments[0].scrollIntoView(true);", add_suffix_click)
    if add_suffix:
        if not status:
            add_suffix_click.click()
            sleep(1)
        log.info("第{0}行勾选【时间后缀】".format(num))
    else:
        if status:
            add_suffix_click.click()
        log.info("第{0}行取消勾选【时间后缀】".format(num))

    # 设置时间格式
    if time_format:
        browser.find_element(By.XPATH, "//*[@name='timeFormat{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'timeFormat{0}') and text()='{1}']".format(num, time_format)).click()
        log.info("设置时间格式: {0}".format(time_format))
        sleep(1)


def file_cp_mode(src_set, dest_set, files_set):
    """
    :param src_set: 源，字典
    :param dest_set: 目标，字典
    :param files_set: 文件配置，数组，必填

    # 源
    {
        "存储类型": "本地",
        "目录": "AI",
        "变量引用": "否"
    }

    # 目标
    {
        "存储类型": "远程",
        "远程服务器": "pw-ftp测试",
        "目录": "根目录-pw-1",
        "变量引用": "否"
    }

    # 文件配置
    [
        {
            "类型": "关键字",
            "文件名": "时间",
            "目标文件": "目标文件1.xlsx",
            "模式": "拷贝"
        },
        {
            "类型": "关键字",
            "文件名": "时间",
            "目标文件": "目标文件2.xlsx",
            "模式": "移动"
        }
    ]
    """
    browser = gbl.service.get("browser")
    # ----源存储类型----
    if src_set:
        if src_set.get("变量引用") == "是":
            source_use_var = True
        else:
            source_use_var = False
        file_cp_mode_src_set(storage_type=src_set.get("存储类型"), use_var=source_use_var,
                             ftp=src_set.get("远程服务器"), dir_name=src_set.get("目录"))

    # ----目标储类型----
    if dest_set:
        if dest_set.get("变量引用") == "是":
            dest_use_var = True
        else:
            dest_use_var = False
        file_cp_mode_dest_set(storage_type=dest_set.get("存储类型"), use_var=dest_use_var,
                              ftp=dest_set.get("远程服务器"), dir_name=dest_set.get("目录"))

    # 文件配置
    rows = len(files_set)
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
            # 本行类型下拉框的值为空，表示这一行不存在，那么上一行就是当前最后一行
            log.info("当前开始从第{0}行开始配置文件".format(num))

            if num > 1:
                browser.find_element(
                    By.XPATH, "//*[@id='oprt_flag{0}']/../following-sibling::div/a[@onclick='addCopyFilePath(this)']".format(
                        num - 1)).click()
            break
        log.info("类型转义: {0}".format(choose_type))

        # 根据类型获取文件名输入框的内容是否为空
        if choose_type == "关键字":
            file_name_element = browser.find_element(By.XPATH, "//*[@name='src_filepath{0}']".format(num))
        else:
            file_name_element = browser.find_element(By.XPATH, "//*[@name='keyExprf{0}']".format(num))
        var_name = file_name_element.get_attribute("value")
        log.info(var_name)
        if var_name:
            # 如果value不为空，表示本条已配置
            num += 1
        else:
            # 第一条配置
            log.info("当前开始从第{0}行开始配置文件".format(num))

            if num > 1:
                browser.find_element(
                    By.XPATH, "//*[@id='oprt_flag{0}']/../following-sibling::div/a[@onclick='addCopyFilePath(this)']".format(
                        num - 1)).click()
            flag = False

    for file_msg in files_set:
        file_cp_mode_file_set(choose_type=file_msg.get("类型"), file_name=file_msg.get("文件名"),
                              dest_file_name=file_msg.get("目标文件"), mode=file_msg.get("模式"), row_num=num)
        log.info("第{0}行文件配置完成".format(num))
        # 如果当前未添加完成，继续配置下一行
        if num < len(files_set):
            browser.find_element(
                By.XPATH, "//*[@id='oprt_flag{0}']/../following-sibling::div/a[@onclick='addCopyFilePath(this)']".format(
                    num)).click()
        num += 1
        sleep(1)


def file_cp_mode_src_set(storage_type, use_var, ftp, dir_name):
    """
    :param storage_type: 存储类型
    :param use_var: 变量引用
    :param ftp: 远程服务器
    :param dir_name: 目录
    """
    browser = gbl.service.get("browser")
    # 存储类型
    if storage_type == "本地":
        log.info("配置本地文件")
        browser.find_element(By.XPATH, "//*[@name='storageType_1' and @onclick=\"getStorageType(this,'0')\"]").click()

        # 变量引用
        js = 'return $("#local_isKeyword_1")[0].checked;'
        status = browser.execute_script(js)
        log.info("源【变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = browser.find_element(By.XPATH, "//*[@id='local_isKeyword_1']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if use_var:
            # 点击源变量引用
            if not status:
                enable_click.click()
            log.info("勾选源【变量引用】")
            # 源目录
            if dir_name:
                browser.find_element(
                    By.XPATH, "//*[@id='local_keyword_span_1']//*[@name='local_keyword']/preceding-sibling::input").clear()
                browser.find_element(
                    By.XPATH, "//*[@id='local_keyword_span_1']//*[@name='local_keyword']/preceding-sibling::input").send_keys(
                    dir_name)
                log.info("设置目录: {0}".format(dir_name))
        else:
            if status:
                enable_click.click()
                log.info("取消勾选源【变量引用】")
            # 源目录
            browser.find_element(
                By.XPATH, "//*[@id='local_srcPath_1']/following-sibling::span//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)
        sleep(1)

    elif storage_type == "远程":
        log.info("配置远程ftp文件")
        browser.find_element(By.XPATH, "//*[@name='storageType_1' and @onclick=\"getStorageType(this,'1')\"]").click()

        # 选择ftp
        browser.find_element(
            By.XPATH, "//*[@id='remote_srcServerId_1']/following-sibling::span//*[@name='srcServerId']/preceding-sibling::input[1]").click()
        server_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'remote_srcServerId_1') and text()='{0}']".format(ftp))
        browser.execute_script("arguments[0].scrollIntoView(true);", server_element)
        server_element.click()
        log.info("选择ftp: {0}".format(ftp))

        # 源ftp目录
        browser.find_element(
            By.XPATH, "//*[@id='remote_choose_span_1']//*[@name='srcPath_2']/preceding-sibling::input[1]").click()
        choose_ftp_dir(path=dir_name)
        log.info("远程ftp目录选择完成")


def file_cp_mode_dest_set(storage_type, use_var, ftp, dir_name):
    """
    :param storage_type: 存储类型
    :param use_var: 变量引用
    :param ftp: 远程服务器
    :param dir_name: 目录
    """
    browser = gbl.service.get("browser")
    # 存储类型
    if storage_type == "本地":
        log.info("配置本地文件")
        browser.find_element(By.XPATH, "//*[@name='storageType_2' and @onclick=\"getStorageType(this,'0')\"]").click()

        # 变量引用
        js = 'return $("#local_isKeyword_2")[0].checked;'
        status = browser.execute_script(js)
        log.info("目标【变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_click = browser.find_element(By.XPATH, "//*[@id='local_isKeyword_2']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_click)

        if use_var:
            # 点击目标变量引用
            if not status:
                enable_click.click()
            log.info("勾选目标【变量引用】")

            # 目标目录
            if dir_name:
                browser.find_element(
                    By.XPATH, "//*[@id='local_keyword_span_2']//*[@name='local_keyword']/preceding-sibling::input").clear()
                browser.find_element(
                    By.XPATH, "//*[@id='local_keyword_span_2']//*[@name='local_keyword']/preceding-sibling::input").send_keys(
                    dir_name)
                log.info("设置目录: {0}".format(dir_name))
        else:
            if status:
                enable_click.click()
                log.info("取消勾选目标【变量引用】")

            # 源目录
            browser.find_element(
                By.XPATH, "//*[@id='local_srcPath_2']/following-sibling::span//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)
        sleep(1)

    elif storage_type == "远程":
        log.info("配置远程ftp文件")
        browser.find_element(By.XPATH, "//*[@name='storageType_2' and @onclick=\"getStorageType(this,'1')\"]").click()

        # 选择ftp
        browser.find_element(
            By.XPATH, "//*[@id='remote_srcServerId_2']/following-sibling::span//*[@name='srcServerId']/preceding-sibling::input[1]").click()
        server_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'remote_srcServerId_2') and text()='{0}']".format(ftp))
        browser.execute_script("arguments[0].scrollIntoView(true);", server_element)
        server_element.click()
        log.info("选择ftp: {0}".format(ftp))

        # 目标ftp目录
        browser.find_element(
            By.XPATH, "//*[@id='remote_choose_span_2']//*[@name='srcPath_2']/preceding-sibling::input[1]").click()
        choose_ftp_dir(path=dir_name)
        log.info("远程ftp目录选择完成")


def file_cp_mode_file_set(choose_type, file_name, dest_file_name, mode, row_num):
    """
    # 可循环调用该函数
    :param choose_type: 类型，关键字/正则匹配，非必填
    :param file_name: 文件名，choose_type为关键字时，传字符串，否则传字典
    :param dest_file_name: 目标文件，可为空
    :param mode: 模式，拷贝/移动，非必填
    :param row_num: 行号

    {
        "类型": "关键字",
        "文件名": "时间",
        "目标文件": "目标文件1.xlsx",
        "模式": "拷贝"
    }

    {
        "类型": "关键字",
        "文件名": "时间",
        "目标文件": "目标文件2.xlsx",
        "模式": "移动"
    }
    """
    browser = gbl.service.get("browser")
    num = row_num
    # 聚焦元素
    row_element = browser.find_element(By.XPATH, "//*[@name='file_choose_type{0}']/preceding-sibling::input".format(num))
    browser.execute_script("arguments[0].scrollIntoView(true);", row_element)

    # 点击选择类型
    if choose_type:
        browser.find_element(
            By.XPATH, "//*[@name='file_choose_type{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'file_choose_type{0}') and text()='{1}']".format(num, choose_type)).click()
        sleep(1)

    # 输入文件名
    js = "return $(\"input[name='file_choose_type{0}']\").val();".format(num)
    choose_type = browser.execute_script(js)
    if choose_type == "0":
        choose_type = "关键字"
    elif choose_type == "1":
        choose_type = "正则匹配"
    else:
        raise Exception("获取类型失败")
    log.info("类型: {0}".format(choose_type))
    if choose_type == "关键字":
        input_xpath = "//*[@id='src_filepath{0}']/following-sibling::span/input[1]".format(num)
        set_text_enable_var(input_xpath=input_xpath, msg=file_name)
        sleep(1)
    else:
        browser.find_element(By.XPATH, "//*[@name='keyExprf{0}']/preceding-sibling::span/a".format(num)).click()
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
                # 切换到文件配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='file_model_content']"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            browser.switch_to.parent_frame()

        # 关闭正则魔方配置
        browser.find_element(By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
    sleep(1)

    # 设置目标文件
    if dest_file_name:
        browser.find_element(By.XPATH, "//*[@id='dest_filepath{0}']/following-sibling::span/input[1]".format(num)).clear()
        browser.find_element(
            By.XPATH, "//*[@id='dest_filepath{0}']/following-sibling::span/input[1]".format(num)).send_keys(dest_file_name)
        sleep(1)

    # 设置模式，拷贝或移动
    if mode:
        browser.find_element(By.XPATH, "//*[@id='oprt_flag{0}']/following-sibling::span/input[1]".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'oprt_flag{0}_') and text()='{1}']".format(num, mode)).click()
        sleep(1)


def file_load_mode(storage_set, files_set):
    """
    :param storage_set: 存储参数配置，字典，必填
    :param files_set: 文件配置，字典，必填

    # 存储参数配置
    {
        "存储类型": "本地",
        "目录": "AI",
        "变量引用": "否"
    }

    # 文件配置
    [
        {
            "类型": "关键字",
            "文件名": "pw自动化测试文件名1",
            "文件类型": "xlsx",
            "编码格式": "UTF-8",
            "开始读取行": "1",
            "sheet页索引": "1",
            "变量": "加载pw自动化测试文件名1",
            "变量类型": "替换",
            "开启过滤": {
                "状态": "开启",
                "设置方式": "选择",
                "正则模版名称": "pw按时间拆分",
                "正则模版配置": []
                }
            }
        },

    ]

    """
    browser = gbl.service.get("browser")
    log.info("开始文件加载模式配置")
    # 存储参数配置
    if storage_set:
        file_load_mode_dir_set(storage_type=storage_set.get("存储类型"), dir_name=storage_set.get("目录"),
                               use_var=storage_set.get("变量引用"), ftp=storage_set.get("远程服务器"))

    # 文件配置
    if files_set:
        rows = len(files_set)
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
                        By.XPATH, "//*[@id='isFilter{0}']/../../following-sibling::div/a[@onclick='addLoadFilePath(this)']".format(
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
                        By.XPATH, "//*[@id='isFilter{0}']/../../following-sibling::div/a[@onclick='addLoadFilePath(this)']".format(
                            num - 1)).click()
                flag = False

        for file_msg in files_set:
            file_load_mode_file_set(choose_type=file_msg.get("类型"), file_name=file_msg.get("文件名"),
                                    file_type=file_msg.get("文件类型"), encoding=file_msg.get("编码格式"),
                                    begin_line=file_msg.get("开始读取行"), seperator=file_msg.get("分隔符"),
                                    sheet_index=file_msg.get("sheet页索引"), var_name=file_msg.get("变量"),
                                    value_type=file_msg.get("赋值方式"), filter_set=file_msg.get("开启过滤"),
                                    row_num=num)
            log.info("第{0}行文件配置完成".format(num))
            # 如果当前未添加完成，继续配置下一行
            if num < len(files_set):
                browser.find_element(
                    By.XPATH, "//*[@id='isFilter{0}']/../../following-sibling::div/a[@onclick='addLoadFilePath(this)']".format(
                        num)).click()
            num += 1
            sleep(1)


def file_load_mode_dir_set(storage_type, dir_name, use_var, ftp):
    """
    :param storage_type: 存储类型，本地/远程，非必填
    :param dir_name: 目录，必填
    :param use_var: 变量引用，非必填
    :param ftp: 远程服务器，storage_type选择远程时，必填

    """
    browser = gbl.service.get("browser")
    # 存储类型
    if storage_type == "本地":
        log.info("配置本地文件")
        browser.find_element(By.XPATH, "//*[@onclick=\"getStorageType(this,'0')\"]").click()
        if use_var == "是":
            # 勾选变量引用
            browser.find_element(By.XPATH, "//*[@id='local_isKeyword']").click()
            # 手动输入目录
            browser.find_element(By.XPATH, "//*[@name='local_keyword']/preceding-sibling::input").clear()
            browser.find_element(By.XPATH, "//*[@name='local_keyword']/preceding-sibling::input").send_keys()
            log.info("开启变量引用")
        else:
            # 目录树选择目录
            browser.find_element(By.XPATH, "//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)

    elif storage_type == "远程":
        log.info("配置远程ftp文件")
        browser.find_element(By.XPATH, "//*[@onclick=\"getStorageType(this,'1')\"]").click()
        # 选择ftp
        browser.find_element(By.XPATH, "//*[@name='srcServerId']/preceding-sibling::input[1]").click()
        server_element = browser.find_element(
            By.XPATH, "//*[contains(@id,'remote_srcServerId') and text()='{0}']".format(ftp))
        browser.execute_script("arguments[0].scrollIntoView(true);", server_element)
        server_element.click()
        log.info("选择ftp: {0}".format(ftp))
        # 点击目录
        browser.find_element(By.XPATH, "//*[@name='srcPath_2']/preceding-sibling::input[1]").click()
        choose_ftp_dir(path=dir_name)
        log.info("远程ftp目录选择完成")


def file_load_mode_file_set(choose_type, file_name, file_type, encoding, begin_line, seperator, sheet_index,
                            var_name, value_type, filter_set, row_num):
    """
    # 循环调用该函数
    :param choose_type: 类型，关键字/正则，非必填
    :param file_name: 文件名，choose_type为关键字时，传字符串，choose_type为正则时，传字典
    :param file_type: 文件类型，非必填
    :param encoding: 编码格式，非必填
    :param begin_line: 开始读取行，非必填
    :param seperator: 分隔符，非必填，file_type选择csv/txt时出现
    :param sheet_index: sheet页索引，非必填，file_type选择xlsx/xls时出现
    :param var_name: 变量
    :param value_type: 赋值方式， 替换/追加，非必填
    :param filter_set: 开启过滤，字典，非必填
    :param row_num: 第几行

    {
        "类型": "关键字",
        "文件名": "pw自动化测试文件名2",
        "文件类型": "csv",
        "编码格式": "GBK",
        "开始读取行": "1",
        "分隔符": "",
        "变量": "加载pw自动化测试文件名2",
        "开启过滤": {
            "状态": "开启",
            "设置方式": "添加",
            "正则模版名称": "pw自动化正则模版",
            "正则模版配置": [
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
            }
        }
    }
    """
    browser = gbl.service.get("browser")
    num = row_num
    # 文件配置
    focus_element = browser.find_element(
        By.XPATH, "//*[@id='loadfilepath{0}']//*[contains(text(),'文件') and @class='requireTag']".format(num))
    browser.execute_script("arguments[0].scrollIntoView(true);", focus_element)

    # 设置类型
    if choose_type:
        browser.find_element(By.XPATH, "//*[@name='file_choose_type{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(
            By.XPATH, "//*[contains(@id,'file_choose_type{0}') and text()='{1}']".format(num, choose_type)).click()
        log.info("类型选择: {0}".format(choose_type))
        sleep(1)

    # 输入文件名
    js = "return $(\"input[name='file_choose_type{0}']\").val();".format(num)
    choose_type = browser.execute_script(js)
    if choose_type == "0":
        choose_type = "关键字"
    elif choose_type == "1":
        choose_type = "正则匹配"
    else:
        raise Exception("获取类型失败")
    log.info("类型: {0}".format(choose_type))
    if choose_type == "关键字":
        input_xpath = "//*[@name='filepath{0}']/preceding-sibling::input".format(num)
        set_text_enable_var(input_xpath=input_xpath, msg=file_name)
        sleep(1)
    else:
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
                # 切换到文件配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='file_model_content']"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            gbl.temp.set("ResultMsg", msg)
        else:
            # 返回上层iframe
            browser.switch_to.parent_frame()

        # 关闭正则魔方配置
        browser.find_element(By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
    log.info("文件名配置完成，使用{0}".format(choose_type))
    sleep(1)

    # 选择文件类型。txt/csv可以设置分隔符，xls/xlsx可以设置sheet
    if file_type:
        browser.find_element(By.XPATH, "//*[@name='fileType{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileType{0}') and text()='{1}']".format(num, file_type)).click()
        log.info("选择文件类型: {0}".format(file_type))
        sleep(1)

    # 设置编码格式
    if encoding:
        browser.find_element(By.XPATH, "//*[@name='fileCode{0}']/preceding-sibling::input".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileCode{0}') and text()='{1}']".format(num, encoding)).click()
        log.info("选择编码格式: {0}".format(encoding))
        sleep(1)

    # 设置sheet页索引
    if sheet_index:
        browser.find_element(
            By.XPATH, "//*[@name='sheetName{0}']/preceding-sibling::input".format(num)).send_keys(sheet_index)
        log.info("设置sheet名: {0}".format(sheet_index))
        sleep(1)

    # 设置开始读取行
    if begin_line:
        browser.find_element(
            By.XPATH, "//*[@name='startRedLine{0}']/preceding-sibling::input".format(num)).send_keys(begin_line)
        log.info("设置开始读取行: {0}".format(begin_line))
        sleep(1)

    # 设置分隔符
    if seperator:
        browser.find_element(
            By.XPATH, "//*[@name='seperator{0}']/preceding-sibling::input".format(num)).send_keys(seperator)
        log.info("设置分隔符: {0}".format(seperator))
        sleep(1)

    # 设置变量
    browser.find_element(
        By.XPATH, "//*[@id='fileVarName{0}']/following-sibling::span[1]/input[1]".format(num)).send_keys(var_name)
    log.info("设置变量名: {0}".format(var_name))
    sleep(1)

    # 设置变量是替换还是追加
    if value_type:
        browser.find_element(By.XPATH, "//*[@id='valueType{0}']/following-sibling::span[1]/input[1]".format(num)).click()
        browser.find_element(By.XPATH, "//*[contains(@id,'valueType{0}') and text()='{1}']".format(num, value_type)).click()
        log.info("设置变量方式: {0}".format(value_type))
        sleep(1)

    # 是否开启过滤
    if filter_set:
        js = 'return $("#isFilter{0}")[0].checked;'.format(num)
        status = browser.execute_script(js)
        log.info("第{0}行【开启过滤】勾选状态: {1}".format(num, status))

        # 聚焦元素
        enable_filter_click = browser.find_element(By.XPATH, "//*[@id='isFilter{0}']".format(num))
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_filter_click)
        if filter_set.get("状态") == "开启":
            log.info("开启过滤")
            # 勾选开启过滤
            browser.find_element(By.XPATH, "//*[@id='isFilter{0}']".format(num)).click()
            sleep(1)
            confirm_selector = "//*[@id='isFilterIfr_{0}']".format(num)
            # 调用正则魔方配置正则
            regular_cube = RegularCube()
            regular_cube.setRegular(confirm_selector=confirm_selector, set_type=filter_set.get("设置方式"),
                                    regular_name=filter_set.get("正则模版名称"), advance_mode=filter_set.get("高级模式"),
                                    regular=filter_set.get("标签配置"), expression=filter_set.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, gbl.service.get("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='file_model_content']"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                gbl.temp.set("ResultMsg", msg)
            sleep(1)
        else:
            if status:
                enable_filter_click.click()
                log.info("第{0}行 取消勾选【开启过滤】".format(num))
            else:
                log.info("第{0}行【开启过滤】标识为否，不开启".format(num))
