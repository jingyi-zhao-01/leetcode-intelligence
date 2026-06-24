# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-equal-subset-sum
# source_path: LeetCode-Solutions-master/Python/partition-equal-subset-sum.py
# solution_class: Solution
# submission_id: 4e6db3cf1a1150b3df33373e74c20d8256250730
# seed: 3530951677

# Time:  O(n * s), s is the sum of nums
# Space: O(s)

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False

        dp = [False] * (s/2 + 1)
        dp[0] = True
        for num in nums:
            for i in reversed(xrange(1, len(dp))):
                if num <= i:
                    dp[i] = dp[i] or dp[i - num]
        return dp[-1]