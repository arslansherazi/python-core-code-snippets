"""
    Important Points::
    =>size of integer and float is unlimited
    =>integer can be positive or negative
    =>long and double data types are not available in python
    =>single character is also considered as string so char data type is also not present in python
    =>We can change type of variable by changing its value
    =>int, float and str are objects of int, float and str classes respectively
"""
if __name__ == '__main__':
    num_positive = 5  # integer(int)
    num_negative = -10  # integer(int)
    cgpa = 3.42  # float
    roll_no = 'BSEF14A513'  # string(str)
    character = 'A'

    print(type(num_positive))
    print(type(num_negative))
    print(type(roll_no))
    print(type(character))

    # Defining empty variables
    name = ''  # string
    roll_no = 0  # int
    cgpa = 0.0  # float

    print('\n')
    print(type(name))
    print(type(roll_no))
    print(type(cgpa))

    # changing type of variable by changing its value
    roll_no = 'BSEF14A513'
    print('\n')
    print(type(roll_no))
