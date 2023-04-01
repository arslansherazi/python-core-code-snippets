"""
    Important Points::
    => Following are some applications of getattr() function
        * Useful in case of Machine Learning features collection in case some features are missing sometimes
        * Useful in web development where some of form attributes are optional

    => conventional method of getting class attributes is faster than getting class attributes by using getattr()
       function
"""


class Student:
    roll_no = 'BSEF14A513'
    name = 'Arslan Haider Sherazi'


if __name__ == '__main__':
    student = Student()
    # get attributes of class using conventional method
    roll_no = student.roll_no
    name = student.name
    # degree = student.degree  # generates error because degree is not an attribute of Student class
    print(roll_no, name)

    # get attributes of class using getattr()
    roll_no = getattr(student, 'roll_no')
    name = getattr(student, 'name')
    degree = getattr(student, 'degree', 'SE')  # do not generate error instead use default value 'SE' for non existing attribute 'degree'  # noqa: 501
    print(roll_no, name, degree)
