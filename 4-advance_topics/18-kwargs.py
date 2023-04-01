import time


def printStudent(**kwargs):
    # keys and values are string type. We should change data type implicitly if required
    for key, value in kwargs.items():
        print(key+"::"+value)


if __name__ == '__main__':
    printStudent(name="Arslan Haider Sherazi", degree="Software Engineering", cgpa="3.42")
    time.sleep(10)