# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:25

import re
import json
from json.decoder import JSONDecodeError
from common.log.logger import log


def update_json(obj, new_dict):
    """
    :param obj: json对象
    :param new_dict: dict，要更新的内容
    :return: 返回替换后的完整json

    {
        "attach_content": {
            "ftp_server_cfg_id": "f01d8cda-e5ed-48cf-bd19-5116b9d6087a",
            "catalog_path": "/pw",
            "catalog_isKeyword": "0",
            "file": "",
            "fileType": "csv",
            "file_choose_type": "1",
            "file_regex_templ_id": "4771FAD2-BA97-4857-A72E-8EF3D912EC50",
            "file_regex_expr": "",
            "file_regex_json": ""
        },
        "attach_source": "4"
    }
    """
    try:
        json2dict = json.loads(obj)

        def round_dict(d):
            # log.info("d: {}".format(d))
            if isinstance(d, dict):
                for x in range(len(d)):
                    temp_key = list(d.keys())[x]
                    temp_value = d[temp_key]
                    # log.info("temp_key: {}".format(temp_key))
                    # log.info("temp_value: {}".format(temp_value))
                    if temp_key == list(new_dict.keys())[0]:
                        log.info("找到key：{}".format(temp_key))
                        d.update(new_dict)
                        break
                    else:
                        round_dict(temp_value)

        round_dict(json2dict)
        return json.dumps(json2dict)
    except JSONDecodeError as e:
        raise e


def update_dict(obj, key, value):

    # 定义输出结果，默认为初始值
    replace_result = obj

    if obj.__contains__(key):
        obj[key] = value
    else:
        # 遍历每个key对应的value，从value继续寻找key
        for _key, _value in obj.items():
            if type(_value).__name__ != "dict":
                pass
            else:
                # 循环调用自身
                update_dict(obj=_value, key=key, value=value)
    return replace_result


def update_dict_by_path(obj, path, value):
    """
    {
        "dataArr": [{
            "name": "日期",
            "color": "",
            "brackets_left": "",
            "brackets_right": "",
            "obj_id": "8C9B307E-15DE-4005-A0FB-199C609E1982",
            "label_id": "label_date",
            "main_value": "\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d",
            "main_len": "+",
            "value_type": "1",
            "expr": "\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d",
            "special": ".",
            "main_text": "2014-05-28 12:30:00"
        }],
        "isAdv": False,
        "expr_input": "",
        "sampleData": "",
        "matchResult": ""
    }

    {
        "dataArr": [{
            "name": "字母",
            "color": "green",
            "brackets_left": "(",
            "brackets_right": ")",
            "obj_id": "0F96CFCF-6C66-4630-810F-F65F68CC5E58",
            "label_id": "label_word",
            "main_value": "",
            "main_len": "+",
            "value_type": "1",
            "expr": "([a-zA-Z]+)",
            "special": ".",
            "main_text": "1到多个"
        }, {
            "name": "自定义文本",
            "color": "",
            "brackets_left": "",
            "brackets_right": "",
            "obj_id": "C6C96A5F-D27E-48AF-A2FF-B665ED298020",
            "label_id": "custom_text",
            "main_value": ":",
            "main_len": "+",
            "value_type": "1",
            "expr": ":",
            "special": ".",
            "main_text": ":"
        }, {
            "name": "字母",
            "color": "green",
            "brackets_left": "(",
            "brackets_right": ")",
            "obj_id": "A8120D18-F630-4E7D-8778-D88C774CDE62",
            "label_id": "label_word",
            "main_value": "",
            "main_len": "+",
            "value_type": "1",
            "expr": "([a-zA-Z]+)",
            "special": ".",
            "main_text": "1到多个"
        }],
        "isAdv": False,
        "expr_input": "",
        "sampleData": "",
        "matchResult": ""
    }
    """
    # obj转成dict
    if isinstance(obj, str):
        # 定义输出结果，默认为初始值
        str_obj = obj.replace("\\", "\\\\")
        json2dict = json.loads(str_obj)
    else:
        json2dict = obj
    sub_object = json2dict
    path_list = path.split(".")
    obj_attr = path_list[-1]
    path_list.pop(0)
    path_list.pop()
    if not isinstance(value, list):
        raise ValueError("替换值需要是数组")
    for p in path_list:
        if p.find("[") == -1:
            # 如果属性没有指定序号，如$.dataArr.obj_id，则替换dataArr下所有obj_id
            sub_object = sub_object[p]
            attr_obj_len = len(sub_object)
            value_len = len(value)
            if attr_obj_len != value_len:
                raise ValueError("替换值个数不匹配，期望{0}个，实际有{1}个".format(attr_obj_len, value_len))
            for i in range(attr_obj_len):
                sub_object[i].update({obj_attr: value[i]})
        else:
            patt = r'([a-zA_Z_]+)\[(\d+)\]'
            match_obj = re.match(patt, p)
            if not match_obj:
                raise KeyError("路径错误: {0}".find(path))
            attr = match_obj.group(1)
            index = match_obj.group(2)
            sub_object = sub_object[attr][int(index)]
            sub_object.update({obj_attr: value})
    log.info(json2dict)
    return json2dict


if __name__ == "__main__":
    a = {
        "dataArr": [{
            "name": "日期",
            "color": "",
            "brackets_left": "",
            "brackets_right": "",
            "obj_id": "8C9B307E-15DE-4005-A0FB-199C609E1982",
            "label_id": "label_date",
            "main_value": "\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d",
            "main_len": "+",
            "value_type": "1",
            "expr": "\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d",
            "special": ".",
            "main_text": "2014-05-28 12:30:00"
        }],
        "isAdv": False,
        "expr_input": "",
        "sampleData": "",
        "matchResult": ""
    }
    c = {
        "dataArr": [{
            "name": "字母",
            "color": "green",
            "brackets_left": "(",
            "brackets_right": ")",
            "obj_id": "0F96CFCF-6C66-4630-810F-F65F68CC5E58",
            "label_id": "label_word",
            "main_value": "",
            "main_len": "+",
            "value_type": "1",
            "expr": "([a-zA-Z]+)",
            "special": ".",
            "main_text": "1到多个"
        }, {
            "name": "自定义文本",
            "color": "",
            "brackets_left": "",
            "brackets_right": "",
            "obj_id": "C6C96A5F-D27E-48AF-A2FF-B665ED298020",
            "label_id": "custom_text",
            "main_value": ":",
            "main_len": "+",
            "value_type": "1",
            "expr": ":",
            "special": ".",
            "main_text": ":"
        }, {
            "name": "字母",
            "color": "green",
            "brackets_left": "(",
            "brackets_right": ")",
            "obj_id": "A8120D18-F630-4E7D-8778-D88C774CDE62",
            "label_id": "label_word",
            "main_value": "",
            "main_len": "+",
            "value_type": "1",
            "expr": "([a-zA-Z]+)",
            "special": ".",
            "main_text": "1到多个"
        }],
        "isAdv": False,
        "expr_input": "",
        "sampleData": "",
        "matchResult": ""
    }
    d = '{"dataArr":[{"name":"日期","color":"","brackets_left":"","brackets_right":"","obj_id":"8C9B307E-15DE-4005-A0FB-199C609E1982","label_id":"label_date","main_value":"\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d","main_len":"+","value_type":"1","expr":"\\d{4}-[01]\\d-[0-3]\\d\\s+[0-2]\\d:[0-5]\\d:[0-5]\\d","special":".","main_text":"2014-05-28 12:30:00"}],"isAdv":false,"expr_input":"","sampleData":"","matchResult":""}'
    log.info(d)
    # oid = ["6b7f063c-6d85-41ad-9add-4930120ac70b", "117f063c-6d85-41ad-9add-4930120ac70b", "227f063c-6d85-41ad-9add-4930120ac70b"]
    oid = ["6b7f063c-6d85-41ad-9add-4930120ac70b"]
    b = update_dict_by_path(d, "$.dataArr.obj_id", oid)
    # log.info(b)
    data = str(b)
    data = data.replace("'", "\"")
    data = data.replace(": ", ":")
    data = data.replace(", ", ",")
    data = data.replace("True", "true")
    data = data.replace("False", "false")
    log.info(data)
