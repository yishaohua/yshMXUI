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

interfaces_config = "/home/qatest/mx-monitor/recommendation/pre.json"
#interfaces_config = "/home/qatest/mx-monitor/recommendation/bak.json"

_Normal = 0
_ResAbnormal = 1
_FieldAbnormal = 2
tabid = []
req = None

def generator():
    userId = "monitor_" + str(random.randint(10000,30000))
    #userId = "TQIxeTAi7pbR0NtG" 
    return userId
   
def field_check(type, result):
    common_list = ["publisher", "artist", "singer", "tv_show", "season", "album", "playlist", "short_video", "movie", "tv_show_video", "song", "live_channel", "live_programme"]
    fields = {
        #"common": ["id", "recallSign"]
        "common": ["id", "recallIdList"]
    }
    if type in common_list:
        checklist = fields["common"]
    else:
        return False

    for i in checklist:
        if hasattr(result, i):
            content = getattr(result, i)
            if content==[] or content==None:
                # print content
                return False
        else:
            return False
    return True


def monitors(reqType, reqFunc, resCheck, metric, attrDict={}):
    global req
    if reqType == "tabsRequest":
        for tab_id in tabid:
            reqType = "tabsRequest2"
            req = RecommendService.Request()
            req.tabId = tab_id
            new_metric = metric + "_" + tab_id
            monitors(reqType, reqFunc, resCheck, new_metric, attrDict)
        return

    payload = []
    ts = int(time.time())
    step = 300
    value = _Normal

    try:
        # to be optimized
        transport = TSocket.TSocket(address, 8083)
        transport.setTimeout(2000)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
    #    print "server reponse: " + msg
        
        if reqType == "offlineRequest":
            req = RecommendService.OfflineRequest()
        elif reqType == "tabsRequest2": 
            pass
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
            print res
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
            
            elif resCheck=="tabList":
                #print res
                if res==[] or len(res.tabList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    for i in range(len(res.tabList)):
                        tabid.append(res.tabList[i].tabId)
                #print tabid

            elif resCheck=="tab_cardList":
                if res==[] or res.tabList==None or len((res.tabList)[0].cardList)<attrDict.get("num", 1):
                    print len((res.tabList)[0].cardList)
                    print res
                    value = _ResAbnormal

            elif resCheck=="bannerList":
                #print res
                if res==[] or len(res.bannerList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal

            elif resCheck=="cardList":
                if res==[] or res[0].cardList==None or len(res[0].cardList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    cards = []
                    for card in res[0].cardList:
                        cards.append(card.cardName)
                    return cards
            else:
                pass
            mes ={
                "endpoint": endpoint,
                "metric": metric,
                "timestamp": ts,
                "step": step,
                "value": value,
                "counterType": "GAUGE",
                "tags": "mx-main-recommendation-interfaces",
                "logid": "13521930283"
              }
            payload.append(mes)
            print payload
            print value
            break
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    finally:
        transport.close()


if __name__ == "__main__":
   # Prod server
#    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=recommendation')
#    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    #print server_groups

    # Pre-prod server
    server_groups = [
        {
            "Node":"pre-prod",
            #"Address":"172.32.27.56"
            #pre-beta:8083,stg:8081
            "Address":"recommendation-beta.internal.mxplay.com"
            #"Address":"reco-stg.internal.mxplay.com"
        }
    ]
    #print server_groups

    with open(interfaces_config, 'r') as f:
        interface_groups = eval(f.read())
    card_names_all = []
    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]
        print address
    # for i in range(1):
       #  endpoint = "rec-1"
       #  address = "172.32.27.58"

        # Check the interfaces in config file
        card_names_server = []
        for interface_group in interface_groups:
            interfaces = interface_groups[interface_group]
            card_names_tab = []
            for interface in interfaces:
                reqType = interface.get("reqType", None)
                reqFunc = interface.get("reqFunc", None)
                resCheck = interface.get("resCheck", None)
                metric  = interface.get("metric", None)
                attrDict = interface.get("attrDict", {})
                cards = monitors(reqType, reqFunc, resCheck, metric, attrDict)
                card_names_tab.append(cards)
            card_names_server.append(card_names_tab)
        card_names_all.append(card_names_server)
    print card_names_all



