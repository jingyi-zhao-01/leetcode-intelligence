# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: wiggle-sort
# source_path: LeetCode-Solutions-master/Python/wiggle-sort.py
# solution_class: Solution2
# submission_id: 4a2e3f7ba39a2f485fde97533b9ed7e5acdc014f
# seed: 153697646

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        med = (len(nums) - 1) // 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]