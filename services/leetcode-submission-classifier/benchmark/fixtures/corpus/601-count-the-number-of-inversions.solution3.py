# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-inversions
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-inversions.py
# solution_class: Solution3
# submission_id: 413d1630908ebb44dd7562e1d2b8fc3e17508da9
# seed: 679465520

# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution3(object):
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
        dp = [0]*(lookup[-1]+1)
        dp[0] = 1
        for i in xrange(n):
            new_dp = [0]*len(dp)
            curr = 0
            for j in xrange(len(dp)):
                curr = (curr+dp[j])%MOD
                if j-(i+1) >= 0:
                    curr = (curr-dp[j-(i+1)])%MOD
                new_dp[j] = curr if lookup[i] == -1 or lookup[i] == j else 0
            dp = new_dp
        return dp[-1]