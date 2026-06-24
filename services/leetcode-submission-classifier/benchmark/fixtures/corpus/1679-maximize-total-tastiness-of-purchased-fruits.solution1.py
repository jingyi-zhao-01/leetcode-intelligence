# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-total-tastiness-of-purchased-fruits
# source_path: LeetCode-Solutions-master/Python/maximize-total-tastiness-of-purchased-fruits.py
# solution_class: Solution
# submission_id: 1ee4800bd5676bba0e3e5cc12113f47070c0758d
# seed: 2762696123

# Time:  O(n * a * c), n = len(price), a = maxAmount, c = maxCoupons
# Space: O(a * c)

import itertools


# dp

class Solution(object):
    def maxTastiness(self, price, tastiness, maxAmount, maxCoupons):
        """
        :type price: List[int]
        :type tastiness: List[int]
        :type maxAmount: int
        :type maxCoupons: int
        :rtype: int
        """
        dp = [[0]*(maxCoupons+1) for _ in xrange(maxAmount+1)]
        for p, t in itertools.izip(price, tastiness):
            for i in reversed(xrange(p//2, maxAmount+1)):
                for j in reversed(xrange(maxCoupons+1)):
                    if i-p >= 0:
                        dp[i][j] = max(dp[i][j], t+dp[i-p][j])
                    if j-1 >= 0:
                        dp[i][j] = max(dp[i][j], t+dp[i-p//2][j-1])
        return dp[maxAmount][maxCoupons]