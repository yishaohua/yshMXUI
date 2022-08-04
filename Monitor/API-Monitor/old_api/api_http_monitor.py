#!/usr/bin/python
#coding: utf-8

import sys
import time
servers_config = "/httprunner/HttpRunner/apitest/api_monitor/servers_debug.json"
#log_file = "/httprunner/HttpRunner/apitest/api_monitor/log"
import json
import requests
import time
import random
import string

class LogParser:
    def __init__(self, logPath):
        self.logPath = logPath
        self.results = []
    def parseLog(self):
        currentNode = None
        for line in open(self.logPath).read().splitlines():
            if line.startswith("qa_check_v3") and ( 16 < len(line) < 60 ):
                currentNode = None
                title = line
                for logObj in self.results:
                    if logObj["title"] == line:
                        currentNode = logObj
                        break
                if currentNode == None:
                    currentNode = {
                        "title": title,
                        "logs": [],
                    }
                    self.results.append(currentNode)
                continue

            if currentNode == None:
                continue
            if line == "." or line.strip() == "" or line.startswith("ERROR") or line.startswith("E"):
                continue
            if line.startswith("=======") or line.startswith("------"):
                continue
            if line.startswith("Ran"):
                break
            currentNode["logs"].append(line)

    def monitors(self):
        _ResAbnormal = 1
        _TypeAbnormal = 2

        _Short_youtubeAbnormal = 3
        _PublisherAbnormal = 4
        _SingerAbnormal = 5
        _Mv_youtubeAbnormal = 6
        _Tv_youtubeAbnormal = 7
        _TvshowAbnormal = 8

        _SeasonTabAbnormal = 10
        _VideoAbnormal = 11
        _UaInfoAbnormal = 12

        _ConfigAbnormal = 9

        _Normal = 0
        ts = int(time.time())
        step = 300

        for logObj in self.results:
            metric = logObj["title"]
            logs = logObj["logs"]

            value = _Normal
            payload = []
            isOk = True
            errorMsg = "ERROR"

            for line in logs:
                if not line.startswith("INFO"):
                    isOk = False

                    if "check item name" in line:
                        errorMsg = line.split(":")[1]
                        if "type" in errorMsg:
                            value = _TypeAbnormal
                        #no resource,the second level
                        elif "uaInfo" in errorMsg:
                            value = _UaInfoAbnormal
                        elif "video" in errorMsg:
                            value = _VideoAbnormal
                        elif "seasonTab" in errorMsg:
                            value = _SeasonTabAbnormal
                        #have resources,the third level
                        elif "v_short_youtube" in errorMsg:
                            value = _Short_youtubeAbnormal
                        elif "v_mv_youtube" in errorMsg:
                            value = _Mv_youtubeAbnormal
                        elif "v_tv_youtube" in errorMsg:
                            value = _Tv_youtubeAbnormal
                        elif "tvshow" in errorMsg:
                            value = _TvshowAbnormal
                        elif "publisher" in errorMsg:
                            value = _PublisherAbnormal
                        elif "singer" in errorMsg:
                            value = _SingerAbnormal
                        else:
                            value = _ResAbnormal
                    elif ("ParseResponseError" in line ) or ("UnicodeEncodeError" in line) or ("ParamsError" in line):
                        value = _ConfigAbnormal
                else:
                    pass
            mes = {
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
            #requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

if __name__ == "__main__":
    with open(servers_config, 'r') as f:
        server_groups = eval(f.read())

    for server_group in server_groups:
        servers = server_groups[server_group]
        for server in servers:
            endpoint = server.get("endpoint", None)
            address = server.get("address", None)
            #logParser = LogParser(log_file)
            logParser = LogParser(sys.argv[1])
            logParser.parseLog()
            logParser.monitors()
