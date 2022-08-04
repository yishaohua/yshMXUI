#!/usr/bin/python
#coding: utf-8

import sys
import time
import commands
servers_config = "/Users/ling.liu/Documents/httprunner/HttpRunner/tests/data/apidata/httprunner_monitor/servers_debug.json"
log_file = "/Users/ling.liu/Documents/httprunner/HttpRunner/newapitest/api_monitor/my_log.log"

def get_log():
    output = commands.getoutput('hrun /Users/ling.liu/Documents/httprunner/HttpRunner/newapitest/testcase/case_online')
    open('my_log.log', 'w').write(output + '\n')

class LogParser:
    def __init__(self, logPath):
        self.logPath = logPath
        self.results = []
    def parseLog(self):
        currentNode = None
        for line in open(self.logPath).read().splitlines():
            if line.startswith("v1_"):
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
        _profileTypeAbnormal = 2
        _ProfileAbnormal = 3
        _relatesCardsTypeAbnormal = 4
        _relatedCardsAbnormal = 5
        _redirectVideoAbnormal = 6
        _profilePublisherAbnormal = 7
        _relatedCardsPublisherAbnormal = 8
        #no response
        _NodataAbnormal = 9

        _Normal = 0
        ts = int(time.time())
        step = 120

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
                        if "profile.type" in errorMsg:
                            value = _profileTypeAbnormal 
                        elif "profile.publisher" in errorMsg:
                            value = _profilePublisherAbnormal 
                        elif "profile" in errorMsg:
                            value = _ProfileAbnormal 
                        elif "relatedCards.0.type" or "relatedCards.0.resources.0.type" or "relatedCards.0.resources.0.resources.0.type" in errorMsg:
                            value = _relatesCardsTypeAbnormal 
                        elif "relatedCards.0.resources.0.resources.0.publisher" in errorMsg:
                            value = _relatedCardsPublisherAbnormal 
                        elif "relatedCards" in errorMsg:
                            value = _relatedCardsAbnormal 
                        elif "redirectVideo.type" in errorMsg:
                            value = _redirectVideoAbnormal 
                        else:
                            value = _ResAbnormal                
                    elif ("ParseResponseError" in line ) or ("UnicodeEncodeError" in line) or ("ParamsError" in line):
                        value = _NodataAbnormal
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

if __name__ == "__main__":
    get_log()

    with open(servers_config, 'r') as f:
        server_groups = eval(f.read())

    for server_group in server_groups:
        servers = server_groups[server_group]
        for server in servers:
            endpoint = server.get("endpoint", None)
            address = server.get("address", None)
            
            logParser = LogParser(log_file)
            logParser.parseLog()
            logParser.monitors()
