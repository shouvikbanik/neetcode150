def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = 0
    sell = 1
    profit_max = 0
    while (sell < len(prices)):
        if prices[buy] < prices[sell]:
            profit_max = max(profit_max, prices[sell] - prices[buy])
        else:
            buy = sell
        sell += 1
    return profit_max
