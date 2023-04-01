"""
    Important Points::
    =>If the body of a def contains yield, the function automatically becomes a generator function
    =>yield saves the current state of function and then returns the value

"""


def names_generator(*args):
    for n in args:
        yield n


def square_generator(limit):
    for n in range(1,limit+1):
        yield n**2


if __name__ == "__main__":
    for name in names_generator("Arslan", "Haider", "Sherazi", "Waqar", "Haider", "Sherazi"):
        print(name)

    print("\nPrime Numbers::")
    for prime_number in square_generator(20):
        print(prime_number)