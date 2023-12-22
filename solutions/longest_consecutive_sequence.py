def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_set = set(nums)
    max_consecutive_len = 0
    for element in nums:
        sequence_len = 0
        number = element
        if number-1 not in num_set:
            while number in num_set:
                sequence_len += 1
                number += 1
        max_consecutive_len = max(max_consecutive_len, sequence_len)
    return max_consecutive_len
