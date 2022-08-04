#!/usr/bin/python
# -*- coding: UTF8 -*-
import json
import datetime
import time
import requests
import os

file_p="/home/qatest/mx-monitor/faiss/monitor.log"

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


def monitor(lines,endpoint):

    _Normal = 0
    _ServiceAbnormal = 4

    value = _Normal
    ts = int(time.time())
    step = 300
    payload = []

    if len(lines) < 158 :
        value = _ServiceAbnormal
        err_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        with open( file_p ) as file_r:
            contents = file_r.read()
        with open( '/home/qatest/mx-monitor/faiss/server_error.log', 'a') as file_w:
            file_w.write( "****************" )
            file_w.write( err_time )
            file_w.write( "****************" )
            file_w.write( contents )
            file_w.write( '\n' * 2 )
    else:
        pass

    mes ={
    "endpoint": endpoint,
    "metric": "faiss_service",
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

    hosts = []

    lines = open(file_p, 'r' ).readlines()
    for line in lines:
        endpoint = "faiss-spot-" +  (lines[1].strip()).split(".")[3]
    print endpoint
    
    hosts.append(endpoint)

    monitor(lines,endpoint)
    add_falcon_hosts("35", hosts)
