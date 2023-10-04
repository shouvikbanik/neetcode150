def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    xor_val = 0
    for num in nums:
        xor_val ^= num
    for num in nums:
        if num ^ xor_val == 0:
            return num
