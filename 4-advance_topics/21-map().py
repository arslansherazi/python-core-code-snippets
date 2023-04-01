"""
    Important Points::
    =>The map() function executes a specified function for each item in an iterable.
    =>map() function returns a list of the results after applying the given function to each item of a given iterable
"""


def calculate_length(list_item):
    return len(list_item)


def concat_fruits(list1, list2):  # We can receive multiple iterables as parameters
    return list1 + list2


if __name__ == '__main__':
    # concat elements of two lists (element by element)
    fruits1 = ['Apple', 'Banana', 'PineApple']
    fruits2 = ['Orange', 'Lemon', 'Cherry']
    fruits = map(concat_fruits, fruits1, fruits2)  # fruits = map object
    for fruit in fruits:
        print(fruit)

    # calculate length of each item in iterable
    fruits_lengths = map(calculate_length, fruits1)
    print(tuple(fruits_lengths))

    # map() using lambda
    numbers = [1, 2, 3, 4, 5, 6, 7]
    results = map(lambda n: n + n, numbers)
    print(list(results))
