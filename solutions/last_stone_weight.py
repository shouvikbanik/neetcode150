from heapq import heapify, heappop, heappush


def last_stone_weight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    stones = list(map(lambda num: num * -1, stones))
    heapify(stones)
    while len(stones) > 1:
        print(stones)
        stone1 = heappop(stones)
        stone2 = heappop(stones)
        heappush(stones, -1 * abs(stone1 - stone2))
    return stones[0] * -1
