# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/2/12 上午9:58

import re


class Global:

    def __init__(self):
        self.service = {}
        self.db = {}
        self.mongo = {}
        self.login = {}
        self.schema = {}
        self.temp = {}
        self.case = {}
        self.global_id = None

        self.service = GlobalSubSet(self.service)
        self.db = GlobalSubSet(self.db)
        self.mongo = GlobalSubSet(self.mongo)
        self.login = GlobalSubSet(self.login)
        self.schema = GlobalSubSet(self.schema)
        self.temp = GlobalSubSet(self.temp)
        self.case = GlobalSubSet(self.case)

    def set_id(self, value):
        if isinstance(value, str):
            tmp1 = value.split("_")  # 将变量以_分割
            tmp2 = ""
            for i in tmp1:
                # 将分割后首字母转成大写，特殊：id转成ID
                if i == "id":
                    tmp2 += "ID"
                else:
                    tmp2 += i[0].upper() + i[1:].lower()
            self.global_id = tmp2
        else:
            raise KeyError("global_id只支持字符串")

    def replace(self, obj):
        obj = self.service.replace(obj)
        obj = self.temp.replace(obj)
        return obj


class GlobalSubSet(dict):

    def __init__(self, subset):
        self.global_set = subset

    def set(self, key, value):
        """
        :param key: 变量名
        :param value: 变量值
        :return: 无返回值，会更新原对象
        """
        self.global_set.update({key: value})
        self.update(self.global_set)

    def empty(self):
        """
        # 在每条测试用例执行之前，清空过程变量，即temp
        :return:
        """
        self.global_set.clear()
        self.update(self.global_set)

    def get(self, var_name):
        """
        :param var_name: 根据变量名，返回变量值
        :return:
        """
        return self.global_set.get(var_name)

    def get_names(self):
        """
        :return: 返回所有变量名list
        """
        var_names = []
        for key in self.global_set:
            var_names.append(key)
        return var_names

    def replace(self, obj):
        """
        使用全局变量的value，替换${xxx}这样的内容
        :param obj: 待替换的内容
        :return:
        """
        for var in self.get_names():
            patt = r'\$\{%s\}' % var
            if re.search(patt, obj):
                if isinstance(self.get(var), int):
                    value = str(self.get(var))
                else:
                    value = self.get(var)
                if not value:
                    break
                    # raise AttributeError("无法替换变量【{}】".format(var))
                if value.find("\\") > -1:  # 新增
                    data = value.replace("\\", "\\\\")
                else:
                    data = value
                obj = re.sub(r'\$\{%s\}' % var, data, obj)
        return obj


gbl = Global()
