# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-inverse-pairs-array
# source_path: LeetCode-Solutions-master/Python/k-inverse-pairs-array.py
# solution_class: Solution
# submission_id: 1a754e13901d9c691bc4a7eb8168f22393f4acaa
# seed: 2537821505

# Time:  O(n * k)
# Space: O(k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [1]
        for i in xrange(n):
            new_dp = [0]*min(len(dp)+((i+1)-1), k+1)
            for j in xrange(len(new_dp)):
                new_dp[j] = dp[j] if j < len(dp) else 0
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[k] if k < len(dp) else 0