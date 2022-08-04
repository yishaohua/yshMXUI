#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-06-05 16:05 
# @Author : lmh
# @Software: PyCharm
#
import re
from util import commonkit
import ast

def juege_contain_message(data,judgemes):
    """是否包含指定内容"""
    if str(judgemes) in str(data):
        return True
    else:
        return False

def judge_contain_http(data,http_list=[]):
    """是否存在http地址"""
    patt = re.compile('"http:.*?"')
    http_list = re.findall(patt,str(data))
    return http_list

def judge_keys_same(input_json, judgelist):
    """字段信息是否一致"""
    if not judgelist:
        return True

    if not input_json :
        return '输入数据为空'

    if isinstance(judgelist,str):
        judgelist = commonkit.literal_eval(judgelist)

    if isinstance(input_json,str):
        input_json = commonkit.literal_eval(input_json)

    keys = list(input_json.keys())
    if sorted(keys) != sorted(judgelist):
        return keys
    else:
        return True

def spilt_text(datastr):
    """根据';','/',','对字符串拆分,返回一个深层遍历列表"""
    spiltresult = []
    list1 = datastr.split(';')

    for i in list1:
        list01 = []

        list2 = i.split('/')
        for i in list2[:-1]:
            list01.append(i)

        list3 = list2[-1].split(',')
        for i in list3:
            list02 = list01[:]
            list02.append(i)
            spiltresult.append(list02)
    return spiltresult


def merge_text(datalist):

    resultlist = []
    for i in datalist:
        value = ''
        for j in i:
            value = value + '/' + str(j)
        resultlist.append(value)

    return resultlist



def judge_value_not_none(input_json,judgetext):
    """深层遍历指定key的值不为空"""
    if not judgetext:
        return True

    if not input_json:
        return '输入数据为空'

    if isinstance(input_json,str):
        input_json = commonkit.literal_eval(input_json)

    spiltlist = spilt_text(judgetext)

    resultdict = {}
    for i in spiltlist:
        value = ''
        key = ''
        for j in i:
            key = key + '/' + str(j)
            value = input_json.get(j)
        resultdict[key] = value

    result = []
    for k,v in resultdict.items():
        if not v:
            result.append(k)

    if not result:
        return True
    else:
        return result

def pathsplit(strdata):
    result = []
    if not strdata:
        return strdata
    strdatas = strdata.split(';')
    for s in strdatas:
        s = s.strip()
        if ':' in s:
            path = s.split(':')[0]
            judge = s.split(':')[1]
        else:
            path = s
            judge = 'NN'

        if '/' in path:
            paths = path.split('/')[:-1]
            field = path.split('/')[-1]
        else:
            paths = None
            field = path

        fields = field.split(',')

        pathlist = []
        pathnum = []
        if paths:
            for p in paths:
                if '-' in p:
                    p1 = p.split('-')[0]
                    p2 = p.split('-')[1]
                else:
                    p1 = p
                    p2 = None
                pathlist.append(p1)
                pathnum.append(p2)

        for f in fields:
            res = []
            temp1 = pathlist[:]
            temp2 = pathnum[:]
            temp1.append(f)
            temp2.append(None)
            res.append(temp1)
            res.append(temp2)
            res.append(judge)
            result.append(res)
    return result

def pandaun(data, field, judge):
    if not data:
        return False

    if isinstance(data, dict):
        value = data.get(field)
        if judge == 'NN':
            if not value and value != 0:
                return False

        if judge == 'EX':
            keys = data.keys()
            if field not in keys:
                return False

        if judge[:1] == 'L':
            length = int(judge[1:])
            if isinstance(value, list):
                if len(value) < length:
                    return False
            else:
                return False
        return True

    elif isinstance(data, list):
        for d in data:
            if isinstance(d, dict):
                value = d.get(field)
                if judge == 'NN':
                    if not value and value != 0:
                        return False

                if judge == 'EX':
                    keys = d.keys()
                    if field not in keys:
                        return False

                if judge[:1] == 'L':
                    length = int(judge[1:])
                    if isinstance(value, list):
                        if len(value) < length:
                            return False
                    else:
                        return False
        return True
    else:
        return False

def existkey(data, key):
    if isinstance(data, dict):
        keys = data.keys()
        if key in keys:
            return True
        else:
            return False
    else:
        return False

def valuenotNone(data, key):
    if isinstance(data, dict):
        value = data.get(key)
        if isinstance(value, int):
            return True
        elif value:
            return True
        else:
            return False
    else:
        return False

def single_result(data, path, num, judge):
    length = len(path)
    if not data :
        return False
    if length>1:
        pi = path[0]
        ni = num[0]
        if isinstance(data, dict):
            data = data.get(pi)
            if isinstance(data, list):
                if ni is not None:
                    if len(data) > int(ni):
                        data = data[int(ni)]
                        return single_result(data, path[1:], num[1:], judge)
                    else:
                        return False
                else:
                    for t in data:
                        if isinstance(t,dict):
                            return single_result(t,path[1:], num[1:], judge)
                        else:
                            return False
            elif isinstance(data, dict):
                return single_result(data, path[1:], num[1:], judge)
        else:
            return False
    field = path[-1]
    res = pandaun(data, field, judge)

    if not res:
        return False
    return True

def judge_json_result(data, judgemes):
    result = []
    spiltres = pathsplit(judgemes)
    for s in spiltres:
        path, num, judge = s
        res = single_result(data, path, num, judge)
        if not res:
            result.append(s)
    return result
