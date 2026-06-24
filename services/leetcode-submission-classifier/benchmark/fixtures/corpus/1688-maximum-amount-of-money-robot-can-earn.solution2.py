# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-amount-of-money-robot-can-earn
# source_path: LeetCode-Solutions-master/Python/maximum-amount-of-money-robot-can-earn.py
# solution_class: Solution2
# submission_id: eb77ce72366cda42de89bf5f76e64efb7e25b81f
# seed: 327201617

# Time:  O(m * n * k) = O(m * n)
# Space: O(min(m, n) * k) = O(min(m, n))

# dp

class Solution2(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        K = 2
        dp = [[float("-inf")]*(K+1) for _ in xrange(len(coins[0]))] 
        for i in xrange(len(coins)):
            new_dp = [[float("-inf")]*(K+1) for _ in xrange(len(coins[0]))]
            for j in xrange(len(coins[0])):
                for k in xrange((K+1)):
                    if i == 0 and j == 0:
                        new_dp[j][k] = max(coins[i][j], 0) if k-1 >= 0 else coins[i][j]
                        continue
                    if i-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], dp[j][k]+coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k-1])
                    if j-1 >= 0:
                        new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k]+coins[i][j])
                        if k-1 >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k-1])
            dp = new_dp
        return dp[-1][-1]