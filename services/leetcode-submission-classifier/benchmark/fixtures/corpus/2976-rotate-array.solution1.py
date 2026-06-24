# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-array
# source_path: LeetCode-Solutions-master/Python/rotate-array.py
# solution_class: Solution
# submission_id: 4d0df838420d64121b11bf2822b030cce120868c
# seed: 3801864679

# Time:  O(n)
# Space: O(1)

class Solution(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, k):
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))