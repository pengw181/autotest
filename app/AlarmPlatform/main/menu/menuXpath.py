# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/10 下午5:19

# 定义一级菜单xpath
first_menu_xpath = {
    "连接配置": "//*[@class='index-menu']/*[text()='连接配置']",
    "告警配置": "//*[@class='index-menu']/*[text()='告警配置']",
    "推送计划": "//*[@class='index-menu']/*[text()='推送计划']",
    "告警信息": "//*[@class='index-menu']/*[text()='告警信息']",
    "推送日志": "//*[@class='index-menu']/*[text()='推送日志']",
}

# 定义二级菜单xpath
second_menu_xpath = {
    "关系型数据库配置": "//*[text()='关系型数据库配置']",
    "表归属配置": "//*[text()='表归属配置']",
    "ES数据库配置": "//*[text()='ES数据库配置']",
    "告警场景配置": "//*[text()='告警场景配置']",
    "FTP配置": "//*[text()='FTP配置']",
    "告警元数据": "//*[text()='告警元数据']",
    "字典配置": "//*[text()='字典配置']",
    "告警计划": "//*[text()='告警计划']",
    "告警规则": "//*[text()='告警规则']",
    "消息模版": "//*[text()='消息模版']"
}
