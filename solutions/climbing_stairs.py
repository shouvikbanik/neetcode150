results={}
def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    results = {}
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in results.keys():
        return results[n]
    else:
        results[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
        return results[n]
