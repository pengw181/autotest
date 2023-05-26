import sys
from time import sleep


def read_file(path, filename, sleep_time=0):
    sleep_time = int(sleep_time)
    if sleep_time < 0:
        sleep_time = 0
    if sleep_time > 0:
        sleep(sleep_time)
    if not path.endswith("/"):
        path += "/"
    path = path + filename
    with open(path, mode="r") as f:
        for line in f.readlines():
            print(line)


if __name__ == "__main__":
    p = sys.argv[1]
    n = sys.argv[2]
    s = sys.argv[3]
    read_file(p, n, s)