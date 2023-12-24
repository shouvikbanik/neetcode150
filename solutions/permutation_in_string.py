def check_inclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if len(s1) > len(s2):
        return False
    s1count, s2count = [0] * 26, [0] * 26
    for index in range(len(s1)):
        s1count[ord(s1[index]) - ord('a')] += 1
        s2count[ord(s2[index]) - ord('a')] += 1
    matches = 0
    for index in range(26):
        if s1count[index] == s2count[index]:
            matches += 1
    left_ptr = 0
    for right_ptr in range(len(s1), len(s2)):
        if matches == 26:
            return True
        index = ord(s2[right_ptr]) - ord('a')
        s2count[index] += 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] + 1 == s2count[index]:
            matches -= 1

        index = ord(s2[left_ptr]) - ord('a')
        s2count[index] -= 1
        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] - 1 == s2count[index]:
            matches -= 1
        left_ptr += 1
    return matches == 26
