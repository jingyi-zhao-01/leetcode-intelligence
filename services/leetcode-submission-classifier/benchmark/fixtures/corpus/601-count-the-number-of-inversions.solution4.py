# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-inversions
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-inversions.py
# solution_class: Solution4
# submission_id: 7e62e732fde9cfdb87eab7e4373e2734b0543a0c
# seed: 362856971

# Time:  O(n * k), k = max(cnt for _, cnt in requirements)
# Space: O(n + k)

# knapsack dp, combinatorics, sliding window, two pointers

class Solution4(object):
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
            dp = [reduce(lambda total, k: (total+dp[j-k])%MOD, xrange(min(i+1, j+1)), 0) if lookup[i] == -1 or lookup[i] == j else 0 for j in xrange(len(dp))]
        return dp[-1]%MOD