def missing_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum_total = 0
    max_val = -999999
    for num in nums:
        sum_total += num
        if num > max_val:
            max_val = num
    sum_actual = max_val * (max_val + 1) / 2
    if sum_actual - sum_total == 0:
        if 0 in nums:
            return max_val + 1
        else:
            return 0
    else:
        return sum_actual - sum_total
