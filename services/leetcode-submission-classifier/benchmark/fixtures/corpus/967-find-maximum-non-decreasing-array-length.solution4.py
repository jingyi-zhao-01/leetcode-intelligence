# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-maximum-non-decreasing-array-length
# source_path: LeetCode-Solutions-master/Python/find-maximum-non-decreasing-array-length.py
# solution_class: Solution4
# submission_id: ef95639e729770795f028bd41f8ece8e09a84e69
# seed: 2013836097

# Time:  O(n)
# Space: O(n)

# dp, greedy, prefix sum, mono stack, two pointers

class Solution4(object):
    def findMaximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        dp = [float("inf")]*(len(nums)+1)
        dp[0] = 0
        prev = [-1]*(len(nums)+1)
        left = -1
        for right in xrange(len(nums)):
            left = max(left, prev[right])
            dp[right+1] = dp[left+1]+1
            next_right = bisect.bisect_left(prefix, prefix[right+1]+(prefix[right+1]-prefix[left+1]))-1
            prev[next_right] = right
        return dp[-1]