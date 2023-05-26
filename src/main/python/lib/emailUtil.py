# -*- encoding: utf-8 -*-
# @Author: peng wei
# @Time: 2021/7/19 下午9:08

import html
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import traceback


def send_email(sender, receivers, body, subject):
    # 第三方 SMTP 服务
    SMTP_host = "smtp-ent.21cn.com"
    mail_user = "pw@henghaodata.com"
    mail_pass = "P!w0401030990"

    message = MIMEMultipart('alternative')

    # 正文
    msg_body = html.escape(body)
    message_html = f'<html><body><pre>{msg_body}</pre></body></html>'
    msg_part = MIMEText(message_html, 'html')
    message.attach(msg_part)

    # 显示发件人
    message['From'] = formataddr(parseaddr(sender))

    # 显示收件人
    message['To'] = formataddr(parseaddr(';'.join(receivers)))

    # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')

    # 发送
    smtpObj = smtplib.SMTP()
    try:
        smtpObj.connect(SMTP_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        traceback.print_exc()
    finally:
        smtpObj.quit()


if __name__ == "__main__":
    sender = 'pw@henghaodata.com'
    receivers = ['pw@henghaodata.com']

    # message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    data = {'Column A': ['Some value', 'Some value2', 'Some value3'],
            'Column B': ['Some value', 'Some value2', 'Some value3'],
            'Column C': ['Some value', 'Some value2', 'Some value3']
            }
    df = pd.DataFrame(data, columns=['Column A', 'Column B', 'Column C'])
    body_msg = f"Dear User, Below are KPI detail:\n\n{df.to_string()}"
    subject = 'Python SMTP 邮件测试'
    send_email(sender, receivers, body_msg, subject)




