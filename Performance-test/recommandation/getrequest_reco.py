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

'''
query_body = {
    "query": {
        "bool": {
            "must": [
                {
                    "terms": {
                        "json_content.message.interfaceName": [
                            "lastest_seasons_of_the_tvshow_version_1_0"
                        ]
                    }
                }
            ]
        }
    },
    "size": 400,
    "sort": [
        {
            "@timestamp": {
                "order": "desc"
            }
        }
    ],
    "_source": ["json_content.message.request"]
}
'''
query_body = {
    "query": {
         "match_all": {}
    },
    "size": 400,
    "sort": [
        {
            "@timestamp": {
                "order": "desc"
            }
        }
    ],
    "_source": ["json_content.message.request"]
}


# doc_index = 'logstash-2018.12.26'
# doc_type = 'recommendation'


def scan_logs(date, service_name, log_file, target_size):
    doc_index = 'logstash-' + str(date)
    doc_type = service_name

    # docs = es_cli.search(index='/', body=query_body)
    # print docs

    docs = scan(es_cli,
                query=query_body,
                index=doc_index,
                doc_type=doc_type,
                scroll='10m'
                )
    size = 0
    with open(log_file, 'w') as f:
        for d in docs:
            #print d
            try:
                req = d.get('_source').get('json_content').get('message').get('request')
                req = req[8:-1]
            except Exception:
                continue
            if req:
                #print req
                f.write(req.encode('utf8'))
                f.write("\n")
                size += 1
            if size >= target_size:
                return


if __name__ == '__main__':
    fire.Fire(scan_logs)
