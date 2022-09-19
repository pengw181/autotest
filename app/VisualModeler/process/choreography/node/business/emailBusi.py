# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午10:05

from common.page.func.alertBox import BeAlertBox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.page.func.processVar import choose_var
from common.page.func.chooseDir import choose_file_dir, choose_ftp_dir
from common.page.func.input import set_text_enable_var, set_blob
from common.page.func.regular import RegularCube
from common.date.dateUtil import set_calendar
from common.page.func.upload import upload
from common.page.func.pageMaskWait import page_wait
from selenium.webdriver.common.action_chains import ActionChains
from common.log.logger import log
from common.variable.globalVariable import *


def email_business(node_name, mode, params_set):
    """
    # 接收
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试邮件节点流程",
            "节点类型": "邮件节点",
            "节点名称": "邮件节点",
            "业务配置": {
                "节点名称": "邮件节点1",
                "邮件模式": "接收",
                "参数配置": {
                    "接收邮箱": "pw@henghaodata.com",
                    "发件开始时间": {
                        "变量引用": "否",
                        "值": "2020-11-20 10:15"
                    },
                    "发件结束时间": {
                        "变量引用": "是",
                        "值": "${时间}"
                    },
                    "收件人": {
                        "正则匹配": "否",
                        "值": "pw@henghaodata.com"
                    },
                    "发件人": {
                        "正则匹配": "否",
                        "值": "pw@henghaodata.com"
                    },
                    "标题": {
                        "正则匹配": "是",
                        "值": {
                            "设置方式": "选择",
                            "正则模版名称": "pw按时间拆分",
                            "正则模版配置": []
                        }
                    },
                    "正文": {
                        "正则匹配": "否",
                        "值": "测试邮件"
                    },
                    "附件": {
                        "正则匹配": "否",
                        "值": "测试邮件"
                    },
                    "附件类型": ["txt", "xlsx"],
                    "存储附件": "开启",
                    "存储附件目录": "AI"
                }
            }
        }
    }

    # 发送
    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试邮件节点流程",
            "节点类型": "邮件节点",
            "节点名称": "邮件节点",
            "业务配置": {
                "节点名称": "邮件节点1",
                "邮件模式": "接收",
                "参数配置": {
                    "发件人": "pw@henghaodata.com",
                    "收件人": {
                        "类型": "自定义",
                        "方式": "请选择",
                        "值": ["pw@henghaodata.com", "pw@163.com"]
                    },
                    "抄送人": {
                        "方式": "变量",
                        "值": "参数1"
                    },
                    "标题": "测试邮件",
                    "正文": [
                        {
                            "类型": "自定义值",
                            "自定义值": "地点:"
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
                            "变量名": "流程实例ID"
                        }
                    ],
                    "附件": [
                        {
                            "操作类型": "添加",
                            "附件配置": {
                                "附件来源": "动态生成",
                                "附件标题": "动态生成标题",
                                "附件内容": "动态生成内容",
                                "附件类型": "csv"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "附件配置": {
                                "附件来源": "本地上传",
                                "文件名": "factor.xlsx"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "附件配置": {
                                "附件来源": "远程加载",
                                "本地": "本地",
                                "变量引用": "否",
                                "目录": "AI",
                                "过滤类型": "关键字",
                                "文件名": "加载文件"
                                "附件类型": "docx"
                            }
                        },
                        {
                            "操作类型": "添加",
                            "附件配置": {
                                "附件来源": "远程加载",
                                "本地": "远程",
                                "远程服务器": "pw-ftp测试",
                                "目录": "根目录-pw-1",
                                "变量引用": "否",
                                "过滤类型": "正则",
                                "文件名": {
                                    "设置方式": "选择",
                                    "正则模版名称": "pw按时间拆分",
                                    "正则模版配置": []
                                },
                                "附件类型": "jpeg"
                            }
                        }
                    ]
                }
            }
        }
    }
    """
    browser = get_global_var("browser")
    sleep(2)
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))
        sleep(1)

    # 邮件模式
    if mode:
        browser.find_element(By.XPATH, "//*[@name='node_model_id']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'node_model_id') and text()='{0}']".format(mode)).click()
        log.info("设置邮件模式: {0}".format(mode))
        page_wait()
        sleep(1)

    # 获取邮件模式当前选择值
    page_wait()
    js = "return $(\"input[name='node_model_id']\").val();"
    operate_mode = browser.execute_script(js)
    log.info("邮件模式: {0}".format(operate_mode))
    if operate_mode == "1001":
        operate_mode = "接收"
    elif operate_mode == "1002":
        operate_mode = "发送"
    else:
        raise Exception("获取邮件模式失败")
    log.info("邮件模式转义: {0}".format(operate_mode))

    # 参数配置
    if operate_mode == "接收":
        email_receive(receiver_email=params_set.get("接收邮箱"), begin_time=params_set.get("发件开始时间"),
                      end_time=params_set.get("发件结束时间"), receiver=params_set.get("收件人"),
                      sender=params_set.get("发件人"), email_title=params_set.get("标题"),
                      email_content=params_set.get("正文"), attach=params_set.get("附件"),
                      attach_type=params_set.get("附件类型"), storage=params_set.get("存储附件"),
                      storage_path=params_set.get("存储附件目录"))

    elif operate_mode == "发送":
        email_send(receiver=params_set.get("收件人"), sender=params_set.get("发件人"),
                   cc=params_set.get("抄送人"), email_title=params_set.get("标题"), email_content=params_set.get("正文"),
                   attach=params_set.get("附件"))
    else:
        raise KeyError("错误的邮件操作模式")

    # 获取节点名称
    node_name = browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='emailSaveBtn']//*[text()='保存']").click()
    log.info("保存业务配置")

    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("操作成功"):
        log.info("保存业务配置成功")
    else:
        log.warning("保存业务配置失败，失败提示: {0}".format(msg))
    set_global_var("ResultMsg", msg, False)

    # 刷新页面，返回画流程图
    browser.refresh()
    return node_name


def email_receive(receiver_email, begin_time, end_time, receiver, sender, email_title, email_content, attach,
                  attach_type, storage, storage_path):
    """
    :param receiver_email: 接收邮箱，必填
    :param begin_time: 发件开始时间，非必填，支持时间控件、变量
    :param end_time: 发件结束时间，非必填，支持时间控件、变量
    :param receiver: 收件人，非必填，支持关键字、正则
    :param sender: 发件人，非必填，支持关键字、正则
    :param email_title: 邮件标题，非必填，支持关键字、正则
    :param email_content: 邮件正文，非必填，支持关键字、正则
    :param attach: 附件内容，非必填，支持关键字、正则
    :param attach_type: 附件类型，非必填，可多选
    :param storage: 存储附件，字典，非必填
    :param storage_path: 存储附件目录
    """
    browser = get_global_var("browser")
    page_wait()
    # 切换到接收模式配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'emailReceive.html')]"))
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@name='account']/preceding-sibling::input")))

    # 接收邮箱
    if receiver_email:
        browser.find_element(By.XPATH, "//*[@name='account']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'account') and text()='{0}']".format(receiver_email)).click()
        log.info("设置接收邮箱: {0}".format(receiver_email))
        sleep(1)

    action = ActionChains(browser)

    # 发件开始时间
    if begin_time:
        # 获取发件开始时间 变量引用当前勾选状态
        js = 'return $("#userVar_1")[0].checked;'
        status = browser.execute_script(js)
        log.info("【发件开始时间 变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        use_var = browser.find_element(By.XPATH, "//*[@id='userVar_1']")

        action.move_to_element(use_var).perform()
        if begin_time.get("变量引用") == "是":
            if not status:
                use_var.click()
            log.info("勾选【发件开始时间 变量引用】")
            # 值
            input_xpath = "//*[@id='emailexpr_6']/following-sibling::span/input[1]"
            set_text_enable_var(input_xpath=input_xpath, msg=begin_time.get("值"))
        else:
            if status:
                use_var.click()
                log.info("取消勾选【发件开始时间 变量引用】")
            else:
                log.info("【发件开始时间 变量引用】标识为否，不开启")
            browser.find_element(By.XPATH, "//*[@id='sendEmailStartTime']/following-sibling::span//a").click()
            # 值
            set_calendar(date_s=begin_time.get("值"), date_format="%Y-%m-%d %H:%M")
        log.info("设置发件开始时间: {0}".format(begin_time))
        sleep(1)

    # 发件结束时间
    if end_time:
        # 获取发件开始时间 变量引用当前勾选状态
        js = 'return $("#userVar_2")[0].checked;'
        status = browser.execute_script(js)
        log.info("【发件结束时间 变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        use_var = browser.find_element(By.XPATH, "//*[@id='userVar_2']")
        action.move_to_element(use_var).perform()
        if end_time.get("变量引用") == "是":
            if not status:
                use_var.click()
            log.info("勾选【发件结束时间 变量引用】")
            # 值
            input_xpath = "//*[@id='emailexpr_7']/following-sibling::span/input[1]"
            set_text_enable_var(input_xpath=input_xpath, msg=end_time.get("值"))
        else:
            if status:
                use_var.click()
                log.info("取消勾选【发件结束时间 变量引用】")
            else:
                log.info("【发件结束时间 变量引用】标识为否，不开启")
            browser.find_element(By.XPATH, "//*[@id='sendEmailEndTime']/following-sibling::span//a").click()
            # 值
            set_calendar(date_s=end_time.get("值"), date_format="%Y-%m-%d %H:%M")
        log.info("设置发件结束时间: {0}".format(end_time))
        sleep(1)

    # 收件人
    if receiver:
        # 获取收件人 正则匹配当前勾选状态
        js = 'return $("#isRegex_1")[0].checked;'
        status = browser.execute_script(js)
        log.info("【收件人 正则匹配】勾选状态: {0}".format(status))
        # 聚焦元素
        use_regular = browser.find_element(By.XPATH, "//*[@id='isRegex_1']")
        action.move_to_element(use_regular).perform()
        if receiver.get("正则匹配") == "是":
            if not status:
                use_regular.click()
            log.info("勾选【收件人 正则匹配】")
            # 值
            browser.find_element(By.XPATH, "//*[@name='keyExpr1']/preceding-sibling::span/a").click()
            # 切换到正则配置iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular = receiver.get("值")
            if regular.get("高级模式") == "是":
                advance_mode = True
            else:
                advance_mode = False
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regular.get("设置方式"), regular_name=regular.get("正则模版名称"),
                                    advance_mode=advance_mode, regular=regular.get("标签配置"),
                                    expression=regular.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    # 切换到接收模式配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'emailReceive.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()
            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
            sleep(1)
        else:
            if status:
                use_regular.click()
                log.info("取消勾选【收件人 正则匹配】")
            else:
                log.info("【收件人 正则匹配】标识为否，不开启")
            # 值
            input_xpath = "//*[@name='emailexpr1']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=receiver.get("值"))
            sleep(1)

    # 发件人
    if sender:
        # 获取发件人 正则匹配当前勾选状态
        js = 'return $("#isRegex_2")[0].checked;'
        status = browser.execute_script(js)
        log.info("【发件人 正则匹配】勾选状态: {0}".format(status))
        # 聚焦元素
        use_regular = browser.find_element(By.XPATH, "//*[@id='isRegex_2']")
        action.move_to_element(use_regular).perform()
        if sender.get("正则匹配") == "是":
            if not status:
                use_regular.click()
            log.info("勾选【发件人 正则匹配】")
            # 值
            browser.find_element(By.XPATH, "//*[@name='keyExpr2']/preceding-sibling::span/a").click()
            # 切换到正则配置iframe
            browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular = sender.get("值")
            if regular.get("高级模式") == "是":
                advance_mode = True
            else:
                advance_mode = False
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regular.get("设置方式"), regular_name=regular.get("正则模版名称"),
                                    advance_mode=advance_mode, regular=regular.get("标签配置"),
                                    expression=regular.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    # 切换到接收模式配置iframe
                    browser.switch_to.frame(
                        browser.find_element(By.XPATH, "//*[contains(@src,'emailReceive.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()
            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
            sleep(1)
        else:
            if status:
                use_regular.click()
                log.info("取消勾选【发件人 正则匹配】")
            else:
                log.info("【发件人 正则匹配】标识为否，不开启")
            # 值
            input_xpath = "//*[@name='emailexpr2']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=sender.get("值"))
            sleep(1)

    # 标题
    if email_title:
        # 获取标题 正则匹配当前勾选状态
        js = 'return $("#isRegex_3")[0].checked;'
        status = browser.execute_script(js)
        log.info("【标题 正则匹配】勾选状态: {0}".format(status))
        # 聚焦元素
        use_regular = browser.find_element(By.XPATH, "//*[@id='isRegex_3']")
        action.move_to_element(use_regular).perform()
        if email_title.get("正则匹配") == "是":
            if not status:
                use_regular.click()
            log.info("勾选【标题 正则匹配】")
            # 值
            browser.find_element(By.XPATH, "//*[@name='keyExpr3']/preceding-sibling::span/a").click()
            # 切换到正则配置iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular = email_title.get("值")
            if regular.get("高级模式") == "是":
                advance_mode = True
            else:
                advance_mode = False
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regular.get("设置方式"), regular_name=regular.get("正则模版名称"),
                                    advance_mode=advance_mode, regular=regular.get("标签配置"),
                                    expression=regular.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    # 切换到接收模式配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'emailReceive.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()
            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
            sleep(1)
        else:
            if status:
                use_regular.click()
                log.info("取消勾选【标题 正则匹配】")
            else:
                log.info("【标题 正则匹配】标识为否，不开启")
            # 值
            input_xpath = "//*[@name='emailexpr3']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=email_title.get("值"))
            sleep(1)

    # 正文
    if email_content:
        # 获取正文 正则匹配当前勾选状态
        js = 'return $("#isRegex_4")[0].checked;'
        status = browser.execute_script(js)
        log.info("【正文 正则匹配】勾选状态: {0}".format(status))
        # 聚焦元素
        use_regular = browser.find_element(By.XPATH, "//*[@id='isRegex_4']")
        action.move_to_element(use_regular).perform()
        if email_content.get("正则匹配") == "是":
            if not status:
                use_regular.click()
            log.info("勾选【正文 正则匹配】")
            # 值
            browser.find_element(By.XPATH, "//*[@name='keyExpr4']/preceding-sibling::span/a").click()
            # 切换到正则配置iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular = email_content.get("值")
            if regular.get("高级模式") == "是":
                advance_mode = True
            else:
                advance_mode = False
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regular.get("设置方式"), regular_name=regular.get("正则模版名称"),
                                    advance_mode=advance_mode, regular=regular.get("标签配置"),
                                    expression=regular.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    # 切换到接收模式配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'emailReceive.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()
            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
            sleep(1)
        else:
            if status:
                use_regular.click()
                log.info("取消勾选【正文 正则匹配】")
            else:
                log.info("【正文 正则匹配】标识为否，不开启")
            # 值
            input_xpath = "//*[@name='emailexpr4']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=email_content.get("值"))
            sleep(1)

    # 附件
    if attach:
        # 获取正文 正则匹配当前勾选状态
        js = 'return $("#isRegex_5")[0].checked;'
        status = browser.execute_script(js)
        log.info("【附件 正则匹配】勾选状态: {0}".format(status))
        # 聚焦元素
        use_regular = browser.find_element(By.XPATH, "//*[@id='isRegex_5']")
        action.move_to_element(use_regular).perform()
        if attach.get("正则匹配") == "是":
            if not status:
                use_regular.click()
            log.info("勾选【附件 正则匹配】")
            # 值
            browser.find_element(By.XPATH, "//*[@name='keyExpr5']/preceding-sibling::span/a").click()
            # 切换到正则配置iframe
            browser.switch_to.frame(
                browser.find_element(By.XPATH, "//iframe[contains(@src,'operateWashRegexBox.html')]"))
            regular = attach.get("值")
            if regular.get("高级模式") == "是":
                advance_mode = True
            else:
                advance_mode = False
            regular_cube = RegularCube()
            regular_cube.setRegular(set_type=regular.get("设置方式"), regular_name=regular.get("正则模版名称"),
                                    advance_mode=advance_mode, regular=regular.get("标签配置"),
                                    expression=regular.get("表达式"))
            if regular_cube.needJumpIframe:
                alert = BeAlertBox(back_iframe="default")
                msg = alert.get_msg()
                if alert.title_contains("成功"):
                    log.info("保存正则模版成功")
                    # 切换到节点iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                    # 切换到业务配置iframe
                    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                    # 切换到接收模式配置iframe
                    browser.switch_to.frame(
                        browser.find_element(By.XPATH, "//*[contains(@src,'emailReceive.html')]"))
                else:
                    log.warning("保存正则模版失败，失败提示: {0}".format(msg))
                set_global_var("resultMsg", msg, False)
            else:
                # 返回上层iframe
                browser.switch_to.parent_frame()
            # 关闭正则魔方配置
            browser.find_element(
                By.XPATH, "//*[text()='正则魔方']/following-sibling::div/a[contains(@class,'close')]").click()
            sleep(1)
        else:
            if status:
                use_regular.click()
                log.info("取消勾选【附件 正则匹配】")
            else:
                log.info("【附件 正则匹配】标识为否，不开启")
            # 值
            input_xpath = "//*[@name='emailexpr5']/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=attach.get("值"))
            sleep(1)

    # 附件类型
    if attach_type:
        browser.find_element(By.XPATH, "//*[@name='attachtype']/preceding-sibling::input").click()
        for i in attach_type:
            browser.find_element(By.XPATH, "//*[contains(@id,'attachtype') and text()='{0}']".format(i)).click()
        log.info("设置附件类型: {0}".format(",".join(attach_type)))
        browser.find_element(By.XPATH, "//*[@name='attachtype']/preceding-sibling::input").click()
        sleep(1)

    # 存储附件
    js = 'return $("#isSaveAttach")[0].checked;'
    status = browser.execute_script(js)
    log.info("【存储附件】勾选状态: {0}".format(status))
    # 聚焦元素
    save_attach = browser.find_element(By.XPATH, "//*[@id='isSaveAttach']")
    browser.execute_script("arguments[0].scrollIntoView(true);", save_attach)
    if storage == "开启":
        if not status:
            save_attach.click()
            log.info("勾选【存储附件】")
        else:
            log.info("【存储附件】已开启")
    else:
        if status:
            save_attach.click()
            log.info("取消勾选【存储附件】")
        else:
            log.info("【存储附件】未开启")

    # 存储附件目录
    if storage_path:
        browser.find_element(By.XPATH, "//*[@name='catagory_id']/preceding-sibling::input").click()
        choose_file_dir(dir_name=storage_path)

    # 返回到上层iframe
    browser.switch_to.parent_frame()


def email_send(sender, receiver, email_title, email_content, cc, attach):
    """
    :param sender: 发件人，必填，选择
    :param receiver: 收件人，必填，可选择，可变量
    :param email_title: 邮件标题，必填
    :param email_content: 邮件正文，必填
    :param cc: 抄送人，非必填，可选择，可变量
    :param attach: 附件，非必填，字典
    """
    browser = get_global_var("browser")
    # 切换到信息推送iframe
    page_wait()
    browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'emailSend.html')]"))
    wait = WebDriverWait(browser, 30)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='sender']/following-sibling::span//a")))
    sleep(1)

    # 发件人
    if sender:
        browser.find_element(By.XPATH, "//*[@id='sender']/following-sibling::span//a").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'sender') and text()='{0}']".format(sender)).click()
        log.info("设置发件人: {0}".format(sender))
        sleep(1)

    # 收件人
    if receiver:
        # 类型
        if receiver.__contains__("类型"):
            receiver_type = receiver.get("类型")
            if receiver_type == "自定义":
                browser.find_element(By.XPATH, "//*[@id='getrecipientsBtn_1']").click()
            else:
                browser.find_element(By.XPATH, "//*[@id='getrecipientsBtn_2']").click()
            log.info("设置收件人类型: {0}".format(receiver_type))

        # 方式。因无法通过js获取方式下拉框的值，所以方式设置为必须参数
        choose_type = receiver.get("方式")
        browser.find_element(By.XPATH, "//*[@id='selUser1']/following-sibling::span//input[1]").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'selUser1') and text()='{0}']".format(choose_type)).click()
        log.info("设置收件人方式: {0}".format(choose_type))
        sleep(1)

        # 值
        receiver_obj = receiver.get("值")
        if choose_type == "请选择":
            browser.find_element(By.XPATH, "//*[@id='recipients_sel']/following-sibling::span//a").click()
            for i in receiver_obj:
                browser.find_element(By.XPATH, "//*[contains(@id,'recipients_sel') and text()='{0}']".format(i)).click()
            # 再点击一次，隐藏下拉框
            browser.find_element(By.XPATH, "//*[@id='recipients_sel']/following-sibling::span//a").click()
            log.info("设置收件人: {0}".format(",".join(receiver_obj)))
        else:
            # 自定义
            browser.find_element(By.XPATH, "//*[@id='dataH_recipientsName']/following-sibling::span//a").click()
            choose_var(var_name=receiver_obj)
            log.info("设置收件人: {0}".format(receiver_obj))
        sleep(1)

    # 抄送人
    if cc:
        browser.find_element(By.XPATH, "//*[@id='selUser2']/following-sibling::span//input[1]").click()
        # 方式
        choose_type = cc.get("方式")
        browser.find_element(By.XPATH, "//*[contains(@id,'selUser2') and text()='{0}']".format(choose_type)).click()
        log.info("设置抄送人方式: {0}".format(choose_type))
        sleep(1)

        # 值
        cc_obj = cc.get("值")
        if choose_type == "请选择":
            browser.find_element(By.XPATH, "//*[@id='copySenders']/following-sibling::span//a").click()
            for i in cc_obj:
                browser.find_element(By.XPATH, "//*[contains(@id,'copySenders') and text()='{0}']".format(i)).click()
            # 再点击一次，隐藏下拉框
            browser.find_element(By.XPATH, "//*[@id='copySenders']/following-sibling::span//a").click()
            log.info("设置抄送人: {0}".format(",".join(cc_obj)))
        else:
            browser.find_element(By.XPATH, "//*[@id='dataH_copySendersName']/following-sibling::span//a").click()
            choose_var(var_name=cc_obj)
            log.info("设置抄送人: {0}".format(cc_obj))
        sleep(1)

    # 标题
    if email_title:
        input_xpath = "//*[@name='theme']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=email_title)
        log.info("设置标题: {0}".format(email_title))
        sleep(1)

    # 正文
    if email_content:
        text_area = browser.find_element(By.XPATH, "//*[@id='email_content']")
        action = ActionChains(browser)
        action.move_to_element(text_area).perform()
        set_blob(textarea=text_area, array=email_content)
        log.info("设置正文: {0}".format(email_content))
        sleep(1)

    # 附件
    if attach:
        row = len(attach)
        log.info("需要设置{0}条附件".format(row))
        for attach in attach:
            opt = attach.get("操作类型")
            attach_msg = attach.get("附件配置")
            attach_opt(opt=opt, attach=attach_msg)
            log.info("附件设置成功")

    # 返回到上层iframe
    browser.switch_to.parent_frame()


def attach_opt(opt, attach):
    """
    :param opt: 操作类型，添加/修改/删除, 必填
    :param attach: 附件信息，字典，必填
    :return: 自动点击保存，并返回到上层iframe

    ---attach---
    # 动态生成
    {
        "附件来源": "动态生成",
        "附件标题": "动态生成标题",
        "附件内容": "动态生成内容",
        "附件类型": "csv"
    }

    # 本地上传
    {
        "附件来源": "本地上传",
        "文件名": "factor.xlsx"
    }

    # 远程加载-本地
    {
        "附件来源": "远程加载",
        "存储类型": "本地",
        "变量引用": "否",
        "目录": "AI",
        "过滤类型": "关键字",
        "文件名": "加载文件"
        "附件类型": "docx"
    }

    # 远程加载-ftp
    {
        "附件来源": "远程加载",
        "存储类型": "远程",
        "远程服务器": "pw-ftp测试",
        "目录": "根目录-pw-1",
        "变量引用": "否",
        "过滤类型": "正则",
        "文件名": {
            "设置方式": "选择",
            "正则模版名称": "pw按时间拆分"
        },
        "附件类型": "jpeg"
    }
    """
    browser = get_global_var("browser")
    attach_obj = browser.find_element(By.XPATH, "//*[@onclick='toAddAttachPage()']//*[text()='添加']")
    browser.execute_script("arguments[0].scrollIntoView(true);", attach_obj)
    # 操作类型
    if opt == "添加":
        browser.find_element(By.XPATH, "//*[@onclick='toAddAttachPage()']//*[text()='添加']").click()
        sleep(1)
        # 切换到附件配置iframe，这里有两层
        wait = WebDriverWait(browser, 30)
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'addEmailAttach.html')]")))
        wait.until(ec.frame_to_be_available_and_switch_to_it((
            By.XPATH, "//iframe[contains(@src,'attachFileUpload.html')]")))

        # 附件来源
        if attach.__contains__("附件来源"):
            attach_source = attach.get("附件来源")
            if attach_source == "动态生成":
                browser.find_element(By.XPATH, "//*[@id='dybuild']").click()
            elif attach_source == "本地上传":
                browser.find_element(By.XPATH, "//*[@id='localUp']").click()
            elif attach_source == "远程加载":
                browser.find_element(By.XPATH, "//*[@id='remoteUp']").click()
            else:
                raise KeyError("附件来源仅支持：动态生成、本地上传、远程加载")
        else:
            attach_source = "动态生成"
            browser.find_element(By.XPATH, "//*[@id='dybuild']").click()
        log.info("附件来源: {0}".format(attach_source))
        page_wait()
        sleep(2)

        # 动态生成
        if attach_source == "动态生成":
            attach_build(attach_tile=attach.get("附件标题"), attach_content=attach.get("附件内容"),
                         attach_type=attach.get("附件类型"))
        elif attach_source == "本地上传":
            # browser.find_element(By.XPATH, "//*[contains(@for,'filebox_file_id')]").click()
            # sleep(1)
            upload(file_name=attach.get("文件名"))
            sleep(1)
        else:
            attach_remote_up(storage_type=attach.get("存储类型"), ftp=attach.get("远程服务器"),
                             use_var=attach.get("变量引用"), dir_name=attach.get("目录"),
                             filter_type=attach.get("过滤类型"), file_name=attach.get("文件名"),
                             file_type=attach.get("附件类型"))
    elif opt == "修改":
        # TODO
        log.info("附件修改成功")
    else:
        # TODO
        log.info("附件删除成功")

    # 点击保存
    browser.find_element(By.XPATH, "//*[@onclick='saveAttachInfoCom()']").click()
    alert = BeAlertBox(back_iframe="default")
    msg = alert.get_msg()
    if alert.title_contains("成功"):
        log.info("保存附件成功")
    else:
        log.warning("保存附件失败，失败提示: {0}".format(msg))
    set_global_var("ResultMsg", msg, False)

    # 切换到节点iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
    # 切换到业务配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
    # 切换到发送模式配置iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, "//*[contains(@src,'emailSend.html')]"))
    sleep(1)


def attach_build(attach_tile, attach_content, attach_type):
    """
    :param attach_tile: 附件标题, 添加时必填，修改非必填
    :param attach_content: 附件正文, 添加时必填，修改非必填
    :param attach_type: 附件类型, 非必填
    """
    browser = get_global_var("browser")
    log.info("设置动态生成附件")
    # 附件标题
    if attach_tile:
        input_xpath = "//*[@name='attachTitle']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=attach_tile)
        log.info("设置附件标题: {0}".format(attach_tile))
        sleep(1)

    # 附件内容
    if attach_content:
        input_xpath = "//*[@name='attachContent']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=attach_content)
        log.info("设置附件内容: {0}".format(attach_content))
        sleep(1)

    # 附件类型
    if attach_type:
        browser.find_element(By.XPATH, "//*[@name='attachType']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'attachType') and text()='{0}']".format(attach_type)).click()
        log.info("设置附件类型: {0}".format(attach_type))
        sleep(1)


def attach_remote_up(storage_type, ftp, use_var, dir_name, filter_type, file_name, file_type):
    """
    :param storage_type: 存储类型，本地/远程，非必填
    :param ftp: storage_type选择远程时需要，非必填
    :param use_var: 变量引用，是/否
    :param dir_name: 个人目录/ftp目录，必填
    :param filter_type: 关键字/正则，非必填
    :param file_name: 文件名/正则配置，必填
    :param file_type: 文件类型，必填
    """
    browser = get_global_var("browser")
    log.info("设置远程加载附件")
    # 存储类型
    if storage_type:
        if storage_type == "本地":
            browser.find_element(By.XPATH, "//*[@id='remote_local']").click()
        else:
            browser.find_element(By.XPATH, "//*[@id='remote_server']").click()
        log.info("设置存储类型: {0}".format(storage_type))
        sleep(1)

    # 获取存储类型当前选定值
    js = 'return $("#remote_local")[0].checked;'
    status_local = browser.execute_script(js)
    js = 'return $("#remote_server")[0].checked;'
    status_server = browser.execute_script(js)
    if status_local and not status_server:
        log.info("存储类型当前选择: 本地")
        storage_type = "本地"
    elif not status_local and status_server:
        log.info("存储类型当前选择: 远程")
        storage_type = "远程"
    else:
        raise Exception("获取存储类型失败")

    # 根据存储类型来决定操作
    if storage_type == "本地":
        # 获取目录 变量引用当前勾选状态
        js = 'return $("#local_isKeyword")[0].checked;'
        status = browser.execute_script(js)
        log.info("【目录 变量引用】勾选状态: {0}".format(status))
        # 聚焦元素
        enable_var = browser.find_element(By.XPATH, "//*[@id='local_isKeyword']")
        browser.execute_script("arguments[0].scrollIntoView(true);", enable_var)
        if use_var == "是":
            if not status:
                enable_var.click()
            log.info("勾选【目录 变量引用】")
            input_xpath = "//*[contains(@name,'keyword')]/preceding-sibling::input"
            set_text_enable_var(input_xpath=input_xpath, msg=dir_name)
        else:
            if status:
                enable_var.click()
                log.info("取消勾选【附件 正则匹配】")
            else:
                log.info("【目录 变量引用】标识为否，不开启")
            browser.find_element(
                By.XPATH, "//*[@id='local_choose_span']//*[@name='srcPath']/preceding-sibling::input").click()
            choose_file_dir(dir_name=dir_name)
            log.info("设置目录: {0}".format(dir_name))
            sleep(1)
    else:
        # 选择ftp
        browser.find_element(By.XPATH, "//*[@id='remote_srcServerId']/following-sibling::span//input[1]").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'remote_srcServerId') and text()='{0}']".format(ftp)).click()
        log.info("选择ftp: {0}".format(ftp))
        sleep(1)

        # 选择ftp目录
        browser.find_element(By.XPATH, "//*[@name='srcPath']/preceding-sibling::input").click()
        choose_ftp_dir(path=dir_name)
        log.info("选择ftp目录: {0}".format(dir_name))
        sleep(1)

    # 过滤类型
    if filter_type:
        browser.find_element(By.XPATH, "//*[@id='fileFilterType1']/following-sibling::span//input[1]").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileFilterType') and text()='{0}']".format(filter_type)).click()
        log.info("选择过滤类型: {0}".format(filter_type))
        sleep(1)

    # 获取过滤类型当前选定类型
    filter_ele = browser.find_element(By.XPATH, "//*[@id='fileFilterType1']/following-sibling::span//input[2]")
    filter_type = filter_ele.get_attribute("value")
    if filter_type == "0":
        filter_type = "关键字"
    else:
        filter_type = "正则"
    log.info("过滤类型当前选择: {0}".format(filter_type))

    # 文件名
    if filter_type == "关键字":
        input_xpath = "//*[@name='filepath1']/preceding-sibling::input"
        set_text_enable_var(input_xpath=input_xpath, msg=file_name)
        log.info("设置文件名: {0}".format(file_name))
    else:
        browser.find_element(By.XPATH, "//*[@id='keyExpr2']/following-sibling::span//a[1]").click()
        sleep(1)
        browser.switch_to.frame(
            browser.find_element(
                By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]"))
        confirm_selector = "//*[@id='regexpPopUp']"
        regular_cube = RegularCube()
        regular_cube.setRegular(confirm_selector=confirm_selector, set_type=file_name.get("设置方式"),
                                regular_name=file_name.get("正则模版名称"), advance_mode=file_name.get("高级模式"),
                                regular=file_name.get("标签配置"), expression=file_name.get("表达式"))
        if regular_cube.needJumpIframe:
            alert = BeAlertBox(back_iframe="default")
            msg = alert.get_msg()
            if alert.title_contains("成功"):
                log.info("保存正则模版成功")
                # 切换到节点iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, get_global_var("NodeIframe")))
                # 切换到业务配置iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[@id='busi_node']"))
                # 切换到接收模式配置iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//*[contains(@src,'emailSend.html')]"))
                # 切换到添加附件iframe
                browser.switch_to.frame(browser.find_element(By.XPATH, "//iframe[contains(@src,'addEmailAttach.html')]"))
                # 切换到附件配置iframe
                browser.switch_to.frame(
                    browser.find_element(By.XPATH, "//iframe[contains(@src,'attachFileUpload.html')]"))
                # 切换到配置正则iframe
                browser.switch_to.frame(
                    browser.find_element(
                        By.XPATH, "//iframe[contains(@src,'/VisualModeler/frame/regexcube/regexpTmplPopUpWin.html')]"))
            else:
                log.warning("保存正则模版失败，失败提示: {0}".format(msg))
            set_global_var("resultMsg", msg, False)

        # 点击确定
        browser.find_element(By.XPATH, "//*[@id='regexp-ok']//*[text()='确定']").click()

        # 返回上层iframe
        browser.switch_to.parent_frame()
        log.info("正则设置完成")
        sleep(1)

    # 文件类型
    if file_type:
        browser.find_element(By.XPATH, "//*[@name='fileType1']/preceding-sibling::input").click()
        browser.find_element(By.XPATH, "//*[contains(@id,'fileType1') and text()='{0}']".format(file_type)).click()
        log.info("设置文件类型: {0}".format(file_type))
        sleep(1)
