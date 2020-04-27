"""
    Important Points::
    => Mongo database will be created when first document is inserted into the database
    => Table in SQL = Collection in Mongo DB
    => Record/Row in SQL = Document in Mongo DB
    => Column in SQL = Field in Mongo DB
"""
import pymongo


def get_all_students():
    students = students_data.find()
    for student in students:
        roll_no = student.get('roll_no')
        name = student.get('name')
        degree = student.get('degree')
        cgpa = student.get('cgpa')
        print(roll_no, name, degree, cgpa)


if __name__ == '__main__':
    # creating mongo db client
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')

    # creating database
    students_db = mongo_client['students_db']

    # creating collection
    students_data = students_db['students_data']

    # insert into collection
    students = [
        {'roll_no': 'BSEF14A513', 'name': 'Arslan Haider Sherazi', 'degree': 'SE', 'cgpa': 3.42},
        {'roll_no': 'BSEF14A530', 'name': 'Danish Ali', 'degree': 'CS', 'cgpa': 2.53},
        {'roll_no': 'BSEF14A536', 'name': 'Babar Ali', 'degree': 'SE', 'cgpa': 2.91},
        {'roll_no': 'BSEF14A526', 'name': 'Asher Butt', 'degree': 'SE', 'cgpa': 3.01}
    ]
    for student in students:
        stu = students_data.find_one({'roll_no': student.get('roll_no')})
        if not stu:
            students_data.insert_one(student)
    get_all_students()

    # update document in collection
    print('\n')
    update_query = {'roll_no': 'BSEF14A530'}
    update_values = {'$set': {'degree': 'SE'}}
    students_data.update_one(update_query, update_values)
    get_all_students()

    # delete a document from collection
    print('\n')
    students_data.delete_one({'roll_no': 'BSEF14A513'})
    get_all_students()
