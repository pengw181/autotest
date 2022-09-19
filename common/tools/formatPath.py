# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/5/24 上午10:03


def struct_path(path):
    """
    ## 处理路径中的/../
    """

    if path.find("..") == -1:   # 找不到/..，返回原值
        str_path = path
    else:
        pos_dd = path.find("/..")
        if pos_dd == 0:    # /..在开始位置，不处理
            str_path = path
        else:
            # /home/user/log/../src/log/test/
            pos_ahead = path[:pos_dd].rfind("/")
            str_path = path[:pos_ahead] + path[pos_dd+3:]
            str_path = struct_path(str_path)
    return str_path


if __name__ == "__main__":
    path = '/home/user/log/../../src/logs/../test/'
    print(path)
    print(struct_path(path))