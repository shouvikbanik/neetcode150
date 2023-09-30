import re


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    regex = re.compile('[^a-zA-Z0-9]')
    string_val = regex.sub('', s)
    string_val = string_val.lower()
    i = 0
    j = len(string_val) - 1
    while i < j:
        if string_val[i] != string_val[j]:
            return False
        i += 1
        j -= 1
    return True
