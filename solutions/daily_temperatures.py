def daily_temperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    number_of_days = [0] * len(temperatures)
    stack_of_temp = []
    for index in range(len(temperatures)):
        value_index_tuple = (temperatures[index], index)
        if len(stack_of_temp) == 0 or (index > 0 and temperatures[index] <= temperatures[index - 1]):
            stack_of_temp.append(value_index_tuple)
        else:
            while len(stack_of_temp) != 0 and stack_of_temp[len(stack_of_temp) - 1][0] < temperatures[index]:
                number_of_days[stack_of_temp[len(stack_of_temp) - 1][1]] = index - \
                                                                           stack_of_temp[len(stack_of_temp) - 1][1]
                stack_of_temp.pop()
            stack_of_temp.append(value_index_tuple)
    return number_of_days
