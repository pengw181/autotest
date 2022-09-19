# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/30 上午10:04

from config.loads import properties


def get_schema(schema):
    if properties.get("environment") == "v3.maria":
        # 9100
        schema_map = {
            "main": "aisee1",
            "sso": "sso",
            "nu": "nu",
            "dashboard": "dashboard"
        }
    elif properties.get("environment") == "gmcc.oracle":
        # 9990
        schema_map = {
            "main": "gd_gz",
            "sso": "sso",
            "nu": "nu",
            "dashboard": "dashboard"
        }
    elif properties.get("environment") == "v31.postgres":
        # 9990
        schema_map = {
            "main": "aisee1",
            "sso": "sso",
            "alarm": "alarm",
            "dashboard": "dashboard"
        }
    else:
        # 默认
        schema_map = {
            "main": "aisee1",
            "sso": "sso",
            "nu": "nu",
            "alarm": "alarm",
            "dashboard": "dashboard"
        }

    return schema_map.get(schema)
