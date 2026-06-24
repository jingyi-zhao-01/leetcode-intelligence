# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-ways-to-distribute-candies
# source_path: LeetCode-Solutions-master/Python/count-ways-to-distribute-candies.py
# solution_class: Solution
# submission_id: 682ee70709111b4082ff1b62ae9a76553d8f173b
# seed: 2543866613

# Time:  O(n * k)
# Space: O(k)

class Solution(object):
    def waysToDistribute(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [1]*k
        for i in xrange(1, n):
            for j in reversed(xrange(1, min(i, k))):
                dp[j] = ((j+1)*dp[j] + dp[j-1]) % MOD
        return dp[k-1]