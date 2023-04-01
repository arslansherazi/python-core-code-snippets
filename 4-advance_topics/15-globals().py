"""
    Important Points::
    =>globals() function in Python returns the dictionary of current global symbol table.
    =>Symbol Table:
      Symbol table is a data structure which contains all necessary information about the program.
      These include variable names, methods, classes, etc.
    =>Global symbol table:
      It stores all information related to the global scope of the program, and is accessed in Python using
      globals() method.The functions, variables which are not associated with any class or function
      are stored in global scope.
    =>main function has global context. We can access global functions and varibales in main function without using
      globals()
      Example(in the following program)::
      globals()['degree'] = 'SE'    is equivalent to    degree = 'SE'
"""
# Global variables
name = 'Arslan Haider'
roll_no = 'BSEF14A513'
degree = ''
cgpa = 0.0


# Global Function
def func():
    name = 'AHS'  # local variable
    print(name)  # AHS
    print(globals()['name'])  # Arslan Haider Sherazi
    print(name)  # AHS


if __name__ == '__main__':
    func()

    print(globals()['name'])  # Arslan Haider
    globals()['name'] = 'Arslan Haider Sherazi'
    print(name)  # Arslan Haider Sherazi
    degree = 'SE'
    globals()['cgpa'] = 3.42
    print(globals()['degree'])
    print(cgpa)

    # calling global function func() using globals()
    globals()['func']()