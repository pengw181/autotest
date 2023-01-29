# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午3:37

import jsonpath
import json
from service.lib.database.SQLHelper import SQLUtil
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log


class ProcessNodeJson:

    def __init__(self, process_name):
        self.sql = "select json from tn_process_conf_info t where t.PROCESS_NAME='{0}'".format(process_name)
        sql_util = SQLUtil(db=get_global_var("Database"), schema="main")
        result = sql_util.select(self.sql)
        self.result_json = json.dumps(json.loads(result), indent=4, ensure_ascii=False)
        log.debug(self.result_json)
        self.result_json = json.loads(result)
        self.process_name = process_name
        self.node_num = 0
        self.node_dict = {}
        self.nodes = jsonpath.jsonpath(self.result_json, "$.nodes")[0]
        log.info("json结果: \n{0}".format(self.result_json))

    def reload(self):
        sql_util = SQLUtil(db=get_global_var("Database"), schema="main")
        result = sql_util.select(self.sql)
        self.result_json = json.loads(result)
        self.nodes = jsonpath.jsonpath(self.result_json, "$.nodes")[0]

    def count_node(self):
        # 统计当前流程的节点数
        self.node_num = len(list(self.nodes.keys()))
        log.info("当前流程节点数为{0}".format(self.node_num))
        return self.node_num

    def get_node_attribute(self, node_id, attribute):
        # 获取指定节点的某个属性值
        attributes = jsonpath.jsonpath(self.result_json, "nodes.{0}.{1}".format(node_id, attribute))[0]
        return attributes

    def get_attributes(self, attribute):
        # 获取指定属性值集合
        attributes = jsonpath.jsonpath(self.result_json, "nodes..{0}".format(attribute))
        log.info("属性{0}值为{1}".format(attribute, attributes))
        return attributes

    def get_node_ids(self):
        # 获取节点id集合
        node_list = list(self.nodes.keys())
        return node_list

    def bind_node_id_name(self):
        """
        :return: 节点ID和节点名称的dict
        """
        # 得到节点id集合
        node_list = self.get_node_ids()

        # 获取节点id和节点名称
        for node_id in node_list:
            self.node_dict[node_id] = jsonpath.jsonpath(self.result_json, "$.nodes.{0}.name".format(node_id))[0]
        log.info("当前流程节点: {0}".format(self.node_dict))
        return self.node_dict

    def get_line_location(self, source_node_name, target_node_name):
        """
        :param source_node_name: 节点名称，需要唯一
        :param target_node_name: 节点名称，需要唯一
        :return: 输出节点连线的左边坐标和右边坐标
        """

        source_left = 0
        source_width = 0
        source_top = 0
        source_height = 0
        target_left = 0
        target_width = 0
        target_top = 0
        target_height = 0
        # 连线类型，1、2、3，默认为3，如果目标节点在源节点左下方，返回类型2
        line_type = 3

        node_dict = self.bind_node_id_name()
        for key, value in node_dict.items():
            if value == source_node_name:
                source_left = int(self.get_node_attribute(node_id=key, attribute="left"))
                source_width = int(self.get_node_attribute(node_id=key, attribute="width"))

                source_top = int(self.get_node_attribute(node_id=key, attribute="top"))
                source_height = int(self.get_node_attribute(node_id=key, attribute="height"))

                # log.info("source_node_name : {0}".format(source_node_name))
                # log.info("source_left : {0}".format(source_left))
                # log.info("source_width : {0}".format(source_width))
                # log.info("source_top : {0}".format(source_top))
                # log.info("source_height : {0}".format(source_height))

                break
            else:
                continue

        for key, value in node_dict.items():
            if value == target_node_name:
                target_left = int(self.get_node_attribute(node_id=key, attribute="left"))
                target_width = int(self.get_node_attribute(node_id=key, attribute="width"))

                target_top = int(self.get_node_attribute(node_id=key, attribute="top"))
                target_height = int(self.get_node_attribute(node_id=key, attribute="height"))

                # log.info("target_node_name : {0}".format(target_node_name))
                # log.info("target_left : {0}".format(target_left))
                # log.info("target_width : {0}".format(target_width))
                # log.info("target_top : {0}".format(target_top))
                # log.info("target_height : {0}".format(target_height))

                break
            else:
                continue

        # 根据位置确定坐标，目前只支持从前往后连（节点从左至右 从上至下）
        if target_left > source_left:
            # 目标节点在源节点的右侧，会从源节点的右侧连到目标节点，通用
            from_x = source_left + source_width
            to_x = target_left

            h1 = source_top + source_height // 2
            h2 = target_top + target_height // 2
            if source_node_name == "开始":
                from_y = h1
            else:
                if h1 <= h2:
                    from_y_value = h1
                else:
                    from_y_value = h2
                from_y = from_y_value
            to_y = from_y
        elif target_left == source_left:
            # 目标节点与源节点在同一x轴上，可能宽度不同,以宽度小的节点取宽度/2
            if source_width >= target_width:
                from_x = source_left + target_width // 2
            else:
                from_x = source_left + source_width // 2
            to_x = from_x
            from_y = source_top + source_height
            to_y = target_top
        else:
            # 目标节点在源节点左侧，就会在源节点下方
            from_x = source_left
            to_x = target_left + target_width
            from_y = source_top + source_height
            to_y = target_top
            line_type = 2

        log.info("节点: {0} 至节点: {1}".format(source_node_name, target_node_name))
        from_location = "{0},{1}".format(from_x, from_y)
        to_location = "{0},{1}".format(to_x, to_y)
        log.info(from_location)
        log.info(to_location)

        return from_location, to_location, line_type

    def get_last_node_location(self):
        nodes = self.get_node_ids()
        x = 0
        y = 0
        if len(nodes) == 1:
            # 只有一个开始节点
            last_node_left = jsonpath.jsonpath(self.result_json, "$.nodes.{0}.left".format(nodes[0]))[0]
            last_node_top = jsonpath.jsonpath(self.result_json, "$.nodes.{0}.top".format(nodes[0]))[0]
            x = last_node_left + 12
            y = last_node_top + 12
        else:
            nodes_dict = self.node_dict
            for i in nodes:
                # log.info(i)
                if nodes_dict[i] == "开始":
                    pass
                else:
                    last_node_left = jsonpath.jsonpath(self.result_json, "$.nodes.{0}.left".format(i))[0]
                    last_node_top = jsonpath.jsonpath(self.result_json, "$.nodes.{0}.top".format(i))[0]
                    # log.info(last_node_left)
                    # log.info(last_node_top)
                    # log.info(x)
                    # log.info(y)
                    if last_node_top > y:
                        # 如果当前节点的top最大，则当作最后一个节点
                        x = last_node_left
                        y = last_node_top
                    elif last_node_top == y:
                        # 如果有多个节点的top值相同，取left最大的
                        if last_node_left > x:
                            x = last_node_left
                            y = last_node_top
                    log.info("节点id: %s, x = %d, y = %d" % (i, x, y))
            x += 12
            y += 12
        log.info("%d, %d" % (x, y))
        return x, y

    def get_last_node_name(self):
        _top = 0
        _left = 0
        last_node_id = None
        for node_id, node_info in self.nodes.items():
            node_top = node_info.get("top")
            node_left = node_info.get("left")
            if node_top > _top:     # 在下方
                last_node_id = node_id
                _top = self.get_node_attribute(last_node_id, "top")
                _left = self.get_node_attribute(last_node_id, "left")
            elif node_top == _top:      # 相同行
                if node_left > _left:       # 在右边
                    last_node_id = node_id
                    _top = self.get_node_attribute(last_node_id, "top")
                    _left = self.get_node_attribute(last_node_id, "left")
                else:
                    continue
            else:
                continue
        if last_node_id:
            return self.get_node_attribute(last_node_id, "name")
        else:
            raise Exception("数据异常")


if __name__ == "__main__":
    set_global_var("Database", 'v31.maria')
    p = ProcessNodeJson("pw自动化测试全流程")
    log.info(p.nodes)
    log.info(p.count_node())
    log.info(p.get_node_ids())
    log.info(p.get_last_node_name())
