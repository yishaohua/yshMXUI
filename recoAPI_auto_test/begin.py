#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-05-07 18:52 
# @Author : lmh
# @Software: PyCharm
#
import unittest
from zz_other import BeautifulReport
#import BeautifulReport
from util import commonkit
from util import smtp_email
from conf.config import *

if __name__ == '__main__':

    # 删除旧的测试报告
    commonkit.deletefiles(reportdir,extension='html')
    commonkit.deletefiles(responsedir, extension='txt')

    # 限制logs目录下,日志文件的数量
    commonkit.files_num_limit(limitnum=4, dirpath=All_logs_dir, extension='log')
    commonkit.files_num_limit(limitnum=4, dirpath=Error_logs_dir, extension='log')

    test_suite = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')

    # 生成测试报告,则打开此注释
    result = BeautifulReport.BeautifulReport(test_suite)
    result.report(filename=reportname, description='recoAPI auto test report', report_path=reportdir)

    # 本地调试时,则打开此注释
    # runner = unittest.TextTestRunner()
    # runner.run(test_suite)

    # 邮件发送测试报告
    # smtp_email.send_email(reportname, reportdir)
