# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/20 下午7:14

import json
from common.tools.updateData import update_dict


# 枚举所有典型元素配置，可在底部继续添加

crawler_element = {
    "点击按钮": {
        "元素名称": "点击按钮",
        "元素类型": "按钮",
        "动作": "单击",
        "标识类型": "xpath",
        "元素标识": "//*[@id='btn']",
        "描述": "点击按钮动作"
    },
    "输入框输入": {
        "元素名称": "输入框输入",
        "元素类型": "输入框",
        "动作": "输入",
        "标识类型": "xpath",
        "元素标识": "//*[@id='input']",
        "描述": "输入框输入动作",
        "值输入": "abc",
        "敏感信息": "是",
    },
    "文本取数": {
        "元素名称": "文本取数",
        "元素类型": "文本",
        "动作": "取数",
        "标识类型": "xpath",
        "元素标识": "//*[@id='text']",
        "描述": "文本取数动作",
        "是否配置期待值": {
            "状态": "开启",
            "期待值": "成功",
            "尝试次数": "3",
            "等待时间": "5"
        }
    },
    "表格取数": {
        "元素名称": "表格取数",
        "元素类型": "表格",
        "动作": "取数",
        "标识类型": "xpath",
        "元素标识": "//*[@id='text']",
        "描述": "表格取数动作",
        "取数模式": "追加",
        "下一页元素标识": "//*[@name='next']",
        "下一页标识类型": "xpath",
        "休眠时间": "5",
        "表格页数": "3",
        "是否配置期待值": {
            "状态": "关闭",
            "期待值": "成功",
            "尝试次数": "3",
            "等待时间": "5"
        }
    },
    "附件上传-动态生成": {
        "元素名称": "附件上传-动态生成",
        "元素类型": "输入框",
        "动作": "附件上传",
        "标识类型": "xpath",
        "元素标识": "//*[@id='filebox_file_id_2']",
        "描述": "附件上传动作",
        "附件": {
            "附件来源": "动态生成",
            "附件标题": "动态csv",
            "附件内容": "我们都是中国人",
            "附件类型": "csv"
        }
    },
    "附件上传-本地上传": {
        "元素名称": "附件上传-本地上传",
        "元素类型": "输入框",
        "动作": "附件上传",
        "标识类型": "xpath",
        "元素标识": "//*[@id='filebox_file_id_2']",
        "描述": "附件上传动作",
        "附件": {
            "附件来源": "本地上传",
            "附件名称": "factor.xlsx"
        }
    },
    "附件上传-远程加载-本地": {
        "元素名称": "附件上传-远程加载-本地",
        "元素类型": "输入框",
        "动作": "附件上传",
        "标识类型": "xpath",
        "元素标识": "//*[@id='filebox_file_id_2']",
        "描述": "附件上传动作",
        "附件": {
            "附件来源": "远程加载",
            "存储类型": "本地",
            "目录": "AI",
            "变量引用": "否",
            "文件过滤方式": "关键字",
            "文件名": "test_",
            "文件类型": "xls"
        }
    },
    "附件上传-远程加载-远程FTP": {
        "元素名称": "附件上传-远程加载-远程FTP",
        "元素类型": "输入框",
        "动作": "附件上传",
        "标识类型": "xpath",
        "元素标识": "//*[@id='filebox_file_id_2']",
        "描述": "附件上传动作",
        "附件": {
            "附件来源": "远程加载",
            "存储类型": "远程",
            "远程服务器": "pw-ftp测试",
            "目录": "AI",
            "变量引用": "否",
            "文件过滤方式": "关键字",
            "文件名": "test_",
            "文件类型": "csv"
        }
    },
    "文件下载": {
        "元素名称": "文件下载",
        "元素类型": "按钮",
        "动作": "下载",
        "标识类型": "xpath",
        "元素标识": "//a[@href=\"javascript:downloadFile('/pw/新文件.xlsx','新文件.xlsx');\"]",
        "描述": "文件下载动作",
        "下载目录": "AI"
    },
    "跳转iframe": {
        "元素名称": "跳转iframe",
        "元素类型": "Iframe",
        "动作": "跳转iframe",
        "标识类型": "xpath",
        "元素标识": "//a[@href=\"javascript:downloadFile('/pw/新文件.xlsx','新文件.xlsx');\"]",
        "描述": "跳转iframe动作"
    },
    "关闭当前窗口": {
        "元素名称": "关闭当前窗口",
        "动作": "关闭当前窗口",
        "描述": "关闭当前窗口动作"
    },
    "休眠": {
        "元素名称": "休眠",
        "动作": "休眠",
        "描述": "休眠动作",
        "循环次数": "3",
        "_休眠时间": "5",
        "刷新页面": "是"
    },
    "悬停": {
        "元素名称": "悬停",
        "元素类型": "文本",
        "动作": "悬停",
        "标识类型": "xpath",
        "元素标识": "//*[@class='title']",
        "描述": "休眠动作"
    },
    "重复步骤": {
        "元素名称": "重复步骤",
        "动作": "重复步骤",
        "描述": "重复步骤动作",
        "重复步骤": [
            "表格取数",
            "悬停",
            "点击按钮",
            "文件下载"
        ]
    },
    "form表单取数": {
        "元素名称": "form表单取数",
        "元素类型": "表单",
        "动作": "取数",
        "标识类型": "id",
        "元素标识": "login_form",
        "描述": "form表单取数",
        "取数模式": "替换",
        "是否配置期待值": {
            "状态": "开启",
            "期待值": "成功",
            "尝试次数": "3",
            "等待时间": "5"
        },
        "变量名": "form表单取数变量名"
    },
    "等待元素": {
        "元素名称": "等待元素",
        "元素类型": "文本",
        "动作": "等待元素",
        "等待元素标识类型": "id",
        "等待元素标识": "userName",
        "描述": "等待元素",
        "最大等待时间": "10",
        "期待值": "成功",
        "变量名": "等待元素变量名"
    }
}


def main():
    test = crawler_element.get("附件上传-远程加载-远程FTP")
    print("替换前：\n%s" % json.dumps(test, indent=4, ensure_ascii=False))
    test = update_dict(test, "目录", "OCR")
    print("替换后：\n%s" % json.dumps(test, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
