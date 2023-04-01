"""
    Important Points::
    =>Following operators are used in python
    >       greater than
    <       less than
    >=      greater than or equal to
    <=      less than or equal to
    !=      not equal to
    <>      not equal to
    and     and
    or      or
    not     not a value

    =>switch structure is not available in python
"""


if __name__ == '__main__':
    # simple if-else structure
    num1 = input('Enter number1::')
    num2 = input('Enter number2::')
    if int(num1) > int(num2):
        print(num1)
    else:
        print(num2)

    # if-else-if structure
    marks = input('\nEnter marks::')
    marks = int(marks)
    if marks > 100 or marks < 0:
        print('Marks are incorrect. Enter valid marks')
    elif marks >= 85:
        print('A')
    elif marks >= 80:
        print('A-')
    elif marks >= 75:
        print('B+')
    elif marks >= 70:
        print('B')
    elif marks >= 65:
        print('B-')
    elif marks >= 60:
        print('C+')
    elif marks >= 55:
        print('C-')
    elif marks >= 50:
        print('D')
    else:
        print('F')

    temperature = None  # temperature = 20 (for else condition)
    if not temperature:
        print('\ntemperature is empty')
    else:
        print('\nTemperature::', temperature, 'degree celcius')