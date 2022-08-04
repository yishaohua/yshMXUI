#!/usr/bin/python
#!-*- coding:utf8 -*-
import json
import os
import time
import requests
import commands

def getProcess():
    try:
        cmd="ps -ef |grep sqs_consumer |grep -v grep |awk '{print $2}' | wc -l "
        info = commands.getoutput(cmd)
        print "processNum: " + info

        if int(info) >= 1:
            return 0
        else:
            return 1
    except Exception as e:
        return 1

def monitors():
    _Normal = 0
    _Abnormal = 1

    value = _Normal

    if getProcess() == 0:
        value = _Normal
    else:
        value = _Abnormal

    ts=int(time.time())
    payload = [
        {
            "endpoint": "DIRealMonitor_sqsConsumer_prod",
            "metric": "DIRealMonitor-sqsConsumer",
            "timestamp": ts,
            "step": 120,
            "value": value,
            "counterType": "GAUGE",
            "tags":"processNum",
        }]

    print payload
    print value
    r=requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text

if __name__ == '__main__':
    monitors()
