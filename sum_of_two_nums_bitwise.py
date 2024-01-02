def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    mask = 0xffffffff
    while (b & mask) != 0:
        carry = (a & b) << 1
        sum_of_bits = (a ^ b)
        a = sum_of_bits
        b = carry
    return (a & mask) if b > 0 else a
