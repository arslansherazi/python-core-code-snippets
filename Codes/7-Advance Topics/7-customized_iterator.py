"""
    Important Points::
    => __iter__() and __next__() functions are called iterator protocol of an iterator
    => __next__() raises a StopIteration exception when there are no more value to return, which is implicitly captured
       by looping constructs to stop iterating.
"""


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.limit = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            self.current += 1
            return self.current-1


if __name__ == '__main__':
    for value in Counter(1, 10):
        print(value)