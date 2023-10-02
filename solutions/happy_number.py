import math


def sum_of_squared_digits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit * digit
        n = int(math.floor(n / 10))
    return sum


def is_happy(n):
    """
    :type n: int
    :rtype: bool
    """
    checked_nums = set()
    while n != 0:
        if n in checked_nums:
            break
        else:
            checked_nums.add(n)
        sum = sum_of_squared_digits(n)
        if sum == 1:
            return True
        else:
            n = sum

    return False
