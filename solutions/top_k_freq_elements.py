from collections import OrderedDict


def top_k_frequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq_dict = {}
    for num in nums:
        if num in freq_dict.keys():
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    freq_dict = OrderedDict(
        {key: value for key, value in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)})
    return_list = []
    for key, value in freq_dict.items():
        if k == 0:
            break
        else:
            k -= 1
            return_list.append(key)
    return return_list
