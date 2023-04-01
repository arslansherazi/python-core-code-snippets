"""
    Important Points::
    => we cannot instantiate abstract base class
    => child classes of abstract base class should override all of its abstract functions otherwise they are considered
       abstract classes and will not be instantiated
"""

from abc import ABC, abstractmethod  # ABC = abstract base class


# abstract base class
class Shape(ABC):
    # normal data members
    width = 0.0
    height = 0.0

    # abstract member functions
    @abstractmethod
    def get_width(self):
        return self.width

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def area(self):
        pass

    # normal member function
    def display(self):
        print('Member function in abstract base class')
        print('Width::', self.width, 'Height::', self.height)


# child classes of abstract base class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # implementation of abstract functions
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, width):
        self.width = width
        self.height = width

    # implementation of abstract functions
    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    # rectangle
    print('####Rectangle####')
    rectangle = Rectangle(5, 10)
    rectangle.display()
    area = rectangle.area()
    print('Area', area)

    # square
    print('\n####Square####')
    square = Square(10)
    square.display()
    area = square.area()
    print('Area', area)


