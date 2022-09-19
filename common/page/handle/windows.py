# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:55

from selenium.common.exceptions import NoSuchWindowException
from common.variable.globalVariable import *
from common.log.logger import log


class WindowHandles:

    def __init__(self):
        self.browser = get_global_var("browser")
        self.win_handles = get_global_var("WinHandles")
        if self.win_handles is None:
            self.win_handles = {}
        # log.info("当前保存窗口信息:{0}".format(self.win_handles))

    def save(self, title):
        current_win = self.browser.current_window_handle
        # log.info("窗口信息：{}".format(self.browser.window_handles))

        # 如果当前打开的窗口只有1个，首次保存
        if len(self.browser.window_handles) == 1:
            self.win_handles[title] = self.browser.window_handles[0]
            set_global_var("WinHandles", self.win_handles)
            log.info("保存首个窗口句柄 %s:%s" % (title, self.browser.window_handles[0]))
        else:
            for handle in self.browser.window_handles:
                # log.info(handle)
                # log.info(current_win)
                # log.info(list(self.win_handles.values()))
                # 如果当前窗口未保存在WinHandles中，则保存
                if current_win != handle and handle not in list(self.win_handles.values()):
                    self.win_handles[title] = handle
                    set_global_var("WinHandles", self.win_handles)
                    log.info("保存新的窗口句柄 %s:%s" % (title, handle))
        log.info("当前窗口信息:{0}".format(get_global_var("WinHandles")))

    def switch(self, title):
        window = self.win_handles.get(title)
        if window:
            window = str(window)
            self.browser.switch_to.window(window)
            log.info("切换到标签页: {0}，{1}".format(title, window))
            # self.browser.switch_to.default_content()
        else:
            raise NoSuchWindowException("Window【{}】not found".format(title))

    def close(self, title):
        # 关闭指定窗口
        if self.win_handles.get(title):
            self.browser.switch_to.window(str(self.win_handles.get(title)))
            self.browser.close()
            self.win_handles.pop(title)
            set_global_var("WinHandles", self.win_handles)
            self.browser.switch_to.window(self.browser.window_handles[-1])
            log.info("窗口【{0}】已关闭.".format(title))
            log.info(get_global_var("WinHandles"))
            self.browser.refresh()
        else:
            log.info("窗口【{0}】不存在，无需关闭.".format(title))
