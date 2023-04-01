"""
    Important Points::
    =>locals() function in Python returns the dictionary of current local symbol table.
    =>Symbol Table:
      It is a data structure created by compiler for which is used to store all information needed to execute a program.
    =>Local Symbol Table:
      This symbol table stores all information which needed to local scope of the program and this information is
      accessed using python built in function locals().
    =>We cannot change values of local variables using locals

"""


def student():
    name = 'Arslan Haider'
    degree = 'SE'
    cgpa = 3.42
    roll_no = 'BSEF14A513'

    print(locals())

    print(locals()['name'])
    locals()['name'] = 'Arslan Haider Sherazi'  # update is not possible using locals()
    print(name)

    print(locals()['roll_no'])
    print(locals()['degree'])
    print(locals()['cgpa'])


if __name__ == '__main__':
    print(locals())
    student()