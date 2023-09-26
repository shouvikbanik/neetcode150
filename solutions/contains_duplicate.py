def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    is_present = False
    digit_set = set()
    for number in nums:
        if number in digit_set:
            is_present = True
            break
        else:
            digit_set.add(number)
    return is_present
