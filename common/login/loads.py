# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/9/13 下午6:04

import os
import configparser
from config.loads import properties


class LoadLoginConfig:

    def __init__(self):
        _conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/loginInfo.ini"
        # print(_conf_dir)

        # 对内容隐藏字符做处理，替换隐藏字符
        # content = open(dir).read()
        # content = re.sub(r"\n", "", content)
        # content = re.sub(r"\xfe\xff", "", content)
        # content = re.sub(r"\xff\xfe", "", content)
        # content = re.sub(r"\xef\xbb\xbf", "", content)
        # open(dir, 'w').write(content)

        self.cf = configparser.ConfigParser()
        self.config = self.cf.read(_conf_dir)

    def get_sections(self):
        return self.cf.sections()

    def get_option(self, section):
        return self.cf.options(section)

    def get_value(self, section, option):
        return self.cf.get(section, option)

    def get_config(self):
        self.config = {}
        for s in self.get_sections():
            _config = {}
            for o in self.get_option(s):
                value = self.get_value(s, o)
                _config[o] = value
            self.config[s] = _config
        return self.config


app = properties.get("application")
login_config = LoadLoginConfig().get_config().get(app)


if __name__ == "__main__":
    print(login_config.get("username"))
