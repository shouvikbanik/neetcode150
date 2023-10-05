def min_cost_climbing_stairs(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    len_cost = len(cost)
    min_cost_dict = {}
    return min(min_cost_climbing_stairs_helper(cost, 0, len_cost, min_cost_dict),
               min_cost_climbing_stairs_helper(cost, 1, len_cost, min_cost_dict))


def min_cost_climbing_stairs_helper(cost, index, length, min_cost_dict):
    if index == length - 1:
        return cost[index]
    elif index == length - 2:
        return cost[index]
    elif index in min_cost_dict.keys():
        return min_cost_dict[index]
    else:
        min_cost = min(cost[index] + min_cost_climbing_stairs_helper(cost, index + 1, length, min_cost_dict),
                       cost[index] + min_cost_climbing_stairs_helper(cost, index + 2, length, min_cost_dict))
        min_cost_dict[index] = min_cost
        return min_cost
