# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午6:10

from time import sleep
from selenium.webdriver.common.by import By
from client.page.func.alertBox import BeAlertBox
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


def common_business(node_name, scene):
    """
    :param node_name: 节点名称
    :param scene: 场景标识，无或其它具体值

    {
        "操作": "NodeBusinessConf",
        "参数": {
            "流程名称": "pw自动化测试流程新",
            "节点类型": "通用节点",
            "节点名称": "通用节点",
            "业务配置": {
                "节点名称": "通用节点1",
                "场景标识": "无"
            }
        }
    }
    """
    browser = get_global_var("browser")
    # 设置节点名称
    if node_name:
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").clear()
        browser.find_element(By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").send_keys(node_name)
        log.info("设置节点名称: {0}".format(node_name))

    # 设置场景标识
    if scene:
        browser.find_element(By.XPATH, "//*[@name='scene_flag']/preceding-sibling::input[1]").click()
        sleep(1)
        browser.find_element(By.XPATH, "//*[contains(@id,'scene_flag') and text()='{0}']".format(scene)).click()
        log.info("设置场景标识: {0}".format(scene))

    # 获取节点名称
    node_name = browser.find_element(
        By.XPATH, "//*[@name='node_name']/preceding-sibling::input[1]").get_attribute("value")

    # 保存业务配置
    browser.find_element(By.XPATH, "//*[@id='save_usual_retrieve']/span/span[1]").click()

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
