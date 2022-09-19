# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021-05-07 14:17

import sys
import re
import json


def get_fline():

    a = "login_username"
    b = "login_passsword"

    print(sys._getframe().f_lineno)


def json_to_list(j):
    print("Receive: {}".format(j))
    print(type(j))
    tmp = json.loads(j)
    print("To: {}".format(tmp))
    print(type(tmp))


def rank():
    a = 'test_1_login'
    b = 'test_shop'
    c = 'test_10_exit'
    d = 'test_2_enter'
    patt = r'test_(\d{0,3})_.+'

    def get_rank(x):
        match_x = re.match(patt, x)
        if match_x:
            return match_x.group(1)
        else:
            return 0

    print(get_rank(a))
    print(get_rank(b))
    print(get_rank(c))
    print(get_rank(d))


if __name__ == "__main__":
    j = '[["name","小明"],["age","11"],["addr","广州市"]]'
    json_to_list(j)
    get_fline()
    rank()
