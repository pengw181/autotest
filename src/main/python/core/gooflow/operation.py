# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/21 上午10:48

import json
from datetime import datetime
from src.main.python.core.loginPage import login
from src.main.python.core.mainPage import AiSee
from src.main.python.lib.logger import log
from src.main.python.lib.globals import gbl
from src.main.python.core.gooflow.controller import serverRun


def basic_run(step):

    # 每一个操作格式：
    """
    {
        "操作": "xxx",
        "参数": {
            "xxx": "xxx",
            "xxx": "xxx"
        }
    }
    """

    # 替换变量
    step = gbl.replace(json.dumps(step))
    log.info("步骤：\n%s" % json.dumps(json.loads(step), indent=4, ensure_ascii=False))
    func = eval(step).get("操作")
    param = eval(step).get("参数")
    log.info("开始执行操作： {0}".format(func))
    # log.info("参数： {0}".format(param))
    gbl.temp.set("ResultMsg", "")
    if func == "LoginAiSee":

        """
        {
            "操作": "LoginAiSee",
            "参数": {
                "用户名": "pw",
                "密码": "1qazXSW#"
            }  
        }  
        """
        username = param.get("用户名")
        password = param.get("密码")
        run_flag = login(username, password)

    elif func == "EnterDomain":

        """
        {
            "操作": "EnterDomain",
            "参数": {
                "归属": "广州市",
                "领域明细": "广州核心网"
            }  
        }
        """

        action = AiSee()
        belong = param.get("归属")
        domain = param.get("领域明细")
        run_flag = action.enter_domain(belong, domain)

    else:
        # 根据系统名称，选择执行具体业务操作
        """
        func = eval(step_one).get("操作")
        param = eval(step_one).get("参数")
        """
        run_flag = serverRun(func, param)

    gbl.temp.set("EndTime", datetime.now().strftime('%Y%m%d%H%M%S'))
    return run_flag
