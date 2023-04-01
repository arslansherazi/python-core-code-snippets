"""
    Important Points::
    => int, float, str and tuple are immutable objects and pass by value to the function
    => list, dict, and set are mutable objects and pass by reference to the function

"""


def func1():
    print('Arslan Haider Sherazi')


def func2(num1, num2):
    return num1 + num2


# pass by reference (list)
def func3(fruits):
    for index in range(len(fruits)):
        fruits[index] = 'Mango'


if __name__ == '__main__':
    func1()

    addition = func2(10, 10)
    print(addition)

    fruits = ['Mango', 'Banana', 'Apple', 'Orange', 'Grapes']
    print(fruits)
    func3(fruits)
    print(fruits)

