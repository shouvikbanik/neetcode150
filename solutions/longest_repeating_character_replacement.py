def character_replacement(s, k):
    """
    :type s: str AABABBA
    :type k: int 1
    :rtype: int 4
    """
    longest_length = 0
    char_dict = {s[0]: 1}
    left = 0
    right = 1
    length = len(s)
    while right != length:
        if s[right] not in char_dict.keys():
            char_dict[s[right]] = 1
        else:
            char_dict[s[right]] += 1
        highest_char_freq = max(char_dict.values())
        if (right - left + 1) - highest_char_freq <= k:
            longest_length = max(longest_length, right - left + 1)
        else:
            char_dict[s[left]] -= 1
            left += 1
        right += 1
    return longest_length
