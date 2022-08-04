#!/usr/bin/env python

import sys
import datetime
sys.path.append('/home/qatest/mx-monitor/recommendation/gen-py')
import json
import requests
import time
import random
import string
import re
from recommend import RecommendService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

interfaces_config = "/home/qatest/mx-monitor/recommendation/interfaces_main_recommendation.json"

_Normal = 0
_ResAbnormal = 1
_FieldAbnormal = 2
_LenthAbnormal = 3

def generator():
    userId = "monitor_" + str(random.randint(10000,30000))
    return userId

def field_check(type, result):
    common_list = ["publisher", "artist", "singer", "tv_show", "season", "album", "playlist", "short_video", "movie", "tv_show_video", "song", "live_channel", "live_programme"]
    fields = {
        "common": ["id", "recallSign"]
    }
    if type in common_list:
        checklist = fields["common"]
    else:
        return False

    for i in checklist:
        if hasattr(result, i):
            content = getattr(result, i)
            if content==[] or content==None:
                # print i
                # print content
                return False
        else:
            # print i
            return False
    return True

def monitors(reqType,reqFunc, resCheck, lenthCheck, metric, attrDict={}):
    payload = []
    ts = int(time.time())
    step = 300

    value = _Normal
    try:
        # to be optimized
        transport = TSocket.TSocket(address, 8081)
        transport.setTimeout(1000)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print "server reponse: " + msg

        if reqType == "offlineRequest":
            req = RecommendService.OfflineRequest()
        else:
            req = RecommendService.Request()

        for attr in attrDict:
            setattr(req, attr, attrDict[attr])
        if "userId" not in attrDict.keys():
            req.userId = generator()
        if "envOption" not in attrDict.keys():
            req.envOption = "prod"

        print req

        while 1 :
            if reqFunc == "recommend":
                res = client.recommend(req)
            elif reqFunc == "offlineRecommend":
                res = client.offlineRecommend(req)
            elif reqFunc == "fetchTab":
                res = client.fetchTab(req)
            elif reqFunc == "fetchBanner":
                res = client.fetchBanner(req)
            else:
                res = ""
            print len(str(res))
            
            if len(str(res))>lenthCheck:
                value = _LenthAbnormal

            if resCheck=="result":
                if res==[] or res.resultList==None or len(res.resultList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    for result in res.resultList:
                        #print result
                        if hasattr(result, "resultType"):
                            if field_check(getattr(result, "resultType"), result)==False:
                                print result
                                value = _FieldAbnormal

            elif resCheck=="offlineResultList":
                if res==[] or res.offlineResultList==None or len(res.offlineResultList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal

            elif resCheck=="tab_cardList":
                if res==[] or res.tabList==None or len((res.tabList)[0].cardList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal

            elif resCheck=="tabList":
                if res==[] or len(res.tabList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal

            elif resCheck=="bannerList":
                if res==[] or len(res.bannerList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal

            elif resCheck=="cardList":
                if res==[] or res[0].cardList==None or len(res[0].cardList)<attrDict.get("num", 1):
                    print res
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
                "tags": "mx-main-recommendation-interfaces"
              }
            payload.append(mes)
            print payload
            print value
            headers = {
                'Connection': 'close',
            }
            r = requests.post("http://127.0.0.1:1988/v1/push", headers=headers, data=json.dumps(payload))
            print r.text
            break
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    finally:
        transport.close()

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

    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=recommendation')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    print server_groups
    hosts = []

    with open(interfaces_config, 'r') as f:
        interface_groups = eval(f.read())

    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]

        # Check the interfaces in config file
        for interface_group in interface_groups:
            interfaces = interface_groups[interface_group]
            
            try:
                for interface in interfaces:
                    reqType = interface.get("reqType", None)
                    reqFunc = interface.get("reqFunc", None)
                    resCheck = interface.get("resCheck", None)
                    lenthCheck = interface.get("lenthCheck", None)
                    metric  = interface.get("metric", None)
                    attrDict = interface.get("attrDict", {})
                    monitors(reqType, reqFunc, resCheck, lenthCheck, metric, attrDict)
                    print "--------------------------------------------------------"
            except Exception, ex:
                print ex
                continue
        print "=========================================================="
        hosts.append(endpoint)

    print hosts
    add_falcon_hosts("27", hosts)

