#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2020-06-15 19:44 
# @Author : lmh
# @Software: PyCharm
#
import json
import requests
import time
import random
import subprocess
import os

from . import flow_test

#_Normal = 0
#_Abnormal = 1
# log文件地址
logfile = "/home/qatest/mx-monitor/flow/flow_monitor.log"
# 登录
keyfile = "/home/qatest/mx-monitor/flow/flow_monitor/mengmai.pem"
# 上报的服务器地址
remote = "ec2-user@ec2-13-126-169-27.ap-south-1.compute.amazonaws.com:/home/ec2-user/monitor_log/flow_monitor"

def save_log(logdata, logfile=logfile, keyfile=keyfile, remote=remote):
    with open(logfile, "a") as f:
        f.write("----------------------------------------\n")
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        f.write(str(logdata) + "\n")
        f.write("----------------------------------------\n")
    # cmd = "scp ult : ' + str(result)ai %s %s %s" % (keyfile, logfile, remote)
    # subprocess.call(cmd.split())

def monitor(payload):
    payload = []
    ts = int(time.time())
    step = 300
#    value = _Normal

    result = flow_test.process()
    if result != 0:
        save_log('  result : '+ str(result))
        print ('result : ' + str(result))

    mes = {
        "endpoint": "flow_mh",
        "metric": "flow_monitor_mh",
        "timestamp": ts,
        "step": step,
        "value": result,
        "counterType": "GAUGE",
        "tags": "result"
    }
    payload.append(mes)
    print ('payload : ' + str(payload))
#    print 'value : ' + str(value)
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print (r.text)


if __name__ == '__main__':
    print ("---------------------------------------------------")
    monitor()
    print ("---------------------------------------------------")

