# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:22

from common.variable.globalVariable import *
from database.colTypeDate import checkColTypeDate


def get_sql(database_type, source_data, table_name):
    """
    :param database_type: 数据库类型
    :param source_data: 原始数据
    :param table_name: 表名
    """
    if database_type not in ['oracle']:
        source_data = source_data.replace("~", r"\r\n")
    data = source_data.split("|")
    column = ""
    fetch = False
    first_add_column_flag = True
    where_condition = "1 = 1"
    for i in range(len(data))[::2]:
        # 组装结果列
        if first_add_column_flag:
            if checkColTypeDate(data[i]):
                if database_type == "mysql":
                    tmp = "CAST({0} AS CHAR) AS {0}".format(data[i], data[i])
                else:
                    tmp = data[i]
            else:
                tmp = data[i]
            column = tmp
            first_add_column_flag = False
        else:
            if checkColTypeDate(data[i]):
                if database_type == "mysql":
                    tmp = "CAST({0} AS CHAR) AS {0}".format(data[i], data[i])
                else:
                    tmp = data[i]
                column = column + ', ' + tmp
            else:
                if data[i] == "FetchID":        # FetchID|script_id
                    fetch = data[i+1]
                    set_global_id(data[i+1])
                else:
                    tmp = data[i]
                    column = column + ', ' + tmp

        # 组装where条件
        if data[i] == "FetchID":       # 获取FetchID对应列名的值，一般为id，这一对不组装到sql中
            pass
        else:
            # 数据库特殊处理开始 #
            if get_global_var("UpperOrLower") == "upper":
                upper_col_list = ["time_field", "field_chinese_name", "field_english_name", "field_english_nick_name"]
                if data[i].lower() in upper_col_list:
                    # 告警平台元数据比对特殊处理
                    data[i+1] = data[i+1].upper()

            # 根据数据库类型替换TimeDataType
            if get_global_var("DatabaseType") in ["mysql"]:
                # mysql的日期自动转成DATETIME
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "DATETIME"
            elif get_global_var("DatabaseType") in ["postgres"]:
                # postgres的日期自动转成DATETIME
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "TIMESTAMP"
            elif get_global_var("DatabaseType") in ["oracle"]:
                # oracle的日期自动转成DATE
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "DATE"

            if get_global_var("DatabaseType") == "oracle":
                # oracle 将varchar转成varchar2
                if data[i + 1] == "${StrDataType}":
                    data[i + 1] = "VARCHAR2"

            # 数据库特殊处理结束 #

            if data[i+1].lower() == "null":
                # 对于空值处理
                where_condition += " and {0} is Null".format(data[i])
            elif data[i + 1].lower() == "notnull":
                # 非空模糊匹配
                where_condition += " and {0} is not Null".format(data[i])
            elif data[i+1].lower() == "now":
                # 表示是本次用例执行期间的时间，需要借助StartTime和EndTime区间来判断
                if database_type in ["oracle", "postgres"]:
                    where_condition += " and to_char({0}, 'yyyymmddhh24miss') between '{1}' and '{2}'".format(
                        data[i], get_global_var("StartTime"), get_global_var("EndTime"))
                else:
                    where_condition += " and {0} between '{1}' and '{2}'".format(
                        data[i], get_global_var("StartTime"), get_global_var("EndTime"))
            elif data[i+1].lower().startswith("contains"):
                # 包含
                s = data[i+1][9: len(data[i+1])-1]
                item = s.split("&&&")
                for k in item:
                    where_condition += " and {0} like '%{1}%'".format(data[i], k.strip())
            else:
                # 具体值匹配
                if checkColTypeDate(data[i]):
                    # 日期字段填写具体值时，做日期转换
                    if database_type in ["mysql"]:
                        where_condition += " and {0} = date_format('{1}', 'yyyy-mm-dd hh24:mi:ss')".format(
                            data[i], data[i + 1])
                    else:
                        where_condition += " and {0} = to_date('{1}', 'yyyy-mm-dd hh24:mi:ss')".format(
                            data[i], data[i + 1])
                else:
                    # 常用字段匹配
                    if database_type == "postgres":
                        # # postgres对于反斜杠转义默认关闭，不支持，只能使用单引号转义
                        # data[i + 1] = data[i + 1].replace("'", "''")
                        # where_condition += " and {0} = '{1}'".format(data[i], data[i+1])
                        # # 去掉转义符\
                        # where_condition = where_condition.replace(r"\'", "'")
                        # where_condition = where_condition.replace(r'\"', '"')

                        # postgres转义
                        if data[i + 1].find("\\") > -1:
                            where_condition += " and {0} = E'{1}'".format(data[i], data[i + 1])
                        else:
                            where_condition += " and {0} = '{1}'".format(data[i], data[i + 1])

                    if database_type == "oracle":
                        # oracle特殊处理
                        clob_col = ['result_sample', 'request_body', 'design_content']
                        if data[i+1] == "":
                            # 空匹配
                            where_condition += " and {0} is Null".format(data[i])

                        if data[i].lower() in clob_col:
                            # oracle clob字段匹配处理

                            # 去掉转义符\
                            clob_col_value = data[i + 1].replace(r"\'", "'")
                            clob_col_value = clob_col_value.replace(r'\"', '"')

                            if clob_col_value.find("~") > -1:
                                # 替换～成换行
                                clob_col_value_temp = clob_col_value.split("~")
                                clob_col_value = "'||chr(13)||chr(10)||'".join(clob_col_value_temp)
                                where_condition += " and dbms_lob.instr({0}, '{1}')>0".format(data[i], clob_col_value)
                            else:
                                where_condition += " and dbms_lob.instr({0}, '{1}')>0".format(data[i], clob_col_value)

                        else:
                            where_condition += " and {0} = '{1}'".format(data[i], data[i + 1])

                    if data[i + 1].find("~") > -1:
                        # 替换～成换行
                        value_temp = data[i + 1].split("~")
                        value_temp = "'||chr(13)||chr(10)||'".join(value_temp)
                        where_condition += " and {0} = '{1}'".format(data[i], value_temp)

                    # if data[i + 1].find("\\'") > -1:
                    #     # 匹配值中仅存在单引号
                    #     print(data[i + 1])
                    #     value_temp = data[i + 1].replace("\\", "")
                    #     print(value_temp)
                    #     where_condition += ' and {0} = "{1}"'.format(data[i], value_temp)
                    # else:
                    #     where_condition += " and {0} = '{1}'".format(data[i], data[i+1])

    # 将FetchID对应列放在最后，便于数组取值
    if fetch:
        column = column + ', ' + fetch
    sql = "select {0} from {1} where {2}".format(column, table_name, where_condition)
    result = {
        "column": column,
        "sql": sql
    }

    return result
