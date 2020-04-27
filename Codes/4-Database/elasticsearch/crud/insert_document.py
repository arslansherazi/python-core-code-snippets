from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

if __name__ == '__main__':
    es_client = Elasticsearch()  # default host = localhost:9200
    index_name = 'students_index'
    document = {
        "roll_no": "BSEF14A513",
        "name": "Syed Arslan Haider Sherazi",
        "degree": "SE",
        "cgpa": 3.42,
        "semesters_details": {
            "semester1": {
                "gpa": 3.34,
                "major_subjects": ["PF", "ITC"]
            },
            "semester2": {
                "gpa": 3.18,
                "major_subjects": ["OOP"]
            },
            "semester3": {
                "gpa": 3.12,
                "major_subjects": ["DSA", "COAL"]
            },
            "semester4": {
                "gpa": 3.42,
                "major_subjects": ["AOA", "OS"]
            },
            "semester5": {
                "gpa": 3.62,
                "major_subjects": ["JAVA"]
            },
            "semester6": {
                "gpa": 3.62,
                "major_subjects": [".NET", "Android"]
            },
            "semester7": {
                "gpa": 3.75,
                "major_subjects": ["OFD"]
            },
            "semester8": {
                "gpa": 3.47,
                "major_subjects": ["DS", "OFD"]
            }
        }
    }
    document_id = document.get('roll_no')
    try:
        es_client.index(index=index_name, doc_type='doc', id=document_id, body=document)
        print('document {} is added successfully'.format(document_id))
    except Exception as e:
        print('document {} is not added successfully'.format(document_id))
