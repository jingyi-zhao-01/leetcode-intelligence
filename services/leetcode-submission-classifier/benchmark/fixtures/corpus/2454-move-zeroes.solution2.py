# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: move-zeroes
# source_path: LeetCode-Solutions-master/Python/move-zeroes.py
# solution_class: Solution2
# submission_id: 376cef67efb8c6889adc11c64945b859caa7c746
# seed: 3302644273

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in xrange(pos, len(nums)):
            nums[i] = 0