# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2023/2/10 下午6:16

import yaml
import os
import configparser
from src.main.python.lib.globals import gbl


class Configuration:

    def __init__(self, config):

        self.properties = {}  # 系统配置
        self.service = {}  # 业务参数，可以修改
        self.db = {}  # 数据库配置
        self.mongo = {}  # mongodb配置
        self.login = {}  # 测试登录参数，可以修改
        self.schema = {}  # schema配置
        self.case = {}  # 测试用例

        if config:
            for filename, file_content in config.items():
                if filename.endswith(".properties"):
                    self.load_properties(file_content)
                elif filename.endswith(".yaml"):
                    self.load_yaml(file_content)

        self.load_db()
        self.load_mongo()
        self.load_login()
        self.load_schema()
        # self.load_case()

    def load_properties(self, file_content):
        self.properties = Properties().get_properties(file_content)

    def load_yaml(self, file_content):
        self.service = yaml.load(file_content, Loader=yaml.FullLoader)

    def load_db(self):
        conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/db.ini"
        self.db = IniConfig(conf_dir).get_config()

    def load_mongo(self):
        conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/mongodb.ini"
        self.mongo = IniConfig(conf_dir).get_config()

    def load_login(self):
        conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/loginInfo.ini"
        self.login = IniConfig(conf_dir).get_config()

    def load_schema(self):
        conf_dir = os.path.dirname(os.path.abspath(__file__)) + "/schema.ini"
        self.schema = IniConfig(conf_dir).get_config()

    def load_case(self):
        application = self.properties.get('application')
        with open(os.path.dirname(os.path.abspath(__file__)) + "/app/{}/case.yaml".format(application), 'r') as f:
            first_line = True
            file_content = ""
            for line in f.readlines():
                if not file_content and first_line:
                    file_content = line
                    first_line = False
                else:
                    file_content = file_content + line
            self.case = yaml.load(file_content, Loader=yaml.FullLoader)


class Properties(object):

    def __init__(self):
        self.properties = {}

    def __get_dict(self, strName, dictName, value):
        if strName.find('.') > 0:
            k = strName.split('.')[0]
            dictName.setdefault(k, {})
            return self.__get_dict(strName[len(k) + 1:], dictName[k], value)
        else:
            dictName[strName] = value
            return

    def get_properties(self, file_content):
        try:
            for line in file_content.split("\n"):
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0]) + 1:]
                    self.__get_dict(strs[0].strip(), self.properties, strs[1].strip())
        except Exception as e:
            raise e
        else:
            return self.properties


class IniConfig:

    def __init__(self, ini_dir):

        # 对内容隐藏字符做处理，替换隐藏字符
        # content = open(ini_dir).read()
        # content = re.sub(r"\n", "", content)
        # content = re.sub(r"\xfe\xff", "", content)
        # content = re.sub(r"\xff\xfe", "", content)
        # content = re.sub(r"\xef\xbb\xbf", "", content)
        # open(dir, 'w').write(content)

        self.cf = configparser.ConfigParser()
        self.config = self.cf.read(ini_dir)

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


def global_config(config_dict=None):

    configs = Configuration(config_dict)

    # service业务参数配置
    if len(configs.service) == 0:     # 读取本地配置文件app.properties和yaml文件
        with open(os.path.dirname(os.path.abspath(__file__)) + "/app.properties", 'r') as f:
            first_line = True
            file_content = ""
            for line in f.readlines():
                if not file_content and first_line:
                    file_content = line
                    first_line = False
                else:
                    file_content = file_content + line
            configs.load_properties(file_content)

        environment = configs.properties.get('environment')
        with open(os.path.dirname(os.path.abspath(__file__)) + "/branch/{}.yaml".format(
                environment.replace(".", "_")), 'r') as f:
            first_line = True
            file_content = ""
            for line in f.readlines():
                if not file_content and first_line:
                    file_content = line
                    first_line = False
                else:
                    file_content = file_content + line
            configs.load_yaml(file_content)

    # 加载case文件
    configs.load_case()

    # properties配置文件
    for key, value in configs.properties.items():
        gbl.service.set(key, value)

    # db配置文件
    for key, value in configs.db.items():
        gbl.db.set(key, value)

    # mongodb配置文件
    for key, value in configs.mongo.items():
        gbl.mongo.set(key, value)

    # login配置文件
    for key, value in configs.login.items():
        gbl.login.set(key, value)

    # schema配置文件
    for key, value in configs.schema.items():
        gbl.schema.set(key, value)

    # case配置文件
    for key, value in configs.case.items():
        gbl.case.set(key, value)

    # yaml配置文件
    gbl.service.set('ControllerPath', configs.service.get('controller').get("path"))
    gbl.service.set('TestCasePath', configs.service.get('testcase').get("path"))
    gbl.service.set('ContinueRunWhenError', configs.service.get('testcase').get("continueRunWhenError"))
    gbl.service.set('BuiltReport', configs.service.get('report').get("build"))
    gbl.service.set('RunAllTest', configs.service.get('testcase').get("runAll"))
    gbl.service.set('RunTestLevel', configs.service.get('testcase').get("runLevel"))

    gbl.service.set('PageUrl', configs.service.get('login').get("url"))
    gbl.service.set('SystemLoginUrl', configs.service.get('login').get("systemUrl"))
    gbl.service.set('BelongID', configs.service.get('login').get("belongId"))
    gbl.service.set('DomainID', configs.service.get('login').get("domainId"))
    gbl.service.set('Belong', configs.service.get('login').get("belong"))
    gbl.service.set('Domain', configs.service.get('login').get("domain"))
    gbl.service.set('LoginUser', configs.service.get('login').get("username"))
    gbl.service.set('LoginPwd', configs.service.get('login').get("password"))

    gbl.service.set('ThirdSystem', configs.service.get('thirdSystem').get("url"))
    gbl.service.set('ThirdSystemHttps', configs.service.get('thirdSystem').get("https"))

    for i in range(len(configs.service.get('netunit'))):
        gbl.service.set('NetunitMME{}'.format(i+1), configs.service.get('netunit')[i])
