"""
    Important Points::
    =>Python descriptors are a way to create managed attributes. Managed attributes are used to protect an attribute
    from changes or to automatically update the values of a dependant attribute.
    =>In general, a descriptor is an object attribute with a binding behavior, one whose attribute access is overridden
    by methods in the descriptor protocol. Those methods are __get__, __set__, and __delete__. If any of these methods
    are defined for an object, it is said to be a descriptor.
    =>Descriptors are assigned to a class, not an instance.
    =>owner is the class where the descriptor was assigned as an attribute
"""


# class based descriptor
class Descriptor(object):
    def __init__(self):
        self.name = ''

    def __set__(self, instance, value):
        print('set is called')
        self.name = value

    def __get__(self, instance, owner):
        print('get is called')
        return self.name

    def __delete__(self, instance):
        print('del is called')
        del self.name


class Person(object):  # owner class
    name = Descriptor()


# Descriptor using decorators
class User:
    def __init__(self):
        self._username = ''

    @property
    def username(self):
        print('Getter is called')
        return self._username

    @username.setter
    def username(self, value):  # setter function name should be same as property function i.e username
        print('Setter is called')
        self._username = value

    @username.deleter
    def username(self):  # deleter function name should be same as property function i.e username
        print('Deleter is called')
        del self._username


# Descriptor using property function
class Student:
    def __init__(self):
        self._name = ''

    def get_name(self):
        print('Getter is called')
        return self._name

    def set_name(self, value):
        print('Setter is called')
        self._name = value

    def delete_name(self):
        print('Deleter is called')
        del self._name

    # properties
    name = property(get_name, set_name, delete_name)


if __name__ == '__main__':
    print('Person::')
    p = Person()
    p.name = 'Arslan Haider Sherazi'
    print(p.name)
    del p.name
    # print(obj.name)  # This line generates error because we deleted name attribute in Descriptor

    print('\nUser::')
    u = User()
    # username = getter/setter/deleter function not attribute/data_member
    u.username = 'arslanhaider95'
    print(u.username)
    del u.username
    # print(u.username) # This line generates error because we deleted _name attribute in Descriptor(User)


    print('\nStudent::')
    s = Student()
    # name = property not attribute/data_member
    s.name = 'Arslan Haider Sherazi'
    print(s.name)
    del s.name
    print(s.name)  # s.name returns nothing because we deleted _name attribute in Descriptor(Student)

