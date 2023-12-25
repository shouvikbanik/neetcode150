import math


def min_eating_speed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    left_ptr = 1
    right_ptr = max(piles)
    min_speed = right_ptr
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours > h:
            left_ptr = mid + 1
        else:
            min_speed=min(min_speed, mid)
            right_ptr = mid - 1

    return min_speed
