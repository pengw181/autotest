import time
import os
from config.loads import properties
from service.lib.tools.formatPath import struct_path


def screenShot(browser):
    pic_path = properties.get("screenImagePath")
    pic_suffix = properties.get("screenImageSuffix")
    img_path = os.path.dirname(os.path.abspath(__file__)) + '/..' + pic_path
    img_path = struct_path(img_path)
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    time_str = time.strftime("%Y-%m-%d_%H-%M-%S")
    img_name = time_str + pic_suffix
    img = '%s%s' % (img_path, img_name)
    # browser.get_screenshot_as_file(img)  # 图片保存在定义路径中
    print("screenshot:%s" % img_name)        # 一定要打印出来，且输入格式不能随便改，报表获取图片地址需要解析
    return img_name
