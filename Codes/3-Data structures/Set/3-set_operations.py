if __name__ == '__main__':
    # creating empty set
    days = set()

    # adding element(s) into set
    days.add('mon')
    days.add('mon')  # set cannot contain duplicates. So this value will be discarded by set automatically
    days.add('tue')
    days.add('wed')
    days.add('thu')
    days.add('fri')
    print(days)

    # finding length of set
    length = len(days)
    print(length)

    # removing element(s) from set
    days.discard('mon')
    days.discard('thu')
    print(days)

    # union of two sets
    days1 = {'mon', 'tue', 'wed', 'fri'}
    days2 = {'thu', 'mon', 'tue', 'sat', 'sun'}
    days = days1 | days2
    print(days)

    # intersection of two sets
    days = days1 & days2
    print(days)

    # difference of two sets
    days = days1 - days2
    print(days)

    # compare sets
    days1 = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    days2 = set(['Mon', 'Tue', 'Wed'])
    is_super_set = days1 >= days2
    if is_super_set:
        print('Days1 is super set of Days2')

    is_sub_set = days2 <= days1
    if is_sub_set:
        print('Days2 is sub set of Days1')
