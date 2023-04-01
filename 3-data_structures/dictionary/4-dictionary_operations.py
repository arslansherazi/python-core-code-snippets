if __name__ == '__main__':
    # create empty dictionary
    student = dict()  # Equivalent => student = {} but student = dict() is recommended by PEP

    # adding key:value pair(s) into dictionary
    student['roll_no'] = 13
    student['name'] = 'Arslan Haider'  # syntax => dict_obj[key] = value
    student['cgpa'] = 3.42
    print(student)

    # accessing value(s) from dictionary
    name = student['name']  # Equivalent => name = student.get('name)
    print(name)

    roll_no = student.get('roll_no')  # Equivalent => roll_no = student['roll_no]
    print(roll_no)

    age = student.get('age', None)  # returns default value if key is not present in dictionary
    print(age)
    roll_no = student.get('roll_no', 'BSEF14A513')  # roll_no = key, BSEF14A513 = default value
    print(roll_no)

    # similar to get(), but will add key:default_value pair into dict if key is not already in dict
    name = student.setdefault('name', None)  # name = key, None = default_value
    print(name)
    age = student.setdefault('age', 24)
    print(student)
    print(age)

    # updating dictionary value(s)
    student['name'] = 'Arslan Haider Sherazi'
    print(student['name'])

    # deleting key:value pair(s) from dictionary
    del student['name']
    print(student)

    #  creating a new dictionary with keys from sequence(list, tuple, set, dict). By default values will set to None
    keys = ('degree', 'programming_language')
    new_student = student.fromkeys(keys)
    print(new_student)

    # creating copy of dictionary
    student_copy = student.copy()
    print(student_copy)

    # merging two dictionaries.
    # if dict2 has same keys then dict1 keys will be overwritten by dict1 keys
    dict1 = {'name': 'Arslan Haider', 'cast': 'Syed'}
    dict2 = {'name': 'Arslan Haider Sherazi', 'age': 24}
    dict1.update(dict2)
    print(dict1)

    # empty dictionary
    student.clear()
    print(student)