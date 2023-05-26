# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:37

import traceback
from time import sleep
from datetime import datetime
from src.main.python.db.SQLHelper import SQLUtil
from src.main.python.core.gooflow.codes import saveCode
from src.main.python.lib.globals import gbl
from src.main.python.lib.updateData import update_json
from src.main.python.lib.logger import log


def preconditions(action):
    """
    :param action: 可以设置全局变量，可以执行sql
    :return: 执行结果，true/false
    """

    # 多条sql语句按换行分隔
    if action.strip() == "":    # 预置条件为空
        run_flag = True
    else:
        pre_list = action.split(chr(10))
        run_flag = False

        # 去掉空行
        _tmp = []
        for one_pre in pre_list:
            one_pre = one_pre.strip()
            if one_pre != "":
                _tmp.append(one_pre)
        pre_list = _tmp

        # 预置条件不为空，拆成多条执行
        for i in range(len(pre_list)):
            one_pre = pre_list[i]
            # 替换${Database}变量
            one_pre = gbl.replace(one_pre)

            if one_pre.lower().startswith("global"):
                # 变量赋值，加入到global_set
                log.info("开始设置全局变量：{0}".format(one_pre))
                # noinspection PyBroadException
                try:
                    var_set = one_pre.split("|", 2)
                    gbl.temp.set(var_set[1].strip(), var_set[2].strip())
                    log.info("设置全局变量：{0}成功".format(var_set[1].strip()))
                    run_flag = True
                except Exception as e:
                    saveCode("设置全局变量异常: {0}".format(str(e)))
                    run_flag = False

            elif one_pre.lower().startswith("updatejson"):
                # 更新json字段的值
                # noinspection PyBroadException
                try:
                    each_pre = one_pre.split("|", 3)
                    json_obj = gbl.replace(each_pre[1])
                    key = each_pre[2]
                    value = each_pre[3]
                    log.info("key: {}".format(key))
                    log.info("value: {}".format(value))
                    log.info("开始更新json：{0}".format(json_obj))
                    json_obj = update_json(json_obj, {key: value})
                    log.info("更新json成功，更新后为：{}".format(json_obj))
                    gbl.temp.set(str(each_pre[1])[2:-1], json_obj)
                    run_flag = True
                except Exception as e:
                    log.error("json更新异常")
                    saveCode("json更新异常: {0}".format(str(e)))
                    run_flag = False

            elif one_pre.startswith("wait"):
                # 等待
                each_pre = one_pre.split('|')
                wait_time = int(each_pre[1])
                log.info("等待{}秒".format(wait_time))
                sleep(wait_time)
                run_flag = True

            elif one_pre.startswith(gbl.service.get("Database")):
                """
                one_pre: ${Database}.main|select 1 from dual|var|continue
                :var： 将sql查询结果赋值给变量var
                :continue：sql执行报错时继续执行后面的语句，否则报错退出
                """
                each_pre = one_pre.split('|')
                # 数据库操作
                db = gbl.service.get("Database")
                if gbl.db.get(db) is None:
                    raise KeyError("db.ini未配置对应数据库信息，请检查")

                # 如果db.ini已配置数据库信息
                schema = str(each_pre[0])[len(db)+1:]
                sql = each_pre[1]
                # 替换变量
                sql = gbl.replace(sql)
                # 根据数据类型，pg数据库自动替换uuid()为gen_random_uuid()
                db_type = gbl.db.get(db).get("type")
                if db_type == "postgres":
                    sql = sql.replace("uuid()", "gen_random_uuid()")
                    sql = sql.replace("UUID()", "gen_random_uuid()")
                if db_type == "oracle":
                    sql = sql.replace("uuid()", "sys_guid()")
                    sql = sql.replace("UUID()", "sys_guid()")
                    sql = sql.replace("now()", "sysdate")
                log.info("{0}【{1}】执行sql语句：{2}".format(db, gbl.schema.get(db).get(schema), sql))
                sql_util = SQLUtil(db=db, schema=schema)
                try:
                    if sql.find("select") == 0 or sql.find("SELECT") == 0:      # 查询
                        sql_result = sql_util.select(sql)
                    else:   # 修改或删除
                        if len(each_pre) > 3 and each_pre[3].lower() == "continue":
                            skip = True
                        else:
                            skip = False
                        sql_result = sql_util.update(sql, skip=skip)
                    log.info("成功执行sql语句：{}".format(sql))
                    # 将第3个参数加入全局变量字典
                    if len(each_pre) > 2:
                        if isinstance(sql_result, int):
                            sql_result = str(sql_result)
                        if isinstance(sql_result, str):
                            gbl.temp.set(each_pre[2], sql_result)
                            log.info("给变量{0}赋值：{1}".format(each_pre[2], sql_result))
                    run_flag = True
                except Exception as e:
                    if len(each_pre) > 3 and each_pre[3].lower() == "continue":
                        # 报错继续执行下一条
                        log.info("sql执行报错，忽略错误")
                        run_flag = True
                        continue
                    traceback.print_exc()
                    saveCode("执行数据库操作异常: {0}".format(str(e)))
                    run_flag = False

            else:
                each_pre = one_pre.split('|')
                try:
                    # 对特定数据库做操作
                    db_tmp = each_pre[0].split(".", 2)
                    db = db_tmp[0] + '.' + db_tmp[1]
                    schema = db_tmp[2]
                    if gbl.db.get(db) is None:
                        raise AssertionError("找不到指定数据源配置: {0}".format(db))

                    sql = each_pre[1]
                    # 替换变量
                    sql = gbl.replace(sql)
                    log.info("{0}【{1}】执行sql语句：{2}".format(db, gbl.schema.get(db).get(schema), sql))
                    sql_util = SQLUtil(db=db, schema=schema)
                    if sql.find("select") == 0 or sql.find("SELECT") == 0:  # 查询
                        sql_result = sql_util.select(sql)
                    else:  # 修改或删除
                        sql_result = sql_util.update(sql)
                    log.info("成功执行sql语句：{}".format(sql))
                    # 将第3个参数加入全局变量字典
                    if len(each_pre) > 2:
                        if isinstance(sql_result, int):
                            sql_result = str(sql_result)
                        if isinstance(sql_result, str):
                            gbl.temp.set(each_pre[2], sql_result)
                            log.info("给变量{0}赋值：{1}".format(each_pre[2], sql_result))
                    run_flag = True
                except Exception as e:
                    if len(each_pre) > 3 and each_pre[3].lower() == "continue":
                        # 报错继续执行下一条
                        log.info("sql执行报错，忽略错误")
                        run_flag = True
                        continue
                    traceback.print_exc()
                    log.error("不支持的预置操作: {0}".format(each_pre[0]))
                    saveCode("预置条件输入错误: {0}".format(str(e)))
                    run_flag = False

            if not run_flag:  # 预置条件执行失败，会执行到空行，结束执行预置条件
                break

        log.info("预置条件全部执行完成")
    gbl.temp.set("EndTime", datetime.now().strftime('%Y%m%d%H%M%S'))
    sleep(1)
    return run_flag
