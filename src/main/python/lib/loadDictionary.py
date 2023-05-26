# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/11 下午9:38

from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl


def load_dictionary(dictionary_file_name):
    file_path = gbl.service.get("ProjectPath") + '/src/main/resources/dictionary/' + dictionary_file_name
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
