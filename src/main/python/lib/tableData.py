# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/10/22 下午3:30

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from src.main.python.lib.globals import gbl
from src.main.python.lib.logger import log


def get_table_data(data_table_xpath, column_table_xpath=None, limit=20, return_column=False):
    """
    :param column_table_xpath: 列名table的xpath
    :param data_table_xpath: 数据table的xpath
    :param limit: 限制数据输出行数，默认输出20行
    :param return_column: 输出是否包含列名
    :return: 二维表
    """
    browser = gbl.service.get("browser")
    # 获取输出变量
    columns = []
    table_data = []

    # 获取列名信息
    if column_table_xpath:
        column_field = browser.find_elements(By.XPATH, column_table_xpath + "/tbody/tr/td/div/span[1]")
        for c in column_field:
            columns.append(c.get_attribute("innerText"))
        log.info("表格列信息:【{}】".format(",".join(columns)))

    # 获取表格数据，会有多行
    for i in range(1, limit+1):
        try:
            data_grid = browser.find_elements(By.XPATH, data_table_xpath + "//tr[{}]//div".format(i))
            tmp = []
            for data in data_grid:
                tmp.append(data.get_attribute("innerText"))
            log.debug("第{0}行：【{1}】".format(i, ','.join(tmp)))
            if len(tmp) > 0:
                table_data.append(tmp)
                i += 1
            else:
                break
        except NoSuchElementException:
            break
    log.info("表格数据信息:\n{}".format(table_data))

    # 输出是否包含列名
    if return_column:
        if column_table_xpath is None:
            raise KeyError("未获取列名信息，请检查参数配置")
        else:
            table_data.insert(0, columns)

    # 输出结果
    return table_data


def get_table_data2(table_xpath, return_column=False):
    """
    :param table_xpath: table的xpath
    :param return_column: 输出是否包含列名
    :return: 二维表
    """
    browser = gbl.service.get("browser")
    # 获取输出变量
    columns = []
    table_data = []

    # 获取列名信息
    if return_column:
        column_field = browser.find_elements(By.XPATH, table_xpath + "/thead/tr/th")
        for c in column_field:
            columns.append(c.get_attribute("innerText"))
        log.info("表格列信息:【{}】".format(",".join(columns)))

    # 获取表格数据，会有多行
    flag = True
    i = 1
    while flag:
        data_grid = browser.find_elements(By.XPATH, table_xpath + "/tbody/tr[{}]/td".format(i))
        if len(data_grid) == 0:
            flag = False
        else:
            tmp = []
            for data in data_grid:
                tmp.append(data.get_attribute("innerText"))
            log.debug("第{0}行：【{1}】".format(i, ','.join(tmp)))
            table_data.append(tmp)
            i += 1

    log.info("表格数据信息:\n{}".format(table_data))

    # 输出是否包含列名
    if return_column:
        table_data.insert(0, columns)

    # 输出结果
    return table_data


if __name__ == "__main__":
    # column_xpath = "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@id='tb']/following-sibling::div[1]/div[2]/div[1]//table"
    # data_xpath = "//*[@menuid='AiSee_Netunit2013']/following-sibling::div[1]//*[@id='tb']/following-sibling::div[1]/div[2]/div[2]//table"
    xpath = "//*[@id='issuingCmdIframeTabletableFormatCfgDiv']/following-sibling::div[1]//*[@class='format_tab']"
    table_data_result = get_table_data(data_table_xpath=xpath)
    log.info(table_data_result)
