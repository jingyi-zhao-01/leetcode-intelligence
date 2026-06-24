# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wiggle-sort
# source_path: LeetCode-Solutions-master/Python/wiggle-sort.py
# solution_class: Solution
# submission_id: 22bdd58cadaa2d7d4ff657bffd7eb316164e4def
# seed: 1377903131

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or \
                (not (i % 2) and nums[i - 1] < nums[i]):
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]