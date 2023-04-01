if __name__ == '__main__':
    student = {
        'roll_no': 13,
        'name': 'Arslan Haider Sherazi',
        'degree': 'SE',
        'cgpa': 3.42
    }

    print('Keys => ', end=" ")
    for key in student.keys():  # Equivalent => for key in student:
        print(key, end=" ")

    print('\nValues => ', end=" ")
    for value in student.values():
        print(value, end=" ")

    print('\n\nKey => Value')
    for key, value in student.items():
        print(key + ':' +str(value))
