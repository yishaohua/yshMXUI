#!/usr/bin/python
# -*- coding: UTF8 -*-
import sys
import time
import datetime
import os
import subprocess
import shutil
import json
import requests

servers_config = "/home/ec2-user/falcon-agent-monitor/monitor_scripts/servers_debug.json"
file_path = "/home/ec2-user/falcon-agent-monitor/monitor_scripts/"
log_file = "/home/ec2-user/MXCMS/log/uwsgi/uwsgi.log"
new_file = file_path + "check_date"

def monitors():
    _LogAbnormal = 1
    _Normal = 0
    value = _Normal
    metric = "cms_loginfo"
    ts = int(time.time())
    step = 120
    payload = []

    #If you empty log_file, you need to delete:monitor_last_line.test
    line_num = 0
    last_line_file = file_path + "monitor_last_line.test"
    if (datetime.datetime.now().hour == 0) and (2 <= datetime.datetime.now().minute < 4):
        #shutil.copy(last_line_file, new_file)
        os.remove(last_line_file)

    if os.path.exists(last_line_file):
        content = open(last_line_file).read().strip()
        line_num = int(content)  

    lines = open(log_file).read().splitlines()
    lines = lines[line_num:]

    error_block = []
    found_error_line = False
    line_nu = -1
    for (line_nu, line) in enumerate(lines): 
        if found_error_line == False:
            if line.startswith("ERROR") or ( line.startswith("2019-") and "ERROR" in line ):
                found_error_line = True

        if found_error_line == True and ( line.startswith("[pid:") or line.startswith("DEBUG") ):
            found_error_line = False

        if found_error_line == True:
            error_block.append(line + '\n') 

    if error_block != []:
        value = _LogAbnormal
        error_block.append('\n' + "**************************" + '\n' + '\n')

    if line_nu == -1:
        last_line = line_num
    else:
        last_line = line_num + line_nu + 1

    open(last_line_file, "w").write(str(last_line))
    open(file_path + "each.log",'w').writelines(error_block)

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
    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))


if __name__ == "__main__":

    with open(servers_config, 'r') as f:
        server_groups = eval(f.read())

    for server_group in server_groups:
        servers = server_groups[server_group]
        for server in servers:
            endpoint = server.get("endpoint", None)
            monitors()
