"""
    Important Points::
    =>constructor overloading is not supported in python but we can achieve this using **kwargs or *args in constructor
    =>we can also achieve constructor overloading using @classmethod decorator on member functions
    =>@classmethod decorator is used to create object of class using class reference cls
    =>class methods are bound to class instead of object/instance
"""


class Shape:
    area = 0.0
    width = 0.0
    height = 0.0
    depth = 0.0

    def __init__(self, **kwargs):
        if len(kwargs) == 1 and {'width'} == kwargs.keys():  # kwargs.keys() = kwargs
            self.width = kwargs['width']
        elif len(kwargs) == 2 and {'width', 'height'} == kwargs.keys():
            self.width = kwargs['width']
            self.height = kwargs['height']
        else:
            self.width = kwargs['width']
            self.height = kwargs['height']
            self.depth = kwargs['depth']

    @classmethod
    def square(cls, width):  # cls = class reference
        return cls(width=width)  # It calls the constructor

    @classmethod
    def rectangle(cls, width, height):
        return cls(width=width, height=height)

    @classmethod
    def cube(cls, width, height, depth):
        return cls(width=width, height=height, depth=depth)

    def calculate_square_area(self):
        self.area = self.width * self.width

    def calculate_rectangle_area(self):
        self.area = self.width * self.height

    def calculate_cube_area(self):
        self.area = self.width * self.height * self.depth

    def get_area(self):
        return self.area


if __name__ == '__main__':
    # constructor overloading using **kwargs
    square = Shape(width=20)
    square.calculate_square_area()
    square_area = square.get_area()
    print('Square Area::', square_area)

    rectangle = Shape(width=20, height=40)
    rectangle.calculate_rectangle_area()
    rectangle_area = rectangle.get_area()
    print('Rectangle Area::', rectangle_area)

    cube = Shape(width=10, height=20, depth=5)
    cube.calculate_cube_area()
    cube_area = cube.get_area()
    print('Cube Area::', cube_area)

    # constructor overloading using @classmethod decorator
    square = Shape.square(40)
    square.calculate_square_area()
    square_area = square.get_area()
    print('Square Area::', square_area)

    rectangle = Shape.rectangle(10, 20)
    rectangle.calculate_rectangle_area()
    rectangle_area = rectangle.get_area()
    print('Rectangle Area::', rectangle_area)

    cube = Shape.cube(10, 20, 50)
    cube.calculate_cube_area()
    cube_area = cube.get_area()
    print('Cube Area::', cube_area)
