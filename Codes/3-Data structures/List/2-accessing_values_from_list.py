"""
    Important Points::
    =>index of list starts from 0
    =>last index of list = length(list)-1
"""
if __name__ == '__main__':
    # accessing values of list using index no
    student = ['Arslan Haider Sherazi', 3.42, 'SE']
    name = student[0]
    cgpa = student[1]
    degree = student[2]
    print(name, cgpa, degree)

    # accessing values of list using range
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    v1 = numbers[:5]  # 0 - 4 (indexes)
    print(v1)
    v2 = numbers[1:len(numbers)]  # 1 - last index
    print(v2)
    v3 = numbers = numbers[2:6]  # 2 - 5 (indexes)
    print(v3)
