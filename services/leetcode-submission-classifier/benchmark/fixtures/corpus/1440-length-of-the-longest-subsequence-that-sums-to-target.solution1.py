# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-the-longest-subsequence-that-sums-to-target
# source_path: LeetCode-Solutions-master/Python/length-of-the-longest-subsequence-that-sums-to-target.py
# solution_class: Solution
# submission_id: 3efee8b3a0b733a06c3baae048cf3c7830174649
# seed: 3086682387

# Time:  O(n * t)
# Space: O(t)

# knapsack dp

class Solution(object):
    def lengthOfLongestSubsequence(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [-1]*(target+1)
        dp[0] = 0
        for x in nums:
            for i in reversed(xrange(x, len(dp))):
                if dp[i-x] != -1:
                    dp[i] = max(dp[i], dp[i-x]+1)
        return dp[-1]