# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/6/22 上午10:44


def checkColTypeDate(col):
    """
    # 判断当前字段是否时间字段
    # create_time: True
    # create_date: True
    # try_time: False
    # cmd_timeout: False
    :return: True/False
    """
    col = str(col.upper())
    if col[-5:] == "_TIME" or col[-5:] == "_TIME":
        if col.find("CREATE") > -1 or col.find("UPDATE") > -1 or col.find("MODIFY") > -1:
            # create_time/create_date
            date_type = True
        else:
            # try_time/wait_time/sleep_time
            date_type = False
    else:
        # cmd_timeout
        date_type = False
    return date_type


if __name__ == "__main__":
    col_name = "try_time"
    print(checkColTypeDate(col_name))
