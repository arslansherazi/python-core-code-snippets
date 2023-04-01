if __name__ == '__main__':
    stack = list()

    # adding data into stack
    stack.append('Arslan')
    stack.append('Danish')
    stack.append('Asher')
    stack.append('Babar')
    print(stack)

    # retrieving data from stack (first-in last-out)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())