# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/5/15 上午11:00

from src.main.python.lib.globals import gbl


def sort_case(case_path, top_level_dir):
    """根据yaml配置文件，确定case加载顺序"""
    dir_name = top_level_dir.split('/')[-1]
    cur_case_names = gbl.case.get("case").get(dir_name)
    if cur_case_names is None:
        return case_path
    _temp_path = case_path
    case_path = []
    for p in cur_case_names:
        if p in _temp_path:
            case_path.append(p)
    return case_path
