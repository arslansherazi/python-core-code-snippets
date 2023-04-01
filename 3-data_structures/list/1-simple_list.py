"""
    Important Points::
    => list is mutable object of class list
"""
if __name__ == '__main__':
    # lists having data of same types
    roll_nos_list = [13, 30, 26, 36]
    names_list = ['Arslan Haider Sherazi', 'Danish Ali', 'Asher Butt', 'Babar Ali']
    cgpas_list = [3.42, 2.53, 3.01, 2.93]

    for roll_no, name, cgpa in zip(roll_nos_list, names_list, cgpas_list):
        print(roll_no, name, cgpa)

    # lists having data of different types
    student = [13, 'Arslan Haider Sherazi', 3.42]
    for info in student:
        print(type(info), end="")  # end is used to print content on same line
        print(info, end=" ")
