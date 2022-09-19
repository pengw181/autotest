# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:24

import logging
import os
from config.loads import properties
from common.variable.globalVariable import *


def get_logger():
    # 创建logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置logger日志等级
    logs_path = properties.get("projectBasePath") + '/webappv31/logs/'
    application = get_global_var("Application")
    if application is None:
        filename = logs_path + "catalina.out"
    else:
        filename = logs_path + application + "_sys.log"

    # logs目录不存在则自动创建
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    if not logger.handlers:
        # 创建handler

        fh = logging.FileHandler(filename, encoding="utf-8")   # 设置日志写入文件
        ch = logging.StreamHandler()    # 控制台输出

        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(pathname)s[%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %X"
        )

        # 为handler指定输出格式，注意大小写
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


log = get_logger()
