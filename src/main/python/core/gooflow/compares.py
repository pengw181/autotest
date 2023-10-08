# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:14

import json
from datetime import datetime
from time import sleep
from src.main.python.core.gooflow.checks import check_db_data, check_msg
from src.main.python.lib.updateData import update_dict_by_path
from src.main.python.lib.download import exist_download_file
from src.main.python.db.SQLHelper import SQLUtil
from src.main.python.db.mongoDB import MongoDB
from src.main.python.core.gooflow.codes import saveCode
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def compare_data(checks):
    """"
    :param: checks：string
    :return: bool
    """
    # 定义一个检查标识
    check_result = True
    sleep(3)

    if checks is None:
        # 无需匹配，直接返回True
        return check_result

    gbl.temp.set("EndTime", datetime.now().strftime('%Y%m%d%H%M%S'))
    check_list = checks.split(chr(10))    # 第一次使用换行拆分比对预期结果单元格内容

    # 去空行、空格
    _tmp = []
    for one_check in check_list:
        one_check = one_check.strip()
        if one_check != "":
            _tmp.append(one_check)
    check_list = _tmp

    check_item_index = 1
    for i in range(len(check_list)):
        one_check = check_list[i]
        log.info("开始处理【{0}】 {1}".format(i+1, one_check))
        my_list = one_check.split('|')   # 将数据以竖线分割
        compare_item = my_list[0]       # CheckData
        check_item_index = i

        if compare_item == "CheckData":
            db_schema_table = my_list[1]
            # log.info("db_schema_table: {}".format(db_schema_table))
            # ${Database}.main.tn_process_conf_info
            tmp = db_schema_table.split(".")
            table_name = tmp[-1]
            schema = tmp[-2]
            db = ".".join(tmp[: -2])
            if schema == "nu":
                table_name = schema + '.' + table_name
                schema = "sso"

            count = my_list[2]
            data = "|".join(my_list[3:])

            # 自动替换${xx}变量
            db = gbl.replace(db)
            table_name = gbl.replace(table_name)
            log.info("db: {0}, schema: {1}".format(db, gbl.schema.get(db).get(schema)))
            data = gbl.replace(data)
            log.info("data: {}".format(data))

            check_result = check_db_data(db, schema, table_name, data, count)
            if not check_result.get("status"):
                saveCode("{0}表数据不匹配，{1}".format(table_name, check_result.get("data")))
                check_result = False
                break

        elif compare_item == "CheckMsg":
            # 校验弹出框信息
            check_result = check_msg(msg=my_list[1])
            if not check_result:
                saveCode("ErrorMsg不匹配，弹出框返回: {}".format(gbl.temp.get("ResultMsg")))
                break

        elif compare_item == "CheckDownloadFile":
            # 检验下载文件名
            my_list = check_list[i].split('|', 2)
            sleep(5)
            check_result = exist_download_file(filename=my_list[1], file_suffix=my_list[2])
            if not check_result:
                saveCode("下载文件名不匹配")
                break

        elif compare_item == "CheckFile":
            # 文件目录管理判断上传文件是否正确
            if my_list[1] != gbl.temp.get("CheckFileName"):
                check_result = False
                saveCode("文件名比对失败，实际文件名: {0}".format(gbl.temp.get("CheckFileName")))
                break
            else:
                check_result = True

        elif compare_item == "NoCheck":
            # 不校验，只要前面步骤不报错，直接通过
            log.info("本条匹配项不做匹配，跳过")

        elif compare_item == "Wait":
            sleep_time = int(my_list[1])
            log.info("Sleep {} seconds".format(sleep_time))
            sleep(sleep_time)

        elif compare_item == "GetData":
            # GetData|${Database}.main|select xx from xx|NodeID
            # 将sql查询到的结果，赋值给新变量名NodeID，匹配结果中，以${NodeID}使用变量的值
            db_tmp = my_list[1].split(".")

            schema = db_tmp[-1]
            db = ".".join(db_tmp[: -1])
            db = gbl.replace(db)
            # schema = schema_config.get(db).get(schema)
            # 如果没创建nu，使用sso登录，但sql语句里需要主动加上nu.前缀
            if schema == "nu":
                schema = "sso"
            log.info("db: {0}, schema: {1}".format(db, gbl.schema.get(db).get(schema)))
            sql = my_list[2]
            # 自动替换${xx}变量
            db = gbl.replace(db)
            sql = gbl.replace(sql)

            sql_util = SQLUtil(db=db, schema=schema)
            sql_result = sql_util.select(sql)
            # 将查到的结果，存入全局变量
            gbl.temp.set(my_list[3].strip(), sql_result)

        elif compare_item == "UpdateData":
            # 更新字典数据
            obj = gbl.temp.get(my_list[1])
            value = gbl.temp.get(my_list[3])
            data = update_dict_by_path(obj, my_list[2], value)
            data = str(data)
            data = data.replace("'", "\"")
            data = data.replace(": ", ":")
            data = data.replace(", ", ",")
            data = data.replace("True", "true")
            data = data.replace("False", "false")
            data = data.replace("\"", "\\\"")
            log.info("数据更新结果: {0}".format(data))
            gbl.temp.set(my_list[1], data)

        elif compare_item == "GetMongoData":
            # 从mongodb获取数据
            # GetMongoData|Workflow.VosNode.AttachFile.files|{"filename": "factor.xlsx"}|[("uploadDate", -1)]|fetchAttachId|AttachID
            mongo_db = MongoDB()
            collection = my_list[1]
            query = json.loads(my_list[2])
            sort = my_list[3]
            fetch_id = my_list[4]
            save_var = my_list[5]
            mongo_db.get_collection(collection=collection)
            mongo_data = mongo_db.find_with_condition(condition=query, sorted=sort)[-1].get(fetch_id)
            log.info("从mongodb获取到数据{0}结果: {1}".format(fetch_id, mongo_data))
            gbl.temp.set(save_var, mongo_data)

        else:
            log.error("非法比对函数: {0}".format(compare_item))
            saveCode("无法找到对应比对函数{0}".format(compare_item))
            check_result = False
            break
    if check_result:
        log.info("比对结果全部执行完成")
    else:
        log.info("第【{}】条数据比对失败".format(check_item_index + 1))
    # 判断返回结果
    return check_result
