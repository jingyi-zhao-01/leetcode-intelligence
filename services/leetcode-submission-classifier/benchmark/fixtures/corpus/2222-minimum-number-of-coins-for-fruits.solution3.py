# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-coins-for-fruits
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-coins-for-fruits.py
# solution_class: Solution3
# submission_id: 67d39c9625084c068f8f4ad6065b998372de207e
# seed: 3352896483

# Time:  O(n)
# Space: O(n)

import collections


# dp, mono deque

class Solution3(object):
    def minimumCoins(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [float("inf")]*(len(prices)+1)
        dp[0] = 0
        for i in xrange(len(prices)):
            for j in xrange(i//2, i+1):
                dp[i+1] = min(dp[i+1], dp[j]+prices[j])
        return dp[-1]