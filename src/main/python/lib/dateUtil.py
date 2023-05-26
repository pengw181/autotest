# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午9:17

import re
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.globals import gbl


def set_calendar(date_s, date_format="%Y-%m-%d"):
    """
    # calendar，告警计划重调
    :param date_s: 字符串，2020-11-15
    :param date_format: 时间格式%Y-%m-%d %H:%M:%S
    """
    browser = gbl.service.get("browser")
    # 解析date_s
    if date_s == "now":
        # 现在
        browser.find_element(By.XPATH, "//*[text()='今天']").click()
    else:
        # date_s = "2019-02-27 17:50:30"
        time = datetime.strptime(date_s, date_format)

        year = time.date().year
        month = time.date().month
        day = time.date().day

        hour = time.hour
        minute = time.minute
        second = time.second
        # 给时分秒单数字前补0
        if hour < 10:
            hour = "0" + str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        if second < 10:
            second = "0" + str(second)

        # 点开年月
        m_y_ele = browser.find_elements(By.XPATH, "//*[@class='calendar-title']/span")
        for y in m_y_ele:
            if y.is_displayed():
                y.click()
                break

        # 设置年
        year_ele = browser.find_elements(By.XPATH, "//*[@class='calendar-menu-year']")
        for y in year_ele:
            if y.is_displayed():
                y.clear()
                y.send_keys(year)
                # log.info("输入年: {0}".format(year))
                break

        # 设置月
        month_ele = browser.find_elements(
            By.XPATH, "//*[contains(@class,'calendar-menu-month') and @abbr='{0}']".format(month))
        for m in month_ele:
            if m.is_displayed():
                m.click()
                # log.info("点击月: {0}".format(month))
                break

        # 设置日
        day_ele = browser.find_elements(
            By.XPATH, "//*[contains(@class,'calendar-day') and @abbr='{0},{1},{2}']".format(year, month, day))
        for d in day_ele:
            if d.is_displayed():
                d.click()
                # log.info("点击日: {0}".format(day))
                break

        # 设置时分秒
        hms_ele = browser.find_elements(By.XPATH, "//*[contains(@class,'timespinner-f')]/following-sibling::span//input[1]")
        for hms in hms_ele:
            if hms.is_displayed():
                hms.clear()
                if second:
                    enter_time = "{0}:{1}:{2}".format(hour, minute, second)
                else:
                    enter_time = "{0}:{1}".format(hour, minute)
                hms.send_keys(enter_time)
                # 点击确定
                ok_button = browser.find_elements(By.XPATH, "//*[@class='datebox-button']//*[text()='确定']")
                for ok in ok_button:
                    if ok.is_displayed():
                        ok.click()
                        break
                # _format = browser.find_elements_by_xpath(
                #     "//*[contains(@class,'timespinner-f')]/following-sibling::span//input[2]")
                # for _ in _format:
                #     if _.is_displayed():
                #         _hms = _.get_attribute("value")
                #         h_len = _hms.split(":")
                #         if len(h_len) == 2:
                #             # 时:分
                #             enter_time = "{0}:{1}".format(hour, minute)
                #         else:
                #             # 时:分:秒
                #             enter_time = "{0}:{1}:{2}".format(hour, minute, second)
                #         hms.send_keys(enter_time)
                #         log.info("设置时分秒: {0}".format(enter_time))
                #
                #         # 点击确定
                #         browser.find_element(By.XPATH, "//*[@class='datebox-button']//*[text()='确定']").click()
                #         break
                # break


def set_laydate(date_s, date_format="%Y-%m-%d"):
    """
    # laydate，用在告警规则选择时间
    :param date_s: 字符串，2020-11-15
    :param date_format: 时间格式%Y-%m-%d %H:%M:%S
    """
    browser = gbl.service.get("browser")
    # 解析date_s
    if date_s == "now":
        # 现在
        browser.find_element(By.XPATH, "//*[@lay-type='now']").click()
    else:
        # date_s = "2019-02-27 17:50:30"
        time = datetime.strptime(date_s, date_format)

        year = time.date().year
        month = time.date().month
        day = time.date().day

        hour = time.hour
        minute = time.minute
        second = time.second

        # 设置年
        browser.find_element(By.XPATH, "//*[@class='laydate-set-ym']/span[1]").click()
        try:
            browser.find_element(By.XPATH, "//*[@lay-ym='{0}']".format(year)).click()
            year_is_show = True
        except NoSuchElementException:
            year_is_show = False
        while year_is_show is False:
            # 判断年是否在可选范围内
            year_period_obj = browser.find_element(By.XPATH, "//*[@class='laydate-set-ym']")
            year_period = year_period_obj.get_attribute("innerText")
            # 2092年 - 2106年
            patt1 = r'(\d{4})年 - (\d{4})年'
            year_period_match = re.match(patt1, year_period).groups()
            year_period_begin = year_period_match[0]
            year_period_end = year_period_match[1]

            if year < int(year_period_begin):
                # 如果年比当前最小年还小，点击往前翻页
                browser.find_element(By.XPATH, "//*[contains(@class,'laydate-prev-y')]").click()
            elif year > int(year_period_end):
                # 如果年比当前最大年还大，点击往后翻页
                browser.find_element(By.XPATH, "//*[contains(@class,'laydate-next-y')]").click()
            else:
                browser.find_element(By.XPATH, "//*[@lay-ym='{0}']".format(year)).click()
                year_is_show = True
        # log.info("选择年: {0}".format(year))

        # 设置月
        patt = r'0{0,}(\d+)'
        month_match = re.match(patt, str(month)).groups()
        month = month_match[0]
        show_month = int(month)-1
        browser.find_element(By.XPATH, "//*[@class='laydate-set-ym']/span[2]").click()
        browser.find_element(By.XPATH, "//*[@lay-ym='{0}']".format(show_month)).click()
        # log.info("选择月: {0}".format(month))

        # 设置日
        patt = r'0{0,}(\d+)'
        day_match = re.match(patt, str(day)).groups()
        day = int(day_match[0])
        ymd = "-".join([str(year), str(month), str(day)])
        browser.find_element(By.XPATH, "//*[@lay-ymd='{0}']".format(ymd)).click()
        # log.info("选择日: {0}".format(day))

        # 点开选择时间
        if hour is not None:
            browser.find_element(By.XPATH, "//*[text()='选择时间']").click()

        action = ActionChains(browser)

        # 设置时
        if hour is not None:
            if hour < 10:
                hour = "0" + str(hour)
            hour_ele = browser.find_element(
                By.XPATH, "//*[text()='时']/following-sibling::ol/li[text()='{0}']".format(hour))
            action.move_to_element(hour_ele).click().perform()
            hour_ele.click()
            # log.info("设置时: {0}".format(hour))

        # 设置分
        if minute is not None:
            if minute < 10:
                minute = "0" + str(minute)
            minute_ele = browser.find_element(
                By.XPATH, "//*[text()='分']/following-sibling::ol/li[text()='{0}']".format(minute))
            action.move_to_element(minute_ele).click().perform()
            minute_ele.click()
            # log.info("设置分: {0}".format(minute))

        # 设置秒
        if second is not None:
            if second < 10:
                second = "0" + str(second)
            second_ele = browser.find_element(
                By.XPATH, "//*[text()='秒']/following-sibling::ol/li[text()='{0}']".format(second))
            action.move_to_element(second_ele).click().perform()
            second_ele.click()
            # log.info("设置秒: {0}".format(second))

        # 点击确定
        browser.find_element(By.XPATH, "//*[@lay-type='confirm']").click()
