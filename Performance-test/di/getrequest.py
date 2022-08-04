# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 下午3:44
# @Author  : yahui yan

import fire
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.helpers import scan


ES_HOST = 'es-logging.internal.mxplay.com'
ES_PORT = 9200

es_cli = Elasticsearch(
    hosts=[{'host': ES_HOST, 'port': ES_PORT}],
    use_ssl=False,
    verify_certs=True,
    timeout=1000,
    connection_class=RequestsHttpConnection,
)

query_body = {
    "query": {
        "match": {
           "service": "di"
         }
     },
    "_source": "message",
    "size": 4
}


# doc_index = 'logstash-2018.12.26'
# doc_type = 'recommendation'


def scan_logs(date, log_file, target_size):
    doc_index = 'logstash-' + date
#    doc_type = service_name

    # docs = es_cli.search(index='/', body=query_body)
    # print docs

    docs = scan(es_cli,
                query=query_body,
                index=doc_index,
 #               doc_type=doc_type,
                scroll='10m'
                )
    size = 0
    with open(log_file, 'w') as f:
        for d in docs:
#            print d
            try:
                req0 = d.get('_source').get('message')
                req = req0.split('DIRequest')[1]
                req = req.split(")],")[0] + ")]"
                #print req
                #req = req[8:-1]
            except Exception:
                continue
            #if req:
            if "idsWithType" in req and "(idsWithTypes:[]" not in req:
 #               print req
                f.write(req.encode('utf8'))
                f.write("\n")
                size += 1
            if size >= target_size:
                return


if __name__ == '__main__':
    fire.Fire(scan_logs)
