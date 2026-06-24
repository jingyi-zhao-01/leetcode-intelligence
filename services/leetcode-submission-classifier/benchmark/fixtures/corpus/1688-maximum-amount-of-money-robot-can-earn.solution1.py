# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-amount-of-money-robot-can-earn
# source_path: LeetCode-Solutions-master/Python/maximum-amount-of-money-robot-can-earn.py
# solution_class: Solution
# submission_id: e08c0a35fa34b8e69c9c57c34965591014d58197
# seed: 1736923696

# Time:  O(m * n * k) = O(m * n)
# Space: O(min(m, n) * k) = O(min(m, n))

# dp

class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        K = 2
        mn = min(len(coins), len(coins[0]))
        mx = max(len(coins), len(coins[0]))
        get = (lambda i, j: coins[i][j]) if len(coins) == mx else (lambda i, j: coins[j][i])
        dp = [[float("-inf")]*(K+1) for _ in xrange(mn)] 
        for i in xrange(mx):
            new_dp = [[float("-inf")]*(K+1) for _ in xrange(mn)]
            for j in xrange(mn):
                for k in xrange(K+1):
                    if i == 0 and j == 0:
                        new_dp[j][k] = max(get(i, j), 0) if k-1 >= 0 else get(i, j)
                        continue
                    if i-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k]+get(i, j))
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k-1])
                    if j-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k]+get(i, j))
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k-1])
            dp = new_dp
        return dp[-1][-1]