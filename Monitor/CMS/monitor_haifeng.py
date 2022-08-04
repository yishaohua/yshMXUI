#!/usr/bin/python
#!-*- coding:utf8 -*-
import json
import os
import time
import psutil
import requests
import commands

def getResult(url):
    try:
        r = requests.get(url)
        print r.status_code
        if str(r.status_code).startswith("4") or str(r.status_code).startswith("5"):
            return 1
        else:
            return 0
    except Exception, e:
        return 1

def main():

    ts=int(time.time())
    payload = [
        {
            "endpoint": "cmsdev",
            "metric": "cmsdev_batch_import",
            "timestamp": ts,
            "step": 120,
            "value": getResult("http://bi.zenmxapps.com/"),
            "counterType": "GAUGE",
            "tags":"status",
     },
    ]

    r=requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text
    print payload
if __name__ == '__main__':
    main()