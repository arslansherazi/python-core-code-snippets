"""
    Important Points::
    => when we import a module then python searches it from builtin modules first then from system paths. If a path
    is not added into system paths and we import a module from that path then an error will be generated
"""
import os
import sys


if __name__ == '__main__':
    # get current working directory
    current_working_directory = os.getcwd()
    print(current_working_directory)

    # adding path into system paths (known to os)
    sys.path.append(current_working_directory)

    # list all system paths
    system_paths = sys.path
    print(system_paths)

    # remove a path from system paths
    sys.path.remove('/media/arslanhaidersherazi/Programming/python-core')
    print(sys.path)

    # remove/clear all system paths
    sys.path.clear()
    print(sys.path)

    # create new directory
    os.makedirs(name='main_directory/sub_directory')  # name = 'path of directory'

    # delete a directory
    os.rmdir('main_directory/sub_directory')  # it cannot remove directories directly which contains sub_directories/files   # noqa: 501

    # list directories within current directory
    directories = os.listdir()
    print(directories)

    # list directories within specified path
    directories = os.listdir(path='/media/arslanhaidersherazi/Programming/Programming')
    print(directories)

    # renaming a directory
    os.rename('main_directory', 'new_name_of_directory')  # if main_directory does not exist then new_name_of_directory
