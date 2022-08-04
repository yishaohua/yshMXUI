#!/usr/bin/python
# -*- coding: UTF8 -*-
import datetime
import time
import json
import requests
import redis

def monitor(queue, num, metric):

    _Normal = 0
    _Abnormal = 1

    value = _Normal

    ts = int(time.time())
    step = 60
    payload = []
 
    if queue > num :
        value = _Abnormal 
    else:
        pass

    mes ={
        "endpoint": "diindex-redis.internal.mxplay.com",
        "metric": metric,
        "timestamp": ts,
        "step": step,
        "value": value,
        "counterType": "GAUGE",
        "tags": "result"
      }
    payload.append(mes)
    print payload
    print value
    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text

if __name__ == "__main__":

    r = redis.Redis(host='diindex-redis.internal.mxplay.com', port=6379)

    artificial = r.llen('artificial_task_queue')
    script = r.llen('script_task_queue')
    
    monitor(artificial,50,"diindex_redis_artificial_task_queue")
    monitor(script,500,"diindex_redis_script_task_queue")
