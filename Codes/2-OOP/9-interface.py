"""
    Important Points::
    => python-interface library should be installed (pip install python-interface)
    => classes that have implemented interface should override all of its methods
    => if a class implements more than one interfaces then it should overrides methods of all implemented interfaces
    => interface can only contain abstract member functions
"""

from interface import Interface, implements


# interfaces
class Animal(Interface):
    def eat(self): pass
    def travel(self): pass


class SavingCapacity(Interface):
    def save(self): pass


# classes
class Camel(implements(Animal, SavingCapacity)):
    def eat(self):
        print('Camel eats leaves')

    def travel(self):
        print('Camel can travel')

    def save(self):
        print('Camel can save water in his stomach')


class Buffalo(implements(Animal)):
    def eat(self):
        print('Buffalo eats grass')

    def travel(self):
        print('Buffalo cannot travel')


if __name__ == '__main__':
    camel = Camel()
    camel.eat()
    camel.travel()
    camel.save()

    buffalo = Buffalo()
    buffalo.eat()
    buffalo.travel()
