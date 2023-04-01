if __name__ == '__main__':
    # tuple packing / assignment
    student = (13, 'Arslan Haider Sherazi', 'SE', 3.42)

    # tuple unpacking
    roll_no, name, degree, cgpa = student  # no of variables on left side must be equal to no of tuple values
    print(roll_no, name, degree, cgpa)

    roll_no, *args = student  # first value is assigned to roll_no while all other values are assigned to *args
    print(roll_no, *args)
    print(roll_no, args[0], args[1], args[2])
