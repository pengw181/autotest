# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:23

import pymysql
import cx_Oracle
import psycopg2
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


class SQLUtil:

    def __init__(self, db, schema):
        """
        :param db: 数据库标识，如gmcc.maria
        :param schema: 原始的schema，如main
        """
        db_info = gbl.db.get(db)
        log.debug("数据库配置信息：{0}".format(db_info))
        try:
            self.database_type = db_info.get("type")
            host = db_info.get("host")
            port = int(db_info.get("port"))
            if schema is None:
                raise KeyError("schema为空，无法操作数据库.")

            username = db_info.get(schema + ".username")
            password = db_info.get(schema + ".password")

            # 根据不同数据库建立连接
            if self.database_type == "mysql":
                database = db_info.get(schema + ".database")
                log.debug("{0}, {1}, {2}, {3}, {4}".format(host, port, database, username, password))
                self.conn = pymysql.connect(host=host, port=port, user=username, password=password, database=database)

            elif self.database_type == "oracle":
                tnsname = db_info.get("tnsname")
                log.debug("{0}, {1}, {2}, {3}, {4}".format(host, port, tnsname, username, password))
                dsn = cx_Oracle.makedsn(host, port, tnsname)
                self.conn = cx_Oracle.connect(username, password, dsn)

            elif self.database_type == "postgres":
                database = db_info.get(schema + ".database")
                self.conn = psycopg2.connect(database=database, user=username, password=password, host=host, port=port)

            else:
                self.conn = None

            if self.conn:
                self.curs = self.conn.cursor()
            else:
                raise KeyError("db.ini未指定当前数据库类型，无法建立数据库连接。")
            log.debug("Connected")
            log.debug("use {0}".format(username))
            self.finish_init = True

            self.result_rows = 0
        except AttributeError as e:
            log.warning("未配置{0}账号信息".format(db))
            raise e

    def select(self, sql):
        if self.finish_init:
            try:
                log.info(">>> 执行sql:> {0} ".format(sql))
                self.curs.execute(sql)
                # cursor.fetchall() 相当于从数据库取数据，但是取完就没有了，再下一行继续 cursor.fetchall()，取到的就只是空列表
                date = self.curs.fetchall()

                count = len(list(date))
                log.info("记录数：{0}".format(count))

                column = self.curs.description
                col_list = []
                for i in range(len(column)):
                    col_list.append(column[i][0])

                date_list = []
                for i in date:
                    date_list.append(list(i))

                # 如果查询结果较多，限制打印行数
                print_rows_limit = 10
                i = 0
                if print_rows_limit < len(date_list):  # 如果结果行数超过print_rows_limit，只打印部分结果
                    for row in date:
                        if i < print_rows_limit:
                            log.debug("{0}: {1}".format(i, list(row)))
                            i += 1
                        else:
                            log.debug("当前查询到的记录较多，只打印前{0}行.".format(print_rows_limit))
                            break

                self.result_rows = len(date_list)

                if self.result_rows == 0:
                    # 查不到结果
                    date_list = None
                else:
                    if self.result_rows == 1 and len(date_list[0]) == 1:
                        # 如果数组只有1个值，取值
                        date_list = date_list[0][0]

                    if isinstance(date_list, list):
                        if self.result_rows <= 5:
                            log.info("查询结果：{0}".format(date_list[:self.result_rows][:]))
                        else:
                            log.info("查询结果较多，此处不打印")
                    else:
                        log.info("查询结果：{0}".format(date_list))

                    # clob转字符串
                    if isinstance(date_list, cx_Oracle.LOB):    # 单个值
                        date_list = date_list.read()
                    elif isinstance(date_list, list):
                        temp_data_list = []
                        for temp in date_list:
                            if isinstance(temp, cx_Oracle.LOB):     # 一维数组
                                temp_data = temp.read()
                                temp_data_list.append(temp_data)
                            else:       # 二维数组
                                _temp_data_list = []
                                for _temp in temp:
                                    if isinstance(_temp, cx_Oracle.LOB):
                                        temp_data = _temp.read()
                                        _temp_data_list.append(temp_data)
                                    else:
                                        _temp_data_list.append(_temp)
                                temp_data_list.append(_temp_data_list)
                        date_list = temp_data_list

            except Exception as e:
                raise e
            finally:
                self.curs.close()
                self.conn.close()
        else:
            log.error("数据库初始异常，请检查！")
            self.curs.close()
            self.conn.close()
            date_list = None
        return date_list

    def update(self, sql, skip=False):
        if self.finish_init:
            try:
                log.info(">>> 执行sql:> {0} ".format(sql))
                if (sql.lower().startswith("update") or sql.lower().startswith("delete")) and sql.lower().find("where") == -1:
                    log.info("### 执行update、delete语句必须包含where条件")
                    flag = False
                else:
                    self.curs.execute(sql)
                    count = self.curs.rowcount
                    log.info("影响记录数：{0}".format(count))

                    # 非查询语句需要提交
                    self.conn.commit()
                    flag = True
            except Exception as e:
                self.conn.rollback()
                if skip:
                    flag = True
                else:
                    raise e
            finally:
                self.curs.close()
                self.conn.close()
        else:
            log.error("数据库初始异常，请检查！")
            flag = False
        return flag


if __name__ == '__main__':
    db1 = "v31.oracle"
    schema1 = "main"
    sql1 = "select column_name from user_tab_columns where table_name = upper('tn_node_email_attach') AND data_type = upper('clob')"
    t = SQLUtil(db1, schema1)
    sql_result = t.select(sql1)
    log.info("返回结果：%s " % sql_result)
    print(sql_result)
    clob_col = sql_result[:, 0]
    print(clob_col)
