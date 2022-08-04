# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Time : 2019-06-03 16:58
# # @Author : lmh
# # @Software: PyCharm
# #
# import time
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from conf.config import report_recivers
#
# def send_email(file_name,file_dir=None):
#
#     senddate=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#     # 设置发件服务器地址
#     host = 'smtp.163.com'
#     # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
#     port = 465
#     # 设置发件邮箱，一定要自己注册的邮箱
#     sender = 'mxplayertest@163.com'
#     # 设置发件邮箱的密码，163邮箱的授权码，等会登陆会用到
#     pwd = 'mxplay666'
#
#     # 设置邮件接收人,是一个字符串,多个收件人逗号隔开
#     receivers = report_recivers
#     # 设置邮件正文，这里是支持HTML的
#     body = '<h1>'+senddate+'</h1><p>recommendAPI测试报告,详情见附件html文件,附件可能加载稍慢,请稍等</p>'
#     # 设置正文为符合邮件格式的HTML内容
#     msg = MIMEText(body, 'html')
#     message = MIMEMultipart()
#     # 设置邮件标题
#     message['subject'] = 'recommendAPI测试报告'
#     # 设置发送人
#     message['from'] = sender
#     # 设置接收人'
#     message['to'] = receivers
#     message.attach(msg)
#
#     if not file_dir:
#         filename = file_name
#     else:
#         filename = os.path.join(file_dir,file_name)
#
#     # 构造附件1，传送当前目录下的 filename 文件
#     att1 = MIMEText(open(filename, 'r').read())
#     att1["Content-Type"] = 'Content-Disposition'
#     # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#     att1["Content-Disposition"] = 'attachment; filename='+ file_name +''
#     message.attach(att1)
#
#     try:
#         s = smtplib.SMTP_SSL(host, port)  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
#         s.login(sender, pwd)  # 登陆邮箱
#         s.sendmail(sender, [receivers], message.as_string())
#         print ('Done.sent email success')
#     except smtplib.SMTPException:
#         print ('Error.sent email fail')
#
