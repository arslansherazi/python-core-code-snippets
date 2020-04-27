"""
    Important Points::
    => We cannot add mutable objects (list, dict, set) as elements into set but we can add elements of immutable objects
       into set
    => We can add immutable objects (tuple) as elements into set
    => update() only adds the elements of sequences(list, dict, tuple, set) into set
"""
if __name__ == '__main__':
    # adding list element into set
    numbers_list = [5, 6, 7, 8, 9, 10]
    numbers_set = set([1, 2, 3, 4])

    numbers_set.update(numbers_list)
    print(numbers_set)

    # adding dict elements(keys, values, key:value pairs) into set
    names_dict = {1: 'Arslan', 2: 'Haider', 3: 'Sherazi'}
    names_set = set(['Waqar', 'Haider', 'Sherazi'])

    names_set.update(names_dict.items())  # adding key:value pairs
    print(names_set)
    names_set.update(names_dict)  # adding keys
    print(names_set)
    names_set.update(names_dict.values())  # adding values
    print(names_set)

    # adding set's elements into set
    numbers = {1, 2, 2, 3, 4, 5, 6, 7, 8}
    numbers_set = set()

    numbers_set.update(numbers)
    print(numbers_set)

    # adding tuples as elements of set
    tup1 = (1, 2, 2, 3)
    tup2 = (4, 4, 5, 6, 7, 8)
    tup3 = (4, 4, 5, 6, 7, 8)  # it will be discarded because of duplication
    numbers_set = set([tup1, tup2, tup3])
    print(numbers_set)

    for tup in numbers_set:
        print(tup)
        for ele in tup:
            print(ele, end=" ")
        print()
