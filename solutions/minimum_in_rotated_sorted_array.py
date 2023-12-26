def find_min(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_ptr = 0
    right_ptr = len(nums) - 1
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if nums[mid] <= nums[(mid + 1) % len(nums)] and nums[mid] <= nums[(mid - 1) % len(nums)]:
            return nums[mid]
        elif nums[mid] < nums[right_ptr]:
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1
