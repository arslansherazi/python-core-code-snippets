if __name__ == '__main__':

    # list Comprehensions
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    list_comp = [n for n in list if n % 2 == 0]
    print("list-Comprehension::")
    print(list_comp)

    comp_list = [n**2 for n in range(1,10)]
    print(comp_list)

    # dictionary Comprehensions
    dict_comp = {var: var**2 for var in range(1, 10)}
    print("dictionary-Comprehension::")
    print(dict_comp)

    # set Comprehension
    list = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    set_comp = {var for var in list if var % 2 == 0}
    print("set Comprehensions::")
    print(set_comp)
