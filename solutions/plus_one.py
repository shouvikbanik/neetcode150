def get_number_from_list(digits):
    num = 0
    for digit in digits:
        num = num * 10 + digit
    return num

def cast_list(test_list, data_type):
    return list(map(data_type, test_list))

def convert_to_list(num):
    return list(str(num))


def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    num = get_number_from_list(digits)
    num += 1
    return cast_list(convert_to_list(num),int)
