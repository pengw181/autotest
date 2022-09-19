# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:27

import re

"""
# 变量集合定义3个分类，
test: 测试参数，比如用户名，领域，系统url等
service: 业务配置参数，业务用表名等，需要在测试之前构造数据
temp: 临时参数，数据匹配查寻结果存储用等，每条执行测试任务前，会清空临时参数
"""

global_set = {
    "test": {},
    "service": {},
    "temp": {}
}

globalId = ""


def init_global_var():
    global global_set
    global_set["test"] = {}
    global_set["service"] = {}
    global_set["temp"] = {}


def set_global_var(key, value, fixed="test"):
    """
    将运行过程中需要的变量分别存入 global_set 的test、service或temp
    :param key: 变量名
    :param value: 变量值
    :param fixed: 是否固定参数，默认是，业务参数配置成service，测试参数配置成test，临时参数需设置为false，默认test，临时参数会自动清理
    :return:
    """
    global global_set
    test = global_set["test"]
    service = global_set["service"]
    temp = global_set["temp"]
    if fixed is False:
        if temp.__contains__(key):
            temp.pop(key)
        temp.update({key: value})
    elif fixed == "service":
        if service.__contains__(key):
            service.pop(key)
        service.update({key: value})
    else:
        if test.__contains__(key):
            test.pop(key)
        test.update({key: value})


def clear_process_var():
    """
    # 在每条测试用例执行之前，清空过程变量，即temp
    :return:
    """
    global global_set
    global_set["temp"] = {}


def get_global_var(var_name):
    """
    :param var_name: 根据变量名，返回变量值
    :return:
    """
    global global_set
    result = None
    if global_set.get("test").__contains__(var_name):
        result = global_set.get("test").get(var_name)
    elif global_set.get("service").__contains__(var_name):
        result = global_set.get("service").get(var_name)
    elif global_set.get("temp").__contains__(var_name):
        result = global_set.get("temp").get(var_name)
    if isinstance(result, int):
        result = str(result)
    return result


def get_global_var_names():
    """
    :return: 返回所有变量名list
    """
    global global_set
    var_names = []
    for key in global_set.get("test"):
        var_names.append(key)
    for key in global_set.get("service"):
        var_names.append(key)
    for key in global_set.get("temp"):
        var_names.append(key)
    return var_names


def set_global_id(value):
    global globalId
    if isinstance(value, str):
        tmp1 = value.split("_")     # 将变量以_分割
        tmp2 = ""
        for i in tmp1:
            # 将分割后首字母转成大写，特殊：id转成ID
            if i == "id":
                tmp2 += "ID"
            else:
                tmp2 += i[0].upper() + i[1:].lower()
        globalId = tmp2
    else:
        raise KeyError("globalId只支持字符串")


def replace_global_var(obj):
    """
    使用全局变量的value，替换${xxx}这样的内容
    :param obj: 待替换的内容
    :return:
    """
    global global_set
    for var in get_global_var_names():
        patt = r'\$\{%s\}' % var
        if re.search(patt, obj):
            if get_global_var(var).find("\\") > -1:     # 新增
                data = get_global_var(var).replace("\\", "\\\\")
            else:
                data = get_global_var(var)
            obj = re.sub(r'\$\{%s\}' % var, data, obj)
    return obj


def get_global_id():
    global globalId
    return globalId
