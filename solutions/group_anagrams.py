def create_tuples_from_string(string):
    list_of_chars = [0] * 26
    for char in string:
        list_of_chars[ord(char) - 97] += 1
    return tuple(list_of_chars)


def group_anagrams(strs):
    list_of_tuples = []
    for string in strs:
        list_of_tuples.append(create_tuples_from_string(string))
    dict_of_tuples = {}
    for index in range(len(list_of_tuples)):
        if list_of_tuples[index] in dict_of_tuples.keys():
            dict_of_tuples[list_of_tuples[index]].append(strs[index])
        else:
            dict_of_tuples[list_of_tuples[index]] = [strs[index]]
    return list(dict_of_tuples.values())
