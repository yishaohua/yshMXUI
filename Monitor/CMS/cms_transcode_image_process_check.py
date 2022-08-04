import json
import os
import time
import psutil
import requests
import commands
pAliveStatus=["sleeping","running", "waiting", "disk_sleep"]

def setProcess(process_name):
    try:
        cmd="ps aux |grep '%s' |grep -v 'grep' | awk '{print $2}'" %process_name
        info = commands.getoutput(cmd)
        for i in info:
            print i
    #     PID=int(info)
    #     p = psutil.Process(PID)
    # if p.status() in pAliveStatus:
    #         return 1
    #     else:
    #         return 0
    except Exception, e:
        return 0

def main():

    ts=int(time.time())
    payload = [
        {
            "endpoint": "cms-transcode-image-01",
            "metric": "cms-transcode-image-process-check",
            "timestamp": ts,
            "step": 60,
            "value": setProcess("celery worker"),
            "counterType": "GAUGE",
            "tags":"status",
     },
    ]

    # r=requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    # print r.text
    # print payload

if __name__ == '__main__':
    main()

