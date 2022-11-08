# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2022/8/25 下午3:37

import socket


def getLocalAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.shutdown(2)
    s.close()
    return ip


if __name__ == "__main__":
    local_ip = getLocalAddress()
    print(type(local_ip))
    print(local_ip)


