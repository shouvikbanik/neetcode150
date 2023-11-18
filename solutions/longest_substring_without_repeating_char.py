def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    char_dict = {}
    left = 0
    right = 0
    length = len(s)
    longest_length = 0
    while right < length:
        if s[right] in char_dict:
            loc = char_dict[s[right]]
            while left != loc + 1:
                char_dict.pop(s[left])
                left += 1
            char_dict[s[right]] = right
        else:
            char_dict[s[right]] = right
            longest_length = max(longest_length, len(char_dict))
        right += 1
    return longest_length
