# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/14 下午6:41

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


# def get_tab_xpath(tab):
#     """
#     # 获取标签xpath
#     :param tab: 标签名
#     :return: xpath or None
#     """
#     result = tab_xpath.get(tab)
#     if result is None:
#         raise Exception("tab标签【(0)】未定义".format(tab))
#     return result
