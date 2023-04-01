"""
    Important Points::
    =>The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the
    list elements mentioned in the sequence passed along.
    =>Steps:
    * At first step, first two elements of sequence are picked and the result is obtained.
    * Next step is to apply the same function to the previously attained result and the number just succeeding
      the second element and the result is again stored.
    * This process continues till no more elements are left in the container.
    * The final returned result is returned and printed on console.
    =>reduce() stores the intermediate result and only returns the final resultant value. Whereas, accumulate()
    returns a list containing the intermediate results. The last number of the list returned is final resultant
    value of the list.
"""
import functools
import itertools
import operator


def calculate_sum(n1, n2):
    return n1+n2


if __name__ == '__main__':
    numbers = [1, 4, 6, 22, 34, 7, 45, 9, 10]

    # calculate sum using reduce()
    sum_numbers = functools.reduce(calculate_sum, numbers)
    print(sum_numbers)

    # reduce() using lambda (calculate maximum number)
    maximum_number = functools.reduce(lambda a, b: a if a > b else b, numbers)
    print(maximum_number)

    # reduce() using operator (concate list elements as single string)
    full_name = functools.reduce(operator.add, ['Arslan ', 'Haider ', 'Sherazi'])
    print(full_name)

    # calculate sum using accumulate()
    sum_numbers_acc = itertools.accumulate(numbers, calculate_sum)  # sum_numbers_acc = accumulate object
    sum_numbers_list = list(sum_numbers_acc)
    print(sum_numbers_list)
    sum_numbers = sum_numbers_list[len(sum_numbers_list)-1]  # last index contains the sum of numbers
    print(sum_numbers)
