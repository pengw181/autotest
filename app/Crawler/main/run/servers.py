# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/13 下午5:10

from common.log.logger import log
from common.wrapper.autoLogin import auto_login_tool
from app.Crawler.config.crawlerTemplate import CrawlerTemplate


@auto_login_tool
def actions(func, param):

    run_flag = True

    if func == "AddCrawlerTemplate":

        action = CrawlerTemplate()
        action.add(template_name=param.get("模版名称"), system_name=param.get("目标系统"),
                   advance_set=param.get("高级配置"))

    elif func == "UpdateCrawlerTemplate":

        action = CrawlerTemplate()
        update_map = param.get("修改内容")
        action.update(obj=param.get("目标模版"), template_name=update_map.get("模版名称"),
                      system_name=update_map.get("目标系统"), advance_set=update_map.get("高级配置"))

    elif func == "DeleteCrawlerTemplate":

        action = CrawlerTemplate()
        action.delete(obj=param.get("目标模版"))

    elif func == "CrawlerTemplateDataClear":

        action = CrawlerTemplate()
        action.data_clear(obj=param.get("模版名称"))

    elif func == "ElementConfiguration":

        action = CrawlerTemplate()
        action.element_config(template_name=param.get("模版名称"), element_config=param.get("元素配置"))

    elif func == "ElementTreeSet":

        action = CrawlerTemplate()
        action.element_tree_set(template_name=param.get("模版名称"), tree_set=param.get("操作树"))

    else:
        log.error("无效的动作函数")
        run_flag = False

    return run_flag
