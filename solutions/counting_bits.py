from hamming_weight import hamming_weight


def count_bits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    bit_count = []
    for num in range(n + 1):
        bit_count += [hamming_weight(num)]
    return bit_count
