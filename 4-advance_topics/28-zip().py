if __name__ == '__main__':
    names = ['Arslan Haider Sherazi', 'Danish Ali', 'Babar Ali', 'Asher Butt']
    roll_nos = ['BSEF14A513', 'BSEF14A530', 'BSEF14A536', 'BSEF14A526']
    cgpas = [3.42, 2.53, 2.93, 3.01]

    # zip
    mapped = zip(names, roll_nos, cgpas)
    student_records_lists = list(mapped)
    print(student_records_lists)

    # unzip
    names, roll_nos, cgpas = zip(*student_records_lists)
    print(names)
    print(roll_nos)
    print(cgpas)

    # iterating using zip
    for name, rol_no, cgpa in student_records_lists:
        print(name + '\t' + rol_no + '\t' + str(cgpa))
