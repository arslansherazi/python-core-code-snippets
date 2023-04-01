class Student:
    def __init__(self, name, roll_no, degree, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.degree = degree
        self.cgpa = cgpa

    def stu_university(self):
        university = 'Punjab University College of Information Technology'
        return vars()  # returns dictionary of local variables of university() function - same as locals()

    def stu_session(self):
        session = '2014-2018'
        return vars(self)  # returns only class attributes not local variables


if __name__ == '__main__':
    print(vars())

    student = Student('Arslan Haider Sherazi', 'BSEF14A513', 'SE', 3.42)
    student_attributes_dict = vars(student)
    print(student_attributes_dict)

    university_dict = student.stu_university()
    print(university_dict)

    student_attributes_dict = student.stu_session()
    print(student_attributes_dict)

