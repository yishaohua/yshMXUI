#!/usr/bin/python
#!-*- coding:utf8 -*-
import json
import time
import requests

def get_result(url):
    try:
        r = requests.get(url)
        if eval(r.text)["errno"]=="200":
            return 0
        else:
            return 1
    except Exception, e:
        return 1

def upload_result(metric, result):
    ts=int(time.time())
    payload = [
        {
            "endpoint": "betaserver00",
            "metric": metric,
            "timestamp": ts,
            "step": 120,
            "value": result,
            "counterType": "GAUGE",
            "tags":"status",
     },
    ]
    # r=requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    # print r.text
    print payload

if __name__ == '__main__':
    upload_result("mx_cms_api_dev", get_result("http://ec2-13-124-180-167.ap-northeast-2.compute.amazonaws.com/mx_cms_api/operation/health"))
    upload_result("mx_cms_api_release", get_result("http://cms.zenmxapps.com/mx_cms_api/operation/health"))