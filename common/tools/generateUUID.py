# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/12 下午4:13

import uuid


def getUUID():
    return str(uuid.uuid4()).lower()


if __name__ == "__main__":
    print(getUUID())
