"""
    Important points::
    => Any returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of
       as a sequence of OR operations on the provided iterables. It short circuit the execution i.e. stop the execution
       as soon as the result is known.
       Syntax : any(list of iterables)
    => All returns true if all of the items are True (or if the iterable is empty). All can be thought of as a sequence of
       AND operations on the provided iterables. It also short circuit the execution i.e. stop the execution as soon as
       the result is known.
       Syntax : all(list of iterables)
"""

if __name__ == '__main__':
    num = input('Enter number::')
    num = int(num)

    data = [20, 20, 30, 40, 50]
    conditions = [20 in data, 30 in data, 70 in data]

    # in
    if num in data:  # returns true if number exists in data list at least once (True for this case)
        print(True)
    else:
        print(False)

    # any
    if any([]):  # False
        print(True)
    else:
        print(False)

    if any([True, True, False]):  # True
        print(True)
    else:
        print(False)

    if any(conditions):  # True
        print(True)
    else:
        print(False)

    # all
    if all([]):  # True
        print(True)
    else:
        print(False)

    if all([True, True, True]):  # True
        print(True)
    else:
        print(False)

    if all(conditions):  # False
        print(True)
    else:
        print(False)
