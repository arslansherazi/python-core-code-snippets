"""
    important Points::
    =>LRU (least recently used) is and algorithm for replacement of data in cache memory
    =>If function is periodically called with the same arguments then its result will be cached for future use
"""
from functools import lru_cache
import time


@lru_cache(maxsize=35)  # maxsize is used to specify how many recent values to cache
def generate_fibonacci_series(limit):
    if limit < 2:
        return limit
    return generate_fibonacci_series(limit-1) + generate_fibonacci_series(limit-2)


def clear_cache(func):
    func.cache_clear()


if __name__ == '__main__':
    # clear_cache(generate_fibonacci_series)
    start_time = time.time()
    limit = input('Enter limit::')
    fibonacci_series = [generate_fibonacci_series(n) for n in range(int(limit))]
    print(fibonacci_series)
    end_time = time.time()
    print('Processing time::', end_time - start_time)
