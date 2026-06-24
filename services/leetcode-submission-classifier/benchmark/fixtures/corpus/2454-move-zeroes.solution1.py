# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: move-zeroes
# source_path: LeetCode-Solutions-master/Python/move-zeroes.py
# solution_class: Solution
# submission_id: bb3c0b8bb3f064634ca7650af9396e81385896ba
# seed: 1834200116

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(cmp=lambda a, b: 0 if b else -1)