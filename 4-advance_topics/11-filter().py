"""
    Important Points::
    =>The filter() method filters the given sequence with the help of a function that tests each element in the
    sequence to be true or not.
    =>filter() returns an iterator that is already filtered.

"""


def filter_vowels(element):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if element in vowels:
        return True
    return False


if __name__ == '__main__':
    # filter list as vowel containing list
    characters_list = ['a', 'e', 'h', 'r', 'y', 'p', 'g', 'h', 'p', 'i', 'r', 'o', 't', 'o', 'l', 'e', 'u', 'u', 'i']
    vowels_filtered_list = filter(filter_vowels, characters_list)  # vowels_filtered_list = filter object
    print(list(vowels_filtered_list))

    # filter() using lambda expression
    numbers = [2, 4, 3, 5, 7, 8, 9, 10, 12, 4, 5, 7, 9, 12, 90]
    even_numbers = filter(lambda num: num % 2 == 0, numbers)
    odd_numbers = filter(lambda num: num % 2 != 0, numbers)
    print(tuple(even_numbers))
    print(tuple(odd_numbers))
