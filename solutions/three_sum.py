def three_sum(nums):
    nums = sorted(nums)
    solution_list = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                solution_list.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else:
                left += 1
    return solution_list
