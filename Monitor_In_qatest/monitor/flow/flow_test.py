#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2020-06-15 19:45 
# @Author : lmh
# @Software: PyCharm
#
import json
import sys
from importlib import reload
sys.path.append('/Users/menghua.li/Desktop/monitor/gen-py')
reload(sys)

from recommend import RecommendService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

def process():
    def getStart(elem):
        return int(elem.split("-")[0])

    transport = TSocket.TSocket('recommendation.internal.mxplay.com', 8081)
    transport = TTransport.TFramedTransport(transport)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = RecommendService.Client(protocol)
    transport.open()

    res = json.loads(client.getRecoFlow())
    flow = {}
    lack_error = 0
    repeat_error = 0
    print (res)
    for item in res:
        if flow.get(item.get("interfaceName")):
            flow[item.get("interfaceName")].append(item.get("range"))
        else:
            flow[item.get("interfaceName")] = [item.get("range")]

    for key in flow.keys():
        flow.get(key).sort(key=getStart)
        pre_end = -1
        total = 0
        error = False
        for item in flow.get(key):
            item = item.strip()
            start = int(item.split("-")[0])
            end = int(item.split("-")[1])
            total += end - start + 1
            if start > pre_end + 1:
                # 覆盖不全的值
                print (key + " flow lack: " + str(flow.get(key)))
                error = True
                lack_error += 1
            if start < pre_end + 1:
                # 返回重复覆盖
                print (key + " flow repeat: " + str(flow.get(key)))
                error = True
                repeat_error += 1
            pre_end = end
        if not error:
            if total < 10000:
                # 覆盖不全的值
                print (key + " flow lack: " + str(flow.get(key)))
                lack_error += 1
            if total > 10000:
                # 重复覆盖
                print (key + " flow repeat: " + str(flow.get(key)))
                repeat_error += 1
    if repeat_error == 0 and lack_error == 0:
        return 0
    if repeat_error == 0 and lack_error != 0:
        return 1
    if repeat_error != 0 and lack_error == 0:
        return 2
    if repeat_error != 0 and lack_error != 0:
        return 3

if __name__ == '__main__':
    a =  process()
    print(a)