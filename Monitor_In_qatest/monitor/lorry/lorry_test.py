#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-09-18 16:48 
# @Author : lmh
# @Software: PyCharm
#
import sys
from importlib import reload
sys.path.append('/home/qatest/mx-monitor/gen-py')
reload(sys)

from recommend import RecommendService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from recommend.ttypes import TabParams
from recommend.ttypes import BannerParams
from recommend.ttypes import CardParams
from recommend.ttypes import ItemParams

def process():

    try:
        transport = TSocket.TSocket('recommendation.internal.mxplay.com', 8081)
        transport = TTransport.TFramedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = RecommendService.Client(protocol)
        transport.open()
        msg = client.test("jack")
        print ("server reponse: " + msg)

        req = RecommendService.LorryRequest()

        req.interfaceName = "lorry_home_first_page_version_1_0"
        req.userId = "b841a365-fb69-4ae4-bb52-d0c16c66a67c5708592-skj"
        req.country= "IND"
        req.area  = ""
        req.language = "en"
        req.networkStatus = "3G"
        req.deviceInfo = "27"
        req.platformId = "1"
        req.tabId = ""
        req.resourceId = ""
        req.languageList = ["en", "hi", "ta"]
        req.clientVersion = "99999999999"
        req.logId = "XXXXXXXXXXXXXXXXXXX"
        req.timeSign = ""
        req.execTimeSign = ""
        req.execTimeDelay = ""
        #req.envOption = ""
        req.debugOption = ""
        req.bottomNavigation = ""
        req.specialMode = "normal"
        req.redPoint = ""

        tabParams = TabParams()
        tabParams.num = 10
        tabParams.finalId = ""
        req.tabParams = tabParams

        bannerParams = BannerParams()
        bannerParams.num = 10
        bannerParams.finalId = ""
        req.bannerParams = bannerParams

        cardParams = CardParams()
        cardParams.num = 10
        cardParams.finalId = ""
        req.cardParams = cardParams

        itemParams = ItemParams()
        itemParams.num = 10
        itemParams.finalId = ""
        req.itemParams = itemParams

        response = client.lorryRecommend(req)

        result = 0
        try:
            if not response.tabResponse.tabList:
                result = 1

            if not response.bannerResponse.bannerList:
                result = 2

            if not response.cardResponse.tabList[0].cardList:
                result = 3
        except:
            return 1

        return result

    except Thrift.TException as ex:
        print ("%s" % (ex.message))

    finally:
        transport.close()

if __name__ == '__main__':
    a =  process()
    print(a)