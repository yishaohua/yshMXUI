#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 2019-10-09 14:38 
# @Author : lmh
# @Software: PyCharm
#
from util import commonkit,excelkit,judgekit,requestskit
from util.log import log1
from conf.config import *


def get_excel_data(env):
    if env == 'release' or env == 'pre':
        ek_data = excelkit.exceldata(excel_path, sheet_release)
        testcases = ek_data.exceldata_row()
        return testcases
    elif env == 'debug':
        pass
    else:
        return False

def get_excelconf_data(version, env):
    """
    根据环境获取excel中config的sheet下对应的数据
    """
    ek_conf = excelkit.exceldata(excel_path, sheet_config)
    configdata = ek_conf.exceldata_col()
    if version == 'ad':
        if env == 'pre' or env == 'release':
            for i in configdata:
                if i.get('name') == 'ad_release':
                    envdata = i
                    return envdata
        elif env == 'debug':
            for i in configdata:
                if i.get('name') == 'ad_debug':
                    envdata = i
                    return envdata
        else:
            print('env 输入错误')
            return False

    elif version == 'beta':
        if env == 'pre' or env == 'release':
            for i in configdata:
                if i.get('name') == 'beta_release':
                    envdata = i
                    return envdata
        elif env == 'debug':
            for i in configdata:
                if i.get('name') == 'beta_release':
                    envdata = i
                    return envdata
        else:
            print('env 输入错误')
            return False
    else:
        print('version 输入错误')
        return False


def testcases_filter(testcases, version):
    """
    根据环境过滤对应的用例
    """
    if version == 'ad':
        adcases = commonkit.excelfilter_contain(testcases, 'env', 'ad')
        adcases = commonkit.excelfilter_notequal(adcases, 'passornot', '1')
        return adcases
    elif version == 'beta':
        betacase = commonkit.excelfilter_contain(testcases, 'env', 'beta')
        betacase = commonkit.excelfilter_notequal(betacase, 'passornot', '1')
        return betacase
    else:
        return False

def reqmodel(data, configdata, header, host, resprename):
    '''
    recommendAPI
    '''
    casenum = data.get('casenum')
    casename = data.get('casename')
    env = data.get('env')
    description = data.get('description')
    API = commonkit.deal(data.get('API'), configdata)
    method = data.get('method')
    authorization = commonkit.deal(data.get('authorization'), configdata)

    param = commonkit.literal_eval(commonkit.deal(data.get('params'), configdata))
    body = commonkit.str_to_json(commonkit.deal(data.get('body'), configdata))

    except_code = data.get('except_code')
    except_text = data.get('except_text')

    judge_contain_message = commonkit.deal(data.get('judge_contain_message'), configdata)
    judge_not_contain_message = commonkit.deal(data.get('judge_not_contain_message'), configdata)

    judge_contain_http = data.get('judge_contain_http')
    judge_value = data.get('judge_value')

    # 如果存在授权信息,则在header中添加该字段
    if authorization:
        header.update({'authorization': authorization})
        log1.info('authorization: ' + str(authorization))

    # 拼接url
    url = 'https://{}/v1{}'.format(host, API)

    log1.info('casename: ' + str(casename))
    status_code, status_result, status_json = requestskit.request(method=method, url=url, params=param, data=body,
                                                                  headers=header)
    print('用例编号 : ' + str(casenum))
    print('用例名称 : ' + str(casename))
    print('用例环境 : ' + str(env))
    print('用例描述 : ' + str(description))
    print('请求地址url : ' + str(url))
    print('请求方法method : ' + str(method))
    print('参数param : ' + str(param))
    print('数据body : ' + str(body))
    print('授权信息authorization : ' + str(authorization))
    print('响应码status_code : ' + str(status_code))

    commonkit.writefile(responsedir, f'{resprename}-{casenum}-{casename}.txt' , str(status_result))

    # 打印响应结果,可对结果长度进行限制
    if result_length == 0:
        print('响应文本status_result : ' + str(status_result))
    elif len(status_result) < result_length:
        print('响应文本status_result : ' + str(status_result))
    elif len(status_result) > result_length:
        print('响应文本过长,不予显示,可在配置文件处设置最大显示长度')
    else:
        print('响应文本status_result : ' + str(status_result))

    # 判断响应码和预期是否一致
    assert status_code == except_code, '实际响应码:{} 与 预期:{}不一致'.format(status_code, except_code)

    # 如果预期结果不为空,则判断响应结果与预期结果是否一致
    if except_text:
        assert except_text == str(status_result), '实际返回文本:{} 与 预期文本:{}不一致'.format(status_result, except_text)

    # 判断响应结果是否包含预期文本
    if judge_contain_message:
        contain_result = judgekit.juege_contain_message(status_result, judge_contain_message)
        assert contain_result == True, '返回结果没有包含预期内容 返回结果: {}, 预期包含内容 : {}'.format(status_result, judge_contain_message)

    # 判断响应结果不包含预期文本
    if judge_not_contain_message:
        notcontain_result = judgekit.juege_contain_message(status_result, judge_not_contain_message)
        assert notcontain_result == False, '返回结果错误包含了预期内容 返回结果: {}, 预期不包含内容 : {}'.format(status_result,
                                                                                         judge_not_contain_message)

    # 若为1,则判断返回结果中是否存在http地址
    if judge_contain_http == '1':
        http_result = judgekit.judge_contain_http(status_result)
        assert http_result == [], '返回结果包含http地址 : {}'.format(http_result)

    if judge_value and judge_value != '-':
        failresult = judgekit.judge_json_result(status_json, judge_value)
        assert failresult == [], '返回结果字段的值与预期不符: {}'.format(failresult)
