#!/usr/bin/env python

import sys
import datetime
import json
import requests
import time
import random
import string
sys.path.append('/Users/ling.liu/Documents/autotest/DI/di.thrift/gen-py') 
from di import DIService
from di.ttypes import IdsWithType

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

interfaces_config = "/Users/ling.liu/Documents/autotest/DI/debug_interfaces_v5.json"
servers_config = "/Users/ling.liu/Documents/autotest/DI/servers_debug.json"

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
    fields = ["id", "name", "icon", "selfPic"]
    return field_check(publisher, fields)

def singer_field_check(singer):
    fields = ["id", "name", "icon", "ecount", "selfPic", "albumIdList", "description"]
    return field_check(singer, fields)

def tv_show_field_check(tv_show):
    fields = ["id", "name", "icon", "ecount", "selfPic", "seasonIdList", "description"]
    return field_check(tv_show, fields)

def season_field_check(season):
    fields = ["id", "name", "icon", "ecount", "selfPic", "tvShowVideoIdList", "tvShow", "description", "releaseDate"]
    return field_check(season, fields)

def album_field_check(album):
    fields = ["id", "name", "icon", "ecount", "selfPic", "songIdList", "singerList", "description", "releaseDate"]
    return field_check(album, fields)

def short_video_field_check(short_video):
    fields = ["source", "publisher"]
    return field_check(short_video, fields)

def tv_show_video_field_check(tv_show_video):
    fields = ["seasonIdList", "tvShow"]
    return field_check(tv_show_video, fields)

def song_field_check(song):
    fields = ["singerList", "albumIdList"]
    return field_check(song, fields)

def playlist_field_check(playlist):
    fields = ["id","playCover","videoIds", "name"]
    return field_check(playlist, fields)

def language_field_check(language):
    fields = ["languageId", "languageName"]
    return field_check(language, fields)

def director_field_check(director):
    fields = ["id", "name"]
    return field_check(director, fields)

def movie_field_check(movie):
    fields = ["actorInfoList", "directorInfoList"]
    return field_check(movie, fields)

def actor_field_check(actor):
    fields = ["id", "name"]
    return field_check(actor, fields)

def genre_field_check(genre):
    fields = ["genresId", "genresName"]
    return field_check(genre, fields)

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

def basevideo_movie_field_check(director):
    fields = ["id", "duration", "picList", "srcURL", "title", "genreses", "languages", "longDescription"]
    return basevideo_field_check(director, fields)

def basevideo_song_field_check(director):
    fields = ["id", "duration", "picList", "srcURL", "title", "longDescription", "languages", "genreses", "playCount"]
    return basevideo_field_check(director, fields)

def basevideo_tv_show_video_field_check(director):
    fields = ["id", "duration", "picList", "srcURL", "title", "longDescription", "languages", "genreses", "playCount"]
    return basevideo_field_check(director, fields)

def basevideo_short_video_field_check(director):
    fields = ["srcURL", "id", "title", "playCount", "picList", "publishTime", "duration"]
    return basevideo_field_check(director, fields)

def basevideo_strs_to_funcs(strs, argument):
    switcher = {
        "movie" : basevideo_movie_field_check,
        "song" : basevideo_song_field_check,
        "tv_show_video" : basevideo_tv_show_video_field_check,
        "short_video": basevideo_short_video_field_check
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
    step = 120

    value = _Normal
    try:
        transport = TSocket.TSocket(address, 19959)
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

        for type1 in res.typeList:
            if type1 == "playlist":
                listname = res.playlistList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "director":
                listname = res.directorList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "movie":
                listname = res.movieList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(type1, detail) == False or strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "short_video":
                listname = res.shortVideoList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(type1, detail) == False or strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "album":
                listname = res.albumList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "genre":
                listname = res.genresList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "tv_show":
                listname = res.tvShowList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "tv_show_video":
                listname = res.tvShowVideoList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(type1, detail) == False or strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "language":
                listname = res.languageList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "publisher":
                listname = res.publisherList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "singer":
                listname = res.singerList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "song":
                listname = res.songList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if basevideo_strs_to_funcs(type1, detail) == False or strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "season":
                listname = res.seasonList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
                            value = _FieldAbnormal
            elif type1 == "actor":
                listname = res.actorList
                if res==[] or listname==None or len(listname)<attrDict.get("num", 1):
                    print res
                    value = _ResAbnormal
                elif res.requestNum != res.responseNum:
                    value = _NumAbnormal
                else:
                    for detail in listname:
                        if strs_to_funcs(type1, detail) == False:
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
                    metric = interface.get("metric", None)
                    attrDict = interface.get("attrDict", {})
                    monitors(metric, attrDict)
