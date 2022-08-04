#!/usr/bin/python
# -*- coding: UTF8 -*-

import urllib
import urllib2
import json
import datetime
import time
import requests

def get_data_64(address, v_type, data_vector):

    para = json.dumps(data_vector)
    requrl = "http://" + address +":4000/" + v_type + "/search"
    req = urllib2.Request(url = requrl, data = para)

    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    ids = res[0]['neighbors'][0]['id']

    data = [{"k": 10, "ids":[ids]}, {"k": 10, "vectors": [[0.5, 0.9, 0.3, 0.1, 0.8, 0.3, 0.2, 0.6, 0.3, 0.5, 0.3, 0.1, 0.3, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.2, 0.2, 0.5, 0.4, 0.7]]}]
    return data

def get_data(address, v_type, data_vector):

    para = json.dumps(data_vector)
    requrl = "http://" + address +":4000/" + v_type + "/search"
    req = urllib2.Request(url = requrl, data = para)
    
    res_data = urllib2.urlopen(req)
    res = json.loads(res_data.read())
    ids = res[0]['neighbors'][0]['id']

    data = [{"k": 10, "ids":[ids]}, {"k": 10, "vectors": [[0.7, 0.3, 0.6, 0.4, 0.1, 0.7, 0.2, 0.0, 0.6, 0.5, 0.3, 0.2, 0.1, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.7, 0.2, 0.5, 0.5, 0.7, 54.7, 0.3, 0.6, 0.4, 0.1, 0.7, 0.2, 0.0, 0.6, 0.2, 0.1, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.7, 0.2, 0.5, 0.5, 0.1,0.1,0.1]]}]
    return data

def monitors(address, v_type, data):

    _Normal = 0
    _ResAbnormal = 1
    _VersionAbnormal = 2
    _NumAbnormal = 3

    for post_para in data:
        if "dev" in v_type and "vector" in post_para:
	    tag = "dev_vector"
	elif "card" in v_type and "vector" in post_para:
	    tag = "card_vector"
	elif "ids" in post_para:
	    tag = "id"
	else:
	    tag = "vector"

        metric = "faiss_" + v_type + "_" + tag  + "_monitor"

        value = _Normal
        ts = int(time.time())
        step = 300
        payload = []

        para = json.dumps(post_para)
        requrl = "http://" + address +":4000/" + v_type + "/search"
        print requrl
        #print para
        req = urllib2.Request(url = requrl, data = para)
        res_data = urllib2.urlopen(req)
        res = json.loads(res_data.read())
        #print res

        if res == [] or res[0]['neighbors'] == None:
            value = _ResAbnormal

        elif "card" not in v_type and len(res[0]['neighbors']) < 10:
            value = _NumAbnormal

        elif tag == "id" and res[0]['id'] != None:

            version = res[0]['version'][8:14]
            print "version:" + version
            c_time = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime('%Y%m%d')[2:]

            if version < c_time:
                value = _VersionAbnormal
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

    data_vector = [{"k": 10, "vectors": [[0.7, 0.3, 0.6, 0.4, 0.1, 0.7, 0.2, 0.0, 0.6, 0.5, 0.3, 0.2, 0.1, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.7, 0.2, 0.5, 0.5, 0.7, 54.7, 0.3, 0.6, 0.4, 0.1, 0.7, 0.2, 0.0, 0.6, 0.2, 0.1, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.7, 0.2, 0.5, 0.5, 0.1,0.1,0.1]]}]

    data = [{"k": 10, "vectors": [[0.5, 0.9, 0.3, 0.1, 0.8, 0.3, 0.2, 0.6, 0.3, 0.5, 0.3, 0.1, 0.3, 0.9, 0.3, 0.6, 0.2, 0.9, 0.5, 0.0, 0.9, 0.1, 0.9, 0.1, 0.5, 0.5, 0.8, 0.8, 0.5, 0.2, 0.6, 0.2, 0.2, 0.7, 0.1, 0.7, 0.8, 0.2, 0.9, 0.0, 0.4, 0.4, 0.9, 0.0, 0.6, 0.4, 0.4, 0.6, 0.6, 0.2, 0.5, 0.0, 0.1, 0.6, 0.0, 0.0, 0.4, 0.7, 0.5, 0.2, 0.2, 0.5, 0.4, 0.7]]}]

    #case1: 9

    #64bit
    type_list1 = [
    "deepwalk/online/card/08f8fce450d1ecf00efa820f611cf57b",
    "deepwalk/online/card/4e82d34404a477419f811cd303e216e7",
    "deepwalk/online/card/5f15a7356cf9dfceeb355fc49dd2be8a",
    "deepwalk/online/card/6256019abbad655653afffa3056345a1",
    "deepwalk/online/card/72d9820f7da319cbb789a0f8e4b84e7e",
    "deepwalk/online/card/7694f56f59238654b3a6303885f9166f",
    "deepwalk/online/card/87c3ddc974dcf12294e9412bec44b097",
    "deepwalk/online/card/feacc8bb9a44e3c86e2236381f6baaf3"]
    #128bit
    '''
    type_list2 = [
    "deepwalk/online_mix/card/7694f56f59238654b3a6303885f9166f",
    "deepwalk/all/card/08f8fce450d1ecf00efa820f611cf57b",
    "deepwalk/all/card/4e82d34404a477419f811cd303e216e7",
    "deepwalk/all/card/5f15a7356cf9dfceeb355fc49dd2be8a",
    "deepwalk/all/card/6256019abbad655653afffa3056345a1" ,
    "deepwalk/all/card/72d9820f7da319cbb789a0f8e4b84e7e",
    "deepwalk/all/card/7694f56f59238654b3a6303885f9166f",
    "deepwalk/all/card/87c3ddc974dcf12294e9412bec44b097",
    "deepwalk/all/card/feacc8bb9a44e3c86e2236381f6baaf3"]
    '''

    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=faiss')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    print server_groups
    hosts = []
   

    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]

	print address
    	for v_type in type_list1:
	    monitors(address, v_type, data)
    	#for v_type in type_list2:
	#    monitors(address, v_type, data_vector)

        #case2: 13*2, total=8+13*2=34
        #64bit
        monitors(address, "research/deepwalk/online/swing/music", get_data_64(address, "research/deepwalk/online/swing/music", data[0]))
        monitors(address, "research/deepwalk/online/swing/tv_show", get_data_64(address, "research/deepwalk/online/swing/tv_show", data[0]))
        monitors(address, "research/deepwalk/online/swing/short_video", get_data_64(address, "research/deepwalk/online/swing/short_video", data[0]))
        monitors(address, "research/deepwalk/online/swing/movie", get_data_64(address, "research/deepwalk/online/swing/movie", data[0]))

        '''
        monitors(address, "euler/randomwalk/v1/publisher", get_data_64(address, "euler/randomwalk/v1/publisher", data[0]))
        monitors(address, "euler/randomwalk/v1/album", get_data_64(address, "euler/randomwalk/v1/album", data[0]))
        monitors(address, "euler/randomwalk/v1/tv_show", get_data_64(address, "euler/randomwalk/v1/tv_show", data[0]))
        '''

        monitors(address, "deepwalk/online/movie", get_data_64(address, "deepwalk/online/movie", data[0]))
        monitors(address, "deepwalk/online/music", get_data_64(address, "deepwalk/online/music", data[0]))
        monitors(address, "deepwalk/online/tv_show", get_data_64(address, "deepwalk/online/tv_show", data[0]))
        monitors(address, "deepwalk/online/short_video", get_data_64(address, "deepwalk/online/short_video", data[0]))
        monitors(address, "deepwalk/online/episode", get_data_64(address, "deepwalk/online/episode", data[0]))
        monitors(address, "deepwalk/online/season", get_data_64(address, "deepwalk/online/season", data[0]))
        monitors(address, "deepwalk/online/singer", get_data_64(address, "deepwalk/online/singer", data[0]))
        monitors(address, "deepwalk/online/publisher", get_data_64(address, "deepwalk/online/publisher", data[0]))
        monitors(address, "deepwalk/online/playlist", get_data_64(address, "deepwalk/online/playlist", data[0]))
        #128bit
        '''
        monitors(address, "deepwalk/online_mix/movie", get_data(address, "deepwalk/online_mix/movie", data_vector[0]))
        monitors(address, "deepwalk/all/movie", get_data(address, "deepwalk/all/movie", data_vector[0]))
        monitors(address, "deepwalk/all/music", get_data(address, "deepwalk/all/music", data_vector[0]))
        monitors(address, "deepwalk/all/album", get_data(address, "deepwalk/all/album", data_vector[0]))
        monitors(address, "deepwalk/all/season", get_data(address, "deepwalk/all/season", data_vector[0]))
        monitors(address, "deepwalk/all/singer", get_data(address, "deepwalk/all/singer", data_vector[0]))
        monitors(address, "deepwalk/all/publisher", get_data(address, "deepwalk/all/publisher", data_vector[0]))
        monitors(address, "deepwalk/all/playlist", get_data(address, "deepwalk/all/playlist", data_vector[0]))
        '''
        hosts.append(endpoint)

    print hosts
    add_falcon_hosts("35", hosts)
