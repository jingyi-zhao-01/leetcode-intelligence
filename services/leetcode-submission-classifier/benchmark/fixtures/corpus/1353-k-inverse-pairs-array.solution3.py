# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-inverse-pairs-array
# source_path: LeetCode-Solutions-master/Python/k-inverse-pairs-array.py
# solution_class: Solution3
# submission_id: 6f1b2e50ecca56939a0670f14a5c336163baf28f
# seed: 3408303072

# Time:  O(n * k)
# Space: O(k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution3(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(k+1)
        dp[0] = 1
        for i in xrange(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in xrange(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr
            dp = new_dp
        return dp[-1]