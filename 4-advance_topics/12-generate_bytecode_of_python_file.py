"""
    Important Points::
    => By default compiled file is saved in __pycache_ folder in the same directory where .py file exists
"""


import py_compile


if __name__ == '__main__':
    py_compile.compile('args.py')
    py_compile.compile('kwargs.py', cfile='kwargs-compiled-file.pyc')  # cfile='path_of_compiled_file/name_of_compiled_file
