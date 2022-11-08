# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/1/20 下午2:39


def transferAppName(num):
    app_map = {
        "1": "AiSee",
        "2": "VisualModeler",
        "3": "Crawler",
        "4": "AlarmPlatform"
    }
    result = app_map.get(num)
    if result:
        return result
    else:
        raise KeyError("当前类型【{0}】未加入到应用映射表".format(num))
