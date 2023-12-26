def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left_ptr = 0
    right_ptr = len(nums) - 1
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if nums[mid] == target:
            return mid
        elif nums[left_ptr] <= nums[mid]:
            if nums[left_ptr] <= target <= nums[mid]:
                right_ptr = mid - 1
            else:
                left_ptr = mid + 1
        else:
            if nums[mid] <= target <= nums[right_ptr]:
                left_ptr = mid + 1
            else:
                right_ptr = mid - 1
    return -1
