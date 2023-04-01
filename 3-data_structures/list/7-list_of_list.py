if __name__ == '__main__':
    students = [
        [13, 'Arslan Haider Sherazi', 3.42],
        [30, 'Danish Ali', 2.53],
        [26, 'Asher Butt', 3.01],
        [36, 'Babar Ali', 2.93],
    ]

    print(students)
    print(students[0])
    print(students[0][1])  # Arslan Haider Sherazi

    for student in students:
        print(student[0], student[1], student[2])
