# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-array
# source_path: LeetCode-Solutions-master/Python/rotate-array.py
# solution_class: Solution4
# submission_id: 6acf9a8f71ffefc719240f591948944dc66014c6
# seed: 3131490025

# Time:  O(n)
# Space: O(1)

class Solution4(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]