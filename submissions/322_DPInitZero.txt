# Problem 322. Coin Change
# Error: dp initialization to 0 instead of inf -> invalid minima

def coinChange(coins, amount):
    dp = [0] * (amount + 1)  # BUG: should be inf for unreachable
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a - c] + 1) if dp[a] else (dp[a - c] + 1)
    return dp[amount] if dp[amount] else -1
