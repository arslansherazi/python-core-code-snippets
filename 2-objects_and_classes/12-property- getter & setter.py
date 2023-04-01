"""
    Important Notes::
    => getter and setter are used for encapsulation in object oriented programming
    => As python does not support private data members so in python main purpose of getter and setter is data
       validation
    => property name and its corresponding data member name should be different
"""


class Student:
    def __init__(self):
        self.name = ''
        self.cgpa = 0

    def set_name(self, name):
        if not name:
            raise ValueError('name cannot be empty')
        else:
            self.name = name

    def get_name(self):
        return self.name

    def delete_name(self):
        del self.name

    # class property using @property decorator
    @property
    def student_cgpa(self):
        return self.cgpa

    @student_cgpa.setter
    def student_cgpa(self, cgpa):
        if not cgpa:
            raise ValueError('cgpa cannot be empty')
        elif cgpa < 2.9:
            raise ValueError('You are not eligible to pass the degree')
        else:
            self.cgpa = cgpa

    # class property using property() function
    student_name = property(get_name, set_name, delete_name, doc='Student name property')


if __name__ == '__main__':
    student = Student()
    student.student_name = 'Arslan Haider Sherazi'  # calls setter(set_name) of property
    print(student.student_name)  # calls getter(get_name) of property

    student.student_cgpa = 3.42
    print(student.student_cgpa)
