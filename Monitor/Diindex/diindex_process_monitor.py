#!/usr/bin/python
#!-*- coding:utf8 -*-
import json
import os
import time
import requests
import commands
import subprocess

def getProcess(ssh_cmd):
    try:
        proc = subprocess.Popen(ssh_cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        cmdout, cmderr = proc.communicate()
        print cmdout

        if ("celery" in ssh_cmd and int(cmdout) >= 9) or ("consumer" in ssh_cmd and int(cmdout) >= 1):
            return 0
        else:
            return 1
    except Exception as e:
        return 1

def add_falcon_hosts(group_id, hosts):
    '''
    group_id: string type
    hosts: list type
    '''
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

def monitors(process,metric):
    _Normal = 0
    _Abnormal = 1

    value = _Normal
    if process == 0:
        value = _Normal
    else:
        value = _Abnormal

    ts=int(time.time())
    payload = [
        {
            "endpoint": endpoint,
            "metric": metric,
            "timestamp": ts,
            "step": 120,
            "value": value,
            "counterType": "GAUGE",
            "tags":"processNum",
        }]
    r=requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text
    print payload
    print value

if __name__ == "__main__":

    celery_cmd = "ps aux |grep celery |grep -v grep |grep -v flower |awk '{print $2}' | wc -l" 
    consumer_cmd = "ps aux |grep consumer |grep -v grep |grep -v flower |awk '{print $2}' | wc -l"
    ssh_portal = "ssh -A -q deploy@deploy.mxplay.com -t "

    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=diindex')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    print server_groups
    hosts = []

    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]
        print address

        ssh_host = "ssh -q -oStrictHostKeyChecking=no diindex@" + address + " -t "
        ssh_celery_cmd = ssh_portal + ssh_host + celery_cmd
        ssh_consumer_cmd = ssh_portal + ssh_host + consumer_cmd

        try:
            monitors(getProcess(ssh_consumer_cmd),"diindex_consumer_process")
            monitors(getProcess(ssh_celery_cmd),"diindex_celery_process")
            print "--------------------------------------------------------"
        except Exception, ex:
            print ex
            continue
        print "=========================================================="
        hosts.append(endpoint)

    print hosts
    add_falcon_hosts("83", hosts)





