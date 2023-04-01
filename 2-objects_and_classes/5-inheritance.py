class Person:
    name = ''
    age = 0
    address = ''

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def output(self):
        print('Name::', self.name)
        print('Age::', self.age)
        print('Address::', self.address)


class Student(Person):  # Person = parent class
    roll_no = 0

    def __init__(self, roll_no, name, age, address):
        super().__init__(name, age, address)  # Equivalent => Person.__init__(self, name, age, address)
        self.roll_no = roll_no

    def output(self):  # function overriding
        print('####Student Info####')
        print('Roll No::', self.roll_no)
        super().output()


class Employee(Person):
    emp_id = ''

    def __init__(self, emp_id, name, age, address):
        super().__init__(name, age, address)
        self.emp_id = emp_id

    def output(self):  # function overriding
        print('\n####Employee Info####')
        print('Employee ID::', self.emp_id)
        super().output()


if __name__ == '__main__':
    student = Student(13, 'Arslan Haider Sherazi', 24, 'Sialkot')
    student.output()

    employee = Employee('arslanh@theentertainerme.com', 'Arslan Haider Sherazi', 24, 'Sialkot')
    employee.output()
