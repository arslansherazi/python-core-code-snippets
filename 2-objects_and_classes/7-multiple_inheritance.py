class Parent1:
    roll_no = 0

    def __init__(self, roll_no):
        self.roll_no = roll_no


class Parent2:
    name = ''

    def __init__(self, name):
        self.name = name


class Child(Parent1, Parent2):
    cgpa = 0.0

    def __init__(self, roll_no, name, cgpa):
        Parent1.__init__(self, roll_no)  # if we call __init__ using super() then only Parent1's __init__ will be called
        Parent2.__init__(self, name)
        self.cgpa = cgpa

    def display(self):
        print(self.roll_no, self.name, self.cgpa)


if __name__ == '__main__':
    child = Child(13, 'Arslan Haider Sherazi', 3.42)
    child.display()
