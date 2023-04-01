from collections import deque

if __name__ == '__main__':
    queue = deque([])

    # adding data into queue
    queue.append('Arslan')
    queue.append('Danish')
    queue.append('Asher')
    queue.append('Babar')
    print(queue)

    # retrieving data from queue (first-in first-out)
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())
    print(queue.popleft())
