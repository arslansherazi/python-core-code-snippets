import time


def printNames(*args):
    for name in args:
        print(name)


if __name__ == '__main__':
    printNames('Arslan', 'Haider', 'Sherazi', 24, 'Waqar', 'Haider', 'Sherazi', 29)
    time.sleep(10)