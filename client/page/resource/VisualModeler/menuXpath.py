# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:50

# 定义一级菜单xpath
first_menu_xpath = {
    "个人中心": "//*[text()='个人中心']",
    "流程编辑器": "//*[text()='流程编辑器']",
    "指令配置": "//*[text()='指令配置']",
    "常用信息管理": "//*[text()='常用信息管理']",
    "统计分析": "//*[text()='统计分析']",
    "数据拼盘": "//*[text()='数据拼盘']",
    "任务管家": "//*[text()='任务管家']",
    "云平台": "//*[@mid='CloudBrain1001']/*[text()='云平台']",
    "告警": "//*[@mid='AlarmPlatform1001']/*[text()='告警']",
    "OA审批": "//*[@mid='Approval1001']/*[text()='OA审批']"
}

# 定义二级菜单xpath
second_menu_xpath = {
    "我的监控": "//a[@mid='PersonalCenter2001']",
    "流程配置": "//a[@mid='Treasury2001']",
    "流程运行日志": "//a[@mid='Treasury2002']",
    "指令集": "//a[@mid='Cmd2001']",
    "指令模版": "//a[@mid='Cmd2002']",
    "指令任务": "//a[@mid='Cmd2003']",
    "正则模版管理": "//a[@mid='Cmd2005']",
    "通用指令解析配置": "//a[@mid='Cmd2004']",
    "变量管理": "//a[@mid='Cmd2006']",
    "指令集黑名单": "//a[@mid='Treasury2001']",
    "网元模版配置": "//a[@mid='DeviceManager2001']",
    "机房信息": "//a[@mid='Common2002']",
    "专业领域管理": "//a[@mid='Common2003']",
    "文件目录管理": "//a[@mid='CataLogMgr2002']",
    "个人目录": "//a[@mid='CataLogMgr3001']",
    "系统目录": "//a[@mid='CataLogMgr3002']",
    "脚本管理": "//a[@mid='Sciprt2001']",
    "AI模型管理": "//a[@mid='Algorithm2001']",
    "OCR识别管理": "//a[@mid='OcrCfg2001']",
    "代理管理": "//a[@mid='Proxy2001']",
    "指标管理": "//a[@mid='Treasury2001']",
    "数据库管理": "//a[@mid='DatabaseMgr2001']",
    "邮箱管理": "//a[@mid='EmailMgr2003']",
    "远程FTP服务器管理": "//a[@mid='FtpMgr2005']",
    "第三方系统管理": "//a[@mid='VosMgr2004']",
    "第三方接口管理": "//a[@mid='VosInterface2005']",
    "微信平台管理": "//a[@mid='wechatPlatform2001']",
    "模版配置": "//a[@mid='Param2001']",
    "数据更新日志": "//a[@mid='Param2003']",
    "任务模版管理": "//a[@mid='Naga2001']",
    "云平台": "//a[@mid='CloudBrain2001']",
    "告警平台": "//a[@mid='AlarmPlatform2001']",
    "数据接入平台": "//a[@mid='DataAccess2001']",
    "OA审批平台": "//a[@mid='ApprovalIndex2001']"
}

# 定义三级菜单xpath
third_menu_xpath = {
    "个人目录": "//*[@mid='CataLogMgr3001']/*[text()='个人目录']",
    "系统目录": "//*[@mid='CataLogMgr3002']/*[text()='系统目录']"
}
