# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:22

from src.main.python.lib.globals import gbl
from src.main.python.db.colTypeDate import checkColTypeDate
from src.main.python.db.SQLHelper import SQLUtil


def get_sql(database_type, source_data, table_name, schema):
    """
    :param database_type: 数据库类型
    :param source_data: 原始数据
    :param table_name: 表名
    :param schema: schema
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
            if checkColTypeDate(table_name, schema, data[i]):
                if database_type == "mysql":
                    tmp = "CAST({0} AS CHAR) AS {0}".format(data[i], data[i])
                else:
                    tmp = data[i]
            else:
                tmp = data[i]
            column = tmp
            first_add_column_flag = False
        else:
            if checkColTypeDate(table_name, schema, data[i]):
                if database_type == "mysql":
                    tmp = "CAST({0} AS CHAR) AS {0}".format(data[i], data[i])
                else:
                    tmp = data[i]
                column = column + ', ' + tmp
            else:
                if data[i] == "FetchID":        # FetchID|script_id
                    fetch = data[i+1]
                    gbl.set_id(data[i+1])
                else:
                    tmp = data[i]
                    column = column + ', ' + tmp

        # 组装where条件
        if data[i] == "FetchID":       # 获取FetchID对应列名的值，一般为id，这一对不组装到sql中
            pass
        else:
            ######## 数据库特殊处理开始 ########
            if gbl.temp.get("UpperOrLower") == "upper":
                upper_col_list = ["time_field", "field_chinese_name", "field_english_name", "field_english_nick_name"]
                if data[i].lower() in upper_col_list:
                    # 告警平台元数据比对特殊处理
                    data[i+1] = data[i+1].upper()

            # 根据数据库类型替换TimeDataType
            database_type = gbl.service.get("DatabaseType")
            if database_type in ["mysql"]:
                # mysql的日期自动转成DATETIME
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "DATETIME"
            elif database_type in ["postgres"]:
                # postgres的日期自动转成DATETIME
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "TIMESTAMP"
            elif database_type in ["oracle"]:
                # oracle的日期自动转成DATE
                if data[i + 1] == "${TimeDataType}":
                    data[i + 1] = "DATE"

            # 根据数据库类型替换StrDataType
            if database_type == "oracle":
                # oracle 将varchar转成varchar2
                if data[i + 1] == "${StrDataType}":
                    data[i + 1] = "VARCHAR2"
            else:
                if data[i + 1] == "${StrDataType}":
                    data[i + 1] = "VARCHAR"

            if database_type == "oracle":
                if gbl.service.get("ClobCol") is None:
                    gbl.service.set("ClobCol", [])
                if gbl.service.get("ClobTableName") is None:
                    gbl.service.set("ClobTableName", [])
                if table_name.upper() not in gbl.service.get("ClobTableName"):
                    find_lob_sql = """select lower(column_name) 
                                      from user_tab_columns 
                                      where table_name = upper('{}')
                                      AND data_type = upper('clob')""".format(table_name)
                    sql_util = SQLUtil(db=gbl.service.get("Database"), schema=schema)
                    sql_result = sql_util.select(find_lob_sql)
                    if isinstance(sql_result, str):
                        gbl.service.get("ClobCol").append(sql_result)
                    elif isinstance(sql_result, list):
                        sql_result = [t[0] for t in sql_result]
                        gbl.service.get("ClobCol").extend(sql_result)

                    # clob_col_list = ['result_sample', 'request_body', 'design_content', 'click_elem_json', 'var_json',
                    #             'json', 'param_cfg', 'param_cfg', 'file_oprt_cfg', 'regx_expr', 'sql_cfg', 'attach_cfg',
                    #             'oprt_cfg', 'config', 'attach_content', 'loop_cnd', 'logic_cnd']
                    gbl.service["ClobTableName"].append(table_name.upper())
            ######## 数据库特殊处理结束 ########

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
                        data[i], gbl.temp.get("StartTime"), gbl.temp.get("EndTime"))
                else:
                    where_condition += " and {0} between '{1}' and '{2}'".format(
                        data[i], gbl.temp.get("StartTime"), gbl.temp.get("EndTime"))
            elif data[i+1].lower().startswith("contains"):
                # 包含
                s = data[i+1][9: len(data[i+1])-1]
                item = s.split("&&&")

                for k in item:
                    if database_type == "oracle":
                        # 去掉转义符\
                        clob_col_value = k.strip().replace(r"\'", "'").replace(r'\"', '"')
                        if data[i].lower() in gbl.service.get("ClobCol"):
                            # oracle clob字段匹配处理
                            where_condition += " and dbms_lob.instr({0}, '{1}')>0".format(data[i], clob_col_value)
                            continue
                    where_condition += " and {0} like '%{1}%'".format(data[i], k.strip())

            else:
                # 具体值匹配
                value4key = data[i + 1]
                if checkColTypeDate(table_name, schema, data[i]):
                    # 日期字段填写具体值时，做日期转换
                    if database_type in ["mysql"]:
                        where_condition += " and {0} = date_format('{1}', 'yyyy-mm-dd hh24:mi:ss')".format(
                            data[i], value4key)
                    else:
                        where_condition += " and {0} = to_date('{1}', 'yyyy-mm-dd hh24:mi:ss')".format(
                            data[i], value4key)
                else:
                    # 常用字段匹配
                    if database_type == "postgres":
                        # # postgres对于反斜杠转义默认关闭，不支持，只能使用单引号转义
                        # value4key = value4key.replace("'", "''")
                        # where_condition += " and {0} = '{1}'".format(data[i], value4key)
                        # # 去掉转义符\
                        # where_condition = where_condition.replace(r"\'", "'")
                        # where_condition = where_condition.replace(r'\"', '"')

                        # postgres转义
                        if value4key.find("\\") > -1:
                            where_condition += " and {0} = E'{1}'".format(data[i], value4key)
                        else:
                            where_condition += " and {0} = '{1}'".format(data[i], value4key)

                    elif database_type == "oracle":
                        # oracle特殊处理

                        if value4key == "":
                            # 空匹配
                            where_condition += " and {0} is Null".format(data[i])
                        else:
                            if data[i].lower() in gbl.service.get("ClobCol"):
                                # oracle clob字段匹配处理

                                # 去掉转义符\
                                clob_col_value = value4key.replace(r"\'", "'").replace(r'\"', '"').replace("\\\\", "\\").replace("'", "''")

                                if clob_col_value.find("~") > -1:
                                    # 替换～成换行
                                    clob_col_value_temp = clob_col_value.split("~")
                                    clob_col_value = "'||chr(13)||chr(10)||'".join(clob_col_value_temp)
                                    where_condition += " and dbms_lob.instr({0}, '{1}')>0".format(data[i], clob_col_value)
                                else:
                                    where_condition += " and dbms_lob.instr({0}, '{1}')>0".format(data[i], clob_col_value)
                                value4key = clob_col_value
                            else:
                                if value4key.find("~") > -1:
                                    # 替换～成换行
                                    value_temp = value4key.split("~")
                                    value_temp = "'||chr(13)||chr(10)||'".join(value_temp)
                                    where_condition += " and {0} = '{1}'".format(data[i], value_temp)
                                    value4key = value_temp
                                else:
                                    where_condition += " and {0} = '{1}'".format(data[i], value4key.replace("\\'", "''"))
                    else:
                        where_condition += " and {0} = '{1}'".format(data[i], value4key)

                    if value4key.find("~") > -1:
                        # 替换～成换行
                        value_temp = value4key.split("~")
                        value_temp = "'||chr(13)||chr(10)||'".join(value_temp)
                        where_condition += " and {0} = '{1}'".format(data[i], value_temp)

                    # if value4key.find("\\'") > -1:
                    #     # 匹配值中仅存在单引号
                    #     print(value4key)
                    #     value_temp = value4key.replace("\\", "")
                    #     print(value_temp)
                    #     where_condition += ' and {0} = "{1}"'.format(data[i], value_temp)
                    # else:
                    #     where_condition += " and {0} = '{1}'".format(data[i], value4key)

    # 将FetchID对应列放在最后，便于数组取值
    if fetch:
        column = column + ', ' + fetch
    sql = "select {0} from {1} where {2}".format(column, table_name, where_condition)
    result = {
        "column": column,
        "sql": sql
    }

    return result
