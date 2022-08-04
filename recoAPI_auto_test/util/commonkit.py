#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-05-08 16:19 
# @Author : lmh
# @Software: PyCharm
#
import configparser
import os
import ast
import time
import json
from util.log import log1
from pprint import pprint

from string import Template

def deal(strdata, dictdata):
    """
    格式化字符串
    """
    if not strdata:
        return strdata
    s = Template(strdata)
    res = s.substitute(**dictdata)
    return res

def excelfilter_notequal(data,field,value):
    """
    筛选指定字段的值和预期字段不一致的数据
    """
    res = []
    for d in data:
        v = d.get(field)
        if str(value) != str(v):
            res.append(d)
    return res

def excelfilter_contain(data,field,value):
    """
    筛选指定字段的值包含预期值的数据
    """
    res = []
    for d in data:
        v = d.get(field)
        if str(value) in str(v):
            res.append(d)
    return res

def str_to_json(strdata):
    """
    字符串转换成json格式
    :param strdata:
    :return:
    """
    if not strdata:
        return strdata
    else:
        return json.dumps(ast.literal_eval(strdata))

def literal_eval(strdata):
    """
    封装ast.literal_eval方法
    :param str:
    :return:
    """
    if not strdata:
        return strdata
    try:
        strdata = ast.literal_eval(strdata)
    finally:
        return strdata

def read_config(section,option,file):
    """
    获取配置文件下,某section下option的值
    :param section:
    :param option:
    :param file:
    :return:
    """
    conf = configparser.ConfigParser()
    conf.read(file)
    try:
        value = conf.get(str(section),str(option))
        log1.info('section: {}, option: {}, value: {}'.format(section, option, value))
        return value
    except BaseException as e:
        log1.error(e)

def files_num_limit(limitnum,dirpath,extension):
    """
    限制某目录下,某后缀名的文件的数量
    :param limitnum: 文件的限制数量
    :param dirpath: 文件目录
    :param extension: 文件后缀名
    :return:
    """
    count = 0
    dict1 = {}
    filenames = os.listdir(dirpath)
    for file in filenames:
        if file.split('.')[-1] == extension:
            file_path = os.path.join(dirpath,file)
            ctime = os.path.getctime(file_path)
            dict1[ctime] = file
            count += 1

    if count > limitnum:
        keys = sorted(dict1.keys(),reverse=False)
        for i in range(count-limitnum):
            os.remove(os.path.join(dirpath, dict1[keys[i]]))

def strtime():
    strtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return strtime

def deletefiles(dir,extension='txt'):
    """
    删除目录下所有文件,忽略文件夹
    :param dir:
    :return:
    """
    os.chdir(dir)
    for file in list(os.listdir(dir)):
        if os.path.isfile(file):
            if file.split('.')[-1] == extension:
                os.remove(file)


def writefile(dir, filename, data):
    if os.path.exists(dir+filename):
        fname, ext = os.path.splitext(filename)
        filename = fname+'-1'+ext
    with open(dir+filename, 'w+') as f:
        f.write(data)
