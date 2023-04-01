if __name__ == '__main__':
    numbers = list()  # equivalent => numbers = [] but numbers = list() is recommended by PEP

    # adding data into list at the tail of list (append)
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    numbers.append(4)
    numbers.append(3)
    print(numbers)

    # count no of data elements in list
    print(len(numbers))

    # count no of appearances of a data item
    total_appearances = numbers.count(3)  # 3 = data item
    print(total_appearances)

    # find lowest index on which a data item appeared
    lowest_index = numbers.index(3)  # 3 = data item
    print(lowest_index)

    # updating list data
    numbers[3] = 44
    print(numbers)

    # insert data at specific index of list
    # value the is already present at the specified index moves one index forward
    numbers.insert(1, 22)  # 1 = index, 22 = data
    print(numbers)

    # delete data from list
    numbers.remove(3) # 3 = data (if list has multiple data items then all data items will be deleted)
    print(numbers)

    # sorting the list
    numbers.sort()
    print(numbers)

    # reversing the list
    numbers.reverse()
    print(numbers)

    # extending the list using sequence(list, dictionary, tuple, set)
    names = {
        'first_name': 'Arslan',
        'last_name': 'Haider'
    }
    numbers.extend(names.values())  # if we only pass dictionary object then by default keys will be extended
    print(numbers)

    # clear/empty list
    numbers.clear()
    print(numbers)