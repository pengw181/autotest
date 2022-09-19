# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/5/11 下午4:58

from time import sleep

def change_color(browser, color):
    """
    # 可视化图样式配置设置【背景颜色】
    :param browser:
    :param color: #FFFFFF
    """
    # 设置颜色
    js = "$('#backgroundColor').val('{0}');".format(color)
    browser.execute_script(js)

    # 调用change方法
    js = "g.visualImageConfig.customBgColorChange($('#backgroundColor'));"
    browser.execute_script(js)
    return


def setVisible(browser, class_name):
    """
    # 应用仪表盘展示menu按钮，比如关闭进入配置页
    :param browser:
    :param class_name: 类名
    """
    # 设置可见
    js = "$('.{0}').css('visibility', 'visible')".format(class_name)
    browser.execute_script(js)
    sleep(1)

    # 设置top
    js = "$('.{0}').css('top', '0')".format(class_name)
    browser.execute_script(js)
    sleep(1)
    return
