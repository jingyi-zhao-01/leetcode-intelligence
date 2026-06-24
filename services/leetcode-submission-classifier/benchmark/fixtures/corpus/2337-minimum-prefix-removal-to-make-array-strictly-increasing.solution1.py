# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-prefix-removal-to-make-array-strictly-increasing
# source_path: LeetCode-Solutions-master/Python/minimum-prefix-removal-to-make-array-strictly-increasing.py
# solution_class: Solution
# submission_id: 53690704369bea6036bbb626a9a8a8799dd3fb56
# seed: 2704433163

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return next((i+1 for i in reversed(xrange(len(nums)-1)) if not nums[i] < nums[i+1]), 0)