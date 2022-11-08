# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午4:12

import traceback
from config.initiation import initiation_work
from service.lib.variable.globalVariable import *
from service.gooflow.precondition import preconditions
from service.gooflow.operations import basicRun
from service.gooflow.compares import compareData


class CaseWorker:

    @staticmethod
    def init():
        """
        业务参数初始化
        """
        if not get_global_var("ServerInit"):
            initiation_work()

    @staticmethod
    def pre(pres):
        """
        预置条件
        @param: pres: 文本，支持多行，以换行分割
        """
        # noinspection PyBroadException
        try:
            result = preconditions(action=pres)
        except Exception:
            result = False
            traceback.print_exc()
        return result

    @staticmethod
    def action(step):
        """
        用户操作，一次一个步骤
        """
        # noinspection PyBroadException
        try:
            result = basicRun(step=step)
        except Exception:
            result = False
            traceback.print_exc()
        return result

    @staticmethod
    def check(items):
        """
        结果匹配
        """
        # noinspection PyBroadException
        try:
            result = compareData(items)
        except Exception:
            result = False
            traceback.print_exc()
        return result
