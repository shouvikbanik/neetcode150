import math


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    first_index = 0
    last_index = len(nums) - 1
    while (first_index <= last_index):
        mid_index = int(math.floor((last_index + first_index) / 2))
        if nums[mid_index] == target:
            return mid_index
        elif target > nums[mid_index]:
            first_index = mid_index + 1
        else:
            last_index = mid_index - 1
    return -1
