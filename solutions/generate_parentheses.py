def generate_parentheses_helper(n, open_brackets, close_brackets, current_string, possible_combinations):
    if close_brackets == n:
        possible_combinations.append(current_string)
        return possible_combinations
    else:
        return_list = []
        if open_brackets < n:
            return_list.extend(generate_parentheses_helper(n, open_brackets + 1, close_brackets, current_string + '(',
                                                           possible_combinations))
        if open_brackets > close_brackets:
            return_list.extend(
                generate_parentheses_helper(n, open_brackets, close_brackets + 1, current_string + ')',
                                            possible_combinations))
        return return_list


def generate_parentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return set(generate_parentheses_helper(n, 0, 0, '', []))
