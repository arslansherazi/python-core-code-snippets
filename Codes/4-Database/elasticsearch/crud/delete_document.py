from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient


if __name__ == '__main__':
    es_client = Elasticsearch()  # default host = localhost:9200
    index_name = 'students_index'
    document_id = 'BSEF14A513'
    try:
        es_client.delete(index=index_name, id=document_id)
        print('document {} is deleted successfully'.format(document_id))
    except Exception as e:
        print('document {} is not deleted successfully'.format(document_id))
