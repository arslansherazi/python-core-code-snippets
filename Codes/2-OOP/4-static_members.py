"""
    Important Points::
    => data members which are declared outside __init__ or other member fucntions without using self are static data
       members
    => we can access static data members using class object as well. They behave like data members as well
    => static methods created using @classmethod are basically factory methods which are used to create objects
      using class reference which is their first parameter "cls" (see from constructor_overloading). They can be called
      by using class name and by using object of class as well. They cannot access the data members of class which are
      created using self. They can only access the static data members using class name or class reference "cls"
    => static methods created using @staticmethod are basically simple utility functions which means they are only used
       for simple processings and cant change the state of the class. They can be called using class name and by using
       object of class as well. They can only access the static data members of class using class name
    => if constructor or any other member function access static data member using self and changed its value then
       object of class will get its changed value but if we access it using class name then its initialized value will
       be accessed instead of changed value
    => noqa: 501 is used to remove warning for extra characters in line
"""


class Student:
    # static data members
    name = 'Arslan Haider Sherazi'
    age = 18
    cgpa = 3.42

    def __init__(self, roll_no):
        self.roll_no = roll_no  # data member

    # static methods
    @staticmethod
    def is_adult(age):
        if Student.age >= 18:
            return True
        return False

    @classmethod
    def get_cgpa(cls):  # cls = class reference
        return cls.name


if __name__ == '__main__':
    name = Student.name
    cgpa = Student.cgpa
    # roll_no = Student.roll_no  # it generates error because we cannot access data members created using self by using class reference # noqa:501
    print(name, cgpa)

    student = Student('BSEF14A513')
    roll_no = student.roll_no
    name = student.name
    cgpa = student.cgpa

    print(roll_no, name, cgpa)

    is_adult = Student.is_adult(24)
    if is_adult:
        print('Adult')
    else:
        print('Not Adult')

    cgpa = Student.get_cgpa()
    print(cgpa)

    # calling static member function using class object instead of class
    cgpa = student.get_cgpa()
    print(cgpa)