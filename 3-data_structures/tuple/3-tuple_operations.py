if __name__ == '__main__':
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    # checking length of tuple
    tuple_length = len(numbers)
    print(tuple_length)

    # concatenate two tuples
    tup1 = (1, 2, 3, 4)
    tup2 = ('Pakistan', 'Bangladesh', 'Nepal', 'Iran')
    tup = tup1 + tup2
    print(tup)

    # find min & max value from tuple (We can only find min max of tuple having elements of same data types)
    min_value = min(tup2)
    print(min_value)

    max_value = max(numbers)
    print(max_value)

    # iterating tuple
    for number in numbers:
        print(number, end=" ")

    print()  # used to move printing cursor on next line
    for value in tup:
        print(value, end=" ")

    # convert list into tuple
    print('\n')
    student = [13, 'Arslan Haider Sherazi', 3.42]
    print(student)
    student_tup = tuple(student)
    print(student_tup)
