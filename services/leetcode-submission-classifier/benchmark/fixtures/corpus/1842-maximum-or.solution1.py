# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-or
# source_path: LeetCode-Solutions-master/Python/maximum-or.py
# solution_class: Solution
# submission_id: 90b274f916cb941b94f07b4991420d4bbcc5ea21
# seed: 672831770

# Time:  O(n)
# Space: O(n)

# prefix sum, greedy

class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = [0]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            right[i] = right[i+1]|nums[i]
        result = left = 0
        for i in xrange(len(nums)):
            result = max(result, left|(nums[i]<<k)|right[i+1])
            left |= nums[i]
        return result