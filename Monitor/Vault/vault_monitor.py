#!/usr/bin/python
# -*- coding: UTF8 -*-
import urllib
import urllib2
import json
import datetime
import time
import requests

def monitors(url_path,request_data):

    _Normal = 0
    _ResAbnormal = 1
    ttl_len = 432000

    value = _Normal

    ts = int(time.time())
    step = 300
    payload = []
    metric = "vault_monitor_" + url_path 

    urls = "http://vault.mxplay.com:8200/v1/auth/token/renew-self"
    datas = "{\"increment\": \"7200h\"}"
    
    requrl = "http://vault.internal.mxplay.com:8200/v1/" + url_path 
    headers = {'X-Vault-Token':'s.ameD56zXqsDunQVTuXN3V8Wd','Content-type':'application/json'}

    if url_path == "mx_reco_v2/data/india_ab_test_range":
        headers = {'X-Vault-Token':'s.cLGVA6K64Jq4DYvhyknN7wF4'}
        req = urllib2.Request(url = requrl, headers = headers)

        res_data = urllib2.urlopen(req)
        res = json.loads(res_data.read()) 
        #print res['data']['data']
        if res == [] or res['data']['data'] != None:
            value = _ResAbnormal

    elif url_path == "auth/token/lookup" and request_data == "{\"token\": \"s.ameD56zXqsDunQVTuXN3V8Wd\"}":

        metric = metric + "_s.ameD56zXqsDunQVTuXN3V8Wd"

        req = urllib2.Request(url = requrl, headers = headers, data = request_data)
        res_data = urllib2.urlopen(req)
        res = json.loads(res_data.read()) 
        #print str(res['data']['ttl'])

        if res['data']['ttl'] < ttl_len:
            req = urllib2.Request(url = urls, headers = headers, data = datas)
            req = urllib2.Request(url = requrl, headers = headers, data = request_data)
            res_data = urllib2.urlopen(req)
            res = json.loads(res_data.read()) 

            if res['data']['ttl'] < ttl_len:
                value = _ResAbnormal
                print res['data']['ttl']
        
    elif url_path == "auth/token/lookup" and request_data == "{\"token\": \"s.cLGVA6K64Jq4DYvhyknN7wF4\"}":

        metric = metric + "_s.cLGVA6K64Jq4DYvhyknN7wF4"

        req = urllib2.Request(url = requrl, headers = headers, data = request_data)
        res_data = urllib2.urlopen(req)
        res = json.loads(res_data.read()) 
        #print str(res['data']['ttl'])

        if res['data']['ttl'] < ttl_len:
            headerss = {'X-Vault-Token':'s.cLGVA6K64Jq4DYvhyknN7wF4','Content-type':'application/json'}
            req = urllib2.Request(url = urls, headers = headerss, data = datas)
            req = urllib2.Request(url = requrl, headers = headers, data = request_data)
            res_data = urllib2.urlopen(req)
            res = json.loads(res_data.read()) 

            if res['data']['ttl'] < ttl_len:
                value = _ResAbnormal
                print res['data']['ttl']
        
    elif url_path == "mx_reco_v2/data/india_user_flow":
        headers = {'X-Vault-Token':'s.cLGVA6K64Jq4DYvhyknN7wF4'}
        req = urllib2.Request(url = requrl, headers = headers)

        res_data = urllib2.urlopen(req)
        res = json.loads(res_data.read()) 
        #print res['data']['data']
        if res == [] or res['data']['data'] == None:
            value = _ResAbnormal
    else:
        pass

    mes ={
        "endpoint": "vault",
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
    monitors("mx_reco_v2/data/india_ab_test_range","")
    monitors("auth/token/lookup","{\"token\": \"s.ameD56zXqsDunQVTuXN3V8Wd\"}")
    monitors("auth/token/lookup","{\"token\": \"s.cLGVA6K64Jq4DYvhyknN7wF4\"}")
    monitors("mx_reco_v2/data/india_user_flow","")
