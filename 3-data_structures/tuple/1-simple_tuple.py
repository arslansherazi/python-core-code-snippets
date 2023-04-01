"""
    Important Points::
    =>tuple is immutable object of class tuple
    =>tuple cannot be changed/updated once initialized
    =>Removing individual tuple elements is not possible but we can delete whole tuple
    =>tuple can contain int, float or str data types
"""
if __name__ == '__main__':
    # simple tuple
    student = (13, 'Arslan Haider Sherazi', 3.42)
    print(student)
    print(student[0])

    # selecting data from tuple
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(numbers[2:])  # 2 - last_index
    print(numbers[:])  # all indexes
    print(numbers[:5])  # 0 - 4 (indexes)
    print(numbers[3:7])  # 3 - 6 (indexes)
