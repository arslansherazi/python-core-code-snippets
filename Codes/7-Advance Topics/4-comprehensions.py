if __name__ == '__main__':

    # List Comprehensions
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    list_comp = [n for n in list if n % 2 == 0]
    print("List-Comprehension::")
    print(list_comp)

    comp_list = [n**2 for n in range(1,10)]
    print(comp_list)

    # Dictionary Comprehensions
    dict_comp = {var: var**2 for var in range(1, 10)}
    print("Dictionary-Comprehension::")
    print(dict_comp)

    # Set Comprehension
    list = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
    set_comp = {var for var in list if var % 2 == 0}
    print("Set Comprehensions::")
    print(set_comp)
