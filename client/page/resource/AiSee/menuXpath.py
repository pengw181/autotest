# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:47

# 定义menu菜单各功能按钮xpath
bar_xpath = {
    "用户管理": "//*[contains(@onclick,'用户管理')]",
    "角色管理": "//*[contains(@onclick,'角色管理')]",
    "功能管理": "//*[contains(@onclick,'功能管理')]",
    "网元管理": "//*[contains(@onclick,'网元管理')]",
    "平台日志": "//*[contains(@onclick,'平台日志')]",
    "应用中心": "//*[contains(@onclick,'appMan')]",
    "云平台": "//*[contains(@onclick,'Cloudbrain')]",
    "告警平台": "//*[contains(@onclick,'AlarmPlatform')]",
    "安全审计": "//*[contains(@onclick,'AiSafe')]",
    "登录页配置": "//*[contains(@onclick,'登录页配置')]"
}


tab_xpath = {
    "仪表盘": "//*[text()='仪表盘']",
    "个人看板": "//*[text()='个人看板']",
    "公告中心": "//*[text()='公告中心']",
    "消息中心": "//*[text()='消息中心']"
}