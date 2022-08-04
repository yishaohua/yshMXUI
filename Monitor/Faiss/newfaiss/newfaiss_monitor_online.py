import os
import requests
import datetime
import sys
import time
import json
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

import grpc
from faiss_grpc import faiss_pb2_grpc, faiss_pb2
from faiss_grpc.faiss_pb2 import UpdateRequest, FaissResponse, Str2FloatMap, FloatArray

def search_vector(vectorType,category):
    channel = grpc.insecure_channel(host_port)
    stub = faiss_pb2_grpc.FaissStub(channel)
    response = stub.search(faiss_pb2.SearchRequest(
        vectorType = vectorType,
        category = category,
        num = 10,
        vector = [FloatArray(val=[1.0 for i in range(64)])],
    ))
    return response

def search_vector_256(vectorType,category):
    channel = grpc.insecure_channel(host_port)
    stub = faiss_pb2_grpc.FaissStub(channel)
    response = stub.search(faiss_pb2.SearchRequest(
        vectorType = vectorType,
        category = category,
        num = 10,
        vector = [FloatArray(val=[1.0 for i in range(256)])],
    ))
    return response

def search_id(vectorType,category,ids):
    channel = grpc.insecure_channel(host_port)
    stub = faiss_pb2_grpc.FaissStub(channel)
    response = stub.search(faiss_pb2.SearchRequest(
        vectorType = vectorType,
        category = category,
        num = 10,
        itemId = ids
    ))
    return response

def get_version(response):
    return response.version

def get_neighbors(response):
    neighbors = dict()
    for k, v in response.similarItems.items():
        neighbors[k] = dict(v.innerMap)
    return neighbors

def get_id(response):
    neighbors = dict()
    for k, v in response.similarItems.items():
        neighbors[0] = dict(v.innerMap)
    return neighbors[0].keys()

def do_monitor(category_list,vectorType, monitorType):

    for category in category_list:

        _Normal = 0
        _ResAbnormal = 1
        _VersionAbnormal = 2
        _NumAbnormal = 3

        res = None
        metric = None
        if monitorType == "monitors_id":
            resp = search_vector(vectorType,category) 
            res = search_id(vectorType,category,get_id(resp))
            metric = "faiss_" + vectorType + "/" + category + "_id_monitor" 
        elif monitorType == "monitors_vector":
            res = search_vector(vectorType,category) 
            metric = "faiss_" + vectorType + "/" + category + "_vector_monitor" 
        elif monitorType == "monitors_vector_256":
            res = search_vector_256(vectorType,category)
            metric = "faiss_" + vectorType + "/" + category + "_vector_monitor"
            #print(res)
	
        version=get_version(res)
        #print(version)
        handler=get_neighbors(res)
        #print(handler)


        value = _Normal
        ts = int(time.time())
        step = 300
        payload = []

        #print(len(list((list(handler.values()))[0])))

        if handler == None:
            value = _ResAbnormal

        elif ("card" not in metric and len(list((list(handler.values()))[0])) < 100) or ("card" in metric and len(list((list(handler.values()))[0])) < 20):
            value = _NumAbnormal
           
        elif version != None and "swing" in metric:

            version = version[8:14]
            print(version)
            c_time = (datetime.datetime.now() + datetime.timedelta(days=-3)).strftime('%Y%m%d')[2:]

            if version < c_time:
                value = _VersionAbnormal
        else:
            pass

        mes ={
            "endpoint": "newfaiss",
            "metric": metric,
            "timestamp": ts,
            "step": step,
            "value": value,
            "counterType": "GAUGE",
            "tags": "result"
          }
        payload.append(mes)
        print(payload)
        print(value)
        requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
        print(r.text)

if __name__ == '__main__':

    host_port='faiss-new.internal.mxplay.com:8080'
    #host_port='ec2-13-235-99-239.ap-south-1.compute.amazonaws.com:50051'

    tab_id = ['08f8fce450d1ecf00efa820f611cf57b','5f15a7356cf9dfceeb355fc49dd2be8a','4e82d34404a477419f811cd303e216e7','4a0eba2ea3b96a2ff2a72f60a0f1693b','6256019abbad655653afffa3056345a1','a78e8100f00962aa48326fd00fed5908','7694f56f59238654b3a6303885f9166f','87c3ddc974dcf12294e9412bec44b097','feacc8bb9a44e3c86e2236381f6baaf3']
    tab_id2 = ['a78e8100f00962aa48326fd00fed5908','08f8fce450d1ecf00efa820f611cf57b','feacc8bb9a44e3c86e2236381f6baaf3']
    tab_id3 = ['08f8fce450d1ecf00efa820f611cf57b','4e82d34404a477419f811cd303e216e7','6256019abbad655653afffa3056345a1','a78e8100f00962aa48326fd00fed5908','7694f56f59238654b3a6303885f9166f','87c3ddc974dcf12294e9412bec44b097','feacc8bb9a44e3c86e2236381f6baaf3']
    category_type1 = ['music','tv_show','short_video','movie'] 
    category_type2 = ['music','tv_show','short_video','movie','episode','season','singer','publisher','playlist']


    do_monitor(tab_id,'deepwalk/online/card','monitors_vector')
    do_monitor(tab_id,'deepwalk/all_mix/card','monitors_vector')
    do_monitor(tab_id2,'deepwalk/online_mix/card','monitors_vector')
    do_monitor(tab_id3,'deepwalk/dnn_vector/card','monitors_vector_256') #except news/web series
    do_monitor(category_type1,'research/deepwalk/online/swing','monitors_vector')
    do_monitor(category_type2,'deepwalk/online','monitors_id')
    do_monitor(category_type1,'research/deepwalk/online/swing','monitors_id')
    do_monitor(category_type2,'deepwalk/online','monitors_vector')
