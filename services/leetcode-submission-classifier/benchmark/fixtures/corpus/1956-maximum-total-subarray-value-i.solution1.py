# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-total-subarray-value-i
# source_path: LeetCode-Solutions-master/Python/maximum-total-subarray-value-i.py
# solution_class: Solution
# submission_id: c217e174c07a2afa6212a4e7784251f2fcdcfc47
# seed: 1567161975

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return k*(max(nums)-min(nums))