#!/usr/bin/env python

import sys
import datetime
# sys.path.append('/mx-beta-falcon/monitor_scrpit/client_check/gen-py')
sys.path.append('/Users/xin.xu/Documents/AutoTest/monitor/thrift-newbeta/gen-py') 
# sys.path.append('/mx-beta-falcon/monitor_scrpit/client_check/interfaces_v5.json')
import json
import requests
import time
import random
import string
from recommend import RecommendService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

# interfaces_config = "/mx-beta-falcon/monitor_scrpit/client_check/interfaces_v5_test.json"
# servers_config = "/mx-beta-falcon/monitor_scrpit/client_check/servers_debug.json"

interfaces_config = "/Users/xin.xu/Documents/AutoTest/monitor/recommendation-monitor-newbeta/interfaces_mx_main_debug.json"
servers_config = "/Users/xin.xu/Documents/AutoTest/monitor/recommendation-monitor-newbeta/servers_debug.json"

_Normal = 0
_ResAbnormal = 1
_FieldAbnormal = 2

def generator():
    userId = "test_" + str(random.randint(10000,30000))
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
                print i
                print content
                return False
        else:
            print i
            return False
    return True

def get_tab_cards(tabId, metric):
    payload = []
    ts = int(time.time())
    step = 120
    value = _Normal

    try:
        # to be optimized
        transport = TSocket.TSocket(address, 8081)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print "server reponse: " + msg
        req = RecommendService.Request()

        req.interfaceName = "fetch_tabs_version_1_0"
        req.type = 0
        req.platformId = "1"
        req.tabId = tabId
        req.num = 50
        req.userId = generator()
        print req

        res = client.fetchTabs(req)

        cards = []
        if res==[]:
            value = _ResAbnormal
        else:
            for tabs in res:
                for card in tabs.cardList:
                    cards.append([card.cardName, card.cardId])

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
        # r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        # print r.text   
        print cards     
        return cards
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    finally:
        transport.close()

def monitors(reqFunc, resCheck, metric, attrDict={}):
    payload = []
    ts = int(time.time())
    step = 120

    value = _Normal
    try:
        # to be optimized
        transport = TSocket.TSocket(address, 8081)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print metric
        print "server reponse: " + msg

        req = RecommendService.Request()

        for attr in attrDict:
            setattr(req, attr, attrDict[attr])
        if "userId" not in attrDict.keys():
            req.userId = generator()
        print req

        while 1 :
            if reqFunc == "recommend":
                res = client.recommend(req)
            elif reqFunc == "fetchTabs":
                res = client.fetchTabs(req)
            else:
                res = ""

            if resCheck=="result":
                if res==[] or res.resultList==None or len(res.resultList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    for result in res.resultList:
                        print result
                        if hasattr(result, "resultType"):
                            if field_check(getattr(result, "resultType"), result)==False:
                                print result
                                value = _FieldAbnormal

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
            # r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
            # print r.text
            break
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    finally:
        transport.close()

def check_tab_cards(cards, tab_index):
     if len(cards) > 0:
        card_index = 1
        for card in cards:
            attrDict = {
                        "interfaceName":"mxbeta_main_version_1_0",
                        "type": 0,
                        "platformId": "1",
                        "country": "CN",
                        "networkStatus": "3G",
                        "cardId": card[1],
                        "cardName": card[0],
                        "num": 2
                        }
            metric = "mx_main_" + tab_index + "_card_" + str(card_index)
            monitors("recommend", "result", metric, attrDict)
            card_index += 1

if __name__ == "__main__":

    with open(servers_config, 'r') as f:
        server_groups = eval(f.read())

    with open(interfaces_config, 'r') as f:
        interface_groups = eval(f.read())

    for server_group in server_groups:
        servers = server_groups[server_group]
        for server in servers:
            endpoint = server.get("endpoint", None)
            address = server.get("address", None)

            # Check the interfaces in config file
            for interface_group in interface_groups:
                interfaces = interface_groups[interface_group]
                for interface in interfaces:
                    reqFunc = interface.get("reqFunc", None)
                    resCheck = interface.get("resCheck", None)
                    metric = interface.get("metric", None)
                    attrDict = interface.get("attrDict", {})
                    monitors(reqFunc, resCheck, metric, attrDict)

            # Check the cards in Home/Buzz/Music/Shows/Movies
            # cards = get_tab_cards("1", "mx_main_1st_tab_fetchtabs_version_1_0")
            # check_tab_cards(cards, "1st_tab")

            # cards = get_tab_cards("2", "mx_main_2nd_tab_fetchtabs_version_1_0")
            # check_tab_cards(cards, "2nd_tab")

            # cards = get_tab_cards("3", "mx_main_3rd_tab_fetchtabs_version_1_0")
            # check_tab_cards(cards, "3rd_tab")

            # cards = get_tab_cards("4", "mx_main_4th_tab_fetchtabs_version_1_0")
            # check_tab_cards(cards, "4th_tab")

            # cards = get_tab_cards("5", "mx_main_5th_tab_fetchtabs_version_1_0")
            # check_tab_cards(cards, "5th_tab")


