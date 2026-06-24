# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: search-insert-position
# source_path: LeetCode-Solutions-master/Python/search-insert-position.py
# solution_class: Solution
# submission_id: d3f21a44aabbb2c8cac17c8b3223eba4a784e1b7
# seed: 3059070742

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left