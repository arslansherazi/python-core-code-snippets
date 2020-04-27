if __name__ == '__main__':
    # for loop
    for i in range(5):  # i => 0-4
        print(i)

    for i in range(1, 5):  # i => 1-4
        print(i)

    for i in range(1, 10, 2): # i => 1,3,5,7,9(increment of 2)
        print(i)

    # for-each loop
    fruits = ['Apple', 'Banana', 'Mango', 'Peach', 'Orange']
    for fruit in fruits:
        print(fruit)

    # while loop
    i = 1
    while i <= 5:
        print(i)
        i = i + 1

    # nested for loop
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 9, 9 ,9]]
    no_of_rows = len(matrix)
    no_of_columns = len(matrix[0])
    for row in range(no_of_rows):
        for column in range(no_of_columns):
            print(matrix[row][column], end=' ')
        print('\n')