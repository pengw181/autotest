# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/2/14 下午5:25

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def calculation(interval, unit, time_format='%Y-%m-%d %H:%M:%S'):
    """
    :param interval: 间隔，0表示当前，正数表示未来，负数表示过去
    :param unit: 单位，年、月、天、时、分、秒
    :param time_format: 时间格式
    :return: 时间字符串
    """
    interval = int(interval)
    if unit not in ["年", "月", "天", "时", "分", "秒"]:
        raise AttributeError("【单位】参数错误：{0}".format(unit))

    now = datetime.now()
    # 间隔为0时，返回当前时间
    if interval == 0:
        cal_result = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    else:
        if unit == "年":
            if interval > 0:
                cal_result = now + relativedelta(years=interval)
            else:
                cal_result = now - relativedelta(years=abs(interval))
            cal_result = cal_result.strftime(time_format)
        elif unit == "月":
            if interval > 0:
                cal_result = now + relativedelta(months=interval)
            else:
                cal_result = now - relativedelta(months=abs(interval))
            cal_result = cal_result.strftime(time_format)
        elif unit == "天":
            delta = timedelta(days=interval)
            cal_result = datetime.strftime(datetime.now() + delta, time_format)
        elif unit == "时":
            delta = timedelta(hours=interval)
            cal_result = datetime.strftime(datetime.now() + delta, time_format)
        elif unit == "分":
            delta = timedelta(minutes=interval)
            cal_result = datetime.strftime(datetime.now() + delta, time_format)
        else:
            delta = timedelta(seconds=interval)
            cal_result = datetime.strftime(datetime.now() + delta, time_format)

    return cal_result


if __name__ == "__main__":
    result1 = calculation("2", "天")
    result2 = calculation("0", "天")
    result3 = calculation("-3", "月")
    result4 = calculation("1", "年")
    result5 = calculation("3", "时")
    result6 = calculation("-30", "分")
    result7 = calculation("-30", "秒")

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
