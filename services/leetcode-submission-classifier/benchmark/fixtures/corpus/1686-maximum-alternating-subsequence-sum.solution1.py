# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-alternating-subsequence-sum
# source_path: LeetCode-Solutions-master/Python/maximum-alternating-subsequence-sum.py
# solution_class: Solution
# submission_id: 59419fa19c9ae306edc95e475494f13982cb3b7f
# seed: 763445346

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in xrange(len(nums)-1):
            result += max(nums[i+1]-nums[i], 0)
        return result