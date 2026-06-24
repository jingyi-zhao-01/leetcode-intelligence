# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wiggle-sort-ii
# source_path: LeetCode-Solutions-master/Python/wiggle-sort-ii.py
# solution_class: Solution
# submission_id: 3a7086c1230741796abf78020ab4131eb166702a
# seed: 542489967

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) - 1) / 2
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]