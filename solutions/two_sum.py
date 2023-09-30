def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # dict_nums stores the numbers as keys and location of list as values
    dict_nums = {}
    for i in range(len(nums)):
        pair_number = target - nums[i]
        if pair_number in dict_nums.keys():
            return {i, dict_nums[pair_number]}
        else:
            dict_nums[nums[i]] = i
