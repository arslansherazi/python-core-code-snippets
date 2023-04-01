"""
    Important Points::
    => importlib library is used to import modules dynamically.
       For example::
       We want to import module on run time by using user input
"""
import importlib
import sys
import os

# adding project working directory into system paths because python searches modules first from built-in modules then
# from system paths
project_directory_path = os.getcwd()
if project_directory_path not in sys.path:
    sys.path.append(project_directory_path)


if __name__ == '__main__':
    for count in range(2):
        module_name = 'modules.module{module_no}'.format(module_no=count+1)
        importlib.import_module(module_name)
