# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: coin-change-2
# source_path: LeetCode-Solutions-master/Python/coin-change-2.py
# solution_class: Solution
# submission_id: 18a8ce4ec2b3e8e8ed224c12fcddeb276575dc3a
# seed: 146245806

# Time:  O(n * m)
# Space: O(m)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in xrange(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]