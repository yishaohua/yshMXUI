#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-05-17 16:56 
# @Author : lmh
# @Software: PyCharm
#
import os
import time
import sys

# 收件人,多个收件人以逗号隔开
report_recivers = 'menghua.li@mxplayer.in'

env = sys.argv[1]
#env = 'release'

host_ad_debug = 'androidapi.dev.mxplay.com'
host_ad_pre = 'androidapi-beta.mxplay.com'
host_ad_release = 'androidapi.mxplay.com'

host_beta_debug = 'androidapi-beta.dev.mxplay.com'
host_beta_pre = 'androidapi-beta.mxplay.com'
host_beta_release = 'androidapi.mxplay.com'

# 测试报告中显示的响应结果的最大结果长度,0为不限制长度
result_length = 300

# 家目录
home = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据路径
excel_path = os.path.join(home,'data/RECOcase.xlsx')
sheet_release = 'release'
sheet_config = 'config'

# testcase路径
case_path = os.path.join(home,'testcase')

# 测试报告路径
reportdir = os.path.join(home,'result/report/')
responsedir = os.path.join(home,'result/response/')
reportname =  'recoAPI_' + str(time.strftime('%Y%m%d%H%M%S',time.localtime()))+'.html'
reportpath = os.path.join(reportdir,reportname)

responsedir = os.path.join(home,'result/response/')
# 测试结果excel表路径
# excel_result_dir = os.path.join(home,'result/excelresult/')
# excel_result_path = os.path.join(home,'result/excelresult/result.xlsx')

# 错误日志存放路径
Error_logs_dir = os.path.join(home, 'logs/Error_logs/')

# 所有日志存放路径
All_logs_dir = os.path.join(home, 'logs/All_logs/')

header_ad_release = {
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.9.1',
    'x-app-version': '1310001155',
    'x-av-code': '23',
    'x-client-id': '15b8168f-539a-4882-ac96-4e8664027cec3721852',
    'x-country': 'US',
    'x-density': '3.0',
    'x-district': 'india',
    'x-lang': 'en',
    'x-mcc': '404',
    'x-platform': 'android',
    'x-resolution': '1080x1920'}
header_ad_pre = header_ad_release
header_ad_debug = {}

header_beta_release =  {
    'x-country' : 'CN',
    'x-lang' : 'zh',
    'x-app-version' : '9999999999'	,
    'x-client-id' : 'mxPlayerAutomateTest_hh'	,
    'x-av-code' : '23'	,
    'x-platform' : 'android'	,
    'x-density'	: '3.0',
    'x-resolution' : '1080x1920',
    'x-packagename' : 'com.mxtech.videoplayer.beta',
    'x-app-mode' : 'normal'	,
    'x-debug-country' : 'IND'	,
    'x-architecture' : 'armeabi-v7a',
    'accept-encoding' : 'gzip'	,
    'user-agent' : 'okhttp/3.10.0',
    'X-Mcc': '310',}
header_beta_pre = header_beta_release
header_beta_debug = {}

