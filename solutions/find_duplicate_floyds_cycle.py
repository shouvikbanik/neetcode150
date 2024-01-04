def find_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow_ptr = 0
    fast_ptr = 0
    while True:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[nums[fast_ptr]]
        if slow_ptr == fast_ptr:
            break
    new_slow_ptr = 0
    first_intersection = fast_ptr
    while True:
        new_slow_ptr = nums[new_slow_ptr]
        first_intersection = nums[first_intersection]
        if new_slow_ptr == first_intersection:
            break
    return new_slow_ptr
