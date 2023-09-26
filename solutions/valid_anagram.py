def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    is_real_anagram=True
    letter_dictionary = {}
    for letter in s:
        if letter in letter_dictionary.keys():
            letter_dictionary[letter]+=1
        else:
            letter_dictionary[letter]=1
    for letter in t:
        if letter not in letter_dictionary.keys() or letter_dictionary[letter]==0:
            is_real_anagram=False
            break
        else:
            letter_dictionary[letter]-=1
    for key in letter_dictionary.keys():
        if letter_dictionary[key] != 0:
            is_real_anagram = False
    return is_real_anagram
