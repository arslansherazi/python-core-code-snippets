"""
    Important Points:
    =>uuid1() generates uuid based on the Host ID and current time
    =>uuid4() generates random uuid
"""
import uuid


if __name__ == '__main__':
    unique_id1 = uuid.uuid1()
    print(unique_id1)

    unique_id2 = uuid.uuid4()
    print(unique_id2)