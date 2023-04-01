"""
    Important Points::
    => named tuple is dict like data structure but unlike dict we can iterate named tuple
    => we can also access named tuple using keys just like in dict
    => we can also access named tuple by using index no. But dict lacks this functionality
"""
from collections import namedtuple


if __name__ == '__main__':
    # defining named tuples
    student = namedtuple('Student', ['roll_no', 'name', 'degree', 'cgpa'])

    # adding values
    student1 = student('BSEF14A513', 'Arslan Haider Sherazi', 'SE', 3.42)
    student2 = student('BSEF14A530', 'Danish Ali', 'SE', 2.53)
    student3 = student('BSEF14A526', 'Asher Butt', 'SE', 3.01)
    student4 = student('BSEF14A536', 'Babar Ali', 'SE', 2.97)

    # accessing values using index
    student_name = student1[1]
    print(student_name)