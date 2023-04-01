"""
    Important Points::
    =>tuple can also contain list, tuple, set or dict as an element
"""
if __name__ == '__main__':
    # dict as an element of tuple
    students = (
        {
            1: [13, 'Arslan Haider Sherazi', 3.42],
            2: (30, 'Danish Ali', 2.53),
        },  # comma should be included at the end if tuple has only one element
    )

    for key, student in students[0].items():
        print(key, end=" => ")
        print(student[0], student[1], student[2])

    # tuple and list as an element of tuple
    students = (
        [13, 'Arslan Haider Sherazi', 3.42],
        (30, 'Danish Ali', 2.53),
        (36, 'Babar Ali', 2.97),
        [26, 'Asher Butt', 3.01]
    )

    for student in students:
        for s in student:
            print(s, end=" ")
        print()
