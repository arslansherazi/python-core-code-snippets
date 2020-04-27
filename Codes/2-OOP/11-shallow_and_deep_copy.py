import copy


class Student:
    roll_no = 0
    name = ''
    cgpa = 0.0

    def __init__(self, roll_no, name, cgpa):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa


if __name__ == '__main__':
    student = Student(13, 'Arslan', 3.42)

    # shallow copy
    student_shallow = student
    student.name = 'Arslan Haider Sherazi'
    print(student.name)
    print(student_shallow.name)

    # deep copy
    student_deep = copy.deepcopy(student)
    student.name = 'Syed Arslan Haider'
    print(student.name)
    print(student_deep.name)
