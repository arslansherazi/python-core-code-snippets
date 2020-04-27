from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient


if __name__ == '__main__':
    es_client = Elasticsearch()  # default host = localhost:9200
    es_indices_client = IndicesClient(es_client)
    index_name = 'students_index'
    if not es_indices_client.exists(index_name):
        print('index {} does not exists'.format(index_name))
    else:
        es_indices_client.delete(index=index_name)
        print('index {} deleted successfully'.format(index_name))