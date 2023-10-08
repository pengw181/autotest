# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/6/22 上午10:44

from src.main.python.lib.globals import gbl
from src.main.python.db.SQLHelper import SQLUtil


def checkColTypeDate(table_name, schema, col):
    if gbl.service.get("DataCol") is None:
        gbl.service.set("DataCol", [])
    if gbl.service.get("DataTableName") is None:
        gbl.service.set("DataTableName", [])
    if table_name.upper() not in gbl.service.get("DataTableName"):
        database_type = gbl.service.get("DatabaseType")
        if database_type == "oracle":
            find_date_type_sql = """SELECT column_name FROM user_tab_columns 
                              WHERE data_type in ('DATE', 'TIMESTAMP', 'DATETIME') 
                              AND table_name = upper('{}')""".format(table_name)        # 查询结果大写
            sql_util = SQLUtil(db=gbl.service.get("Database"), schema=schema)
            sql_result = sql_util.select(find_date_type_sql)
        elif database_type == "mysql":
            find_date_type_sql = """SHOW columns from {} where type in ('datetime')""".format(table_name)   # 表名不区分大小写，查询结果小写
            sql_util = SQLUtil(db=gbl.service.get("Database"), schema=schema)
            sql_result = sql_util.select(find_date_type_sql)
            if sql_result is not None:
                sql_result = [t[0] for t in sql_result]
        elif database_type == "postgres":
            find_date_type_sql = """select s.col_name from (
                                SELECT 
                                    distinct a.attname as col_name,
                                    a.atttypid as col_type_id,
                                    format_type(a.atttypid,a.atttypmod) as col_type
                                FROM 
                                    pg_class as c,pg_attribute as a 
                                where 
                                    a.attrelid = c.oid and a.attnum>0 and c.relname = '{}'
                            ) s where s.col_type_id in (select oid from pg_type t where t.typname in ('timestamp'))
                            """.format(table_name)      # 表名区分大小写，要小写
            sql_util = SQLUtil(db=gbl.service.get("Database"), schema=schema)
            sql_result = sql_util.select(find_date_type_sql)
        else:
            raise KeyError("错误的DatabaseType")

        if sql_result is not None:
            if isinstance(sql_result, str):
                gbl.service.get("DataCol").append(sql_result)
            elif isinstance(sql_result, list):
                sql_result = [t[0] for t in sql_result]
                gbl.service.get("DataCol").extend(sql_result)
        gbl.service["DataTableName"].append(table_name.upper())
    col = str(col.upper())
    is_date_type = True if col in gbl.service.get("DataCol") else False
    return is_date_type


if __name__ == "__main__":
    table = "tn_process_conf"
    schema = "main"
    col_name = "try_time"
    print(checkColTypeDate(table, schema, col_name))
