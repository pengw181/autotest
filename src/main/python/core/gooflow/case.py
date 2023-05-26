# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午4:12

import traceback
from src.main.python.lib.globals import gbl
from src.main.python.lib.generateUUID import getUUID
from src.main.python.core.gooflow.precondition import preconditions
from src.main.python.core.gooflow.operation import basic_run
from src.main.python.core.gooflow.compares import compare_data
from src.main.python.conf.config import global_config
from src.main.python.core.gooflow.initiation import initiation_work


class CaseWorker:

    @staticmethod
    def init():
        """
        业务参数初始化
        """
        global_config()
        # 生成文件夹uuid，用于保存截图
        gbl.service.set("FolderID", getUUID())
        if not gbl.service.get("ServerInit"):
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
            result = basic_run(step=step)
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
            result = compare_data(items)
        except Exception:
            result = False
            traceback.print_exc()
        return result
