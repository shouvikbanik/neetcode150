def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    max_int = 2 ** 31 - 1  # 2,147,483,647
    min_int = -2 ** 31  # -2,147,483,648
    reverse_val = 0
    negative_flag = False
    if x < 0:
        negative_flag = True
        x *= -1
    while x != 0:
        if reverse_val > max_int / 10 or reverse_val < min_int / 10:
            return 0
        else:
            digit = x % 10
            reverse_val = (10 * reverse_val) + digit
            x //= 10
    if negative_flag:
        return -1 * reverse_val
    else:
        return reverse_val
