# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/13 下午5:35

from src.main.python.lib.globals import gbl
from src.main.python.core.controller.VisualModeler.servers import actions as visual_actions
from src.main.python.core.controller.Crawler.servers import actions as crawler_actions
from src.main.python.core.controller.AiSee.servers import actions as aisee_actions
from src.main.python.core.controller.AlarmPlatform.servers import actions as alarm_actions


def serverRun(func, param):
    """
    根据系统名称，到指定系统的目录下加载操作方法
    :param func: 操作
    :param param: 参数
    """
    application = gbl.service.get("application")

    if application == "VisualModeler":
        run_flag = visual_actions(func, param)
    elif application == "Crawler":
        run_flag = crawler_actions(func, param)
    elif application == "AiSee":
        run_flag = aisee_actions(func, param)
    elif application == "AlarmPlatform":
        run_flag = alarm_actions(func, param)
    else:
        raise Exception("非法的application名称: {}".format(application))

    return run_flag
