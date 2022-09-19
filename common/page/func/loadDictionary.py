# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/11 下午9:38

from config.loads import properties
from common.log.logger import log


def load_dictionary(dictionary_file_name):
    if not properties.get("projectBasePath").endswith("/"):
        properties["projectBasePath"] += "/"
    file_path = properties.get("projectBasePath") + properties.get("projectName") + "/resources/dictionary/" + dictionary_file_name
    log.info("从{}加载字典数据".format(file_path))
    content = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            content.append(line)
    return content


if __name__ == "__main__":
    file_content = load_dictionary("ping_sample.txt")
    log.info(file_content)
