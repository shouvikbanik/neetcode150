def eval_rpn(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for element in tokens:
        if element.isdigit() or element[1:].isdigit():
            stack.append(int(element))
        elif element == '/':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(int(val2 / val1))
        elif element == '-':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 - val1)
        elif element == '+':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 + val1)
        elif element == '*':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 * val1)
    return stack[0]
