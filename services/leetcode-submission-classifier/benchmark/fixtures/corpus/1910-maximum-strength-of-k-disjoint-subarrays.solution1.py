# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-strength-of-k-disjoint-subarrays
# source_path: LeetCode-Solutions-master/Python/maximum-strength-of-k-disjoint-subarrays.py
# solution_class: Solution
# submission_id: 87df9ff8e9655e3969f6de15b705713469a6021f
# seed: 328934643

# Time:  O(k * n)
# Space: O(n)

# dp, greedy, kadane's algorithm

class Solution(object):
    def maximumStrength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0]*(len(nums)+1)
        for i in xrange(k):
            new_dp = [float("-inf")]*(len(nums)+1)
            for j in xrange(len(nums)):
                new_dp[j+1] = max(new_dp[j], dp[j])+nums[j]*(k-i)*(1 if i%2 == 0 else -1)
            dp = new_dp
        return max(dp)