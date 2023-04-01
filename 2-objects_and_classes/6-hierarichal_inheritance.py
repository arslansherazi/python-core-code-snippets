class Parent:
    roll_no = 0

    def __init__(self, roll_no):
        self.roll_no = roll_no

    def get_roll_no(self):
        return self.roll_no


class Child(Parent):
    name = ''

    def __init__(self, roll_no, name):
        Parent.__init__(self, roll_no)  # Equivalent => Parent.__init__(self, roll_no)
        self.name = name

    def get_name(self):
        return self.name


class GrandChild(Child):
    cgpa = 0.0

    def __init__(self, roll_no, name, cgpa):
        super().__init__(roll_no, name)
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


if __name__ == '__main__':
    grand_child = GrandChild(13, 'Arslan Haider Sherazi', 3.42)
    roll_no = grand_child.get_roll_no()
    name = grand_child.get_name()
    cgpa = grand_child.get_cgpa()
    print(roll_no, name, cgpa)

