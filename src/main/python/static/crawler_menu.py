# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/2/8 下午2:55

# 定义一级菜单xpath
first_menu_xpath = {
    "任务": "//*[text()='任务']",
    "配置": "//*[text()='配置']"
}

# 定义二级菜单xpath
second_menu_xpath = {
    "运行实例": "//a[@menuid='CrawlerApp1001']",
    "爬虫模版": "//a[@menuid='CrawlerApp2001']",
    "第三方系统管理": "//a[@menuid='CrawlerApp2002']",
    "代理管理": "//a[@menuid='CrawlerApp2003']",
    "个人目录": "//a[@menuid='CrawlerApp2004']",
    "系统目录": "//a[@menuid='CrawlerApp2005']",
    "正则模版管理": "//a[@menuid='CrawlerApp2006']",
    "FTP服务器管理": "//a[@menuid='CrawlerApp2007']"
}

# 定义tab标签xpath
tab_xpath = {
    "爬虫模版": "//*[@lay-id='CrawlerApp2001']",
    "第三方系统管理": "//*[@lay-id='CrawlerApp2002']",
    "代理管理": "//*[@lay-id='CrawlerApp2003']",
    "个人目录": "//*[@lay-id='CrawlerApp2004']",
    "系统目录": "//*[@lay-id='CrawlerApp2005']",
    "正则模版管理": "//*[@lay-id='CrawlerApp2006']",
    "FTP服务器管理": "//*[@lay-id='CrawlerApp2007']"
}
