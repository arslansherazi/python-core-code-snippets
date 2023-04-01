"""
    Important Points::
    =>set is an object of class set
    =>The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
    =>The elements in the set cannot be duplicates.
    =>set can contain int, float and str as elements
    =>There is no index attached to any element in a python set. So they do not support any indexing or slicing
    operation.
    =>We cannot access individual values in a set
    =>set is unordered. The order of elements that is defined by us will not be maintained by interpreter
"""
if __name__ == '__main__':
    # creating set using set() function
    days_of_week = set(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
    print(type(days_of_week))
    print(days_of_week)

    # creating set using curly braces
    months = {'Jan', 'Feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'oct', 'nov', 'dec'}
    print(type(months))
    print(months)

    # set having elements of different data types
    student_set = {13, 'Arslan Haider Sherazi', 3.42, 3.42}
    print(student_set)
