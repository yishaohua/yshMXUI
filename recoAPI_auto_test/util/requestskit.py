#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-05-15 18:25 
# @Author : lmh
# @Software: PyCharm
#
import requests
from util.log import log1

def request(method,url=None,params=None,data=None,headers=None,):
    if method is None:
        method = 'get'

    if method.lower() == 'get':
        try:
            r = requests.get(url, params=params, data=data, headers=headers)
            # log1.info("请求的url: {}".format(url))
            # log1.info("method : get")
            # log1.info("请求内容params：{}".format(params))
            # log1.info("请求内容data：{}".format(data))
            # log1.info("headers：{}".format(headers))
            status_code = r.status_code  # 获取返回的状态码
            # log1.info("获取返回的状态码: {}".format(status_code))
            response_text = r.text  # 响应内容

            try:
                response_json = r.json()
            except:
                response_json = ''

            # log1.info("响应内容：{}".format(response_text))
            #print(status_code,response_json)
            return status_code, response_text, response_json # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！ {}".format(e))

    if method.lower() == 'post':
        try:
            r = requests.post(url, params=params, data=data, headers=headers)
            # log1.info("请求的url: {}".format(url))
            # log1.info("method : post")
            # log1.info("请求内容params：{}".format(params))
            # log1.info("请求内容data：{}".format(data))
            # log1.info("headers：{}".format(headers))
            status_code = r.status_code  # 获取返回的状态码
            # log1.info("获取返回的状态码: {}".format(status_code))
            response_text = r.text  # 响应内容
            try:
                response_json = r.json()
            except:
                response_json = ''
            # log1.info("响应内容：{}".format(response_text))
            return status_code, response_text, response_json    # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！{}".format(e))
