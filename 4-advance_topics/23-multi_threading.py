import threading
import time
import os


def thread1_func(num):
    for n in range(num):
        time.sleep(1)
        print('Thread1: ' + str(n) + '\n')


def thread2_func(num):
    for n in range(num):
        time.sleep(1)
        print('Thread2: ' + str(n) + '\n')


if __name__ == '__main__':
    print('ProcessID::' + str(os.getpid()) + '\n')
    thread1 = threading.Thread(target=thread1_func, args=(10,))
    thread2 = threading.Thread(target=thread2_func, args=(10,))

    thread1.start()
    thread2.start()