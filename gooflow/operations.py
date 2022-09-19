# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/23 下午9:30

from datetime import datetime
import json
from time import sleep
from app.AiSee.main.loginPage import login
from app.AiSee.main.mainPage import AiSee
from common.log.logger import log
from common.variable.globalVariable import *
from common.run.servers import serverRun


def basicRun(step):

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
    step = replace_global_var(json.dumps(step))
    log.info("步骤：\n%s" % json.dumps(json.loads(step), indent=4, ensure_ascii=False))
    func = eval(step).get("操作")
    param = eval(step).get("参数")
    log.info("开始执行操作： {0}".format(func))
    # log.info("参数： {0}".format(param))
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
        sleep(2)

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

    set_global_var("EndTime", datetime.now().strftime('%Y%m%d%H%M%S'), False)
    return run_flag
