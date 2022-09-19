# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午2:45

import os
from common.log.logger import log
from config.loads import properties


def exist_download_file(filename, file_suffix):

    """
    :param filename: 文件名部分信息
    :param file_suffix: 文件后缀
    :return: True/False
    """

    find_flag = False
    downLoadPath = properties.get("projectBasePath") + properties.get("projectName") + properties.get("downLoadPath")
    dir_files = os.listdir(downLoadPath)
    for f in dir_files:
        if f.find(filename) > -1 and f.endswith(file_suffix.lower()):
            log.info("{0}下找到文件 {1}，满足匹配".format(downLoadPath, f))
            find_flag = True
    if not find_flag:
        log.info("当前下载目录下未找到指定文件，文件列表如下：\n{0}".format("\n".join(dir_files)))
        raise FileNotFoundError("未找到指定下载文件")
    return find_flag


if __name__ == "__main__":
    exist_download_file("函数", "xls")
