#!/usr/bin/env python

import sys
import datetime
import json
import requests
import time
import random
import string
sys.path.append('/home/qatest/mx-monitor/di/gen-py') 
#sys.path.append('/home/qatest/mx-monitor/di/di.thrift/gen-py') 
from di import DIService
from di.ttypes import IdsWithType

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

#interfaces_config = "/home/qatest/mx-monitor/di/test.json"
interfaces_config = "/home/qatest/mx-monitor/di/interfaces_main_di.json"

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
    fields = ["id", "name", "icon", "posterList","videoCount","description"]
    return field_check(publisher, fields)

def singer_field_check(singer):
    fields = ["id", "name", "icon", "ecount", "selfPicList", "albumIdList", "description","categoryId","releaseDate","languageList","genresList","audioLanguageList","videoCount","publisher"]
    return field_check(singer, fields)

def tv_show_field_check(tv_show):
    fields = ["id", "name", "icon", "ecount", "selfPicList", "albumIdList","categoryId","videoCount","publisher", "description","releaseDate","languageList","genresList","audioLanguageList"]
    return field_check(tv_show, fields)

def season_field_check(season):
    fields = ["id", "name", "icon", "ecount", "selfPicList", "videoIdList", "tvShow", "description", "publisher", "releaseDate","num","audioLanguageList","firstIsYoutube"]
    return field_check(season, fields)

def album_field_check(album):
    fields = ["id", "name", "icon", "ecount", "selfPicList", "songIdList", "singer", "description", "releaseDate","num","publisher","audioLanguageList","firstIsYoutube"]
    return field_check(album, fields)

def short_video_field_check(short_video):
    fields = ["relationType", "relationId", "publisher"]
    return field_check(short_video, fields)

def tv_show_video_field_check(tv_show_video):
    fields = ["publisher", "num"]
    return field_check(tv_show_video, fields)

def song_field_check(song):
    fields = ["publisher", "num"]
    return field_check(song, fields)

def playlist_field_check(playlist):
    fields = ["id","playCover","videoIds","name","videoCount","description","releaseDate","icon","selfPicList","genresList","firstIsYoutube"]
    return field_check(playlist, fields)

def language_field_check(language):
    fields = ["languageId", "languageName"]
    return field_check(language, fields)

def director_field_check(director):
    fields = ["id", "name"]
    return field_check(director, fields)

def movie_field_check(movie):
    fields = ["publisher", "num"]
    return field_check(movie, fields)

def actor_field_check(actor):
    fields = ["id", "name"]
    return field_check(actor, fields)

def genre_field_check(genre):
    fields = ["genresId", "genresName"]
    return field_check(genre, fields)

def card_field_check(card):
    fields = ["cardId", "cardName"]
    return field_check(card, fields)

def tab_field_check(tab):
    fields = ["id", "name"]
    return field_check(tab, fields)

def live_channel_field_check(live_channel):
    fields = ["domain", "title", "url", "playUrl", "thumbnailUrls"]
    return field_check(live_channel, fields)

def card_list_field_check(card_list):
    fields = ["tabId", "listStyles", "cardIds", "id", "moreStyles"]
    return field_check(card_list, fields)

def browse_item_list_field_check(browse_item_list):
    fields = ["id", "genresList", "releaseYears", "directorList", "actorList", "thumbnailUrls", "languageList"]
    return field_check(browse_item_list, fields)

def offer_field_check(offer):
    fields = ["id", "offerUrl", "vendor", "offerName", "codesS3Url", "details"]
    return field_check(offer, fields)

def vendor_field_check(vendor):
    fields = ["id", "thumbnailUrls"]
    return field_check(vendor, fields)

def question_field_check(question):
    fields = ["id", "options", "title"]
    return field_check(question, fields)

def cricket_field_check(cricket):
    fields = ["id"]
    return field_check(cricket, fields)

def cricket_widget_field_check(cricket_widget):
    fields = ["id","cricketWidgetName"]
    return field_check(cricket_widget, fields)

def strs_to_funcs(strs, argument):
    switcher = {
        "playlist" : playlist_field_check,
        "genre" : genre_field_check,
        "movie" : movie_field_check,
        "publisher" : publisher_field_check,
        "singer" : singer_field_check,
        "tv_show" : tv_show_field_check,
        "season" : season_field_check,
        "album" : album_field_check,
        "short_video": short_video_field_check,
        "tv_show_video": tv_show_video_field_check,
        "song" : song_field_check,
        "actor" : actor_field_check,
        "director" : director_field_check,
        "card" : card_field_check,
        "card_list" : card_list_field_check,
        "browse_item" : browse_item_list_field_check,
        "tab" : tab_field_check,
        "vendor" : vendor_field_check,
        "question" : question_field_check,
        "offer" : offer_field_check,
        "cricket" : cricket_field_check,
        "cricket_widget" : cricket_widget_field_check,
        "live_channel" : live_channel_field_check,
        "language" : language_field_check
    }
    func = switcher.get(strs, lambda x : False)
    return func(argument)


def basevideo_field_check(result, checklist):
    for i in checklist:
        if hasattr(result.BaseVideo, i):
            content = getattr(result.BaseVideo, i)
            if content==[] or content==None:
                print i
                print content
                return False
        else:
            print i
            return False
    return True

def basevideo_basevideo_field_check(director):
    fields = ["id", "thumbnailUrls", "createTime", "duration", "publisherId", "status","publishTime", "title", "viewCount","drmProtect", "releaseDate", "videoHash", "languageList", "categories", "genresList", "description","transcodeResult","audioLanguageList","playWithYoutube"]
    return basevideo_field_check(director, fields)

def basevideo_song_field_check(director):
    fields = ["id", "thumbnailUrls", "createTime", "duration", "publisherId", "status","publishTime", "title", "viewCount","drmProtect", "releaseDate", "videoHash", "languageList", "categories", "genresList", "audioLanguageList","youtubeId","playWithYoutube"]
    return basevideo_field_check(director, fields)

def basevideo_strs_to_funcs(strs, argument):
    switcher = {
        "movie" : basevideo_basevideo_field_check,
        "song" : basevideo_song_field_check,
        "tv_show_video" : basevideo_basevideo_field_check,
        "short_video": basevideo_basevideo_field_check
    }
    func = switcher.get(strs, lambda x : False)
    return func(argument)

def monitors(metric, attrDict={}):
    _ResAbnormal = 1
    _FieldAbnormal = 2
    _NumAbnormal = 3
    _Normal = 0
    payload = []
    ts = int(time.time())
    step = 360

    value = _Normal
    try:
        transport = TSocket.TSocket(address, 4000)
	transport.setTimeout(1000)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = DIService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print "server reponse: " + msg

        IdsWith_Types = []
    	IdsWithType1 = IdsWithType()
        for attr in attrDict:
            setattr(IdsWithType1, attr, attrDict[attr])
        IdsWith_Types.append(IdsWithType1)
        
    	req = DIService.DIRequest(idsWithTypes=IdsWith_Types, logId="1546", serviceName="test_client")    
        res = client.getDetail(req)
        #print req
        #print res

        for res_type in res.typeList:
            if res_type == "playlist":
                listname = res.playlistList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "director":
                listname = res.directorList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "vendor" :
                listname = res.vendorList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "question" :
                listname = res.questionList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "offer" :
                listname = res.offerList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "cricket_widget" :
                listname = res.cricketWidgetList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "cricket" :
                listname = res.cricketList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "card_list" :
                listname = res.cardListList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "live_channel" :
                listname = res.liveChannelList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "tab" :
                listname = res.tabList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "browse_item" :
                listname = res.browseItemList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "card" :
                listname = res.cardList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "movie":
                listname = res.movieList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(res_type, detail) == False or strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "short_video":
                listname = res.shortVideoList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(res_type, detail) == False or strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "album":
                listname = res.albumList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "genre":
                listname = res.genresList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "tv_show":
                listname = res.tvShowList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "tv_show_video":
                listname = res.tvShowVideoList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(res_type, detail) == False or strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "language":
                listname = res.languageList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "publisher":
                listname = res.publisherList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "singer":
                listname = res.singerList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "song":
                listname = res.songList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(res_type, detail) == False or strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "season":
                listname = res.seasonList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
                            value = _FieldAbnormal
            elif res_type == "actor":
                listname = res.actorList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(res_type, detail) == False:
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

    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=di')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    hosts = []
    #print server_groups

    with open(interfaces_config, 'r') as f:
        interface_groups = eval(f.read())

    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]

        for interface_group in interface_groups:
            interfaces = interface_groups[interface_group]
            for interface in interfaces:
                metric = interface.get("metric", None)
                attrDict = interface.get("attrDict", {})
                monitors(metric, attrDict)

        hosts.append(endpoint)

    print hosts
    add_falcon_hosts("28", hosts)


