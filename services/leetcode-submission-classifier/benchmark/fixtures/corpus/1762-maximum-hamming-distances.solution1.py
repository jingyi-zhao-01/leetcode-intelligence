# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-hamming-distances
# source_path: LeetCode-Solutions-master/Python/maximum-hamming-distances.py
# solution_class: Solution
# submission_id: d7c73c4986e68a62d8489dc485681ae8d843e10b
# seed: 956897461

# Time:  O(m * 2^m)
# Space: O(2^m)

# bitmasks, knapsack dp

class Solution(object):
    def maxHammingDistances(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: List[int]
        """
        dp = [float("-inf")]*(1<<m)
        for x in nums:
            dp[x] = 0
        for i in xrange(m):
            new_dp = dp[:]
            for mask in xrange(1<<m):
                new_dp[mask] = max(new_dp[mask], dp[mask^(1<<i)]+1)
            dp = new_dp
        return [dp[x] for x in nums]