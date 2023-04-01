if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(numbers)

    # using del
    del numbers[2]  # deletes element present at index 2
    print(numbers)

    # using pop
    numbers.pop(0)  # deletes element at index 0 and returns the deleted element
    print(numbers)
