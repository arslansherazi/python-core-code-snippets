"""
    Important Points::
    =>access specifiers are not present in python
    =>all members of a class in python are public
"""


class Student:
    # data members (attributes)
    name = 'Arslan Haider Sherazi'
    cgpa = 0.0

    # constructor
    def __init__(self, roll_no, cgpa):
        self.roll_no = roll_no  # new attribute roll_no is created because is it not created already
        self.cgpa = cgpa  # referring already present attribute

    # member functions
    def output(self, name):
        self.name = name
        print(self.roll_no, self.name, self.cgpa)


if __name__ == '__main__':
    student1 = Student(13, 3.42)
    roll_no = student1.roll_no
    name = student1.name
    cgpa = student1.cgpa
    print(roll_no, name, cgpa)

    student2= Student(30, 2.53)
    student2.output('Danish Ali')
