#!/usr/bin/env python

import sys
import datetime
sys.path.append('/mx-beta-falcon/monitor_scrpit/client_check/gen-py')
# sys.path.append('/Users/xin.xu/Documents/AutoTest/monitor/thrift2/gen-py') 
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

interfaces_config = "/mx-beta-falcon/monitor_scrpit/client_check/interfaces_v5_test.json"
servers_config = "/mx-beta-falcon/monitor_scrpit/client_check/servers_debug.json"

# interfaces_config = "/Users/xin.xu/Documents/AutoTest/monitor/interfaces_v5_test.json"
# servers_config = "/Users/xin.xu/Documents/AutoTest/monitor/servers_debug.json"

def generator():
    userId = "test_" + "".join(random.sample(string.ascii_lowercase + string.digits, 27))
    #print userId
    return userId

def field_check(result, checklist):
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

def publisher_field_check(publisher):
    fields = ["type", "id", "name", "icon", "selfPic"]
    return field_check(publisher, fields)

def singer_field_check(singer):
    fields = ["type", "id", "name", "icon", "desc", "selfPic", "albumIds",]
    return field_check(singer, fields)

def tv_show_field_check(tv_show):
    fields = ["type", "id", "name", "icon", "desc", "selfPic", "albumIds", "languages", "genreses"]
    return field_check(tv_show, fields)

def season_field_check(season):
    fields = ["type", "id", "name", "icon", "desc", "selfPic", "channelIds", "videoIds", "channelInfoLite"]
    return field_check(season, fields)

def album_field_check(album):
    fields = ["type", "id", "name", "icon", "desc", "selfPic", "channelIds", "videoIds", "channelInfoLite"]
    return field_check(album, fields)

def short_video_field_check(short_video):
    fields = ["srcURL", "id", "source", "title", "type", "channel", "attachContent", "time", "playCount", "picList", "copyright", "publishTime", "author", "duration", "authorPicture", "recallSign", "totalScore", "rankScore", "author", "styles", "resultType", "channelIds"]
    return field_check(short_video, fields)

def tv_show_video_field_check(tv_show_video):
    fields = ["id", "duration", "picList", "srcURL", "title", "recallSign", "longDescription", "resultType", "channelIds", "albumIds", "languages", "genreses", "playCount"]
    return field_check(tv_show_video, fields)

def song_field_check(song):
    fields = ["id", "duration", "picList", "srcURL", "title", "recallSign", "longDescription", "resultType", "channelIds", "albumIds", "languages", "genreses", "playCount"]
    return field_check(song, fields)

def playlist_field_check(playlist):
    fields = ["type", "id", "name", "icon", "selfPic"]
    return field_check(playlist, fields)

def genres_field_check(genres):
    fields = ["genresId", "genresName", "backgroundPic"]
    return field_check(genres, fields)

def strs_to_funcs(strs, argument):
    switcher = {
        "publisher" : publisher_field_check,
        "singer" : singer_field_check,
        "tv_show" : tv_show_field_check,
        "season" : season_field_check,
        "album" : album_field_check,
        "short_video": short_video_field_check,
        "tv_show_video": tv_show_video_field_check,
        "song" : song_field_check,
        "playlist" : playlist_field_check,
        "genres" : genres_field_check
    }
    func = switcher.get(strs, lambda x : False)
    return func(argument)

def monitors(reqFunc, resCheck, metric, attrDict={}):
    _ResAbnormal = 1
    _FieldAbnormal = 2
    _Normal = 0
    payload = []
    ts = int(time.time())
    step = 120

    value = _Normal
    try:
        transport = TSocket.TSocket(address, 19889)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print "server reponse: " + msg

        req = RecommendService.Request()
        
        for attr in attrDict:
            setattr(req, attr, attrDict[attr])
        if "userId" not in attrDict.keys():
            req.userId = generator()
        if "uuid" not in attrDict.keys():
            req.uuid = generator()

        while 1 :
            if reqFunc == "recommend":
                res = client.recommend(req)
            elif reqFunc == "fetchBannerData":
                res = client.fetchBannerData(req)
            elif reqFunc == "getGenresList":
                res = client.getGenresList(req)
            else:
                res = ""

            if resCheck=="detailList":
                if res==[] or res.detailList==None or len(res.detailList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    for detail in res.detailList:
                        if hasattr(detail, "type"):
                            if strs_to_funcs(getattr(detail, "type"), detail)==False:
                                # print detail
                                value = _FieldAbnormal

            elif resCheck=="resultList":
                if res==[] or res.resultList==None or len(res.resultList)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                else:
                    for result in res.resultList:
                        if hasattr(result, "resultType"):
                            if strs_to_funcs(getattr(result, "resultType"), result)==False:
                                # print result
                                value = _FieldAbnormal

            elif resCheck=="banner":
                if res==None or res==[]:
                    print res
                    value = _ResAbnormal
                else:
                    for banner in res:
                        if hasattr(banner, "detailInfo") and getattr(banner, "detailInfo")!=None:
                            detailInfo = getattr(banner, "detailInfo") 
                            if hasattr(detailInfo, "type"):
                                if strs_to_funcs(getattr(detailInfo, "type"), detailInfo)==False:
                                    # print detailInfo
                                    value = _FieldAbnormal
                            else:
                                value = _FieldAbnormal
                        elif hasattr(banner, "Result") and getattr(banner, "Result")!=None:
                            Result = getattr(banner, "Result") 
                            if hasattr(Result, "resultType"):
                                if strs_to_funcs(getattr(Result, "resultType"), Result)==False:
                                    # print Result
                                    value = _FieldAbnormal
                            else:
                                value = _FieldAbnormal
                        elif hasattr(banner, "videoInfo") and getattr(banner, "videoInfo")!=None:
                            videoInfo = getattr(banner, "videoInfo") 
                            if hasattr(videoInfo, "resultType"):
                                if strs_to_funcs(getattr(videoInfo, "resultType"), videoInfo)==False:
                                    # print videoInfo
                                    value = _FieldAbnormal
                            else:
                                value = _FieldAbnormal 
                        else:
                            value = _FieldAbnormal

            elif resCheck=="genres":
                if res==None or res==[]:
                    print res
                    value = _ResAbnormal
                else:
                    for genres in res:
                        if strs_to_funcs("genres", genres)==False:
                            # print result
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
            r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
            print r.text
            break
    except Thrift.TException, ex:
        print "%s" % (ex.message)
    finally:
        transport.close()


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
            for interface_group in interface_groups:
                interfaces = interface_groups[interface_group]
                for interface in interfaces:
                    reqFunc = interface.get("reqFunc", None)
                    resCheck = interface.get("resCheck", None)
                    metric = interface.get("metric", None)
                    attrDict = interface.get("attrDict", {})
                    monitors(reqFunc, resCheck, metric, attrDict)














    
     
