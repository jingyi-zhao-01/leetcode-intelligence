# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-inversions
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-inversions.py
# solution_class: Solution
# submission_id: 8c08b303e66f59b5b9ec25de03770600c65eba50
# seed: 3668967582

# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        lookup = [-1]*n
        for i, c in requirements:
            lookup[i] = c
        dp = [1]
        prev = 0
        for i in xrange(n):
            if lookup[i] != -1:  # optimized
                dp = [reduce(lambda total, i: (total+dp[i])%MOD, xrange(max((lookup[i]-i)-prev, 0), min((lookup[i]+1)-prev, len(dp))), 0)]
                prev = lookup[i]
                continue
            new_dp = [0]*min(len(dp)+((i+1)-1), (lookup[-1]+1)-prev)
            for j in xrange(len(new_dp)):
                new_dp[j] = dp[j] if j < len(dp) else 0
                if j-1 >= 0:
                    new_dp[j] = (new_dp[j]+new_dp[j-1])%MOD
                if j-(i+1) >= 0:
                    new_dp[j] = (new_dp[j]-dp[j-(i+1)])%MOD
            dp = new_dp
        return dp[-1]