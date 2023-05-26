# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/2/14 下午5:07

import inspect
import ctypes
import threading
from src.main.python.lib.logger import log


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    main_pid = threading.main_thread().ident
    log.info("主线程: {}".format(main_pid))
    pid = thread.ident
    log.info("关闭线程: {}".format(pid))
    _async_raise(thread.ident, SystemExit)
