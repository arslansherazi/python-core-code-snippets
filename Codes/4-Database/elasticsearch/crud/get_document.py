from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.client import IndicesClient


if __name__ == '__main__':
    es_client = Elasticsearch()  # default host = localhost:9200
    index_name = 'students_index'
    document_id = 'BSEF14A513'
    try:
        document = es_client.get(index=index_name, id=document_id)
        print(document)
    except NotFoundError:
        print('document {} does not exist'.format(document_id))
    except Exception:
        print('Something went wrong while retrieving document {}'.format(document_id))
