'''
    Important Notes:
    lambda is anonymous function which can accept multiple arguments but can only return single expression
'''

def multiplier(value):
    return lambda a : a * value


if __name__ == '__main__':
    addition = lambda value1, value2, value3 : value1 + value2 + value3
    print(addition(2,2,2))

    mul = multiplier(2)
    print(mul(4))  # 4 = argument of lambda expression
