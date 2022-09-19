# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/9 上午11:19


def getImageType(image_type_name):
    image_map = {
        "柱状图": "bar",
        "折线图": "line",
        "饼状图": "pie",
        "仪表图": "gauge",
        "雷达图": "radar",
        "数据表格": "table",
        "地图": "map",
        "文本块": "text",
        "散点图": "scatter",
        "矩形树图": "treeMap",
        "iframe块": "iframe"
    }
    return image_map.get(image_type_name)
