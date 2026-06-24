# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-an-array-is-consecutive
# source_path: LeetCode-Solutions-master/Python/check-if-an-array-is-consecutive.py
# solution_class: Solution
# submission_id: 6bb820b52b5864cb146c4336cf6d3b4537365552
# seed: 1119924109

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def isConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return max(nums)-min(nums)+1 == len(nums) == len(set(nums))