if __name__ == '__main__':
    fruits = ['apple', 'banana', 'orange', 'mango']

    for fruit in enumerate(fruits):
        print(fruit, end=" ")

    print()
    for index, fruit in enumerate(fruits):
        print(index, fruit, end=" ")

    print()
    for index, fruit in enumerate(fruits, 100):
        print(index, fruit, end=" ")