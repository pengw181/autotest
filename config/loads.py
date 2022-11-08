# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午10:24

import os
import configparser
from .app import transferAppName
from service.lib.variable.globalVariable import *


class LoadDBConfig:

    def __init__(self):
        _conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/db.ini"
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


db_config = LoadDBConfig().get_config()


class LoadMongoConfig:

    def __init__(self):
        _conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/mongodb.ini"

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


mongo_config = LoadMongoConfig().get_config()


class Properties(object):

    def __init__(self):
        self.fileName = os.path.dirname(__file__) + "/app.properties"
        self.properties = {}

    def __get_dict(self, strName, dictName, value):
        if strName.find('.') > 0:
            k = strName.split('.')[0]
            dictName.setdefault(k, {})
            return self.__get_dict(strName[len(k)+1:], dictName[k], value)
        else:
            if strName == "application":    # application参数映射，特殊处理
                value = transferAppName(value)
            dictName[strName] = value
            return

    def get_properties(self):
        try:
            pro_file = open(self.fileName, 'r')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0])+1:]
                    self.__get_dict(strs[0].strip(), self.properties, strs[1].strip())
        except Exception as e:
            raise e
        else:
            pro_file.close()
        return self.properties


properties = Properties().get_properties()
set_global_var("Application", properties.get("application"))
set_global_var("Environment", properties.get("environment"))
set_global_var("CrawlerVersion", properties.get("crawlerVersion"))


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


login_config = LoadLoginConfig().get_config().get(properties.get("application"))
