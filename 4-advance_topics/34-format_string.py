"""
    Important Points::
    => f-prefix method of formatting strings is more powerful than rest methods of string formatting
    => %s is used for strings and objects(list, dict, set ect) while %d is used for numbers in % formatting.
"""
if __name__ == '__main__':
    # % formatting
    name = 'Arslan Haider Sherazi'
    age = 25
    gpas = [3.34, 3.18, 3.17, 3.45, 3.38, 3.65, 3.65, 3.75]
    student = 'name:: %s\nage:: %d\ngpas:: %s' % (name, age, gpas)
    print(student)

    # format()
    student = '{roll_no}  {name} :: {degree} :: {cgpa} => {university}'.format(
        roll_no='BSEF14A513',
        name='Arslan Haider Sherazi',
        degree='Software Engineering',
        cgpa=3.42,
        university='Punjab University College of Information Technology, Lahore'
    )
    print(student)

    # f-prefix
    roll_no = 'BSEF14A513'
    name = 'Arslan Haider Sherazi'
    degree = 'Software Engineering'
    cgpa = 3.42
    university = 'Punjab University College of Information Technology, Lahore'
    student = f'{roll_no}  {name} :: {degree} :: {cgpa} => {university}'
    print(student)
