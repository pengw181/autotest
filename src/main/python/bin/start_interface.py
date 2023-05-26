# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 上午11:22

import flask
import threading
from werkzeug.routing import BaseConverter
from src.main.python.conf.config import global_config
from src.main.python.lib.globals import gbl

app = flask.Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/http/web-test', methods=['GET', 'POST'])
def main():
    print("------------------------")

    req_method = flask.request.method
    print("req_method: {}".format(req_method))
    print("req_form: {}".format(flask.request.form.to_dict()))
    config = {}
    for file in flask.request.files.getlist('file'):
        file_name = file.filename
        print("接收配置文件: {}".format(file_name))
        file_content = file.stream.read().decode('utf8')
        config[file_name] = file_content
    if len(config) == 0:
        print("客户端未发送配置文件，使用本地配置文件")
    global_config(config_dict=config)
    gbl.service.set('application', flask.request.form.get("application"))
    gbl.service.set('environment', flask.request.form.get("environment").replace("_", "."))
    print("service: {}".format(gbl.service))
    print("db: {}".format(gbl.db))
    print("mongo: {}".format(gbl.mongo))
    print("login: {}".format(gbl.login))
    print("schema: {}".format(gbl.schema))

    from src.main.python.core.gooflow.case import loadCase
    # 开始运行，第一个数字为读取第几个测试用例文件（从1开始），第二个数字为读取测试用例的第几行（从1开始）
    begin_file = int(flask.request.form.get("begin_file"))
    begin_case = int(flask.request.form.get("begin_case"))
    username = flask.request.form.get("username")
    if username:
        gbl.service.set("LoginUser", username)
    password = flask.request.form.get("password")
    if password:
        gbl.service.set("LoginPwd", password)
    callback_url = flask.request.form.get("callback_url")
    threads = threading.Thread(target=loadCase, args=(begin_file, begin_case, callback_url))
    threads.setDaemon(True)
    threads.start()
    threads.join()  # 所有子线程运行完成后主线程再返回
    gbl.service.set("Thread", threads)
    return flask.jsonify({"success": True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8099, debug=True)
