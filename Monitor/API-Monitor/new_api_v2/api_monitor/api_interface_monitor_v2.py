#!/usr/bin/python
#coding: utf-8

import sys
import time
import requests
import re
import linecache
import json
import os
import commands
ips_file = "/home/qatest/mx-monitor/androidapi_test/api_monitor/ips_config" 
log_file = "/home/qatest/mx-monitor/androidapi_test/api_monitor/my_log.log"
log_path = "/home/qatest/mx-monitor/androidapi_test/api_monitor/"
case_file = "/home/qatest/mx-monitor/androidapi_test/testcase/case.json"

def get_machines():
    ip_list = []
    ip_list2 = []
    lines = []

    os.remove(ips_file)
    for files in os.listdir(log_path + "logfile"):
        os.remove(log_path + "logfile/" + files)


    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=androidapi')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))

    for server in server_groups:
        ip_address = server["Address"]
        endpoint = server["Node"]
        open(ips_file,'a').write(str(ip_address.replace('\'','\"')) + ' ' + endpoint + '\n')

    with open(ips_file,'r') as f:
        for line in f.readlines():
            ip_v = line.split()[0]
            ip_list.append( ip_v )
        ip_list2 = "[%s]" % ",".join(map(lambda e: '"%s"' % e, ip_list))

    ips = "             {\"ip\": " + str(ip_list2) + "}" + '\n'
    f = open(case_file,'r')
    for line in f:
        if line.startswith("             {\"ip\":"):
            continue
        lines.append(line)
    f.close()
    lines.insert(4,ips)
    s = ''.join(lines)
    f = open(case_file,'w+')
    f.write(s)
    f.close()

def get_log():

    output = commands.getoutput('hrun /home/qatest/mx-monitor/androidapi_test/testcase/case.json')
    open(log_file, 'w').write(output + '\n')

    source_file = log_file    
    fp = open(source_file, 'r')
 
    number =[]
    lineNumber = 1
    keyword = "Ran"
    outfilename = log_path + "logfile/" + "out"
 
    for eachLine in fp:       
        m = re.search(keyword, eachLine)
        if m is not None:
           number.append(lineNumber) 
        lineNumber = lineNumber + 1
    
    size = int(len(number))

    for i in range(0,size-1):
	if i == 0:
    	    line0 = linecache.getlines(source_file)[0:number[0]]
            fp_w = open(outfilename + str(i)+'.txt','w') 
	    for key in line0:
                fp_w.write(key)
            fp_w.close()
	
        start = number[i]
        end = number[i+1]
        destLines = linecache.getlines(source_file)[start:end] 
        fp_w = open(outfilename + str(i+1)+'.txt','w') 
        for key in destLines:
            fp_w.write(key)
        fp_w.close()

def add_falcon_hosts(group_id):
    '''
    group_id: string type
    hosts: list type
    '''
    hosts = []
    with open(ips_file,'r') as f:
        for line in f.readlines():
            hosts_v = line.split()[1]
            hosts.append( hosts_v )
    print hosts
    url_login = "http://ec2-35-154-68-167.ap-south-1.compute.amazonaws.com:1234/auth/login"
    url_addhosts = "http://ec2-35-154-68-167.ap-south-1.compute.amazonaws.com:5050/host/add"
    
    data_login = {
        "name": "xuxin",
        "password": "123456"
        }

    data_addhosts = {
        "group_id": group_id,
        "hosts": "\n".join(hosts)
        }

    s = requests.session()
    r1 = s.post(url_login, data=data_login)
    c = requests.cookies.RequestsCookieJar()
    c.set('cookie-name', 'cookie-value')
    s.cookies.update(c)
    cookies = s.cookies.get_dict()
    r2 = requests.post(url_addhosts, data=data_addhosts, cookies=cookies)
    print eval(r2.text)["data"]

class LogParser:
    def __init__(self, logPath):
        self.logPath = logPath
        self.results = []
    def parseLog(self):
        currentNode = None
        for line in open(self.logPath).read().splitlines():
            if line.startswith("INFO     Start to run testcase: 172"):
                address = (line.split(":")[1]).strip()
            if line.startswith("v1_"):
                currentNode = None
                title = line
		for logObj in self.results:
                    if logObj["title"] == line:
                        currentNode = logObj
                        break
                if currentNode == None:
                    currentNode = {
                        "address":address,
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
        step = 300

        for logObj in self.results: 
            metric = logObj["title"]
            logs = logObj["logs"]
	    ip = logObj["address"]
            for line in open(log_path + "ips_config").read().splitlines():
	        if ip in line:
		    endpoint = line.split()[1]
                    break
		else:
		    endpoint = "new-_machine"
            
            value = _Normal
            payload = []
            isOk = True
            errorMsg = "FAIL"

            for line in logs:
                if not line.startswith("INFO"):
                    isOk = False
   
                    if "AssertionError: validate:" in line:
                        errorMsg = line.split(":")[2]
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
                    elif ("ParseResponseError" in line ) or ("Failed to extract" in line ) or ("UnicodeEncodeError" in line) or ("ParamsError" in line):
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
    get_machines()
    get_log()

    file_dir = log_path + "logfile/"
    for files in os.listdir(file_dir):
        log_file = file_dir + files
    	logParser = LogParser(log_file)     
   	logParser.parseLog()
  	logParser.monitors()
    
    add_falcon_hosts(30)
