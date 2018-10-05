# coding=utf-8
from elasticsearch import Elasticsearch


def index_sina(search_key, index_name, page_from, page_size):
    es_client = Elasticsearch(['192.168.31.172:9200'])
    sina_doc = es_client.search(
        index=index_name,
        doc_type='doc',
        body={
            "query": {
                "function_score": {
                    "query": {
                        "match_phrase": {
                            "text": search_key
                        }
                    },
                    "script_score": {
                        "script": {
                            "source": "doc['commentsCount'].value + doc['attitudesCount'].value"
                        }
                    }
                }
            },
            "from": page_from,
            "size": page_size
            #     },
            #     "aggs": {
            #         "top_10_states": {
            #             "terms": {
            #                 "field": "state",
            #                 "size": 10
            #             }
            #         }
            #     }
        }
    )
    response = sina_doc['hits']
    return response


def index_zhihu(search_key, index_name, page_from, page_size):
    es_client = Elasticsearch(['192.168.31.172:9200'])
    zhihu_doc = es_client.search(
        index=index_name,
        doc_type='doc',
        body={
            "query": {
                "function_score": {
                    "query": {
                        "match_phrase": {
                            "content": search_key
                        }
                    },
                    "script_score": {
                        "script": {
                            "source": "doc['commentCount'].value + doc['voteupCount'].value"
                        }
                    }
                }
            },
            "from": page_from,
            "size": page_size
            #     },
            #     "aggs": {
            #         "top_10_states": {
            #             "terms": {
            #                 "field": "state",
            #                 "size": 10
            #             }
            #         }
            #     }
        }
    )
    response = zhihu_doc['hits']
    return response


def index_synthesize(search_key, index_name, page_from, page_size):
    es_client = Elasticsearch(['192.168.31.172:9200'])
    all_doc = es_client.search(
        # index=index_name,
        doc_type='doc',
        body={
            "query": {
                "function_score": {
                    "query": {
                        "match_phrase": {
                            "content": search_key
                        }
                    }
                    # },
                    # "script_score": {
                    #     "script": {
                    #         "source": "doc['commentCount'].value + doc['voteupCount'].value"
                    #     }
                    # }
                }
            },
            "from": page_from,
            "size": page_size
            #     },
            #     "aggs": {
            #         "top_10_states": {
            #             "terms": {
            #                 "field": "state",
            #                 "size": 10
            #             }
            #         }
            #     }
        }
    )
    response = all_doc['hits']
    return response
