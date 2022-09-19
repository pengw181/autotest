# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午10:37

from common.page.func.alertBox import BeAlertBox
from time import sleep
from common.page.func.processVar import choose_var
from common.page.func.input import set_blob
from common.page.func.chooseDir import choose_file_dir
from common.page.func.input import set_text_enable_var
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.log.logger import log
from common.variable.globalVariable import *


def info_business(node_name, mode, info_desc, show, info, download_set, var_name):
    """
    :param node_name: 节点名称
    :param mode: 操作模式
    :param info_desc: 信息描述
    :param show: 显示在运行信息的标题，是/否
    :param info: 信息明细， 数组
    :param download_set: 启用下载，字典
    :param var_name: 变量选择

    # 结果呈现/下载
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试信息处理节点流程",
            "节点类型": "信息处理节点",
            "节点名称": "信息处理节点",
            "业务配置": {
                "节点名称": "信息处理节点1",
                "操作模式": "结果呈现/下载",
                "信息描述": "运行结果",
                "显示在运行信息的标题": "是",
                "信息明细": [
                    {
                        "类型": "自定义值",
                        "自定义值": "地点"
                    },
                    {
                        "类型": "快捷键",
                        "快捷键": "换行"
                    },
                    {
                        "类型": "变量",
                        "变量分类": "流程定义变量",
                        "变量名": "地点"
                    },
                    {
                        "类型": "快捷键",
                        "快捷键": "换行"
                    },
                    {
                        "类型": "自定义值",
                        "自定义值": "流程实例id:"
                    },
                    {
                        "类型": "快捷键",
                        "快捷键": "换行"
                    },
                    {
                        "类型": "变量",
                        "变量分类": "系统内置变量",
                        "值": "流程实例ID"
                    }
                ],
                "启用下载": {
                    "状态": "开启",
                    "文件配置": [
                        {
                            "目录": "AI",
                            "文件名": "aaa.txt"
                        },
                        {
                            "目录": "OCR",
                            "文件名": "说明文档.docx"
                        },
                        {
                            "目录": "AI",
                            "文件名": "数据.xlsx"
                        },
                        {
                            "目录": "OCR",
                            "文件名": "日期.xls"
                        }
                    ]
                }
            }
        }
    }

    # 告警推送
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试信息处理节点流程",
            "节点类型": "信息处理节点",
            "节点名称": "信息处理节点",
            "业务配置": {
                "节点名称": "信息处理节点3",
                "操作模式": "告警推送",
                "变量选择": "地点"
            }
        }
    }
    """
    browser = get_global_var("browser")
    # 等待页面加载
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]")))
    sleep(2)

    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 操作模式
    if mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(mode)).click()
        log.info("设置操作模式: {0}".format(mode))
        sleep(1)

    # 获取操作模式当前选择值
    js = "return $(\"input[name='node_model_id']\").val();"
    operate_mode = browser.execute_script(js)
    log.info("操作模式: {0}".format(operate_mode))
    if operate_mode == "1201":
        operate_mode = "结果呈现/下载"
    elif operate_mode == "1202":
        operate_mode = "微信消息推送"
    elif operate_mode == "1203":
        operate_mode = "告警推送"
    else:
        raise Exception("获取操作模式失败")
    log.info("操作模式转义: {0}".format(operate_mode))

    if operate_mode == "结果呈现/下载":
        # 切换到信息配置iframe
        browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'resultNodeInfoCfg.html')]"))

        # 信息描述
        if info_desc:
            browser.find_element(By.XPATH, "//*[@name='resultDesc']/preceding-sibling::input").clear()
            input_xpath = "//*[@name='resultDesc']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=info_desc)
            log.info("设置信息描述: {0}".format(info_desc))
            sleep(1)

        # 显示在运行信息的标题
        js = 'return $("#isshow")[0].checked;'
        status = browser.execute_script(js)
        log.info("【显示在运行信息的标题】勾选状态: {0}".format(status))
        # 聚焦元素
        is_show = browser.find_element(By.XPATH, "//*[@for='isshow']")
        browser.execute_script("arguments[0].scrollIntoView(true);", is_show)
        if show:
            if show == "是":
                if not status:
                    is_show.click()
                log.info("勾选【显示在运行信息的标题】")
            else:
                if status:
                    is_show.click()
                log.info("取消勾选【显示在运行信息的标题】")

        # 信息明细
        if info:
            text_area = browser.find_element(By.XPATH, "//*[@id='resultDetail']")
            set_blob(textarea=text_area, array=info)
            log.info("信息明细填写完成")
            sleep(1)

        # 启用下载
        if download_set:
            # 获取启用下载当前勾选状态
            js = 'return $("#isdownload")[0].checked;'
            status = browser.execute_script(js)
            log.info("【启用下载】勾选状态: {0}".format(status))
            # 聚焦元素
            enable_download = browser.find_element(By.XPATH, "//*[@for='isdownload']")
            browser.execute_script("arguments[0].scrollIntoView(true);", enable_download)
            if download_set.get("状态") == "开启":
                if not status:
                    enable_download.click()
                log.info("勾选【启用下载】")

                # 文件配置
                file_set = download_set.get("文件配置")
                num = 1
                flag = True
                while flag:

                    # 先获取文件过滤类型
                    js = "return $(\"input[name='catagoryId{0}']\").val();".format(num)
                    download_dir = browser.execute_script(js)
                    log.info("下载目录: {0}".format(download_dir))
                    if download_dir:
                        num += 1
                    else:
                        log.info("当前开始从第{0}行开始配置文件".format(num))

                        if num > 1:
                            browser.find_element(
                                By.XPATH, "//*[@id='file_name{0}']/../following-sibling::div[1]/a[@onclick='addFileDownPath()']".format(
                                    num - 1)).click()
                        flag = False

                for f in file_set:
                    set_download_file(file_path=f.get("目录"), file_name=f.get("文件名"), row_num=num)
                    if f != file_set[-1]:
                        browser.find_element(
                            By.XPATH, "//*[@id='downloadDiv']/div[{0}]//*[@onclick='addFileDownPath()']".format(num)).click()
                        num += 1
            elif download_set.get("状态") == "关闭":
                if status:
                    enable_download.click()
                    log.info("取消勾选【启用下载】")
                else:
                    log.info("【启用下载: flag】标识为否，不开启")
            else:
                raise KeyError("【启用下载】状态只支持：开启/关闭")

        # 返回到上层iframe
        browser.switch_to.parent_frame()
    elif operate_mode == "告警推送":
        # 切换到信息推送iframe
        wait = WebDriverWait(browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[contains(@src,'noticeNodeInfoCfg.html')]")))
        # browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'noticeNodeInfoCfg.html')]"))
        wait = WebDriverWait(browser, 30)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='dataH_noticeVarName']/following-sibling::span//a")))

        # 变量选择
        if var_name:
            browser.find_element(By.XPATH, "//*[@id='dataH_noticeVarName']/following-sibling::span//a").click()
            choose_var(var_name=var_name)
            log.info("变量选择: {0}".format(var_name))

        # 返回到上层iframe
        browser.switch_to.parent_frame()
    else:
        # 微信推送
        pass

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='saveInfoHandleBtn']//*[text()='保存']").click()
    log.info("保存业务配置")

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("保存成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    set_global_var("ResultMsg", msg, False)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name


def set_download_file(file_path, file_name, row_num):
    browser = get_global_var("browser")
    num = row_num
    # 目录
    browser.find_element(By.XPATH, "//*[@name='catagoryId{0}']/preceding-sibling::input".format(num)).click()
    choose_file_dir(dir_name=file_path)

    # 文件名
    browser.find_element(By.XPATH, "//*[@name='file_name{0}']/preceding-sibling::input".format(num)).clear()
    input_xpath = "//*[@name='file_name{0}']/preceding-sibling::input".format(num)
    set_text_enable_var(input_xpath=input_xpath, msg=file_name)
    log.info("输入文件名: {0}".format(file_name))
    log.info("第{0}行文件配置完成".format(num))
    sleep(1)
