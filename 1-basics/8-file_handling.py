"""
    Important Points::
    =>while writing to the file, if file is not present then it will be created automatically
"""
import pickle


class Student:
    def __init__(self, name, roll_no,degree, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.degree = degree
        self.cgpa = cgpa


if __name__ == '__main__':
    # writing to the file
    file = open('my_file.txt', 'w')  # w = write, a = append
    file.write('Waqar Haider Sherazi   29\n')
    file.write('Fasi Haider Sherazi    26\n')
    file.write('Arslan Haider Sherazi  24\n')
    file.write('Ghulam Haider Sherazi  19\n')
    file.close()

    # reading from the file
    file = open('my_file.txt', 'r')  # r = read
    name = file.read(14)  # 13 = no of bytes to read from file
    print(name)
    print('\n')

    # setting reading pointer at the beginning, 0 = offset(position of the read/write pointer within the file)
    file.seek(0)

    names = file.readlines()
    for name in names:
        print(name)
    file.close()

    # serialization
    student1 = Student('Arslan Haider Sherazi', 'BSEF14A513', 'SE', 3.42)
    student2 = Student('Danish Ali', 'BSEF14A530', 'SE', 2.53)

    students_file = open('students.bin', 'wb')  # wb = write binary, ab = append binary
    pickle.dump(student1, students_file)  # returns bytes array and also stores into file as serialized object
    pickle.dump(student2, students_file)
    students_file.close()

    students_file = open('students.bin', 'rb')  # rb = read binary
    students = []
    while True:
        try:
            student = pickle.load(students_file)
            students.append(student)
        except EOFError:
            break
    for student in students:
        print(student.name, student.roll_no, student.degree, student.cgpa)
