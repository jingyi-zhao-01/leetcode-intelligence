# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-inverse-pairs-array
# source_path: LeetCode-Solutions-master/Python/k-inverse-pairs-array.py
# solution_class: Solution2
# submission_id: 1a224a28943f079355f39820b0cdb7e9ef99d879
# seed: 3370046923

# Time:  O(n * k)
# Space: O(k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution2(object):
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
            for j in xrange(len(dp)):
                new_dp[j] = dp[j]
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]