# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:15

from datetime import datetime
from service.lib.database.sqlFormat import get_sql
from service.lib.database.SQLHelper import SQLUtil
from service.lib.variable.globalVariable import *
from service.lib.log.logger import log
from config.loads import properties, db_config


def check_db_data(db, schema, table_name, data, count):

    # 定义返回结果集
    rat = {
        "status": False,
        "data": ""
    }
    need_set_global = False

    # 如果匹配数据末尾有FetchID|script_id，则表示要获取script_id字段，并存入全局变量中，变量名ScriptID，用${ScriptID}来使用变量值
    if data.find("FetchID") > -1:
        need_set_global = True

    data_temp = data
    # 对于字段是json，值里面带有双引号，需要先用\转义
    data = data.replace("\\", "\\\\")   # 新增
    data = data.replace('"', '\\"')
    data = data.replace("'", "\\'")

    db_info = db_config.get(db)
    database_type = db_info.get("type")
    result = get_sql(database_type, data, table_name)
    sql = result.get("sql")
    column = result.get("column")
    log.info("原始sql: {}".format(sql))
    sql_util = SQLUtil(db=db, schema=schema)
    sql_result = sql_util.select(sql)

    last_match_column = ""
    if int(count) == sql_util.result_rows:
        log.info("数据结果匹配成功")
        if need_set_global:
            set_global_var(get_global_id(), str(sql_result[0][-1]), False)
            log.info("设置globalId: {0}，值为: {1}".format(get_global_id(), str(sql_result[0][-1])))
        rat["status"] = True
    else:
        """
        # 数据匹配不成功，将匹配不到的数据打印出来，用于查看具体不匹配字段。
        # 使用第一个字段值来查询，所以务必保证第一个字段值能找到数据。如果按第一个字段值查到多条，循环每一行进行比对；如果查不到，则结束比对。

        """
        search_item = data_temp.split("|", 2)
        search_col = search_item[0]
        search_value = search_item[1]
        log.info("数据库表比对失败，开始找出差异字段....")
        if search_value.lower().startswith("contains"):
            s = search_value[9: len(search_value) - 1]
            item = s.split("&&&")
            where_tmp = "1 = 1"
            for k in item:
                where_tmp += " and {0} like '%{1}%'".format(search_col, k.strip())
            sql = "select {0} from {1} where {2}".format(column, table_name, where_tmp)
        else:
            if search_value == "now":
                if database_type in ["oracle", "postgres"]:
                    search_col = "to_char({}, 'yyyymmddhh24miss')".format(search_col)
                sql = "select {0} from {1} where {2} between '{3}' and '{4}'".format(
                    column, table_name, search_col, get_global_var("StartTime"), get_global_var("EndTime"))
            elif search_value.lower() == "null":
                sql = "select {0} from {1} where {2} is None".format(column, table_name, search_col)
            else:
                sql = "select {0} from {1} where {2} = '{3}'".format(column, table_name, search_col, search_value)

        # 从原比对数据中找到一个排序字段
        order_by_column = None
        tmp1 = data_temp.split("|")
        for c in range(len(tmp1)):
            if tmp1[c].lower() == "now":
                order_by_column = tmp1[c - 1]
                break
        if order_by_column:
            sql += " order by {} desc".format(order_by_column)
        log.info("根据第一个字段查询sql: {0}".format(sql))
        sql_util = SQLUtil(db=db, schema=schema)
        sql_result = sql_util.select(sql)
        result_rows = sql_util.result_rows
        log.info("表里找到{0}条匹配数据".format(result_rows))
        max_num = int(properties.get("maxMatchNumWhenRetry"))
        if result_rows > max_num:
            sql_result = sql_result[:max_num][:]
            log.info("使用前{}条数据进行比对".format(max_num))
            log.info(sql_result)

        finish_flag = False
        if result_rows == 0:
            last_match_column = search_col
            log.info("根据 {0} = '{1}' 无法找到合适数据，匹配失败，请检查数据！".format(search_col, search_value))
            finish_flag = False
        else:
            num = 1
            failed_match_column = None
            for record in sql_result:

                check_list = []
                check_flag = True
                log.info("第{0}次比对".format(num))
                log.info("实际数据: {0}".format(record))
                tmp = data_temp.split("|")

                # 将预期结果字段重新调整
                for i in range(len(tmp))[::2]:
                    if tmp[i + 1] == "now":
                        value = "{0} 至 {1}".format(get_global_var("StartTime"), get_global_var("EndTime"))
                    elif tmp[i + 1].lower() == "null":
                        value = "None"
                    else:
                        if database_type == "postgres":
                            # postgres对于反斜杠转义默认关闭，不支持，只能使用单引号转义
                            # tmp[i + 1] = tmp[i + 1].replace("'", "''")
                            # value = tmp[i + 1]
                            # # 去掉转义符\
                            # value = value.replace(r"\'", "'")
                            # value = value.replace(r'\"', '"')
                            if tmp[i + 1].find("\\") > -1:
                                value = "E'{}'".format(tmp[i + 1])
                            else:
                                value = tmp[i + 1]
                        else:
                            value = tmp[i + 1]
                    check_list.append(value)
                log.info("比对数据: {0}".format(check_list))
                column_name = column.split(", ")

                # 开始逐字段匹配
                for i in range(len(record)):
                    # log.info("check_list[i]：{}".format(check_list[i]))
                    # log.info("GlobalId：{}".format(get_global_id()))
                    if check_list[i] == get_global_id():
                        # log.info("GlobalId字段【{}】不用匹配".format(get_global_id()))
                        pass
                    else:
                        if check_list[i].find("至") > -1:  # 时间比较
                            patt = r"(.+)\s至\s+(.+)"
                            match = re.match(patt, check_list[i])
                            # log.info(match.group())
                            begin = match.group(1)
                            end = match.group(2)
                            record_time = record[i]
                            if database_type in ["mysql"]:
                                record_time = datetime.strptime(record_time, '%Y-%m-%d %H:%M:%S')
                            record_time = datetime.strftime(record_time, '%Y%m%d%H%M%S')
                            if begin > record_time or record_time > end:
                                log.info("列名：{0}".format(column_name[i]))
                                log.info("实际：{0}".format(record_time))
                                log.info("预期：{0}, {1}".format(begin, end))
                                last_match_column = column_name[i]
                                check_flag = False
                                break
                        elif check_list[i] == "None":
                            if record[i] is not None:
                                log.info("列名：{0}".format(column_name[i]))
                                log.info("实际：{0}".format(record[i]))
                                log.info("预期：{0}".format(check_list[i]))
                                last_match_column = column_name[i]
                                check_flag = False
                                break
                        elif check_list[i].lower() == "notnull":
                            if record[i] is None:
                                log.info("列名：{0}".format(column_name[i]))
                                log.info("实际：{0}".format(record[i]))
                                log.info("预期：{0}".format(check_list[i]))
                                last_match_column = column_name[i]
                                check_flag = False
                                break
                        elif check_list[i].lower().startswith("contains"):
                            s = check_list[i][9: len(check_list[i]) - 1]
                            item = s.split("&&&")
                            for k in item:
                                if str(record[i]).find(k.strip()) == -1:
                                    log.info("列名：{0}".format(column_name[i]))
                                    log.info("实际：{0}".format(record[i]))
                                    log.info("预期：{0}".format(k.strip()))
                                    last_match_column = column_name[i]
                                    check_flag = False
                                    break
                                else:
                                    continue
                            if not check_flag:
                                break
                        else:
                            check_tmp = check_list[i]
                            check_list[i] = check_tmp.replace('”', '"')
                            # check_list[i] = check_list[i].replace("''", "'")
                            # if database_type in ["oracle"]:
                            #     if check_list[i] == "":
                            #         check_list[i] = None
                            if str(record[i]) != check_list[i]:
                                log.info("列名：{0}".format(column_name[i]))
                                log.info("实际：{0}".format(record[i]))
                                log.info("预期：{0}".format(check_list[i]))
                                last_match_column = column_name[i]
                                check_flag = False
                                break
                if check_flag:
                    log.info("数据比对成功！")
                    last_match_column = ""
                    finish_flag = True
                    break
                else:
                    log.info("{}比对不通过".format(last_match_column))
                    if num == 1:
                        failed_match_column = last_match_column
                    num += 1      # 如果不继续匹配，则跳出循环
                    # break
                if failed_match_column:
                    last_match_column = failed_match_column
        if not finish_flag:
            rat["status"] = False
            rat["data"] = last_match_column
        else:
            rat["status"] = True
            rat["data"] = ""
    return rat


def check_msg(msg):
    # 将操作后得到的弹出框或其他返回信息，用set_global_var存起来，用于compare里信息比较
    if isinstance(msg, str):
        return get_global_var("ResultMsg").find(msg) > -1
    else:
        log.error("匹配信息不是字符串，无法匹配")
        return False
