# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/7 下午2:30

from common.variable.globalVariable import *


class BasePage:

    def __init__(self):
        self.browser = get_global_var("browser")