import time
import math


# class based decorator
class CalculateTimeDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, num):
        begin = time.time()
        result = self.function(num)
        end = time.time()
        print("Total time taken for ", self.function.__name__, "=>", end - begin)

        return result


# function based decorator
def calculate_time_decorator(func):
    def inner(num):
        begin = time.time()
        func(num)
        end = time.time()
        print("Total time taken for ", func.__name__, "=>", end-begin)

    return inner


@calculate_time_decorator
def factorial(num):
    time.sleep(2)
    fact = math.factorial(num)
    print("Factorial of " + str(num) + " = " + str(fact))


@CalculateTimeDecorator
def power(num):
    time.sleep(2)
    p = math.pow(num, 100)
    print(str(num) + "^100 = " + str(p))


if __name__ == "__main__":
    factorial(5)
    print('\n')
    power(2)
