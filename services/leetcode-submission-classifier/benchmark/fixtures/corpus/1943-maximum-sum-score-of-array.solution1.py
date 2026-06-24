# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-score-of-array
# source_path: LeetCode-Solutions-master/Python/maximum-sum-score-of-array.py
# solution_class: Solution
# submission_id: 4fd865bc7a6c8638cc94bf48b64adbb3167b02f4
# seed: 2442143338

# Time:  O(n)
# Space: O(1)

# prefix sum, math

class Solution(object):
    def maximumSumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = suffix = 0
        result = float("-inf")
        right = len(nums)-1
        for left in xrange(len(nums)):
            prefix += nums[left]
            suffix += nums[right]
            right -= 1
            result = max(result, prefix, suffix)
        return result