#!/usr/bin/python
# -*- coding: UTF8 -*-
import urllib
import urllib2
import json
import datetime
import time
import requests

def monitors(address):

    _Normal = 0
    _ResAbnormal = 1
   # _VersionAbnormal = 2

    value = _Normal

    ts = int(time.time())
    step = 300
    payload = []
    metric = "fairplay_spc_monitor"

    headers = {'Content-type':'application/json'}
    request_data = open("/home/qatest/mx-monitor/fairPlay/post_data").read()

    requrl = "http://" + address +":8081/fps/rest/getLicense"
    req = urllib2.Request(url = requrl, headers = headers, data = request_data)

    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read()) 
    print res

    if res == [] or res["ckc"] == None:
        value = _ResAbnormal

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
    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text


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


if __name__ == "__main__":


    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=fairplay')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    print server_groups
    hosts = []


    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]

	print address

        monitors(address)
        hosts.append(endpoint)

    print hosts
    add_falcon_hosts("36", hosts)

