#!/usr/bin/python
# -*- coding: UTF8 -*-

from tensorflow_serving.apis import predict_pb2, prediction_service_pb2
from grpc.beta import implementations
import tensorflow as tf
import requests
import time
import json

def float_feature(value):
    return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def client_res():
    channel = implementations.insecure_channel("dnn.internal.mxplay.com", 80)
    #channel = implementations.insecure_channel("dnn.dev.mxplay.com", 80)
    stub = prediction_service_pb2.beta_create_PredictionService_stub(channel)
    req = predict_pb2.PredictRequest()
    req.model_spec.name = 'banner_rank_wdl_1'
    req.model_spec.signature_name = 'serving_default'

    feature_dict = {
        'tabID': bytes_feature(value=''.encode()),
        'itemID': bytes_feature(value=''.encode()),
        'clientWeekday': bytes_feature(value=''.encode()),
        'clientHour': bytes_feature(value=''.encode()),
        'index': float_feature(value=int(1)),
        'sumClickTimes': float_feature(value=float(1)),
        'sumViewTimes': float_feature(value=float(1)),
        'sumPlayTime': float_feature(value=float(1)),
        'duration': float_feature(value=float(1)),
        'avgPlayTime': float_feature(value=float(1)),
        'playCompleteRate': bytes_feature(value=''.encode()),
        'category': bytes_feature(value=''.encode()),
        'type': bytes_feature(value=''.encode()),
        'languageId': bytes_feature(value=''.encode()),
        'languageId1': bytes_feature(value=''.encode()),
        'genresId': bytes_feature(value=''.encode()),
        'genresId1': bytes_feature(value=''.encode()),
        'ctr': bytes_feature(value=''.encode()),
        'publisher_name': bytes_feature(value=''.encode()),
    }
    example = tf.train.Example(features=tf.train.Features(feature=feature_dict))
    serialized = example.SerializeToString()
    req.inputs['inputs'].CopyFrom(
        tf.contrib.util.make_tensor_proto(serialized, shape=[1]))
    result_future = stub.Predict.future(req, 5.0)
    prediction = result_future.result()
    click_rate = prediction.outputs['scores'].float_val[1]
 
    if click_rate == [] or click_rate == None:
        return False
    else:
        return True

def monitors():
    
    _Normal = 0
    _ResAbnormal = 1

    value = _Normal

    ts = int(time.time())
    step = 300
    payload = []
    metric = "dnn_click_rate_monitor"

    res = client_res()
    if res == False:
        value = _ResAbnormal

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
    requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text

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

    r = requests.get('http://127.0.0.1:8500/v1/catalog/service/web?tag=dnn')
    server_groups = eval(r.text.replace("false", "False").replace("true", "True"))
    print server_groups
    hosts = []

    for server in server_groups:
        endpoint = server["Node"]
        address = server["Address"]

        print address

        monitors()
        hosts.append(endpoint)

    print hosts
    #add_falcon_hosts("43", hosts)
