# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:18

from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def saveCode(msg):
    if msg:
        if gbl.temp.get("ErrorMsg") is None:
            gbl.temp.set("ErrorMsg", msg)
        else:
            msg = str(gbl.temp.get("ErrorMsg")) + '\n' + msg
            gbl.temp.set("ErrorMsg", msg)
        log.info(gbl.temp.get("ErrorMsg"))
    else:
        raise KeyError("msg不能为空")
