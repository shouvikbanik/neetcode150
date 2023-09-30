def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    brackets_stack = []
    for bracket in s:
        if bracket in ['{', '[', '(']:
            brackets_stack.append(bracket)
        elif len(brackets_stack) != 0:
            last_bracket = brackets_stack.pop()
            if bracket == '}' and last_bracket != '{':
                return False
            elif bracket == ')' and last_bracket != '(':
                return False
            elif bracket == ']' and last_bracket != '[':
                return False
        else:
            return False
    if len(brackets_stack) == 0:
        return True
    else:
        return False
