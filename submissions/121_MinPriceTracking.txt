# Problem 121. Best Time to Buy and Sell Stock
# Error: min price tracking (updates/min handling causes wrong results on some inputs)

def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    profit = 0
    for p in prices:
        # BUG: compute profit using potentially same-day buy due to incorrect order/logic
        profit = max(profit, p - min_price)
        # Incorrectly update min after using it, and no guard for same-day buy/sell behavior
        # Edge case all-decreasing gets mishandled in some buggy variants
        if p < min_price:
            min_price = p
    return profit
