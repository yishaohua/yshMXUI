#!/usr/bin/python
# -*- coding: UTF8 -*-

import time
import datetime
import os
import json
import requests

#servers_config = "/httprunner/HttpRunner/apitest/api_monitor/servers_debug.json"
#filePath = "/tmp/testlog"
servers_config = "/home/ec2-user/tensorflow_serving/monitor/servers_debug.json"
filePath = "/home/ec2-user/tensorflow_serving/log/tensorflow.log"


def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    return fsize

def monitors():
    _LogAbnormal = 1
    _Normal = 0
    metric = "check_loginfo"

    while 1:
        now_hours = time.strftime( '%Y-%m-%d %X', time.localtime() )[-8:-6]
        #print now_hours 

        if ( 0 <= int(now_hours) <= 20 ):
            payload = []
            ts = int(time.time())
            step = 120
            value = _Normal
    
            fileSize1 = get_FileSize(filePath)
            time.sleep(10)
            fileSize2 = get_FileSize(filePath)
        
            print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            if fileSize2 <= fileSize1:
                value = _LogAbnormal
            else:
                pass 

            mes ={
                "endpoint": endpoint,
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
            r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        else:
            break

if __name__ == "__main__":

   with open(servers_config, 'r') as f:
        server_groups = eval(f.read())

   for server_group in server_groups:
        servers = server_groups[server_group]
        for server in servers:
            endpoint = server.get("endpoint", None)
            monitors()
